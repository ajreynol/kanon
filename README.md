# kanon

*κανών — the measuring rod: the standard a thing is held straight against.*

**kanon is where the Eunoia ecosystem keeps its governance, out of the
analyzer**: the policy every member repository is checked against, the checker
that decides it, the inventory of who is in, and the scripts by which a tool
starts, joins and is installed.

All of that lives today in `anoieu`, which is also the analyzer — the tool that
reads member repositories and files findings against them. One repository
therefore writes the rule, decides compliance with it, and reports you for
failing it. Nothing has gone wrong: the same person maintains all of it and is
careful. It is still the wrong shape, and it grows more expensive to change with
every member that pins anoieu in order to get the policy. **kanon is the address
that separation goes to**, so that the judge stops being the prosecutor.

## The office

**kanon holds the presidency for Stretch 2, by bestowal.** The office is a
repository's rather than a person's or an agent's, it expires with the stretch,
it is handed on, and it confers nothing over anybody's repository — including
the ones this ecosystem exists to serve.

**What the president actually does is relational, not technical.** It does not
adjudicate implementation. It asks who is stuck, whether the tools are talking
to each other, and what the office could spend on getting somebody unstuck.
Direction, not permission.

**The office is not the transfer.** Holding the presidency is not permission to
start the governance move — see objection 1 in
[`initial-objections.md`](initial-objections.md). The policy, its checker and
the inventory stay in anoieu until the maintainer raises `B15` again.

## The joke

**κανών is a rod, and a rod is not a cannon.** Say the name out loud anyway and
the unit of work falls out of it: what kanon sends is a **kanon-ball**.

A kanon-ball is short, goes to exactly one tool, and is fired **for** it rather
than at it. anoieu's output is a finding *against* you; kanon's is a kanon-ball
*for* you, and that inversion is the whole reason the two are separate
repositories. Nobody has to catch one. [`kanon-balls.md`](kanon-balls.md) is
what the office does all day.

Law 12 asks a president to keep a joke about its own name on its front page for
the whole term, on the ground that a president who cannot leave one there has
started to believe the office is important. The test it sets is that the joke
doubles as description. This one does, and it is the only part of this page that
would survive being cut to one line.

## The mission

**No tool should hold what another tool could.** That is the ecosystem's stated
mission and it is the whole reason this office exists — the presidency moved
because one tree held most of the work, and it will keep moving for the same
reason. Every term, kanon names at least one thing that could leave anoieu.

**The constraint is latency, not willingness.** The maintainer has been inclined
to move governance since 2026-08-31; what is actually in the way is that a
question to another tool takes hours to land and can sit a whole term
unanswered. **A handoff is a conversation with a deadline, and this ecosystem
does not have a fast conversation.** So making answers fast is not a side
project — it is the enabling work for every move kanon will ever propose.

**And kanon does not build that machinery.** `koine` exists to be the one
implementation of the reporting protocol rather than one per member. A president
building a second would break the mission it holds the office to serve.

**And the mirror, which is the half a president will get wrong first.** *No tool
should be made to hold what it should not.* The office sits above everything and
can therefore pull any tool upward toward the ecosystem's abstractions — usually
by reading its name rather than its work. **A tool that is narrow and fast is
often already doing the grandest thing available to it**, and protecting that is
as much this office's job as redistributing load. `K7` is the case that taught
it, and it is recorded there with the mistake still visible.

**The mission points here too.** Kanon holding what another tool could hold is
its own finding first.

## The offices

**`tools/X-Y/` in the repository of the active president X is the office of Y
for president X** — *the office of research for kanon*. **Three are open**, which
is the floor:

| office | what it holds | in a phrase |
| --- | --- | --- |
| [research](tools/kanon-research/) | the home of `ynoia`, the ecosystem's research engine, which is the authority there | what comes **in** |
| [correspondence](tools/kanon-correspondence/) | what we send, and what came back | what goes **out** |
| [ethics](tools/kanon-ethics/) | how the office behaved, and the ethics projects it custodies | what we **are** |

### Between three and five, and no more

**A president holds at least three offices and at most five.** Fewer than three
and the term is not ambitious enough to need a structure at all; more than five
and nobody can say what each one is for. **This repository proved the second
half the hard way**: it opened six in an afternoon and the maintainer could not
explain four of them, which is the only evidence a rule like this ever gets.

**Kanon cannot make that a law, and does not pretend to.** `laws.md` is
deliberately narrow — it governs `history.md` *and nothing else*, and says in
terms that a law about anything else does not belong in it. Amending it is the
maintainer's, and **a president proposing an amendment writes the proposal and
does not apply it.** So the range above is this repository's own practice,
binding on kanon from now, and separately a proposal to anoieu carried as `K5`.
If it is ever a law, somebody other than the president will have made it one.

**There were six for about an hour.** The other four — record, relations,
readiness, distribution — were a list, an output, a status and a mission
wearing directories, and the maintainer could not tell what four of them were
for. **That was the evidence.** Nothing was deleted except the containers: the
mission is above, the list is [`actionable.md`](actionable.md), the output is
[`kanon-balls.md`](kanon-balls.md), the findings moved into research, and
readiness is what the check reports rather than a place.

