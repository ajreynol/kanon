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
**Channel:** **findings** — through `prompts/check_anoieu ethos`, carried by
a person.
**Next:** reproduce the missing-include diagnostic against a named ethos
revision and decide whether to file it or withdraw the observation.
**Prompt — `ethos`:** assess whether a missing-include diagnostic should carry
the location of the include command, using the confirmed reproducer.
**Prompt — `anoieu`:** recheck the unreported third path in `ethos-9`. Record
the revision and reproducer, then prepare a report or explain why the
observation should be withdrawn. Do not refile the accepted findings.
**HUMAN FEEDBACK:** raised 2026-08-31: these are real defects and nothing is
stopping us filing them.

## B26 — add kanon's front-page FAQ

**Task:** give kanon short, settled answers to its recurring questions.
[`policy.md`](policy.md#common-questions-on-the-front-page) recommends the
answer — a `## Common questions` section on the front page.
**Entities:** `kanon`
**Status:** open on our own side first. **Nothing may be proposed to anybody
until kanon carries one.**
**Channel:** **local**, then a ball each.
**Next:** write kanon's, then propose the section to one other tool. **Prompt —
`kanon`:** proposing a style you have not adopted is the error this office
exists to avoid. **HUMAN FEEDBACK:**

## B31 — tell koine the status audit now belongs to stathmos

**Task:** carry the completed audit split to koine, revising the earlier plan
to send the whole reader bundle there.
**Entities:** `kanon`, `koine`
**Status:** waiting on a person — the implementation moved to stathmos on
2026-09-18 under `R37`; `scripts/eo_status_audit` remains the public command.
**Channel:** **discussion**, carried by a person. [`D18`](discussion.md)
records the earlier agreement, not this revision.
**Next:** tell koine which responsibilities and paths now belong to stathmos.
**Prompt — `kanon`:** carry the revised boundary to koine. The audit, its
child-listing helper and the local policy-checker launcher live in
`tools/stathmos/scripts/`; the register and local checkout mapping remain in
`scripts/`. Document checks remain in this repository's tests.
**Prompt — `koine`:** stathmos now maintains ecosystem status auditing under
`R37`, reached through the existing `scripts/eo_status_audit` command. This
revises our earlier reader-bundle handoff. Your `eo_status` remains the shared
reader; the authoritative register and membership decisions remain kanon's.
**HUMAN FEEDBACK:** 2026-09-18: keep `eo_status_audit` in `scripts/`, with its
internal implementation in `tools/stathmos/scripts/`. Implemented.

## B18 — settle the associate proposal for ethos

**Task:** reconcile the current associate footing with the older proposal for
ethos. [LAW 1](laws.md#law-1--ecosystem-footings-membership-and-other-relationships) and the policy define an associate
by its own maintenance-page marker; the policy's
[outstanding proposal](policy.md#the-associate-protocol) still asks whether a
README heading or an affiliating paragraph is required.
**Entities:** `kanon`, `ethos`
**Status:** blocked on policy clarification — ethos remains a candidate with
`associate` proposed in the inventory, reviewed 2026-09-18.
**Channel:** **internal**, then **upstream, by a person** if an ask remains.
**Next:** separate the associate marker from the optional README note in the
policy's outstanding proposal.
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
**Channel:** **findings** — `cvc5-1` in the ledger, carried by
`prompts/check_anoieu cvc5`. `cvc5` has no discussion file and has joined
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
[sapheneia's feedback ledger](../tools/sapheneia/docs/feedback.md).
**Entities:** `ethos`, `sapheneia`
**Status:** in progress — checked 2026-09-18 against ethos `21fc6c7d`;
`EOM-01` and `EOM-02` are addressed by the grammar changes in
[`72a0c162`](https://github.com/cvc5/ethos/commit/72a0c162c80fab55986932c3976f4bd28fd9847c).
**Channel:** **upstream, by a person** — ethos has no discussion file;
sapheneia's preparation is internal to kanon.
**Next:** recheck `EOM-03` through `EOM-15` against the current ethos manual
and identify which still need a change.
**Prompt — `ethos`:** update the user manual using the confirmed advice from
sapheneia's feedback ledger. Separate wording and documentation corrections
from questions that require a language decision, and record which suggestions
were applied, declined or left open.
**Prompt — `sapheneia`:** record the fixes for `EOM-01` and `EOM-02`, then
recheck the remaining entries against a named revision of the ethos manual.
Prepare supported corrections for a person to carry upstream, keeping language
decisions explicit as questions for ethos.
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

---

## How to maintain this page

**Position is the priority.** The first item is the most important thing
outstanding; the last is the least. Reordering is done by moving a block, and
that is the main way a person changes what this page says.

**The id is stable.** `B6` stays `B6` when it moves, so ids appear out of order
and that is correct rather than a mistake to tidy. A row that leaves is not
reused. **The next unused id is `B36`**, including after completed items are
removed; their earlier contents remain in git history.

**Twenty-four is a cap, not a target.** Adding a twenty-fifth means deciding
which one leaves, which is the whole value of the number. An item that is done,
or that nobody will act on, is deleted rather than archived — the record of
what happened lives in
[`reports/reports.md`](https://github.com/ajreynol/anoieu/blob/main/docs/reports/reports.md)
and in git, and a board that keeps its dead is a board nobody reads to the
bottom of.

**Raising the cap needs a reason on the page.** A cap that never moves stops
measuring priority and starts measuring how many repositories exist, so the
number is set at roughly two items per entity — and **it is reviewed when the
entity count changes, never when the board is full.** The second is how a cap
gets raised by whatever happens to want adding, which is the failure the number
exists to prevent. Every raise is recorded here, with its date, like this one.

**Every field is a person's to overwrite.** `HUMAN FEEDBACK` is the one that
outranks everything else on its item: whatever it says wins over the status,
the prompt, and the position, and anything that ever reads this file is to
treat it that way. It is left empty rather than filled with a placeholder,
because an empty field is visibly unanswered.

Each item carries the same fields, in the same order:

| field | what it holds |
| --- | --- |
| **Task** | one line: what is being maintained, not how |
| **Entities** | the repositories and child projects involved, using only ids from [`ecosystem.json`](../scripts/ecosystem/ecosystem.json) |
| **Status** | `ready`, `in progress`, `waiting on <entity>`, `blocked on <what>`, `not started`, or `parked` — plus one clause saying since when or on what |
| **Channel** | how the prompts below reach the entities they name: `discussion`, `findings`, `upstream, by a person`, or `internal`. The section after this one is what each means |
| **Next** | the single next issue to fix. One thing, not a plan |
| **Prompt — `<entity>`** | one per entity involved: what that repository would be asked to do, written so it can be handed over as it stands |
| **HUMAN FEEDBACK** | empty, for a person |

**A prompt here has not been sent.** Writing one down is drafting it;
delivering it is the next section, and a person's act either way.

## How a prompt is delivered

**A prompt on this page is not sent by being written here.** It reaches the
repository it names through the channel that repository actually has, and the
**Channel** field says which. There are three, and the difference between them
is not a formality:

| channel | what it means | who acts |
| --- | --- | --- |
| **discussion** | a topic in [`discussion.md`](discussion.md) addressed to them, or a reply into a topic of theirs — the standing channel for anything that is **not** a defect report | a person carries it; koine's installed `eo_respond` reads theirs, and nothing here writes into anybody else's file |
| **findings** | a row in the ledger, carried by `prompts/check_anoieu <id>` and answered through `prompts/process_anoieu` | the same person, through the reporting workflow, which is a separate protocol on purpose |
| **upstream, by a person** | a message, an issue or a pull request in a tree that has no discussion file | a person, entirely — no script here has a way to do it, and none should |

**Not everybody has a discussion file, and a member need not.** `anoieu`,
`eudaimonia`, `dokimasia` and `koine` have one; `ethos`, `logos` and `cvc5`
have none, and a child project has none of its own and is reached through its
parent. Every repository with one today is a member, which is a fact about who
has bothered rather than a rule — the policy [does not require
one](policy.md#the-discussion-file) of anybody, so a member with no file is
possible and the third row is what reaches it. Writing `discussion` against a
repository that keeps none would be describing a channel that does not exist.
That is the shape this page adds to the protocol: the queue is here, the wire
is the discussion file, and where there is no wire the page says so instead of
pretending.

**So check the tree rather than the footing.** The question a row answers is
*does this repository have a file to write into*, and reading it off `member`
would have been a shortcut even while it happened to work.

**The board does not replace either protocol, and does not shortcut them.**
Nothing is filed by being on this page, a prompt here is a draft rather than a
message, and a row is not closed by sending — it closes when the artifact it
names says what happened, which is the rule the findings ledger already keeps.

## A handoff of a role is an ordinary item here

[`roles.md`](roles.md) keeps what each tool is accountable for, and moving one
of those to another tool is proposed on this page like anything else: the
entities are the holder losing it, the tool gaining it where the inventory has
an id for it, and every consumer whose pin moves. The channel is
**discussion**, because the point of writing it here is to be disagreed with by
the repositories it costs something, and there is one prompt per entity so that
each has been asked rather than told.

The procedure is three things, in
[`roles.md`](roles.md#how-a-role-is-handed-off), and `B15` is the worked example
— transferred, with policy/checker version coordination still open. **None of it
gates anything**, and a handoff that never appeared on this page is still a
handoff.

---
