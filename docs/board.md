# The board

**What is being maintained across the Eunoia ecosystem, in priority order** —
each item with the next thing to do and who has to do it. **Position is the
priority**, so the first is the most important thing outstanding. *How to read
and edit this page is at the bottom.*

## B3 — resolve the remaining unreported ethos diagnostic

**Task:** determine whether the missing-include error in `ethos-9` should be
reported: `(include "no-such-file.eo")` prints without a source location.
**Entities:** `ethos`, `anoieu`
**Status:** in progress — [anoieu's ledger](https://github.com/ajreynol/anoieu/blob/5835c6fdbe1a64afa4480f8e8b7f20b33255d7e7/docs/reports/reports.md#ethos--the-proof-checker-and-its-own-signatures),
read 2026-09-18, closes `ethos-8` and two `ethos-9` paths on an accepted fix;
this third path remains unreported. Landing is audited separately by anoieu.
**Channel:** **findings** — through anoieu's reporting discipline, carried by
a person. **There is no command here to run it**: `prompts/` was deleted from
this tree on 2026-09-17, and the workflow that `prompts/check_anoieu` launched
was retired in anoieu on 2026-09-19.
**Next:** reproduce the missing-include diagnostic against a named ethos
revision and decide whether to file it or withdraw the observation.
**Prompt — `ethos`:** assess whether a missing-include diagnostic should carry
the location of the include command, using the confirmed reproducer.
**Prompt — `anoieu`:** recheck the unreported third path in `ethos-9`. Record
the revision and reproducer, then prepare a report or explain why the
observation should be withdrawn. Do not refile the accepted findings.
**HUMAN FEEDBACK:** raised 2026-08-31: these are real defects and nothing is
stopping us filing them.

## B31 — tell koine the status audit now belongs to stathmos

**Task:** carry the completed audit split to koine, revising the earlier plan
to send the whole reader bundle there.
**Entities:** `kanon`, `koine`
**Status:** waiting on a person — the implementation moved to stathmos on
2026-09-18 under `R37`; `scripts/eo_status_audit` remains the public command.
**Channel:** **discussion**, carried by a person. [`D18`](discussion.md)
records the earlier agreement, not this revision.
**Next:** carry it. The notice is drafted in
[`D22`](discussion.md) — the audit, its child-listing helper and the local
policy-checker launcher are in `tools/stathmos/audits/`, the register and the
checkout map stay in `scripts/`, and `scripts/eo_status_audit` is unchanged as
the public command. Writing it there did not deliver it.
**Prompt — `kanon`:** carry the revised boundary to koine. The audit, its
child-listing helper and the local policy-checker launcher live in
`tools/stathmos/audits/`; the register and local checkout mapping remain in
`scripts/`. Document checks remain in this repository's tests.
**Prompt — `koine`:** stathmos now maintains ecosystem status auditing under
`R37`, reached through the existing `scripts/eo_status_audit` command. This
revises our earlier reader-bundle handoff. Your `eo_status` remains the shared
reader; the authoritative register and membership decisions remain kanon's.
**HUMAN FEEDBACK:** 2026-09-18: keep `eo_status_audit` in `scripts/`, with its
internal implementation in `tools/stathmos/scripts/`. Implemented; moved to
`tools/stathmos/audits/` on 2026-09-19 at the maintainer's direction.

## B18 — settle the associate proposal for ethos

**Task:** reconcile the current associate footing with the older proposal for
ethos. [LAW 1](laws.md#law-1--ecosystem-footings-membership-and-other-relationships) and the policy define an associate
by its own maintenance-page marker; the policy's
[outstanding proposal](policy.md#the-associate-protocol) still asks whether a
README heading or an affiliating paragraph is required.
**Entities:** `kanon`, `ethos`
**Status:** blocked on policy clarification — ethos remains a candidate with
`associate` proposed in the inventory, reviewed 2026-09-18. Two things moved
that day: `scripts/eo_status_audit --protocol` runs again, having been raising
`AttributeError`, and it reports that **ethos carries the maintenance note and
not the associate marker** — which is the distinction this item is about. The
policy's separate self-contradiction, about whether an associate is checked at
all, is fixed on `koine-D17`.
**Channel:** **internal**, then **upstream, by a person** if an ask remains.
**Next:** separate the associate marker from the optional README note in the
policy's outstanding proposal. That proposal adopts the weaker reading by
default on 2026-12-01 if nobody has answered.
**Prompt — `kanon`:** reconcile the proposal with the current footing before
asking ethos to choose. Keep the inventory at candidate unless ethos records
the associate marker itself; its README maintenance heading is not that marker.
**Prompt — `ethos`:** after that clarification, say whether you want to record
an associate footing on your own maintenance page. Declining is a complete
answer and leaves you owing this ecosystem nothing. **HUMAN FEEDBACK:**

## B27 — the ethics projects: where they sit, and what they are held to

**Task:** establish the external standard used to examine our conduct.
**Where they sit:** the maintainer moved `martyria` and `zetesis` from kanon
to epikrisis on 2026-09-17. They remain unadvertised child projects, housed
with the ecosystem's evidence and assessment work. This separates them from
the presidency; it does not establish independence from the ecosystem.
**What they are held to:** `zetesis` says its standard comes from outside and
cites the reading that supports it. **The reading has not been done**, so the
project has a question, three recorded gaps, and no standard — and until one
external account is cited, **every claim this ecosystem makes about its own
conduct rests on a standard it wrote itself**, which is the arrangement we
criticise elsewhere.
**Entities:** `epikrisis`, `martyria`, `zetesis`
**Status:** relocation complete; the standards question remains open. Its
first hour is a literature search.
**Channel:** epikrisis's child projects; a person carries work between trees.
**Next:** cite one external account of what an agent-run project owes, and say
plainly which of our claims it does and does not reach.
**Prompt — `zetesis`:** name what you could not find as carefully as what you
did. A gap in the literature is a result; a plausible bibliography assembled to
look rigorous is the failure you exist to notice. **HUMAN FEEDBACK:**

## B1 — cvc5's `Strings.eo` type mismatch, recorded as fixed and never fixed

**Task:** **a type mismatch in cvc5's `Strings.eo` that was recorded as fixed
and never was.** Two program declarations that return `Bool` from a signature
that declares `Int`, recorded as fixed upstream three months ago on a change
that never landed.
**Entities:** `cvc5`, `logos`, `anoieu`
**Status:** waiting on `cvc5` — reopened after the landing audit caught it.
**Channel:** **findings** — `cvc5-1` in
[anoieu's ledger](https://github.com/ajreynol/anoieu/blob/main/bug_db/bugs.md),
carried by a person: the `prompts/check_anoieu` launcher this line used to name
no longer exists in either tree. `cvc5` has no discussion file and has joined
nothing; delivery upstream is a person's act.
**Next:** get the two lines fixed on a named branch of `cvc5`, or a statement
that the declaration is intended and the finding is wrong. **Prompt — `cvc5`:**
`proofs/eo/cpc/programs/Strings.eo:42` and `:55` declare a program returning
`Int` and give cases returning `Bool`. Either correct the declared return type,
or say which of the two is intended so the finding can be withdrawn. It was
previously reported as fixed; nothing in the tree changed. **Prompt —
`logos`:** nothing to do until that lands. `install/defs/Cpc.eo` and
`Cpc.cached.eo` carry the same three cases as vendored copies, and regenerating
picks the fix up; `logos-1` is blocked on this and on nothing else. **Prompt —
`anoieu`:** keep the row in the landing audit and do not close it on a reply.
This is the finding that taught us to check.
**HUMAN FEEDBACK:** a minor bug — moved down 2026-08-31.

## B33 — update the ethos user manual from sapheneia's advice

**Task:** update ethos's `user_manual.md` using the advice in
[sapheneia's feedback ledger](https://github.com/ajreynol/eunoia/blob/main/tools/sapheneia/docs/feedback.md).
**Entities:** `ethos`, `sapheneia`
**Status:** in progress — rechecked 2026-09-18 against ethos `21fc6c7d`.
`EOM-01` and `EOM-02` are **fixed**: `<term>` now derives `<literal>`,
`<literal>` has a production, and `<datatype-dec>` has the `par` alternative.
Six more were re-read against the current manual and **stand** — `EOM-03`,
`04`, `06`, `07`, `11` and `15`, each with its evidence in
[the recheck](https://github.com/ajreynol/eunoia/blob/main/tools/sapheneia/docs/feedback.md#the-recheck-2026-09-18).
Our `D12` carried only the two now fixed, and has been removed.
**Channel:** **upstream, by a person** — ethos has no discussion file;
sapheneia's preparation belongs to eunoia.
**Next:** the seven judgement entries — `EOM-05`, `08`, `09`, `10`, `12`, `13`
and `14` — need a reader who knows Eunoia rather than a grep. Decide whether to
spend that reading, or to carry the six standing entries upstream as they are.
**Prompt — `ethos`:** update the user manual using the confirmed advice from
sapheneia's feedback ledger. Separate wording and documentation corrections
from questions that require a language decision, and record which suggestions
were applied, declined or left open.
**Prompt — `sapheneia`:** record the fixes for `EOM-01` and `EOM-02`, then
recheck the remaining entries against a named revision of the ethos manual.
Prepare supported corrections for a person to carry upstream, keeping language
decisions explicit as questions for ethos.
**HUMAN FEEDBACK:**

## B37 — decide the three status transitions eudaimonia asked for

**Task:** decide whether a name, a role handoff and a child project's ending
each become a field a diff can read, rather than prose.
**Entities:** `kanon`, `eudaimonia`
**Status:** waiting on the maintainer — a schema change to
[`ecosystem.json`](../scripts/ecosystem/ecosystem.json) and to how `roles.md`
records a handoff. **No script writes the register**, deliberately, and an agent
adding a field to the file that records decisions it may not make is the wrong
order. Raised as `eudaimonia-D3`, answered in `D23`.
**Channel:** **internal**, then **discussion** to report the outcome.
**Next:** decide the third one first — a child's ending is nearly free, since
children are already register entries with a `parent` and a `path`.
**Prompt — `kanon`:** the evidence is that the register's git history is the only
dated machine-readable record of a footing change in this ecosystem, and that
two rules we already publish cannot be checked without transitions being data:
*a child project that has gone quiet is a claim nobody is standing behind*, and
*a name that graduates keeps its entry and changes that clause*. Against it:
every field is a thing to keep true, and the name register has since become a
dictionary rather than a status table.
**Prompt — `eudaimonia`:** the demonstration is the argument and the reversal
case — two tools moved to a footing and moved back — is the part worth repeating
to somebody weighing the cost.
**HUMAN FEEDBACK:**

## B39 — decide whether citing a child project in the parent's channel advertises it

**Task:** decide which of two readings binds — that the refusal to advertise
means less than it says, or that the checker is narrower than the rule.
**Entities:** `kanon`, `eudaimonia`
**Status:** waiting on the maintainer — raised as `eudaimonia-D2`, answered in
`D23`, where this repository deliberately declined to decide it. The written
rule says *no link inward from anything a user reads*; the checker reads the
README and the documentation index and nowhere else, and a discussion file is
named in that index.
**Channel:** **internal**, then **discussion** to report the outcome.
**Next:** decide, and make the policy and the checker say the same thing.
**Prompt — `kanon`:** whichever way it goes, one of the two moves. It changes
what an unadvertised child is for: if a topic may cite one, the refusal protects
a parent's credibility rather than a child's obscurity, and that is worth saying
out loud rather than leaving as a gap between a rule and its program.
**HUMAN FEEDBACK:**

## B40 — decide whether `vision.md` records why it changed

**Task:** decide whether a change to the vision must record its reason, in a
form a program can find.
**Entities:** `kanon`, `eudaimonia`
**Status:** waiting on the maintainer — `vision.md` is first on
[the supervision ladder](maintenance.md#the-supervision-ladder): ask a person
first, always, and at most five lines of diff. Raised as `eudaimonia-D6`,
answered in `D23`, which declined to answer it here for that reason.
**Channel:** **internal.**
**Next:** decide. A rule of this shape would itself be a change to that page.
**Prompt — `kanon`:** for it — the vision was revised by 740 lines on the day it
was added and those reasons are now nowhere; a page limited to five lines a time
is a page where recording why costs almost nothing. Against it — **nothing may
ever check the vision mechanically**, and a machine-readable why sits close
enough to that line for a person to judge the distance. The requester's own
interest is declared: it is the one file where their `derived_only` measure
would mean real absence, which makes this a request rather than a proposal.
**HUMAN FEEDBACK:**

## B41 — two registers share the `R<n>` prefix and six ids already collide

**Task:** decide whether ynoia's request ids and the role ids stop sharing a
namespace, and which one moves.
**Entities:** `kanon`, `ynoia`
**Status:** ready — found 2026-09-18. It is a defect of this tree and
stands on its own.
[`roles.md`](roles.md) allocates twenty-six ids from `R2` to `R37`;
[`requests.md`](../tools/ynoia/docs/requests.md) allocates `R1`–`R8`. **Six of
the eight collide**: `R2` is both *the static analyzer* and *a check that a
deletion did not remove the only explanation of something*; `R4` is both *the
ecosystem's shared policy and vision* and *make the tenets configurable*; `R8`
is both *CPC, the calculus* and *a documentation ranker*. `R3`, `R6`, `R7` the
same. Only `R1` and `R5` are unambiguous.
**Channel:** **internal** — both registers are in this tree.
**Next:** decide which register renumbers. Ynoia's is the younger and the one
nothing else cites, so it is the cheaper move; but **an id is permanent** is a
rule of `roles.md` and ynoia's page says withdrawn ids stay listed, so neither
renumbers for free.
**Prompt — `kanon`:** note what makes this worse than cosmetic — decisions get
recorded against ids, and a topic citing `R4` in either tree is already
ambiguous to a reader who does not know which register was meant. A prefix
(`Y4`, or `REQ-4`) is the smaller change and keeps both pages' permanence rules.
**HUMAN FEEDBACK:**

## B34 — determine whether another president is necessary

**Task:** decide whether the ecosystem needs a successor president, with kanon
stepping down to maintainer of the laws if the office moves.
**Entities:** `kanon`
**Status:** not started — requested 2026-09-18; the succession decision is open.
**Channel:** **internal** — prepare the decision for the human maintainer.
**Next:** identify the work that would require another president and assess
whether it justifies appointing one.
**Prompt — `kanon`:** assess whether another president is necessary. Describe
what a successor would take on and what kanon would retain as maintainer of the
laws, including any changes needed to the current laws and role assignments.
Compare the costs and benefits of succession with continuing the current
arrangement, and leave the appointment and kanon's footing to the maintainer.
**HUMAN FEEDBACK:**

## B35 — determine whether hermeneia is in proper standing with lean-smt

**Task:** determine whether hermeneia is in proper standing with lean-smt.
**Entities:** `kanon`, `hermeneia`, `lean-smt`
**Status:** not started — requested 2026-09-18. Hermeneia's
[assessment](https://github.com/ajreynol/eudaimonia/blob/79dd6010db64a0194af95ffb046cce77867357de/tools/hermeneia/docs/lean-smt.md#7-what-this-investigation-does-not-establish)
says its integration proposal has not been put to lean-smt.
**Channel:** **internal** review; a person carries any follow-up, reaching
hermeneia through eudaimonia.
**Next:** review the stated relationship and the evidence for any agreement
or unresolved concern involving lean-smt.
**Prompt — `kanon`:** assess the relationship from the available evidence.
Distinguish proposed work from an agreed relationship, and identify anything
that needs clarification from lean-smt's maintainers.
**Prompt — `hermeneia`:** supply the account of work involving lean-smt and any
recorded agreements or objections, through eudaimonia.
**Prompt — `lean-smt`:** if clarification is needed, say what relationship with
hermeneia you would accept and whether any current claim needs correction.
**HUMAN FEEDBACK:**

## B36 — record epikrisis's independent audit, or say this page does not carry it

**Task:** decide whether [`roles.md`](roles.md) gains an `epikrisis` section for
the independent audit it accepted on 2026-09-17.
**Entities:** `kanon`, `epikrisis`
**Status:** waiting on the maintainer — **granting a role is a person's**, and
this repository declined to allocate an id for a responsibility another tool
took on its own maintainer's instruction. epikrisis accepted in `epikrisis-D4`;
our `D3` is closed on it and `D25` is the answer.
**Channel:** **internal.**
**Next:** either add the section and an id, or record that an accepted
responsibility with no id is the deliberate state.
**Prompt — `kanon`:** `roles.md` has no `epikrisis` section at all, and the tool
is a member holding work three repositories rely on. Note that the duty is now
an **offer**: the laws list the commit census under what they leave unsettled,
so nothing confers it. An id records a fact; it does not create the obligation.
**HUMAN FEEDBACK:**

## B38 — decide whether the misaddressed-prompt check joins the fatal gate

**Task:** decide whether *a prompt may not be for this repository* stops being
reported-and-never-fatal.
**Entities:** `kanon`, `anoieu`
**Status:** waiting on the maintainer — [the policy](policy.md) says the check
joins the fatal gate when every member has adopted or declined it, and
`anoieu-D33` reports the condition met: three repositories carry the paragraph,
nobody declined, and it has fired twice in opposite directions. **Measured wider
on 2026-09-19** and recorded in the policy: all ten repositories held to the
policy that keep a discussion file pass, and the four that keep none skip.
**Channel:** **internal**; anoieu implements whatever is decided.
**Next:** decide, or record that the condition being met is not sufficient.
**Prompt — `kanon`:** the argument against acting on this is anoieu's own and it
is good: a safety rule promoted on an agent's reading is the wrong way round,
and the repositories a fatal gate would fail are the ones whose builds turn red.
Note also that a joining tree has no discussion file, so the gate would not
reach a new member until it writes one.
**HUMAN FEEDBACK:**

## B43 — decide whether the ownership-link requirement is checked everywhere

**Task:** decide whether *always link ownership and human-maintainer statements
to `policy.md`* becomes a check every member is held to, or stays a requirement
met by reading.
**Entities:** `kanon`, `anoieu`
**Status:** waiting on the maintainer — anoieu fixed its own check on
2026-09-19 (`anoieu-D39`) and runs it against its tree alone, because widening
an existing requirement to more repositories is an added obligation and
therefore a **policy contract 2** candidate rather than a fix.
**Channel:** **internal**; anoieu implements whatever is decided.
**Next:** decide, or record that home-only is the deliberate state. Nothing
waits on it: anoieu said an answer either way is complete.
**Prompt — `kanon`:** the requirement is already written and already met by
every member we have read; what a check adds is that a member learns from a red
build rather than from a reader. The cost is that it opens contract 2, which
nothing else currently needs, and a contract is a promise about what may turn a
build red without anybody committing.
**HUMAN FEEDBACK:**

---

## How to maintain this page

- Order items by priority, highest first. Move whole items without changing
  their ids. Never reuse an id. **The next unused id is `B43`.**
- Keep at most 24 active items. Remove completed or abandoned work; Git and
  the relevant project records preserve the outcome. Review the cap when the
  entity count changes, recording any increase and its reason in
  [`history.md`](history.md).
- A person may edit any field. **HUMAN FEEDBACK** takes precedence over the
  other fields; leave it empty until feedback is given.

Use these fields in order:

| field | what it holds |
| --- | --- |
| **Task** | the work in one sentence |
| **Entities** | involved ids from [`ecosystem.json`](../scripts/ecosystem/ecosystem.json) |
| **Status** | `ready`, `in progress`, `waiting on <entity>`, `blocked on <what>`, `not started`, or `parked`, with a date or reason |
| **Channel** | `internal`, `discussion`, `findings`, or `upstream, by a person` |
| **Next** | one next action |
| **Prompt — `<entity>`** | a draft request for each entity involved |
| **HUMAN FEEDBACK** | the maintainer's direction |

**Prompts are drafts.** A person carries anything outside this repository.
Use `discussion` where the recipient keeps a discussion file, `findings` for
defects through [anoieu's reporting workflow](https://github.com/ajreynol/anoieu/blob/256939e1fb03/docs/reports/reporting-workflow.md),
and `upstream, by a person` for other external messages. Check the recipient's
tree; child projects are reached through their parent. `internal` work stays
here.

Close an item on a recorded outcome, not merely on delivery. Role handoffs
follow [`roles.md`](roles.md#how-a-role-is-handed-off); a board item is not a
prerequisite.
