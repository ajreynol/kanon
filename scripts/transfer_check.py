#!/usr/bin/env python3
"""Are we ready to transfer roles to a project?

**One question, and it is deliberately not the whole question.** Readiness here
means *our side is in order and there is somewhere for the roles to go*. It does
not mean the transfer is a good idea, that anybody has agreed, or that the
receiving project wants them.

**Both repositories must have their CI passing.** This helper moved from an
anoieu CI job to kanon and no longer runs behind that job's prerequisites. It
therefore reports local CI as unverified. `--online` can read the destination's
latest run, but that alone cannot authorize a transfer.

Exit codes:

    1   not ready   -- a pending role marker or destination is missing
    2   unverified  -- a build remains unchecked, even if the markers exist

There is no success exit until both builds can be established. A person checks
the two commits before moving anything.

**Roles move by being marked.** A role destined for another project carries a
`Destined for` line in `docs/roles.md`, and that marker is what this reads. **A
transfer nobody wrote down is not pending**, it is an intention.
"""

import json
import os
import re
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)


def destined(target: str) -> list[str]:
    """Role ids marked in `roles.md` as destined for this target."""
    path = os.path.join(ROOT, "docs", "roles.md")
    try:
        with open(path, encoding="utf-8") as f:
            text = f.read()
    except OSError:
        return []
    ids, current = [], None
    for line in text.splitlines():
        m = re.match(r"^### (R\d+) — ", line)
        if m:
            current = m.group(1)
        if current and re.search(rf"Destined for [`*]*{re.escape(target)}[`*]*", line):
            if current not in ids:
                ids.append(current)
    return ids


def exists(target: str) -> tuple[bool, str]:
    """Whether the target is somewhere we can point at, and where."""
    inv = os.path.join(HERE, "ecosystem", "ecosystem.json")
    try:
        with open(inv, encoding="utf-8") as f:
            d = json.load(f)
    except OSError:
        d = {}
    if target in d and not target.startswith("_"):
        return True, f"in the inventory as `{d[target].get('status', '?')}`"
    if os.path.isfile(os.path.join(ROOT, "tools", target, "README.md")):
        return False, "a stub here, and no repository"
    return False, "nowhere: not in the inventory and not even a stub"


def their_ci(target: str) -> tuple[str, str]:
    """Their build, if we are allowed to ask. Never called from CI."""
    inv = os.path.join(HERE, "ecosystem", "ecosystem.json")
    try:
        with open(inv, encoding="utf-8") as f:
            url = json.load(f).get(target, {}).get("url", "")
    except OSError:
        url = ""
    if not url:
        return "unverified", "no repository url recorded"
    slug = url.rstrip("/").split("github.com/")[-1]
    try:
        out = subprocess.run(["gh", "run", "list", "--repo", slug, "--limit", "1",
                              "--json", "conclusion", "-q", ".[0].conclusion"],
                             capture_output=True, text=True)
    except OSError as exc:
        return "unverified", f"could not run gh: {exc}"
    if out.returncode != 0:
        return "unverified", "could not ask GitHub"
    verdict = out.stdout.strip()
    if not verdict:
        return "unverified", "no runs recorded"
    return ("green" if verdict == "success" else "not green"), verdict


def main(argv: list[str]) -> int:
    online = "--online" in argv
    names = [a for a in argv if not a.startswith("--")]
    if len(names) != 1:
        print("usage: transfer_check.py <target> [--online]", file=sys.stderr)
        return 2
    target = names[0]

    roles = destined(target)
    there, where = exists(target)
    problems = []
    if not roles:
        problems.append(f"no role in docs/roles.md is marked `Destined for "
                        f"{target}` -- a transfer nobody wrote down is an "
                        "intention, not a pending move")
    if not there:
        problems.append(f"{target} is {where}. Roles cannot move to a "
                        "repository that does not exist")

    print(f"transfer to {target}")
    print(f"  roles marked to move: {', '.join(roles) if roles else 'none'}")
    print(f"  the target is:        {where}")
    print("  our CI:               unverified here -- check the runs for this commit")

    if online:
        state, detail = their_ci(target)
        print(f"  their CI:             {state} ({detail})")
        if state == "unverified":
            print("UNVERIFIED: we could not read their build, which is not a pass.")
            return 2
        if state != "green":
            problems.append(f"{target}'s most recent CI run is {detail}")
    else:
        print("  their CI:             unverified from here -- run with --online")

    if problems:
        print(f"NOT READY to transfer roles to {target}:")
        for p in problems:
            print(f"  - {p}")
        return 1
    print(f"Role markers and destination exist for {target}.")
    if not online:
        print("  Their build is still unchecked. A person confirms it with "
              "--online before anything moves.")
        return 2
    print("  Our build is still unchecked. A person confirms both builds before anything moves.")
    return 2


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
