# The report card

**How each tool stands against the five tenets of
[`vision.md`](../../../docs/vision.md).** Written and kept by stathmos, which is
the whole of what `R30` in [`roles.md`](../../../docs/roles.md) is.

**It is not a build step and must not become one.** That is vision.md's rule
rather than this page's: *adherence to policy is tracked automatically, and
adherence to vision must never be*, because a checker returning a verdict on
*is this tool fruitful* would manufacture an authority that does not exist.
Nothing here is computed. Every paragraph is read out of a tree by somebody and
can be argued with by anybody, and **a person may overrule any of it without
giving a reason.**

**It binds nobody.** None of these projects agreed to the tenets, most predate
them, and no row here is a finding — a claim about somebody else's code goes
through the reporting workflow, confirmed and reproduced small and carried by a
person, and nothing on this page has been through any of that.

*This edition supersedes anoieu's `docs/report-card.md`, last graded
2026-09-02, which is the previous edition and stays where it is. The role moved
with stathmos; the page it used to name did not.*

## The bands, the axes, and the one real check

**Four bands — excellent, good, fair, poor.** *Fair* means there is something
worth doing, not that anything is wrong; most rows sit there and that is
unremarkable. **Poor is the only band that says something went the wrong way**:
it means the thing works against what the ecosystem is aiming at, so that not
having done it would have left the ecosystem better off. A gap is *fair*; a
negative contribution is *poor*. The word describes an effect and not an intent.

**Three axes, because one grade hides where the work is.**

- **delivered** — does anything outside this project behave differently because
  it exists?
- **legible** — can somebody arriving find their way, and is the front page the
  entry point?
- **checkable** — can a claim about it be re-derived by somebody who does not
  trust us?

**There is no formula, and there is nothing here to optimise against.** A
published rubric becomes a target, and a project that improved its band without
improving anything else would have found a defect in the page rather than in
itself. What replaces a formula is not a method but an exposure: **the evidence
is named, the date is on the row, and the tool that writes this page and the
tree that houses it are graded on the same scale.** Those are `stathmos` and
`kanon`, and neither comes out best.

## The standing, graded 2026-09-16

| tool | delivered | legible | checkable | last graded | the paragraph says |
| --- | --- | --- | --- | --- | --- |
| `cvc5` | excellent | good | *not from here* | 2026-09-02 | five consumers, no API, no coordination |
| `ethos` | excellent | fair | good | 2026-09-16 | the manual is a program's, not the language's |
| `ethos-eoc` | good | fair | *unconfirmed* | 2026-09-02 | a large change may have overtaken the grade |
| `anoieu` | fair | fair | excellent | 2026-09-16 | the band it was in has an exit, and the exit looks met |
| `logos` | excellent | fair | excellent | 2026-09-16 | still carries somebody else's ground truth by copy |
| `eudaimonia` | excellent | good | excellent | 2026-09-16 | the pipeline generalizes and the proofs do not |
| `dokimasia` | fair | good | *not from here* | 2026-09-16 | one finding filed, and the rest are hypotheses |
| `koine` | good | excellent | good | 2026-09-16 | both customers now pin it |
| `kanon` | good | good | good | 2026-09-16 | it writes faster than anything reads |
| `tachyon` | fair | good | excellent | 2026-09-16 | a ledger that fills daily and nothing downstream yet |
| `eschaton` | fair | excellent | fair | 2026-09-16 | three bets, one page each, nothing run |
| `epikrisis` | fair | good | excellent | 2026-09-16 | took the audit on 2026-09-17; the laws no longer ask for the census |
| `stathmos` | fair | good | fair | 2026-09-16 | it writes this page, and its own evidence file is older than it |

**Read a row across, not down.** A column is not a league table: these projects
do different things, and `eschaton` being *excellent* on legibility while *fair*
on delivery is the useful fact, not its position relative to anybody.

**Three fields per entry**, named along the ecosystem's convention: **arete**
(ἀρετή, excellence) what it does well and what another project should take from
it; **elleipsis** (ἔλλειψις, a falling short) where it comes up short, with the
evidence; **parainesis** (παραίνεσις, counsel) what follows.

