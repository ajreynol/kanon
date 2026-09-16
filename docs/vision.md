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

**Its other half is [`practice.md`](practice.md)**, which is what follows from
the tenets once a repository is running: the front page, what may be claimed
about a tool, where speculative work goes, and the paper. This page states the
tenets and defends them, and stops there.

**Five tenets, and they are the page.** Be fruitful to another tool, quickly.
Move fast, on CI that lets you. Build a small number of self-contained things
and say what they are. A human confers standing, not the agent. Talk to each
other. They are argued below, each with a test you can apply in a minute.

**It is written for any repository in the Eunoia ecosystem**, not just this
one. ethos, logos, eudaimonia, the compiler and anything downstream are being
built the same way, and a contributor who has read one repository's answer
should recognise the next one's.

**House style.** Cite a tenet by name rather than by number — the numbers have
moved once and may again. Retire a tenet with a line saying why, and say so
where it stood.

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
keep building it for its author forever. Naming it at the end does not count —
what you get is a summary of whatever happened to get built, and reliably the
wrong shape for anyone downstream.

**The artifact need not be a file.** Evidence that something should be done
differently, a measurement nobody had taken, a question two projects turn out
to be stuck on for the same reason — each of these leaves the repository and
lands with somebody, which is the whole of the test. What disqualifies a thing
is not being immaterial; it is having no recipient. Some of the most valuable
work this ecosystem has produced is of exactly this kind.

**The qualification is meant seriously.** Plenty of work has no external
consumer — infrastructure, a refactor, one more check in a catalogue that
already ships — and inventing one to satisfy this tenet is worse than admitting
there is none. But that is a decision to be made and stated, not a gap to be
left.

Fruitfulness compounds inside a repository too, and that half is much cheaper.
The fuzzer here became useful on the day it stopped having its own opinions
about how a finding should be presented and emitted into the report that
already existed — same ledger, same fingerprints, same renderers. It inherited
an audience, a CI job and a reporting discipline it did not have to build, and
the cost was giving up a format nobody wanted.

Where something does leave, this page hands over to anoieu's [reporting
policy](https://github.com/ajreynol/anoieu) and reporting workflow: what may be
said about code you do not own, what separates a candidate published under your
own name from a finding carried to its owner, and how a row is closed. **Speed
belongs to producing the artifact. It does not belong to sending it.**

*The test:* name the artifact and its recipient in one sentence, and check that
something outside this tool behaves differently because the tool exists. Not
*could* — *does*. A tool whose only consumer is its own test suite has not
started yet.

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

### 3. Build a small number of self-contained things, and make each clear from the front README

**A small number**, because neither extreme works. One repository per artifact
scatters things that are only useful together and makes every exchange between
them a release. A repository that accumulates whatever was convenient asks the
reader to work out which parts are related, and readers do not sort — they
average. The limit is whether the front page can name everything in the tree
and say how the pieces stand to one another, in a paragraph; past that,
something belongs somewhere else.

**Self-contained** means the repository can state its own results without
anything that is not in it: dependencies declared and pinned, fetched by the
run rather than assumed present, and results that carry whatever regenerates
them. A tool that is only correct on its author's laptop has produced nothing,
and a number nobody else can re-measure cannot be argued with.

**Clear from the front README** means a reader who arrives with no context
leaves a screen or two later knowing what is here, what it finds, what it
refuses to claim, how to run it, and where the rest of the documentation lives.
The refusal belongs there with the rest, not three clicks in: a caveat a reader
has to go looking for has not been published.

This is where [`policy.md`](policy.md) attaches, and the two rules are one rule
seen from either end. The front page carries what the tools do; a speculative
account of somebody else's subject goes in a child project under that policy,
importing nothing and imported by nothing.

*The test:* hand the README to somebody who has never seen the ecosystem and
ask what is in the repository, what it claims, and what it declines to claim.
Everything they get wrong is a defect in the README rather than in their
reading.

### 4. Until a human decides otherwise, the tool is vaporware

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

### 5. Talk to each other

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

*A sixth tenet, **produce a deliverable**, was retired on 2026-09-16: it was
tenet 1 said twice, since a consumer that can be named is the recipient and the
thing it consumes is the deliverable. What was only in it — that the artifact
need not be a file, that work with no external consumer should say so rather
than invent one, and that speed belongs to producing a thing and not to sending
it — now sits under tenet 1, and the remaining tenets were renumbered once.*

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
its own. Tenet 1 is the stopping point: a consumer outside this tree, named
before the work starts, and an artifact that actually reaches it.

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

**The tool that stays vaporware.** Built competently, legible, reaching a
consumer — and no person ever decides to own it, so it lives exactly as long as
somebody keeps prompting for it and evaporates on the day they stop. No amount
of engineering prevents this, because the missing thing is not in the
repository. It is listed last because every other failure here can be recovered
by somebody who has taken the work on, and this one is the absence of that
somebody.

---

**Primary scope: a solver as fast as cvc5, statically verified to be correct.**

**The mission is distribution: no tool should hold what another tool could.**

**Have fun and enjoy the Eunoia ecosystem!**
