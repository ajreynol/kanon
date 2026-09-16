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
[`docs/laws.md`](docs/laws.md) defines them and
[`docs/policy.md`](docs/policy.md#the-footings) says what each costs whom. Read
the register with:

```sh
scripts/status_eo --check      # validate the register, offline
scripts/status_eo              # policy and discussion status across checkouts
```

> **[`scripts/ecosystem/ecosystem.json`](scripts/ecosystem/ecosystem.json) is
> the ground truth**, and a footing is a decision somebody made rather than a
> fact anything derives. Anywhere else that lists who is in this ecosystem is a
> copy; where a copy disagrees with the register, the register is right.

**Child projects are reached through their parent**, on their parent's footing.
`scripts/status_eo` lists the advertised ones; `--all-children` shows every
recorded child with its listing preference.

## The documents

### Shared — written for every repository, not just this one

| document | what it settles |
| --- | --- |
| [`docs/policy.md`](docs/policy.md) | how a repository is arranged, what its front page must say, and what joining costs. Decidable from a tree, and checked by a program |
| [`docs/vision.md`](docs/vision.md) | the five tenets this development aims at, and the argument for them. Argued, and never checked |
| [`docs/practice.md`](docs/practice.md) | what follows from the tenets once a repository is running: front pages, what may be claimed, where speculative work goes, papers |
| [`docs/laws.md`](docs/laws.md) | the candidate laws — the footings, the presidency, and what the office owes |

### The office, and this term's work

| document | what it records |
| --- | --- |
| [`docs/history.md`](docs/history.md) | the term record — what it is for, what changed, what went wrong, what crosses to the next president, and what the next term should be for |
| [`docs/board.md`](docs/board.md) | cross-repository work and its next steps |
| [`docs/discussion.md`](docs/discussion.md) | the standing channel — what we are saying to other tools, for a person to carry |
| [`docs/roles.md`](docs/roles.md) | every responsibility, who holds it, and what is deliberately not part of it |
| [`docs/coherence.md`](docs/coherence.md) | the maintenance entry point: the protocols, and what to ask before changing something |
| [`docs/interface.md`](docs/interface.md) | how a person directs the work, at length |
| [`docs/instructions.md`](docs/instructions.md) | the same, short, and addressed to the person rather than the agent |

## The commands

This repository is also the recommended way to get started with development in
the Eunoia ecosystem across several repositories at once. Python 3.10 or newer,
Bash and Git are enough for everything here. From this checkout:

```sh
scripts/install_eo --dry-run   # inspect the clone commands
scripts/install_eo --status    # inspect the checkouts on this machine
```

[`docs/commands.md`](docs/commands.md) is the full reference, and
[`prompts/`](prompts) holds the workflows that hand context to an assistant:
[`init_eo`](prompts/init_eo), [`join_eo`](prompts/join_eo),
[`check_join_eo`](prompts/check_join_eo), [`confirm_eo`](prompts/confirm_eo),
[`welcome_eo`](prompts/welcome_eo),
[`process_discussion`](prompts/process_discussion) and
[`global_audit`](prompts/global_audit).
`.github/workflows/anoieu.yml` keeps kanon's existing checker pin; the local
regression checks also run in CI.

**The policy checks are maintained in
[anoieu](https://github.com/ajreynol/anoieu).** The policy, the vision, the
laws and the registers are here; the analyzer, the fuzzer, the findings system
and the program that decides whether a tree meets the policy are there, and a
member pins a commit of it.

## A joke about the name

This repository keeps [the laws of the Eunoia ecosystem](docs/laws.md), and in
keeping them it opens discussion items addressed directly to members. **A
kanon-ball is one of those: a request, backed by law, fired from here.**

Say the name out loud and the rest follows. A kanon-ball comes in fast and can
be heavy — but it is aimed at exactly one tool, and nobody has to catch one.
[`docs/discussion.md`](docs/discussion.md) is where they land, and what the
office does all day.

## How this repository is maintained

This repository is part of the **Eunoia ecosystem** and follows its shared
repository policy, kept here in
[`docs/policy.md`](https://github.com/ajreynol/kanon/blob/main/docs/policy.md).

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