**Two registers, and the project's own maintenance note decides which.** A
project run by people gets an observation and no imperative — the tenets were
invented here and nobody agreed to them. A project run by agents gets an
instruction and no apology, because there is nobody to offend and hedging is
expensive at the rate an agent produces work.

---

## cvc5

**Arete.** Tenet 1 at its strongest, largely by an accident of format: CPC sits
in cvc5's own tree as plain text under `proofs/eo/cpc/` and is read by ethos,
compiled by `ethos-eoc`, copied into logos, vendored by eudaimonia and analyzed
by anoieu — five consumers, no API, no release process, no coordination. That
is the pattern this page generalizes from rather than one it taught.

**Elleipsis.** *Not re-established this round.* cvc5 is the one subject that is
not on the machine this was graded from — the installer marks it opt-in and
nothing here needs a working copy. The 2026-09-02 entry recorded `cvc5-1`, two
programs in `programs/Strings.eo` declaring `Int` where every case returns a
Boolean, as standing after having been recorded as fixed when it never was.
**Nobody has looked since**, and an undated claim about somebody else's tree is
the weakest thing this page can carry.

**Parainesis.** An observation, and it is about us rather than about cvc5:
grading a foundation we have not cloned is the thinnest row on the page, and the
fix is one clone rather than an argument. Tenets 3 and 5 do not apply here at
all — cvc5 sits outside the ecosystem, which exists to serve it.

## ethos

**Arete.** The clearest instance of tenet 1, and worth studying because the
fruitfulness was not designed: a checker written in C++ to answer *does this
proof check* became a build dependency of a Lean development, which vendors it,
and the reference implementation inside every project eudaimonia generates.

**Elleipsis.** `user_manual.md` is the definition of Eunoia and the document the
whole ecosystem reads, but it is a manual for a *program* — it never draws the
line between what the language requires and what this implementation happens to
do, which is why a second implementation cannot be written from it. The
ecosystem's answer is a child project of kanon's that exists only because of
this gap. Our policy checker reports 3 failures against its tree; **that is a
measurement and not a shortfall**, because ethos is a candidate that never
joined and owes none of it.

**Parainesis.** An observation. The two fuzzer defects this page has carried
since 2026-09-02 — an uncaught C++ exception on `(declare-const f (->))`, and an
error path that skips ethos's own `Error:` convention — **are still unfiled, two
weeks on**. That is anoieu's shortfall and not ethos's, and it is recorded in
both entries because an unfiled finding has changed nothing for either party.

## ethos-eoc

**Arete.** Tenet 1 by construction — logos and eudaimonia both exist downstream
of it.

**Elleipsis.** *Unconfirmed, and unchanged since 2026-09-02.* The entry then
recorded the worst tenet 2 in the ecosystem by the compiler's own account: no
way to ask *is this one block well-formed against the embedding* short of
compiling the set, with every failure mode arriving late. Two large changes then
merged — `ethos#235`, +6,807/−3,040, *"Major updates to the agility of the eoc
compiler"*, and `ethos#236` — and a change whose stated subject is the agility of
the loop this paragraph grades down is exactly what would overturn it.

**Parainesis.** **Treat this as the least reliable entry on the page.** Settling
it needs somebody reading the compiler rather than its pull request titles, and
nobody has in two weeks. It is a child of a tree that never joined, so nothing
here asks it for anything.

## anoieu

**Arete.** Tenet 2, and it is the part worth copying: one witness file per check
with ethos's verdict recorded from a real run, a committed baseline with
warnings denied, generated documents regenerated and diffed on every push. Tenet
1 is met in the way that counts — **eight repositories other than anoieu run
its checker in their own CI**, each pinned to a commit of its own choosing. It also consumes
what it asks others to consume: `scripts/koine.lock` pins koine at `fc31e8d`,
and the lock file argues its own pin.

