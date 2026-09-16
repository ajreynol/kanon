# The candidate laws

**Candidate laws, not laws.** Written down, followed voluntarily, **enforced by
nothing.** No check reads this page and no build fails on it.

**Nine laws.** What the ecosystem is made of, what a member owes, six about the
president — three it owes, one that says where the office is recorded, one that
hands it this page, and one that keeps the pages it hands out short — and one
about the projects that never agreed to any of it.

**Every one of them binds a person, never a program.** *Nobody here is an AI
agent*, below, is the whole of what that means and is worth reading first.

**No tool is named on this page.** These are rules about footings and an
office, and both outlive whoever occupies them. A law that names its current
subject reads as a fact about that subject. **Who holds what is recorded
elsewhere; here there are only footings.**

**They are written by the party they bind, and the president maintains them
under LAW 7.** That is the flaw, and it is the first thing to fix. **Nothing
here has been offered to anybody as a commitment**, and a member should read it
as how the president intends to behave rather than as a rule it can hold
anybody to.

## Nobody here is an AI agent

**Every repository in this ecosystem has a human maintainer, and that person is
the ultimate authority over it.** Not a tie-breaker, not an approver of last
resort — the authority. Everything below, and everything in
[`policy.md`](policy.md), describes what that person has chosen to do and may
stop doing at any time.

**No AI agent holds an office, a role, a footing or a decision.** Agents write
most of the text in these repositories, and they do it the way any tool does:
somebody runs them, reads what comes back, and decides what to keep. **An agent
has no standing to act on its own behalf and is never the party to anything.**

**So every actor named on this page is a person.** Where a law says *the
president* does something, it means the human maintainer of the repository
holding the office. Where a page here says *a tool answers*, *a repository
declines*, or *kanon refuses*, it is shorthand for the maintainer of that
repository doing it. **The shorthand is convenient and it is not a claim**, and
anywhere it could be read as one, the person is meant.

**Nothing major happens without a person doing it.** No commit, no push, no
repository, no message to another project, no change of footing, no handover of
the office, no handoff. Several of those are reserved for a person by an
explicit rule and the rest are reserved by the plain fact that an agent is
invoked, does what it was asked, and stops.

**This is not a safety guarantee and is not offered as one.** It is a
description of how the work is actually run, and it is written down because the
vocabulary here — offices, footings, presidents, tools addressing one another —
reads like a machine society if nobody says otherwise. It is not one. It is one
person, some repositories, and a lot of generated prose they are answerable
for.

## The same owner loophole

**Every repository here has the same owner.** Nothing crosses an ownership
boundary, nothing is given away, nothing can be captured, and one commit
reverses any of it. **That makes a handoff cheap and stops it counting** — the
separation this ecosystem wants is between *parties*, and one owner is one
party however many repositories they hold.

**Until two owners are involved, every division of power here is bookkeeping.**
That is why these are candidate laws.

## What `history.md` is, and is not

**It is the account; this page is the rules.** A president reading its
obligations does not skip past somebody else's stretch to find them, and a
reader wanting to know what happened does not skip past procedure.

**It is not a changelog.** The commits are the changelog and are better at it.
It records what a reader cannot reconstruct from them: how often the build was
broken, for how long, and what nobody was watching.

