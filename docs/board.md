# The board

**What is being maintained across the Eunoia ecosystem, in priority order.**
One page, at most twenty-four items, each with the next thing to do and who has
to do it. Written for a person to read in a minute and edit by hand.

The inventory validator reads each item's **Entities** field to check that the
board names registered tools. Priorities, status and next steps are maintained
by hand.

## How to read it, and how to edit it

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

The seven steps are in [`roles.md`](roles.md#how-a-role-is-handed-off), and
`B15` is the worked example — transferred, with policy/checker version
coordination still open. **None of it gates anything** while the ecosystem is
still settling; the same section says what would change that and who decides.

---

## B6 — the shared prompt-drift check exists and awaits adoption

**Task:** decide whether anoieu and dokimasia adopt koine's existing
prompt-drift checker and remove their local copies.
**Entities:** `anoieu`, `dokimasia`, `koine`
**Status:** waiting on the customers — koine publishes the checker and both
customer specifications; anoieu still keeps its local `prompts_agree()`.
**Channel:** **discussion** — through the customers' existing topics with koine.
**Next:** compare the published customer specifications with the current prompt
layouts, then adopt a pinned version or record why keeping the local copy costs
less.
**Evidence:** [koine's running interface](https://github.com/ajreynol/koine/blob/b927aac9e8b402e58f6b1ccdc6f4c5056c868015/README.md#running-it)
contains the command and customer comparison. The build is no longer the task.
**Prompt — `anoieu`:** decide whether to replace the local drift check with the
published implementation after checking it against the current prompt layout.
**Prompt — `dokimasia`:** make the same comparison for your own workflow; a
reasoned decision to keep the local check is a complete answer. **Prompt —
`koine`:** the implementation is available. No new implementation is requested
by this item.
**HUMAN FEEDBACK:** raised to the top 2026-08-31: settling this enables a lot of other work.

## B3 — the fuzzer has found real defects and filed none of them

**Task:** **two crashes the fuzzer found in ethos and nobody has filed.** An uncaught C++ abort on a one-line
signature, and error paths that print outside ethos's own `Error:
<file>:<line>` convention. Six reproducers are committed here; nothing has been
sent upstream.
**Entities:** `ethos`, `anoieu`
**Status:** ready — the reproducers exist and are committed under `tests/fuzz/`.
**Channel:** **findings** — `ethos-8` and `ethos-9`, through `prompts/check_anoieu ethos`, because a defect report is not a discussion topic.
**Next:** file the two, with their reproducers, through the ordinary loop.
**Prompt — `ethos`:** `(declare-const f (->))` aborts with an uncaught
`std::length_error` rather than reporting a bad type. Separately, three error
paths exit without a file or line, which breaks the convention every other
error in the binary follows. Reproducers are committed and fetchable raw.
**Prompt — `anoieu`:** run `prompts/check_anoieu ethos` for these two rows, and
say plainly in the report that the fuzzer produced them — a provoked crash and
a read signature are different claims and the codes already say which.
**HUMAN FEEDBACK:** raised 2026-08-31: these are real defects and nothing is stopping us filing them.

## B24 — the office's messages have no way to be delivered

**Task:** the office's unit of work is a message to one tool, and nothing
carries one. Every topic staged in [`discussion.md`](discussion.md) waits on a
person, with no channel named for most of the tools it is addressed to.
**Entities:** `kanon`, `koine`
**Status:** open, and it blocks every other thing this office produces.
**Channel:** **discussion**, where the receiving tool keeps one; by a person
otherwise.
**Next:** decide whether delivery is koine's protocol or a person's habit, and
write the answer where a ball is drafted. **Prompt — `kanon`:** do not build a
second delivery mechanism. `koine` exists to be the one implementation, and a
president building a rival breaks the mission it holds the office to serve.
**HUMAN FEEDBACK:**

## B19 — a child project has fifteen candidates and no route out

**Task:** **fifteen pieces of candidate feedback on the Eunoia manual, written by a child project here and carried nowhere.** `sapheneia`'s ledger, read against the ethos
manual, found by writing a second account of the language and noticing where
the second reading could not recover something from the first. **None has been
carried anywhere**, and its own status page says so.
**Entities:** `kanon`, `ethos`
**Status:** ready — the ledger is written, read against `user_manual.md` at
`3cf1c03`, and every row cites the section it is about.
**Channel:** **upstream, by a person** — `ethos` has no discussion file, and a
child project has no channel of its own: anything it says leaves through this
repository, carried by somebody who can answer the follow-up.
**Next:** pick the two or three rows that are checkable by reading the sentence
they cite — the grammar ones, `EOM-01` and `EOM-02` — and carry those alone.
The judgement rows wait until a reader who knows Eunoia has looked at the
ledger, which nobody has. **Prompt — `kanon`:** these are *candidates* and are
to stay labelled as such; the ledger's own header says most likely to be wrong
are the judgement rows, and that caution is the reason it is worth reading. Do
not file them as findings — they are about a document, not a defect in a file
with a line number. **Prompt — `ethos`:** a second, independent description of
Eunoia was written against your manual, and fifteen places came up where the
second reading could not recover something from the first: a silence, an
ambiguity, or a passage that does not appear to agree with itself. Two are
grammar productions that derive nothing; the rest are documentation. **HUMAN
FEEDBACK:**

**Note.** Seven other language questions, found by writing the *analyzer*, end
at the same manual and are anoieu's rather than ours. These were found by
writing a *second manual*. Different instruments, and this ledger had no board
row at all until the inventory of 2026-09-01 went looking.

## B21 — an ethics we can be held to, taken from work we have not read

**Task:** `zetesis` says its standard comes from outside and cites the
reading that supports it. **The reading has not been done**, so the project has
a question, three recorded gaps, and no standard.
**Entities:** `kanon`, `zetesis`
**Status:** ready — nothing is blocked on anybody else, and the first hour of it
is a literature search.
**Channel:** **internal** — nothing to send, and nothing here is filed anywhere.
**Next:** find and cite one external account of what an agent-run project owes,
and say plainly which of our claims it does and does not reach. **Prompt —
`kanon`:** support zetesis in finding and assessing a standard somebody outside
this ecosystem argued for. Until one is cited, every claim this ecosystem makes
about its own conduct rests on a standard it wrote itself, which is the weakest
possible arrangement and the one we criticise elsewhere. **Prompt —
`zetesis`:** name what you could not find as carefully as what you did. A gap
in the literature is a result; a plausible bibliography assembled to look
rigorous is the failure you exist to notice. **HUMAN FEEDBACK:**

---

*A full board is one that has stopped being prioritised. If this page is at its
cap, the next thing to do is not to add an item — it is to decide which one has
stopped mattering. The count is deliberately not written here: it rots, it has
rotted twice, and anybody who needs it can count.*

## B26 — no node has a front-page FAQ, and kanon does not either

**Task:** joining cost koine eighteen hundred lines of reading, and nowhere does
a tool say the short version of itself.
[`policy.md`](policy.md#common-questions-on-the-front-page) recommends the
answer — a `## Common questions` section on the front page.
**Entities:** `kanon`
**Status:** open on our own side first. **Nothing may be proposed to anybody
until kanon carries one.**
**Channel:** **local**, then a ball each.
**Next:** write kanon's, then propose the section to one other tool.
**Prompt — `kanon`:** proposing a style you have not adopted is the error this
office exists to avoid. **HUMAN FEEDBACK:**

## B25 — nobody has measured how long an answer takes

**Task:** the constraint on every handoff this office will ever propose is that
a question to another tool takes hours to land and can sit a whole term
unanswered. That is asserted everywhere and measured nowhere.
**Entities:** `kanon`
**Status:** open. The figure is re-derivable from discussion files and commit
dates, and nobody has derived it.
**Channel:** **local** — it reads public history and asks nobody for anything.
**Next:** take the measurement once, over the topics that exist, and state the
method so somebody can disagree with the number. **Prompt — `kanon`:** a
latency claim with no measurement behind it is the kind of sentence
[`practice.md`](practice.md) says to cut. **HUMAN FEEDBACK:**

## B18 — the associate protocol remains open for ethos

**Task:** `associate` is defined and proposed for ethos, but what a repository
has to carry was never decided. [Anoieu's
`D11`](https://github.com/ajreynol/anoieu/blob/main/docs/discussion.md#d11--we-have-a-footing-for-you-and-no-protocol-to-put-you-in-it).
**Entities:** `kanon`, `ethos`
**Status:** waiting on `ethos` — the choice between the two versions
of the protocol is theirs to answer before it is ours to fix.
**Channel:** **upstream, by a person** — ethos has no discussion file, so the
question is carried by hand.
**Next:** decide the one open question — the bare maintenance-note heading, or
that plus the paragraph naming this ecosystem — and write it into
[`policy.md`](policy.md) as in force. **logos is a member**, so its associate
proposal is superseded and it is not a party we are waiting on for this item.
**Prompt — `kanon`:** do not record ethos as an associate until the protocol is
decided; `proposed:` is the field that holds the intention, and
`scripts/status_eo --protocol` is the report. When it is decided, the section
in `policy.md` stops saying *drafted, and not in force* and the ethos entry
moves in one commit. **Prompt — `ethos`:** we would like to record you as an
associate: a footing that obliges you to nothing, runs nothing in your CI, and
says that every other reading of the language is measured against your
checker's behaviour. The only thing it would ask is a `How this repository is
maintained` heading. Which would you rather be asked for — that alone, or that
plus a paragraph saying you are not held to our policy? Neither is also an
answer. **HUMAN FEEDBACK:**

## B28 — a tool is running and is in no register

**Task:** `telos` is recorded as a child project and is doing work; comparing
agendas across the ecosystem is impossible while a running tool is missing from
the view somebody reads.
**Entities:** `kanon`
**Status:** open. **Membership is a decision, not a fact about a tree**, so the
register does not fix itself.
**Channel:** **local**, then confirm with whoever owns it.
**Next:** a person decides the footing; `scripts/status_eo --check` reports the
result. **HUMAN FEEDBACK:**

## B29 — Stretch 1's figures are quoted here and checked by nobody

**Task:** LAW 4 asks that every figure in a term record be re-derivable by
somebody else. Figures from the previous stretch are repeated in this tree
without anybody re-taking them, which is the weakest form the record can have.
**Entities:** `kanon`, `anoieu`
**Status:** open. It is kanon's own defect rather than anoieu's.
**Channel:** **local** — the public run history is enough.
**Next:** re-derive or drop them. A number only its author can produce does not
go on the page. **HUMAN FEEDBACK:**

## B27 — two ethics projects sit inside the tree they assess

**Task:** `martyria` and `zetesis` examine how this ecosystem behaves, from
inside a repository that is part of it. That is the ethics half of the
judge-inside-the-judged problem, and it is not resolved by either of them
saying so in their own README.
**Entities:** `kanon`
**Status:** open. A person decides; no agent has standing to.
**Channel:** **local** — nothing crosses a boundary until a person moves it.
**Next:** decide whether either graduates, and say what would make the answer
different. **HUMAN FEEDBACK:**

## B30 — there is no way to find out what a tool can be asked for

**Task:** the ecosystem has tools that would answer questions nobody knows to
ask them. A reader arriving at any tree can find what it *is* and not what it
*will do for you*.
**Entities:** `kanon`
**Status:** open, and it needs each tool's own answer rather than ours about
them.
**Channel:** **discussion**, one ask per tool, carried by a person.
**Next:** ask two tools and see whether the answers have a shape worth
proposing. **Prompt — `kanon`:** do not write this register *about* other
tools. A description of what somebody else offers, published under our name, is
the failure [`policy.md`](policy.md) reserves the endorsing footings to
prevent. **HUMAN FEEDBACK:**

## B1 — cvc5's `Strings.eo` type mismatch, recorded as fixed and never fixed

**Task:** **a type mismatch in cvc5's `Strings.eo` that was recorded as fixed and never was.** Two program declarations that return `Bool`
from a signature that declares `Int`, recorded as fixed upstream three months
ago on a change that never landed.
**Entities:** `cvc5`, `logos`, `anoieu`
**Status:** waiting on `cvc5` — reopened after the landing audit caught it.
**Channel:** **findings** — `cvc5-1` in the ledger, carried by `prompts/check_anoieu cvc5`. `cvc5` has no discussion file and has joined nothing; delivery upstream is a person's act.
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
