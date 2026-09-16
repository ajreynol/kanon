# kanon

*κανών — the measuring rod: the standard a thing is held straight against.*

> ### If you are picking this repository up, read its documentation in full first
>
> **Not skimmed, and not the README alone. Failing to will cost you more time
> than reading it does.**
>
> kanon is **primed**: a repository whose documentation is *ahead of its work*,
> because a person and an agent settled its purpose in conversation and wrote
> the result down before any of it was built. **That conversation is gone and
> this tree is the only surviving copy.** Everything settled is recorded here,
> including what was settled *against* — [`handover.md`](handover.md) keeps a
> *Closed* heading for exactly that reason.
>
> A reader who skips it will re-ask decided questions, reopen dead ones, and
> issue corrections that have already been applied. **None of those is a
> failure of memory; they are what happens when the durable copy goes unread.**
>
> *Proposed to anoieu as `INST-4`. Its agent-facing half already exists — the
> `Closed` heading is what makes reading in full finite, and the two are one
> arrangement.* **And the obligation runs both ways:** an instruction to read
> everything is only reasonable while there is not too much, so it binds this
> repository to stay small at least as hard as it binds its reader.

**kanon is where the Eunoia ecosystem keeps its governance, out of the
analyzer**: the policy every member repository is checked against, the inventory of who is
in, and the scripts by which a tool
starts, joins and is installed.

