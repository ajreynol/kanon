# kanon

*κανών — the measuring rod: the standard a thing is held straight against.*

**kanon is current the Eunoia ecosystem's governance.**
  
## The documents

**Every document in this tree appears below.** A document not worth a row is
not worth adding.

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

### The tree

| where | what it is |
| --- | --- |
| [`docs/commands.md`](docs/commands.md) | installation, status, prompt previews and local validation |
| [`scripts/`](scripts) | the commands themselves, their data, and the launcher for anoieu's checker |
| [`tools/`](tools) | child projects, each with its own charter. The directory listing is their index |
| [`tests/`](tests) | the regression checks this repository runs on itself |

### `docs/misc/` — housed, and not required

| where | what it is |
| --- | --- |
| [`docs/misc/conversation.md`](docs/misc/conversation.md) | the verbatim transcript of the session that primed this repository. The tree is what was decided; this is what was said |
| [`docs/misc/brainstorm-offices.md`](docs/misc/brainstorm-offices.md) | the internal office structure, **deferred as premature**. It establishes nothing, and is kept for [the safety scenarios](docs/misc/brainstorm-offices.md#scenarios) and [the ethics notes](docs/misc/brainstorm-offices.md#ethics), which are cited from live work |
| [`docs/misc/initial-objections.md`](docs/misc/initial-objections.md) | the reservations recorded when the office was offered, before it was held |

## The commands

Python 3.10 or newer, Bash and Git are enough for the local commands. From this
checkout:

```sh
scripts/status_eo --check      # validate the register, offline
scripts/status_eo              # policy and discussion status across checkouts
scripts/install_eo --dry-run   # inspect the clone commands
scripts/install_eo --status    # inspect the checkouts on this machine
python3 scripts/policy_check.py --root .
```

Policy checks use an **anoieu checkout beside kanon**, or one selected with
`ANOIEU_ROOT`. The local `scripts/policy_check.py` is a launcher for that
checkout's checker, not a second implementation, and its output identifies the
checker commit. Installation status and offline register validation work
without that dependency.

[`docs/commands.md`](docs/commands.md) is the full reference.
`.github/workflows/anoieu.yml` keeps kanon's existing checker pin; the local
regression checks also run in CI.

**kanon publishes the standard; [anoieu](https://github.com/ajreynol/anoieu)
publishes the checker.** The policy, the vision, the laws and the registers are
here. The analyzer, the fuzzer, the findings system and the program that
decides whether a tree meets the policy are there, and a member pins a commit
of it.

## The joke

This repository is the current keeper of the laws of the Eunoia ecosystem [link here].
In establishing these laws, it gives discussion items that are targetted directly to members of the Eunoia ecosystem.
A **kanon-ball** is a request, backed by law, originating from this repository.
A kanon-ball is intended to come fast and potentially give a heavy request.

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