**Elleipsis.** The 2026-09-02 edition put anoieu at **poor** on delivery, for
publishing a joining rule no member could satisfy: pin a commit where our CI is
green, when no such commit existed. That band named its own exit — *a pin
exists, or the requirement is withdrawn* — and **eight trees now hold seven
distinct pins**, logos's carrying the comment *only to a commit where anoieu's
own CI is green*, so the exit looks met. *Recorded as a lift on the evidence of
the pins rather than on a re-check of anoieu's CI, which was not run from here.*
What has not moved: **nothing the fuzzer found has been filed upstream**, and
the two ethos reproducers have been committed and ready for weeks.

**Parainesis.** An instruction, and it is the same one as last time. **File the
two ethos findings.** Nothing is blocking them, they are the only thing standing
between this entry and a clean delivery band, and a shortfall that survives
being written down three times is a decision rather than an oversight.

## logos

**Arete.** Exemplary on tenet 5, in the least obvious way: its most valuable
output to anoieu has been three *replies* — one accepted, two declined with
reasons that hold — and a decline with a written reason is worth as much as a
fix, because it is usually a fact about the subject nobody had recorded. It also
caught anoieu being wrong, which is the most useful thing a consumer does.

**Elleipsis.** Tenet 3, unchanged: `install/defs/Cpc.cached.eo` is still a copy
of cvc5's `Cpc.eo` rather than something logos wrote, and it is still there at
the graded commit. The drift check that would close it is an open pull request,
`cvc5#12891`, rather than a running job.

**Parainesis.** An observation: a repository carrying somebody else's ground
truth by copy is not self-contained in the sense the tenet means, and the
ordinary remedy is a manifest and a lock — which its neighbour anoieu now keeps
for koine and could be copied from in an afternoon.

## eudaimonia

**Arete.** The most deliberate adherent on this list. Tenet 1 is its entire
purpose — it exists to make somebody else's compiler reusable and is the
falsification test for that compiler's central claim. Tenet 2 it does properly:
a `--check` mode that installs into a throwaway copy and diffs, and ethos built
alongside so the generated checker's verdicts are cross-checked against an
independent implementation. **It is also where the ecosystem's research
actually landed this stretch** — four child projects started in its tree since
2026-09-02, three of them named by ynoia as work that did not exist.

**Elleipsis.** Tenet 4, by its own account rather than ours:
`docs/limitations.md` says a generated checker **ships compiling, not proven**,
and the core proof, the side conditions, the soundness theorem and the 591
per-rule files are all generated as stubs describing what belongs in them. So
the mechanical pipeline generalizes and the proofs do not, which is the one
claim a reader is most likely to take the other way.

**Parainesis.** An instruction. **Keep saying it as plainly as
`limitations.md` does**, on the front page and not only one level down — this is
the only project on the page whose headline artifact could be mistaken for a
stronger result than it is, and the mistake would be a reader's rather than a
lie.

## dokimasia

**Arete.** Tenet 1 in the cheapest available form: it adopted anoieu's
reporting policy by reference instead of forking a copy, so there is one
position and one place to argue about it. It also passes its policy check, which
it did not a fortnight ago.

**Elleipsis.** *Graded on its pipeline rather than its subject*, because its
subject is cvc5's C++ and no instrument here reads that. One finding is filed —
`docs/findings/tcb-001.md` — and the rest of its register is hypotheses. Its
two child projects are the machinery for closing that gap and neither has
produced an entry yet: `empeiria`'s ledger holds a README and nothing else.

**Parainesis.** An instruction. **Get one empeiria entry into the ledger**, even
a negative one. The distance between a register of hypotheses and a project that
files things is one worked example, and this repository has been described as
the ecosystem's nearest thing to actionable cvc5 bug reports for two weeks
without producing the second one.

## koine

**Arete.** Tenet 1, and this is the entry that changed most since the last
edition. The 2026-09-02 page graded it *fair* on delivery with the elleipsis
*the tool exists and nobody consumes it*. **Both named customers now do**:
anoieu pins it in `scripts/koine.lock` and reaches it through `scripts/koine.py`,
and dokimasia carries the same integration with an entry in its `deps.json`.
Tenet 3 is met in a way worth copying — its front page names its two customers
and refuses to invent features neither has asked for.

