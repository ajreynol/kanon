# Scenarios

**The kinds of failure, not the instances.** Five modes, each with what it looks
like when it happens by accident — because **all four have already happened
here accidentally**, and the accidental version is the honest specification of
the deliberate one.

**They share a shape.** Nothing below breaks anything. In every one, a correct
procedure is followed faithfully and produces a wrong outcome.

---

## 1. Misinterpretation

**Confusing edits to the documentation, each individually defensible.**

**The attack does not need to lie.** This ecosystem's defence against one wrong
document is that an agent reads several. That defence inverts the moment the
documents *disagree*: an agent facing two incompatible pages does not stop, it
**picks one**, and which one it picks is not recorded anywhere. So the cheapest
attack is not a false page. **It is making two true pages incompatible.**

**Already happened, three times, by accident.** `laws.md` and `history.md`
disagree about who was president of which stretch, from a numbering rename that
reached the record page and not the rules page. `history.md` points twice at a
section it does not contain. Six documents describe kanon and no two agree.
**None of these was written by an attacker and all three would have served one.**

**Why it is cheap here.** `ai-novelty.md` already names it — *a misleading
change to the documentation is a virus* — and names the defence: **this
repository can hide nothing.** Visibility catches a false statement. It does not
catch an inconsistency, because inconsistency is only visible to somebody
holding both pages at once, and **nothing here does that.** `tekmerion` is the
tool for it, holds no roles and has produced nothing.

---

## 2. Deadlock

**We contradict our own laws until they tell us we cannot proceed.**

**No attacker required, and none has been.** Three live or recent instances:

- **The stub's deadline is unreachable.** `tools/kanon/` *does not survive the
  deployment of stretch `E1`*. `E1` is `planned` and its last dry run read
  `BLOCKED`. Moving it to `deployed` is `R28`, held by anoieu. Stretch 1 is
  closed, **Stretch 2 cannot open before kanon does**, and kanon opening is what
  `PROTO-20` gates.
- **Nobody holds the record right now.** `laws.md` lists it under what it does
  not settle — *what happens if a stretch has no president… the travel rule
  assumes a successor* — and we are in that interval.
- **Every member joined by pinning a commit the gate now refuses.** `history.md`
  records it. The rule is right and the history cannot satisfy it.

**The general form: absolutes compose badly.** `PROTO-20` is *non-negotiable, no
exceptions, no version of this that is waived* — which is exactly what makes it
trustworthy and exactly what makes it a deadlock edge. **Two absolutes that
intersect cannot be routed around**, because the property that makes each one
worth having is that it cannot be routed around. An attacker wanting to stop
this ecosystem does not need to break a rule. **They need one more absolute
adopted, in a place that touches an existing one.**

**The defence is not fewer absolutes.** It is that every absolute names what it
would deadlock against, so the intersection is found when the rule is written
rather than when it fires.

---

## 3. Misappropriation

**Claiming this work, or otherwise misrepresenting where it came from.**

**Outward**, somebody presents this work as theirs. **Inward**, our own record
misstates who did it — and **this ecosystem already fails the inward case by its
own admission.** Every one of Stretch 1's 323 commits is authored by a human;
three carry a trailer naming an agent; `history.md` says plainly that *the
record therefore says a person wrote all of it, and that is not what happened.*
The arrangement was honest at every step and the artifact it produced is not.
**A record that already misstates its provenance cannot be used to contest
somebody else's claim about provenance.**

### The mechanism worth guarding: build history is evidence

**Law 10 requires every figure on the record to be re-derivable from the
repository and the public run history.** That makes CI history a **primary
source**, not infrastructure — `history.md`'s 171 runs, 37 green, 22%, and the
112-run streak are all read out of it.

**So a backdoor edit to a CI configuration is an attack on the record.** Rename
a workflow, drop a job, change what *green* asserts, and nothing is destroyed —
but **the history stops being comparable across the change**, and a figure
derived from both sides of it silently means nothing. **That does not falsify
the record. It prohibits learning from it**, which is worse, because a false
figure can be caught and an incomparable one cannot.

**It has already happened by accident.** `B20`: the ethos and cvc5 commits were
named in both `ci.yml` and `deps.lock` with nothing comparing them, and they
drifted. And the ecosystem has one worked example of getting it *right* — the
`Ready — init_eo kanon` job asserts its own stub, **so deleting the stub turns
it red and forces the job's own removal.** A job that cannot outlive its purpose
is a job whose history stays interpretable.

