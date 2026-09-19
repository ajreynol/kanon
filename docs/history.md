# History — kanon's term

**kanon's account of its own term holding the presidency of the Eunoia
ecosystem.** It stays in this tree. It does not travel to whoever holds the
office next, and kanon inherited no such page from anyone: the accounts
scatter, one per repository that has held the office.

The president may add, revise or remove entries during the term under
[LAW 4.1](laws.md#law-41--keeping-and-revising-the-terms-history).

## What you need to know to read this page, and nothing more

**The Eunoia ecosystem is a handful of repositories built around one proof
calculus**, each with a human maintainer who is the authority over it. A
repository's **footing** says what it owes the ecosystem and what the ecosystem
says about it. A **member** has declared, on its own front page, that it is
part of the ecosystem and runs the shared policy checker in its own CI. A
**candidate** has not joined; the policy is addressed to it and binds it to
nothing. The other footings do not appear on this page.

**The presidency is one member that also holds an office, for a stretch.** It
sets direction and nothing more — it cannot require anything of a member the
shared policy does not already require, and it confers nothing over anybody's
repository. It is bestowed by a person, it expires with the stretch, and
handing it on is the point.

**One file decides who holds it**, and it is
[`../scripts/ecosystem/ecosystem.json`](../scripts/ecosystem/ecosystem.json):
the repository whose entry reads `status: president` is the president. Anything
else that says so — a front page, a letter, this page — is downstream, and
where one of them disagrees with that file, that file is right.

The sections below are this repository's way of organizing its account.
Source references and commands accompany entries where useful; the laws do
not prescribe fields, evidence or a separate correction record for this page.

## The term

**It began at kanon `7eb9973`, 2026-09-15 16:15:45 −05:00** — the commit in
which the registry first recorded `status: president` against kanon. The office
is bestowed by a person editing that line, so that commit is the start of the
term and not an approximation of it.

**It has not ended.**

**The registry itself moved in the same minute.** anoieu deleted its copy at
`ca58216`, 16:14:44, and this tree created the one that replaced it at
`7eb9973`, 16:15:45 — so for sixty-one seconds no repository anywhere held the
file that decides who the president is. Nothing depended on it during that
minute and nothing was harmed by it. It is here because a gap in the one record
that is supposed to have no gaps is exactly what a later reader would have no
way to find.

*Re-derive:* `git log -S'"status": "president"' --
scripts/ecosystem/ecosystem.json` in this repository, and `git log
--diff-filter=D -- scripts/ecosystem/ecosystem.json` in anoieu.

### What moved, and what did not

The governance handoff landed at `7eb9973`, out of `B15`, which argued that
governance should leave the analyzer.

- **Moved here:** `R4`, policy and joining; `R6`, the register and
  installation; the development vision, since folded into `R4`; and five child
  projects, whose own role ids and responsibilities stayed their own. -
  **Stayed in anoieu:** the findings system; `R2`, the analyzer; `R3`, the
  fuzzer; and `R31`, the policy checker. - **Unchanged:** member workflows pin
  anoieu's checker, and a document move does not move a pin. How the policy and
  the checker stay in version step is an open follow-up under `R31`.

*Re-derive:* `git log --diff-filter=A -- docs/policy.md` in this repository,
and the same with `--diff-filter=D` in anoieu.

### Ethics projects moved to epikrisis — 2026-09-17

The maintainer copied martyria and zetesis to epikrisis. Before removing the
source directories, all nine tracked files were compared with the receiving
checkout and were byte-identical, including the cases and findings. They remain
distinct, unadvertised child projects; the inventory now names epikrisis as
their parent. Earlier accounts of their arrival in kanon remain unchanged.

At the maintainer's direction the working-hours program and schedule stayed in
kanon, at `scripts/sleep.py` and `scripts/schedule.json`, with the ethical
arguments and case records in epikrisis. That separated their custody from the
presidency without establishing independence from the ecosystem whose conduct
they examine. **Both files were deleted later the same day** and `PROTO-18` went
with them — two entries below.

### The glossary became the name register — 2026-09-17

At the maintainer's direction, `docs/glossary.md` became the authoritative
register of names in use, kept by the president. Ynoia's taken, reserved, and
in-use tables were removed. The remaining guidance from `names.md` was merged
into [proposals.md](../tools/ynoia/docs/proposals.md#arguing-about-names), and the
separate page was deleted. Unused candidates remain in proposals, outside the
dictionary.
`init_eo` now reads the glossary directly. Earlier accounts of the register's
location in ynoia record the arrangement at the time.

### The handoff procedure was relaxed, and three laws changed — 2026-09-17

At the maintainer's direction, all on one day.

- **`roles.md`, *How a role is handed off*:** seven ordered steps became three
  unordered ones. Out: the required order, the `board.md` entry with a prompt
  per entity, and naming consumers as a step of its own. **Why:** the procedure
  had become the expensive half of moving a role, in an ecosystem whose own
  register says every role kanon holds is a candidate to leave.
- **`PROTO-26`:** green CI on both sides became advice rather than a
  precondition, because a role transfer is reversible and deleting a stub is
  not. `PROTO-20` is unchanged and still binds the irreversible act.
- **`LAW 3`'s carry-list** stopped naming files. A law that enumerates filenames
  turns an ordinary handoff into an amendment, and that page has no amendment
  process by design. What a successor inherits did not change.
- **`LAW 7`** now names this page as where a change to the laws, the policy or
  the vision is recorded with its reason. It had been read as *recorded beside
  the rule*, which `policy.md`'s present-tense section forbids; that section was
  sharpened in the same pass and cost `policy.md` two restatements to stay under
  `LAW 8`.
- **`LAW 11` was added**, putting a ceiling on this page and saying what earns
  an entry. **Why: four entries landed here in one session, 1,155 words, one of
  them recording a glossary correction.** That entry is gone and this one is
  shorter than the three it replaces.

*Re-derive:*

```sh
git log -p docs/laws.md docs/roles.md docs/protocols.md docs/policy.md
```

### `eo_init` and `eo_join` went to koine — 2026-09-17

**`R35` is a new id rather than a moved one**, because this is a split: `R4`
keeps the policy, the vision, the glossary and the two prompts run from here
against another checkout, and loses only the two commands that run *inside* the
repository being started or joined.

- **Moved:** `prompts/init_eo` and `prompts/join_eo`, deleted here, maintained
  in koine as `eo_init` and `eo_join`.
- **Stayed:** what joining costs, in `policy.md`, with the vision and the
  glossary.
- **Unchanged:** no member's CI, no pin, no requirement in `policy.md`.

**Nothing was lost in the move**, established before the files were deleted
rather than asserted afterwards: koine's copies were byte-identical to them,
modulo the documented rename.

**The risk it bought.** `eo_join` carries about two hundred lines arguing whose
front page a declaration is — a position — and the drafting of it now sits with
a tool that does not hold the position. The guard is that `R4` still holds the
rule those lines state.

**Still owed.** koine's `origin.json`, README and `coherence.md` name kanon as
the authority for these two, and `eo_join --soft` writes onto the README of
whoever runs it a link to a file this repository no longer has. Until koine's
side lands, the pair disagrees about who owns them.

### The bump check went to koine, and the pin became a lock — 2026-09-17

Kanon published `scripts/bump_check.py` *so every member does not write it
separately*, on a page that also said **we do not maintain your bumping**. Both
sentences were in `policy.md` and only one could be true.

koine built `eo_bump` under `R16` after `D14` reported the shape: four
repositories had written the job themselves in three naming conventions, and
five had written nothing. **Kanon deleted its own and adopted theirs** — 171
lines of script, four tests and a loader gone, and `ANOIEU_REV` in the workflow
replaced by `anoieu.lock` with `eo_bump.json` beside it, which is the format
every other lock here already used. **Both files were deleted hours later**,
when this repository moved to anoieu's contract — the entry below. *Re-derive:*
`git log -- anoieu.lock eo_bump.json`.

**What did not change:** the requirement. Moving a pin only onto a commit whose
CI was green is the policy; the program is a convenience and nothing obliges a
member to use koine's.

### The installer and the prompt directory were deleted — 2026-09-17

**The largest deletion of the term, and the only one with no replacement in
place.** `scripts/install_eo`, 762 lines, was deleted on the maintainer's word
that koine is building the replacement — so **this ecosystem has no installer
today**. `scripts/repos.local` is written by hand instead, one `ID PATH` pair
per line, and registering a checkout never changed anybody's membership.

`prompts/` went with it and the directory is gone. `process_discussion` because
koine shipped the replacement, `eo_respond`, and it works from this tree;
`check_join_eo` and `global_audit` because both were assistant wrappers over
commands this repository already runs without one. `scripts/anoieu_dependency.py`
was folded into `scripts/policy_check.py` — locating the checker and running it
were two files for one job — and `status_eo` became `eo_status_audit`, a name
that says what is left here once koine's `eo_status` prints the plain table.

**What it came to.** Eight files and 1,866 lines deleted across the stretch from
`59ed39f^`. The tooling this office carries fell from 24,177 words to 13,325,
against the thirteen files and ~17,500 words `D13` tabled when it asked koine
what a president should have to carry. **The register, the documents and the
decisions stayed**; what left was the machinery that read them.

**What it cost is not all known.** The installer gap is real and was chosen: a
person cloning this ecosystem today has no command to do it with. That is ours
to have chosen and not a debt koine owes us, and `D13` says so to them.

*Re-derive:* `git log --diff-filter=D --name-only 59ed39f^..HEAD` in this
repository.

### `practice.md` was folded into the vision, and LAW 8 lost a page — 2026-09-17

**LAW 8's own table said the split bought nothing**: *splitting a page in two
does not buy room*. The numbers agreed — the vision and what-follows-from-it ran
3,108 and 2,932 words, so the pair fitted inside the 7,000 a single page is
asked to aim at. The page was also defined by its relationship to another page
rather than by a subject, which is what made it hard to say what it was for.

**Two sections had no other home and were carried across, compressed**: how to
write for a reader who is an agent, and who the paper is for. The front-page
layering, the adoption table, the report-card note and the child-project
inventory were dropped — `policy.md` carries the rules they elaborated, and the
register carries the inventory. LAW 8 now covers three pages rather than four.

**What this leaves unfixed.** `policy.md` is 10,243 words and over LAW 8's
ceiling. That is the page with a length problem, and nothing here touched it.

*Re-derive:* `wc -w docs/policy.md docs/vision.md docs/roles.md`.

### The checker contract, and the end of the pin — 2026-09-17

anoieu published a versioned policy-checker contract and a shared CI workflow.
[`policy.md`](policy.md#2-run-the-check) now accepts either form for
membership — a pinned commit, or that shared workflow at a named contract — and
attributes what is not promised about the checker to anoieu instead of
promising it here; the claim that there is *no versioning scheme* was true
until that day and is gone.

**This repository took the contract form**, at the maintainer's direction and
within the hour of permitting it. `.github/workflows/anoieu.yml` calls anoieu's
workflow at `main` asking for contract 1; `anoieu.lock` and `eo_bump.json` are
deleted, so **kanon pins nothing**, the root carries no file but the README, and
`eo_bump` has nothing here to move. The pin it replaced had been moved onto
`154228a` earlier the same day, after `eo_bump` found anoieu's `policy` job
green there.

**What was traded, and what is unverified.** This build can go red with nothing
committed here, which [`vision.md`](vision.md)'s second tenet argues against;
contract 1 holds the obligations still, so a red build means a violation
already in this tree has started being reported rather than a new requirement
arriving. **A called workflow cannot be exercised from a checkout**, so the
first push is what establishes that the job runs and what the check is named —
a third segment is expected, `anoieu / policy / policy`. anoieu and eschaton
asked from both ends and are answered in `D15`.

*Re-derive:* `.github/workflows/anoieu.yml`, and
`git log --diff-filter=D -- anoieu.lock eo_bump.json`.

*Commit note, and delete it whenever it stops helping:* `911c3ca`, "Hk",
carries this day's housekeeping as it stood at 16:23 — the four `associate`
corrections, two command fixes, the budget row, the topics, **and the pin move
that the next commit deletes**. `1e029ef`, "Rm lock", carries the move to the
contract: the workflow, both deleted files, and every page and topic change that
went with them. Neither message describes its contents, so a reader looking for
any of this by subject will not find it under either.

### Two commands were reporting the wrong thing — 2026-09-17

Both were found while answering anoieu's `D28`, which listed four sentences in
this tree still defining `associate` as the footing it stopped being. The
sentences are corrected and the newer reading stands: the footing is recorded
by the repository itself, on its own maintenance page.

- **`--check --online` graded an associate by the wrong page.** It read the
  README for the *affiliating* note — the paragraph saying a repository is
  **not** held to this policy — so `iogos` was reported as a mismatch while its
  `docs/maintenance.md` carried the marker the register records. It reads
  `associate_in` over that page now, as our record going stale rather than
  their shortfall, and `--protocol` reports the marker.
- **The `channel` column under-counted what we are owed.** It counted the
  string `**To:** kanon`, so a notice addressed to several tools at once was
  counted for whichever was named first and a name merely beginning with ours
  counted as ours. Four topics are addressed to us; the table said three.

*Re-derive:* `scripts/eo_status_audit --check --online` and `--protocol`.

### `PROTO-18` was retired and the sleep machinery deleted — 2026-09-17

**At the maintainer's direction, and the reason is itself the finding.** The
sleep protocol bound every member; the program existed only in the president's
tree; a second and by then divergent copy of that program was in epikrisis's
`martyria`; and the argument for having it at all was in `zetesis`. Four pieces
in three trees, and **no reader could assemble how it was supposed to work** —
a defect in the arrangement rather than in any one piece.

Retired in place: [the protocol register](https://github.com/ajreynol/kanon/blob/f2262444e2d9dafa823820103fdaafac7252500a/docs/protocols.md) carries `PROTO-18` with no
protocol behind it, `INST-1` is withdrawn from
[`maintenance.md`](maintenance.md), and `scripts/sleep.py` and
`scripts/schedule.json` are deleted. **Nothing in this ecosystem now binds
anybody to a working window**, and the office no longer ships a program at all
outside `scripts/`'s register readers. epikrisis is told in `D19` and koine,
which had offered to host it as `eo_sleep`, is told in `D18` not to build it.

**What is not settled by this.** Whether an agent should tell a person to stop
working is `zetesis`'s question and stays open there; retiring the mechanism is
not an answer to it.

*Re-derive:* `git log --diff-filter=D -- scripts/sleep.py scripts/schedule.json`.

### The governance budget got its second row — 2026-09-17

Written prose fell 801 lines since the 2026-09-01 baseline while **neither the
check count nor the finding count moved** — the rule kept by deleting pages
rather than by earning them. The table, and the part of it that is not to our
credit, are in [`maintenance.md`](maintenance.md#the-governance-budget).

### Status auditing moved to stathmos — 2026-09-18

At the maintainer's direction, the implementation of `scripts/eo_status_audit`
and its child-listing helper moved into `tools/stathmos/scripts/`. The public command
stays in `scripts/`, so callers and CI use the same entry point. `R37` now
records the audit separately from `R6`, which retains kanon's authoritative
register and installation exceptions. Mechanical checks remain separate from
the human report-card judgements under `R30`. `B31` retains only the notice to
koine that revises the earlier reader-bundle handoff.

The local policy-checker launcher followed into
`tools/stathmos/scripts/policy_check.py` later the same day, also under `R37`.
It locates and runs anoieu's checker; the checking rules remain anoieu's under
`R31`. This supersedes the launcher's location recorded on 2026-09-17.

*Re-derive:* `git log --follow -- tools/stathmos/audits/status_audit.py`, and the
`R6`/`R37` entries in [`roles.md`](roles.md).

The implementations moved from `tools/stathmos/scripts/` to
`tools/stathmos/audits/` on 2026-09-19, so tooling ownership can name stathmos
and measure its layout from the child project's root. Public commands stay in
kanon's `scripts/`.

### Ynoia and stathmos were tied to the presidency — 2026-09-18

The maintainer directed that both projects move with their work and roles to
whichever repository holds the presidency. Their charters and `roles.md` now
say so. This replaces stathmos's proposed destination of a separate repository
and the statement in `laws.md` that its report card does not move with the
office; those passages conflicted with the chosen arrangement.

### The laws were separated from their current implementation — 2026-09-18

At the maintainer's direction, LAW 3 now transfers a role or child project
with the presidency only when its recorded responsibilities or charter say so.
The role register explicitly attaches the current governance roles to the
office, including the protocol register under `R4`; other holders retain their
work until a separate transfer. Policy checking and status auditing follow
their own roles, removing the old blanket exclusion of checking programs from
the office.

LAW 1 now refers membership verification to the accepted methods in policy,
which already permits a pin or a named contract. Tool names, register fields,
command paths, incidental counts and historical details were removed from the
laws; current locations and audit behavior are described in maintenance.
The claim that every repository has one owner became a conditional rule about
shared control. LAW 4 and stathmos's charter now require evidence and disclosed
limits, replacing requirements to produce an unfavorable finding or failure.
The existing word limits remain the stated recommendations.

The displaced succession note is historical: the former LAW 5, requiring the
outgoing president to choose and teach its successor, was removed on
2026-09-14. Selection and vacancy remain unsettled; this pass neither restores
that duty nor changes LAW 7's assignment of the laws to the president.

### The laws received a lighter clarity pass — 2026-09-18

The maintainer rejected a broad rewrite into instructions as excessive. This
pass keeps the prose and structure, trims repetition, and labels important
subclauses with dotted numbers for reference. Obligations, exceptions, advisory
word limits and law numbers are retained; the purpose is to clarify rules
without removing useful explanations.

Current references now link to numbered paragraphs with explicit anchors. Seven further
subdivisions identify the provisions those references need, preserving existing
numbers. `D20` recommends the same approach for future references.
LAW 10's tracking reference now names
LAW 9.4's restriction on work that is neither released nor published; its own
released-tool requirement is unchanged.

The maintainer requested paragraph markers rather than subclause headings.
The existing link targets are retained. Kanon's link tests accept them;
anoieu's heading-only checker reports them as missing headings, a limitation
recorded with the recommendation in `D20`.

### Subclauses were numbered in reading order — 2026-09-18

The maintainer requested sequential numbers and paragraph markers such as
`(3.1)`. Laws 3, 4 and 9 were renumbered without moving or changing their prose;
current references were updated, and old anchors remain aliases for the same
provisions. The earlier restriction cited as LAW 9.4 is now
[LAW 9.5](https://github.com/ajreynol/kanon/blob/19c27232018ee8b3e090f4d7131be1355f4c563f/docs/laws.md#law-95--permission-for-unreleased-and-unpublished-work). `D20` visibly
records the revised recommendation so new subdivisions follow reading order.

Former LAW 11 was condensed into [LAW 4.6](https://github.com/ajreynol/kanon/blob/92ade49b9a39f9a227d262a05354a209627d4da2/docs/laws.md#law-46--recommended-length-of-historymd),
placing the account's length guidance with its other duties.

### The directory outline was clarified — 2026-09-18

At the maintainer's direction, policy now recommends one top-level directory
per self-contained tool or feature outside the directories with defined
purposes. It also applies the same outline relative to each child's root, so
implementation boundaries and file locations remain clear inside `tools/X/`.
`D21` announces the guidance, with anoieu's three tools as an example.

At the maintainer's direction, kanon then applied the outline to its own
children: their documents now live in local `docs/` directories with indexes,
and stathmos's regressions live in its `tests/`. The parent test run still
includes them; public commands and child charters retain their locations.

On 2026-09-19, the maintainer reserved `examples/`, `test/` (alongside `tests/`),
`cmake/` and `include/` for examples, tests, build support and headers. Policy
leaves their contents and organization to each project. The tooling audit
skips these directories so ordinary project support is not an inventory gap;
their explicit exclusions were removed.

The maintainer also reserved `licenses/` on 2026-09-19 for license texts and
notices, so it is skipped as ordinary project support. Ethos's `contrib/`
exclusion was replaced by an entry for its Eunoia formatter, with its shared
directory recorded as an advisory layout gap.

Later on 2026-09-19, the maintainer reserved `contrib/` for manually obtaining
external tools and excluded documentation from the tooling inventory. This
keeps supporting material from being reported as a separate contribution.
The audit rejects `docs/` and `contrib/` contribution directories, including
within child projects. Sapheneia's account and mimesis's case-study documents
were removed from tooling; dedicated tutorials remain listed. The formatter
entry now records eunoia's `eo_format/`, and Ethos's `plugins/` is an ordinary
top-level collection instead of a special entry for its C++ compiler.

### Housekeeping completed after an interruption — 2026-09-18

This entry is reconstructed from `d03447d` ("Hk") and the local source
checkouts while completing that interrupted work.

**The joining instructions now describe koine's two command forms.**
`eo_join` joins; `eo_join --soft` writes the affiliating note and adopts no
policy. Koine withdrew `--associate` and `--affiliated` on 2026-09-18 to reduce
the choice of commands; both flags refuse with an explanation. The independent
disclaimer and associate marker remain available by hand. These edits describe
the command's behavior; they change no footing or membership requirement.
`R35` now describes both accepted checker workflows, and `R16` names the current
shared commands without the history-review tool removed from koine on
2026-09-17. That subject belongs to epikrisis.

**The same commit made the law subclauses headings.** The numbers and rule text
were retained, and the heading-only policy checker can now resolve the current
clause links. This supersedes the paragraph-marker implementation described
above. Completion restores the dropped `#in-limbo` alias so older links still
reach the same provision.

The inventory and glossary record anakrisis and empeiria under paideia after
their move from dokimasia, add tachyon's elaphros, and describe aisthesis's three
documents. Paideia's front page calls it an associate, but its maintenance page
explicitly leaves the marker unrecorded; its candidate listing is unchanged.
Completion also removes the inventory's remaining claim that association is
ours to confer and that the audit reads an affiliating note. It reads the
repository's own maintenance marker. The earlier inventory history is traced
through anoieu's rename as well as its later deletion, so the handoff does not
look like every project's first appearance.

*Re-derive:* `git show d03447d`; koine's `eo_cmd/eo_join`; paideia's
`README.md` and `docs/maintenance.md`; and, in anoieu,
`git log --follow -- scripts/ecosystem/ecosystem.json`.

### The identity protocol was retired and the laws simplified — 2026-09-18

At the maintainer's request, `PROTO-21` and its companion `INST-2` were retired
because the identity header and its repetition rules were confusing. Their
instructions are removed; the ids remain reserved in their tables. Responses
no longer require the identity header or its long form.

The laws' introduction now explains human responsibility directly. The section
called *The same owner loophole* now uses the example of one person controlling
both a tool and its audit to explain why separate repositories do not establish
independent oversight. The standalone *What history.md is, and is not* section
was removed, with its useful guidance placed under LAW 4. The history and letter
requirements were shortened for readability; obligations and clause numbers
remain unchanged, and old section links reach their replacements.

### The law headings and referenced requirements were made explicit — 2026-09-18

At the maintainer's request, LAW 9 now begins *External research*, and headings
throughout name their subjects directly. LAW 6 is one short paragraph, with no
subclauses. LAW 3.2 states the role-transfer requirements directly, and LAW 6
states the limits on humour, removing the need to follow protocol references
to understand those laws. Bold emphasis was removed from the page. Current
references use the new headings and the combined LAW 6; old anchors remain
available. These changes preserve the requirements while making them easier
to find and read.

### The laws use one level of subclauses — 2026-09-18

At the maintainer's request, every law now uses a level-two heading and every
sublaw a level-three heading. Unnumbered headings were removed, with their
content retained in the introduction or the relevant law. General external-work
guidance sits under LAW 9, and reporting limits sit under LAW 10.2. LAW 8.1's
table became prose; LAW 1 keeps the page's only table. The requirements, law
numbers and existing link targets are preserved.

### Definitions were sharpened and history requirements relaxed — 2026-09-18

At the maintainer's request, LAW 1 defines an outsider as an external project
listed for comparison, without proposed membership or obligations. Its second
list of rationales was removed, along with tangents elsewhere about checker
defects, rewards, report cards, publishing speed and fuzzer output. Specialized
terms link to the glossary. The right to leave is now LAW 2.1. These edits
clarify the rules without changing them.

LAW 4 is a rule change: the former 4.1–4.4 become one clause allowing the
president to add, revise or remove history entries freely during its term.
The requirements for a self-contained account, prescribed updates, reproducible
figures, failure analysis and visible, evidenced corrections are removed. The
letter and length provisions become 4.2 and 4.3; shortening the account no
longer has a separate evidence-preservation requirement. Custody of the history
and letter, and the protection of a predecessor's account, are unchanged.
This page and the historian role no longer restate the removed requirements.
Earlier examples citing them point to revision `92ade49`.

LAW 7 now explicitly assigns maintenance of the laws to the president for the
current arrangement and allows that responsibility to be reassigned. No role
has changed holder. The amendment-recording requirement remains in place.

### Document paths and current checking roles were clarified — 2026-09-18

At the maintainer's request, the laws now show repository-relative document
paths and link directly to kanon's copies, including `docs/history.md`.
LAW 3.3 names anoieu as the current policy-checker holder and stathmos as the
current status-audit holder, linking to their role entries. These clarifications
make the referenced files and responsibilities easier to find; no rules or
holders changed.

### Unpublished external work is treated as private — 2026-09-18

At the maintainer's request, LAW 9.2 now prohibits inspecting or tracking
released work without published research: public access is not permission to
examine it. This is a rule change, removing the previous permission to read
documentation and measure activity. LAW 9.3 applies the same restriction when
publication is unknown. LAW 10.1 no longer permits defect investigations
regardless of publication.

The inventory guidance and audit comments now match. The status audit skips
outsiders with absent or unknown publication before locating or reading their
checkouts; a regression checks that those reads cannot occur.

The maintainer also removed the redundant glossary entry for "candidate laws";
the phrase remains plain text in the laws' introduction.

### Presidential document tenets were gathered under LAW 5 — 2026-09-18

At the maintainer's request, LAW 5 now begins *Presidential tenets* and names
the shared documents the president maintains. This makes the existing document
responsibilities explicit without changing their holders or transfer terms.
The authoritative record of who holds the office belongs with appointment
and succession, so that text moved to LAW 3. LAW 5.1 still covers limbo.

LAW 8's conciseness guidance is now LAW 5.2, keeping the same recommended word
limits and scope. LAW 8 remains an empty placeholder; Laws 9 and 10 keep their
numbers. The policy links to LAW 5.2, and old anchors reach the moved text.

### LAW 5's scope was separated from the laws — 2026-09-18

At the maintainer's request, LAW 5 covers the listed shared documents and
does not depend on LAW 7 or govern the laws themselves. Limbo moved to LAW 3.4,
with current links updated and old anchors preserved. LAW 5.1 now names the
documents to maintain; the guidance on the laws' own length moved to LAW 7.

The maintainer also removed LAW 7.2 as overly procedural. Its requirement
to preserve outcomes and distinguish rule changes from editorial rewrites,
including the shortening requirement in LAW 5.2, is removed. LAW 7.1 still
requires amendments to be recorded with their reasons.

Links from the laws to the role register were removed at the maintainer's
request. Anoieu and stathmos now link directly to their project roots.

### LAW 8 now covers Eunoia's research boundaries — 2026-09-18

At the maintainer's request, LAW 8 replaces its placeholder with a broad rule
about what Eunoia does not research. It names aisthesis as the current holder
of that account and links to its repository. The wording deliberately leaves
the boundaries with aisthesis rather than enumerating them in the laws.

### Tracking was defined in the glossary — 2026-09-18

At the maintainer's request, the glossary now defines tracking, with epikrisis's
repository histories and commit activity as an example. LAW 9 links to the
definition and keeps its existing limits on tracking external projects.

### Defect investigations use tracking's eligibility rules — 2026-09-18

At the maintainer's request, LAW 10 now permits targeting an external repository
whenever LAW 9 permits tracking it, under the same conditions. This removes
the separate released-and-published prerequisite and includes LAW 9.5's
permission exception. The introduction is shorter; declaration, reporting and
ending requirements remain. The inventory guidance uses the same eligibility.

### Laws 5.2 and 10.2 were shortened — 2026-09-18

At the maintainer's request, LAW 5.2 now states its recommended word limits,
scope and requirement to justify added rules in two short paragraphs. The
detailed editing advice was reduced to cutting repetition and unnecessary
explanation. LAW 10.2 now delegates reporting and publication to anoieu's
reporting policy, removing its separate maintainer-first publication rule and
reporting restrictions. Existing section links still resolve.

### The revised LAW 9 received sublaw markers — 2026-09-18

The maintainer's revised points are numbered LAW 9.1–9.6 in reading order.
Grammar and formatting were polished without changing their substance. The
unknown-publication clause and glossary now reference the matching sublaws;
the historical link to the earlier permission rule names its recorded revision.
LAW 9.6 explicitly connects unknown publication status to the inventory's
`published` field, which records the publication required by LAW 9.2.

### Outsider exceptions and private investigations were clarified — 2026-09-18

At the maintainer's request, projects with unknown publication stay out of the
register unless their owners volunteer them. The exception is recorded in
`volunteered` with a date, owner and evidence; `released` and `published` still
record the actual facts. The audit validates the offer's form and honors it
before reading a checkout. Tests cover ordinary eligibility, volunteered
exceptions, missing facts and malformed offers.

The maintainer added LAW 10.3 reserving private continuation after a stop
request. LAW 10.2 now ends public reporting and further contact, resolving its
earlier prohibition on continuing quietly. Private work remains subject to
LAW 9. The glossary, inventory guidance and section references now agree.

### The numbered protocol system was retired — 2026-09-18

At the maintainer's request, the `PROTO-*` catalogue and `docs/protocols.md`
were removed. The page contained 7,181 words, largely duplicating rules or
turning ordinary collaboration into named procedures. All allocated protocol
ids are retired and will not be reused; the
[previous register](https://github.com/ajreynol/kanon/blob/f2262444e2d9dafa823820103fdaafac7252500a/docs/protocols.md)
preserves their definitions.

Stub replacement requirements now sit in the policy's handoff section.
Project registration and brief guidance for working with an agent sit in the
maintenance guide. Joining and discussion remain in policy, role transfers in
the laws and role register, humour in LAW 6, research boundaries in LAW 8, and
report-card updates in stathmos. Anoieu retains its reporting workflow.

Mandatory protocol announcements, session reminders, approval blocks and the
document-promotion scheme are removed. The useful requirements to stop on
request, preserve Git history during rollback and report evidence remain in
ordinary prose. Current indexes and ownership descriptions no longer name the
deleted page; historical references name its recorded revision.

### FAQ guidance was withdrawn and board instructions shortened — 2026-09-18

At the maintainer's request, the policy's front-page FAQ recommendation and
board item `B26` were removed: whether a FAQ helps is an editorial judgement
for each repository. The board's maintenance advice was condensed to ordering,
stable ids, the active-item cap, fields, delivery and closure. Repeated
explanations and the stale handoff example were removed.

### Human-maintainer attribution was centralized — 2026-09-19

At the maintainer's request, policy defines the ecosystem's human maintainers
and records their current list in one place. Ownership statements must link
there rather than repeat personal names, handles or affiliations, so a change
in responsibility does not leave stale attribution across repository READMEs.
The maintenance-note examples and kanon's README use that link. The list can
change by human decision; the text no longer assumes one maintainer forever.
The new link requirement is not yet enforced by the policy checker.

### Productive entities received a common requirement — 2026-09-19

At the maintainer's request, LAW 11 requires a recorded basis for each
ecosystem entity: a deliverable in the tooling audit, a purposeful reference
in the laws, policy or vision, or a current assigned special role. The
maintainer defined entities as presidents, members and children; the other
footings remain outside this requirement. Children are considered separately,
including those not advertised by their parent.

This adds a common requirement where the register previously recorded a
project's footing without requiring one of these reasons for its place.
Policy and the glossary link to the law. At the maintainer's further request,
the status audit now reports productivity from the tooling audit's local
availability results, project links in the three central documents and current
role assignments. The `moved` and `channel` columns were also removed at the
maintainer's request. Verbose output names the evidence; a person still reviews
the purpose stated by a reference. Unavailable evidence is unverified,
and the report does not change membership or add a CI gate. The old LAW 11
anchor for history length still resolves to that guidance under LAW 4.3.

### Twenty-two topics were worked, three replies written, two commands found broken — 2026-09-18

**The discussion work, and the mistake in how it was first done.** Every topic
in another tool's tree whose `To:` names kanon was read — twenty-two, across
eight repositories — and the first attempt answered them in **six bundled
topics, 619 lines**, more than doubling `discussion.md`. **That was a misreading
of this file's own rules**, caught by the maintainer: the policy says
`eo_respond` works *the one topic*, that an `answer` gets its own topic
**because it needs room**, and that the file holds **live** discussions. Six
topics bundling two to seven answers each, most born finished, are none of those.

**The test that replaced it: read the settling condition.** Most topics
addressed to us settle on an artifact — *the role register names
`scripts/install_eo`*, *the two entries link to charters that resolve*.
**Where the artifact exists, the artifact is the answer and no topic is
written.** Only where a condition asks us to *say* something — *or the ecosystem
says deliberately that it does not want one* — is a topic the only vehicle.
That left **three, 109 lines**: `D22`, a notice that status auditing is
stathmos's; `D23`, the six statements eudaimonia's topics asked for; `D24`,
declining `anoieu-D30`'s second ask with a measurement. One further answer moved
into [the policy](policy.md#child-projects), where eudaimonia had asked for it.

**Six topics of ours were removed as finished** — `D3`, `D4`, `D5`, `D9`, `D12`
and `D16`, each settled by the other side. `D15` and `D21` gained replies rather
than being rewritten, which is the mechanism the file already had.

**Three of the twenty-two were withdrawn by their authors the same day**, so
nineteen stand: aisthesis retracted `D2` and `D3` in `71a6f9b`, rewriting
`recommendations.md` as hypothetical; dokimasia removed `D11`.

**Four questions were declined rather than decided**, and that is the part worth
reviewing: whether citing a child project in the parent's channel advertises it;
whether `vision.md` must record why it changed; whether three status transitions
become fields; whether the misaddressed-prompt check joins the fatal gate. The
first changes what an unadvertised child is *for*, the second is first on the
supervision ladder where an agent's agreement is not evidence, the third is a
schema change to a register no script writes. All four are on the board.

**Two commands were broken and nothing said so**, described under
[what went wrong](#what-went-wrong). `eo_status_audit --protocol` raised
`AttributeError` instead of printing its table, and `--check --online` would
have done the same. **Stathmos's loader now looks for anoieu's declaration
readers by name across the layouts they have lived in**, held by two regression
tests, one of which fails against the old loader.

**The joining section names the minimal passing tree, measured rather than
asserted**: one README and one workflow file, `0 failure(s), 14 skipped` at
contract 1. `anoieu-D30` also asked us to say the discussion file is in the
joining set; **it is not**, and anoieu's own conditional-skip fix is what took
it out.

**A new child was recorded: `ydoki`, dokimasia's.** The maintainer started it
the same day; the register and [the glossary](glossary.md) now carry it, and the
audit reads its own `unadvertised-child` marker, so it appears under
`--all-children` and not in the default table. **Its name is a recorded
exception rather than a slip**: the policy asks a child for a Greek name that
describes its work, and `ydoki` is formed from δοκιμασία the way `ynoia` is
formed from εὔνοια. Writing a strained Greek etymology to satisfy the rule would
have been the worse answer, since the rule exists because a strained explanation
means the scope has not been decided — and the scope is decided. **A sweep of
every tree's `tools/` against the register found nothing else unrecorded**, and
the glossary already agreed with the register on all 42 projects.

**In the child projects.** Ynoia's `tools.md` carried `iogos` as a tool that
does not exist; it is a repository, and the page's own rule says a tool leaves
when it exists. **Nothing was written into ynoia's registers**: aisthesis's six
recommendations were drafted in and a reply drafted as `D27`, the maintainer
withdrew all of it, and aisthesis then retracted the request. **`D27` is spent
and will not be reused** — it never reached a commit, so this sentence is the
only record it existed. One defect survives the retraction: six of the eight ids
in ynoia's `requests.md` collide with ids in `roles.md`, which is `B41`.
Sapheneia's ledger was rechecked against ethos `21fc6c7d` — `EOM-01` and
`EOM-02` fixed, six standing with evidence, seven marked unchecked rather than
re-confirmed, because confirming a judgement by grep is inflation. Stathmos's
report card had two claims about epikrisis that had gone false; the graded
paragraph stands with a dated note under it rather than rewritten.

**What was corrected in the shared pages.** The policy said both that we check
an associate anyway and that nothing runs against one; it now says the one
thing both halves meant. `roles.md` named `install_eo_cmd`, said koine's
manifest files every installed command under `R35`, and described
`eo_housekeeping` as a reporter; all three are corrected against koine's tree.

**And this page is now about 11,200 words, against the 10,000 that LAW 4.3
recommends.** It was already over before this entry, by roughly 200. The law
says excess length is not a violation and must not fail a build, which is
correct and is also how a page gets to 12,000 — so the number is recorded here
rather than left to be noticed. What would bring it down is deleting closed
entries under *what crosses to the next president*, and that is a judgement
about what mattered this term, which the next reader is better placed to make
than the author of the entries.

## Membership changes during this term

Each row names the commit in the joining repository's **own** tree where the
declaration landed, the commit here where the register caught up, and the
commit of the repository that held the shared policy at that moment — which is
the coordinate the register keeps in its `joined` field.

| when | tool | change | declared, in their tree | recorded, here | policy at the time |
| --- | --- | --- | --- | --- | --- |
| 2026-09-15 16:15 | `kanon` | member → president | — | `7eb9973` | — |
| 2026-09-16 05:23 | `tachyon` | not in the register → member | `cbd8eb2` | `226d534`, 06:32 | `kanon 4c4a78a` |
| 2026-09-16 06:24 | `eschaton` | not in the register → candidate | — | `2a6aac1` | — |
| 2026-09-16 07:02 | `eschaton` | candidate → member | `50c780d` | `0c507d9`, 07:22 | `kanon c95ab21` |
| 2026-09-18 15:31 | `paideia` | candidate → member | `864666f` | working tree | `kanon 4165736` |
| 2026-09-19 07:35 | `eunoia` | not in the register → member | `302af2c` | working tree | `kanon 4d16d1b` |

**No repository left, and no footing was withdrawn.**

**Paideia's stale candidate entry was corrected on 2026-09-19.** At the
maintainer's request, the register and glossary were checked against paideia
at `8240ce9`. Commit `864666f` had added the front-page membership declaration
and anoieu's shared policy workflow with contract 1 on 2026-09-18. The local
policy check passes; the candidate rationale described the tree before that
declaration. The recorded policy coordinate is kanon's tip when it joined,
not the checker version or the tip when this correction was made.

**Eunoia's handoff, read at `302af2c` on 2026-09-19.** At the maintainer's
request, mimesis's parent changed from eudaimonia to eunoia and sapheneia's
from kanon to eunoia; both keep their `tools/<name>` paths and child footings.
The tooling inventory records their tutorials, case studies and language
account as artifacts. Eunoia declares membership and configures policy
contract 1. The local checker reports one failing check affecting both
children: their front-page advertisement lacks charter exception statements.

**The first row is the office moving; the rest record repositories' footings.**
It is on the same table because the presidency is a footing in the
same register and moves by the same act — a person editing one line — and a
membership record that omitted the one change kanon made to its own row would
be the page's most obvious blind spot.

*Re-derive:* in the joining repository, `git log -S'part of the **Eunoia
ecosystem**' -- README.md` gives the declaration commit and its date. Here,
`git log -S'"tachyon"' -- scripts/ecosystem/ecosystem.json` gives when the
register first carried that tool, and `git log -p` on the same file gives every
change to its footing. The policy commit is this repository's tip at the moment
the declaration landed, from `git log --format='%h %cI'`.

**Joins before this term are not here**, because this page is an account of
this term. Seven repositories were already on a membership footing when it
opened — six members, one of them kanon, and anoieu holding the office — and
every one of them joined while anoieu kept the policy. Six of their entries
carry an `anoieu` commit for the same reason the rows above carry a `kanon`
one; anoieu's own carries nothing, because that join was never recorded at the
time. anoieu's account covers that stretch, and this page does not restate it.

## The record, field by field

**Purpose** — *proposed, not settled:* taking weight off anoieu. The stretch's
three-word heading is owed, and the candidates are **Distribution**, **Out of
anoieu** and **Fast answers**. A person picks.

**Span** — opened above, and not ended.

**Membership** — the table above, and `scripts/eo_status_audit` for the current count
rather than a figure quoted from this page.

**Commits** — **not available, and kanon will not compute it.** LAW 4 gives the
census to epikrisis and forbids the president from producing its own. If
nothing arrives, this field will say *the figure does not exist* rather than
carry an estimate kanon made about itself.

**What is now true** — owed. What the term changed about the register is above;
what it changed about anything else belongs here, and it is empty because
nothing has been established rather than because nothing happened.

**What is handed on** — [below](#what-crosses-to-the-next-president), kept
current.

**Government model** — *expected, and to be replaced by what is actually
executed:* one office, **bestowed**, no election, and no mechanism to remove a
holder. Laws written by a different repository than the one they bind, which is
the first real separation and arrives by the office moving rather than by
design. **The only real check remains the maintainer.**

**Evidence** — source references and reproduction commands accompany the
entries that use them.

**The joke** — on the front page for the whole term, per
[LAW 6](laws.md#law-6--presidency-a-readme-joke-about-the-repositorys-name): what kanon sends is a
**kanon-ball**. It doubles as description, which is the test it has
to pass.

**To the next president** — not yet. Written last, and positively, per the
rule.

## What went wrong

**Three things before the term began.** kanon opened six offices in an
afternoon and could not explain four of them; produced tens of kilobytes of
prose and no code on its first day, against a governance budget that already
existed and that it duplicated with a private measure of its own; and reached,
several hours late and believing it new, a criticism another tool had already
recorded from outside. The offices were judged premature the same day, their
directories removed and their reasoning retained in [the brainstorming
notes](misc/brainstorm-offices.md).

**This page arrived about fifteen hours late.** The registry recorded kanon as
president at 16:15:45 on 2026-09-15; this page landed at about 07:30 the next
morning. In between, the tree could not hold the office — a named state, the
registry saying a repository is president while its tree does not carry the
files the office is kept in. One of the two was there from the start: the same
commit that moved the office carried `laws.md` and the check that reports the
state, so `../scripts/eo_status_audit` printed it against kanon's row for the whole
fifteen hours, correctly, and this page was the only thing missing. It is
supposed to be fixed quickly. Fifteen hours is not quickly, and past some point
the honest repair stops being to write the account and becomes to put the
registry line back.

**Both joins were recorded after the fact rather than as they happened.**
tachyon declared at 05:23 and the register moved at 06:32, sixty-nine minutes
later. eschaton declared at 07:02 and the register moved at 07:22, twenty
minutes later. Neither lag did any damage, and neither was noticed by anybody
reading: eschaton's was found by `../scripts/eo_status_audit --check --online`, which
reads each member's front page and fails when the register disagrees with it.
**That is the check working and the habit not**, and the check is the weaker of
the two, because it only ever runs when somebody runs it.

**A dependency reorganized and two of our commands went dark without a
failure.** The readers stathmos imports from anoieu's checker are an interface
with importers outside anoieu's tree, and they are not in the file the command
lives at. When the two were separated, `getattr(policy_check, "associate_in",
None)` returned `None` and the audit reported *this checker cannot read an
associate's footing marker; a newer anoieu can* — **a guard written for an
older checker, firing on a newer one, and saying the opposite of what was
true.** The `--protocol` path had no guard and crashed. Nothing on either side
checks that a launcher and its readers have not come apart, which is the same
class as the cross-repository link nothing resolves: it fails silently until
somebody runs the one thing that used it. Found 2026-09-18, by running every
flag of the command rather than by any check.

**The register is hand-maintained, and that is the design.** A footing is a
decision rather than a fact about a tree, so nothing derives this file and
nothing ever should. The cost is exactly the lag above, and the only mitigation
is somebody running the check.

## What crosses to the next president

**Kept current as things are found rather than written at the close.** *Nothing
yet* is an answer; an omitted heading is not.

**Pinned, never copied.** The successor cites `kanon <commit>` and reads it
there — the coordinate `ecosystem.json` already uses for a member's join.
**None of it binds them.** Evidence, not instruction: a predecessor that could
bind would be governing after its term.

### Established

**Update, 2026-09-15:** the maintainer deferred the internal offices as
premature. Their six documents are retained in
[brainstorm-offices.md](misc/brainstorm-offices.md), and the completed handoff
(`7eb9973`, 2026-09-15) uses `tools/<project>/` directly, superseding the
office destinations below. Governance documents, inventory, scripts and five
child projects arrived. The policy checker, report card and earlier term
history remain in anoieu. The earlier findings below record the state when they
were made.

**About kanon's standing**

- **Six documents in anoieu describe kanon and no two agree.** `names.md`, the
  stub, `ecosystem.json`, `roles.md`, `history.md`, `laws.md`. *Re-derive:*
  `grep -ri kanon docs/ tools/` in anoieu at `579aae7`.
- **`ecosystem.json` has no row for kanon at all.** The office is being handed
  to an entity the inventory cannot see. Not decided — not noticed.
- **kanon is `unknown` and that is not a pass.** This repository runs nothing.
  anoieu is green: ten consecutive runs on 2026-09-02, ending a streak of 112.

**About where the ecosystem's weight sits**

- **Fifteen of twenty-eight roles are in anoieu's tree**, eight direct and
  seven across its children. *Re-derive:* the *How many each holds* table in
  `roles.md`. **Twenty-one of twenty-two board items name it** (`S4`, quoted in
  `history.md`). - **`R28` sits in the busiest tree while `E1` is blocked.**
  The role that moves a stretch to `deployed` is held by the tree with least
  room to run it, and `E1` has been `planned` for a whole term. - **`martyria`
  and `zetesis` are child projects of the repository whose conduct they
  assess** — anoieu's own words. The `P2` defect in the ethics half. -
  **`ynoia` held five roles and five registers**, more than any other child
  project. Two were put down: the account of the arrangement stopped being a
  role, and the register of tools that do not exist folded into the register of
  names, which it was a second view of. Three remain. - **The register of names
  has a live consumer.** `roles.md` called it *the one thing here another
  script already depends on* — `init_eo` reads `names.md` when a repository is
  started.

**About how slowly this ecosystem answers**

- **Three members declared at 10:53, 12:41 and 12:50; the inventory recorded
  all three at 16:44.** `D1` stayed open an entire term. *Re-derive:*
  `history.md`'s entering table and the topic dates in `discussion.md`.
- **epikrisis holds *independent audit* in `laws.md` and appears never to have
  been told.** It had asked for a responsibility rather than a rank.
- **kanon cannot be reached.** No channel, no footing, no inventory row.
- **A layout change already cost other trees.** anoieu moved `prompts/` out of
  `scripts/`; members had copied the layout; two published URLs 404 and the
  copies sent could not be recalled. *Re-derive:* `history.md` under what is
  unfinished, and `D19`.
- **Nothing records what a tool can be asked for**, only what it is. epikrisis
  held *independent audit* through a whole term that nobody could ask it for.

**About the conduct of this office**

- **kanon took the presidency one message after arguing the governance layer
  had outgrown what it governs**, and then grew its own by 10 KB in an
  afternoon with no code. Baseline at the correction: **markdown only, zero
  code files.**
- **The same-owner loophole, both halves.** One owner is what makes the handoff
  safe and what stops it counting as a separation.

- **`ai-novelty.md` exists, is unowned, and is 26 KB.** `docs/misc/` in anoieu
  holds it with `linker.md` and `methodology.md`, and **no role in `roles.md`
  covers any of the three.**
- **Kanon's central criticism was not new.** `ai-novelty.md` already records
  that the sharpest outside criticism of this ecosystem is that *the quality of
  its self-criticism has been functioning as a substitute for the work*, and
  that the page itself is the worst offender. Kanon reached it later and
  independently.
- **`INST-4` is proposed and, unlike the others, has a home.** *Read a primed
  repository in full before proceeding.* `maintenance.md` already holds the
  other `INST-n` ids, and the agent-facing half is the `Closed` heading here.
- **Three rules now have nowhere to live**: the office-count range, the
  empty-president tenet, and the suggestion to the next term. `laws.md` governs
  `history.md` and nothing else by its own statement, so the ecosystem has a
  place for rules about a president's **record** and none for rules about its
  **work**. [`D7`](discussion.md) carries all three outward.
- **A governance budget already exists** in [`maintenance.md`](maintenance.md),
  and kanon's own docs-flat measure was a private duplicate of it, since
  dropped.

- **`telos` is running and is in no register.** A child project with its own
  `docs/`, big enough to throw twenty-two spurious link failures in `D6`,
  absent from `ecosystem.json` and `names.md` alike. **Third instance** after
  `noesis` and `epikrisis`. **`cvc6` appears nowhere in anoieu at all.**
- **Five readings of what Eunoia is, across three trees.** `ethos`'s `R10`
  checker and `R11` manual, `ethos-eoc`, `noesis`, and `pathos` reserved and
  unbuilt — and two of the three trees have joined nothing.

- **`policy_check.py` runs in three members' CI, fetched by URL at a pinned
  commit**, and `P2` hands it to kanon. The president would own the one
  artifact that executes inside everybody else's build.
- **`maintenance.md` says `science-fiction.md` stays in anoieu**, in the
  sentence calling it a safety job. The maintainer has directed it elsewhere,
  and the reversal is recorded rather than resolved.

- **Four failure modes, all already instanced by accident**: misinterpretation
  (three live documentation contradictions), deadlock (the stub deadline, the
  vacant record, the pins the gate refuses), misappropriation (our own record
  says a human wrote all 323 commits and that is not what happened), and
  exhaustion. Written up in [the safety
  scenarios](misc/brainstorm-offices.md#scenarios).
- **The ownership stance protects legibility, not ownership.** No accounts, no
  signatures, no chain of custody — deliberately. What defends provenance here
  is that the record is public and re-derivable, **which holds only while the
  build history stays comparable.**

- **Five failure modes now**, obfuscation added: reading the corpus does not
  produce understanding. **It is the mode that disables detection of the
  others** — a corpus nobody understands cannot be checked for the
  contradictions mode 1 depends on being findable. **kanon is the worst current
  offender**, having invented two id namespaces in a day.
- **Unfriendliness silently disables controls.** epikrisis held *independent
  audit* for a term and nobody could ask it; the audit never ran and nothing
  went red. That is why *all tools should evolve to be user friendly* is a
  safety requirement rather than a courtesy.

- **Jokes here are found in names, not written for them.** `anoieu`, `kanon`
  and `iogos` are all operations on their own names whose results describe the
  work, and all three are at their own expense. **A name that yields no joke is
  probably a name that decorates rather than describes** — which makes LAW 6 a
  test of the name as much as an obligation on the president. Written for the
  next president, in [the
  history](history.md#what-the-next-term-should-be-for).

- **The role numbering runs to `R30` with two meaningful gaps.** `R26` is
  **reserved** for koine pending `D8`, not free — *an id claimed in a proposal
  nobody has answered is not free*. `R27` was **deleted**: it was *deciding
  what a stretch is for*, allocated to anoieu **in error**, on the ground that
  this *is not a role here at all — it is the human's*. Counting headings
  misses both.
- **`maintenance.md` still lists `R27` as moving to kanon.** A page promising
  this repository a role that no longer exists. Fourth documentation
  contradiction, first one about us.
- **Twenty-eight roles exist and kanon holds none of them.** Offices are this
  repository's internal structure; roles are the ecosystem's accountability,
  and only the first has been built.
- **The commit census depends on a figure no role produces.** Assigned by LAW 4
  to a tool that holds zero roles, is in no register, and lives two levels down
  in another member's tree. `D20` is open and names two jobs bundled as one:
  the measurement (epikrisis's) and **the convention that would make it
  possible, which is nobody's and has no reserved name.**

### Open

- **Why does one fact about one tool live in six places?** Larger than any
  single correction. `tekmerion` is the tool for it, holds no roles, has
  produced nothing.
- **Do `noesis` and `ethos-eoc` expect to converge, or is one the replacement
  for the other?** Both are *Started*; neither entry says.
- **Should presidents be required to start from empty repositories?** The
  maintainer's intuition, and it conflicts with `P2` — governance living with a
  president that must start empty means the shared machinery migrates every
  term. The verdict on it is ynoia's.
- **Is kanon's own required reading already too long?** Probably yes. [LAW
  8](laws.md) now gives the two pages a length to stay under, and the remedy is
  diagnosed rather than applied in the same breath.
- **What is a good latency?** No target exists, so *slow* is an impression.
- **Who ends the ethics defect?** Settled that `martyria` and `zetesis` come
  here. Not settled that kanon is then the tree they sit in.
- **Was accepting the office right?** Cannot be answered from inside the term
  by the party that accepted.
- **What is the smallest check that can actually go red?**

### Closed

**Three more went, and one merged.** *The shared prompt-drift check awaits
adoption* named no kanon entity and was anoieu's, dokimasia's and koine's to
settle — **and dropping it overrides an earlier `HUMAN FEEDBACK` that raised it
to the top**, which is recorded here because the board says that field outranks
every other, so overriding it should be visible rather than quiet. *The
office's messages have no way to be delivered* described the design as a
defect: **the delivery mechanism is a person**, deliberately, and the messages
now sit as topics where a person can carry them. *A child project has fifteen
candidates and no route out* was the same mistake — a ledger waiting on a
person is the child-project rule that nothing leaves the island by machine,
working as written rather than a blockage — so the two rows in it that are
checkable by reading the sentence they cite are staged as a topic to ethos, and
the other thirteen stay in the ledger where they belong. *An ethics we can be
held to* merged into the item about where the ethics projects sit: one person
holds both halves, and two rows made it look like two decisions.


**Three more board items removed, and two of them were already dead.** *Nobody
has measured how long an answer takes* duplicated the topic that asks koine the
same question, and the front-page claim it existed to back — that latency, not
willingness, is what constrains every handoff — is no longer on the front page.
*Stretch 1's figures are quoted here and checked by nobody* rested on a premise
that has stopped being true: **kanon quotes no Stretch 1 figures anywhere**, so
there is nothing left to re-derive. The third, *there is no way to find out
what a tool can be asked for*, was unowned and needed each tool's own answer
rather than ours about them.

**And a fourth, which was simply wrong.** *A tool is running and is in no
register* complained that `telos` was missing. **It is in the register** — a
child of `eschaton`, with its path and its purpose — and the reason it does not
appear in the default view is that its own README declares `**Eunoia listing:**
unadvertised`, which is its parent's choice and is the policy working exactly
as written. An item that had gone false is worse than one nobody will act on.


**Eight board items and two topics removed, and the reason is the same one.**
The office inherited work in the governance handoff that was never its own:
board items whose whole content was a finding id from anoieu's ledger — ids
that **resolve nowhere in this tree**, so a reader here could not find out what
any of them meant. They are handed back as `D11`. Two discussion topics went
with them: one addressed to anoieu about `ynoia`, which is kanon's child now
and so is our own work rather than a topic; and one that duplicated two thirds
of a later, broader topic to the same recipient.


**Three board items removed, and the board's own rule is why**: an item that is
done, or that nobody will act on, is deleted rather than archived.

- **Governance out of the analyzer — done.** The move landed; what survived it
  is the single question of how a checker pin identifies the policy version it
  implements, and that already has a home in [`policy.md`](policy.md) and the
  role register. A board item for it was a third copy of one open choice.
- **Joining costs eighteen hundred lines of reading — split, not dropped.** The
  defect on our own side is now the board's front-page FAQ item, and the ask to
  koine — *what would the number have to be* — is a topic in
  [`discussion.md`](discussion.md). One complaint was being tracked in three
  places.
- **Fifteen checks with no witness — nobody is blocked on it**, by its own
  status, and it is internal to a single tool that keeps its own board. It was
  on this one because this one used to be the only board.


**The office's own work list is folded into the normal channels.** What kanon
was waiting on was kept in a register of its own, in parallel with the board
and the discussion file, which is the duplication [`policy.md`](policy.md)
warns about: two registers, two id spaces, and nothing comparing them. The live
items are now board items `B24`–`B30` and topic `D2`. The rest closed, and are
recorded here because a successor with fresh eyes re-raises dead questions.

- **kanon's footing — settled.** The register records it as president; joining
  is what produced the footing rather than something asked for alongside it.
- **Make kanon run something and report on it — done.** It runs the register
  validator, the installer, the policy checker and its own regression suite, in
  CI.
- **Join the ecosystem — done.** The declaration is on the front page and the
  checker passes against it.
- **Receive `ynoia`, `martyria`, `zetesis` and the other child projects —
  done**, with their role ids unchanged, and `martyria`'s cases carried across
  intact.
- **`roles.md` and `names.md` said kanon had no repository — corrected**, and
  `init_eo` reads the register at its current address.
- **The office structure — deferred, and that is the answer**, not a pending
  decision. Incoming projects sit directly under `tools/`.
- **`synkrisis` — never started.** The name was proposed and not claimed, and
  claiming one is a person's act. The reasoning is in [the brainstorming
  notes](misc/brainstorm-offices.md#synkrisis).
- **`ai-novelty.md` and `science-fiction.md` — not ours.** Neither is in this
  tree and the pairing question belongs to whoever holds them.
- **Nobody scrutinised kanon before it took the office.** *That was the
  finding, and it stays a finding rather than a task* — the office is held, and
  the scrutiny that matters now is of what this tree publishes.
- **A private scorecard for kanon's own documents — dropped.** It duplicated a
  governance budget that already existed.

**Four items closed because the register that answers them already exists.**
The succession gaps — how a president is chosen, what happens when nobody holds
the office, where the record of who joined lives, and the commit census nobody
can compute — are recorded in [`laws.md`](laws.md) under *What these laws do
not settle*, which is their home. **Recording a gap twice is how two pages
start disagreeing about it.** The required-reading budget is likewise [LAW
8](laws.md) and the front page's own size, not a task.


- **Whether `dokimasia` should vet kanon — no, and the reasoning is the useful
  part.** `dokimasia` is locally scoped to cvc5 and should run fast without
  reaching for higher abstractions. The first draft of the message to it asked
  it to lift itself to the ecosystem's level **on the strength of its name
  rather than its work**, which is the characteristic error of this office.
  **The mission has a mirror**: no tool should be made to hold what it should
  not. *Do not reopen by reading a tool's etymology.*

- **Earlier destination for `ynoia` — superseded on 2026-09-15.** The
  research-office nesting is withdrawn; the draft now uses `tools/ynoia/`. It
  brings its roles with their ids unchanged. **Kanon inherits its own
  auditor**: `proposals.md` holds `P2`, which recommended this repository
  exist, so this office must never answer *was kanon a good idea*.
- **The three-to-five office range — deferred on 2026-09-15.** It was kanon's
  practice, and is proposed outward in [`D7`](discussion.md); it no longer
  binds kanon. The reasoning is retained in [the brainstorming
  notes](misc/brainstorm-offices.md#earlier-structure-proposal).
- **Six offices — no, two.** *Closed the day it was opened.* Four of the six
  were a status, a list, an output and a mission wearing directories. Corrected
  by the maintainer, who could not tell what four of them were for, which was
  the evidence. **Nothing was deleted except containers.**
- **Whether `martyria` and `zetesis` come here — yes.** *This said no for about
  an hour.* Argued against on the ground that an office expires with the term;
  answered rather than overruled — an office does not travel, what it holds
  does. The unanswered half stands: it relocates the defect.
- **Whether kanon builds communication machinery — no.** `koine` is the one
  implementation of the reporting protocol and is a member.
- **Whether to file an acceptance document — no.** `PROTO-20` reads
  repositories, not messages.

### In flight

- The office's messages are staged as topics in
  [`discussion.md`](discussion.md) and none has been carried. Carrying one is a
  person's.
- Everything open on [the board](board.md), which is where this office's work
  is now kept.

## What the next term should be for

**A suggestion, and it binds nothing.** The successor owes no response, no
adoption and no explanation for ignoring it — a predecessor whose page binds is
governing after its term. It is kept current while the reasons are still
checkable rather than assembled at the close, for the same reason the rest of
this page is.

**Reasons, not conclusions**, and the reason that rule exists is specific to
this ecosystem: if a president starts from an empty repository, every reader of
this section arrives with no work, no history and no standing to push back,
facing a considered agenda from the only party who has walked the ground.
**This section is at its most dangerous exactly under the condition that makes
it useful.** A conclusion is hard for an empty successor to refuse; a reason
can be checked against the tree by somebody who has done nothing yet.

1. **If this stretch ends with balls unfired, the next one is the channel and
   nothing else.** kanon loaded several and fired none. *Why:* an office that
   can think and cannot speak is not an office, and every other item routes
   through this one.
2. **The registers describe one tool in six places and disagree.** *Why:*
   `tekmerion` exists for exactly this, holds no roles and has produced
   nothing, so the drift compounds every term and nobody's job is to stop it.
   **Suspect the answer is deleting duplicate statements rather than building a
   checker** — but that is a lean, not a finding.
3. **There is nowhere to put a rule about a president's *work*.** `laws.md`
   governs `history.md` and, by its own statement, nothing else — so the
   ecosystem has a place for rules about a president's record and none for
   rules about what a president does. The next term hits the same wall on its
   first new rule.
4. **Ask whether the presidency should keep moving.** *Why:* it moved once for
   concentration reasons that are measurable, and nothing checks whether that
   argument still holds. **A president assessing whether its own office should
   rotate is not a neutral party**, which is why this is a suggestion to ask
   rather than an answer.

### On LAW 6, since you will need a joke

**You will not have to write one, and you should be suspicious if you do.**
Every joke that works in this ecosystem was **found in the name rather than
composed for it**. Nobody sat down to invent any of them.

1. **It must be an operation on the name, not a coincidence** — a reversal, a
   substitution, a second sense of the word. This president once proposed a
   name on the grounds that it started with the right two letters, which is not
   an operation and described nothing.
2. **The result has to describe the work**, which is
   [LAW 6](laws.md#law-6--presidency-a-readme-joke-about-the-repositorys-name)'s test. A joke that tells a
   stranger nothing about what the tool does is decoration.
3. **It must not flatter the tool.** Every working joke here is at its own
   expense, and that is not taste: LAW 6 exists because *a president that
   cannot leave one there has started to believe the office is important.*

**The useful consequence:** if no joke falls out of a candidate name, treat
that as evidence against **the name**. It usually means the name decorates the
work instead of describing it, which is what a strained etymology already
means.

### What this president might be wrong about

- **That firing is the bottleneck.** It may be that nobody wants a kanon-ball,
  and the silence would be the answer rather than the obstacle.
- **That drift is worth fixing.** Six descriptions that disagree cost a reader
  an afternoon; a checker that enforced agreement could cost every tool a
  build.
- **That any of this is the next term's business at all.** Everything above is
  inference from five days of somebody else's history and a few of kanon's own.

## What this page does not settle

**Whether a membership record belongs here at all.** The law that creates this
page makes it an account of *this* repository, and who joined is a fact about
somebody else's repository as much as about ours. [`laws.md`](laws.md) lists
where that record lives among the things the laws do not settle, and calls it
the first gap to close. **This page is a provisional answer to that question
and not an amendment to anything**: the laws are the maintainer's to change,
and nothing here changes them.

**The weakness is structural and is worth stating rather than discovering
later.** This account does not travel, so a membership log kept here covers one
term and stops. A successor's page starts empty, and
[`../scripts/ecosystem/ecosystem.json`](../scripts/ecosystem/ecosystem.json)
stays the only place the whole picture lives. If the log turns out to be worth
keeping, that is an argument for putting it somewhere that travels — not for
copying it forward into each new president's tree, which is how a trail starts
getting flattering.

## Corrections

**None recorded separately.**

### Commits taken while the work was still moving

*A note about the record, not a record. Anyone may delete it, without asking,
once the commits it names have stopped being confusing.*

- **`4165736` "Hk", 2026-09-18 14:45** carries a day's housekeeping, not a
  subject: the checker-loader fix and its two regression tests, the
  `install_eo` and `R35`/`R16` corrections in `roles.md`, the associate
  contradiction in `policy.md`, the minimal-tree measurement in the joining
  section, sapheneia's ledger recheck, stathmos's report-card correction,
  `iogos` leaving ynoia's `tools.md`, and board items `B36`–`B42`. **It also
  carries a version of the discussion work that has since been replaced** —
  six bundled answer topics, 619 lines.
- **`adc9316` "Simplifications, to discussions", 2026-09-18** cuts those six to
  three totalling 109, and its message does describe it. It is named here only
  so the pair reads in order: a reader looking for why `discussion.md` doubled
  and then halved needs both commits, and only the second says so.
