# The tools that do not exist

**Every tool this project has named and nobody has built, in priority order —
most promising first.** Seven labelled fields each, the same seven every time,
and no argument on the page: the argument for each is in
[`why-eunoia.md`](why-eunoia.md) or in [`proposals.md`](proposals.md), and this
page links to it rather than restating it.

It brings the ideas in the account and proposals into an order somebody with
an afternoon can question: *which one of these is worth starting?* The
[glossary](../../../docs/glossary.md) records names in use; this page argues the
priority of work that does not exist yet.

**This page decides nothing**, like every other page here. An ordering is a
judgement, it is this project's judgement, and the whole of what it costs to
disagree is moving a block.

**A tool leaves this page when it exists**, rather than being marked done and
kept. **euthyna** left when eudaimonia started it and **koine** left when its
repository existed; both are now in
[`../../../docs/roles.md`](../../../docs/roles.md), which is where a tool with a
role is described. **Five more left on 2026-09-16** — **kanon** and
**epikrisis**, now members in
[`ecosystem.json`](../../../scripts/ecosystem/ecosystem.json), and **noesis**,
**hermeneia** and **mimesis**, started as child projects and documented at their
sources. **`iogos` left on 2026-09-18**, being a repository on an associate
footing since the day before; the argument its entry carried is the fork with
noesis, which is in
[`proposals.md`](proposals.md#p3--the-semantics-and-the-compiler-defined-in-lean)
and in [`why-eunoia.md`](why-eunoia.md#iogos--logos-in-a-second-proof-assistant),
where it belongs. A page that keeps its graduates is a page whose first entries
are all finished work.

**[How this page is maintained](#how-this-page-is-maintained) is at the bottom**,
and it serves [`proposals.md`](proposals.md) and [`papers.md`](papers.md) too:
the ordering rule, the fields, the naming arguments, and what a listing arrives
with are written once, there.

## nomophylax — the laws, out of the hands of the party they bind

**What:** the tool that maintains `docs/laws.md` — the rules under which a
president writes the ecosystem's history — and checks that a closed stretch
entry was written the way the laws say. **Not a lawgiver:** amendments stay a
person's, and this holds the page, watches compliance, and proposes.
**State:** `named` — suggested 2026-09-02, the day the laws were first written
down. Not audited; there is no proposal for it yet.
**Settles:** nothing in [`why-eunoia.md`](why-eunoia.md). What it settles is a
defect `laws.md` still states about itself, in its opening section as read on
2026-09-19: the president maintains the laws under `LAW 7`, and **they are
written by the people they govern.** Same defect, and the page no longer puts it
in the sharper words this entry used to quote. That is the
whole of the case for it, and the page makes the case better than this entry
does.
**Costs:** little today, because nothing depends on `laws.md` yet. **The cost is
in waiting** — the longer one party holds both, the more of the record was
produced under rules its own author could have shaped.
**Before it:** a second president. With one, the separation is theatre: there is
nobody yet whose stretch was judged by rules somebody else wrote. `kanon`
taking Stretch 1 is what makes this real rather than tidy.
**Today:** `docs/laws.md` is held by kanon, the current president, following
the 2026-09-15 handoff. Separating custody of the laws remains a proposal.
**Why here:** **first, now that `kanon` has left the page.** It is not urgent — one stretch, one president, and the maintainer
reviews every commit, which is real oversight even if it is not independence.
It is placed above the research tools because **the defect it fixes gets worse
with every stretch that closes**, and the entries written before it exists
cannot be revisited later.

*On the name: νομοφύλαξ, guardian of the laws — an office that held the statutes
and checked that magistrates acted within them. It completes a family this
ecosystem already has by accident: `dokimasia` is the scrutiny **before** office
and `euthyna` the audit **after** it; this is the one that watches **during**.
`thesmos` — θεσμός, that which is laid down — was the alternative and is the
better name if the thing turns out to be a register of rules rather than an
office that guards them.*

## euboulia — the ethical advisor to whoever holds the laws

**What:** the ethics of this ecosystem, gathered into one place and given a
reader: **`nomophylax`**, the tool that holds `docs/laws.md`. It advises and
does not decide — **the laws are held by one party, amended by a person, and
advised by this one**, and none of the three is the other.
**State:** `named` — suggested 2026-09-02, alongside `nomophylax`. Not audited;
there is no proposal for it yet, and there is a real question below that a
proposal would have to answer first.
**Settles:** nothing in [`why-eunoia.md`](why-eunoia.md). What it settles is
that this repository's ethics work is **scattered across child projects of the
tool it is meant to hold to account**, which is the same defect `kanon` and
`nomophylax` each fix in their own area, in the one area where it is least
comfortable to say so.
**Costs:** it would take custody of the two existing ethics child projects —
[`martyria`](https://github.com/ajreynol/epikrisis/blob/main/tools/martyria/README.md), the actionable half, and
[`zetesis`](https://github.com/ajreynol/epikrisis/blob/main/tools/zetesis/README.md), the general one — and **what they are
advising changes with them.** They examine the ecosystem's conduct. Under this
they would advise an office. **That is not a smaller job or a bigger one, it is
a different one**, and a proposal has to say whether both belong or only one.
**Before it:** `nomophylax`, obviously — an advisor with nobody to advise is a
register with extra steps. And a second president, for the same reason that one
gives.
**Today:** `martyria` and `zetesis` moved from kanon to epikrisis on
2026-09-17, remaining distinct child projects there. Their relocation does not
by itself establish independence from the ecosystem whose conduct they assess.
**Why here:** **second, behind `nomophylax`.** It cannot be built before the
thing it advises exists, and it is placed above the research tools for the same
reason: what it fixes gets quietly worse while nothing is done, because every
stretch that closes was assessed by a project living inside the assessed.

*On the name: εὐβουλία, good counsel — the quality of deliberating well, as
against the deliberating itself. Chosen for what it claims and does not: it
names an advisor's virtue rather than an authority, which is the whole of the
office. It shares its prefix with **eunoia** by construction rather than by
accident. Its near neighbour `bouleusis` — deliberation about particulars —
would better describe something that decides cases, which this does not;
`martyria` already holds particulars, and if this ever starts
deciding them, it has taken the wrong job.*

## aphairesis — a delta-debugger for CPC proofs

**What:** a CPC proof reducer that emits a smaller reproducer preserving a
user-selected failure or checker disagreement, with the command to replay it.
**State:** `named` — requested by the maintainer on 2026-09-21; candidate names
`aphairesis` and `ddcpc`, neither adopted. Placement has not been audited.
**Settles:** reduces the cost of investigating **O6**'s differential findings;
the [scope and naming argument](why-eunoia.md#aphairesis--reducing-cpc-proofs)
distinguish reduction from explaining a failure or deciding which checker is
right.
**Costs:** preserving step references, declarations and assumption scopes while
shrinking, and keeping the intended failure rather than an unrelated error.
**Before it:** `nothing` beyond choosing the first reproduction predicate and
CPC fragment; it need not wait for elenchos.
**Today:** anoieu's `anoieu_fuzz shrink` already reduces commands and term
fragments against a finding bucket. The proposed work adds CPC structure and a
user-supplied predicate; the existing shrinker is the baseline to improve.
**Why here:** ahead of elenchos because a reducer can serve existing failures
without building a new generator or instrumentation. First delivery: reduce
real CPC cases, preserve their chosen behavior, and record size and replay cost
against the current shrinker.

## elenchos — differential fuzzing as a derived artifact

**What:** a research-quality fuzzer for the ecosystem's checkers — coverage
guidance, a generator that assembles derivations which *should* be accepted, and
the semantics itself as an oracle.
**State:** `named` — a proposed name for the work described in the account,
not a reservation or an existing project.
**Settles:** **O6**. The arrangement manufactures its own second implementation
and the claim that this is close to free has never been tested against the other
half: whether the free second implementation is *worth having*, measured in
defects it finds in the first.
**Costs:** a differential finding names a direction and never a culprit, so
every one costs a person's judgement before it can be filed — and the generated
checker is less independent than the argument wants, since it reads the same
signature through the same compiler.
**Before it:** `nothing`. It can start without a decision being made first.
**Today:** the baseline, [`anoieu_fuzz/fuzzing.md`](https://github.com/ajreynol/anoieu/blob/main/anoieu_fuzz/fuzzing.md) —
grammar-directed generation, a mutated seed corpus, three verdict-level oracles,
and no instrumentation anywhere. It is deliberately the floor, which is what
makes *research-quality* a measurable claim rather than an adjective.
**Why here:** behind the narrower CPC reducer, ahead of the new verified
checker proposals. It has a floor already built, it needs no question settled
first, and it tests the value of generation through defects found in its
outputs.

## bebaiosis — verified checking of SAT witnesses

**What:** an executable checker and a Lean correctness theorem establishing
that a supplied assignment satisfies a formula in a stated supported fragment.
**State:** `named` — requested by the maintainer on 2026-09-21; candidate names
`bebaiosis` and `sat-witness`, neither adopted. Placement has not been audited.
**Settles:** none of the account's numbered objections directly; extends the
ecosystem's checking work to SAT answers. The
[scope and naming argument](why-eunoia.md#bebaiosis--checking-sat-witnesses)
also describe its possible use as an oracle for elenchos.
**Costs:** executable model evaluation, its correctness proof, and an explicit
boundary between parsed input, supported semantics and SMT-LIB text.
**Before it:** choose a Boolean/bit-vector fragment and witness representation;
establish which parts of Logos's semantics can support that checker.
**Today:** Logos supplies model semantics and an UNSAT proof checker; no
dedicated verified SAT-witness checker was found in the local ecosystem review
of 2026-09-21. External model validation provides comparison points, not this
artifact.
**Why here:** behind the debugging tools because it needs new formalization,
ahead of pathos because a small fragment can open a new use of the semantics
without first solving the efficient-proof-checker problem. First delivery:
accept genuine Boolean/bit-vector witnesses, reject corrupted assignments,
report unsupported input, and prove what acceptance establishes.

## pathos — an efficient verified proof checker

**What:** a checker that is both fast and verified, removing the choice the
ecosystem currently offers between ethos and the generated Lean checker.
**State:** `named`.
**Settles:** reason **4** and **open question 5**, by dissolving the trade-off
rather than measuring it, and arrangement **D**, whose only stated blocker is
that measurement. The trusted base becomes the kernel, the parser and the
statement rather than a C++ program about which nothing is proved.
**Costs:** efficiency under verification is hash consing, term sharing and
mutable state, whose invariants are the hard part of the proof. That is why the
two words have historically been alternatives, and it is where the work would
go.
**Before it:** `nothing`, and nothing else here waits on it.
**Today:** two half-answers — ethos, fast and unverified, and the generated Lean
checker, verified and unmeasured.
**Why here:** the promise is real and entirely local. It improves the
arrangement's weakest artifact and touches nothing else, so every other open
question in the account is exactly as open the day after it lands — which is
worth saying, because *we are building a verified checker* is easily heard as
*the rest is settled*.

---

## How this page is maintained

**This footer is the one place ynoia's registers state their shared
conventions.** [`proposals.md`](proposals.md) and [`papers.md`](papers.md) point
here rather than repeating it; what is specific to one of them stays on that
page.

### The registers, and what each asks

| page | its question |
| --- | --- |
| [glossary](../../../docs/glossary.md) | what names are in use, what they mean, and which work they identify. **The president's, and authoritative** |
| **this page** | **which tool that does not exist is worth building first** |
| [`proposals.md`](proposals.md) | should this be a repository of its own — and where the answer is no, whose existing tree the work belongs in |
| [`papers.md`](papers.md) | which tool that *does* exist has a result worth writing up |

The line between this page and `proposals.md` is **whether anybody has audited
it**. A name with a priority argument belongs here; a name with a verdict
against a standard belongs there, and an entry can be on both.

### Ordering

**Position is the priority**, exactly as on
[`../../../docs/board.md`](../../../docs/board.md). The first entry is the one
most worth starting; the last is the least. Reordering is done by moving a
block, and that is the main way a person changes what a register here says.

**Most promising means what it would change, weighed against whether anybody
could start it.** Both halves are load-bearing. Ordered only by what a tool
would change, the largest goes first every time and the page is useless to
somebody with an afternoon; ordered only by cheapness, it is a list of things
not worth doing. Where the two pull apart, the entry says so in words rather
than hiding it in the position.

**The ordering is the part to argue with.** Every other field summarises
something argued elsewhere, and correcting one is bookkeeping. **Why here** is
the page's own claim and the only field worth an afternoon of disagreement.

### The fields

Nothing consumes these files yet. They are written to be *parsed later* rather
than parsed now: the same labels, in the same order, always present, and a field
with nothing in it says `nothing` rather than being left out.

| field | what it holds |
| --- | --- |
| **What** | one line: the artifact, not the case for it |
| **State** | `named`, `audited`, or `parked` — plus one clause saying by whom or since when |
| **Settles** | which arguments, objections, open questions or arrangements it moves, by their ids in [`why-eunoia.md`](why-eunoia.md) |
| **Costs** | where the difficulty actually sits. One line, and not a schedule |
| **Before it** | what has to be decided or built first, or `nothing` |
| **Today** | what stands in its place, or `nothing` |
| **Why here** | the argument for this position, which is the field that changes when the entry moves |

**Entries carry no id.** They are identified by their working name, and
[`proposals.md`](proposals.md) works the same way except for the audited `P<n>`
proposals, whose numbers are cited from outside this project and stay.

### Arguing about names

The president's [glossary](../../../docs/glossary.md) is the authoritative name
register: what a name means and which work it identifies. Ynoia argues how a
name fits its work, and keeps no list of taken, reserved or free names.

**A name should describe what the work does to its subject.** Explain the fit in
one sentence, then state the strongest likely misreading. **If the explanation is
strained, revisit the scope rather than searching for a more elaborate word** —
a name that needs a paragraph is telling you the scope is undecided. Greek draws
on vocabulary the ecosystem already uses, and the etymology is an argument a
reader can challenge; a descriptive name can earn its place too. Distinctive
names help a reader tell a project from its subject, which is the reason for the
convention rather than a reason to force a word onto unsuitable work.

For an **existing** name, cite its glossary entry and the project's own
explanation, and say which reading works, which misleads and why. Suggest a
correction; do not keep a competing definition here.

For **proposed** work, put the candidate name, scope, etymology, alternatives
and objections with its entry. A suggestion reserves nothing, so check the
glossary and the existing trees before treating a candidate as available.
[`P2`](proposals.md#p2--the-ecosystems-governance-out-of-the-analyzer) and
[`P1`](proposals.md#p1--central-tooling-for-reporting) show the form: what the
name claims, and the objection to it. They preserve the choices considered then;
the glossary records the names in use now.

When a person adopts a name and the work exists, its definition belongs in the
glossary, and when the work moves the inventory and the glossary entry move
together. **Ynoia keeps the reasoning, not a second register to synchronise.**

### What a listing arrives with

**None of this is a gate.** A request that arrives with none of it is still
listed, and the worst outcome is an entry saying `nothing` in several fields,
which is information rather than a rejection.

**The one thing worth having first is the vision** — not code, not a design, not
a schedule, but a written statement of what the tool is *for*: the artifact it
would produce, the consumer that would read it, what it refuses to answer, and
what would show the idea was wrong. The judgement is made against that, and
where there is none the audit has to invent one in order to have something to
weigh — **an audit that invents what it is judging is grading its own work.**

**How strongly it is recommended depends on who ends up holding the thing.**

- **Internal** — a child project, a tool a member would fetch, shared machinery.
  **Strongly, and it costs nothing**, because the vision is already owed
  elsewhere: the policy asks a child project to open with its question, its
  goals, its wishue and what is out of scope, and the ecosystem's vision asks
  that the consumer be named before the work starts. A request that arrives with
  those answered can be judged the day it arrives.
- **Standalone** — its own repository, its own maintainer, possibly somebody who
  has never heard of this ecosystem and owes it nothing. **Much more weakly, and
  the asymmetry is deliberate**: the vision would be theirs to write, and asking
  for it first asks them to commit to a shape before they have the artifact that
  would tell them which shape is right. Several entries here were named with no
  vision at all — a Greek word, a paragraph in an account, an argument that
  their absence distorts something — and are better for it. The honest minimum is
  one line on the artifact and one on what its existence would change.

Enough to fill the fields, or an honest gap where it cannot: a **working name**
checked against the glossary and the existing trees; **one line on the artifact**;
**what it would settle**, by the ids in [`why-eunoia.md`](why-eunoia.md) where it
touches the account; **what stands in its place today**, including `nothing`,
which is the field most often omitted and the one that most often changes the
position; and **where the vision is written down**, or `nothing`, said plainly.

**A listing with no vision is still made**, as `named`, with the missing
statement recorded as the first thing in the way. What it cannot be is
*audited*: the standard in [`proposals.md`](proposals.md) asks questions a scope
has to exist to answer, and run against a gap it returns a verdict about this
project's imagination rather than about the idea.
