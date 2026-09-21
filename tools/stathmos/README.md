# stathmos

A **child project** under [`docs/policy.md`](../../docs/policy.md). Started by a
human, and advertised in ecosystem listings. Its audits read repositories and
report observations without changing them.

This project is tied to the presidency: when the office changes hands, stathmos
moves with its work and roles to the repository that holds the presidency.

## The name

*σταθμός — a standard weight: the thing an object is weighed against, rather
than the scale or the verdict.*

**In one line: it audits ecosystem status and tooling, and keeps
[the report card](docs/report-card.md).**

**This project is not an island:** its work serves the ecosystem through kanon.
Stathmos maintains the public
`scripts/eo_status_audit`, `scripts/eo_tooling_audit`,
`scripts/eo_dioktes_audit` and `scripts/eo_ci_audit` launchers in kanon's
top-level `scripts/`, with their implementation in this project's `audits/`.
Kanon's tests and CI exercise that implementation. The audits read kanon's
registers; the status audit runs anoieu's policy checker through the local launcher.
`roles.md` records these responsibilities; `laws.md` and `vision.md` reference
the report card. These are documented interfaces of a maintained child project.

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
[`audits/status_audit.py`](audits/status_audit.py), with child-listing declarations read by
[`audits/child_listing.py`](audits/child_listing.py). `--help` documents the options and
columns. The command works from any working directory.

The audit reads kanon's authoritative
[`ecosystem.json`](../../scripts/ecosystem/ecosystem.json), checks its structure
with `--check`, and compares declarations in remote trees with `--check --online`.
Its table reports local policy checks through
[`audits/policy_check.py`](audits/policy_check.py), which locates and runs
anoieu's checker. To check one tree directly, run
`python3 tools/stathmos/audits/policy_check.py --root PATH` from kanon's root;
omitting `--root` checks kanon. The audit never changes a membership decision
or the register.

