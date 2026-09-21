# kanon

*κανών — the measuring rod: the standard a thing is held straight against.*

**kanon keeps the Eunoia ecosystem's governance.** It maintains the recommended
policy a member repository is checked against, the vision that policy is argued
from, the laws of the office, and the register of who is in and on what
footing.

It currently holds the ecosystem's **presidency** — an office in this
ecosystem's own work, which expires with the stretch and confers nothing over
anybody's repository.

## The register

**Who is in the Eunoia ecosystem, and on what terms.** A footing says what a
tool owes us and what we say about it, and the two are not the same scale —
[Ecosystem footings](docs/laws.md#law-1--ecosystem-footings-membership-and-other-relationships)
defines these relationships. Audit the register with:

```sh
scripts/eo_status_audit --check      # validate the register, offline
scripts/eo_status_audit              # policy and discussion status across checkouts
scripts/eo_ci_audit                  # GitHub Actions at each member's default-branch HEAD
```

**Hosted CI:** `scripts/eo_ci_audit` reports each member's
GitHub Actions results using `gh` when available, with a Python HTTP fallback
for public reads and optional `GH_TOKEN`/`GITHUB_TOKEN` authentication.
PyYAML supplies trigger inspection.
`--verbose` includes every
workflow and run link; `--check` exits 0 when all pass, 1 for failures, and 2
for pending or unverified results. Absent reusable-only and other non-push
workflows are marked `not_expected`; missing push runs remain unverified.
[Coverage and options](tools/stathmos/README.md#the-ci-audit).

> **[`scripts/ecosystem/ecosystem.json`](scripts/ecosystem/ecosystem.json) is
> the ground truth**, and a footing is a decision somebody made rather than a
> fact anything derives. Anywhere else that lists who is in this ecosystem is a
> copy; where a copy disagrees with the register, the register is right.

**Child projects are reached through their parent**, on their parent's footing.
`scripts/eo_status_audit` lists the advertised ones; `--all-children` shows every
recorded child with its listing preference.

**What tooling is available:** `scripts/eo_tooling_audit` reads
[`ecosystem_tooling.json`](scripts/ecosystem/ecosystem_tooling.json) and reports
owners, locations, layout exceptions and inventory gaps. Child projects can own
tooling. Two tables separate tools (general tools, solvers and proof checkers)
from artifacts (webpages, databases, other artifacts and tutorials).
`--verbose` includes entry points, content files and documentation; `--check` validates the inventory
offline, and `--check --local` also checks the available working trees.
Foundation tooling such as cvc5 is included. Explicitly excluded directories
remain visible with their reasons and count as non-compliant inventory coverage.

## The documents

[`docs/README.md`](docs/README.md) is the index, and names every page in
`docs/`. The two tables below are the ones a reader of this repository needs
first.

### Shared — written for every repository, not just this one

| document | what it settles |
| --- | --- |
| [`docs/policy.md`](docs/policy.md) | repository layout, ownership, maintenance, child projects and membership requirements |
| [`docs/vision.md`](docs/vision.md) | the five tenets this development aims at, the argument for them, and what follows for anything that leaves the repository. Argued, and never checked |
| [`docs/laws.md`](docs/laws.md) | the laws — the footings, the presidency, and what the office owes |
| [`docs/glossary.md`](docs/glossary.md) | the authoritative name register and alphabetized dictionary of eo's terms, maintained by the president |

### The office, and this term's work

| document | what it records |
| --- | --- |
| [`docs/history.md`](docs/history.md) | the term record — what it is for, what changed, what went wrong, what crosses to the next president, and what the next term should be for |
| [`docs/board.md`](docs/board.md) | cross-repository work and its next steps |
| [`docs/roles.md`](docs/roles.md) | every responsibility, who holds it, and what is deliberately not part of it |
| [`docs/maintenance.md`](docs/maintenance.md) | **start here to maintain this tree** — where to start, what you do, and what this repository is responsible for |

## If you maintain a tool and want to join

**Addressed to whoever maintains a tool *related to* the Eunoia ecosystem** —
a checker, a compiler, a Lean development, an analyzer, a template.

**Joining has two requirements: a reference in your README, and a CI job that
checks the reference is true.** Nothing else is asked — no discussion file, no
document you do not already keep.
[`docs/policy.md`](docs/policy.md#joining-the-eunoia-ecosystem) is the
authority; this is only the route in.

| where you are | what to run, **in your own repository** |
| --- | --- |
| the repository does not exist yet | `eo_init new` — writes a README saying what the tool is for, what it declines to answer, and why it is called what it is. **It complies with nothing, deliberately**: knowing what you are building is what makes the rest decidable, and joining comes later |
| it exists, and you want to join | `eo_join` — adds the declaration to your maintenance note and the `anoieu / policy` workflow, in either of the two forms [`policy.md`](docs/policy.md#2-run-the-check) accepts |
| it exists, and should *not* join | `eo_join --soft` — the maintenance note alone, joining nothing: it names this ecosystem and says you are **not** held to its policy. A note naming nobody at all is the same section with one paragraph swapped, and you write it yourself |
| it exists, and is held to the policy without saying so out front | **no command** — write the footing marker on your own maintenance page, saying what you hold yourself to. No front-page declaration, and you answer to that marker rather than to us |

**These commands live in [koine](https://github.com/ajreynol/koine)**, and
koine's `install_eo` puts them on your path. **What joining costs is this
repository's**:
[`docs/policy.md`](docs/policy.md#joining-the-eunoia-ecosystem) is the authority
on what a repository that joins is held to.

**Read it before you run it.** Each takes `--show-prompt`, which prints
exactly what it would hand an assistant and does nothing else.

**The answer to *should we join* is often no, and this page is better for
saying so.** A tool with conventions of its own, or maintainers who have agreed
to none of this, is worse off adopting a policy it did not choose — which is
what `--soft` is for. **Joining obliges you to a shared policy and one CI job
and nothing else**: no ownership of your tree, no authority over how you run
it, and leaving is a commit. And **a declaration on a shared tree is not one
maintainer's alone to make**, which is the first thing `eo_join` asks.

## A joke about the name

This repository keeps [the laws of the Eunoia ecosystem](docs/laws.md), and in
keeping them it opens discussion items addressed directly to members. **A
kanon-ball is one of those: a request, backed by law, fired from here.**

Say the name out loud and the rest follows. A kanon-ball comes in fast and can
be heavy — but it is aimed at exactly one tool, and nobody has to catch one.

## How this repository is maintained

This repository is part of the **Eunoia ecosystem** and follows its shared
repository policy, kept here in
[`docs/policy.md`](https://github.com/ajreynol/kanon/blob/main/docs/policy.md).

**Ecosystem human maintainers:** [the shared accountability list](docs/policy.md#human-maintainers).

**Written by an agent, under a maintainer's supervision.** The tree was settled
in conversation with the maintainer and written down by an agent working in
this checkout; the maintainer directs it, reads what is published and decides
what crosses to anybody else. **Nothing leaves this repository by machine.**

**What the supervision does not cover.** The maintainer has not re-derived
every claim this tree makes about a repository other than this one — those are
read from other trees and are the reading of whoever did it, correctable by the
repository they are about. And the supervision is of what is *written*, which
is the scope of their review. Automated checks report only the properties they
exercise; they do not establish the truth of every claim in these documents.
