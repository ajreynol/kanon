#!/usr/bin/env python3
"""Stathmos's ecosystem status audit, run through scripts/eo_status_audit.

No assistant and no prompting -- this is a local command that reads trees and
reports. It is the thing to run when the question is *where does everything
stand*; `--all --verbose` is what to read when the question needs somebody to
read across the answer and form a view.

    scripts/eo_status_audit            # the table
    scripts/eo_status_audit --verbose  # and why each policy verdict came out
    scripts/eo_status_audit --check    # is the inventory itself still true?
    scripts/eo_status_audit --check --online   # ... and ask each remote

Health here means **what can be established from a checkout in about a second**:
does it declare membership, does the policy check pass, is there a channel to
reach them, how long since anything moved. It deliberately does not build,
test, or read anybody's source. A row that says `ok` is a claim about form, and
a quiet row is not evidence that a tool is well -- the same caution the analyzer
carries about its own silence applies here.

Membership is a decision rather than a measurement, so the `status` column comes
from `scripts/ecosystem/ecosystem.json` and is never inferred. Where the measurement and the
recorded status disagree, the row says so; changing the file is a person's job.
Child rows follow the parent's choice in the child's local README, defaulting
to advertised when the README has no declaration.
`--all-children` includes every recorded child and explains its listing state.

`--check` is the same principle with an exit code, and it is what CI runs. Two
questions, and the second is why it exists:

**Is the inventory well formed?** Offline, and always: every entry has the fields
its status requires, every parent named by a child exists, and every repository
the board addresses has a row here. Similar names can identify distinct tools.

**Is it still true?** With `--online`, each entry that is somebody's own
repository has one page fetched from the remote and read by the same function
that decides it on a checkout: a member's README for the membership
declaration, by `policy_check.declaration_in`, and an associate's
`docs/maintenance.md` for the footing marker, by `policy_check.associate_in`.
A tool recorded as a candidate that now declares membership is a stale
inventory, and so is a member that has stopped declaring. That is the failure
this was written for: three tools joined and the file did not move for long
enough that nobody could say from the file alone which of them had.

**What it cannot see** is whether a declaration is backed: that needs their whole
tree and their own CI is where it is decided. A remote that cannot be reached is
reported as unverified (exit 2), not as a compliance failure.
"""

from __future__ import annotations

import datetime
import json
import os
import re
import subprocess
import sys
import textwrap
import urllib.error
import urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))
sys.path.insert(0, ROOT)
from tools.stathmos.scripts.policy_check import policy_checker
from tools.stathmos.scripts.child_listing import read_listing, unverified_note
INVENTORY = os.path.join(ROOT, "scripts", "ecosystem", "ecosystem.json")
REPOS_FILE = os.environ.get("ANOIEU_REPOS_FILE",
                            os.path.join(ROOT, "scripts", "repos.local"))


#: What each status requires of an entry, beyond `what`.
#:
#: `associate` requires `vetted` and `why`, and nothing else requires either.
#: **The footing rests on their declaration rather than on our judgement**, so
#: what these two record is our reading of it: `vetted` is the date a person
#: last read their marker, and `why` is what that marker said. A marker can be
#: rewritten in their tree without anybody here noticing, which is the whole
#: reason the date is required and is not a second `what`.
REQUIRED = {
    "member": ("repo", "url"),
    "associate": ("repo", "url", "vetted", "why"),
    "candidate": ("repo", "url"),
    "foundation": ("repo", "url"),
    "child": ("parent",),
    # A tool outside this ecosystem that we track and are **not** proposing to
    # promote. It exists so that "how active were we this stretch" has
    # something to be compared against: our own numbers alone say nothing about
    # whether five days of commits is a lot. `why` is what it is being compared
    # for, and `vetted` is the date somebody last looked at the entry -- because
    # writing about a project that never asked to be written about should carry
    # a date the way every other claim here does.
    #
    # `released` and `published` are **two different facts** and LAW 9 turns on
    # the difference. `released` is where the code was made public. `published`
    # is the intellectual claim -- a paper, with an argument in it and its
    # authors' names on it -- and a great many public tools have none yet.
    #
    # Released but not published means we may track the artifact and **not the
    # contribution**: no positioning of our ideas against theirs, because a
    # repository with no paper behind it may be under review or being written up
    # right now, and we do not get to frame somebody's contribution before they
    # have. So `published` is required, and takes one of three values: a
    # citation, `"none"` where somebody established there is no paper, or
    # `"unknown"` where nobody has looked. The third exists because `"none"` is
    # a claim about somebody else's work -- asserting a project has published
    # nothing, when it has, is a falsehood in our register about them.
    # `"unknown"` permits exactly what `"none"` permits, so the careful
    # behaviour is what happens when nobody knows.
    #
    # Neither is printed in any table: they back the footing rather than
    # describing the tool.
    "outsider": ("repo", "url", "vetted", "why", "released", "published"),
    # The office, which `docs/laws.md` makes a footing. It asks for exactly what
    # `member` asks for because **a president is a member** -- LAW 2 binds it
    # like any other, and the office adds obligations rather than replacing
    # them. It is a separate status and not a flag on `member` because the
    # laws put it in the same table as the others, and because only one
    # repository holds it at a time, which `--check` enforces below.
    "president": ("repo", "url"),
}