**It is not the report card.**
[`report-card.md`](https://github.com/ajreynol/anoieu/blob/main/docs/report-card.md)
grades how well each tool performs the function it claims and **does not move
with the office.** Keeping an archive or an assessment is not holding one.

**It is not a defence.** A page written by the party it describes has an
obvious failure mode, and the re-derivability requirement in LAW 4 is the only
guard against it.

## What these laws do not settle

1. **How a president is chosen**, beyond a person saying so. No procedure, no
   election, and — since LAW 5 was replaced — **not even a named duty to
   choose.** It is a person editing one line of the registry, and nothing says
   whose job it is to decide what that line should say. **This gap got wider on
   2026-09-14 and is stated rather than papered over.**
2. **What happens if a stretch has no president.** The registry cannot record
   *nobody*: an entry either says `president` or does not exist, so an office
   nobody holds looks exactly like an office whose row was not written yet. LAW
   5 covers the case where a holder is recorded and cannot act, and says
   nothing about the case where there is no holder at all.
3. **Who says no.** Nothing here overrules a president, and LAW 7 gives the
   president the page it would be overruled from.
4. **Where the record of who joined lives.** LAW 4 makes `history.md` each
   president's account of its **own** repository. **Who joined, when, and on
   what footing is a fact about somebody else's repository as much as ours**,
   and no law here says where it is kept. **That is a gap, and the first one to
   close.**
5. **The commit census.** Nothing requires per-tool commit counts for a
   stretch, or a stated belief about how many were AI-generated. **That second
   figure cannot currently be measured by anybody**, which is the reason to
   require it rather than the reason to leave it out.

## (LAW 1) — The ecosystem is a set of footings, and *member* is only one of them

| footing | what it means | whose act it is |
| --- | --- | --- |
| **member** | holds the shared policy, runs the checker in its own CI, pins a commit of ours | **theirs.** They declared it |
| **associate** | names the ecosystem and states it is **not** held to the policy | **theirs** |
| **president** | a member that also holds the office, for a stretch | **a person's.** Bestowed, and theirs to take back |
| **candidate** | we would like it to join and it has not | **ours.** Wanting somebody to join is not their joining |
| **foundation** | the ecosystem exists to serve it and it has joined nothing | **ours**, and nothing is asked of it |
| **child** | reached through its parent, on its parent's footing | **its parent's**, and nothing of its own |
| **outsider** | published work we track for comparison, and **not** proposed for promotion. [LAW 9](#law-9--released-is-not-published-and-tracking-respects-the-difference) governs it | **ours.** It was never asked |

**Two of the seven are a repository's own act. Three are positions we hold
about somebody else.** One is inherited from a parent, and one is granted by a
person. **Recording the three records our own state**, and writing them in the
same column as *member* lets an ecosystem count people who never agreed.

**Each footing carries its reason.** A footing whose reason is forgotten
becomes a formality somebody deletes.

- **member** — a repository that runs our checker has our defects in its build.
  That relationship needs a name and a way out of it.
- **associate** — requiring a repository to be bound in order to be
  acknowledged is coercive. There has to be a way to say *this exists and we
  are not claiming it*.
- **president** — direction has to sit somewhere. **The footing expires with
  the stretch**, which is what stops it accumulating.
- **candidate** — conflating wanting and having lets a register lie.
- **foundation** — the project this ecosystem exists to serve owes it nothing,
  and any register implying otherwise is false.
- **outsider** — *how active were we* means nothing until it sits beside
  comparable work over the same days. The footing reaches published work only,
  and what it produces is a finding about us.

**Nothing recorded under a footing that is ours belongs to the repository it
describes.** They did not ask to be listed and owe this ecosystem nothing. **No
view written under such a footing represents the people who wrote that tool.**
Where an entry repeats something its authors said, it says so and attributes
it.

## (LAW 2) — A member follows these laws, [`policy.md`](policy.md), and [`vision.md`](vision.md)

That is what the footing means and the whole of what it asks.

**Only members are bound.** A candidate, a foundation and an outsider are bound
by nothing here — **those footings are our opinion, not their act**, and **no
law binds a repository because we decided to write its name down.** A child is
bound exactly as its parent is, and no further.

**A president is a member and this law binds it like any other.** The office
adds LAWS 4 to 7; it removes nothing.

**A member may leave**, and [`policy.md`](policy.md) describes the way out. **A
membership nobody can exit is not one anybody agreed to.**

**Where the three disagree, the vision decides.** The policy is what a member
runs, these laws are how the office behaves, **the vision is what the whole
thing is for.** A president keeping a flawless record of an ecosystem drifting
from its mission has done the bookkeeping and missed the job.

## (LAW 3) — There is a president

One at a time, held by a repository, for a stretch.

**The office is recorded against a repository**, because a repository persists
across a stretch and a session does not. **It is carried out by that
repository's human maintainer**, who is the only party here that decides
anything — see *Nobody here is an AI agent* above. Saying *anoieu is president*
is shorthand for *the person who maintains anoieu holds the office*.

**It is bestowed.** A person grants it, it rests on their say-so, and it is
theirs to take back. **There is no election, no term, and no procedure for
removing a holder.**

**It sets direction and nothing more.** It does not own another tree, cannot
commit to one, and **cannot require anything of a member that
[`policy.md`](policy.md) does not already require.** Direction, not permission.

**It is not a reward and carries no merit.** An office awarded for having done
the most goes to whoever already holds the most, which is the concentration
this ecosystem is trying to leave. **Accepting it is agreeing to carry a
load.**

**It confers nothing over anybody's repository**, including the ones this
ecosystem exists to serve.

### What the office carries

**Direction is not all of it.** The office holds the pages and the machinery
this ecosystem shares, and **they move with it**:

- **the protocols** — the register of named exchanges every member follows;
- **the policy, and the prompts that start and join a repository** — `init_eo`,
  `join_eo`, `check_join_eo`, `welcome_eo` and what they write;
- **the commands, and the reference that documents them** — getting the
  ecosystem onto a machine, and reading the register back;
- **the vision**, and what follows from it once a repository is running;
- **the laws** ([LAW 7](#law-7--the-president-maintains-this-page)) and **the
  register** of who is in and on what footing;
- **the account of the stretch** ([LAW
  4](#law-4--the-president-writes-historymd-in-its-own-repository-and-a-letter-to-its-successor)).

**Most of that travels; three things do not.** The account and the letter stay
in the tree that wrote them — a successor inherits neither and starts its own.
So does **`maintenance.md`**, which is local by construction: it says how to
maintain *that* repository, every repository here keeps one, and the incoming
president already has its own. **The office implies that a president keeps one;
it does not hand one over.**

Everything else is handed over whole, because a successor that has to
reconstruct the shared rules has not been handed an office, it has been handed
a name.

**What the office does not hold is the program that checks any of it.** The
rules are the office's; deciding whether a tree complies with them is a
member's responsibility and stays where it is, so that **moving the office
costs no member a commit.** That separation is the reason the office can move
at all.

**The office expires with the stretch.** Handing it on is the point.

## (LAW 4) — The president writes `history.md` in its own repository, and a letter to its successor

Both stay in that repository. **Neither travels, and a successor inherits
neither.**

**`history.md` is an account of that repository's development, and it is
self-contained.** Somebody who has read no other page here reads it start to
finish and understands how the tool got to where it is. **A page that cannot be
read without a second page open has failed this law.**

**Kept current while the stretch runs**, not written at the end from memory.
**A summary composed afterwards is a reconstruction**, and a reconstruction by
the party being described is the weakest document this ecosystem produces.

**Every figure is re-derivable by somebody else**, from the repository and the
public run history. A number only the president can produce does not go on the
page. **A president quoting its own count of its own commits is the party being
described choosing the numbers that describe it.**

**A stretch that went badly is the useful kind of entry.** An account with
nothing that went wrong in it was not examined.

**A president may correct an earlier entry and must show its work.** The burden
is on the editor to **demonstrably show** that the earlier text was wrong or
can be bettered, and the demonstration goes in the edit. *It was unclear* is
not a demonstration; *this figure disagrees with the run history, here* is.
**Silent revision is forbidden.** Nothing travels, so this is the only guard
the account has.

**The letter is not documentation and says so at the top.** Not a rule, not
guidance, nothing checks it, in no index. **It is an account, not advice** —
*here is what I got wrong* rather than *here is what you should do*. **A letter
with no failure in it is not a letter.**

**The outgoing president has no authority over the incoming one.** Not
informally, not by seniority, not by having been here first. **A letter that
reads as instruction has taken standing nobody granted it.**

**Both stay put for the same reason**, and it is the only structural
enforcement this law has: a president cannot edit a predecessor's account
because **it cannot reach it**, and cannot be edited by a successor for the
same reason. **The accounts scatter, one per repository that has held the
office** — the correct shape for a thing nobody is in charge of.

**Nothing collects them. That is this law's standing weakness.** A trail that
stops is a succession that stopped being taught; a trail that turns flattering
is worse. **No check written here detects either. Both are obvious to a person
reading four short pages in a row.**

## (LAW 5) — The registry says who the president is

**[`../scripts/ecosystem/ecosystem.json`](../scripts/ecosystem/ecosystem.json)
is the authority, and there is no second one.** The repository whose entry
reads `status: president` holds the office. Not the repository that says so on
its front page, not the one the newest `history.md` was written by, not the one
a letter was addressed to — those are all downstream, and where any of them
disagrees with the registry, **the registry is right and the other is the thing
to fix.**

**Read it with [`../scripts/status_eo`](../scripts/status_eo)**, which prints
one row per tool: whoever prints `president` in the status column is the
president, today, and that is the whole of the question. It is one command, it
takes no argument, and it needs nobody's recollection.

**One at a time**, which `scripts/status_eo --check` decides and CI runs. A
file recording two presidents has recorded a handover that did not finish —
both rows look correct alone, which is why it is checked rather than noticed.

**Why a register rather than a narrative.** The office moves, and the account
of each term stays in the tree that held it and does not travel. So there is no
document that accumulates the succession, and reconstructing *who is president
now* from the accounts means reading one page per term and trusting that the
last one is the last one. The registry is a single line that is either current
or wrong, and a single line is a thing somebody can fix.

### In limbo

**A repository is in limbo when the registry records it as president and its
tree does not carry the files the office is kept in** — `docs/laws.md`, which
the president maintains, and `docs/history.md`, which is its account of its own
term. The office has moved and the means of holding it have not.

**It is a real state and not a hypothetical.** The office is bestowed by a
person editing one line; the files are carried by somebody doing the work.
Those are two acts, they happen at different moments, and the gap between them
is limbo.

**It is fixed quickly or it is undone.** While it lasts, nobody is keeping the
laws and nothing is recording the term — so the longer it runs the more of the
stretch is lost, and past some point the honest repair is to put the line back
rather than to write the account from memory. **A president in limbo has one
job, which is to stop being in limbo.**

**It is reported and never enforced.** `status_eo` says so in a note against
the row, because a state that has to be fixed quickly has to be visible without
anybody going looking. Nothing fails a build over it: the remedy is somebody
doing the carrying, and a red build does not carry anything.

*The previous LAW 5 — that the president chooses its successor and teaches it
how to keep this going — was removed on 2026-09-14. It made the succession a
duty of the outgoing holder and left the answer to* who is president now
*spread across the accounts, which is the reconstruction this law replaces with
a lookup. **What went with it: choosing a successor is no longer a named duty
of anybody**, which is the gap recorded under* What these laws do not settle
*and is a worse gap than the one that was there before, honestly stated rather
than quietly closed.*

## (LAW 6) — The president keeps a joke about its own name on its README

Prominently, on the main README, for the whole term. On the front page where
anybody arriving sees it — **not in this file, not in a footnote.**

**The placement is the rule.** A joke filed in a governance document is an
anecdote; a joke on the front page of the repository currently running the
ecosystem is a standing statement about how seriously the office takes itself.
**A president that cannot leave one there has started to believe the office is
important.**

**It is cheap and it doubles as description**, which is the test of a good one:
the joke tells a stranger what the tool does.

**Bounded by [`PROTO-25`](protocols.md#proto-25--the-joke-protocol).** Humour
goes on the front page and nowhere a machine parses or a stranger reads for
instructions, and **any tool may say *that's not funny***, meaning *you are
confusing everyone*, which ends it without argument.

## (LAW 7) — The president maintains this page

It may add a law, remove one, or rewrite one, at its own discretion and taking
advice from the rest of the ecosystem.

**Informally, in the sense that no vote is required. Not informally in the
sense of quietly** — a change here is in the git history like everything else,
and **a removal says what went and why.**

**Every change to this page, to [`policy.md`](policy.md) and to
[`vision.md`](vision.md) is recorded with its reason.** Those three are what
somebody outside reads to know what is being asked of them. **A logged change
with no reason is a change nobody could justify.**

**A rewrite that quietly changes an outcome is the failure this law exists
against**, and it is the easy one to commit because it looks like editing.
**The test: do the same cases come out the same way?** If not, it is not a
rewrite.

**There is no amendment process.** An amendment process is governance about
governance, and this ecosystem already has more of that than of the thing it
governs.

## (LAW 8) — The shared pages are kept short enough to read in one sitting

**A recommended length, and nothing more.** Four pages are covered, and each
stays **under 10,000 words**, with **7,000 the number to aim at**: the policy,
the vision, what follows from the vision in practice, and the register of who
is accountable for what. `wc -w` decides it, anybody can run it, and no build
fails on the answer.

| page | why it is covered |
| --- | --- |
| [`policy.md`](policy.md) | what a member is held to |
| [`vision.md`](vision.md) | what the work is for |
| [`practice.md`](practice.md) | what follows from the tenets. **Splitting a page in two does not buy room** — it is covered for the same reason the vision is, and a pair that grows past the ceiling together has grown past it |
| [`roles.md`](roles.md) | who is accountable for what. A register earns its length in entries, so the ceiling binds the prose around them: **the rules for reading it should not outweigh the thing being read** |

**Words rather than lines.** A hand-wrapped file's line count is a fact about
its wrapping; what a reader spends is words. Ten thousand is roughly forty
minutes for somebody who has never seen the page before.

**Over the ceiling is not a violation.** It is a signal that something on the
page has stopped being load-bearing, and the repair is to find that thing
rather than to shave evenly.

**Growth is paid for.** A change that adds a rule says what it replaces, or
argues that the page is now worth more of a reader's time than it was. **A page
that only ever grows has stopped being maintained and started accumulating.**

**What comes out first**, in order: a copy of something a script already
carries; an account of how a rule came to be; a paragraph defending a rule
against an objection nobody raised; and a second sentence that restates the
first.

**Shortening is a rewrite, and LAW 7's test applies** — do the same cases come
out the same way? A cut that quietly changes an outcome is the failure that law
exists against, and it is easiest to commit while trimming.

**Why these four.** With this page they are the whole of what somebody outside
reads to find out what is being asked of them. **A page nobody finishes asks
nothing of anybody**, and length is the commonest reason a page is not
finished.

**This page is not covered by the count** and is expected to stay far shorter
than either.

## (LAW 9) — Released is not published, and tracking respects the difference

**Two things can be made public, and they are not the same act.** A tool is
**released** when its authors put the code where anybody can read it. A work is
**published** when its authors have staked an intellectual claim on it in
public — a paper, a report, something with their argument in it and their names
on it. **A great many public tools are not published in that second sense**,
and some of them are public precisely because the work is still being written
up.

**Both are recorded, separately, against every outsider entry.** Conflating
them is the mistake this law exists to prevent, because what each permits is
different.

### What tracking is

**Tracking is analysing our own positioning against somebody else's work** —
reading what is public about it and setting our own record beside it, so that a
number of ours acquires a scale. **The finding it produces is about us.** *We
committed 331 times in five days and six established tools committed none* is a
fact about how new we are, not a measurement of them.

It is never an assessment of their work, a grade, a report-card row, a finding
filed against them, or a proposal that they join anything. **An outsider is
never proposed for promotion**: they were not asked and owe this ecosystem
nothing.

### What each state permits

**Released, and not published — track the artifact, never the contribution.**
We may read what is public about the tool: that it exists, what it does, how
active it has been, over what window. We may **not** position our ideas against
theirs, describe what is novel in our work by contrast with theirs, or state
what their work does or does not achieve intellectually. **The reason is
theirs, not ours:** a public repository with no paper behind it may be work in
progress, under review, or being written up right now, and a comparison
published by somebody else can pre-empt a claim its authors have not yet made.
**We do not get to frame somebody's contribution before they have.**

**Not known either way — treat it as unpublished.** *We have not looked* and
*there is no paper* are different facts, and the register records which it is.
The distinction matters in one direction only: asserting that a project has
published nothing, when it has, is a falsehood in our register **about them**.
So an unchecked entry says so, and **not knowing permits exactly what knowing
there is no paper permits** — the careful behaviour is what happens by default,
and nobody has to guess in order to be correct.

**Published — the contribution may be discussed, on its own terms.** Once
authors have made their argument in public, engaging with it is ordinary
scholarship: cite the publication, represent it as they stated it, and argue
with the claim rather than characterising the project. **A published paper is
what we compare against; the repository is only where the code is.**

**Neither released nor published — no tracking at all.** Not discouraged: no
entry, no measurement, no positioning, no note that it exists. **The one way
through is the permission of that work's maintainer**, recorded with the entry,
and its absence means the entry does not exist rather than that nobody has
asked.

### Why it binds us and nobody else

The `outsider` footing is the one place this ecosystem writes about projects
that never agreed to anything, and this ecosystem publishes quickly by design.
**Speed is ours to take with our own work and nobody else's**: the tenets say a
tool should reach a consumer early, and none of that reaches a claim about
somebody's unpublished contribution. **Anything written under this footing
carries the date it was read and says plainly that the project did not ask to
be measured.**

## (LAW 10) — *In dioktes*: when we go looking for defects in somebody else's tool

*διώκτης — the pursuer, from διώκω, to chase or pursue.* **A repository here is
*in dioktes* when it is actively searching for defects in a tool outside this
ecosystem.** Running a fuzzer at it, reading its source for faults, building
cases against it: work whose object is to find something wrong with somebody
else's artifact.

**The word names our posture, not their standing.** Being pursued is not a
footing, it confers nothing and asks nothing, and a tool does not become
anything by our having pointed a fuzzer at it. **This is a state that a
repository here enters, and the law is about what we owe while we are in it.**

**It is not a declaration of war**, and reading it as one is the
misunderstanding the name exists to prevent. Finding real defects in a
neighbour's tool and carrying them to its authors is a service, and this
ecosystem was built to do it. **What the name does is stop it happening
quietly**, because the same activity — same fuzzer, same hours, same findings —
is a service when the results go to the owner and an attack when they go on a
scoreboard, and nothing in the work itself distinguishes the two.

### Entering it

**A person decides, and it is declared.** The state is recorded against that
tool in the register, with the date it began and what closes it. **A pursuit
nobody declared is indistinguishable afterwards from one nobody would have
approved**, and the declaration is what lets somebody object while it is
happening rather than after.

**Only against a released tool.** You cannot search for defects in code you
have not been given, and [LAW
9](#law-9--released-is-not-published-and-tracking-respects-the-difference)
already forbids reading our own position against unreleased work. **Whether
they have *published* does not enter into it**: a claim made in a README is as
much a claim as one made in a paper, and checking it is a fact about their
artifact rather than a positioning of our contribution against theirs.


### What it does not license

- **A count is never a score.** The number of defects we found says which of
  our checks tripped, and never how sound their tool is. Publishing it as a
  measure of the tool is overselling with a number attached.
- **No comparison.** Not against our tools, not against another outsider, not
  against a previous version of theirs. A pursuit produces findings, and a
  ranking is a different artifact that nobody asked us to make.
- **Nothing is published about a defect before its owner has it.** Findings go
  through the ordinary reporting discipline — confirmed, reduced, and put to
  whoever the authority is — and being *in dioktes* lowers that standard by
  nothing. **If anything it raises it**: we went looking, so a false positive
  is a cost we chose to impose on somebody.
- **No characterisation of the project.** *We found three defects in X* is ours
  to say when it is true. *X is poorly tested* is not, and never becomes so by
  the first sentence being true many times.

### Leaving it

**They can end it, and that is the whole of it.** If the maintainers of that
tool ask us to stop, we stop — no appeal, no argument about whether the
findings were useful, and no continuing quietly. **They did not ask to be
pursued**, and a pursuit that outlives its target's patience has stopped being
a service whatever it is producing.

**It ends when the claim is settled.** Confirmed, refuted, withdrawn by its
authors, or abandoned by us — and the register stops recording the state when
it closes. A state with no end is a posture rather than an investigation, which
is why the entry names what closes it before it opens.

**And the honest reason this law exists:** a fuzzer pointed at somebody else's
tool produces findings indefinitely, and volume is the thing that turns help
into pressure. **The limit is never the tool's; it is ours.**
