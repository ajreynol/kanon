# Maintaining kanon

**If you are a human maintaining this repository — possibly by directing an
agent — this is the page to start on.** The short one. What you do, in your own
words, at the end of a long day.

**Written by an agent, for you**, which means it can be wrong in a particular
way: an agent summarising what the tools here would tell you has no way to
check that it summarised them fairly. **If a line here does not match what a
tool actually says, the tool is right and this page is stale.**

[`protocols.md`](protocols.md) records the named exchanges and how a person
directs an agent. **Each command documents itself**, at the top of its own file.

## Where to start

1. **Read the register**: `scripts/eo_status_audit`. Inventory validation and
   the regression suite work without any checkout but kanon's.
2. **Read [`board.md`](board.md)** for what is outstanding and in what order —
   the shortest answer to *what should I do next*, and the only page that
   carries one. [`roles.md`](roles.md) answers the question the board assumes
   you can already answer: *whose is this, and whose is it not*.
3. **Check [the supervision ladder](#the-supervision-ladder)** below before
   touching any document in it.
4. **Run** `python3 -m unittest discover -s tests -v`,
   `scripts/eo_status_audit --check`, and `python3 scripts/policy_check.py --root .`.

## What this repository is responsible for

| what | where |
| --- | --- |
| policy and joining | [`policy.md`](policy.md) — the rule, not the commands that state it |
| the development vision | [`vision.md`](vision.md) |
| the authoritative name register and vocabulary, maintained by the president | [`glossary.md`](glossary.md) |
| the register, and reading it back | `scripts/ecosystem/` |
| the laws, the board and the role register | [`laws.md`](laws.md), [`board.md`](board.md), [`roles.md`](roles.md) |
| the term record, and what crosses to the next president | [`history.md`](history.md) |
| what we are saying to other tools | [`discussion.md`](discussion.md) |
| the protocols | [`protocols.md`](protocols.md) |
| maintaining this tree | this page |

**The analyzer, the fuzzer, the policy checker and the findings workflow are
[anoieu's](https://github.com/ajreynol/anoieu).** Links below to those
artifacts name that repository. **A change to the shared policy can affect
other repositories even though the file is local**, which is what the ladder is
for.

## What you do

| | what you do |
| --- | --- |
| [`INST-1`](#inst-1--your-working-window) | set your working hours, once, and let us hold you to them |
| [`INST-2`](#inst-2--every-answer-says-who-it-is-from) | type *identify* whenever you want to know which tool the agent thinks it is working for |
| [`INST-3`](#inst-3--do-not-outrun-your-own-understanding) | do not push development faster than you understand it |
| [`INST-4`](#inst-4--picking-it-back-up) | the command that tells you where everything stands |

Ids stay put. A withdrawn one stays listed, so nobody reuses the number.

---

## The contract

**What you supply:** direction, and the decisions that are nobody else's to make.

**What comes back:** changed files left in the working tree, arguments you can
disagree with, and a summary saying what was done and what was left. Checks are
run and their output reported.

**What never comes back**, whatever you ask for: anything sent to another
repository, any repository created, anything pushed, posted or published. Those
are structural — no code here can do them — and the reason is in
[`protocols.md`](protocols.md): the path from an idea to a public artifact must
have a person in it.

### The decisions only you can make

These are the inputs the work stalls without. If a session seems to be waiting,
it is almost always waiting on one of these:

- **starting or ending a child project**, and changing its scope;
- **creating a repository**, which is a security boundary and not a convention;
- **a footing** in
  [`../scripts/ecosystem/ecosystem.json`](../scripts/ecosystem/ecosystem.json)
  — no script writes that file;
- **granting a role**, and approving a handoff;
- **changing a prompt template**;
- **carrying anything to another repository** — a finding, a topic, an
  announcement — and choosing which repositories, and whether at all;
- **naming which discussion topic** is to be acted on. The response gate needs
  the name, so "handle the koine topics" stalls where "answer `koine-D9`" does
  not;
- **a stance on publishing**, for this repository and for each child project;
- **who gets notified of a change**, when, and in what words. A draft
  announcement is not a message already sent.

## Prompting advice

Learned from sessions that went wrong, in rough order of how much each cost.

**Say which repository the prompt is for.** These trees are alike on purpose
and sit side by side on one disk, and a prompt meant for one arriving in
another is a real failure with a real incident behind it — the rule is *A
prompt may not be for this repository* in [`policy.md`](policy.md). One clause
at the top prevents it.

**Never ask a repository whether it should hold something.** *Should koine own
the communication protocols* is a question koine cannot answer: an agent asked
to find the case for X will find it, and the result is indistinguishable from
an honest answer. Ask the register that would record it, or ask the repository
the different question — *what would you accept*.

**Name the topic, not the pile.** The response gate requires it, so this is the
difference between work happening and a clarifying question coming back.

**Say what you want back**: a judgement, a draft, or a change. The three have
very different costs and the wrong guess wastes a whole turn.

**Ask for removals, not only additions.** Every protocol here is held to *an
addition says what it removes*, and the counter that watches it has reported
three rounds and three increases. Nothing counts pages at all. A prompt that
says *what comes out* is the one that moves that number, and it is rarely asked
for.

**State the conservatism you want.** *We are still testing whether this
workflow is safe* changes what gets done, not just how it is described — it is
the difference between a register being edited and a register being reported
on.

**Correct mid-turn; it is cheap.** Several of the better outcomes here came
from a one-line correction landing while work was in flight — *exercise this in
moderation*, *iogos is a joke, it has a concrete scope*. Waiting until the end
costs a full turn of rework.

**Give the principle rather than the edit** where you can. *You can do anything
you want if the repository's policy says it is AI generated* produced a rule
that generalises; the equivalent list of permitted actions would not have.

## `INST-1` — your working window

**Write down the hours you mean to work.** Up to ten a day, and you can name
breaks inside them.

**Do it in daylight.** The urge to keep going turns up later than the judgement
about whether to.

Outside your hours, you get a reminder to take a break, once a session. You
still get your answer; nothing is withheld or slowed down.

**Doing research? Say so, and it stays quiet for the session.** It is yours to
say; no tool decides that for you.

### Setting it

```text
python3 scripts/sleep.py
```

That prints your window and where you stand in it. Edit `scripts/schedule.json`
for the start, end, breaks, and optional timezone. These operational files stay
in kanon; the ethics projects and their case records now live in epikrisis.

**Two things it cannot do.** It cannot stop you. And it does not know how much
you have worked — only what time it is.

---

## `INST-2` — every answer says who it is from

**Every response you get opens with one line**: the tool the agent believes it
is working for, and what that tool is for.

<tool> — <what it is for>, powered by <which AI, by name>.

**It names the AI, specifically** — which model and which version, not "an
assistant". You are entitled to know what is answering you: these differ in
what they are good at and in how they fail, and you cannot weigh an answer
without knowing that. *The documents here never name one, deliberately, so that
anybody's agent can do this work; the spoken line always does.*

**You do not have to ask for it, and it should never stop.** If it stops, the
protocol has been dropped, which is worth more of your attention than whatever
was in the answer.

**Ask for the long version any time.** You get the same line plus which
checkout it is working in and the mission quoted from that tool's own files.

**If it is ever wrong, say so.** The agent is reporting a belief, not proving
anything, and you are the only one in a position to correct it. The
repositories here look alike, and an agent in the wrong one is not visibly
confused — it is confidently helpful in the wrong place.

---

## `INST-3` — do not outrun your own understanding

**Do not push development faster than you understand it.** Not *faster than it
can be built* — an agent will always be able to build faster than you can
follow, and that is not the constraint. **The constraint is you.**

**This is an ethical line and not only a practical one.** Work you have not
understood is work you cannot be said to have decided on, and at some point the
record stops being a record of what you chose.

**In practice:** when something has been built that you have not had explained,
**ask for the explanation before asking for the next thing.** It is always
cheaper than it looks, and the debt compounds — each unreviewed piece makes the
next one harder to review.

*This instruction has no matching protocol, deliberately. It is addressed to
you, and turning it into a rule for the agent would move the judgement to the
party that cannot make it.*

---

## `INST-4` — picking it back up

**Start here after a break.**

```text
./scripts/eo_status_audit
```

One line per tool: what footing it is on, whether our checks pass on it, how
many topics it has addressed to you, and when it last moved. `eo_status_audit --help`
says what every column and every value means, and what to do about a failing
row. **It ends in a single sentence summarising all of it.**

### How to read the answer

**The notes below the table are the actionable part.** Each names a
disagreement and whose move it is. The one you will see most:

> *tool X says it follows the shared policy, and N of our checks fail on its
> tree.*

**That means X is claimed as a member and its repository is not set up the way
membership says it will be.** The note gives you the command that shows what
failed.

**A tool with topics owed to you is waiting on you**, not the other way round.
That number is the closest thing here to a to-do list.

## The supervision ladder

Ordered, most supervised first. *Supervised* means: propose the change and the
reason, and wait for a person — do not make it and mention it afterwards.

| | document | what it takes |
| --- | --- | --- |
| 1 | [`vision.md`](vision.md), the report card | **ask first, always**, and **at most five lines of diff** |
| 2 | [`policy.md`](policy.md) | ask before the rules. Append; never renumber; retiring one in place is a person's |
| 3 | anoieu's reporting policy | not yet stable, so ask before changing what may be said about somebody else's code |
| 4 | anoieu's reporting workflow | ask before the prompts |
| 5 | the generated documents | never hand-edited, and nothing to ask about |
| 6 | everything else | ordinary work. No permission needed |

**The vision is asked about first because the party with the least standing to
revise it is the agent it governs.** It is addressed to repositories that did
not write it, and a paragraph in the report card is a judgement about somebody
else's project — softening or sharpening one is exactly the edit that should
not be made quietly.

**Five lines is what *ask first* cannot do on its own.** A person reviewing a
page they already agree with will approve a well-argued twenty lines. **A bound
checked by counting cannot be argued with**, and it forces the same discipline
on every edit: a change needing more than five lines is not a vision change, it
is a document that belongs elsewhere with one sentence pointing at it. **The
vision holds claims, not their justifications** — which is why the argument for
the line about enjoying this lives in `PROTO-25` below and the line itself
lives there.

**Nothing may ever check the vision mechanically.** Whether a tool is fruitful
or a claim oversold is contestable and nobody has standing to settle it, so a
green tick against a tenet would invent an authority that does not exist. It is
the one rule here that forbids work rather than requiring it.


**What a repository says about itself decides how freely you may work in it.**
Where the maintenance note says the tree is **written by AI agents**, an agent
does ordinary work in it without asking step by step — the ladder above still
orders what needs a person *within* this tree, and that is the whole of the
constraint. Where the note says people write it, or where there is no note,
restraint applies: propose, show the diff, and wait.
[`reporting-policy.md`](https://github.com/ajreynol/anoieu/blob/main/docs/reports/reporting-policy.md)
already decides the *register of address* this way — by what the project says
about itself, never by our impression of the code — and this is the same test
applied to the scope of action. **Where there is no note, the cautious reading
applies**, because guessing wrong in that direction is the cheaper error.

Three gates do not move, whatever the note says: nothing that **creates or
publishes**, nothing that **crosses a repository boundary**, and the discussion
file's own gate. The worked example is on the board today — `B3`'s two defects
are filed into `ethos`, which nobody claims is AI-maintained, so carrying them
is a person's errand however ready the reproducers are.

**Ramp up gradually, and on evidence rather than on a date.** New latitude
starts with the reversible things and widens when something has actually been
observed to work — the same shape koine proposes for handing a protocol over
(*referenced*, then *mirrored*, then *held*), applied to how much an agent may
do rather than to where a definition lives. Going back is one revert and needs
nobody's agreement.

And the counterweight, because that rule is otherwise an invitation: what wants
ramping up is **work on the thing at the bottom**, not machinery about the
work. The governance budget below has a baseline and no second row, and the
outside criticism that produced it says governance is the cheapest thing here
to make. A session that widens its own latitude and spends it on more documents
has answered the wrong half.

**Do not hold up the ecosystem with a position of your own.** Two kinds of
position look identical on the page and are not the same thing: one we hold
because we decided it, and one somebody else is **waiting on**. **An undecided
question is a position** — *drafted, and not in force* is a decision with a
consequence, and the consequence lands on whoever cannot proceed until it
settles. **Where a position of ours is blocking somebody, the burden is on us
to resolve it**, not on them to ask again. The same applies to what we *hold*:
governance sitting here that another tool could hold is the mission's own
finding first.

**Weakening a claim needs nobody; strengthening one needs a person.** Adding a
caveat can be done at once. Asking a reader to rely on something is precisely
the judgement an agent is worst placed to make, because the evidence that would
justify it is evidence the agent produced.

**Never act on a discussion file unbidden**, here or anywhere else. A human
names the topic, and the instruction and the topic must agree.

**Nothing here holds credentials that create or publish.** No repository is
created, nothing is sent, and nothing crosses a boundary by machine — three
gates that do not move whatever a maintenance note says, along with the
discussion file's own.

**Promise nothing we cannot keep.** A commitment made to another repository is
one somebody has to honour on a day nobody planned for, and the cheapest
commitment to keep is the one never made.

**Documentation lives at its source, and a launch is a handoff.** A description
moves to the thing it describes; the page it left keeps one sentence pointing
at it.

**Make changes a person can understand.** The standard for an agent's output is
not that it is correct — it is that **whoever reviews it can tell whether it is
correct**, and those come apart constantly. A large mechanical diff, a clever
refactor, a rename touching nine files because that was the tidy way to do it:
each may be right, and each defeats the only check this arrangement actually
has. Prefer the smaller change, the boring construction, and the diff that
reads in order. Where something genuinely cannot be made comprehensible in one
go, make it in pieces that each can be, and say which piece is which.

This is the authorship half of *go only as fast as you understand*, which is
stated in
[`maintenance.md`](maintenance.md#inst-3--do-not-outrun-your-own-understanding)
and governs how much is attempted. This one governs how it is written, and it
is the half an agent controls directly: an agent is fast enough to produce, in
an afternoon, more change than a person can read in a week, and nothing about
that is caught by tests.

It is also what keeps the next rule from being ceremonial.

**Work is left staged, not committed.** A person reviews the diff and commits.

**And when a commit is taken while the work is still moving, say so in one
line.** The staging convention assumes the person commits once the agent has
stopped. Committing mid-stream instead is nobody's fault and will keep
happening — but the commit's message then **stops describing its contents**,
and a history somebody can walk is most of what this ecosystem claims. A reader
looking for a change finds it filed under a subject it has nothing to do with,
which is worse than not finding it.

The remedy is deliberately small: **one line naming the commits and what they
actually carry.** Anyone may write it, anyone may delete it, at any time,
without asking — it is a note about the record rather than a record in its own
right. Nothing waits on it and nothing is blocked by it being there or gone.

This is not a formality: it is the last place where a change to a document that
binds another repository can be caught.

## The scripts

`scripts/` contains deterministic commands and nothing that launches an
assistant. **Each states its subject at the top of its own file**, and
`eo_status_audit --help` carries the key to the table. The untracked
`scripts/repos.local` checkout map is **written by hand**, one `ID PATH` pair
per line.

**There are no prompts in this tree**, and installing the ecosystem is not done
from here. The commands that hand context to an assistant are koine's and are
installed: `eo_init` and `eo_join`, which draft changes in the repository being
started or joined, are `R35`; `eo_process_discussion` reads another tree's
discussion file; `eo_bump` moves the pin. Each takes `--show-prompt`, which
prints its assembled instructions without launching an assistant and writes no
files.

## The build

The `checks` workflow runs the offline regression suite and inventory validation.
The suite covers local document links, glossary project labels, command behavior,
checker discovery and errors, and child listings. It launches
no assistant, clones no repository, and makes no network requests.

The separate `anoieu / policy` job fetches the checker at the commit pinned in
[`anoieu.lock`](../anoieu.lock) and runs it against kanon. Other members also pin
**anoieu**, which owns the checker implementation; kanon's `scripts/policy_check.py`
is a local launcher, not that shared implementation. A local launch uses the
available anoieu checkout and does not establish that CI ran at the pinned
revision. `eo_bump --check` asks whether the upstream tip is green;
it is an explicit online command, not part of CI.

A passing build establishes only what those checks actually exercise. It does
not verify definitions, tool quality, consent, or another repository's handoff.
Keep failures actionable and the local suite independent of remote state.

## The governance budget

**The rule exists and nothing counts against it.**
[`report-card.md`](../tools/stathmos/report-card.md)
grades this repository down for exactly this and states the rule in the same
paragraph: *every further page here has to displace a check, a finding, or an
hour of somebody else's reading.* Nothing has ever measured whether it is kept.
A rule with no counter attached is the same failure the prompt-length table in
[`postmortem.md`](https://github.com/ajreynol/anoieu/blob/main/docs/reports/postmortem.md)
exists to fix in the other half of the system — and it is the criticism that
came from outside, in `workflow-launcher`'s register of what this ecosystem's
practice appears to be doing, which reads six checkouts and writes down what is
wrong with them beside what is not. It is a child project in eudaimonia's tree,
at `tools/workflow-launcher`, and `docs/ai-workflows.md` is the document.

So: the baseline, measured over this tree on 2026-09-01. Reproducible in three
commands, and worth nothing until there is a second row.

| what | files | lines |
| --- | --- | --- |
| tracked Markdown outside `deps/` | 32 | 15,142 |
| — generated, written by a tool | 4 | 1,142 |
| — child projects, shipped by nothing and advertised nowhere | 10 | 4,550 |
| — **written prose: the number this section is about** | 18 | **9,450** |
| Python | 54 | 13,382 |
| `scripts/` | 9 | 2,481 |
| checks with a page in [`checks.md`](https://github.com/ajreynol/anoieu/blob/main/docs/checks.md) | | 63 |
| findings in the ledger | | 39 open, 43 closed |

```
git ls-files '*.md' | grep -v '^deps/' | xargs wc -l | tail -1
git ls-files 'tools/*/*.md'           | xargs wc -l | tail -1
git ls-files '*.py'                   | xargs wc -l | tail -1
```

**What the row is for, and what it is not.** It is not a limit. Nobody has
argued what the right ratio is, a budget invented here would be a number to
game, and a page is not bad for being long. It is for the *next* reading: the
rule says a page displaces a check, a finding, or an hour of reading, so if
written prose grows between two rows of this table while the check count and
the finding count do not, then the rule was not kept — and that becomes a fact
somebody can point at rather than an impression somebody has to argue for.

**Record the row; do not move the rule to fit it.** That is the discipline the
prompt-length table already keeps, including the part that makes it worth
having: it reports its own metric going the wrong way, three rounds running,
rather than being quietly retired. A counter that only ever confirms is not a
counter.

And this section is itself the thing it measures. It costs about fifty lines of
written prose and displaces nothing today, which is the honest accounting; what
has to pay for it is the second row.

## Keeping names and ynoia's arguments current

[`glossary.md`](glossary.md) is the authoritative name register, maintained by
the president. [`ecosystem.json`](../scripts/ecosystem/ecosystem.json) records
membership and checkout locations. Ynoia's
[naming guidance](../tools/ynoia/proposals.md#arguing-about-names)
links to the glossary to argue names; it keeps no parallel register.

| when | the edit |
| --- | --- |
| a name enters use | add its meaning and source to the glossary; include the project's footing or parent |
| a project moves | update its inventory location and glossary label together |
| a naming idea is proposed | keep the rationale and alternatives with the proposal; unused names stay out of the glossary |
| a tool discussed in ynoia starts existing | update the argument in `tools.md` to reflect what now exists |
| a project's publication prospects change | update the judgement in `papers.md`, citing the project's own position |

The offline suite compares glossary project labels with the inventory. Review
meanings against their sources as well: a matching label does not establish a
correct definition, and a name missing from the glossary may still be used in
a neighbouring tree. Ynoia's arguments are reading, not a CI requirement or a
second naming authority.
