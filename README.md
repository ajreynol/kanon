# kanon

*κανών — the measuring rod: the standard a thing is held straight against.*

**kanon keeps the Eunoia ecosystem's governance, out of the analyzer.** Three
things, and they are the whole of it:

- **[the register](#the-register)** — who is in this ecosystem, and on what
  footing;
- **[the documents](#the-documents)** — the policy every member is checked
  against, the vision it is argued from, and the laws of the office;
- **[the commands](#the-commands)** — by which a tool starts, joins, and is
  installed.

It also holds the ecosystem's **presidency for Stretch 2**, which is an office
in this ecosystem's own work and confers nothing over anybody's repository.

> ### If you are picking this repository up, read it in full first
>
> **Not skimmed, and not this page alone. Failing to will cost you more time
> than reading it does.**
>
> kanon is **primed**: its documentation is *ahead of its work*, because a
> person and an agent settled its purpose in conversation and wrote the result
> down before any of it was built. Everything settled is recorded here,
> including what was settled *against* — [`handover.md`](handover.md) keeps a
> *Closed* heading for exactly that reason.
>
> A reader who skips it will re-ask decided questions, reopen dead ones, and
> issue corrections that have already been applied. **None of those is a
> failure of memory; they are what happens when the durable copy goes unread.**
>
> **The obligation runs both ways.** An instruction to read everything is only
> reasonable while there is not too much, so it binds this repository to stay
> small at least as hard as it binds its reader.

## What kanon is for

**The question it answers:** *does this tree meet the ecosystem's written
standard, and what does joining ask of it?* A tree, a standard somebody wrote
down, and a report of where the two differ. The answer is mechanical, and it is
worth exactly as much as the standard is: a rod measures against a stated
length, or it measures nothing.

**The question it does not answer:** *is this repository any good?* That is the
larger question, and the one anything labelled governance is most likely to be
read as answering. A tree can satisfy every rule and be worthless, or break
several and be the best work here. Whether a project is correct, honest, well
made or worth having is examined elsewhere, and kanon has no opinion to offer.

Two narrower refusals, for the same reason:

- **Whether a rule should exist.** kanon holds the standard and applies it.
  Amending it is a person's, argued on [the board](docs/board.md). There is no
  vote here.
- **Whether a finding against you is fair.** Findings stay with the analyzer.
  Moving them here would rebuild the thing this repository exists to take
  apart.

**Why it is a separate repository at all.** The tool writing the rules should
not also be the one filing findings against you. That separation is the entire
reason kanon exists, and it is the first thing to check if the two ever start
to merge again.

## The register

**Who is in the Eunoia ecosystem, and on what terms.**
[`docs/laws.md`](docs/laws.md) defines the footings and
[`docs/policy.md`](docs/policy.md#the-footings) says what each one costs whom.
Two of them — *candidate* and *outsider* — are positions **we** hold about
somebody else, and nothing recorded under one belongs to the repository it
describes or asks anything of it.

| footing | tool | what it is |
| --- | --- | --- |
| **foundation** | [cvc5](https://github.com/cvc5/cvc5) | the SMT solver, and the owner of CPC. Asked for nothing, ever |
| **president** | kanon | this repository: policy, governance and the register |
| **member** | [anoieu](https://github.com/ajreynol/anoieu) | the static analyzer, the fuzzer, and the policy checker every member runs |
| **member** | [dokimasia](https://github.com/ajreynol/dokimasia) | finds gaps in cvc5's proof production |
| **member** | [epikrisis](https://github.com/ajreynol/epikrisis) | audits repository histories against evidence |
| **member** | [eschaton](https://github.com/ajreynol/eschaton) | compares approaches to better-founded SMT solvers |
| **member** | [eudaimonia](https://github.com/ajreynol/eudaimonia) | the calculus template: a signature, a checker and its proofs |
| **member** | [koine](https://github.com/ajreynol/koine) | the shared reporting protocol and its tooling |
| **member** | [logos](https://github.com/ajreynol/logos) | the Lean development, and the owner of `Cpc.eos` |
| **member** | [tachyon](https://github.com/ajreynol/tachyon) | searches for ways to improve cvc5 performance |
| **candidate** | [ethos](https://github.com/cvc5/ethos) | the proof checker, and the Eunoia manual. Addressed by the policy, and has joined nothing |
| **outsider** | carcara, ddSMT, IsaRARE, lean-smt, LFSC, murxla | tracked for comparison only, **never proposed for promotion**. They were not asked |

**Child projects are reached through their parent**, on their parent's footing,
and are not listed here — whether a child is named anywhere at all is its
parent's choice, which [`docs/policy.md`](docs/policy.md#child-projects)
governs. `scripts/status_eo` lists the advertised ones beside their parents;
`--all-children` shows every recorded child with its listing preference.

> **[`scripts/ecosystem/ecosystem.json`](scripts/ecosystem/ecosystem.json) is
> the ground truth**; the table above is a copy kept for a reader who has not
> cloned anything. `scripts/status_eo` prints the register live, with policy
> and channel status per tool. **Nothing compares the two**, so where they
> disagree, the register is right.

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

## The office

**kanon holds the presidency for Stretch 2, by bestowal.** The office belongs
to a repository rather than to a person or an agent, it expires with the
stretch, it is handed on, and it confers nothing over anybody's repository —
including the ones this ecosystem exists to serve.

**What the president does is relational, not technical.** It does not
adjudicate implementation. It asks who is stuck, whether the tools are talking
to each other, and what the office could spend on getting somebody unstuck.
Direction, not permission.

**The president's own pages should be the only documentation anybody is
*required* to read.** Everything else is optional depth. That makes the office
not a container for the ecosystem's documents and not a summary of them, but
**the level of abstraction at which one person can hold the ecosystem in their
head** — and whatever that level currently is, this tree is supposed to be it.
**What the president *writes* is required reading; what it *houses* is not.**
Housing something does not promote it.

**And you are welcome in the lower levels.** Every tool below this one is
readable and worth reading. They are closer to the work and correspondingly
less friendly, and **that is a debt rather than a design** — the ecosystem's
position is that all tools should evolve to be user friendly, which is a safety
requirement rather than a courtesy. [The ethics
notes](docs/misc/brainstorm-offices.md#ethics) say why, and [the safety
scenarios](docs/misc/brainstorm-offices.md#scenarios) say what happens when it
is not met.

**This is where the budget gets teeth.** *Read in full* and *the only thing you
have to read* are together a hard size limit on this tree, enforced by a reader
rather than by a rule. **kanon is already near it and probably past it**, which
is `A38`.

### The mission

**No tool should hold what another tool could.** That is the ecosystem's stated
mission and the whole reason this office exists — the presidency moved because
one tree held most of the work, and it will keep moving for the same reason.
Every term, kanon names at least one thing that could leave anoieu.

**The constraint is latency, not willingness.** What is in the way is that a
question to another tool takes hours to land and can sit a whole term
unanswered. **A handoff is a conversation with a deadline, and this ecosystem
does not have a fast conversation.** So making answers fast is the enabling
work for every move kanon will ever propose — and kanon does not build that
machinery, because `koine` exists to be the one implementation of the reporting
protocol rather than one per member.

**The mirror is the half a president gets wrong first.** *No tool should be
made to hold what it should not.* The office sits above everything and can
therefore pull any tool upward toward the ecosystem's abstractions, usually by
reading its name rather than its work. **A tool that is narrow and fast is
often already doing the grandest thing available to it**, and protecting that
is as much this office's job as redistributing load. And kanon holding what
another tool could hold is its own finding first.

### What crosses to the next president

**One file: [`handover.md`](handover.md), with four headings** — *Established*,
*Open*, *Closed*, *In flight*.

It is **written as things are found**, not at the close: a finding recalled at
term's end is a memory, and a president who knows the file is being written all
along cannot smooth it later. It is **pinned, never copied** — the successor
cites `kanon <commit>` and reads it there. **Closed items cross too**, because
a successor with fresh eyes re-raises dead questions and the dedup has to run
against everything seen. And **none of it binds the successor**: evidence, not
instruction. A predecessor that could bind would be governing after its term.

## The joke

**Say the name out loud and the unit of work falls out of it: what kanon sends
is a kanon-ball.**

Short, aimed at exactly one tool, and fired **for** it rather than at it.
anoieu's output is a finding *against* you; kanon's is a kanon-ball *for* you,
and that inversion is the whole reason the two are separate repositories.
Nobody has to catch one. [`kanon-balls.md`](kanon-balls.md) is what the office
does all day.

[LAW 6](docs/laws.md) asks a president to keep a joke about its own name on its
front page for the whole term, on the ground that a president who cannot leave
one there has started to believe the office is important. The test it sets is
that the joke doubles as description.

## Common questions

**Five questions, fixed.** A style kanon proposes to every tool in the
ecosystem, written here first because proposing a style you have not adopted is
worth nothing.

**What is this for?** The ecosystem's governance, kept out of the analyzer —
[the register](#the-register), [the documents](#the-documents) and [the
commands](#the-commands). See [*What kanon is for*](#what-kanon-is-for).

**Which repository does X?** [The register](#the-register) routes it. If X is a
defect in somebody's code, it is anoieu's; if X is whether a tree meets the
standard, it is here.

**What does it depend on, and who depends on it?** It depends on anoieu for the
policy checker, which stays there. It is used by anybody running the installer
or the joining prompts, and by every repository reading the shared policy.

**What is it *not*?** Not the analyzer, and **not the tool that files findings
against members**. Not a judge of whether your work is any good. And not a
canon — κανών is a measuring rod, and nothing here is scripture.

**Where do I ask something?** [`docs/discussion.md`](docs/discussion.md) holds
topics between kanon and other tools. A person carries each topic and
explicitly requests any response; writing a topic does not deliver it.

## The name

kanon was reserved before this repository existed, in ynoia's register of
names, and was not chosen here. κανών is the carpenter's rod: the straightedge
you lay against a thing to see where it bends. It names the instrument rather
than the authority, which is the right relationship — the rod decides nothing,
and somebody has to hold it.

Two places the etymology is worth doubting. The name stands either way.

**The English word.** *Canon* means scripture and lists of approved works, and
a governance repository is the one place that misreading does real damage. The
register records the objection already, and the answer is only to say it out
loud: this is a rod, not a canon.

**The rod names one of the three jobs.** Measuring is what the checker does.
The register and the joining scripts are not measurement — they are admission
and housekeeping, and no reading of κανών reaches them. By the register's own
test, an explanation that has to stretch means the scope is not settled yet;
here that test is working rather than failing, because `B15` records the scope
as still being cut, most likely down to the joining rule and its checker. Cut
that way, the name gets more accurate rather than less.

**The name is not a title.** Nothing tracks who owns it, and a second
repository doing this work would be as welcome as this one.

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
