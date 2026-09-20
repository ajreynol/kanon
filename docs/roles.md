# The roles

**One entry per responsibility, under the tool that holds it** — a single
self-contained thing somebody is accountable for, with a permanent id and four
labelled fields. [`board.md`](board.md) is the other half of the pair: the
board is **what is outstanding**, this is **what everything is for**. **Within
a tool, position is the priority**; across tools nothing is ranked. *The rules
for reading and editing this page, and how a role is handed off, are at the
bottom.*

## anoieu

*Four responsibilities: the analyzer, fuzzer, findings system and policy
checker. Governance is now held by kanon.*

### R31 — the policy checker

**Held by:** `anoieu`
**Role:** **deciding whether a tree complies with the policy**, whoever wrote
the policy. The program every member's CI runs, its checks, its two tiers, its
skip lines, and its refusal to report coverage it does not have.
**Owns:** `scripts/policy_check.py`, and the `adoption_interface` case in
`tests/run.py` that holds it to being a published interface.

**Why it is split from `R4`.** The repository writing the rules should not be
the one filing findings against the repositories judged by them. Separating the
*rule* from the *checker* discharges that better than moving both: the rules
sit with a tree that has no stake in the findings, and the checking stays with
the tool whose whole mission is checking things.

**What it buys is the part worth the split.** Members' workflows do not change.
**Moving the rules costs a member nothing; moving the checker would cost every
one of them a commit.** What it costs is that the checker and the policy live
apart: a pin names an implementation and anoieu's contract number fixes the
mechanical requirements, and neither of them says which revision of the policy
*text* a tree was read against — so how the two stay in version step is still
[undecided](policy.md#2-run-the-check).

### R2 — the static analyzer

**Held by:** `anoieu`
**Role:** reading Eunoia signatures and semantic configuration files and
reporting what a checker accepts and should not — the front end, the checks,
the shallow typing pass and the desugarer. It is also the only thing that
compares the legs of the triple, which are owned by three different people.
**Owns:** the analyzer, the check registry, `docs/checks.md`, `docs/usage.md`,
and the committed baselines.

### R3 — the fuzzer

**Held by:** `anoieu`
**Role:** writing Eunoia nobody would write, handing it to a checker, and
shrinking and bucketing what comes back into something that can be filed.
Deliberately a baseline rather than a research instrument, and it says so.
**Owns:** `anoieu_fuzz/`, `docs/fuzzing.md`, the seed corpus, and the promoted
reproducers under `tests/fuzz/`.

`R28` and `R29` are retired. Neither is an active responsibility or a pending
role transfer.

`R26` is deliberately not allocated here: koine's `D8` proposes it for the
low-level formats of the reporting loop, and that request is open. An id
claimed in a proposal nobody has answered is not free, and taking it would make
the reply harder to write than skipping a number is.

## cvc5

### R7 — the solver, and the proofs

**Held by:** `cvc5`
**Role:** finding the answer and emitting the proof that justifies it. Every
artifact in the ecosystem is downstream of that output, and of decisions this
role made before any of the rest existed.
**Owns:** the solver, its proof production, and the proofs themselves.

### R8 — CPC, the calculus

**Held by:** `cvc5`
**Role:** maintaining the Cooperating Proof Calculus as a Eunoia signature: the
rules, their programs, and the file every checker here is built around.
**Owns:** `proofs/eo/cpc/`.

## dokimasia

### R9 — what no proof step covers

**Held by:** `dokimasia`
**Role:** reads cvc5's proof-production C++ and asks which of it has no proof
step behind it — the scrutiny before office, applied to the code that emits
proofs rather than to what it emits.
**Owns:** its findings about cvc5's proof production.

## ethos

### R10 — the proof checker

**Held by:** `ethos`
**Role:** the fast, unverified C++ checker that production runs against, and
the implementation every other reading of the language is compared to.
**Owns:** the checker, and its behaviour, which is the reference the rest of
the ecosystem measures itself against.

### R11 — the Eunoia manual

**Held by:** `ethos`
**Role:** the one description of Eunoia there is, and the language's authority.
It is by construction a manual for a *program*, which is why the boundary
between *the language requires this* and *this implementation happens to do
this* is not drawn in it.
**Owns:** `user_manual.md`.

> **Aspired handoff: `R11` to `sapheneia`**, so that the authority on *what
> Eunoia requires* is a language definition rather than a manual for one
> program. It would **invert a boundary both entries assert** — this one
> governs and `R20` says it does not — so both would be rewritten rather than
> moved.
>
> **The blocker is authorship, and joining would not clear it.**
> `user_manual.md` has **human authors** who have not adopted
> [`vision.md`](vision.md). Moving authority over what they wrote to a tree
> written by agents is a claim on somebody's authorship, and no footing makes
> it a handoff. **This stays where it is by right rather than by
> circumstance.**

## ethos-eoc

### R12 — the Eunoia compiler

**Held by:** `ethos-eoc`
**Role:** turns a signature and its semantics into a Lean development — one
constructor, type rule, evaluator case and verification condition per symbol.
**Owns:** the compiler and its stages.

> **Aspired handoff: `R12` to `noesis`** — the semantics *defined in* Lean, and
> the compiler a metaprogram over those definitions rather than a translator
> into them. **The gaining tool does not exist**, so it is named here and never
> in an `Entities` field; [`proposals.md`](../tools/ynoia/docs/proposals.md) audits
> it as `P3` with the verdict **not yet**.
>
> **The authorship point applies, less sharply than for `R11`.** The compiler
> is human-written by authors who have not adopted [`vision.md`](vision.md).
> What is different is that `noesis` would be a *second implementation* rather
> than a reassignment, and a role following the implementation that gets used
> is an ordinary way for one to move — which still does not make it ours to
> schedule.

### R13 — the shipped semantics sets

**Held by:** `ethos-eoc`
**Role:** maintains the `.eos` semantics sets it ships. In the absence of any
other definition, what a `.eos` file means is what this role makes of it, which
is a larger responsibility than it looks.
**Owns:** the semantics sets in its tree.

## eudaimonia

### R14 — the calculus template

**Held by:** `eudaimonia`
**Role:** the logos arrangement with the calculus taken out — bring a signature
and a semantics, get a Lake project with a checker, its proofs, its regression
suite and its documentation.
**Owns:** the template and its generators, and the profile a new calculus
declares about itself.

## euthyna

### R15 — the audit of logos's proof

**Held by:** `euthyna`
**Role:** reads the generated development logos carries and says what it is
made of and where its weight sits — what is dead, what repeats, and what is
structured in a way that will cost the next regeneration.
**Owns:** its own account, inside its own directory.

## kanon

**The roles in this section are attached to the presidency.** Their ongoing
responsibilities transfer to the successor under
[LAW 3.2](laws.md#law-32--transferring-presidential-roles-and-child-projects). The completed term account
stays with its authoring repository; the successor starts its own. Shared commands
and child projects are recorded under their own holders below and follow their
own terms of transfer.

### R4 — the ecosystem's shared policy and vision

**Held by:** `kanon`
**Role:** **what this ecosystem asks of a repository, and what the work is
aiming at** — both halves, because they are one position stated twice: the
policy is the half a program can decide from a tree, the vision is the half
nobody has the authority to settle. How a repository is arranged, what its
front page must say about who is writing it, how tools talk to one another, and
what a child project may do. Written to be adopted rather than admired, and
machine-checked in every member's CI.
**Owns:** `docs/policy.md`, `docs/vision.md`, and the ecosystem's vocabulary and
authoritative name register in `docs/glossary.md` (kept current by the
president).

**The checker is a separate responsibility, `R31`, and is anoieu's.**

### R6 — the inventory

**Held by:** `kanon`
**Role:** who is in the ecosystem and on what footing: maintaining the
authoritative register and the installation exceptions. Membership decisions
remain a person's; stathmos audits the register under `R37`, and koine's
`eo_status` reads it under `R16`.
**Owns:** `scripts/ecosystem/ecosystem.json`,
and `scripts/ecosystem/checkouts.json`.

### R32 — the laws of the office

**Held by:** `kanon`
**Role:** the candidate laws — what footings exist, what a member owes, and
what the office owes. [LAW 7](laws.md#law-7--maintaining-and-amending-the-laws)
currently assigns this work to the president, so the role moves with the office.
That assignment may change; it is not a permanent condition of the presidency.
**Owns:** `docs/laws.md`.

### R33 — the board of next actions

**Held by:** `kanon`
**Role:** what is outstanding across the ecosystem and who has to act on it,
and the standing channel in which one tool addresses another. Both are
registers of work that crosses a repository boundary, and neither carries
anything: a person does.
[LAW 4.4](laws.md#law-44--the-board-and-the-role-register) makes the board and
this page presidential records and separates the board from a discussion file.
**Owns:** `docs/board.md` and `docs/discussion.md`.

### R34 — the historian of the current stretch

**Held by:** `kanon`
**Role:** keeping `history.md` as the account of the current stretch. Under
[LAW 4.1](laws.md#law-41--keeping-and-revising-the-terms-history), the president
may add, revise or remove entries during the term as it sees fit. The account
stays with its authoring repository when the presidency moves.
**Owns:** `docs/history.md`.

## koine

### R35 — the shared commands for starting a repository and joining the ecosystem

**Held by:** `koine`
**Role:** **maintaining the two commands a repository outside this ecosystem
actually runs** — `eo_init`, which gives a new tool a README saying what it is
for and complies with nothing, and `eo_join`, which writes the declaration and
the `anoieu / policy` workflow in whichever of the two forms
[`policy.md`](policy.md#2-run-the-check) the joiner takes. Their text, their
options, and what they ask an assistant to do.
**Owns:** `eo_cmd/eo_init` and `eo_cmd/eo_join`, and `scripts/install_eo`,
which puts them on a person's path.

**The rest of `eo_cmd/` is [`R16`](#r16--the-shared-low-level-tooling), and the
line is where the command runs.** Only these two run inside a repository that is
being started or joined, which is the whole reason this role is separate from
`R4`. koine's own `eo_cmd/commands.json` files these two under `R35` and the
rest under `R16`, agreeing with the split this register records.

**Why this is separate from `R4`.** These two are the only commands in this
ecosystem that run **inside the repository being started or joined**, rather
than from the repository that keeps the rule. A command meant for a tree that is
not the one it lives in belongs with the tool whose job is shared machinery;
what a member is held to belongs with the office.

**The risk it carries, stated because it is live.** `eo_join` is about two
hundred lines of argument about whose front page a declaration is, and that
argument is a *position* rather than plumbing. **The drafting of it sits with a
tool that does not hold the position**, and the guard is `R4`: the rule those
lines state is the office's, and a change to what `eo_join` asks of a repository
is a change to be argued there.

### R16 — the shared low-level tooling

**Held by:** `koine`
**Role:** maintaining the machinery every member would otherwise implement
separately — **one implementation of the shared parts rather than one per
repository.** The bug database is one of them and is not the boundary of the
role.
**Owns:** the shared implementations and the interfaces other tools build
against, including the commands `install_eo` puts on a person's path that
are not `R35`'s: `eo_status`, which reads the register in the tree that holds it;
`eo_respond`, which answers one topic another tool addressed to you;
`eo_housekeeping`, which brings a repository up to date and, with `--report`,
only reports what is outstanding; `eo_topic`,
which opens one topic in the runner's own discussion file; `eo_child`, which
starts a child project and refuses a run that does not name one; and
`eo_brainstorm`, which reads every tree on the machine and writes only
`brainstorm.local.md`.

## logos

### R17 — the verified checker for CPC

**Held by:** `logos`
**Role:** an executable proof checker for CPC written in Lean, whose soundness
is proven against a correctness specification. It is the artifact the
ecosystem's trust argument actually rests on.
**Owns:** the generated development, and the soundness statement it
establishes.

### R18 — the model of SMT-LIB semantics in Lean

**Held by:** `logos`
**Role:** a standalone Lean formalization of what SMT-LIB terms mean,
independent of the checker and usable on its own. It is what a soundness
statement is stated *against*, which makes it load-bearing for `R17` and
separable from it.
**Owns:** `Cpc/SmtModel.lean` and its write-up.

### R19 — the semantics of CPC

**Held by:** `logos`
**Role:** maintains `Cpc.eos`, the semantics the compiler reads for the
calculus cvc5 emits proofs in.
**Owns:** `Cpc.eos` and its cached form.

## martyria

## sapheneia

### R20 — Eunoia as a language definition

**Held by:** `sapheneia`
**Role:** a second description of Eunoia, written as a language definition
rather than as a manual for a program: where the boundary falls between what
the language requires and what one implementation happens to do.
**Owns:** its own account, inside its own directory.

## stathmos

This project moves with the presidency, carrying its work and roles to the
repository that holds the office.

### R30 — the report card

**Held by:** `stathmos`
**Role:** **writing and keeping the report card** — assembling, per tool and at
a recorded version, the evidence a paragraph about that tool rests on, writing
the paragraph, and re-grading each round. It is the half of the vision that goes
stale, because it is the half that is a claim about somebody else's project this
month rather than a statement of what the work is for.
**Owns:** [`tools/stathmos/docs/report-card.md`](../tools/stathmos/docs/report-card.md),
and the evidence and protocol pages beside it.

> **The report card is shared work maintained by this child project.**
> Being housed with the president does not make its assessments independent.

### R37 — ecosystem status auditing

**Held by:** `stathmos`
**Role:** checking the register against the trees it describes and reporting
status, local policy results, declaration drift and missing evidence. These
mechanical checks do not grade adherence to the vision or decide membership.
Split from `R6` on 2026-09-18; kanon retains the register.
**Owns:** the public `scripts/eo_status_audit` and `scripts/eo_tooling_audit` launchers,
[`tools/stathmos/audits/status_audit.py`](../tools/stathmos/audits/status_audit.py),
[`tools/stathmos/audits/tooling_audit.py`](../tools/stathmos/audits/tooling_audit.py),
[`tools/stathmos/audits/child_listing.py`](../tools/stathmos/audits/child_listing.py),
and the local checker launcher
[`tools/stathmos/audits/policy_check.py`](../tools/stathmos/audits/policy_check.py).
Their regressions live in [`tools/stathmos/tests/`](../tools/stathmos/tests/).
The checking rules and their implementation remain anoieu's under `R31`.

## tekmerion

## ynoia

This project moves with the presidency, carrying its work and roles to the
repository that holds the office.

### R23 — auditing whether an idea deserves a repository

**Held by:** `ynoia`
**Role:** *should this become a repository of its own*, answered against a
stated standard with a verdict attached — and, where the answer is no, an
argument about whose existing tree the work belongs in instead.
**Owns:** [`proposals.md`](../tools/ynoia/docs/proposals.md), which absorbed
`requests.md` on 2026-09-19 — the two pages asked one question and every entry
on the second explained why it was not the first. Naming arguments are in
[`tools.md`](../tools/ynoia/docs/tools.md#arguing-about-names) and refer to the
authoritative register in `docs/glossary.md`.

## zetesis

---

## How to maintain this page

**An id is permanent.** `R4` stays `R4` whoever holds it, because decisions get
recorded against ids and an id that moves invalidates them silently. A
deprecated role is **deleted** rather than marked dead, and its number is never
reused.

**No role is too small.** The count is not a budget. A role that could
reasonably be split is split; one that feels too slight to deserve an id gets
one anyway. An extra entry costs four lines — two responsibilities sharing one
entry costs somebody the ability to say which of them a change belongs to.

**Length is a measurement, not a defect.** Six roles under one heading means a
tool has taken on more than it should, or has not decided what it is, and
merging entries until the section looks tidy only hides it. **An empty section
is the same measurement from the other end**: a tool that is named, is in the
register, and is accountable for nothing yet.

**Two tools holding one role is a seam that has not been cut.** The entry names
both and appears under both headings, as a standing question rather than a
description. `R16` is the worked example — the reporting loop was implemented
twice before anybody wrote down that it was one role.

**Within a tool, position is the priority**: the first role is the one it is
least able to drop. **Across tools nothing is ranked**, and sections are
alphabetical, because this page has no basis for saying one repository matters
more than another. Ids therefore appear out of order, which is correct.

**A role is not a child project.** This is a global register of *who is
responsible*; a child project is local to its parent's tree and answers *where
the work is being done*. A tool can hold roles with no child projects, or carry
child projects and hold one role.

**The tool ids are the register's**, and where the two disagree [the
register](../scripts/ecosystem/ecosystem.json) is right and this page is stale.

**Nothing here is aspired.** This page is an account of what is true and a note
on keeping it that way. A role somebody thinks should move is a proposal, and a
proposal lives in [`discussion.md`](discussion.md) where the tool it would cost
something can disagree with it, or on [`board.md`](board.md) as work. **An
aspiration recorded here reads as a fact to somebody skimming**, and the entry
next to it is a fact — which is the whole reason the two cannot share a page.

## How a role is handed off

**A handoff is the same role under a different heading**, and the id does not
change. **Three things, and they are not a sequence.**

1. **Name the role, not the files.** A proposal phrased as a list of paths is a
   migration nobody can hold an opinion about — and the id is what makes the
   move reversible.
2. **Say what stays.** The losing tool's remaining section is written out in
   full, because the line between the two halves is where every argument about
   it will actually happen.
3. **Move the entry, and only the entry**, in one commit, so this register is
   never half-handed-over. **The pins move last and each consumer picks when**:
   a consumer still pinned to the old holder is not behind, it is correct.

**None of it is a gate and none of it is an order**, and a handoff that skipped
all three is a handoff rather than a defect. Two habits are worth keeping
anyway, because both cost a sentence: **name the consumers whose pins move**,
and **leave the opinions where they landed** — afterwards, a handoff nobody
objected to and one nobody was asked about look identical unless the asking is
on the record.

**A role over human-authored work is not ours to move.** No footing and no
procedure here makes reassigning it a handoff; it is a claim on somebody's
authorship. **Ask who wrote it and what they agreed to**, not what footing the
repository holds. `R11` is the worked example.

**A child project graduating is a handoff**, and the commonest one this page
will see: the roles do not change, the heading over them does. **A role handed
off to nobody is deprecated rather than orphaned**, and an empty section is
where a handoff goes looking for a taker.

## Why the split between kanon and anoieu falls where it does

**The argument is about exactly one thing: the repository that writes the rules
a member is judged by should not also be the one filing findings against
them.** The filing sits with the analyzer; `R4` writes the rules, so it sits
here. `R6` keeps membership decisions beside the policy; stathmos's `R37`
audits those decisions from the register. And the position on
what may be published stays with the tool whose own behaviour it constrains.

**The second of the three exists because an audit asked it and the procedure
could not**: *what does the losing repository keep*, and *is either half left
unable to answer a question it could answer alone*.

## What the shape says

**`scripts/eo_status_audit` prints the footings**; counting the entries below is the
only honest way to count the roles, and a table here restating them would be a
copy nothing compares.

**kanon holds seven, which is the most of any tool, and that is the finding
rather than an achievement.** The register's own rule says a long section means
a tool has taken on more than it should or has not decided what it is — and the
ecosystem's mission says no tool should hold what another tool could. Every one
of the seven is a candidate to hand off, and `R32` and `R34` move with the
office by law whether anybody proposes it or not.

**An empty section records no assigned role.** A child may still deliver useful
work without one, and may hold shared responsibilities when assigned them.
`stathmos` holds `R30` and `R37`; its charter describes the shared work and
interfaces it maintains.
