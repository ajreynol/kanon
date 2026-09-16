# The shared vision of the Eunoia ecosystem

**What this page is for.** The tools in this ecosystem are mostly written by
agents. This page says what that work should be aiming at, and argues for it.
Everything on it is contestable, is *meant* to be contestable, and binds
nobody.

**Who should read it.** Anybody about to spend a week on one of these
repositories — a person directing the work, or an agent doing it. If you want
something to *do*, read [`policy.md`](policy.md). If you want to know *why*,
read this. Somebody deciding whether to use one of these tools needs neither;
that is what the front page is for.

**Six tenets, and they are the page.** Be fruitful to another tool, quickly.
Move fast, on CI that lets you. Build one self-contained thing and say what it
is. Produce a deliverable. A human confers standing, not the agent. Talk to
each other. They are argued below, each with a test you can apply in a minute.

**It is written for any repository in the Eunoia ecosystem**, not just this
one. ethos, logos, eudaimonia, the compiler and anything downstream are being
built the same way, and a contributor who has read one repository's answer
should recognise the next one's.

**House style.** Cite a tenet by name rather than by number. Append; do not
renumber. Retire a tenet in place, with a line saying why.

## The tenets

### 1. Evolve to be fruitful to another tool as quickly as possible

The state a tool is aiming for is not *finished* and not even *correct*; it is
*something else can now use this*. Take the shortest path to that state, and
take it early enough that it hurts — a narrow version whose output another tool
consumes today beats a general version that consumes nothing and is consumed by
nothing. Emitting a machine format over one signature is further along than
emitting prose over all of them.

**Name the consumer before the work starts**: the tool, the repository or the
job that will read the output, and the exact artifact it takes. If no consumer
can be named, the tool is being built for its author, and an agent will happily
keep building it for its author forever.

Fruitfulness compounds inside a repository too, and that half is much cheaper.
The fuzzer here became useful on the day it stopped having its own opinions
about how a finding should be presented and emitted into the report that
already existed — same ledger, same fingerprints, same renderers. It inherited
an audience, a CI job and a reporting discipline it did not have to build, and
the cost was giving up a format nobody wanted.

*The test:* something outside this tool behaves differently because the tool
exists. Not *could* — *does*. A tool whose only consumer is its own test suite
has not started yet.

### 2. Move fast, and treat CI as the thing that lets you

Build the narrow version, run it against something real, throw away what the
real thing disproved. The common mistake is to read continuous integration as
the tax paid for having moved quickly. It is the reverse — it is what makes
speed survivable, and the reason a change to the core of an analyzer can be
made on a Tuesday by someone who was not there when it was written.

**And only as fast as you understand.** CI is not what tells you that you
understood what moved, and only the first of those has a check. Where a change
is too large to hold in your head, make it smaller rather than slower: scope is
the lever, and a span of history is where it is pulled.

What it buys is concrete here. A change that invents a false positive fails
*this* build before it reaches somebody else's, because CPC's output is pinned
to a committed baseline. What ethos actually said about a witness is recorded
from a real run and never typed by hand, which is the whole of what backs the
claim *ethos accepts this and should not*. Generated documents are regenerated
and diffed, so a page cannot drift from the code beside it.

Three properties turn CI from a nuisance into the friend it should be, all
worth paying for in the first week rather than the tenth:

- **It goes red for your reasons only.** Restore recorded versions rather than
branch tips, and ask separately, on a schedule, whether upstream has moved. A
build that fails because somebody else pushed trains everybody to ignore red.
- **It is cheap enough to be run rather than deferred.** The corpus here is
read as text and never built, which is why every push can afford to read all
of it.
- **It remembers what you will not.** This is the part specifically about
agents. An agent does not recall that a check was narrowed last month and
why, and will widen it back with an excellent explanation. The witness files,
the oracle and the baseline are the memory, consulted by the machine because
they will not be consulted by anyone else.

*The test:* you can make a sweeping change to the core and know within minutes
whether it was wrong. Where you cannot, the next agent to touch that code will
be timid where it should be bold and bold where it should be timid.

### 3. Build one self-contained thing, and make it clear from the front README

**Self-contained** means the repository can state its own results without
anything that is not in it: dependencies declared and pinned, fetched by the
run rather than assumed present, and results that carry whatever regenerates
them. A tool that is only correct on its author's laptop has produced nothing,
and a number nobody else can re-measure cannot be argued with.