The `productive` column reports evidence under
[Productive entities](../../docs/laws.md#law-11--productive-entities), using
[`audits/productivity.py`](audits/productivity.py). For each president, member
and child, `yes` means a deliverable is present in the tooling audit for that
owner, a project link references it in laws/policy/vision, or it holds a current
role in the role register or the presidency. `no` means none was found; `?` means
verification is incomplete; other footings show `-`. Layout and unrelated
inventory gaps do not disqualify a present deliverable. Parents and children
are assessed separately. `--verbose` names the evidence, and `--all` includes
unadvertised children. A person reviews whether a central reference explains
the purpose adequately; the audit only locates it. Missing productivity is
reported without changing membership or failing `--check`.

**These are mechanical checks, not report-card grades.** The report card remains
human judgement against the vision. An unavailable observation is unverified,
not a pass or a failure; local policy results are not the corresponding CI run.
Koine's `eo_status` remains the shared command for reading the register.

## The CI audit

**`scripts/eo_ci_audit` answers whether members' GitHub Actions are passing.**
[`audits/ci_audit.py`](audits/ci_audit.py) reads the registered members and
president, discovers each default branch, and checks its current commit.
Children share their parent's CI; other footings are excluded. It requires
Python 3 and authenticated GitHub CLI (`gh auth login`), works from any directory,
and makes only read requests. Install the pinned YAML parser from kanon's root
to inspect absent workflows' triggers:

```sh
python3 -m pip install -r tools/stathmos/audits/requirements.txt
```

```sh
scripts/eo_ci_audit                    # table and details for non-passing results
scripts/eo_ci_audit --verbose          # every workflow and run link
scripts/eo_ci_audit --repo kanon       # one member; repeat --repo for several
scripts/eo_ci_audit --check            # 0 all pass, 1 failure, 2 otherwise incomplete
scripts/eo_ci_audit --json             # dated observations, commits and workflow results
```

`pass` needs successful observed runs and no missing push-triggered workflows
at that commit. For each absent workflow, the audit reads its YAML definition
at the same commit. A reusable-only workflow (`workflow_call`) has no standalone
run to expect; its results belong to caller runs, which are checked normally.
Other workflows without a push trigger, including schedule/manual and PR-only
workflows, also need not run on every default-branch commit. These absences are
shown as `not_expected`, with their reason, and do not count as passes or block
successful observed CI. A repository with only expected absences remains
unverified because it has no observed standalone CI result.

`fail` means a failed, cancelled, timed-out or otherwise failed run; `pending`
means work is queued, running or waiting. Every observed run counts even if it
was scheduled or manually requested: trigger inspection only explains absences
and never excuses an observed failure. Skipped, neutral and unknown results
remain `unverified`, as do missing push-triggered runs, unreadable or unrecognized
trigger definitions, an unavailable YAML parser, inaccessible repositories,
incomplete API responses and a branch advancing during the audit. Branch and
path filters are not evaluated, so an absent filtered push run remains
unverified. A workflow accepting both `workflow_call` and `push` still needs
standalone evidence. Disabled workflows, PR runs,
branch-protection requirements and CI outside GitHub Actions are outside scope.

The audit reads every results page and selects the newest run per workflow and
event, including its latest attempt. A successful manual run cannot hide a
failed push run, and an old green commit cannot stand in for the current one.
Without `--check`, observations do not change the exit code; invalid arguments
or an unreadable/empty register still exit 2. With `--check`, an observed failure
takes precedence over incomplete results elsewhere. The offline regression
suite covers this command; kanon's CI does not depend on live results from
other repositories.

## The tooling audit

**`scripts/eo_tooling_audit` reports available tooling by kind and inventory
gaps.** [`audits/tooling_audit.py`](audits/tooling_audit.py) reads kanon's
[`ecosystem_tooling.json`](../../scripts/ecosystem/ecosystem_tooling.json).
Each entry names a repository, a directory, entry points or content files,
and documentation. Tools include programs and importable libraries; a library's
public module is an entry point even when it has no standalone executable.
An optional `owner` can name a child project; the directory
is measured from that owner's root when checking layout. All paths remain
relative to the containing repository, including shared launchers and docs.
The audit reuses the status audit's checkout resolver and repository footings.
It includes foundations such as cvc5 as tooling providers, without running
policy checks or imposing requirements on them.
It never executes the recorded entry points. The output has a Tools table for
`tool`, `solver` and `checker`, and an Artifacts table for `webpage`, `database`,
`artifact` and `tutorial`. Webpage artifacts record their generators as entry
points. Kinds are counted separately:

| kind | contribution | required content |
| --- | --- | --- |
| `tool` (default) | general programs and libraries | `entrypoints` |
| `solver` | constraint solvers, such as cvc5 | `entrypoints` |
| `checker` | proof-checking programs and libraries | `entrypoints` |
| `webpage` | sites, such as GitHub Pages | generator `entrypoints` |
| `database` | maintained records, such as bug databases | `files` |
| `artifact` | other maintained data, such as proof signatures | `files` |
| `tutorial` | instructional guides, such as paideia's bootcamp and mimesis's tutorials | `files` |

Every kind also requires documentation. Documentation supports an entry through
its `docs` metadata; it is never itself a tooling entry. The owner's
`docs/` and `contrib/` cannot be tooling directories. `contrib/` is reserved for
manually obtaining external tools.

The tables show the tool or artifact, kind, repository, path and purpose.
Missing paths, unverified checkouts and layout exceptions appear below them.
Ownership remains in the registry for layout checks and productivity. Discovery
flags unregistered tracked top-level directories within repositories and named
child owners for a person to classify. Directories reserved by the
[policy layout](../../docs/policy.md#the-layout), including `examples/`, `test/`,
`tests/`, `cmake/`, `include/`, `licenses/` and `contrib/`, are skipped;
explicit exclusions are listed after the tables with their availability and
reasons, and marked non-compliant inventory coverage. That describes our record,
not an obligation on the owner.
Nested tools
and root implementations need explicit entries. A research charter alone is
not evidence of tooling, and file presence is not evidence that a tool works.

Stathmos owns the tooling in `audits/`; it is a top-level tool directory within
this child project. Kanon's `scripts/` retains the public launchers.

`--verbose` prints sources, entry points, content files and docs. `--check` validates the
inventory without sibling checkouts; `--check --local` also compares working
trees, and `--check --online` compares GitHub default-branch trees. Missing
observations are unverified. Layout gaps are advisory; inventory gaps, including
intentional exclusions, fail a requested comparison. Structural validation alone
still accepts explained exclusions. `--help` documents limits and exit codes.

## The dioktes audit

**`scripts/eo_dioktes_audit` reports what this ecosystem is looking for defects
in, and whether it is still allowed to.**
[`audits/dioktes_audit.py`](audits/dioktes_audit.py) reads the `_pursuits`
records in kanon's [`ecosystem.json`](../../scripts/ecosystem/ecosystem.json),
which [LAW 10](../../docs/laws.md#law-10--investigations-declaring-conducting-and-ending-one)
requires a person to declare.

**The basis is re-derived on every run rather than trusted.** A declaration
records the footing it rested on the day it was written, and that footing is a
line in somebody else's entry: a member leaving under
[LAW 2.1](../../docs/laws.md#law-21--a-members-right-to-leave) ends the standing
LAW 10.4 supplied, and an entry losing its `published` ends what LAW 10.1
permitted, in both cases without the investigation's own record changing by a
character. A lapsed basis is reported against the row and fails `--check`.

`--verbose` adds the scope, the closing condition and the responsible
maintainer. Rows whose reporting is `stopped` sort first, because those carry a
LAW 10.2 obligation somebody can still breach. The audit reports and changes
nothing: starting an investigation, ending one, and acting on a lapsed basis
are each a person's act.

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
now houses this project. Moving the directory does not establish independence.
A self-assessment states its evidence, what was examined and the limits of that
examination. Favorable and unfavorable conclusions need the same support;
there is no required number of unfavorable findings.

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

**It has held the report card since 2026-09-16.** The September 19 edition of
[`docs/report-card.md`](docs/report-card.md) covers fifteen repositories and the
two previously assessed projects, ethos-eoc and stathmos. It uses the tooling
audit, epikrisis's history reports and its LOC instrument, with fixed revisions
in [`docs/evidence.md`](docs/evidence.md) and [`docs/evidence.json`](docs/evidence.json).
Activity informs review priorities; LOC informs the new frugality assessment.
Neither computes a grade.

**And it is graded on it.** The assessed revision still had an older evidence
file than report card. This edition repairs that mismatch, but the correction
is outside its recorded pin and earns no retrospective credit.

## Layout

- [`docs/README.md`](docs/README.md) indexes the report card, evidence and protocol.
- [`audits/`](audits/) holds the status, CI, tooling and dioktes audits and their helpers.
- [`tests/`](tests/) holds their offline regressions. Kanon's test run includes them.

From this directory, run `python3 -m unittest discover -s tests -v` to test
stathmos on its own.