#: The footings that are membership. A president is one of them: the office is
#: held *by* a member, so every count, every policy check and every question
#: asked of a member's README applies to it unchanged.
#: Every footing held to the shared policy by its name alone. `associate` is
#: deliberately not here: what an associate owes is written on its own
#: maintenance page rather than in this register, so the footing name cannot
#: decide it -- `still_true` and `--protocol` read that page's marker instead.
MEMBERS = ("member", "president")

#: The files the office is kept in, and the test for *limbo* -- the registry
#: recording a repository as president while its tree cannot hold the office.
#: The office moves by a person editing one line; these are carried by somebody
#: doing the work, and the gap between the two acts is the state this detects.
#: Reported against the row and never enforced: the remedy is somebody carrying
#: files, and a red build carries nothing.
PRESIDENT_FILES = {
    "docs/laws.md": "the laws, which the president maintains",
    "docs/history.md": "its account of its own term",
}

#: The repositories that have held the shared policy, and so the only ones a
#: `joined` coordinate may name. That field names a repository as well as a
#: commit because a bare sha identifies nothing once more than one tree could
#: have produced it, and the policy moves with the office. A name here is a
#: statement that a repository has kept the policy, and is never removed.
POLICY_HOLDERS = ("anoieu", "kanon")

#: A short git object name, the only form `joined` is written in. Long enough
#: to be unambiguous in trees this size and short enough to read in a table.
SHORT_SHA = re.compile(r"[0-9a-f]{7,40}")

#: A footing an entry says we *intend*, in `proposed`, while its `status` stays
#: what is true today. It exists because the associate protocol is drafted and
#: not decided: recording the intention as the fact would be this file asserting
#: something nobody has agreed to, and recording nothing would lose it.
PROPOSABLE = ("associate",)

#: The statuses whose entry asserts something about a README somebody else
#: keeps, and which `--online` therefore reads. `foundation` is deliberately not
#: here: its entry is a fact about *our* arrangement, asserts nothing about their
#: tree, and asking them for anything is what that footing exists to refuse.
OWN_REPO = ("member", "president", "associate", "candidate")


# The key printed under the table. A reader who cannot decode `3 failing` in a
# `candidate` row cannot tell a disagreement from a measurement, and the table
# had been printing that distinction for months without saying it anywhere.
#
# These are a **copy**: what a footing means is decided in `docs/policy.md`, and
# what a verdict means is decided by `check()` and by the branches in `main()`
# below. Keep the names aligned with REQUIRED. Nothing compares the prose,
# which is the half that can still drift.

#: One line per footing, in the order a reader meets them. Keep the keys equal
#: to `REQUIRED`'s; the value says how to *read the column*, never what the
#: footing means in full -- that is the policy's, and is linked below.
FOOTINGS = {
    "president": "a member, and holds the office. This column is the authority "
                 "on who that is; a note says so if the tree cannot hold it",
    "member": "declared membership. Held to the policy, and checked here",
    "candidate": "has not joined. The policy is addressed to them and binds them to nothing",
    "associate": "owes us nothing, and is checked anyway so the result is "
                 "known. A failure here is nobody's fault",
    "foundation": "the ecosystem is downstream of it. Asked for nothing, ever",
    "child": "a project inside another repository, on its parent's footing",
    "outsider": "published work outside the ecosystem, tracked so our own numbers "
                "have something to be compared against",
}

#: Every value the `policy` column can print, and what it means.
POLICY_VALUES = (
    ("ok", "every check that applies to that tree passed"),
    ("N failing", "N of our checks failed on a tree that is held to them"),
    ("N tracked", "N of our checks failed on an associate, which owes us "
                  "nothing. A measurement, and not a shortfall: nobody is at "
                  "fault for it and nobody is asked to fix it"),
    ("not held", "an outsider. No policy check was run"),
    ("no checkout", "not on this machine, so nothing could be run"),
    ("unverified", "the checker could not run; no compliance verdict is available"),
    ("-", "a child or a foundation: not a repository this table checks"),
)

#: Every value the `advertised?` column can print. Only a widened table shows
#: it: in the default view every row is one the default view kept, so the
#: column would say `yes` all the way down and answer nothing.
ADVERTISED_VALUES = (
    ("yes", "a child its parent advertises, which the default table also shows"),
    ("no", "a child its parent does not advertise. Here only because --all "
           "or --all-children asked for it"),
    ("?", "a child whose README could not be read, or which declared two "
          "things at once. Not advertised, and not a choice either"),
    ("-", "a repository, which has no listing preference to declare: this "
          "column is a child's"),
)

#: Every value the `channel` column can print, and what it means.
CHANNEL_VALUES = (
    ("N for us", "N topics in it are addressed to kanon"),
    ("yes", "they keep one, and nothing in it is for us"),
    ("none", "they keep none. Not a defect: the file is optional"),
    ("-", "a child or a foundation"),
)