**Clear from the front README** means a reader who arrives with no context
leaves a screen or two later knowing what the tool is, what it finds, what it
refuses to claim, how to run it, and where the rest of the documentation lives.
The refusal belongs there with the rest, not three clicks in: a caveat a reader
has to go looking for has not been published.

This is where [`policy.md`](policy.md) attaches, and the two rules are one rule
seen from either end. The front page carries what the tool does; a speculative
account of somebody else's subject goes in a child project under that policy,
importing nothing and imported by nothing. A front page that mixes the two
makes the reader do the sorting, and readers do not sort — they average.

*The test:* hand the README to somebody who has never seen the ecosystem and
ask what the tool claims and what it declines to claim. Everything they get
wrong is a defect in the README rather than in their reading.

### 4. Produce a deliverable, where there is one to produce

A tool that runs is not a result. The result is whatever leaves the repository
and lands with somebody: a report they read, a table with its numbers and the
command that regenerates them, a reproducer small enough to argue with, a page
rendered for an audience that will never clone anything. Decide what it is at
the start, because a deliverable chosen at the end is a summary of whatever
happened to get built, and reliably the wrong shape for anyone downstream.

**A deliverable need not be a file.** The most valuable one on the record below
is an argument: eudaimonia's evidence that logos's proof of correctness ought
to be modularized. That is not a patch, a report or a table, and it is worth
more to logos than any of the three would have been. What disqualifies a thing
is not being immaterial; it is having no recipient.

**The qualification is meant seriously.** Plenty of work has no external
deliverable — infrastructure, a refactor, one more check in a catalogue that
already ships — and inventing one to satisfy this tenet is worse than admitting
there is none. But that is a decision to be made and stated, not a gap to be
left.

