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
repositories. Nobody has to catch one. [`kanon-balls.md`](tools/kanon-relations/kanon-balls.md) is
what the office does all day.

Law 12 asks a president to keep a joke about its own name on its front page for
the whole term, on the ground that a president who cannot leave one there has
started to believe the office is important. The test it sets is that the joke
doubles as description. This one does, and it is the only part of this page that
would survive being cut to one line.

## The offices

**`tools/X-Y/` in the repository of the active president X is the office of Y
for president X** — *the office of research for kanon*, and so on. Six are
open, and each was opened with work already in it:

| office | what it holds |
| --- | --- |
| [record](tools/kanon-record/) | what happened, kept current while it happens |
| [relations](tools/kanon-relations/) | who is talking to whom, and who is stuck |
| [distribution](tools/kanon-distribution/) | what one tool holds that another could |
| [readiness](tools/kanon-readiness/) | is anybody blocked, and are we |
| [research](tools/kanon-research/) | what we do not know yet |
| [ethics](tools/kanon-ethics/) | how the office itself behaved |

**The prefix is the term, and an office does not travel.** When the presidency
moves, the successor opens `tools/<their-name>-research/` in its own tree and
these stay here as the record of one term. **The record travels and the offices
do not** — the opposite of `history.md`, and deliberately.

**But what an office *holds* does travel.** A permanent project custodied by an
office keeps its own name and its own history and moves to the successor's
office of the same name; only the heading over it changes, which is exactly how
`roles.md` already describes a child project graduating. The directory is the
term's record; the work inside it is the ecosystem's. **This distinction was
missing from this page until the ethics handoff was decided against my
recommendation, and the gap was here rather than in the decision.**

**They are named in plain English, which follows the register's reasoning rather
than breaking it.** `names.md` asks for Greek and allows descriptive names where
a thing is a program rather than an account — but its real argument is that a
name must grep unambiguously, and the case it cites is a child project called
`ethics` that lasted about an hour because the bare word matched prose about the
subject. **`kanon-ethics` is the repair for exactly that**: the compound never
turns up by accident. A Greek office name would also have to come out of the
register, where `euboulia` and `nomophylax` are held for tools somebody may
build — and spending one on a directory that dies with the term would be a claim
on a name rather than a use of it.

**The offices are internal.** A tool outside this repository has no authority to
look inside them, and the active president reserves that right over its own
offices without sharing it. **This is not a special case.** The ecosystem
already holds that where a register disagrees with a repository about its own
work, the repository is right; the offices are that rule applied, and need no
exception written for anybody in particular. What leaves an office is what kanon
chooses to fire.

*A person reads whatever they like — this is about which **tool** may claim
standing to inspect, not about what `PROTO-20` lets a human read before deciding
anything.*

### What crosses to the next president

**Each office keeps a `handover.md` with four headings, and that file is the
only thing that crosses.** Not the directory, not the working material, not the
office itself.

| heading | what goes under it |
| --- | --- |
| **Established** | shown to be true, with how somebody else re-derives it |
| **Open** | still live, stated without this office's preferred answer |
| **Closed** | answered or abandoned, and why, so it is not raised again |
| **In flight** | mid-motion at term's end, and who holds the other end |

**It is written as things are found, not at the close.** Law 11 already says a
summary composed afterwards is a reconstruction; a finding recalled at term's
end is a memory, and a president who knows the file is being written all along
cannot smooth it later.

**It is pinned, never copied.** The successor cites
`kanon <commit>` and reads it there — the same coordinate `ecosystem.json`
already uses for a member's join, because there is no version number here and a
commit is the honest answer. Copying is what puts one fact in six places.

**Each office writes its own, and the president does not aggregate them.** A
president summarising its own offices is the party describing itself, which is
the failure law 9 addresses one level up. It also lets a successor read one
office without reading a whole term.

**None of it binds the successor.** It is evidence, not instruction — a
predecessor that could bind would be governing after its term. *Nothing yet* is
an answer and is written; an omitted heading is not.

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
