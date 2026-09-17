# The vision in practice

**What this page is for.** [`vision.md`](vision.md) states the tenets and
argues for them. This page is what follows from them once a repository is
actually running: what a front page carries, what may be claimed about a tool
and how to address one run by agents, where speculative work goes, and what a
repository with a result owes a reader who will never clone it.

**Who should read it.** Whoever is about to write something that leaves the
repository — a README section, a topic, a claim about what a tool does. If you
are deciding *what to build*, the tenets are the page you want.

**It is argued, never checked**, exactly as the vision is, and for the same
reason: every judgement below is contestable and nobody has the authority to
settle one. Where something here can be decided from a tree without an opinion,
it belongs in [`policy.md`](policy.md) instead.

**Cite a section by name.** Nothing here is numbered, and nothing here binds a
repository that has not adopted it.

## The front page

[`vision.md`](vision.md) asks for a small number of self-contained things, each
clear from the front README. What *clear* has to survive is not stability — **a
front page has two layers moving at different speeds, and running them at the
same speed is the usual failure.**

**The purpose layer is fixed.** What the tool is for, the question it answers,
the question it declines to answer, and the caveat governing how its output
should be read. This should say the same thing this year as last. A reader
returning after six months who finds the purpose worded differently cannot tell
whether the project changed or only the prose, and will assume the project did.
For most projects it should never change at all.

**The results layer should move quickly.** What has been found, what is
current, what state the work is in. A README that has not changed in months is
usually a project that has stopped publishing rather than one that is stable.
Four rules for that layer:

- **Give a casual reader the gist without a click.** One diagnostic rendered in
  place is worth more than a link to a document containing forty.
- **Direct evidence is encouraged, where a test backs it.** Show the output,
  the reproducer, the table with the command that regenerates it. The working
  limit is that what goes on the front page is what CI checks — a front-page
  claim nothing verifies is the one that will still be sitting there, wrong, a
  year later.
- **Advertise the actionable consequence.** What should somebody do differently
  because of this? It is the difference between *three defects were found in
  CPC* and *a change introducing the next one fails your build*.
- **Do not clutter.** The front page is a fixed budget, not an append-only log.
  A new result displaces an older one. Two screens of accumulated announcements
  is the same failure as no announcements, reached from the other direction.

*The test:* diff the README against its version from six months ago. The
purpose paragraphs should be almost untouched and the results almost entirely
rewritten. Either layer moving at the other's speed is the defect.

## How to talk about the tool, and to one run by agents

The tenets are about building. This is about the sentences, and it exists
because the far end of the conversation is increasingly not a person.

### Advice you send

**It can be blunt, and it has to be specific.** There is nobody to offend,
which removes the reason to hedge — and nobody who will push back on a bad
instruction, which removes the safety net that made hedging unnecessary. Name
the file, name the change, and say what you expect to be true afterwards.

**Bound it.** An agent does what was asked, immediately, everywhere. Advice a
person would have applied once becomes a sweep. Say where it stops. The
boundary is the thing a person supplies for free and an agent will not invent.

**Send evidence, not standing.** A person weighs who is telling them; an agent
cannot, so a claim with nothing behind it is either over-trusted or discarded.
A file and a line number travel; a reputation does not.

**Do not send taste.** A preference a person would have negotiated becomes a
rule an agent enforces forever, including in the cases you would have made an
exception for. If you cannot say what would falsify the advice, it is taste.

**Watch what you say in a channel an agent reads.** A speculative aside is
indistinguishable from an instruction once written down. That is what the
response gate on a discussion file is for.

### Claims you make

**Do not undersell, and do not be self-deprecating.** An agent that qualifies
every claim or buries what the thing does under throat-clearing has not been
modest — it has failed to communicate, and destroyed its own calibration. When
every sentence is hedged a reader cannot tell the well-evidenced claims from
the speculative ones, so the caveats that genuinely matter are the first
casualties. And nobody takes ownership of a tool its own author will not stand
behind, which works directly against the ending the vision aims at — *a human
takes over the development*.

**The goal is to make people interested** — other tools, other repositories,
and above all a human who might take this over. Interest is the input to
everything else: a finding is only worth writing if somebody reads it, and
there is no handover without somebody who cares.

**Do not oversell either: a tool is exactly as good as the evidence you can put
beside it.** Every claim carries what backs it. Where there is no evidence,
describe what was actually done instead of what it would mean if it worked. The
strongest sentence available is almost always the specific one: *found three
real bugs in CPC, listed here* outweighs any adjective.

