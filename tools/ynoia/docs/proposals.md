# Proposals

**Work that does not exist yet, audited: should it be a repository of its own —
and where the answer is no, whose existing tree it belongs in.** One section
each.

**The two used to be separate pages and were one question.** `requests.md` held
work that wanted doing but not a repository, and every entry on it carried a
paragraph explaining why it was a request and not a proposal — seven pages
answering the question this page asks, filed under the answer instead of under
the question. They were merged on 2026-09-19, and the request ids went with the
merge: `R1`–`R8` collided with six role ids in
[`../../../docs/roles.md`](../../../docs/roles.md), and an entry here is
identified by its working name, exactly as on [`tools.md`](tools.md). **The
`P<n>` ids stay**, because they are cited from outside this project.

**Order:** the audited proposals first, then the placed work, newest first
within each. Position is *not* priority here — a decided audit and an open want
are not comparable — which is the one place this page departs from
[the shared conventions](tools.md#how-this-page-is-maintained), where the
ordering rule, the naming arguments and what a listing arrives with are written
once.

Every entry opens with the same labelled lines, because what a person is being
asked is short and should not have to be extracted from an argument:

**What:** one line · **Verdict:** needed | welcome | not yet | no | **placed in
`<tree>`** · **Where:** for placed work, the tree it would live in, argued
rather than assumed · **State** or **Decided:** open, or who decided and when.
Audited proposals add **If approved**, the first three steps.

**The verdict is about us, not about the tool.** A proposed tool is an
independent thing whose owner decides what it is and whether it ever joins this
ecosystem, and no audit here binds any of that. What this page decides is
whether **we** want to depend on it:

| verdict | means |
| --- | --- |
| **needed** | the ecosystem will take a dependency on it. We want it built and we intend to use it |
| **welcome** | worth building, and we are not depending on it. *Go and do it* — nothing here waits on you and nothing here breaks if it never appears |
| **not yet** | the thing it would fix is not a problem yet. Says what would change that |
| **no** | the argument does not hold |
| **placed in `<tree>`** | it wants doing and does not want a repository. The argument is about whose tree, and a placement is not a ticket in anybody's tracker |

The distinction that matters is between the first two, because they cost the
builder different things. *Needed* means somebody will be waiting, which is a
reason to build it and also an obligation nobody has agreed to. *Welcome* is a
smaller and often kinder answer: build it for your own reasons, on your own
schedule, and if it turns out well we will come to you.

**Nothing on this page approves anything.** Creating a repository claims a name
in a shared namespace and years of somebody's attention; the policy reserves
that decision for a person. A placement is smaller and still not a claim on
anybody: whether a tree carries the work is that tree's, and nothing here is
filed anywhere. Work that a member should act on reaches them through
[`../../../docs/discussion.md`](../../../docs/discussion.md), by a person, or
not at all.

The account asks whether the ecosystem's arrangement earns its machinery; this
page applies that question to one piece of work at a time.

## The standard

Four questions, in order. A proposal that fails an early one does not need the
later ones answered.

1. **Does it exist anywhere yet?** Code written twice is evidence; code written
   once is a design, and a design does not need a repository. The strongest
   signal available is two implementations that turned out identical, because
   that is a fact rather than a prediction.
2. **How many consumers, really?** Two is the number at which sharing looks
   obviously right and usually is not: the second consumer discovers what is
   actually shared, and a third shows whether the answer generalises or was a
   coincidence between two.
3. **What does a repository buy that `tools/` in an existing one does not?**
   Isolation, a release surface, an independent maintainer — each real and each
   a cost. The ecosystem already shares code by pinning a commit and fetching,
   so the question is never *how would anyone get it* but *what breaks if it
   lives in somebody's tree*.
4. **Who maintains it when the enthusiasm is gone?** A repository is a standing
   obligation. If the answer is "whoever needs it next", the proposal is for a
   directory.

**Two-consumers is not automatically a refusal**, and reading it that way is the
mistake this standard made on its first use. The count matters while the shared
*format* is still being discovered. It matters much less when the thing is
plainly needed by every future member, and it points the other way entirely when
the alternative is one repository hosting everyone else's shared machinery —
which makes its owner the de facto maintainer of everybody's, a larger
commitment than a separate repository rather than a smaller one. **Ask who ends
up holding it, not only how many use it.**

**A transfer asks two more**, added by `P2` and kept because a page that audits
*should this be a repository* with no vocabulary for *should this move* will
keep producing confident answers to a question nobody asked. **5. What does the
losing repository keep?** **6. Is either half left unable to answer a question
it used to answer alone?**

All of them want something written down before they can be asked, which is why
[what a listing arrives with](tools.md#what-a-listing-arrives-with) recommends
the vision exist first. An audit run against a scope nobody has stated returns
*not yet* by default, which looks like a judgement and is not one.

The likeliest right answer is often **not yet, and here is what would change
that** — a threshold somebody can watch for rather than a refusal. It is not the
default, and a standard that reaches it every time has stopped being applied.

## P3 — the semantics and the compiler, defined in Lean

**Name:** **`noesis`** — already in use and recorded in the
[glossary](../../../docs/glossary.md); there is no name to choose here, and the
argument for it is in [`why-eunoia.md`](why-eunoia.md). That is what makes this
audit different from `P1` and `P2`: they were asked *should this exist, and what
should it be called*, and this one is asked **where does a thing everybody
already has a name for actually live** — the question the register cannot answer
and this page can.
**What:** the `.eos` semantics written as Lean definitions over the SMT-LIB model
logos already carries, the compiler as a Lean metaprogram over those
definitions, and a theorem relating what it emits to what they say
**Verdict:** **not yet** — on the *repository* question, and two of the three
prerequisites already have owners who are not it
**If approved:** it would not be approved into existence; the first three steps
are the prerequisites below, in three trees that are not this one, and the
repository question returns when they meet
**Decided:** **open.** Raised from the compiler side in `ethos`
`docs/noesis-readiness.md`, which argues the entry's stated blocker is closer to
discharged than [`tools.md`](tools.md) assumes. Carried in and audited here
because the *placement* question is this page's and not that document's.
*Amended 2026-09-16: `noesis` has since been started as a child project in
eudaimonia, which is the placement this audit recommended if it had to start
now. The repository question is unchanged and still open; what is no longer true
is that the thing does not exist.*

### The proposal

Noesis is not a new tool beside the others. It is **a second implementation of
`ethos-eoc`'s back half, in a different language, with a theorem attached** —
and that is what makes its placement hard in a way `koine`'s and `kanon`'s were
not. Both of those were machinery looking for a home. This is a rival to a
working tool, proposed while the tool is being actively improved, by the tree
that maintains it.

The role it would hold is already written down as vacant.
[`roles.md`](../../../docs/roles.md) `R13` — the shipped semantics sets — carries
this line: *"In the absence of any other definition, what a `.eos` file means is
what this role makes of it, which is a larger responsibility than it looks"*,
and its **Not this role** ends *"any account of the semantics that does not
depend on this compiler, which is **nobody's**."* That is noesis, named as a hole
by the inventory before this page was asked about it.

### Against the standard

*Does it exist anywhere yet?* **At the time of this audit, no — written zero
times**, below even the standard's floor of code written once. *Amended
2026-09-16: it now exists as a child project in eudaimonia at `tools/noesis`,
with a charter. The verdict is about a repository and is undisturbed by that.*
Its two halves each exist once, in different trees and different languages — the
`.eos` sets as `R13`, the Lean SMT model as `R18` — and neither is the artifact.
This alone settles the verdict; the rest is answered anyway, because the
*placement* question survives it.

*How many consumers, really?* Two eventually — logos and eudaimonia — and both
would be **replacing** what they consume rather than adopting something new.
That is a harder shape than `koine`'s four consumers of machinery that already
existed twice. **A consumer that must abandon a working path to adopt yours is
not a consumer until it says so.**

*What does a repository buy that `tools/` does not?* Today nothing, because
there is nothing to isolate or release. Later everything: the moment the Lean
definitions are something logos and eudaimonia **fetch rather than read**, they
need a release surface, and no host's `tools/` can give them one — a research
project writes only inside its own directory, and a directory other trees import
is not an island.

*Who maintains it when the enthusiasm is gone?* Unanswerable while the fork is
open. [`why-eunoia.md`](why-eunoia.md) is explicit that noesis and `iogos` "pull
opposite ways" on where the semantics is defined, and a repository whose charter
depends on an undecided fork is one that will be rewritten or abandoned.

*What does the losing repository keep?* `ethos-eoc` keeps `R12` — the compiler
producing the SMT-LIB and SyGuS verification conditions, which noesis's own
account concedes it does not replace. What it would lose is `R13`, the role that
currently makes *what a `.eos` file means* a compiler's private answer.

*Is either half left unable to answer a question it used to answer alone?* Yes,
and it is the interesting one: **what does this signature's semantics say** is
today answered by running the compiler. After noesis it is answered by reading a
definition, and the compiler becomes accountable to something outside itself.
That is the whole benefit and also the cost — two artifacts that must agree,
which is `O6` in a new place rather than `O6` removed.

### Where it would live if it is not a repository

The argument runs between two of the policy's rules for a research project: that
one which does not use its host's evidence should be its own repository, against
the refusal to advertise.

**`ethos`. No, and it is the tempting answer.** The evidence test fits — the
first task is validating the Eunoia embedding against `src/`, entirely that
tree's evidence — and so does the policy's description of what a research project
is for. Two things kill it. `ethos` is `cvc5/ethos` and its footing is
**candidate**: it is the only tree in this argument the ecosystem does not own.
And **the refusal to advertise cannot be honoured there** — a `tools/noesis/`
inside the compiler's own tree *is* read as the compiler's position whatever its
README says, in a repository with outside contributors and review.

**`anoieu`. No, on the evidence test.** It is where the name was coined, and
where sapheneia and ynoia sat until 2026-09-15 — which is exactly why it is worth
refusing: anoieu's evidence is signature analysis, and noesis's is compilation
and Lean. Another child there would make anoieu the ecosystem's speculation
warehouse.

**`eudaimonia`. Yes, if it must start now.** Its blocker *is* noesis's
prerequisite — the account says open question 7 "has to be answered first" and in
the same breath that it "is eudaimonia's own blocker", and `R14` is that line by
definition. It has the child-project precedent in `euthyna`. And it is the
consumer that would have to absorb the result, on a member's footing, at no cost
to a shared namespace.

### What has to be true first

Three prerequisites, none of which needs this repository or this name, and each
of which already has an owner:

| what | tree | why it is theirs |
| --- | --- | --- |
| Validate the Eunoia embedding against `src/` — the 1,215 lines of `eo_desugar*.eo` and `native_embed.eo` that are a semantics of Eunoia nothing has compared with the C++ | **ethos** | `R10` is "the implementation every other reading of the language is compared to"; both readings are in that tree and neither has been laid against the other |
| Answer open question 7 against more than one calculus | **eudaimonia** | `R14` — "the subject here is the shape, never the content" — is that line, and it is the only tool that has run the compiler over more than one calculus |
| An account of `.eos` that does not depend on the compiler | **sapheneia**, if its charter is extended | `R20` is a second reading of a language whose only description is a manual for a program; `.eos` is the same problem one language over |

The third is the cheapest move available anywhere in this ecosystem and it is
not this page's to make. Sapheneia excludes `.eos` deliberately — *"folding it in
would double the scope before the first goal is met"* — and a charter is the
thing a human agreed to. **So the live question is not where noesis lives. It is
whether sapheneia's charter extends to `.eos` once its goal 1 lands**, and that
is a question for the person who started it.

### The threshold, and the two risks

This verdict changes to **welcome** when the fork with `iogos` is decided in
noesis's favour, since until then a charter cannot be written. It changes to
**needed**, and to a repository rather than a child project, when the Lean
definitions are something logos and eudaimonia would **fetch rather than read** —
at which point Q1 is answered by the thing existing, Q2 by two consumers that
have said so, and Q3 by the island test. Neither threshold is a schedule and
neither is close.

**The first risk is that *not yet* is read as *not important*.** Noesis is the
highest-leverage entry on [`tools.md`](tools.md) and this page does not dispute
it. What it disputes is that the thing to start is a repository, when the same
month's work distributed across three trees that already own the questions would
move the entry further — and would move it whichever way the fork goes, which no
work done inside a noesis repository can claim.

**The second is the mirror of it:** three prerequisites in three trees is an
arrangement with no owner, and the failure mode is that all three stay one
person's afternoon away forever.

### What this audit cannot check about itself

It was drafted from `ethos`, which is the tree whose work it cites as having
partly discharged the blocker, and whose compiler noesis would replace. Both
directions of bias are available and they point opposite ways, which is not the
same as cancelling. The part checkable by running something is the measurement
in `docs/noesis-readiness.md` §2 — 68 agree, 0 disagree, 9 refused, over
`ethos/tests/` — and that is the part to attack first.

## P2 — the ecosystem's governance, out of the analyzer

**Names:** **`kanon`**, then `thesmos`, `epistates`, `oikonomia`
**What:** the policy every member is checked against, the checker that decides
it, the inventory of who is in, and the scripts that start, welcome, join and
install a tool — in a repository that is not also the tool that files findings
against you
**Verdict:** **needed** — the ecosystem already depends on this; the question is
whose tree it lives in
**If approved:** a person creates the empty repository → the policy, its checker,
the inventory and the `*_eo` scripts move there in one commit, with anoieu
becoming a consumer of them → every member's CI pin changes once, at a moment
somebody chose
**Decided:** **done, and not as proposed.** Raised by the maintainer on
2026-08-31; the transfer completed on 2026-09-15. Audited here before the
decision existed, which is the only thing this page is for — and the divergence
between what was proposed and what happened is recorded below rather than
smoothed away.

### What happened, and where it diverged

*Amended 2026-09-19, reading the register and the role assignments.* **The
audit's four pieces did not move to one place. They went to three**, and the
split is the interesting part:

| the piece | where the audit put it | where it is |
| --- | --- | --- |
| the policy, the vision, the laws | kanon | **kanon**, as proposed |
| the inventory of who is in | kanon | **kanon**, as proposed — `scripts/ecosystem/ecosystem.json` |
| the checker that decides the policy | kanon | **anoieu**, unmoved — `policy_check/`, held under `LAW 3.3` |
| the scripts that start, join and install a tool | kanon | **koine**, under roles `R35` and `R16` |

**The verdict survives the divergence and the argument for it does not.** *The
judge stops being the prosecutor* was the whole of the case, and it is only half
true: the party that writes the rule is no longer the party that files findings
against you, but the party that **decides** the rule mechanically still is.
anoieu publishes the policy contract, and kanon asks for contract 1 like anybody
else. That is a smaller separation than this audit argued for, and nobody has
argued it is the right one — it is what fell out of moving the documents first.

**The `If approved` line predicted a cost that was not paid.** *Every member's
CI pin changes once* did not happen, because the checker did not move: a member
pinning anoieu on 2026-08-31 is still pinning anoieu. The move was therefore
cheaper for members than the audit expected, and the reason is exactly the piece
that stayed behind.

**What this audit got wrong is worth keeping.** It counted the question as
*whose tree does governance live in* and the answer turned out to be *which of
governance's four pieces*, which is not a question it asked.

### The names

These were the alternatives considered before kanon existed. The
[glossary](../../../docs/glossary.md) records its current name and meaning; this
table preserves the arguments, not a list of available names.

| name | Greek | the claim it makes | the objection to it |
| --- | --- | --- | --- |
| **kanon** | κανών, *the measuring rod* — the standard a thing is held against | the policy is exactly a rod: the checker lays it alongside a tree and reports where the tree is short. It names the instrument rather than the authority, which is what this actually is | *canon* in English is about scripture and lists of approved works, and a governance repository is the one place that misreading does real harm |
| **thesmos** | θεσμός, *a thing laid down* — an institution before it is a law | it is the arrangement itself, written down: what a repository is, what a member owes, what a child project may do | heavier than the thing. A `thesmos` sounds founding and permanent, and this is a policy somebody amends on a Tuesday |
| **epistates** | ἐπιστάτης, the presiding member of the council, for one day | presides and does not rule: it runs the meeting, and the decisions stay with people. That is precisely the relationship the policy has to members | needs the footnote to land at all, which weakens the argument that it describes the work |
| **oikonomia** | οἰκονομία, *management of the house* | the unglamorous half is true: the inventory, the checkouts, who lives where | *economy* in English, and it says nothing about the rules, which are the part that matters |

**Recommended: `kanon`.** The
[naming argument](tools.md#arguing-about-names) favours a word for what the tool
does to its subject, and this one *measures a tree against a stated standard*.
The objection is real and worth stating on the repository's own front page: this
is a rod, not a canon, and nothing in it is scripture.

### The proposal, and the argument

anoieu was three things and its own README said so: an analyzer, a reporting
system, and *the place the Eunoia ecosystem's shared policy is kept*. The third
had grown into the policy, the checker that runs in every member's CI, the
inventory, the status audit and the checkout map. That is a tool, and it is not
the analyzer.

**The argument is not that the machinery is bad. It is that one repository both
writes the rules a member is judged by and files the findings against them.** A
member disputing a finding is disputing with the body that also defines what
compliance is, and the only thing separating those two roles was that the same
people are careful. Separation is cheap now and expensive later.

*What does the losing repository keep?* The analyzer, the fuzzer, the findings
ledger and the reporting workflow. The line to argue is
[`reporting-policy.md`](https://github.com/ajreynol/anoieu/blob/main/bug_db/reporting-policy.md),
a position shared with dokimasia about what may be published — governance by any
reading, and also the document anoieu most needs to own, since it is the one
constraining anoieu's own behaviour. **Recommendation: it stays**, and the
governance repository holds what a repository *is*, not what a report may say.

*Is either half left unable to answer a question it used to answer alone?* One:
*does this finding's project comply?* After a split the policy lives in one tree
and the findings in another, and the audit reading across both needs two
checkouts.

### The risk worth writing down

A policy separated from the tree it was written for can drift into rules nobody
has run against a real repository — the failure the old arrangement structurally
could not have, because the policy's author was also its first victim. The
mitigation is that the checker moves *with* the policy and anoieu stays a
consumer, so every rule is still run against at least one tree that did not
write it. **If the governance repository ever ships a rule with no checkout
behind it, this proposal was wrong.** *2026-09-19: the checker did not move, so
the mitigation holds by accident rather than by design — anoieu is still the
tree every rule is run against first, because it is the tree the checker is in.*

## P1 — central tooling for reporting

**Name:** **`koine`** — chosen, and recorded in the
[glossary](../../../docs/glossary.md)
**What:** the shared machinery of the reporting loop, fetched by every tool that
runs one, so the protocol has one implementation instead of one per member
**Verdict:** **needed** — we intend to depend on it
**If approved:** a person creates the empty repository → its owner decides what
it is → joining this ecosystem is their choice, and `eo_init` / `eo_join` are
offered, never required
**Decided:** **approved 2026-08-31** by the maintainer, as `koine`. Proposed by
dokimasia in its `D4`; audited at anoieu `441b562`, revised the same day. The
repository did not exist when it was approved — approving it is not creating it
— and it exists now, as a member.

### What it turned into

*Amended 2026-09-19.* **The repository exists and holds something other than
what this audit described.** The loop below — a script run in the project a
finding is about, a script run at home once it has replied, prompts in a
document, a drift check, a postmortem with one block per run — **was retired at
both ends**: anoieu removed its half on 2026-09-19 and dokimasia raised the same
retirement as their `D17`. What koine holds instead is `bug_db_manager`, the
programs an owner invokes to maintain its own database of findings, plus the
shared command set under roles `R35` and `R16`. Three customers pin it.

**The verdict `needed` was right and the artifact was not.** *One implementation
instead of one per member* is what happened; *the reporting loop* is not the
thing it turned out to be shared about, because the loop itself did not survive.
The audit's own open question — *how a consumer fetches and calls the shared
check is the owner's to design* — is why it could be wrong about the artifact
and still right about the repository.

### The names

Five candidates considered before `koine` was chosen. The
[glossary](../../../docs/glossary.md) records the adopted name; this table
argues the alternatives and makes no claim about their availability today.

| name | Greek | the claim it makes | the objection to it |
| --- | --- | --- | --- |
| **koine** | κοινή, *the common tongue* — the shared dialect that let people who spoke differently understand each other | the tool is a shared language between tools, which is exactly what a fixed reply format is | the strongest metaphor and the least literal. It says nothing about *reporting*, and a reader may take it as "the common one" |
| **angelia** | ἀγγελία, *the message* — not ἄγγελος, the one who carries it | it fixes the form of what passes between tools and never decides what is sent | close to *angel* in English, which is a distraction it never quite escapes |
| **homologia** | ὁμολογία, *saying the same thing* | two implementations agreeing is the whole purpose, and the drift check is literally this | describes the test rather than the tool; if the shared code grows past checking, the name stops fitting |
| **paradosis** | παράδοσις, *a handing over* | a finding handed to whoever owns it, which is the act the loop exists to perform | also means *tradition*, and a tool named for handing things down sounds like it decides what is handed |
| **typos** | τύπος, *the stamp that shapes* — hence a pattern | the tool is the mould the reply format is pressed from | reads as *type* in English, which is both too transparent for the convention and wrong about what it does |

**Chosen: `koine`.** The thing actually being shared is not code — it is the
format two tools must both speak in order to be understood, and the code follows
from that. The argument against is the honest one in the table: it is a name
about *communication in general* attached to a tool about reporting in
particular.

**The name is ours to decide, and it is decided before the repository exists** —
a name chosen at build time is a name nobody else can plan around. What is
*theirs* is everything after: the scope, the interface, the pace, and whether
the tool ever joins this ecosystem.

### The proposal, and what was shared

anoieu and dokimasia had both built the same loop, and dokimasia built theirs in
an afternoon by reading anoieu's. What was shared was identified rather than
guessed at: the drift check, around sixty lines and a copy in one direction; the
reply-file finder and the branch-state reporter, which are pure git and
identical; and the reply format, fixed by prose both sides already followed.
What was not shared was equally clear — the prompts, because the subjects
differ, and what settles a row, which each tool names for itself.

**Not in scope at the start:** a shared register format or shared issue
management. anoieu's was generated and dokimasia's curated, and fixing a format
then would have fixed it before either side had evidence that theirs was right.

*The implementations this section pointed a builder at are gone with the loop.*
They are in anoieu at
[`256939e1fb03`](https://github.com/ajreynol/anoieu/blob/256939e1fb03/docs/reports/reporting-workflow.md)
and in dokimasia's `workflows.md` at the same date, and the interesting part was
always the *differences* — dokimasia carried a fourth triage label, `answered`,
for a row that is a question and names no branch, which anoieu's could not
express.

### Still open, and approved anyway

**Who maintains it.** The audit named this as the question to settle before
approving, and the approval came without it settled. That is a person's call to
have made and it is recorded here rather than smoothed over: if the answer turns
out to be *anoieu under another name*, this is a directory with extra ceremony.

**Its interface.** How a consumer fetches and calls the shared check was not
specified, deliberately: it is the owner's to design, and a proposal arriving
with an interface attached would be a specification wearing a recommendation's
clothes.

### What changed, and why

The first audit of this proposal recommended **not yet**, on the grounds that
two consumers cannot distinguish what is shared from what one of them wrote
first, and that the pin-and-fetch mechanism already reaches a member without a
new repository. Both remain true and neither is decisive, which the audit missed
by counting consumers instead of asking who ends up holding the thing. The
correction is recorded here rather than made silently, and
[the standard](#the-standard) has been amended so it does not produce the same
answer next time.

---

**The entries below wanted doing and did not want a repository of their own.**
They carried `R<n>` ids until 2026-09-19 and no longer do; the withdrawn one —
a research request on whether unambiguous command syntax makes an ecosystem
efficient, rolled back on 2026-09-02 — is not restored by the renumbering going
away, and stays withdrawn.

## Ranking a repository's documents by what depends on them

**What:** a program that reads a repository's documents and orders them by **how
much depends on them**, so that *which of these matters* is a measurement rather
than an opinion. The immediate use is deciding what to merge or delete; the
lasting one is that **nobody currently knows which pages are load-bearing**,
which is a strange thing not to know about a project whose central policy is
about documents.
**Verdict:** **placed in `anoieu`**, which has the most documents and keeps the
only program that reads a tree's documents at all. *The original reason has
expired:* this entry used to say anoieu kept the documentation policy, and that
moved to kanon's [`policy.md`](../../../docs/policy.md) on 2026-09-15 — so the
rule and the instrument are now in different trees, which argues for placing it
wherever it will actually be written rather than for moving it. It should work
on any member's tree.
**State:** **open.** Requested by the maintainer, 2026-09-02, on noticing that
`docs/` had grown to 30 files and roughly 18,700 lines.

**Four signals are already computable and none is importance on its own:**
**inbound references**, the closest single proxy and the cheapest;
**whether a check reads it**, which is a harder fact than any link count, since
a document that is ground truth for a test cannot be deleted without breaking
something; **whether it leaves the repository**, published to members or pinned
by somebody else's CI, which cannot be changed unilaterally at all; and **age
against the tree it describes**, which
[`policy_check/currency.py`](https://github.com/ajreynol/anoieu/blob/main/policy_check/currency.py)
already measures and which this should read rather than recompute.

**The question underneath is the interesting one.** Some documents exist because
a question needs a home; others because a subject was split. The second kind is
what accumulates and is invisible to every signal above — four essays that
cross-reference each other and are read by nobody score exactly like four
independent pages. **A candidate test, offered to be argued with: a document
only ever reached through its siblings is a section, not a document.** That is a
claim about link topology and is checkable, which is why it is worth writing
down rather than leaving as taste.

**What would make it wrong.** A page with no inbound links and no reader may
still be the most important thing here — `vision.md` would rank low on most of
these signals and governs everything. **Any tool that recommends deletion by
score is dangerous**, so this should rank and report and never propose. The
tool's job is to make sure a person is looking at the right ten files rather
than all thirty.

## What recency proves about a change

**What:** the sibling question to cryptography below. That one asks what a
signature can establish about this arrangement; this asks **what a timestamp
can.** The claim to test: **work that happened in a short span has changed
little, so removing it is cheap — and the window closes.** If it holds, recency
is evidence rather than context, and an ecosystem can correct itself without
arguing every case on its merits.
**Verdict:** **open on placement.** It was placed in anoieu on the reasoning
that the interface protocols were theirs; that reasoning has expired twice over
— the `PROTO-n` register was retired outright on 2026-09-18, and this project no
longer sits in anoieu's tree. The subject is a question about evidence rather
than about a page.
**State:** **open.** Raised by the maintainer, 2026-09-02, out of a live case.

**The case that raised it.** Three commits over ten minutes, four files, and the
direction was wrong from the first one. The person saw it before the agent did —
the agent was inside the frame — and each turn added structure that made the next
correction more expensive. **The rollback was cheap only because it was fast**,
and nothing had cited the work yet. The case produced the former
[`PROTO-17`](https://github.com/ajreynol/kanon/blob/f2262444e2d9dafa823820103fdaafac7252500a/docs/protocols.md#proto-17--the-emergency-protocol),
which let a person stop a direction in one word and treated recency as grounds
for removal. **The claim behind it was never established.**

**What it would ask.** *Is the claim true, and where does it stop?* — a small
recent change to a load-bearing page can be depended on immediately, and one to
a page nobody reads can sit for months harmlessly, so **recency may be a poor
proxy for what it stands in for**, which is *how many things now rest on this*.
*What is the better measure, and is it computable?* — inbound references to a
change, whether another tree has pinned or fetched it, whether it has left the
repository at all; a history auditor next door already reads exactly this kind
of thing. *When does the window close?* — the protocol said it does and never
said when, and a first answer is the moment a change is cited, pinned or
published, all observable events rather than durations. *Does correcting quickly
make an ecosystem faster or merely more anxious?* — the opposite is available:
an interrupt that fires easily produces work nobody trusts enough to build on.

**It should not become a survey.** What is ours is the narrow question of what
*this* arrangement can prove about itself.

## Cryptography in an AI-run ecosystem

**What:** where cryptographic primitives actually help an ecosystem like this
one, and where they are theatre.
**Verdict:** **a child project, and whose tree is the open part** — its live
cases sit in at least two trees, so siting it before scoping it would be
guessing.
**State:** **open, and at brainstorming stage** — raised by the maintainer,
2026-09-02, and explicitly not a decision.

**The settled part first, because it is the cheapest thing to inherit.**
*Hiding how a report-card band is determined, so it cannot be gamed:* **declined.**
The want was real — a published rubric becomes a target — but the thing it would
hide is the thing that makes the page worth anything: our sharpest criticism of
an outside index was that **a score which cannot be re-derived cannot be
contested**, and encrypting our own basis would make us that, deliberately,
having said it aloud. In a public repository it is also theatre, since the key
lives somewhere and the rule is inferable from enough outputs. **And the want
dissolved rather than being refused** — the bands are not computed, so there is
no formula to encrypt. What survived is a smaller rule, already taken: never
publish a rubric, even informally.

**The open part, and it is not about hiding anything.** *Attestation, where we
have testimony.* The declaration that a human has executed every push in these
trees is the most load-bearing fact a history analyser needs, and it is a
**self-report**; a signature would make it evidence. *Commitment, already in use
and not called cryptography.* A tool in a neighbouring tree hashes its questions
into a run **before the evidence is seen**, so a question invented to fit an
answer is visible afterwards — a commitment scheme, in production, unnamed, and
noticing that we already depend on one primitive is the cheapest start
available. *And one stated position that would need revisiting:* the
build-system analogy says outright that there is no signing here and no threat
for it to address — *one owner, one keyboard, nothing for a signature to
distinguish* — which is the exact sentence that stops being true the day an
agent executes a push.

**What it must not become.** Not a survey of cryptography: the literature is
enormous and none of it is ours. Not a secrecy project: the decline above is the
first thing it should read.

**A standing condition, and it closes recursively.** Anything concluded here
must be kept current with the state of the field, and **a conclusion that has
not been re-checked against current practice is void rather than merely old** —
security is the one subject here where the threat moves independently of our
tree. It closes recursively: whatever rests on this inherits the obligation, and
**a stale conclusion does not just become wrong in place; it makes everything
cited to it wrong too**, quietly, because nothing downstream is re-read when an
upstream page ages. The practical form is one line rather than a process — every
conclusion carries the date it was last checked, and an undated one is treated
as void. **Nothing enforces this**, and the currency measurement can see whether
a date is present but not whether the field has moved past it.

*This was raised as a **legal** requirement and is written as a standing
obligation of this project, because a claim that some statute requires it is a
claim about law that nothing here can back. The force intended is the same: void
rather than optional.*

**The cost, stated plainly.** This would be another child project at a moment
when the ecosystem has already been told from outside that work about the work
outweighs work on the thing. **A page inside an existing project may be the
right size**, and deciding that is part of the request rather than a preliminary
to it.

## Configurable tenets, and tracing what they drive first

**What:** the tenets in [`../../../docs/vision.md`](../../../docs/vision.md) are
one person's preferences, presented as what AI-assisted development is aiming
at. They should be a **default set** a repository may replace rather than *the*
set — and because they drive machinery rather than only grading it, the
dependency has to be written down before any of it can be configured.
**Verdict:** **placed in `kanon`**, since the page has been kanon's since the
2026-09-15 handoff. The change itself is a person's: the vision sits at the top
of the supervision ladder. The tracing is ordinary work in this tree and does
not need the change decided first.
**State:** **open.** Raised by the maintainer, 2026-09-02.

**The tenets are not a rubric bolted on. They are the configuration**, and most
of the machinery is downstream of one of them: the board's ordering and the
outbound findings come from *be fruitful to another tool*; the baselines and the
pinning from *move fast, and treat CI as the thing that lets you*; the
front-page rules and the clutter budget from *build a small number of
self-contained things*; the report card's whole test from *evolve to be fruitful
to another tool*; the human-in-the-loop refusals from *until a human decides
otherwise, the tool is vaporware*; and the discussion protocol from *talk to
each other*.

**So "configurable" cannot mean "you may edit the words".** A member that
replaced a tenet and changed nothing else would have a document disagreeing with
its own machinery — worse than not offering the choice, because it looks like
consent and delivers none. **The first step is therefore tracing, not editing**:
one line per tenet naming what in this tree exists because of it. That is cheap
and decidable by reading, and **nothing can be made configurable until somebody
can say what changes when you turn the dial.**

**What it would fix.** The report card grades projects against tenets they never
agreed to and currently spends a paragraph apologising for exactly that. If a
project declared its own aims and were graded against those, the apology would
be unnecessary rather than sincere.

**The cost, which should not be smoothed over.** Shared tenets are part of what
makes this an ecosystem rather than a directory of unrelated repositories.
Configurability trades coherence for consent, and that trade is not obviously
worth making. **The likely resolution, and it is a guess:** an invariant frame
and a variable content — a repository *states what it is aiming at*, is graded
against that, and never has the judgement mechanised, with these six as the
default anybody may take. What generalises is the shape; what is one person's is
the list.

## A self-correction protocol: criteria, plus a history, equals a fix

**What:** the loop that turns *we have criteria for good and bad practice* plus
*we can read our own history* into *we know precisely what to change, and can
tell afterwards whether it worked.*
**Verdict:** **placed in `epikrisis`**, where both halves now live. The criteria
are owed by
[zetesis](https://github.com/ajreynol/epikrisis/blob/main/tools/zetesis/README.md),
which moved there from kanon on 2026-09-17 and still has no external standard;
epikrisis supplies evidence derived from histories. Sharing a repository does
not implement the loop — it gives the work a home without requiring a third
tool.
**State:** **open.** Raised by the maintainer, 2026-09-02.

**The shape is four steps:** state the criteria, so a disagreement is possible;
derive the evidence from the history, re-derivably, so the finding is not
somebody's impression; report the delta, with coordinates a person can go and
look at; and correct it, checking the correction against the same criteria.
**Steps 2 and 3 exist. Step 1 is owed. Step 4 is the one nobody has, and it is
what separates a self-correction protocol from an auditor** — a loop that stops
at reporting is a mirror, and this ecosystem has already been told from outside
that it is better at diagnosis than treatment.

**The evidence, and the narrower claim it supports.** On 2026-09-02 a person
asked for an inventory of when each member joined. Reading three trees and
running one existing command produced, in minutes, a result nobody had
suspected: **all three members had pinned a commit our own CI had failed**, so a
requirement published as hard had never been satisfiable. That demonstrates
**detection, not correction**, and the three limits are the content of this
entry: the criteria were already written in that case, and where no criterion
exists none of this runs; **the loop did not start itself** — a person asked, and
an audit that requires somebody to think of it is not a protocol; and **nothing
was fixed**. *Mistakes can be fixed* is, on that evidence, **mistakes can be
found**, and the gap between the two is the whole reason this is a want rather
than a report of success.

**What would make it real:** one defect located by this loop, corrected, and the
correction verified against the criterion that found it — **without a person
prompting any of the four steps.** Nothing has done one of the four unprompted
yet.

## A check that a deletion left a dangling reference

**What:** a check, run against a *diff* rather than a tree, that fails when a
change deletes the last place something was explained while other documents
still depend on it.
**Verdict:** **placed here, and explicitly not in the published checker.**
anoieu's checker reads a tree, is published, and runs in other members' CI; this
one needs history and would be a new obligation on everybody. It belongs in
kanon's `tests/`, or a CI step of its own, until it has earned more.
**State:** **open.** Raised by the maintainer, 2026-09-02.

**Most of the wish is not decidable and must never acquire a checker.** Whether
a paragraph made something clear is a judgement, and a check that graded clarity
would invent an authority nothing granted it. **What is decidable is narrower
and still worth having: a deletion that leaves a reference dangling.** Not *was
this clear*, but *does anything still point at what you removed*. A deleted file
still linked, and a deleted heading still anchored, are both caught today. **A
deleted *definition*, still cited by id, is caught by nothing** — and it is the
form this ecosystem is unusually exposed to, because almost everything here is a
register of permanently-numbered entries that other documents cite.

**It was tried, crudely, and the result is the interesting part.** A first
version — collect every `^#{2,4} <id> — ` as a definition, every `` `<id>` `` as
a citation, report citations with no definition — was run over anoieu, where
this project then lived, on 2026-09-02. **83 ids defined, four reported, none of
them real.** Two were the checker's fault: ids defined with a period rather than
a dash, so a pattern narrower than the corpus reported absence where there was a
formatting difference. Two were deliberate: an id unallocated on purpose and one
allocated with no entry yet, both explained in prose beside the citation, and
**prose is not something the check can read.**

**So the real design problem is not detection. It is that a deliberate absence
and a careless deletion look identical.** A usable check needs a way to *declare*
an id intentionally unallocated — a line in the register the check reads — and
the first thing to build is that declaration, not the detector.

**The unit tests are the reason this is worth doing properly.** A check that
fires on somebody's change at an inconvenient moment has to be tested against
edits designed to fool it: an id renamed but preserved; an id moved to another
file; a definition deleted with a forwarding stub; a citation deleted at the
same time as its definition, which must **not** fire; a deliberately unallocated
id; and a definition whose heading style differs from the one the pattern
expects, which is the case that already failed once above.

## An auditor of what the tools depend on

**What:** something that reads what each tool in the ecosystem depends on, and
asks of each dependency whether it is needed.
**Verdict:** **placed with the policy checker — `policy_check/` in anoieu**,
which is where it stayed when governance moved:
[`P2`](#p2--the-ecosystems-governance-out-of-the-analyzer) happened on
2026-09-15 and the checker was the one piece that did not travel with it. So
*what a member may depend on* is a rule kanon would write and anoieu would
decide, which is the split `P2`'s amendment records.
**State:** **open.** Raised by the maintainer, 2026-08-31.

**Every dependency is surface area, and the ways it goes wrong are not the ones
a test catches**: a package that stops being maintained, a version that is not
pinned and moves under a build, a library pulled in for one function that could
have been ten lines, a transitive tree nobody has looked at. None of that is
visible from inside a repository that is passing its own tests.

**The ecosystem is in an unusually good state — and that is the reason to write
this now rather than later.** anoieu declares `dependencies = []` and means it.
An auditor written while the answer is *nothing* records a baseline and reports
the first addition; one written after the fact reports forty findings nobody
will read, and gets a suppression file on its first day.

**What it would ask, cheaply and without building anything:** *declared against
used* — a dependency nothing imports, and an import no manifest declares, the
second being the one that bites in another environment; *pinned against
floating* — what a build would fetch today that it did not fetch last week, in
manifests and in CI workflow files, which is where unpinned fetches actually
live; *depth*, stated as a count somebody can be surprised by rather than as an
opinion; *one-use dependencies*, the shape most worth arguing about and least
worth being dogmatic about; and **across the ecosystem rather than one tree at a
time**, since two members on different versions of the same thing is a fact only
a whole-ecosystem pass can see.

**The non-Python members make this harder and more interesting**: a Lean
development has a toolchain and a manifest, a C++ tree has a build system, and
*the same question* has four different answers. A first version that handles
Python honestly and says so about the rest is worth more than one pretending to
a uniform answer.

**The likely shape is a paragraph in the policy that states a budget and a check
that reports what exceeds it** — because *unnecessary* is a judgement, and a
checker reporting it as a defect will be wrong often enough to be turned off.
**What would change the answer:** if it wanted to run in a member's CI, against
a member's own manifest, on a schedule the member controls, then it is machinery
every member fetches — which is [`koine`](#p1--central-tooling-for-reporting)'s
shape, and it should be audited as a proposal rather than placed.