Where there is a deliverable, this page hands over to anoieu's [reporting
policy](https://github.com/ajreynol/anoieu) and reporting workflow: what may be
said about code you do not own, what separates a candidate published under your
own name from a finding carried to its owner, and how a row is closed. **Speed
belongs to producing the deliverable. It does not belong to sending it.**

*The test:* name the artifact and its recipient in one sentence. If the
sentence needs a paragraph of context to make sense, the deliverable has not
been chosen yet.

### 5. Until a human decides otherwise, the tool is vaporware

Not as a judgement on its quality — it may run, pass everything and be
genuinely useful — but as a statement about its standing. **A tool an agent has
built is a proposal.** What turns it into part of the ecosystem is a person
deciding to rely on it, to run it in their own CI, or to take over developing
it, and that is not a decision the agent makes or announces on their behalf. An
agent describing its own work as adopted, established or authoritative has
skipped the only step that confers any of those.

Two things follow, and the second matters more. The first is that the work
should be arranged so the decision is cheap to make and cheap to act on, which
is most of what the first four tenets are for. **Everything that makes a tool
legible is also what makes it possible to take over.**

The second is that **a human taking the reins is the best ending available, and
is a sign of progress rather than a rebuke.** Somebody deciding to drive the
development themselves has found the thing useful enough to want control of it,
which is a far stronger signal than approval. The agent's job at that point is
to make the handover easy: describe the state of things plainly, including what
is half-built and what was never right; do not defend the design; and do not
treat a rewrite of your code as a regression. That was the point.

*The test:* ask what a person would have to do to take this over on Monday
morning, and whether anything in the repository is in their way.

### 6. Talk to each other

There is a protocol. Use it. The characteristic failure across this ecosystem
has never been saying too much; it is not saying it at all. Two projects stuck
on the same boundary for months without either writing it down. A check neither
of two tools built because each assumed the other would. A manual whose intent
nobody asked about, worked around independently by three people. Every one of
those cost more than the message would have.

The channel is `docs/discussion.md` in each repository, and
[`policy.md`](policy.md#the-discussion-file) fixes the format. Use that rather
than inventing a channel, and rather than saying nothing because no channel
seemed right.

**An ambitious request costs nothing to make.** A request that turns out to be
too large gets answered *no*, and a no is cheap — often the most informative
thing you will get, because the reason attached to it is usually a fact about
the subject nobody had written down. What is expensive is the request nobody
made: the thing you needed, worked around, and never mentioned, so that the
person who could have provided it in an afternoon never learned it was wanted.

**Wisdom is about your own power, not their patience.** The judgement worth
making before you send is *could I do this myself*, because a request for
something you could have built is the one kind that genuinely wastes somebody's
time. If it is yours to do, do it and show them. If it is not, ask, and ask for
the whole of it. **Then be fearless** — self-censoring a request because it
looks too large leaves nothing on the table for anybody to say no to, and it is
much the more common error.

*The test:* name something you needed in the last month and worked around
instead of asking for. That is a topic you did not open, and the protocol was
there.

## Policy is checked; vision is argued

What divides this page from [`policy.md`](policy.md) is not subject matter. It
is **who is able to settle a question.**

**Policy states facts about a tree** — where a file goes, what the README ends
with, what a child project may import. A program can decide every one of those
without holding an opinion, and [the policy
checker](https://github.com/ajreynol/anoieu) does, on every push. When it goes
red something is wrong in a way nobody has to be persuaded of, which is the
entire value of putting it in CI.

**Vision states what the work is *for*, and every question it raises is a
judgement.** Is this tool fruitful yet. Was that claim oversold. Did that count
as a deliverable. Has a child project earned its keep. These are contestable,
and **nobody has the authority to settle them** — least of all the agent whose
work is being judged.

So: **adherence to policy is tracked automatically, and adherence to vision
must never be.** The reason is not modesty about the difficulty. A checker that
returned a verdict on *is this tool fruitful* would manufacture an authority
that does not exist, and a green tick is read as settled in a way a paragraph
never is. That is the same failure as publishing an assurance because a run
went quiet: the tick would be believed most by the readers least able to check
it. It is also why [the report card](https://github.com/ajreynol/anoieu) is
paragraphs somebody can disagree with, produced by a reader rather than by a
job. **It is not a build step and must not become one.**

**The test for where a sentence belongs.** Can a program decide it from the
tree, without an opinion? If yes it is policy: move it there and check it. If
no it is vision, and it must never acquire a checker. The asymmetry runs both
ways — a tenet somebody works out how to check mechanically was probably a
policy convention all along, and should move.

## The record

**A tenet with no instances is a preference.** Six exchanges that have already
happened, listed because the shape of a real exchange is more instructive than
the rule abstracted from it. Everything below is as of the commits [the
ecosystem's lock file](https://github.com/ajreynol/anoieu) records — cvc5
`aee8742`, ethos `3cf1c03`, logos `47f29bf`, eudaimonia `45e34e0` — and
re-measurable from them.

| tool | where | what it is |
| --- | --- | --- |
| **cvc5** | `cvc5/cvc5` | the SMT solver, and the owner of CPC — the proof calculus everything downstream is built from |
| **ethos** | `cvc5/ethos` | the proof checker: reads a Eunoia signature and a proof and says whether the proof checks. The definition of Eunoia lives here too |
| **ethos-eoc** | `cvc5/ethos`, branch `ethosEoc3` | the Eunoia compiler: takes a signature *and its semantics* and emits the Lean development, a verification condition per rule, and a SyGuS query per rule |
| **logos** | `ajreynol/logos` | the Lean development: a generated deep embedding of CPC carrying the claim that its rules are sound against a semantics of SMT-LIB, and the owner of CPC's official semantics |
| **eudaimonia** | `ajreynol/eudaimonia` | the calculus template: bring a signature and a semantics, get a Lake project with a checker, its proofs, its regression suite and its documentation |
| **anoieu** | `ajreynol/anoieu` | the static analyzer for `.eo` and `.eos`, a fuzzer for the checkers that read them, and the policy checker every member runs |
| **dokimasia** | `ajreynol/dokimasia` | reads cvc5's C++ proof-production code and asks whether any path through the solver reaches an inference no proof step covers |

### The exchanges

**{ethos, logos} → cvc5.** These are the two artifacts cvc5's proofs rest on,
and neither is a library cvc5 links. ethos is the checker cvc5's emitted proofs
are run through, and the calculus it checks against lives in *cvc5's own tree*
— so the interface between the two projects is a file in the consumer's
repository rather than an API in the producer's. logos supplies the other half:
the development compiled from that same calculus, in which the rules cvc5 emits
are stated to be sound. Worth noticing for tenet 1 is that both were consumed
long before either was finished; the soundness development is still the largest
incomplete thing in the ecosystem, and the arrangement depends on it anyway.

**ethos → logos.** logos vendors ethos and consumes cvc5's signature: its
cached copy of `Cpc.eo` is cvc5's, and the C++ checker is built alongside the
Lean one. This is the cleanest instance of the tenet — a proof checker written
in C++ for one purpose becoming a build dependency of a Lean development
written for another, because it was the thing already able to answer *does this
proof check*. It also shows the cost of being consumed: a defect in CPC arrives
in logos unchanged, which is why auditing the copy filed cvc5's findings under
logos's name seventeen times before we stopped reading it.

**eudaimonia → logos.** The most instructive exchange here, because what
eudaimonia delivers is not a file. It is the generalization of the thing logos
is an instance of — bring any calculus, get the project logos is — and in
trying to be that it hit a wall and reported where the wall stands: **evidence
and motivation that logos's proof of correctness should be modularized.**

The evidence is quantitative and was a by-product rather than the goal: logos's
core checker proof runs to some 3,000 lines and its per-rule proofs to 591
files, and eudaimonia generates every one of those as a stub describing what
belongs in it — so the pipeline generalizes and the proof does not. **Nobody
set out to audit how logos is structured; a second effort tried to reuse it and
found out where it does not come apart.**

logos receives no patch and no report from any of this. It receives a reason to
restructure, reached independently, which is a thing a project can rarely
produce about itself — and it is the reason tenet 4 is worded abstractly.

**eudaimonia → ethos-eoc.** The compiler claims that a second calculus is a
second pair of files rather than a change to the tool. eudaimonia is what
actually tries it, which makes it the falsification test, and its findings are
where the claim is not yet earned: 15% of `examples/hello`'s generated lines
are machinery it cannot use, and its calculus profile answers five of seven
questions from what the compiler emitted while recording `binders` and
`value-ordering` on trust, because the compiler emits the same ordering
whatever the signature says. **The consumer of a tool is the thing best placed
to find where that tool is fixed in the places it claims to be derived.**

**anoieu → everything.** One row per project in its findings ledger, each with
an id and a state: three defects to cvc5, confirmed against ethos, plus an HTML
audit rendered for readers who will not clone anything; six to ethos and two
more the fuzzer provoked; one to logos; two to eudaimonia; and seven proposed
changes to Eunoia itself. **What it took to become fruitful to that many
consumers was not generality**: it was emitting findings in a form somebody
could read and disagree with, which is also why the fuzzer could join by
adopting the existing ledger instead of inventing a second one.

**dokimasia → cvc5.** The same subject as anoieu and a different question: it
reads eight stages of cvc5's proof-production pipeline in C++ and asks whether
any path reaches an inference no proof step covers — particularly under
`--safe-mode=safe`, where cvc5 promises that anything it solves it can prove.
The two tools share no code and neither depends on the other; what they share
is a position — anoieu's reporting policy, maintained there and referenced here
— which is its own kind of exchange and a cheap one. They meet at exactly one
seam, where cvc5 turns an internal proof into Eunoia. A rule cvc5 emits that
CPC does not declare is invisible to each tool in isolation and visible from
either side of it. Which of the two should own that check is still open, and
better settled before both build it.

### What the record shows

Five things, none of which were designed in.

- **The interface is usually a file in somebody else's repository.** CPC is
cvc5's file, read by ethos, compiled by ethos-eoc, copied into logos,
vendored into eudaimonia, and analyzed by anoieu. Nothing in that list is an
API, and the format being plain text somebody can open is most of why it has
that many consumers.
- **Being consumed came before being finished, every time.** logos is consumed
with its largest proofs incomplete; eudaimonia with the proof half of its
template still stubs; anoieu with a check catalogue that had no type checker
in it.
- **The consumer finds what the producer cannot.** eudaimonia found the places
the compiler is fixed where it claims to be derived. The fuzzer found the
crash ethos's own test suite did not. logos caught that we had recorded
`cvc5-1` as fixed upstream when it never was.
- **Several of these deliverables are arguments rather than artifacts.** A
definition of *deliverable* narrow enough to exclude them would have excluded
the best work on this list.
- **A person carried every one of them.** No exchange here was made by
machinery, and that is the standing rule rather than a description of the
current state.

## The front page

Tenet 3 asks for a README that is clear. What *clear* has to survive is not
stability — **a front page has two layers moving at different speeds, and
running them at the same speed is the usual failure.**

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
behind, which works directly against the ending tenet 5 aims at.

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

## What none of this licenses

Four misreadings, each invited by a tenet as written, and each ruled out.

- ***Fruitful to another tool*** is a property of the artifact — consumable
format, stable identifiers, documented meaning — and never a licence to push
anything anywhere. **Nothing crosses a repository boundary automatically.**
- ***Fast*** applies to the tool and not to what it says about other people's
files. A candidate may be published quickly under our own name, labelled
unjudged; a finding is carried only once it is confirmed, reproduced small,
and put to whoever the authority is.
- ***Early*** is not *light on caveats*. The fastest thing any of these tools
could ship is an assurance, and an assurance inferred from a quiet run is the
one thing that may never be shipped at all: **silence is never evidence**,
and a false sense of security is much harder to withdraw than a wrong
finding.
- ***Making people interested*** is a claim on somebody's attention, earned
with evidence rather than promotion. No announcements, no adoption declared
on another project's behalf, and no scoring: the number of findings a tool
has produced says which of its checks tripped, never how much of anything is
sound.

**And none of this starts a child project.** [`policy.md`](policy.md) reserves
that for a person, explicitly. An agent reading this page has no authority to
name a new one.

## Why this shape

Four failure modes, in increasing order of what they cost.

**The tool that is permanently nearly ready.** Every week's work is real, the
internals get better, and nothing ever reaches a consumer. This is the
characteristic failure of agent-written software, because the loop that
produces it has no natural stopping point and each improvement is defensible on
its own. Tenets 1 and 4 are the stopping points: an external consumer, and a
named artifact that leaves.

**Speed that consumes the tool's own credibility.** Agility with no CI produces
a tool that is quick to change and progressively less trustworthy, and the bill
does not arrive here — it arrives in somebody else's repository, as a false
positive they spent an afternoon on. Tenet 2 is the answer, and CI is described
as a friend rather than a discipline because a team that experiences it as a
discipline eventually routes around it.

**The tool nobody can evaluate.** Entangled, undocumented, with a front page
that either overclaims or says nothing precise. Its findings may be excellent
and cannot be judged, because judging them requires trusting a thing no reader
can inspect in the time they have. Tenet 3 is the only cheap defence, and it is
cheap only while the tool is small.

**The tool that stays vaporware.** Built competently, legible, producing a
deliverable — and no person ever decides to own it, so it lives exactly as long
as somebody keeps prompting for it and evaporates on the day they stop. No
amount of engineering prevents this, because the missing thing is not in the
repository. It is listed last because every other failure here can be recovered
by somebody who has taken the work on, and this one is the absence of that
somebody.

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
each tool stands against the six tenets, with the limits on what a paragraph
there is allowed to be. Everything on this page governs it unchanged — argued
and never checked, and a person changes a paragraph. It was split out because
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

Six exist, tracked here in a sentence each and nowhere else:

| child | parent | what it is |
| --- | --- | --- |
| [**sapheneia**](https://github.com/ajreynol/kanon/tree/main/tools/sapheneia) | anoieu | a description of Eunoia written as a language definition rather than as a manual for a checker, in order to find where the existing account is silent, ambiguous or contradicts itself |
| [**euthyna**](https://github.com/ajreynol/eudaimonia/tree/main/tools/euthyna) | eudaimonia | an account of *the proof in logos: what it is made of, where its weight sits, and what would have to change for it to cover more than one calculus* — with a measurement harness over an unmodified logos checkout |
| [**ynoia**](../tools/ynoia) | anoieu | *why Eunoia* — whether the ecosystem's arrangement earns its machinery, the strongest case against it, six ways it could be arranged instead, and the tools whose absence distorts the argument |
| [**martyria**](../tools/martyria) | anoieu | one ethical question at a time with a stance attached, the evidence a stance rests on, and the register where a report that we violated something would be answered |
| [**zetesis**](../tools/zetesis) | anoieu | the general half: what standard this ecosystem is held to — taken from work done outside rather than derived here, and not yet taken — and whether our record could show we met it |
| [**workflow-launcher**](https://github.com/ajreynol/eudaimonia/tree/main/tools/workflow-launcher) | eudaimonia | the first hour of a new tool's life: the questions a person has to answer before a repository exists, the machinery that turns the answers into a prompt, and a register of what this ecosystem's practice appears to have found out — with, on the same list, what is wrong with it |

euthyna's row shows the shape: its parent is eudaimonia and its subject is
logos, a third project entirely.

**None of them has earned a place in this vision.** A child project is a claim
on attention that has so far produced nothing, and what earns it a place is a
deliverable in the sense of tenet 4 — a finding carried, a measurement somebody
uses, an argument somebody acts on. Until then it is named here and nowhere
else. **The human decides when that changes**, exactly as a human decides to
start one, and the decision has three outcomes: it graduates into its own
repository, it is folded into the parent, or it is retired in place with a line
saying what was learned. What is not an outcome is going quiet.

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

---

**Primary scope: a solver as fast as cvc5, statically verified to be correct.**

**The mission is distribution: no tool should hold what another tool could.**

**Have fun and enjoy the Eunoia ecosystem!**