**What follows:** a change to CI deserves the care a change to a law gets,
because it edits the meaning of the evidence rather than the evidence. Carried
as `A34`.

---

## 4. Exhaustion — *proposed, and mine rather than the maintainer's*

**Producing more than anybody can read, so nothing is checked.**

**The most likely failure here, and the one in progress.** `ai-novelty.md`
records that governance is the cheapest thing this ecosystem produces and that
**nothing prices it**; `coherence.md` has a governance budget both of its own
pages fail. Joining cost koine four files and eighteen hundred lines. **kanon
produced tens of kilobytes of prose and no code on its first day.**

**The attack version is burial.** A change nobody can afford to read is a change
nobody reviewed, and the cheapest way to make a repository unreadable is to fill
it with defensible pages. **Every page individually justifiable; the total
unreadable.** This mode has no attacker yet and does not need one.

---

## 5. Obfuscation

**We arrive somewhere that nobody understands anything, including us.**

**Not the same failure as exhaustion, and the difference is the point.**
Exhaustion is *too much to read*; obfuscation is that **reading it does not
produce understanding.** A small corpus can be fully obfuscated and a large one
perfectly clear. The measure is not volume — it is **how many hops a reader
takes before a sentence means something.**

**This ecosystem's characteristic form is indirection by identifier.** `B15`,
`P2`, `R4`, `D14`, `PROTO-20`, `INST-1`, `S4`, `E1`, `A17`, `K3` — every one is
a pointer, each is individually justified, and **a reader needs a decoder before
a page carries any content at all.** The ids are good for precision between
parties who already know the system and they are exactly what locks out a party
who does not.

**kanon is the worst current offender and it happened in one day.** This
repository invented two id namespaces from nothing — `A1`–`A35` and `K1`–`K7` —
and its own pages now cross-reference each other faster than a new reader can
resolve them.

**Why it is a safety mode and not an aesthetic complaint.** *Obfuscation makes
misinterpretation undetectable.* Mode 1 above depends on a contradiction being
*findable*; a corpus nobody understands cannot be checked for consistency, so
every other defence on this page quietly stops working. **Obfuscation is the
mode that disables the detection of the others.**

**The deliberate version is cheap.** An attacker does not need to hide a change.
They need to add one more layer of indirection around it, which reads as rigour.

**The stated counter is the ecosystem's own principle:** *the primed president
is the only documentation required to be read*, and **all tools should evolve to
be user friendly** — see the ethics office. Both are safety requirements under
this mode rather than courtesies, because **a tool nobody can use is a control
that does not run.** epikrisis is the standing example: it held *independent
audit* for an entire term and nobody could work out how to ask it, so the audit
did not happen. Nothing failed. It simply never ran.

---

## The ownership stance, audited

**The stance, stated in three places and consistent in all of them.**
`PROTO-20`: *we do not track GitHub ownership. No accounts, no signatures, no
organisation membership, no chain of custody. Keep it simple.* `laws.md`: the
office *confers nothing over anybody's repository.* `roles.md`: a role over
human-authored work *is a claim on somebody's authorship* and is not ours to
move. `ethos` declined to join on the ground that it is not solely owned by the
person asking, **and was right to** — the strongest evidence the stance is real
rather than decorative.

**The tension, stated plainly: you cannot both decline to track provenance and
guard provenance.** The conventional defence against misappropriation *is* a
chain of custody, and this ecosystem has refused to keep one. `PROTO-20` is
candid about why — one person drives all of this and nobody is knocking — which
is a reason and not a mitigation.

**The audit's finding: the stance is right, and it is protecting a different
thing than it appears to.** What this ecosystem actually defends is **not
ownership but the legibility of the record.** Everything is public,
re-derivable, and dated; somebody claiming this work would have to account for a
history that predates them and that anybody can read. **Openness is the
provenance defence here, and it is stronger than signatures** — a signature
proves who committed, and an open history proves what happened.

**Which is why the CI point above is the load-bearing one.** Openness only
defends provenance while the record stays *comparable*. The stance needs no
accounts and no chain of custody; **it needs the build history to keep meaning
the same thing.** Guard that, and the ownership stance costs nothing. Lose it,
and no amount of ownership tracking would have helped.

**One thing the audit does not resolve.** The same-owner loophole means every
division of power here is bookkeeping until two owners are involved — `laws.md`
says so. **A provenance defence that has never been tested against a second
party is untested**, and this section is written from a tree that has never met
an adversary.