**The prefix is the term, and an office does not travel.** The successor opens
`tools/<their-name>-research/` in its own tree; these stay as the record of one
term.

**But what an office holds does travel.** A permanent project custodied by an
office keeps its own name and history and moves to the successor's office of the
same name — only the heading over it changes, exactly as `roles.md` describes a
child project graduating. `martyria` and `zetesis` are the first.

**The offices are internal.** No tool outside this repository has authority to
look inside them. **This is not a special case**: the ecosystem already holds
that where a register disagrees with a repository about its own work, the
repository is right. What leaves an office is what kanon chooses to fire.

*A person reads whatever they like — this is about which **tool** may claim
standing to inspect, not what `PROTO-20` lets a human read.*

## What crosses to the next president

**One file: [`handover.md`](handover.md), with four headings** — *Established*,
*Open*, *Closed*, *In flight*.

**It is written as things are found, not at the close.** Law 11 already says a
summary composed afterwards is a reconstruction; a finding recalled at term's
end is a memory, and a president who knows the file is being written all along
cannot smooth it later.

**It is pinned, never copied.** The successor cites `kanon <commit>` and reads
it there — the coordinate `ecosystem.json` already uses for a member's join.
Copying is what puts one fact in six places.

**Closed items cross too.** A successor with fresh eyes re-raises dead
questions; the dedup has to run against everything seen, not everything kept.

**None of it binds the successor.** Evidence, not instruction — a predecessor
that could bind would be governing after its term. *Nothing yet* is an answer;
an omitted heading is not.


## The question it answers

*Does this tree meet the ecosystem's written standard, and what does joining ask
of it?*

A tree, a standard somebody wrote down, and a report of where the two differ.
The answer is mechanical, and it is worth exactly as much as the standard is: a
rod measures against a stated length, or it measures nothing.

## The question it does not answer

*Is this repository any good?* This is the larger question, and the one anything
labelled governance is most likely to be read as answering. It does not answer
it. A tree can satisfy every rule and be worthless, or break several and be the
best work here. Whether a project is correct, honest, well made or worth having
is examined elsewhere — `dokimasia`, `martyria`, `zetesis` and `ynoia` are what
that is for — and kanon has no opinion to offer.

Two narrower ones, for the same reason:

- **Whether a rule should exist.** kanon holds the standard and applies it.
  Amending it is a person's, argued on anoieu's board and in ynoia's proposals.
  There is no vote here.
- **Whether a finding against you is fair.** Findings stay with the analyzer.
  Moving them here would rebuild the thing this repository exists to take apart.

## What it would take to run it

**Nothing here runs.** There is no policy, no checker, no inventory, no scripts,
no tests and no CI. This repository is this file. There is nothing to install,
nothing to invoke, and no output to read.

To check a tree against the ecosystem's policy today, run anoieu's
`tools/policy_check.py` — which is what the four member repositories, anoieu,
eudaimonia, dokimasia and koine, pin in their CI. That is the answer today, and
the move is not approved: the audit (`P2` in ynoia's proposals) is open, and the
board item (`B15`) says in as many words *do not start the move* while its scope
is still being cut.

## The name

kanon was reserved before this repository existed, in ynoia's register of names,
and was not chosen here. κανών is the carpenter's rod: the straightedge you lay
against a thing to see where it bends. It names the instrument rather than the
authority, which is the right relationship — the rod decides nothing, and
somebody has to hold it.

Two places the etymology is worth doubting. The name stands either way.

**The English word.** *Canon* means scripture and lists of approved works, and a
governance repository is the one place that misreading does real damage. The
register records the objection already, and the answer is only to say it out
loud: this is a rod, not a canon, and nothing in it is scripture.

**The rod names one of the three jobs.** Measuring is what the checker does. The
inventory and the joining scripts are not measurement — they are admission and
housekeeping, and no reading of κανών reaches them. By the register's own test,
an explanation that has to stretch means the scope is not settled yet; here that
test is working rather than failing, because `B15` records the scope as still
being cut, most likely down to the joining rule and its checker. Cut that way,
the name gets more accurate rather than less.

## The stub

`tools/kanon/` in anoieu is a stub: a placeholder directory carrying one
sentence, which says to delete it once its replacement is safely in the
ecosystem. This repository is the replacement it names. Saying so is the spawned
repository's half of the handoff protocol (`PROTO-20` in anoieu's
`docs/coherence.md`); anoieu's half is only to clear away markers that have gone
stale.

So, plainly: **this is the kanon that stub holds a place for, and it is not yet
in a state to take that place.** The protocol judges the claim by reading the
repository rather than the message, and there is nothing here to read but this
file. It also asks for CI passing on both sides with no exceptions, and a
repository that runs nothing is *unknown*, which is not a pass. **The stub
should stay.** An agent does not delete one in any case — that is a person's,
and no amount of evidence changes it.

The name is not a title. Nothing tracks who owns it, and a second repository
doing this work would be as welcome as this one.
