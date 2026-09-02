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
