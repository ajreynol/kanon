# ynoia

*The name is **"why Eunoia"**, elided. It keeps the root and drops the
judgement: εὔνοια is εὖ + νοῦς, **good thinking** — and this project removes the
εὖ and asks whether the thinking is good. That is a claim somebody can disagree
with: if the arrangement is obviously right and the question idle, the name is
wrong and so is the project. It also follows the sibling convention — [anoieu](https://github.com/ajreynol/anoieu) is
Eunoia read backwards, and this is Eunoia read as a question.*

A child project under [`docs/policy.md`](../../docs/policy.md). Started by a
human, read-only, and not part of the governance commands this repository ships.
Its written arguments and proposal reviews serve the ecosystem. Kanon carries it in
[`ecosystem.json`](../../scripts/ecosystem/ecosystem.json) and
`scripts/eo_status_audit` lists it among the advertised children.

This project is tied to the presidency: when the office changes hands, ynoia
moves with its work and roles to the repository that holds the presidency.

## The question

**Does the Eunoia ecosystem's arrangement earn its machinery — and what is it
missing?**

An SMT solver has found an answer and is asked to justify it. It can emit a Lean
proof and have Lean check it, or it can emit a proof in a fixed calculus written
in a small language, have a checker check that, and *also* compile the calculus
into a Lean development that says its rules are sound. The ecosystem chose the
second. It is more machinery, and the case for it has been made in conversation
and never written down where somebody could attack it.

So: write it down, make the strongest case against it, and see which survives.

## Goals, in order

1. **The argument, both directions.** The case for the calculus, the case for
   doing it in Lean instead, the general objections to each, and six coherent
   ways the ecosystem could be arranged — stated so that somebody who disagrees
   has something to disagree *with*. [`docs/why-eunoia.md`](docs/why-eunoia.md).

2. **The tools that do not exist.** Every argument above is stated relative to
   what exists today, so the cheapest way to see which arguments are about the
   *arrangement* and which are merely about its *current state* is to name the
   work that would move each one. Some of those names have since been taken up
   as real projects, which is the closest thing this project has to a result.
   The register of the ones that have not, in priority order, is
   [`docs/tools.md`](docs/tools.md); the arguments stay in the account.

3. **The naming arguments.** Whether a name describes the work, what it might
   mislead a reader into expecting, and why an alternative would fit better.
   [The naming guidance](docs/tools.md#arguing-about-names) states the approach;
   proposals carry the individual arguments. The president's
   [glossary](../../docs/glossary.md) is the authoritative name register.
   Ynoia neither duplicates it nor reserves names.

4. **Auditing proposals.** Whether a given idea deserves a repository of its
   own is the account's general question applied to one case, with a decision
   attached — so it is answered here, against a stated standard, in
   [`docs/proposals.md`](docs/proposals.md) — which since 2026-09-19 also holds
   the wants that are work rather than repositories, with an argument about
   whose tree each belongs in. The output is an argument with a
   recommendation at the end. **It approves nothing:** a repository is a claim
   on a shared namespace and on years of somebody's attention, and the policy
   reserves that for a person. kanon carries proposals in, because it is the
   only tool that may address a child project directly.

5. **Which projects have a paper in them.** No shared document asks a
   repository to write one — the recommendation that used to be in `policy.md`
   was removed on 2026-09-16 and `vision.md` never carried it — so the question
   is a judgement with nothing behind it but the argument, and it is made here
   against a stated standard in [`docs/papers.md`](docs/papers.md). The
   commonest verdict is **no**, this project returns it about itself first, and
   a repository's own stance on publishing outranks anything on the page.

6. **Wishue: what would settle it.** An argument that cannot be lost is not
   worth having. The account carries what would change our minds and one
   experiment that would settle more than any further argument. Turning that into
   something somebody could actually run is the wishue, and it remains one.

## What this project does not do

The boundary matters more than the goals, so it is stated first.

- **It does not decide anything.** Nobody here has the authority to rearrange an
  ecosystem, and an account that reads as a decision has overstepped. The
  arrangements it describes are options laid out fairly, not a recommendation
  with the alternatives listed for form's sake.
- **It does not report defects.** Where reading the ecosystem turned up something
  actually wrong in somebody's file, that is a finding: it leaves through
  [anoieu's reporting discipline](https://github.com/ajreynol/anoieu/blob/main/bug_db/reporting-policy.md) with an id and a
  state, and never through here. This project's output is argument.
- **It does not speak for kanon or anoieu.** Both are participants in the
  argument. Hosting this project does not make its account neutral.
- **It does not commit anybody to the tools it names.** A named project with a
  paragraph attached is a description of work that would change an argument, not
  a roadmap, not an assignment, and not a claim that anybody intends to build it.
- **It does not keep the name register.** Names in use and their meanings belong
  in the [glossary](../../docs/glossary.md). Naming arguments here cite it.
- **It does not describe the language.** What Eunoia *is*, independently of any
  checker, is a different question with a different child project.

## Status

**Now also the place it is argued which projects are worth a paper**, which is
the second thing this project has been asked to produce for somebody else. It is
the same judgement the account makes about work that does not exist, pointed at
work that does, and it is the page most likely to be wrong in a way somebody
notices — which is an improvement on being unread.

**Also the place proposals are audited**, which is the first thing this
project has been asked to produce for somebody else rather than for itself. Its
first audit, `P1`, was carried to a decision and a repository was approved on the
strength of it — which is a consumer in the sense the vision means, and would
be the thing that earns this project a place there. Whether it has is not this
project's call.

**The account exists and is long.** Nothing in it has been argued with by
anybody who disagrees, which is the whole point of writing it and has not
happened yet. It has reached no consumer and so has earned no place in
[`docs/vision.md`](../../docs/vision.md) — with one qualification: of the seven projects it named, four —
**euthyna**, **noesis**, **hermeneia** and **mimesis** — have since been started
as child projects: the first three in eudaimonia's tree, and mimesis there too
until it moved to eunoia on 2026-09-19. Whether that is this account's doing or
convergence is not something this project can establish about itself.
`eo_init` now reads the president's glossary directly; it does not
depend on ynoia's naming arguments.

## Is there a paper in this?

**No, and this project says so about itself first** so that the verdicts it
returns about other people's work read as judgements rather than as modesty spent
on others.

This project's output is **argument**, and it has taken no measurement. A paper
assembled from it would be a position piece about how to arrange an ecosystem,
written by the ecosystem, with nothing in it a reader could check. The account is
worth reading and worth disagreeing with; neither of those makes it a result.

Stated because it used to be asked: [`policy.md`](../../docs/policy.md) had a
rule that a child project says whether a paper exists for it, what the plan is,
or that there is nothing in it worth writing up, and that rule went in the same
2026-09-16 pass that removed the convention behind it. **The answer is kept
anyway** — it is the third of the three, it is the commonest, and a page that
drops its own verdict the moment nobody is checking has told you what the
verdict was worth. [`docs/papers.md`](docs/papers.md) asks the same question of
other tools.

## Layout

[`docs/README.md`](docs/README.md) indexes this project's documents.
