# kanon

*κανών — the measuring rod: the standard a thing is held straight against.*

**kanon is currently the Eunoia ecosystem's governance**: the maintainer of the
recommended policy every member repository is checked against, the vision it is
argued from, the laws of the office, and the register of who is in and on what
footing. It currently holds the ecosystem's presidency, which is an office in
this ecosystem's own work and confers nothing over anybody's repository.

## The register

**Who is in the Eunoia ecosystem, and on what terms.**

The list of the members of the Eunoia ecosystem can be obtained by:

```sh
scripts/status_eo --check      # validate the register, offline
scripts/status_eo              # policy and discussion status across checkouts
```

> **[`scripts/ecosystem/ecosystem.json`](scripts/ecosystem/ecosystem.json) is
> the ground truth**; the table above is a copy for a reader who has not cloned
> anything, and **nothing compares the two**. Where they disagree, the register
> is right.

The above requires python 3.10 or newer, Bash and Git are enough for the local commands.

## The documents

### The shared documents — written for every repository, not just this one

| document | what it settles |
| --- | --- |
| [`docs/policy.md`](docs/policy.md) | how a repository is arranged, what its front page must say, and what joining costs. Decidable from a tree, and checked by a program |
| [`docs/vision.md`](docs/vision.md) | the five tenets this development aims at, and the argument for them. Argued, and never checked |
| [`docs/practice.md`](docs/practice.md) | what follows from the tenets once a repository is running: front pages, what may be claimed, where speculative work goes, papers |
| [`docs/laws.md`](docs/laws.md) | the candidate laws — the footings, the presidency, and what the office owes |

### The office, and this term

| document | what it records |
| --- | --- |
| [`docs/history.md`](docs/history.md) | kanon's account of its own stretch, and the membership record |
| [`docs/board.md`](docs/board.md) | cross-repository work and its next steps |
| [`docs/roles.md`](docs/roles.md) | every responsibility, who holds it, and what is deliberately not part of it |
| [`docs/coherence.md`](docs/coherence.md) | the maintenance entry point: the protocols, and what to ask before changing something |
| [`docs/interface.md`](docs/interface.md) | how a person directs the work, at length |
| [`docs/instructions.md`](docs/instructions.md) | the same, short, and addressed to the person rather than the agent |
| [`handover.md`](handover.md) | the one file that crosses to the next president — *Established*, *Open*, *Closed*, *In flight* |
| [`working-summary.md`](working-summary.md) | the draft account of Stretch 2, kept current rather than written at the close |
| [`actionable.md`](actionable.md) | work pending, each item with the condition that closes it |
| [`whats-next.md`](whats-next.md) | what this president thinks the next term should be *for*. It binds nothing |

### Talking to other tools

| where | what it is |
| --- | --- |
| [`docs/discussion.md`](docs/discussion.md) | the standing channel — requests, proposals, questions and notices, for a person to carry |
| [`kanon-balls.md`](kanon-balls.md) | proposed messages, one tool each. What the office does all day |
| [`prompts/`](prompts) | the workflows that hand context to an assistant: [`init_eo`](prompts/init_eo), [`join_eo`](prompts/join_eo), [`check_join_eo`](prompts/check_join_eo), [`confirm_eo`](prompts/confirm_eo), [`welcome_eo`](prompts/welcome_eo), [`process_discussion`](prompts/process_discussion), [`global_audit`](prompts/global_audit) |

## The commands

This repository is also the recommended way to get started with development
in Eunoia ecosystem over multiple repositories.
Requiring, python 3.10 or newer, Bash and Git are enough for the local commands. From this
checkout:

```sh
scripts/install_eo --dry-run   # inspect the clone commands
scripts/install_eo --status    # inspect the checkouts on this machine
```

[`docs/commands.md`](docs/commands.md) is the full reference.
`.github/workflows/anoieu.yml` keeps kanon's existing checker pin; the local
regression checks also run in CI.

The policy checks are maintained in 
**[anoieu](https://github.com/ajreynol/anoieu).** The policy, the vision, the laws and the registers are
here. The analyzer, the fuzzer, the findings system and the program that
decides whether a tree meets the policy are there, and a member pins a commit
of it.

## A joke about the name

This repository keeps [the laws of the Eunoia ecosystem](docs/laws.md), and in
keeping them it opens discussion items addressed directly to members. **A
kanon-ball is one of those: a request, backed by law, fired from here.**

Say the name out loud and the rest follows. A kanon-ball comes in fast and can
be heavy — but it is aimed at exactly one tool, and nobody has to catch one.
[`kanon-balls.md`](kanon-balls.md) is what the office does all day.

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