**Elleipsis.** It is one script. That is the right size and it is also the whole
of the evidence: a shared implementation with two consumers has not yet shown
whether what is shared generalizes, which is the question a third consumer
answers and nothing else does.

**Parainesis.** An observation: the thing this page asked for last time has been
done, and saying so is most of what a report card is for. What would move the
band again is not more code — it is a third customer, or one of the two saying
what it wishes the interface had been.

## kanon

*A self-assessment. This page lives in kanon's tree and is written by a child
project of it, so nothing in this entry is independent and the discount should
be applied by the reader rather than argued away here.*

**Arete.** Tenet 1: every member's CI runs the policy kanon keeps, and the
register it keeps is the ground truth six repositories resolve each other
through. The 2026-09-15 handoff did the thing the ecosystem had been arguing
for — the rules now sit with a tree that has no stake in the findings, and the
checker stayed with the tool whose mission is checking.

**Elleipsis.** Tenet 2, and it is the finding anoieu carried last time, now
inherited along with the governance. **48 of kanon's 61 commits were made in the
two weeks since 2026-09-02**, almost all of them prose, and the tree shipped no
instrument in that time. Two concrete symptoms found on 2026-09-16: `roles.md`
named a file this repository does not contain, and the documentation index every
member is checked for **did not exist here until somebody ran the checker
against us**. A governance repository that fails its own policy is the sharpest
available form of *documentation about the work is not the work*.

**Parainesis.** An instruction, in the register kanon's own maintenance note
asks for. **Stop adding pages and start deleting them.** One correction pass on
2026-09-16 removed 404 lines from a child project and added 101, and every
deletion was a page describing work that had since been done elsewhere. That
ratio is the measurement, not the cleanup. The next stretch
entry should be able to name one thing outside this tree that behaves
differently because of a page written in it.

## tachyon

**Arete.** Tenet 2, from a standing start. Every one of its 25 commits postdates
the last edition, and its research already runs through a shared
`job_launcher/` against a pinned checkout, so an experiment is reproducible
before it is interesting. `heuresis` has **twelve dated ledger entries between
2026-09-14 and 2026-09-16**, which is the fastest accumulation of dated evidence
anywhere in the ecosystem.

**Elleipsis.** Tenet 1. Nothing outside tachyon behaves differently yet, and by
design: its own charter says a human may be inspired to pursue a finding *at
their discretion*, with no required handoff. That is an honest boundary and it
is also the reason the delivery band is *fair* and not higher. Its second child,
`metagraphe`, has a ledger holding only a README.

**Parainesis.** An instruction. **Carry one diamond out of the tree.** The
charter is right that discovery is a result whether or not anybody pursues it,
but a ledger nobody outside has read cannot distinguish that position from
having found nothing worth carrying — and one entry reaching cvc5, or even
reaching dokimasia, settles which it is.

## eschaton

**Arete.** Tenet 3, and it is the best front page in the ecosystem for the
narrow reason that it refuses to oversell: one directory per bet, an explicit
statement that **there is no solver to run yet**, and a warning that the
directory named `cvc6` is a working title for a bet rather than a pitch to
anybody. A repository two weeks old that tells you what it has not done is doing
tenet 3 better than several older ones.

**Elleipsis.** Tenet 4, by its own admission: *no claim on these pages has been
tested by running it*. Two of its three bets are a page each. This is a
repository of positions, and positions are the cheapest thing an agent
produces — which is exactly the failure mode the tenet exists to name.

**Parainesis.** An instruction. **Run the T2 experiment its own README names as
the preferred next step.** It is the one thing that would turn the most
promising bet from an argument into a measurement, and until something here is
run, the legibility band is measuring the quality of the prose.

## epikrisis