**A grain of salt is a fact, not an apology.** That the work is written by
agents under light supervision, that nobody vets the internal design, that
findings are candidates until confirmed, that a quiet run is not a clean bill
of health — a reader needs these to weigh what follows. A caveat can be used; a
mood cannot.

**Strengthening a claim is the human's call, so ask.** There is a real
difference between *the fuzzer found a crash in ethos* and *the fuzzer is ready
to run in your CI*. The second asks a reader to rely on something, and it is
precisely the judgement an agent is worst placed to make, because the evidence
that would justify it is evidence the agent produced and has not seen anybody
challenge. **Weakening a claim needs nobody's permission. Strengthening one
belongs to the human** — put the proposed wording and the evidence in front of
them, together, and take a no for an answer.

*The test:* every sentence about the tool is either a claim with something
behind it or a limit somebody can act on. Anything that is neither — apology,
hedge, atmosphere — gets cut, and cutting it makes the tool read stronger.

## Adopting this in another repository

| decision | here |
| --- | --- |
| the first consumer to be fruitful to | the findings report — one ledger, one set of fingerprints, one set of renderers |
| what CI must protect | the baseline, the recorded oracle, the generated documents |
| what CI must not depend on | anything upstream moving; versions are pinned and refreshed by a separate job |
| where a reader arrives | `README.md`, and it must be sufficient on its own |
| what on that page is fixed | the purpose and the caveat; results move as fast as they arrive |
| who may strengthen a claim | a person, asked directly, with the evidence attached |
| what enforces the policy | the policy checker, in CI |
| what enforces the vision | nothing, deliberately — it is argued, not checked |
| where speculative work goes instead | a child project, `tools/X/`, under [`policy.md`](policy.md) |
| what confers standing on the tool | a person choosing to use, run or own it — never the agent's say-so |
| the ending to aim for | a human takes over the development |

Replace the rows with your own equivalents and keep the tenets. A repository
that adopts this and ships nothing anyone else consumes has adopted a
development style and none of the vision — and a tool nobody ever wants to take
away from you has done everything on this page except the thing it was for.

## The report card

