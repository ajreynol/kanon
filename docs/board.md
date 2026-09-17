# The board

**What is being maintained across the Eunoia ecosystem, in priority order** —
each item with the next thing to do and who has to do it. **Position is the
priority**, so the first is the most important thing outstanding. *How to read
and edit this page is at the bottom.*

## B3 — the fuzzer has found real defects and filed none of them

**Task:** **two crashes the fuzzer found in ethos and nobody has filed.** An
uncaught C++ abort on a one-line signature, and error paths that print outside
ethos's own `Error: <file>:<line>` convention. Six reproducers are committed
here; nothing has been sent upstream.
**Entities:** `ethos`, `anoieu`
**Status:** ready — the reproducers exist and are committed under
`tests/fuzz/`.
**Channel:** **findings** — `ethos-8` and `ethos-9`, through
`prompts/check_anoieu ethos`, because a defect report is not a discussion
topic.
**Next:** file the two, with their reproducers, through the ordinary loop.
**Prompt — `ethos`:** `(declare-const f (->))` aborts with an uncaught
`std::length_error` rather than reporting a bad type. Separately, three error
paths exit without a file or line, which breaks the convention every other
error in the binary follows. Reproducers are committed and fetchable raw.
**Prompt — `anoieu`:** run `prompts/check_anoieu ethos` for these two rows, and
say plainly in the report that the fuzzer produced them — a provoked crash and
a read signature are different claims and the codes already say which.
**HUMAN FEEDBACK:** raised 2026-08-31: these are real defects and nothing is
stopping us filing them.

## B26 — no node has a front-page FAQ, and kanon does not either

**Task:** joining cost koine eighteen hundred lines of reading, and nowhere
does a tool say the short version of itself.
[`policy.md`](policy.md#common-questions-on-the-front-page) recommends the
answer — a `## Common questions` section on the front page.
**Entities:** `kanon`
**Status:** open on our own side first. **Nothing may be proposed to anybody
until kanon carries one.**
**Channel:** **local**, then a ball each.
**Next:** write kanon's, then propose the section to one other tool. **Prompt —
`kanon`:** proposing a style you have not adopted is the error this office
exists to avoid. **HUMAN FEEDBACK:**

## B18 — the associate protocol remains open for ethos

**Task:** `associate` is defined and proposed for ethos, but what a repository
has to carry was never decided. [Anoieu's
`D11`](https://github.com/ajreynol/anoieu/blob/main/docs/discussion.md#d11--we-have-a-footing-for-you-and-no-protocol-to-put-you-in-it).
**Entities:** `kanon`, `ethos`
**Status:** waiting on `ethos` — the choice between the two versions of the
protocol is theirs to answer before it is ours to fix.
**Channel:** **upstream, by a person** — ethos has no discussion file, so the
question is carried by hand.
**Next:** decide the one open question — the bare maintenance-note heading, or
that plus the paragraph naming this ecosystem — and write it into
[`policy.md`](policy.md) as in force. **logos is a member**, so its associate
proposal is superseded and it is not a party we are waiting on for this item.
**Prompt — `kanon`:** do not record ethos as an associate until the protocol is
decided; `proposed:` is the field that holds the intention, and
`scripts/eo_status_audit --protocol` is the report. When it is decided, the section
in `policy.md` stops saying *drafted, and not in force* and the ethos entry
moves in one commit. **Prompt — `ethos`:** we would like to record you as an
associate: a footing that obliges you to nothing, runs nothing in your CI, and
says that every other reading of the language is measured against your
checker's behaviour. The only thing it would ask is a `How this repository is
maintained` heading. Which would you rather be asked for — that alone, or that
plus a paragraph saying you are not held to our policy? Neither is also an
answer. **HUMAN FEEDBACK:**

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

---

## How to maintain this page

**Position is the priority.** The first item is the most important thing
outstanding; the last is the least. Reordering is done by moving a block, and
that is the main way a person changes what this page says.

**The id is stable.** `B6` stays `B6` when it moves, so ids appear out of order
and that is correct rather than a mistake to tidy. A row that leaves is not
reused. **The next unused id is `B31`**, including after completed items are
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
| **discussion** | a topic in [`discussion.md`](discussion.md) addressed to them, or a reply into a topic of theirs — the standing channel for anything that is **not** a defect report | a person carries it; `prompts/process_discussion` reads theirs, and nothing here writes into anybody else's file |
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
