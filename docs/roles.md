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
**Not this role:** what the rules *are*, which is `R4` and is held by kanon.
This role implements somebody else's document and has no standing to change
what it says.

**Why it is split from `R4`.** The repository writing the rules should not be
the one filing findings against the repositories judged by them. Separating the
*rule* from the *checker* discharges that better than moving both: the rules
sit with a tree that has no stake in the findings, and the checking stays with
the tool whose whole mission is checking things.

**What it buys is the part worth the split.** Members' workflows do not change.
**Moving the rules costs a member nothing; moving the checker would cost every
one of them a commit.** What it costs is that the checker and the policy live
apart — `ANOIEU_REV` pins only the checker, and how the two stay in version
step is [undecided](policy.md#2-run-the-check).

### R2 — the static analyzer

**Held by:** `anoieu`
**Role:** reading Eunoia signatures and semantic configuration files and
reporting what a checker accepts and should not — the front end, the checks,
the shallow typing pass and the desugarer. It is also the only thing that
compares the legs of the triple, which are owned by three different people.
**Owns:** the analyzer, the check registry, `docs/checks.md`, `docs/usage.md`,
and the committed baselines.
**Not this role:** what happens to a finding once it exists, which is the
reporting workflow rather than a role here, and generating cases nobody wrote,
which is `R3`.

### R3 — the fuzzer

**Held by:** `anoieu`
**Role:** writing Eunoia nobody would write, handing it to a checker, and
shrinking and bucketing what comes back into something that can be filed.
Deliberately a baseline rather than a research instrument, and it says so.
**Owns:** `anoieu_fuzz/`, `docs/fuzzing.md`, the seed corpus, and the promoted
reproducers under `tests/fuzz/`.
**Not this role:** reading a signature without running anything, which is `R2`,
and the research-quality successor, which is nobody's — it has a name,
`elenchos`, and no repository.

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
**Not this role:** checking them — that is `R10` and `R17` — and adopting
anything from this ecosystem. Its footing is **foundation**: nothing here
constrains it and nothing here asks it for anything.

### R8 — CPC, the calculus

**Held by:** `cvc5`
**Role:** maintaining the Cooperating Proof Calculus as a Eunoia signature: the
rules, their programs, and the file every checker here is built around.
**Owns:** `proofs/eo/cpc/`.
**Not this role:** the semantics of CPC, which is `R19` and lives in another
tree entirely, and the language the signature is written in, which is `R11`.

## dokimasia

### R9 — what no proof step covers

**Held by:** `dokimasia`
**Role:** reads cvc5's proof-production C++ and asks which of it has no proof
step behind it — the scrutiny before office, applied to the code that emits
proofs rather than to what it emits.
**Owns:** its findings about cvc5's proof production.
**Not this role:** the calculus, the checkers, or the proofs. It reads the code
that produces a proof, never the proof.

## ethos

### R10 — the proof checker

**Held by:** `ethos`
**Role:** the fast, unverified C++ checker that production runs against, and
the implementation every other reading of the language is compared to.
**Owns:** the checker, and its behaviour, which is the reference the rest of
the ecosystem measures itself against.
**Not this role:** saying what the language *is*, which is `R11` in the same
tree, and being verified, which is nobody's — the name `pathos` is reserved for
it and there is no repository.

### R11 — the Eunoia manual

**Held by:** `ethos`
**Role:** the one description of Eunoia there is, and the language's authority.
It is by construction a manual for a *program*, which is why the boundary
between *the language requires this* and *this implementation happens to do
this* is not drawn in it.
**Owns:** `user_manual.md`.
**Not this role:** drawing that boundary. A second reading is `R20`, and it is
additive: this role governs and that one does not.

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
**Not this role:** what the emitted development goes on to prove, which is
`R17`, and carrying what a proof establishes into Lean's own terms, which is
nobody's.

> **Aspired handoff: `R12` to `noesis`** — the semantics *defined in* Lean, and
> the compiler a metaprogram over those definitions rather than a translator
> into them. **The gaining tool does not exist**, so it is named here and never
> in an `Entities` field; [`proposals.md`](../tools/ynoia/proposals.md) audits
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
**Not this role:** `Cpc.eos`, which is `R19`, and any account of the semantics
that does not depend on this compiler, which is nobody's.

## eudaimonia

### R14 — the calculus template

**Held by:** `eudaimonia`
**Role:** the logos arrangement with the calculus taken out — bring a signature
and a semantics, get a Lake project with a checker, its proofs, its regression
suite and its documentation.
**Owns:** the template and its generators, and the profile a new calculus
declares about itself.
**Not this role:** any particular calculus. CPC is `R8`'s and its development
is `R17`'s; the subject here is the shape, never the content.

## euthyna

### R15 — the audit of logos's proof

**Held by:** `euthyna`
**Role:** reads the generated development logos carries and says what it is
made of and where its weight sits — what is dead, what repeats, and what is
structured in a way that will cost the next regeneration.
**Owns:** its own account, inside its own directory.
**Not this role:** maintaining or rewriting what it reads, which stays `R17`.
Anything it wants to say leaves through its parent, like any other finding.

## kanon

*These are the **office's** rather than this repository's.*
[`laws.md`](laws.md#what-the-office-carries) lists what the presidency carries
— the protocols, the policy and the joining prompts, the vision, the laws, the
register, the glossary, the commands, and the account of the stretch. **They
move when the office moves**, except the account, which stays in the tree that
wrote it; a successor inherits the rest whole.

### R4 — the ecosystem's policy, and joining it

**Held by:** `kanon`
**Role:** **what this ecosystem asks of a repository, and what the work is
aiming at** — both halves, because they are one position stated twice: the
policy is the half a program can decide from a tree, the vision is the half
nobody has the authority to settle. How a repository is arranged, what its
front page must say about who is writing it, how tools talk to one another, and
what a child project may do. Written to be adopted rather than admired, and
machine-checked in every member's CI.
**Owns:** `docs/policy.md`, `docs/vision.md`, `docs/practice.md`, the ecosystem's
vocabulary in `docs/glossary.md` (kept current by the president), and the
`init_eo`, `join_eo`, `check_join_eo` and `global_audit` prompts.
**Not this role:** who is actually in the ecosystem, which is `R6`; and
**deciding whether a tree complies, which is `R31` and stays in anoieu.**

**The checker is a separate responsibility, `R31`, and is anoieu's.**

### R6 — the inventory, and getting the ecosystem onto a machine

**Held by:** `kanon`
**Role:** who is in the ecosystem and on what footing, and the commands that
clone the rest of it beside a checkout, record where each one landed, and
report what has drifted.
**Owns:** `scripts/ecosystem/ecosystem.json`,
`scripts/ecosystem/checkouts.json`, `scripts/ecosystem/ecosystem.py`,
`scripts/install_eo`, `scripts/status_eo`, and the `welcome_eo` prompt.
**Not this role:** deciding membership — a status is changed by a person and no
script writes that file — and the rules a member is checked against, which are
`R4`.

### R32 — the laws of the office

**Held by:** `kanon`
**Role:** the candidate laws — what footings exist, what a member owes, and
what the office owes. LAW 7 gives the page to whoever holds the presidency,
which makes this role move with the office rather than staying here.
**Owns:** `docs/laws.md`.
**Not this role:** what a member is *checked* against, which is `R4` and is
mechanical; and choosing who holds the office, which is a person's and no law
here settles.

### R33 — the board, and what this ecosystem says to another tool

**Held by:** `kanon`
**Role:** what is outstanding across the ecosystem and who has to act on it,
and the standing channel in which one tool addresses another. Both are
registers of work that crosses a repository boundary, and neither carries
anything: a person does.
**Owns:** `docs/board.md` and `docs/discussion.md`.
**Not this role:** carrying a defect in somebody's file, which goes through the
reporting workflow and has its own ledger and its own standard; and the
machinery a message runs on, which is `R16`.

### R34 — the historian of the current stretch

**Held by:** `kanon`
**Role:** **keeping the account of the stretch while it runs** — what it was
for, what changed, what went wrong, and what crosses to whoever holds the
office next. LAW 4 makes it each office-holder's account of its **own** term,
kept current rather than written at the close, with every figure re-derivable
by somebody else.
**Owns:** `docs/history.md`.
**Not this role:** the per-tool commit census, which LAW 4 gives to `epikrisis`
and **forbids this role from producing**; and grading how well a tool performs,
which is `R30`.

## koine

### R16 — the shared low-level tooling

**Held by:** `koine`
**Role:** maintaining the machinery every member would otherwise implement
separately — **one implementation of the shared parts rather than one per
repository.** The reporting loop is the first of them and is not the boundary
of the role.
**Owns:** the shared implementations, and the interfaces other tools build
against.
**Not this role:** deciding what any member reports, or what settles a row.
Those differ per tool and are each tool's own.

## logos

### R17 — the verified checker for CPC

**Held by:** `logos`
**Role:** an executable proof checker for CPC written in Lean, whose soundness
is proven against a correctness specification. It is the artifact the
ecosystem's trust argument actually rests on.
**Owns:** the generated development, and the soundness statement it
establishes.
**Not this role:** speed, which is `R10`'s and is the reason two checkers
exist, and whether the development can be read by a person, which is `R15`'s
subject.

### R18 — the model of SMT-LIB semantics in Lean

**Held by:** `logos`
**Role:** a standalone Lean formalization of what SMT-LIB terms mean,
independent of the checker and usable on its own. It is what a soundness
statement is stated *against*, which makes it load-bearing for `R17` and
separable from it.
**Owns:** `Cpc/SmtModel.lean` and its write-up.
**Not this role:** the Eunoia semantics of a calculus, which is `R13` and
`R19`, and carrying what it says into Lean's native logic, which is nobody's.

### R19 — the semantics of CPC

**Held by:** `logos`
**Role:** maintains `Cpc.eos`, the semantics the compiler reads for the
calculus cvc5 emits proofs in.
**Owns:** `Cpc.eos` and its cached form.
**Not this role:** the signature it is the semantics of, which is `R8` and sits
in a different tree under a different owner. Two legs of one triple, held apart
— which is exactly why something has to compare them, and that is `R2`.

## martyria

## sapheneia

### R20 — Eunoia as a language definition

**Held by:** `sapheneia`
**Role:** a second description of Eunoia, written as a language definition
rather than as a manual for a program: where the boundary falls between what
the language requires and what one implementation happens to do.
**Owns:** its own account, inside its own directory.
**Not this role:** governing. `R11` remains the authority and this account says
so on its own front page; where the two disagree, that disagreement is a
finding and it leaves through the reporting workflow.

## stathmos

### R30 — the report card

**Held by:** `stathmos`
**Role:** **writing and keeping the report card** — assembling, per tool and at
a recorded version, the evidence a paragraph about that tool rests on, writing
the paragraph, and re-grading each round. It is the half of the vision that goes
stale, because it is the half that is a claim about somebody else's project this
month rather than a statement of what the work is for.
**Owns:** [`tools/stathmos/report-card.md`](../tools/stathmos/report-card.md),
and the evidence and protocol pages beside it. *Before 2026-09-16 this role
held the pen over a page anoieu kept; that page is the previous edition and
stays in anoieu's tree.*
**Not this role:** the tenets themselves, which are part of `R4`; **settling
anything** — `vision.md` forbids adherence to vision from being tracked
automatically, so the page is never a build step and a person may overrule any
paragraph; and reading *histories*, which another tree already does.

> **A child project holding a role is not an island, and the exception is
> deliberate**: the tool writing the report card should not indefinitely be the
> tool it grades most closely. The stated destination is a repository of its
> own, and the role keeps its id when it goes.

## tekmerion

## ynoia

### R23 — auditing whether an idea deserves a repository

**Held by:** `ynoia`
**Role:** *should this become a repository of its own*, answered against a
stated standard with a verdict attached — and, where the answer is no, an
argument about whose existing tree the work belongs in instead.
**Owns:** `proposals.md` and `requests.md`.
**Not this role:** approving anything, and creating anything. A repository is a
person's decision and a person's act, and this role produces an argument with a
recommendation at the end.

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

## How a role is handed off

**A handoff is the same role under a different heading**, and the id does not
change. Seven steps, in this order because each is cheap to get wrong and
expensive to discover later.

1. **Name the roles, not the files.** A proposal phrased as a list of paths is
   a migration nobody can hold an opinion about.
2. **Say what stays.** The losing tool's remaining section is written out in
   full, because the line between the two halves is where every argument about
   it will actually happen.
3. **Name the consumers**, by id. Where a role carries a CI contract that is
   *every member*, and the count grows with each tool that joins first —
   usually the strongest argument for doing it sooner.
4. **Put it on [`board.md`](board.md)**, with one prompt per entity. A prompt
   written to be answered is a different artifact from an announcement.
5. **Collect the opinions, and leave them where they landed.** Afterwards, a
   handoff nobody objected to and one nobody was asked about look identical
   unless the asking is on the record.
6. **Move the entry, and only the entry**, in one commit, so this register is
   never half-handed-over.
7. **The pins move last, and each consumer picks when.** A consumer still
   pinned to the old holder is not behind; it is correct.

**None of them is a gate.** They describe the honest way to hand a role over
and stop nobody's work. What would change that is the ecosystem being stable
enough that a handoff nobody was asked about costs somebody a red build — and
that is a person's decision, made once and written here.

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
here. `R6` follows `R4`, because the audit that reads across both wants the
register beside the policy rather than beside the ledger. And the position on
what may be published stays with the tool whose own behaviour it constrains.

**Two of the seven steps exist because an audit asked them and the procedure
could not**: *what does the losing repository keep*, and *is either half left
unable to answer a question it could answer alone*.

## What the shape says

**`scripts/status_eo` prints the footings**; counting the entries below is the
only honest way to count the roles, and a table here restating them would be a
copy nothing compares.

**kanon holds seven, which is the most of any tool, and that is the finding
rather than an achievement.** The register's own rule says a long section means
a tool has taken on more than it should or has not decided what it is — and the
ecosystem's mission says no tool should hold what another tool could. Every one
of the seven is a candidate to hand off, and `R32` and `R34` move with the
office by law whether anybody proposes it or not.

**Four sections are empty** — a child project usually has no users and owes
nobody an artifact, so that is the expected state rather than an omission.
**`stathmos` is the exception and says so**, holding `R30` from its first day,
which makes it not an island for a reason written beside the role. The rows
worth reading are the longest, the empty ones, and that one.
