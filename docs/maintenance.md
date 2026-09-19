# Maintaining kanon

**If you are a human maintaining this repository — possibly by directing an
agent — this is the page to start on.** The short one. What you do, in your own
words, at the end of a long day.

**Written by an agent, for you**, which means it can be wrong in a particular
way: an agent summarising what the tools here would tell you has no way to
check that it summarised them fairly. **If a line here does not match what a
tool actually says, the tool is right and this page is stale.**

Shared requirements are in [`policy.md`](policy.md) and [`laws.md`](laws.md).
**Each command documents itself**, at the top of its own file.

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
   `scripts/eo_status_audit --check`, `scripts/eo_tooling_audit --check`, and
   `python3 tools/stathmos/audits/policy_check.py --root .`.

The regression suite includes stathmos's tests from
[`tools/stathmos/tests/`](../tools/stathmos/tests/). Run those alone with
`python3 -m unittest discover -s tools/stathmos/tests -v`.

The authoritative register is
[`scripts/ecosystem/ecosystem.json`](../scripts/ecosystem/ecosystem.json).
An entry with `status: president` identifies the current holder. The offline
audit rejects multiple holders. In the status table, the audit reports limbo
when the recorded president lacks `docs/laws.md` or `docs/history.md`, under
[LAW 3.4](laws.md#law-34--when-the-recorded-president-cannot-maintain-the-office); that observation does not fail a build or
withdraw the appointment. The command's
`--help` describes its current coverage and limits.

## Recording a new project

A person chooses its footing and authorizes any new repository. `eo_init` can
draft a README for new work or a project moving out of a child directory.

1. Read the project's own description when inspection is permitted under
   [LAW 9](laws.md#law-9--external-research-release-publication-and-permitted-comparisons).
   Record its footing and required evidence in
   [`ecosystem.json`](../scripts/ecosystem/ecosystem.json).
2. Include existing children, advertised or not, under their parent. Record
   names in use and their footings in [`glossary.md`](glossary.md); unused
   naming ideas stay with proposals.
3. Run `scripts/eo_status_audit --check` and the regression suite. Use
   `scripts/repos.local` for an existing checkout outside the normal search
locations; local paths do not belong in the shared inventory.
4. Installation uses the inventory and `checkouts.json` exceptions. Children
   arrive with their parent; outsiders are not cloned. A child's README
   controls its [listing preference](policy.md#child-projects).

Record tools, artifacts and tutorials in
[`ecosystem_tooling.json`](../scripts/ecosystem/ecosystem_tooling.json): its
repository, directory, entry points or content files, and documentation.
Tools include libraries: their public modules count as entry points without
requiring a standalone executable.
`owner` defaults to the repository and can name a child project; layout is
measured within that owner's root. All entry paths remain repository-relative.
`kind: artifact` records maintained data, such as bug databases and proof
signatures; `kind: tutorial` records instructional guides. Both use content
`files` without requiring executable entry points. Documentation is recorded
in `docs`, never as its own
tooling entry; `docs/` and `contrib/` cannot be tooling directories. `contrib/`
is reserved for manually obtaining external tools. Shared launchers and docs
may sit outside the owner. `scripts/eo_tooling_audit`
reports missing paths, unregistered top-level directories and layout gaps;
`--verbose` shows the recorded entry points and source revisions. Explain
nonstandard layouts with `layout_note` and non-inventory directories with
`exclude`, whose directory names are relative to the named owner's root.
Exclusions are displayed with their reasons as non-compliant inventory coverage;
recording one explains the gap without hiding or clearing it. Foundation tooling
such as cvc5 is included without changing its footing or policy obligations.
`--check` validates records without checkouts; add `--local` or `--online` to
compare trees. Explicit exclusions fail those comparisons, while layout
observations alone never fail a check.

Joining through `eo_join` is the owner's choice. No welcome message or
post-join grade is required.

## What this repository is responsible for

| what | where |
| --- | --- |
| policy and joining | [`policy.md`](policy.md) — the rule, not the commands that state it |
| the development vision | [`vision.md`](vision.md) |
| the authoritative name register and vocabulary, maintained by the president | [`glossary.md`](glossary.md) |
| the authoritative register and installation exceptions | `scripts/ecosystem/` |
| the status audit, maintained by stathmos | `scripts/eo_status_audit` runs [`tools/stathmos/audits/status_audit.py`](../tools/stathmos/audits/status_audit.py) |
| the tooling audit, maintained by stathmos | `scripts/eo_tooling_audit` runs [`tools/stathmos/audits/tooling_audit.py`](../tools/stathmos/audits/tooling_audit.py) |
| the laws, the board and the role register | [`laws.md`](laws.md), [`board.md`](board.md), [`roles.md`](roles.md) |
| the term record, and what crosses to the next president | [`history.md`](history.md) |
| what we are saying to other tools | [`discussion.md`](discussion.md) |
| maintaining this tree | this page |

**The analyzer, the fuzzer, the policy checker and the findings workflow are
[anoieu's](https://github.com/ajreynol/anoieu).** Links below to those
artifacts name that repository. **A change to the shared policy can affect
other repositories even though the file is local**, which is what the ladder is
for.

## What you do

| | what you do |
| --- | --- |
| `INST-1` | withdrawn, 2026-09-17 |
| `INST-2` | withdrawn, 2026-09-18 |
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
are structural — no code here can do them. The path from an idea to a public
artifact must have a person in it.

### Working with an agent

When asked to stop, stop and summarize what changed. If a rollback is requested,
confirm its boundary when unclear and restore through forward changes without
rewriting history. Point out affected published or pinned versions.

Read available evidence before asking questions. Continue authorized work that
does not depend on an answer, and ask only when different interpretations
would lead to consequentially different actions. Report concrete changes,
checks and remaining uncertainty. When approval is needed, state the exact
action and its evidence; no fixed approval block is required.

Before making a claim about another project, check the source and its version
when access is permitted, date the claim, and say what could not be verified.

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

**Ask for removals, not only additions.** Ask what a new rule or document
replaces, and what can be shortened or deleted. A prompt that says *what comes
out* makes that tradeoff explicit.

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
is a document that belongs elsewhere with one sentence pointing at it.

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
file's own gate. Filing a defect against ethos is a person's errand however
ready the reproducer is; its human-maintained checker is not ours to change.

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
started or joined, are `R35`; the rest are `R16` — `eo_respond`, which answers
one topic another tree has addressed to us and refuses a run that names none;
`eo_housekeeping`, which reads what is outstanding across the checkouts;
`eo_topic`, which opens one topic in our own discussion file and asks the person
running it for the thing a tree cannot supply; `eo_child`, which starts
`tools/<name>/` here and refuses a run with no name, because naming the child is
the decision the policy reserves to a person; and `eo_brainstorm`, which reads
every tree on the machine and writes only `brainstorm.local.md`. Each takes
`--show-prompt`, which prints its assembled instructions without launching an
assistant and writes no files. `eo_status` reads the register directly and
hands nothing to an assistant.

## The build

The `checks` workflow runs the offline regression suite and inventory validation.
The suite covers local document links, glossary project labels, command behavior,
checker discovery and errors, and child listings. It launches
no assistant, clones no repository, and makes no network requests.

The separate `anoieu / policy` job is
[anoieu's shared workflow](https://github.com/ajreynol/anoieu/blob/main/docs/policy-checker.md)
called at `main`, asking for **policy contract 1**. **This repository pins
nothing for it**, so there is no checker lock to update. What is held still
is the contract, and the implementation behind it may change
between two runs of the same commit. [`policy.md`](policy.md#2-run-the-check)
accepts a pinned commit just as well, and a member may be on either form — read
a member's own workflow file rather than assuming.

**anoieu** owns the checker implementation; stathmos's
[`tools/stathmos/audits/policy_check.py`](../tools/stathmos/audits/policy_check.py)
is the local launcher. A local launch uses
whatever anoieu checkout is on this machine, at whatever revision it is on, and
establishes nothing about what CI ran. **That gap is the subject of `D1`** and
it widened with this change: there is no pinned revision here to reproduce
against any more, only a contract to ask for.

A passing build establishes only what those checks actually exercise. It does
not verify definitions, tool quality, consent, or another repository's handoff.
Keep failures actionable and the local suite independent of remote state.

## The governance budget

**The rule exists and nothing counts against it.**
[`report-card.md`](../tools/stathmos/docs/report-card.md)
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

So: the rows, measured over this tree, each as *files, lines*. Reproducible in
three commands, and the second row is what the first was worth waiting for.

| what | 2026-09-01 | 2026-09-17 | 2026-09-18 |
| --- | --- | --- | --- |
| tracked Markdown outside `deps/` | 32, 15,142 | 31, 15,757 | 33, 15,639 |
| — generated, written by a tool | 4, 1,142 | none: every page here is hand-written | none |
| — child projects, shipped by nothing and advertised nowhere | 10, 4,550 | 16, 7,108 | 19, 7,246 |
| — **written prose: the number this section is about** | 18, **9,450** | 15, **8,649** | 14, **8,393** |
| Python | 54, 13,382 | 8, 2,069 | 9, 1,986 |
| `scripts/` | 9, 2,481 | 8, 2,025 | 3, 571 |
| checks with a page in [`checks.md`](https://github.com/ajreynol/anoieu/blob/main/docs/checks.md) | 63 | 63 | 63 |
| findings in the ledger | 39 open, 43 closed | 39 open, 43 closed | 41 open, 43 closed |

**What the second row says, including the part that is not to our credit.**
Written prose fell by 801 lines while **neither the check count nor the finding
count moved** — both read from anoieu's tree on 2026-09-17 and both are
anoieu's to change, not ours. So the rule was kept in the only direction
available to a repository that writes documents: by deleting pages, not by
earning them. The Python column fell by 11,313 lines for two reasons that are
not the same, and only one is a saving: commands went to koine or were deleted
outright, and `martyria` and `zetesis` moved to epikrisis, which moves lines off
this table without removing them from the ecosystem. **Child-project prose grew
by 2,558 lines**, which is the row to watch next: it is the part of this tree
that nothing advertises and nobody is asked to read.

```
git ls-files '*.md' | grep -v '^deps/' | xargs wc -l | tail -1
git ls-files 'tools/*/*.md'           | xargs wc -l | tail -1
git ls-files '*.py'                   | xargs wc -l | tail -1
git ls-files 'scripts/*'              | xargs wc -l | tail -1
```

The fourth was added on 2026-09-18, because the `scripts/` row had been in the
table with no command behind it since the table was written.

**The third row, and the day it measures went both ways.** Written prose fell by
**256 lines**, and **almost all of the movement is one file**: `discussion.md`
went from 1,185 lines to 697. Six finished topics were removed, and six bundled
answers to other tools — 619 lines, written earlier the same day — were replaced
by three short ones totalling 109. **The first version of that work would have
put this row at +188**, and the row is worth having because somebody read the
file rather than the number.

**What the rule actually caught.** Correspondence is the cheapest thing this
office produces and the hardest for it to stop producing, and a discussion file
is where it accumulates without looking like accumulation — every topic is
individually defensible. **The check that shrank it was not this counter**; it
was reading the settling condition of each incoming topic and noticing that most
name an artifact, so the artifact is the answer and no topic is owed. The
counter's job was to make the first version's cost visible, and it would have.

**Two columns moved for reasons that are not savings, and reading them as such
would be the second failure this table exists to prevent.** `scripts/` fell from
2,025 lines to 571 because the audit's implementation moved to
`tools/stathmos/scripts/`, where it counts as Python and as a child project —
the same shape as `martyria` and `zetesis` moving to epikrisis a day earlier.
And **the ledger counts were re-derived differently**, because anoieu split
`reports.md` into `open-findings.md` and `closed-findings.md`; the 41 and 43
above are rows in those two files, and the earlier columns counted a page that
no longer exists in that form. **A counter whose source moves is a counter that
can drift without anybody lying**, and nothing here checks it.

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

And this section is itself the thing it measures. It costs about sixty lines of
written prose, and with a second row it has at last reported something a reader
can check — which is the first time it has paid for any of itself.

## Keeping names and ynoia's arguments current

[`glossary.md`](glossary.md) is the authoritative name register, maintained by
the president. [`ecosystem.json`](../scripts/ecosystem/ecosystem.json) records
membership and checkout locations. Ynoia's
[naming guidance](../tools/ynoia/docs/proposals.md#arguing-about-names)
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