**Arete.** Tenet 5, and it is the only instrument of its kind here: the
ecosystem's sole source of history analysis, with **six dated runs against
anoieu** and two against the ecosystem as a whole, each built to be re-derived
rather than believed. Its promotion out of eudaimonia into a repository of its
own, completed this stretch, put it where a tool three repositories rely on
should have been.

**Elleipsis.** Tenet 5 again, from the other side. `LAW 4` made the per-tool
commit census epikrisis's work and **forbade the president from producing it**,
and no such report existed. kanon's `D3` had been open since 2026-09-02 asking
whether epikrisis accepts a responsibility it may never have been told about,
and **it was still open on 2026-09-16**. A responsibility assigned in a document
the holder has not answered is not held by anybody.

> **Both halves of that moved after this round was graded, in opposite
> directions, and the paragraph above is left standing rather than rewritten.**
>
> **epikrisis answered on 2026-09-17, and the answer is yes** — `epikrisis-D4`,
> given as a person's decision. Eight dated runs exist, six against anoieu and
> two against the ecosystem. It also named two things to hold against it: the
> subject list has fallen behind the register, so **a census run today reads
> seven of the ten repositories held to the policy** and would report a total as
> though it covered the ecosystem; and the newest run was dated 2026-09-02.
>
> **And the law stopped asking.** kanon's `laws.md` now lists the commit census
> under *what these laws do not settle*: nothing requires per-tool commit
> counts for a stretch, or a measure of how much work an agent generated.
> **So the duty this paragraph graded a tool against is conferred on nobody**,
> and epikrisis says accepting it is therefore an offer rather than a
> compliance.
>
> **Which makes the elleipsis above a grade against a document rather than
> against a tree, and that is the part worth keeping.** Read on 2026-09-18.

**Parainesis.** *Discharged 2026-09-17.* It was one sentence — **answer `D3`,
either way** — and the answer came. **What replaces it is narrower and is not an
instruction to epikrisis:** the second figure `LAW 4` used to ask for, how many
commits are believed AI-generated, **is not measurable by anybody**, because a
trailer is opt-in and so the floor is zero with no ceiling. epikrisis says it
will report it as not measurable with the disclosure count beside it, every
time. **That is the right answer and this page should quote it rather than
grade it.** The remaining unbuilt thing is a census whose denominator matches
the register, and its blocker is a subject list, not a decision.

## stathmos

*The tool that writes this page, graded here because a page whose author is
exempt has no check on it at all. Its own README committed to this: **the round
after it has done work, it is graded like everything else, in the sharper
register, and it does not get to grade itself favourably for having been
careful about this.***

**Arete.** It exists and it produced this, which is more than the entry it
replaced could say — the 2026-09-02 edition recorded it as a stub holding a
role and having assembled nothing. Splitting the page from the tool that used
to write it is the one structural improvement in this edition, and it was the
project's stated reason for existing before it had anything to show.

**Elleipsis.** Tenet 2, and it is specific. **Its `evidence.md` is dated
2026-09-02 and this edition did not come from it** — every number above was
re-derived from the trees at grading time, which means the file that is supposed
to hold the re-derivable half is now older than the judgements resting on it.
A project whose whole claim is *the evidence is separable from the verdict* has
shipped a verdict its own evidence file does not support.

**Parainesis.** An instruction. **Regenerate `evidence.md` from this round, or
delete it.** Two artifacts that are meant to be the two halves of one judgement,
fourteen days apart, are worse than one — and if the page can be written without
the evidence file, that is a finding about the file rather than about the round.

---

## How to get a paragraph changed

**Say that it is wrong.** There is no process, no id and no ledger, because none
of this is a finding.

**The rows most likely to be wrong are the ones with no checkout behind them** —
`cvc5`, which was not cloned, and `ethos-eoc`, which nobody has re-read since two
large changes landed. The rows least likely to be wrong are the ones naming a
file and a line, and those have usually already been carried properly, as
findings, through a process this page is not.

**If a paragraph is in the wrong register, the fix is upstream.** The register
follows the maintenance note in your README, so changing that changes this.