def render_key() -> str:
    """The legend. Printed by `--help` and by nothing else.

    It ends with what to do about a failing row, because that is the question
    the table provokes and the one it was answering nowhere: the count is here,
    the detail is in another program, and which of the two repositories owns the
    problem depends on a column further left.

    **Not printed under the table.** It is twenty-odd fixed lines against a
    twenty-four line table, read once and never again, in a command that is run
    often -- so under the table it is the bulk of the output every time in order
    to be useful once. The table carries a one-line pointer to it instead, which
    is the part that cannot be dropped: a legend nobody is told about is not a
    legend, and *print it every run* and *do not mention it* are both wrong.
    """
    values = (tuple(FOOTINGS.items()), POLICY_VALUES, CHANNEL_VALUES)
    # One width across all three lists, so every description starts in the same
    # column. Widths computed per list read as three tables that happen to be
    # adjacent, which is what they looked like when this was first written.
    w = max(len(k) for group in values for k, _ in group) + 2

    def block(group) -> None:
        for k, why in group:
            out.append(f"             {k:<{w}}{why}")

    out = ["key"]
    out.append("  tool     its id in scripts/ecosystem/ecosystem.json -- what every prompt "
               "here calls it by")
    out.append("  status   what it owes us, and what we say about it. In full: "
               "docs/policy.md,")
    out.append("           \"The footings, and what each one costs whom\"")
    block(FOOTINGS.items())
    out.append("  policy   tools/stathmos/scripts/policy_check.py, run over that checkout by this "
               "command just now")
    block(POLICY_VALUES)
    out.append("  channel  their docs/discussion.md, which is optional and which "
               "most tools do not keep")
    block(CHANNEL_VALUES)
    out.append("  advertised?  what a child's README declares, shown only by "
               "--all and --all-children")
    block(ADVERTISED_VALUES)
    out.append("  moved    days since the last commit in the checkout on this "
               "disk, not on their remote")
    out.append("  where    where that checkout is")
    out.append("  purpose  `short`, falling back to `what`, in scripts/ecosystem/ecosystem.json")
    out.append("           at most 60 characters; longer descriptions end with an ellipsis")
    out.append("")
    out.append("fixing a `N failing` row")
    out.append("  The count is all this table has. To see what failed:")
    out.append("      python3 tools/stathmos/scripts/policy_check.py --root <where>")
    out.append("  Each FAIL line names the check and what it found.")
    out.append("  Whose it is to fix depends on the status column, and the two "
               "cases are not alike.")
    out.append("    member, president  they declared they follow this, so the "
               "tree and the claim")
    out.append("                       disagree. Theirs to fix, and a note "
               "below says so by name.")
    out.append("    anything else      they never agreed to any of this. It is a "
               "measurement and")
    out.append("                       not a shortfall, nobody owes us the fix, "
               "and it is not")
    out.append("                       something to open a topic about.")
    out.append("  And where the check is wrong -- it fires on something that is "
               "not a problem,")
    out.append("  or the policy does not fit a legitimate shape of repository -- "
               "that one is")
    out.append("  fixed in kanon/docs/policy.md for policy defects, or in "
               "anoieu/scripts/policy_check.py for checker defects.")
    return "\n".join(out)


def git(*args, cwd=None):
    out = subprocess.run(["git", *args], cwd=cwd, capture_output=True, text=True)
    return out.stdout.strip() if out.returncode == 0 else ""


