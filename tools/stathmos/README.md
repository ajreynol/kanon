# stathmos

A **child project** under [`docs/policy.md`](../../docs/policy.md). Started by a
human, read-only, and advertised in ecosystem listings.

This project is tied to the presidency: when the office changes hands, stathmos
moves with its work and roles to the repository that holds the presidency.

## The name

*σταθμός — a standard weight: the thing an object is weighed against, rather
than the scale or the verdict.*

**In one line: it audits ecosystem status and keeps
[the report card](report-card.md).**

**This is not an island**, and the exception is deliberate. Other documents in
this repository point at the page — `roles.md` records its roles, `laws.md` and
`vision.md` name it. The public command `scripts/eo_status_audit` runs this
project's implementation, and the repository's tests exercise it. The audit
reads kanon's register and runs anoieu's checker through its local launcher. These
connections outside this directory are deliberate: the command and the
assessment must be usable by the repository that houses them.

**For the report card:** assemble, per tool and at a recorded version, the evidence a
paragraph would rest on; write the paragraph; and re-grade each round. **What it
still does not do is settle anything.** The page is argued and never checked,
`vision.md` forbids it from becoming a build step, and **a person may overrule
any paragraph without giving a reason.** Adherence to policy is tracked
automatically; adherence to vision must never be.

The objection worth recording: σταθμός also means a halting-place or station,
and it sits close to `kanon` — the measuring rod proposed for the governance
repository — closely enough that somebody could confuse the two. The difference
is in their responsibilities: kanon maintains the rules and recorded membership
decisions; stathmos checks the evidence and keeps the assessments.

## The status audit

**`scripts/eo_status_audit` is the public command.** Its implementation lives in
[`scripts/status_audit.py`](scripts/status_audit.py), with child-listing declarations read by
[`scripts/child_listing.py`](scripts/child_listing.py). `--help` documents the options and
columns. The command works from any working directory.

The audit reads kanon's authoritative
[`ecosystem.json`](../../scripts/ecosystem/ecosystem.json), checks its structure
with `--check`, and compares declarations in remote trees with `--check --online`.
Its table reports local policy checks through
[`scripts/policy_check.py`](scripts/policy_check.py), which locates and runs
anoieu's checker. To check one tree directly, run
`python3 tools/stathmos/scripts/policy_check.py --root PATH` from kanon's root;
omitting `--root` checks kanon. The audit never changes a membership decision
or the register.

**These are mechanical checks, not report-card grades.** The report card remains
human judgement against the vision. An unavailable observation is unverified,
not a pass or a failure; local policy results are not the corresponding CI run.
Koine's `eo_status` remains the shared command for reading the register.

## The question

**What does each tool in this ecosystem actually weigh against the tenets, at
the version we recorded — and what is the evidence?**

Not *is it good*. That question belongs to whoever writes the paragraph, and
this project exists to make sure they are weighing something rather than
remembering something.

## Why it is a separate thing at all

**The report card and status audit have a named maintainer**, with
responsibilities separate from writing the governance they examine. The project
remains a child of the repository holding the presidency; `R30` and `R37` keep
their numbers when it moves, under the handoff described in
[`../../docs/roles.md`](../../docs/roles.md).

Assessments made while this project was in anoieu remain marked as
self-assessments. **New assessments of kanon are self-assessments**, since it
now houses this project. Moving the directory does not establish independence. That rule is borrowed rather than invented — a
neighbouring tool that audits histories holds itself to it, and a
self-assessment producing no unfavourable findings is void.

## What it does not do

- **It does not reach verdicts.** It assembles evidence; a person grades. A
  paragraph on the report card is a judgement about somebody else's project and
  the kernel forbids a program from producing one.
- **It does not read histories.** *What happened over time, and what the way a
  project changed did well and badly* is an instrument another tree already
  built. This one asks it a question rather than rebuilding it.
- **It does not grade conduct.** Whether this ecosystem behaves well is
  [martyria](https://github.com/ajreynol/epikrisis/blob/main/tools/martyria/README.md) and
  [zetesis](https://github.com/ajreynol/epikrisis/blob/main/tools/zetesis/README.md). Both now live in epikrisis. Utility and ethics are judged in
  this ecosystem, and they are judged in different places on purpose.
- **It does not settle anything.** It writes paragraphs; a person may overrule
  any of them, and no tool may put a verdict against a tenet.
- **Its assessments are written inside this directory.** The audit reads files
  and reports to the terminal; it changes no repository.

## Status

**Started 2026-09-02**, by the maintainer, in an explicit instruction — the only
way one of these may begin.

**Status auditing moved here on 2026-09-18**, at the maintainer's direction.
`R37` holds that responsibility, split from kanon's inventory role `R6`;
`scripts/eo_status_audit` remains the public entry point.

**It now holds the page rather than only the role**, since 2026-09-16:
[`report-card.md`](report-card.md) is written here, supersedes the edition
anoieu last graded on 2026-09-02, and covers twelve tools.

**And it is graded on it**, which the first edition promised and deferred: *a
project on its first day has no record to weigh*. It has one now, its entry is
in the sharper register, and the shortfall it records against itself is that
[`evidence.md`](evidence.md) is older than the page resting on it.