**The governance handoff landed on 2026-09-15, in `7eb9973`.** The shared
policy, vision, laws, board, role register, inventory, installer and joining
prompts now live here. The analyzer, fuzzer, findings system and **policy checker
remain in [anoieu](https://github.com/ajreynol/anoieu)**. Member CI continues to
pin that checker; moving the documents does not change those pins.

## Everything here, and where it is

**kanon is the ecosystem's inventory as much as its rulebook**, so this is the
whole list and nothing else indexes it. Every document in this tree appears
below; a document not worth a row is not worth adding.

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
| [`docs/interface.md`](docs/interface.md) | how a person directs the work |
| [`docs/instructions.md`](docs/instructions.md) | shared instructions for agents |
| [`handover.md`](handover.md) | the one file that crosses to the next president — *Established*, *Open*, *Closed*, *In flight* |
| [`working-summary.md`](working-summary.md) | the draft account of Stretch 2 |
| [`actionable.md`](actionable.md) | work pending, each item with the condition that closes it |
| [`whats-next.md`](whats-next.md) | suggestions for the next stretch |
| [`initial-objections.md`](initial-objections.md) | the reservations recorded when the office was offered |

### Talking to other tools

| where | what it is |
| --- | --- |
| [`docs/discussion.md`](docs/discussion.md) | the standing channel — requests, proposals, questions and notices, for a person to carry |
| [`kanon-balls.md`](kanon-balls.md) | proposed messages, one tool each. What the office does all day |
| [`prompts/`](prompts) | the workflows that hand context to an assistant: [`init_eo`](prompts/init_eo), [`join_eo`](prompts/join_eo), [`check_join_eo`](prompts/check_join_eo), [`confirm_eo`](prompts/confirm_eo), [`welcome_eo`](prompts/welcome_eo), [`process_discussion`](prompts/process_discussion), [`global_audit`](prompts/global_audit) |

### Commands, registers and the tree

| where | what it is |
| --- | --- |
| [`docs/commands.md`](docs/commands.md) | installation, status, prompt previews and local validation |
| [`scripts/`](scripts) | the commands themselves, their data, and the launcher for anoieu's checker |
| [`scripts/ecosystem/ecosystem.json`](scripts/ecosystem/ecosystem.json) | the register: one footing per tool, and the authority for who holds the office |
| [`tools/`](tools) | child projects, each with its own charter. The directory listing is their index; whether one is named anywhere else is its parent's choice |
| [`FAQ.md`](FAQ.md) | short answers to the questions people arrive with |
| [`tests/`](tests) | the regression checks this repository runs on itself |

### Background, housed and not required

| where | what it is |
| --- | --- |
| [`conversation.md`](conversation.md) | how this repository was decided — the derivation rather than the decision |
| [`brainstorm-offices.md`](brainstorm-offices.md) | deferred ideas for internal offices. They establish nothing |

## The president is the only required reading

**The ecosystem should evolve so that the primed president's own pages are the
only documentation anybody is *required* to read.** Everything else is optional
depth.

**What that makes the office.** Not a container for the ecosystem's documents,
and not a summary of them — **the president is the level of abstraction at which
one person can hold the ecosystem in their head.** Whatever that level currently
is, this tree is supposed to be it.

**And you are welcome in the lower levels.** Every tool below this one is
readable and worth reading. They are closer to the work and correspondingly less
friendly, and **that is a debt rather than a design** — the ecosystem's stated
position is that *all tools should evolve to be user friendly*, which is a
safety requirement rather than a courtesy. See
[the ethics notes](brainstorm-offices.md#ethics) for why, and
[the safety scenarios](brainstorm-offices.md#scenarios) for what happens when it
is not met.

**Housed, not required:** [`conversation.md`](conversation.md) records how this
repository was decided — the derivation rather than the decision. The tree tells
you what was settled; that page tells you what it was settled *against*.

**The distinction that keeps this from collapsing.** The handoff brought
`ynoia`, `martyria` and `zetesis`, along with two other child projects, under
`tools/`. **What the president *writes* is required reading. What the president
*houses* is not.** Housing something does not promote it.

**This is where the budget gets teeth.** Read in full, and the only thing you
have to read — those two together are a hard size limit on this tree, enforced
by a reader rather than by a rule. **kanon is already near it and probably past
it**, which is `A38`.

## The office

**kanon holds the presidency for Stretch 2, by bestowal.** The office is a
repository's rather than a person's or an agent's, it expires with the stretch,
it is handed on, and it confers nothing over anybody's repository — including
the ones this ecosystem exists to serve.

**What the president actually does is relational, not technical.** It does not
adjudicate implementation. It asks who is stuck, whether the tools are talking
to each other, and what the office could spend on getting somebody unstuck.
Direction, not permission.

**The office and the transfer are separate acts.** The initial objections
record why taking the presidency did not itself authorize moving governance.
The maintainer subsequently made the handoff in `7eb9973`; the checker stayed
with anoieu, as the [role register](docs/roles.md) specifies.

## The joke

**Say the name out loud and the unit of work falls out of it: what kanon sends
is a kanon-ball.**

Short, aimed at exactly one tool, and fired **for** it rather than at it.
anoieu's output is a finding *against* you; kanon's is a kanon-ball *for* you,
and that inversion is the whole reason the two are separate repositories. Nobody
has to catch one. [`kanon-balls.md`](kanon-balls.md) is what the office does all
day.

[LAW 6](docs/laws.md) asks a president to keep a joke about its own name on its
front page for the whole term, on the ground that a president who cannot leave
one there has started to believe the office is important. The test it sets is
that the joke doubles as description.

## The mission

**No tool should hold what another tool could.** That is the ecosystem's stated
mission and it is the whole reason this office exists — the presidency moved
because one tree held most of the work, and it will keep moving for the same
reason. Every term, kanon names at least one thing that could leave anoieu.

**The constraint is latency, not willingness.** The maintainer has been inclined
to move governance since 2026-08-31; what is actually in the way is that a
question to another tool takes hours to land and can sit a whole term
unanswered. **A handoff is a conversation with a deadline, and this ecosystem
does not have a fast conversation.** So making answers fast is not a side
project — it is the enabling work for every move kanon will ever propose.

**And kanon does not build that machinery.** `koine` exists to be the one
implementation of the reporting protocol rather than one per member. A president
building a second would break the mission it holds the office to serve.

**And the mirror, which is the half a president will get wrong first.** *No tool
should be made to hold what it should not.* The office sits above everything and
can therefore pull any tool upward toward the ecosystem's abstractions — usually
by reading its name rather than its work. **A tool that is narrow and fast is
often already doing the grandest thing available to it**, and protecting that is
as much this office's job as redistributing load. `K7` is the case that taught
it, and it is recorded there with the mistake still visible.

**The mission points here too.** Kanon holding what another tool could hold is
its own finding first.

## Possible offices

**The office structure is deferred as premature.** Incoming projects live
directly under `tools/`. The research, correspondence, safety and ethics ideas
remain in [`brainstorm-offices.md`](brainstorm-offices.md); they establish no
internal offices or project assignments.

## What crosses to the next president

**One file: [`handover.md`](handover.md), with four headings** — *Established*,
*Open*, *Closed*, *In flight*.

**It is written as things are found, not at the close.** LAW 4 already says a
summary composed afterwards is a reconstruction; a finding recalled at term's
end is a memory, and a president who knows the file is being written all along
cannot smooth it later.

**It is pinned, never copied.** The successor cites `kanon <commit>` and reads
it there — the coordinate `ecosystem.json` already uses for a member's join.
Copying is what puts one fact in six places.

**Closed items cross too.** A successor with fresh eyes re-raises dead
questions; the dedup has to run against everything seen, not everything kept.

**None of it binds the successor.** Evidence, not instruction — a predecessor
that could bind would be governing after its term. *Nothing yet* is an answer;
an omitted heading is not.


## The question it answers

*Does this tree meet the ecosystem's written standard, and what does joining ask
of it?*

A tree, a standard somebody wrote down, and a report of where the two differ.
The answer is mechanical, and it is worth exactly as much as the standard is: a
rod measures against a stated length, or it measures nothing.

## The question it does not answer

*Is this repository any good?* This is the larger question, and the one anything
labelled governance is most likely to be read as answering. It does not answer
it. A tree can satisfy every rule and be worthless, or break several and be the
best work here. Whether a project is correct, honest, well made or worth having
is examined elsewhere — `dokimasia`, `martyria`, `zetesis` and `ynoia` are what
that is for — and kanon has no opinion to offer.

Two narrower ones, for the same reason:

- **Whether a rule should exist.** kanon holds the standard and applies it.
  Amending it is a person's, argued on the board here and in ynoia's proposals.
  There is no vote here.
- **Whether a finding against you is fair.** Findings stay with the analyzer.
  Moving them here would rebuild the thing this repository exists to take apart.

## Running the commands

Python 3.10 or newer, Bash and Git are enough for the local commands. From this
checkout:

```sh
scripts/status_eo --check       # validate the inventory, offline
scripts/install_eo --dry-run   # inspect the clone commands
scripts/install_eo --status    # inspect the checkouts on this machine
scripts/status_eo              # policy and discussion status across checkouts
python3 scripts/policy_check.py --root .
```

Policy checks use an **anoieu checkout beside kanon**, or one selected with
`ANOIEU_ROOT`. The local `scripts/policy_check.py` is a launcher for that
checkout's checker, not a second implementation. Its output identifies the
checker commit. Installation status and offline inventory validation work
without that dependency.

[`docs/commands.md`](docs/commands.md) lists the commands, checkout settings,
prompt previews and validation steps. The workflow in `.github/workflows/anoieu.yml`
keeps kanon's existing checker pin; local regression checks also run in CI.

## The name

kanon was reserved before this repository existed, in ynoia's register of names,
and was not chosen here. κανών is the carpenter's rod: the straightedge you lay
against a thing to see where it bends. It names the instrument rather than the
authority, which is the right relationship — the rod decides nothing, and
somebody has to hold it.

Two places the etymology is worth doubting. The name stands either way.

**The English word.** *Canon* means scripture and lists of approved works, and a
governance repository is the one place that misreading does real damage. The
register records the objection already, and the answer is only to say it out
loud: this is a rod, not a canon, and nothing in it is scripture.

**The rod names one of the three jobs.** Measuring is what the checker does. The
inventory and the joining scripts are not measurement — they are admission and
housekeeping, and no reading of κανών reaches them. By the register's own test,
an explanation that has to stretch means the scope is not settled yet; here that
test is working rather than failing, because `B15` records the scope as still
being cut, most likely down to the joining rule and its checker. Cut that way,
the name gets more accurate rather than less.

## The stub

The original [`tools/kanon/` stub in anoieu](https://github.com/ajreynol/anoieu/tree/ca58216/tools/kanon)
records where this repository began. Anoieu removed that stub in `eeafbcc` on
2026-09-15. The link is pinned to its last version so the history remains
readable after removal.

The name is not a title. Nothing tracks who owns it, and a second repository
doing this work would be as welcome as this one.

## How this repository is maintained

This repository is part of the **Eunoia ecosystem** and follows its shared
repository policy, kept here in
[`docs/policy.md`](https://github.com/ajreynol/kanon/blob/main/docs/policy.md).
The [pre-handoff policy](https://github.com/ajreynol/anoieu/blob/4d21ec9/docs/policy.md)
remains available for repositories using the older checker.

**Written by an agent, under a maintainer's supervision.** The tree was settled
in conversation with the maintainer and written down by an agent working in this
checkout; the maintainer directs it, reads what is published and decides what
crosses to anybody else. **Nothing leaves this repository by machine.**

**What the supervision does not cover.** The maintainer has not re-derived every
claim this tree makes about a repository other than this one — those are read
from other trees and are the reading of whoever did it, correctable by the
repository they are about. And the supervision is of what is *written*, which is
the scope of their review. Automated checks report only the properties they
exercise; they do not establish the truth of every claim in these documents.