def locate(repo: str) -> str:
    """A repo id, the way every script here resolves one: the mapping file, then
    a scan of $ANOIEU_REPOS. Never a bare path -- these ids come from a file."""
    if os.path.isfile(REPOS_FILE):
        with open(REPOS_FILE, encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line or line.startswith("#"):
                    continue
                parts = line.split(None, 1)
                if len(parts) == 2 and parts[0] == repo:
                    path = os.path.expanduser(parts[1].strip())
                    if os.path.isdir(path):
                        return path
    roots = os.environ.get("ANOIEU_REPOS", "").split(os.pathsep)
    for r in [p for p in roots if p] + [os.path.dirname(ROOT), os.path.expanduser("~")]:
        cand = os.path.join(r, repo)
        if os.path.isdir(cand):
            return cand
    return ""


def age(path: str) -> str:
    when = git("log", "-1", "--format=%cI", cwd=path)
    if not when:
        return "?"
    then = datetime.datetime.fromisoformat(when)
    days = (datetime.datetime.now(then.tzinfo) - then).days
    return "today" if days == 0 else f"{days}d"


def check(path: str) -> tuple[str, list[str]]:
    out = subprocess.run(
        [sys.executable, os.path.join(HERE, "policy_check.py"),
         "--root", path], capture_output=True, text=True)
    # count the failing *checks*, not their detail lines: one check that reports
    # three things is one thing wrong, and saying "3 fail" overstates it.
    failed, detail = [], []
    in_failure = False
    for line in out.stdout.splitlines():
        if line.startswith("FAIL "):
            failed.append(line[5:].strip())
            detail.append(failed[-1])
            in_failure = True
        elif in_failure and line.startswith("     "):
            detail.append(line.strip())
        else:
            in_failure = False
    if out.returncode not in (0, 1) or (out.returncode == 1 and not failed):
        return "unverified", [out.stderr.strip() or out.stdout.strip()
                              or "the policy checker did not report a result"]
    return (f"{len(failed)} failing" if failed else "ok"), detail


def addressed_to(line: str, who: str) -> bool:
    """Does this `**To:**` line address `who`?

    A topic may name several tools at once -- a global notice names every
    member -- so the field is a list and not a name. Reading it as a name is
    what this used to do, by counting the string `**To:** kanon`, and every
    topic that named somebody else first was silently not counted: the table
    said a tool owed us nothing while a notice addressed to us sat in its file.
    """
    m = re.match(r"\*\*To:\*\*\s*(.+)", line.strip())
    return bool(m) and who in {n.strip(" `") for n in m.group(1).split(",")}


def topics_for(path: str, who: str = "kanon") -> str:
    """The `channel` column: whether a tool keeps a discussion file, and how
    many topics in it are addressed to us."""
    disc = os.path.join(path, "docs", "discussion.md")
    if not os.path.isfile(disc):
        return "none"
    with open(disc, encoding="utf-8") as f:
        for_us = sum(1 for line in f if addressed_to(line, who))
    return f"{for_us} for us" if for_us else "yes"


def board_entities() -> set[str]:
    """Every repository the board addresses, from its `Entities` lines."""
    path = os.path.join(ROOT, "docs", "board.md")
    if not os.path.isfile(path):
        return set()
    out = set()
    with open(path, encoding="utf-8") as f:
        for line in f:
            m = re.match(r"\*\*Entities:\*\* (.+)", line.strip())
            if m:
                out |= {e.strip(" `") for e in m.group(1).split(",")}
    return out


def well_formed(inv: dict) -> list[str]:
    """The inventory read as a document about itself. No network, no checkouts."""
    bad = []
    for name, e in inv.items():
        status = e.get("status", "")
        if status not in REQUIRED:
            bad.append(f"{name}: status {status or '(none)'} is not one this file defines")
            continue
        for field in REQUIRED[status] + ("what",):
            if not e.get(field):
                bad.append(f"{name}: a {status} entry needs `{field}`")
        if status == "child":
            parent = e.get("parent", "")
            if parent not in inv:
                bad.append(f"{name}: its parent `{parent}` is not in this file")
            elif inv[parent].get("status") == "child":
                bad.append(f"{name}: its parent `{parent}` is itself a child project")
        proposed = e.get("proposed", "")
        if proposed:
            if proposed not in PROPOSABLE:
                bad.append(f"{name}: `proposed` is {proposed!r}, and the only "
                           f"footing that may be proposed is {PROPOSABLE[0]!r}")
            elif proposed == status:
                bad.append(f"{name}: proposes the footing it already holds; "
                           "`proposed` records an intention, not the fact")
            else:
                # An intention nobody has read the tree for is a wish. The same
                # two fields the footing itself requires are required to propose
                # it, which is what stops `proposed` becoming a cheaper way in.
                for field in ("vetted", "why"):
                    if not e.get(field):
                        bad.append(f"{name}: proposing `{proposed}` needs `{field}`, "
                                   "the same as holding it")
        # LAW 9: `published` records an intellectual claim its authors made, and
        # `"none"` is the answer when they have not made one yet. A blank is
        # neither answer, and the two permit different things.
        # LAW 10: *in dioktes* is a state this ecosystem enters, declared against
        # the tool it concerns so that somebody can object while it is happening
        # rather than afterwards. It is entered **only where we believe a claim
        # that tool has made is inaccurate**, so the field reads "<date began> --
        # <the claim, and what closes it>": a pursuit with no stated end is a
        # posture rather than an investigation, and one whose belief was written
        # afterwards is whatever the findings happened to support. The entry is
        # removed when the claim settles either way, rather than kept as a record
        # of having once been in one.
        dioktes = e.get("dioktes", "")
        if dioktes:
            if status != "outsider":
                bad.append(f"{name}: `dioktes` is declared against a {status} "
                           "entry; LAW 10 is about tools outside this ecosystem")
            elif "--" not in dioktes:
                bad.append(f"{name}: `dioktes` is {dioktes!r}; it reads "
                           "\"<date began> -- <what closes it>\", and a pursuit "
                           "with no stated end is a posture")

        if status == "outsider":
            pub = e.get("published", "")
            if pub and pub not in ("none", "unknown") and "http" not in pub \
                    and len(pub) < 12:
                bad.append(f"{name}: `published` is {pub!r}; write the paper it "
                           "cites, `none` where somebody established there is "
                           "not one, or `unknown` where nobody has looked")

        url = e.get("url", "")
        if url and not url.startswith("https://"):
            bad.append(f"{name}: `{url}` is not an https url")
        # `joined` names the commit of whichever repository held the shared
        # policy at the time, so it reads `kanon 1a2b3c4`. Checked because the
        # tempting shorthand -- a bare sha -- was unambiguous only while one
        # repository had ever kept the policy, and that stopped being true at
        # the 2026-09-15 handoff. Nothing requires the field; this decides only
        # whether a value that is there can be read.
        joined = e.get("joined", "")
        if joined:
            if status not in MEMBERS:
                bad.append(f"{name}: a {status} entry carries `joined`, which "
                           "records when a repository joined; this one has not")
            parts = joined.split()
            if len(parts) != 2 or parts[0] not in POLICY_HOLDERS \
                    or not SHORT_SHA.fullmatch(parts[1]):
                bad.append(f"{name}: `joined` is {joined!r}; it names the "
                           "repository that held the policy and that "
                           "repository's commit, as in `kanon 1a2b3c4`, from "
                           f"{' or '.join(POLICY_HOLDERS)}")
    # `docs/laws.md`, LAW 3: there is a president, "one at a time". A file that
    # records two has recorded a handover that did not finish, which is the one
    # way this footing can go wrong silently -- both rows look correct alone.
    held = [k for k, v in inv.items() if v.get("status") == "president"]
    if len(held) > 1:
        bad.append("two repositories are recorded as president -- "
                   + ", ".join(sorted(held))
                   + " -- and the office is held one at a time")
    for entity in sorted(board_entities() - set(inv)):
        bad.append(f"docs/board.md addresses `{entity}`, which has no row here")
    return bad


def remote_file(url: str, rel: str, timeout: int = 20) -> tuple[str, str]:
    """One file from a repository's remote. Returns (text, why-not).

    Read over https rather than by cloning, because this runs on every push and
    the question is one file. Only GitHub urls can be turned into a raw one from
    here; anything else is reported as unreadable rather than guessed at.

    Two files are asked for: a README, which is where a member declares, and
    `docs/maintenance.md`, which is where an associate records its footing.
    """
    m = re.match(r"https://github\.com/([^/]+)/([^/]+?)(?:\.git)?/?$", url)
    if not m:
        return "", f"{url} is not a github url this can read a file from"
    raw = f"https://raw.githubusercontent.com/{m.group(1)}/{m.group(2)}/HEAD/{rel}"
    try:
        with urllib.request.urlopen(raw, timeout=timeout) as r:  # noqa: S310
            return r.read().decode("utf-8", "replace"), ""
    except urllib.error.HTTPError as e:
        if e.code == 404:
            return "", ""          # an absent file is an answer, not a failure to ask
        return "", f"{raw}: HTTP {e.code}"
    except (urllib.error.URLError, OSError, ValueError) as e:
        return "", f"{raw}: {str(e)[:60]}"


def readme_of(url: str, timeout: int = 20) -> tuple[str, str]:
    """A repository's README, from its remote."""
    return remote_file(url, "README.md", timeout)


def still_true(inv: dict) -> tuple[list[str], list[str]]:
    """Ask each remote whether the status recorded here is still the right one.

    Returns (failures, unreachable). Unreachable leaves the claim unverified;
    it is not evidence of stale membership.
    """
    policy_check = policy_checker()

    bad, unseen = [], []
    for name, e in inv.items():
        status = e.get("status")
        if status not in OWN_REPO:
            continue
        text, why = readme_of(e.get("url", ""))
        if why:
            unseen.append(f"{name}: {why}")
            continue
        missing = policy_check.declaration_in(text)
        declares = not missing
        if status == "candidate" and declares:
            bad.append(f"{name} declares membership on its default branch and is "
                       "recorded here as a candidate: it has joined, and this file "
                       "has not been told")
        if status in MEMBERS and not declares:
            bad.append(f"{name} is recorded here as a {status} and its README "
                       f"does not declare membership: {missing[0]}")
        if e.get("proposed") == "associate" and status != "associate":
            # Proposed affiliations are reported by --protocol, not a failed
            # fetch or a requirement of the repository's current footing.
            continue
        if status == "associate":
            # **The footing is recorded on their own maintenance page**, which
            # is what the associate protocol settled it to be, so that is the
            # page this asks. It used to ask the README for the *affiliating*
            # note -- the paragraph a repository writes to say it is **not**
            # held to this policy -- which is very nearly the opposite claim,
            # and reported a correctly marked associate as a mismatch.
            if declares:
                bad.append(f"{name} declares full membership on its front page "
                           "and is recorded here as an associate: it has joined, "
                           "and this file has not been told")
                continue
            marker_in = getattr(policy_check, "associate_in", None)
            if marker_in is None:
                unseen.append(f"{name}: this checker cannot read an associate's "
                              "footing marker; a newer anoieu can")
                continue
            page, why = remote_file(e.get("url", ""), "docs/maintenance.md")
            if why:
                unseen.append(f"{name}: {why}")
                continue
            gone = marker_in(page)
            # Their tree owes us nothing, so this is phrased as our record being
            # out of step rather than as their shortfall. `vetted` and `why` in
            # the entry are a person's reading of a marker that can be rewritten
            # without anybody here noticing, and this is what notices.
            if gone:
                bad.append(f"{name} is recorded here as an associate and its "
                           f"docs/maintenance.md no longer records that footing: "
                           f"{gone[0]}. Ours to re-read, not theirs to fix")
    return bad, unseen


def page_for(name: str, e: dict, rel: str) -> tuple[str, str]:
    """One page of a tool's tree, from its checkout if that checkout has it and
    from its remote otherwise. Returns (text, source), where source is what to
    print.

    The checkout is preferred because this report is run while somebody is
    deciding something and a network round trip per tool makes it a job rather
    than a command. Which one answered is printed, because a stale checkout and
    a published page are different claims and the difference matters here.

    **Per file, and not per tree.** A checkout can be half a checkout -- a clone
    that failed leaves a working tree with a README and no history and no
    `docs/` -- and resolving the tree once would then report a repository as
    missing a page its remote carries.
    """
    path = locate(e.get("repo", name))
    if path and os.path.isfile(os.path.join(path, rel)):
        with open(os.path.join(path, rel), encoding="utf-8") as f:
            return f.read(), "checkout"
    text, why = remote_file(e.get("url", ""), rel)
    return (text, "remote") if not why else ("", "unreachable")


def readme_for(name: str, e: dict) -> tuple[str, str]:
    """A tool's README, wherever `page_for` finds it."""
    return page_for(name, e, "README.md")


def protocol(inv: dict) -> int:
    """`--protocol`: who would satisfy the associate protocol, in each of the
    versions of it that is still on the table.

    **It reports and it never fails.** Every repository in it is held to none of
    this, most of them have not been asked, and the protocol itself is drafted
    rather than decided -- see *The associate protocol* in `docs/policy.md`. A
    non-zero exit here would be this repository grading somebody for failing to
    comply with a rule that does not exist yet.

    Three columns, because the undecided question is *which* of them we would
    require, and a person deciding that should be able to see what each would
    cost today rather than predict it:

      marker        the settled half: `**Footing:** associate` on their own
                    `docs/maintenance.md`, saying what they hold themselves to.
                    A recorded associate carries this and a proposed one need
                    not, since nobody has asked them for anything yet
      note          a `How this repository is maintained` heading, with
                    something under it. The drafted protocol, and the whole of it
      affiliating   that, and a paragraph naming the ecosystem and saying the
                    repository is not held to its policy. The stronger option
      declares      a full membership declaration, which no associate needs and
                    which would mean the footing is the wrong one

    **The marker and the other three answer different questions**, and the
    table used to carry only the second kind. What an associate records is
    settled; what to ask of a tree that adopts none of this is not.
    """
    try:
        policy_check = policy_checker()
    except (OSError, ImportError) as exc:
        print(f"UNVERIFIED: {exc}")
        return 2

    marker_in = getattr(policy_check, "associate_in", None)
    rows = []
    for name, e in inv.items():
        status, want = e.get("status", ""), e.get("proposed", "")
        if "associate" not in (status, want):
            continue
        text, source = readme_for(name, e)
        if source == "unreachable":
            rows.append((name, status, want, "?", "?", "?", "?", "unreachable"))
            continue
        yes = lambda missing: "no" if missing else "yes"  # noqa: E731
        page, page_source = page_for(name, e, "docs/maintenance.md")
        if marker_in is None:
            marker = "?"
        elif page_source == "unreachable":
            marker = "?"
        else:
            marker = yes(marker_in(page))
        where = (source if page_source in (source, "unreachable")
                 else f"{source}/{page_source}")
        rows.append((name, status, want, marker,
                     yes(policy_check.note_in(text)),
                     yes(policy_check.affiliation_in(text)),
                     yes(policy_check.declaration_in(text)),
                     where))

    if not rows:
        print("-- nobody holds or is proposed for `associate`, so there is "
              "nothing to report")
        return 0

    w = max(len(r[0]) for r in rows) + 2
    print(f"{'tool':<{w}}{'footing':<12}{'proposed':<11}{'marker':<9}"
          f"{'note':<7}{'affiliating':<13}{'declares':<10}read from")
    for name, status, want, marker, a, b, c, source in rows:
        print(f"{name:<{w}}{status:<12}{want or '-':<11}{marker:<9}"
              f"{a:<7}{b:<13}{c:<10}{source}")

    print()
    print("`marker` is settled and the three columns after it are not: "
          "docs/policy.md,")
    print("`The associate protocol`, says which question is still open.")
    print("Nothing here is a verdict and nothing here fails. Every tool in this "
          "table is held")
    print("to none of this repository's policy, and most of them have not been "
          "asked to be.")
    return 0



def audit(online: bool) -> int:
    """`--check`: the inventory as a document, and optionally as a claim.

    Named apart from `check` above, which asks the policy checker about one
    checkout. The two were briefly the same name, and the table stopped working
    for as long as that was true.
    """
    with open(INVENTORY, encoding="utf-8") as f:
        inv = json.load(f)
    inv = {k: v for k, v in inv.items() if not k.startswith("_")}

    bad = well_formed(inv)
    for b in bad:
        print(f"FAIL {b}")
    print(f"-- inventory structure: {len(bad)} failure(s), "
          f"{len(inv)} entries")

    if bad:
        return 1
    if not online:
        print("-- structure only; --online compares each remote with what is "
              "recorded here")
        return 0

    try:
        stale, unseen = still_true(inv)
    except (OSError, ImportError) as exc:
        print(f"UNVERIFIED: {exc}")
        return 2
    for b in stale:
        print(f"FAIL {b}")
    for u in unseen:
        print(f"UNVERIFIED {u}")
    asked = sum(1 for e in inv.values() if e.get("status") in OWN_REPO) - len(unseen)
    print(f"-- remote declarations: {len(stale)} mismatch(es), "
          f"{asked} read, {len(unseen)} unverified")
    print("   One section of one page is what this reads, and which page depends "
          "on the\n   footing: the README for a member's declaration, "
          "`docs/maintenance.md` for an\n   associate's footing marker. Whether "
          "their tree backs a declaration is decided\n   by their own CI, running "
          "the same checker, and is not visible from here.")
    print("   Whether an associate is still worth vetting is nobody's to decide "
          "from here\n   either: the `vetted` date says when a person last did, "
          "and it does not expire\n   on its own.")
    return 1 if stale else (2 if unseen else 0)


USAGE = """usage: eo_status_audit [--verbose] [--all | --all-children] [--check [--online]] [--protocol]

  (no arguments)  the table: repositories and advertised children
  --verbose       ... and, per tool, which checks failed and what they found
  --all           every row this table can show, which today means every
                  recorded child including the unadvertised ones. The table
                  and nothing else
  --all-children  the same rows, and a note per child saying what it declared
                  and why -- for auditing the preferences rather than reading
                  the table
  --check         is the inventory itself well formed? No network, no checkouts
  --check --online  ... and does each remote still agree with it -- a member's
                  README, an associate's maintenance page
  --protocol      where each tool proposed for `associate` stands against the
                  drafted protocol. Reports, and never fails
  --help          this, and the key below

A child opts out by recording **Footing:** `unadvertised-child` in its own
README, spelled exactly as anoieu's checker reads it. Missing declarations mean
advertised. Opting out changes the listing and nothing else: the footing stands,
the checker still runs, and --all shows every row.
Preferences are read from local parent checkouts; unavailable or invalid reads
are reported as unverified. --check still validates the complete inventory.
A fenced example, an HTML comment or ordinary prose is not a declaration, an
unsupported value is unverified, and so is a README carrying two that disagree.

exit codes
  0  the table, or every requested comparison succeeded
  1  invalid inventory, or a remote page that disagrees with the register
  2  verification is incomplete -- a network failure is unverified, and not
     evidence against anybody. The ordinary table is a report, not a CI gate.
"""


#: Every option this command takes. An unrecognised one is refused rather than
#: ignored, because a silently accepted flag prints the default table and looks
#: exactly like a flag that worked -- which is how `--all` behaved before it
#: existed, and is a worse failure than an error.
FLAGS = frozenset({"--help", "-h", "-help", "--check", "--online",
                   "--protocol", "--verbose", "--all", "--all-children"})


def main() -> int:
    unknown = [a for a in sys.argv[1:] if a not in FLAGS]
    if unknown:
        print("eo_status_audit: not an option here: " + ", ".join(unknown),
              file=sys.stderr)
        print(USAGE, file=sys.stderr)
        return 2
    if "--help" in sys.argv or "-h" in sys.argv or "-help" in sys.argv:
        print(USAGE)
        print(render_key())
        return 0
    if "--online" in sys.argv and "--check" not in sys.argv:
        print("eo_status_audit: --online requires --check", file=sys.stderr)
        return 2
    if "--check" in sys.argv:
        return audit("--online" in sys.argv)
    if "--protocol" in sys.argv:
        inv = json.load(open(INVENTORY, encoding="utf-8"))
        return protocol({k: v for k, v in inv.items() if not k.startswith("_")})
    verbose = "--verbose" in sys.argv
    all_children = bool({"--all", "--all-children"} & set(sys.argv))
    #: Both flags widen the table; only one explains itself. `--all-children`
    #: is for auditing the preferences, so it says what each child declared and
    #: why. `--all` is for reading the table, where a note per child is a screen
    #: of prose between you and the rows you asked for.
    listing_notes = "--all-children" in sys.argv
    with open(INVENTORY, encoding="utf-8") as f:
        inv = json.load(f)
    rows, notes = [], []
    child_listings, parent_paths = {}, {}

    for name, e in inv.items():
        if name.startswith("_"):
            continue
        status = e.get("status", "?")
        if status == "child":
            parent = e.get("parent", "")
            if parent not in parent_paths:
                parent_paths[parent] = locate(inv.get(parent, {}).get("repo", parent))
            listing = read_listing(parent_paths[parent], e.get("path", ""))
            child_listings.setdefault(parent, []).append(listing)
            if listing_notes:
                detail = f" ({listing.reason})" if listing.reason else ""
                notes.append(f"{name}: Eunoia listing: {listing.state}{detail}")
            if not all_children and not listing.advertised:
                continue
        if status in ("child", "foundation"):
            listed = {"advertised": "yes", "unadvertised": "no"}.get(
                listing.state, "?") if status == "child" else "-"
            rows.append((name, status, "-", "-", "-", e.get("parent", ""), listed))
            continue
        path = locate(e.get("repo", name))
        if not path:
            rows.append((name, status, "no checkout", "-", "-", "", "-"))
            continue
        # An associate is held to none of this, so nothing here runs the checker
        # over its tree. A failure count in that row would be this table
        # grading somebody who never agreed to be graded, which is the whole of
        # what the footing refuses.
        # An associate owes us nothing and is checked anyway: knowing whether
        # a tree we depend on conforms is worth having, and it costs them
        # nothing because no answer obliges them. The verdict is spelled
        # differently on purpose -- `tracked` rather than `failing` -- because
        # the same number means a shortfall for a member and a measurement
        # here, and a column that printed them identically would be inviting
        # the reader to draw a conclusion the footing refuses.
        if status == "outsider":
            verdict, fails = "not held", []
        elif status == "associate":
            verdict, fails = check(path)
            if verdict.endswith("failing"):
                verdict = verdict.replace("failing", "tracked")
        else:
            verdict, fails = check(path)
        topics = topics_for(path)
        rows.append((name, status, verdict, topics, age(path), path, "-"))
        # Both notes name the disagreement and then say whose move it is,
        # rather than stating the rule -- "this is the state the check exists
        # to catch" explains the check to somebody who already knows why it is
        # there, and tells a reader arriving cold nothing they can act on.
        if verdict == "ok" and status == "candidate":
            notes.append(
                f"{name} passes our checks but we still have it down as a "
                "candidate rather than a member. If it has joined since, our "
                "inventory is out of date -- ours to fix, in scripts/ecosystem/ecosystem.json")
        if verdict == "unverified":
            notes.append(f"{name}: policy unverified: {'; '.join(fails)}")
        elif verdict != "ok" and status in MEMBERS:
            # The count comes from `verdict`, which counts failing *checks*.
            # `fails` is their detail lines and there are more of them -- the
            # overstatement `check()` warns about three lines above its return.
            n_fail = verdict.split()[0]
            where_short = path.replace(os.path.expanduser("~"), "~")
            notes.append(
                f"{name} says it follows the shared policy, and {n_fail} of our "
                "checks fail on its tree. Theirs to fix, not ours. To see what: "
                f"python3 tools/stathmos/scripts/policy_check.py --root {where_short}")
        # Limbo. Said against the row rather than left for somebody to notice,
        # because it is the one state here that is supposed to be brief: while
        # it lasts nobody is keeping the laws and nothing is recording the term.
        if status == "president":
            absent = [f"`{f}` ({why})" for f, why in PRESIDENT_FILES.items()
                      if not os.path.isfile(os.path.join(path, f))]
            if absent:
                notes.append(
                    f"IN LIMBO: the registry records {name} as president and its "
                    f"tree does not carry {', '.join(absent)}. The office has "
                    "moved and the means of holding it have not. Fix it quickly "
                    "-- carry the files, or put the registry line back. Nothing "
                    "here fails a build over it")

        # A checkout whose directory is not called what the inventory calls it.
        # Said loudly because the quiet version of this cost us a member: the
        # tree was on disk as `eudiamonia`, the inventory said `eudaimonia`, and
        # the row read `no checkout` for a repository that was right there --
        # hiding its failures and eleven topics it was owed. A near-miss is
        # worse than an absence: absence is obvious and this is not.
        if path:
            want = inv[name].get("repo", name)
            got = os.path.basename(os.path.normpath(path))
            if got != want:
                notes.append(f"NAME MISMATCH: {name} is checked out as `{got}` "
                             f"and we expect `{want}`. One of the two is a typo, "
                             "and until it is fixed this row is resolved by a "
                             "hand-written line in scripts/repos.local rather "
                             "than by its name")
        if verbose and fails:
            notes.append(f"{name}: " + "; ".join(fails))

    for parent, listings in child_listings.items():
        note = unverified_note(parent, listings)
        if note:
            notes.append(note)


    w = max((len(r[0]) for r in rows), default=4) + 2
    locations = {r[0]: r[5].replace(os.path.expanduser("~"), "~") for r in rows}
    where_width = max([len("where")] + [len(path) for path in locations.values()]) + 2
    # The column earns its width only where unadvertised rows can appear.
    ad = f"{'advertised?':<13}" if all_children else ""
    print(f"{'tool':<{w}}{'status':<11}{'policy':<12}"
          f"{'channel':<10}{ad}{'moved':<8}{'where':<{where_width}}purpose")
    for name, status, verdict, topics, moved, where, listed in rows:
        purpose = textwrap.shorten(inv[name].get("short") or inv[name].get("what") or "-",
                                   width=60, placeholder="…")
        print(f"{name:<{w}}{status:<11}{verdict:<12}"
              f"{topics:<10}{f'{listed:<13}' if all_children else ''}"
              f"{moved:<8}{locations[name]:<{where_width}}{purpose}")

    # The pointer, not the key. One line, immediately under the table, because
    # the moment somebody needs the legend is the moment they are looking at a
    # column they cannot read.
    print()
    print("-- what the columns mean, and what to do about a failing row: "
          "eo_status_audit --help")

    if notes:
        print()
        for n in notes:
            print(f"note: {n}")

    counts: dict[str, int] = {}
    for r in rows:
        counts[r[1]] = counts.get(r[1], 0) + 1
    members = [r for r in rows if r[1] in MEMBERS]
    passing = sum(1 for r in members if r[2] == "ok")
    owed = sum(int(r[3].split()[0]) for r in rows if r[3].endswith("for us"))

    #: Plurals not formed by adding an s.
    PLURAL = {"child": "children"}
    parts = ", ".join(f"{n} {PLURAL.get(k, k + 's') if n != 1 else k}"
                      for k, n in sorted(counts.items(), key=lambda kv: -kv[1]))

    # One sentence, last, after everything. A reader who wants the state of the
    # ecosystem should not have to add a column up themselves, and it is held to
    # one sentence because a summary that grows into a paragraph is a second
    # report -- and then there are two of them to keep true.
    print()
    # `members` is every footing held to the policy, which is member *and*
    # president -- so calling the number "members" contradicted the footing
    # counts in the same sentence, which say 8 members and 1 president.
    print(f"In short: {parts}; {passing} of {len(members)} repositories held to "
          f"the policy pass their check, {owed} topic{'s' if owed != 1 else ''} "
          f"{'are' if owed != 1 else 'is'} owed to us, "
          "and how good any of these tools actually are is a judgement kept in "
          "https://github.com/ajreynol/kanon/blob/main/tools/stathmos/report-card.md "
          "rather than in this table.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