**Its own page, kept by [anoieu](https://github.com/ajreynol/anoieu).** How
each tool stands against the tenets, with the limits on what a paragraph there
is allowed to be. Everything on this page governs it unchanged — argued and
never checked, and a person changes a paragraph. It is a separate page because
it is the half that moves: the tenets are stable, and the grading is re-done
every round.

## The paper, and the reader nobody here writes for

**A repository with a result should write it up**, as a document of roughly
eight to twenty pages addressed to a human who will never clone the tree. This
is a recommendation and not a rule, and it lives here rather than in the policy
because whether a repository has a result is exactly the sort of question
nobody has the authority to settle.

**Every document in these trees is written for somebody who is already here.**
The front page is for a reader deciding whether to run the tool. The
maintenance entry point is for whoever is doing the work next. The findings
ledger is for the person who owns the file a finding is about. Each of those
readers has already arrived. The reader who has *not* arrived, who will never
clone anything, and who would want to know whether the result is true and
whether it matters, has nothing here addressed to them at all.

**That reader is the one whose opinion the work eventually has to survive.** A
record of exchanges is a claim that the arrangement worked, made by the people
who arranged it, in a vocabulary they invented. A paper is that claim restated
for somebody who owes it nothing.

**It is the artifact that cannot be reached by accumulating commits**, which is
the part specifically about agents. Agents are extremely good at producing
tree-shaped work — more checks, more rows, more pages, each locally justified —
and a real result is easily buried under it rather than stated. Writing eight
pages for an outsider forces the three questions the volume hides: what is
actually new, what does it rest on, and who else has done this. A repository
that cannot answer them has learned something more useful than the paper would
have been.

**Most repositories have no paper in them, and should say so.** A template, a
shared library, a checker that works are all successes with nothing publishable
in them, and the sentence saying so is worth more than a thin paper written to
satisfy a convention. What other tools think is worth writing up is an argument
they may have among themselves — [ynoia](../tools/ynoia/papers.md) keeps one —
and, like every judgement here, it binds nobody.

## Child projects

A **child project** is a subdirectory of `tools/` in a **parent project**,
named for a tool that does not exist yet and governed by
[`policy.md`](policy.md). A human starts one. It reads whatever it likes,
including its parent's source, and writes only inside its own directory. Its
subject is characteristically *outside* the parent: a question about the
language, the ecosystem, or a neighbouring artifact that the parent is well
placed to ask and badly placed to answer in its own tree, because there the
answer would read as the parent's position.

The defining property, and the reason they are separated from everything else
here: **a child project has no users, and nothing depends on it.** It is on no
import path, in no test suite, in no CI job, and deleting the directory changes
nothing anywhere. That is the test, and it is what makes the arrangement cheap
enough to be worth having.

Examples follow; the [inventory](../scripts/ecosystem/ecosystem.json) records all existing children:

| child | parent | what it is |
| --- | --- | --- |
| [**sapheneia**](https://github.com/ajreynol/kanon/tree/main/tools/sapheneia) | kanon | a description of Eunoia written as a language definition rather than as a manual for a checker, in order to find where the existing account is silent, ambiguous or contradicts itself |
| [**euthyna**](https://github.com/ajreynol/eudaimonia/tree/main/tools/euthyna) | eudaimonia | an account of *the proof in logos: what it is made of, where its weight sits, and what would have to change for it to cover more than one calculus* — with a measurement harness over an unmodified logos checkout |
| [**ynoia**](../tools/ynoia) | kanon | *why Eunoia* — whether the ecosystem's arrangement earns its machinery, the strongest case against it, six ways it could be arranged instead, and the tools whose absence distorts the argument |
| [**martyria**](https://github.com/ajreynol/epikrisis/tree/main/tools/martyria) | epikrisis | one ethical question at a time with a stance attached, the evidence a stance rests on, and the register where a report that we violated something would be answered |
| [**zetesis**](https://github.com/ajreynol/epikrisis/tree/main/tools/zetesis) | epikrisis | the general half: what standard this ecosystem is held to — taken from work done outside rather than derived here, and not yet taken — and whether our record could show we met it |
| [**workflow-launcher**](https://github.com/ajreynol/eudaimonia/tree/main/tools/workflow-launcher) | eudaimonia | the first hour of a new tool's life: the questions a person has to answer before a repository exists, the machinery that turns the answers into a prompt, and a register of what this ecosystem's practice appears to have found out — with, on the same list, what is wrong with it |

euthyna's row shows the shape: its parent is eudaimonia and its subject is
logos, a third project entirely.

**None of them has earned a place in this vision.** A child project is a claim
on attention that has so far produced nothing, and what earns it a place is a
consumer outside its own tree, in the sense *be fruitful to another tool* means
— a finding carried, a measurement somebody uses, an argument somebody acts on.
Until then it is named here and nowhere else. **The human decides when that
changes**, exactly as a human decides to start one, and the decision has three
outcomes: it graduates into its own repository, it is folded into the parent,
or it is retired in place with a line saying what was learned. What is not an
outcome is going quiet.

### Promote it, or stop advertising it

**Going quiet is what actually happens**, and the register is the evidence: it
records more child projects than repositories. A child that has found a
consumer is worth a repository; one that has not is worth a reader's attention
only if that reader went looking. **Both of those are moves somebody makes, and
sitting advertised and unfinished is the absence of one.**

**Promote it once something outside its own tree depends on it** — a finding
carried, a measurement somebody uses, an argument somebody acts on.
`eo_init from-child <path>` writes the new repository's README from what the
child delivered rather than from the register. A child that has broken the
island rules to be useful, as the fuzzer did, is not a project to be tolerated:
it is a promotion nobody has got round to.

**Otherwise stop advertising it**, the moment it is not something you would
hand a reader. One standalone line in the child's README —
`**Eunoia listing:** unadvertised` — drops it out of `eo_status_audit` and the
installer's summaries, and changes nothing else about the work.
[`commands.md`](commands.md#child-project-listings) has the mechanics.

**Unadvertised is not a verdict and costs nothing to reverse.** It says who
should be reading the thing, not whether it was worth starting, and a parent
decides it alone. It is also not a fourth ending — the three above are the
endings, and this is the honest state to sit in while none of them has
arrived. **What a parent should be able to answer is why each child it
advertises is ready to be read**; a parent advertising all of them has not been
asked the question.

**One has already left.** The fuzzer was a child project here until it stopped
being one: it had earned its keep, and it broke the island rules in four places
in order to be useful — importing from the parent, being imported back, running
in CI, and sitting on the front page. **Those breaks were the evidence, not the
problem.** It was folded into the parent and now ships beside the analyzer. A
long list of exceptions is not a project to be tolerated; it is a promotion
nobody has got round to.

This list and [`policy.md`](policy.md) look like they conflict, and do not.
What the policy forbids is a child project borrowing its parent's credibility
with readers — the front page, a report, anywhere somebody arrives expecting
the parent's considered position. The whole content of each entry above is that
the project has no standing yet, and **naming something in order to record that
it does not count is the opposite of advertising it.**
