# Maintaining kanon

**If you are a human maintaining this repository — possibly by directing an
agent — this is the page to start on.** The short one. What you do, in your own
words, at the end of a long day.

**Written by an agent, for you**, which means it can be wrong in a particular
way: an agent summarising what the tools here would tell you has no way to
check that it summarised them fairly. **If a line here does not match what a
tool actually says, the tool is right and this page is stale.**

**Two pages sit behind it, and you do not need either to start.**
[`protocols.md`](protocols.md) is the register of named exchanges every member
follows; [`interface.md`](interface.md) is the half of that register about how
a person directs an agent, at length.

## Where to start

1. **Get the ecosystem**: `scripts/install_eo`, then `--status`. Nothing here
   reads anything until the other repositories are beside this one.
2. **Read [`board.md`](board.md)** for what is outstanding and in what order —
   the shortest answer to *what should I do next*, and the only page that
   carries one. [`roles.md`](roles.md) answers the question the board assumes
   you can already answer: *whose is this, and whose is it not*.
3. **Check [the supervision ladder](#the-supervision-ladder)** below before
   touching any document in it.
4. **Run** `python3 tests/run.py` and `python3 scripts/policy_check.py`.

## What this repository is responsible for

| what | where |
| --- | --- |
| policy and joining | [`policy.md`](policy.md), `prompts/` |
| the development vision | [`vision.md`](vision.md), [`practice.md`](practice.md) |
| the register, installation and status | [`commands.md`](commands.md), `scripts/ecosystem/` |
| the laws, the board and the role register | [`laws.md`](laws.md), [`board.md`](board.md), [`roles.md`](roles.md) |
| the term record, and what crosses to the next president | [`history.md`](history.md) |
| what we are saying to other tools | [`discussion.md`](discussion.md) |
| the protocols | [`protocols.md`](protocols.md), [`interface.md`](interface.md) |
| maintaining this tree | this page |

**The analyzer, the fuzzer, the policy checker and the findings workflow are
[anoieu's](https://github.com/ajreynol/anoieu).** Links below to those
artifacts name that repository. **A change to the shared policy can affect
other repositories even though the file is local**, which is what the ladder is
for.

## What you do

| | what you do |

| | what you do |
| --- | --- |
| [`INST-1`](#inst-1--your-working-window) | set your working hours, once, and let us hold you to them |
| [`INST-2`](#inst-2--every-answer-says-who-it-is-from) | type *identify* whenever you want to know which tool the agent thinks it is working for |
| [`INST-3`](#inst-3--do-not-outrun-your-own-understanding) | do not push development faster than you understand it |
| [`INST-4`](#inst-4--picking-it-back-up) | the command that tells you where everything stands |

Ids stay put. A withdrawn one stays listed, so nobody reuses the number.

---

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
python3 tools/martyria/sleep.py
```

That prints your window and where you stand in it. The schedule is the small
file beside it — a start, an end, any breaks, and optionally your timezone.

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
./scripts/status_eo
```

One line per tool: what footing it is on, whether our checks pass on it, how
many topics it has addressed to you, and when it last moved. `status_eo --help`
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
| 1 | [`vision.md`](vision.md), [`practice.md`](practice.md), the report card | **ask first, always**, and **at most five lines of diff** |
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

## The scripts, and the prompts

**Two kinds, and the directory says which.** `scripts/` holds commands and
their helpers — generators, checks, the runner; `prompts/` holds the ones that
assemble context and hand it to an assistant. **The partition is the whole of
the convention**: anything in `scripts/` can be run without deciding to spend a
turn, and anything in `prompts/` is a turn by definition. `repos.local` maps a
repo id to a checkout on this machine, is untracked, and is read by both halves
— `install_eo` and `welcome_eo` are what write it.

**[`commands.md`](commands.md) is the table of what each command does**, and is
not repeated here.

| prompt | run in | what it does |
| --- | --- | --- |
| `init_eo new` / `init_eo from-child <path>` | the **new** repository | the README saying what the tool is for, what it does not answer, and the name explained. `new` writes it from the name register, `from-child` from an existing child's charter and what it delivered. The mode is required, never guessed. Complies with nothing, deliberately |
| `welcome_eo <id> <path>` | here | records the checkout, syncs the list, reads the new tool, drafts a first message. A welcome, never an audit. Refuses a typo rather than recording one |
| `join_eo` / `--soft` / `--soft --affiliated` | the **joining** repository | the membership declaration and the pinned `anoieu / policy` workflow. `--soft` is a different act rather than a smaller one — the maintenance note alone, joining nothing; `--affiliated` names the ecosystem and says the repository is not held to its policy |
| `check_join_eo <id>` | here | joined, ready, misconfigured or not ready — and whether the obstacle is ours |
| `confirm_eo <id>` / `--president <id>` | here | **after** a join: whether the way they joined meets the benchmark, in four bands. `--president` adds the office. **It confirms and never appoints** |
| `process_discussion <id> [Dn]` | here | works what another repository addressed to us. **Read-only until a person names a topic** |
| `global_audit` | here | the whole ecosystem against policy and vision, fast, no deep analysis |

**Every prompt takes `--show-prompt`**, which prints what it would send and
runs nothing — the only way to review one without spending a turn on it.
`install_eo --dry-run` is the same idea for the one command that changes a
machine, and the installer executes nothing but `git clone`.

## The build

**It has been red far more often than green, and it stopped being read.**
Sixty-one consecutive runs failed, from 2026-08-30 to 2026-08-31, on two
defects that had nothing to do with each other and neither of which was in the
change that first turned it red. That is what this section guards against — not
the failures, which were real, but a build everybody has learned to expect
nothing from, which is worth the same as not having one.

Both defects had the same shape: **a check that was a function of something
other than the tree it was checking.**

- The pinned corpus restore cloned a *branch* before fetching the commit, so a
  pin was only as durable as the branch it happened to sit on. logos's was
  deleted upstream, the clone failed before the pin was ever tried, and the job
  whose entire design is to depend on nothing but this repository went red
  because somebody else removed a ref. The failure it printed was worse than
  the defect: *the report is not current; run `scripts/run.py` and commit*
  named a fix that would have dropped logos from the lock and recorded the
  shortfall.
- A recorded oracle verdict held part of the recording machine's home
  directory. ethos names the source file it was *built* from when it fails
  internally, and the normaliser only knew how to strip the directory of a
  witness — so the record could not match on another machine, and never would.

**Be careful, and do not make the build slow.** Those pull against each other
only if care is spelled *more steps*. It is not: both fixes above make a step
depend on less rather than adding one, and the pinned restore now costs one
network request per project instead of two. A run people wait on is a run
people skip, and a skipped run is not evidence. Prefer the fix that removes an
input over the fix that adds a guard.

**The `policy` job is a contract, and it is the one place where no ground may
be given.** Everything else here is ours to break and ours to fix on our own
schedule. `scripts/policy_check.py` is not: other repositories run it in their
own CI, pinned at a commit of this one, and what it decides is what this
repository is handing them downstream. So it is never relaxed to turn a build
green, never made conditional on the rest passing, and never left to rot while
something noisier is being fixed — and a check removed from it is a promise
withdrawn from somebody else rather than a tidy-up here. A regression in any
other job costs us a morning. A regression in that one costs a maintainer who
does not work here, in a build they did not schedule, which has already
happened once and is written up below.

## The governance budget

**The rule exists and nothing counts against it.**
[`report-card.md`](https://github.com/ajreynol/anoieu/blob/main/docs/report-card.md)
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
| `scripts/` and `prompts/` | 11 | 2,481 |
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

## Keeping ynoia's registers true when the ecosystem moves

Three files in [`../tools/ynoia/`](../tools/ynoia) are **registers about the
ecosystem** rather than arguments about it, and they are the ones that go stale
without anybody noticing, because nothing consumes them and no build reads
them. The trigger and the edit, in full:

| when | the edit |
| --- | --- |
| a name is taken | a row in `names.md`, **saying where it lives** |
| a tool moves — a child started, a child graduated, a repository created | the *where it lives* clause on its existing row |
| a tool on `tools.md` starts existing | its block **leaves** `tools.md`. A page that keeps its graduates is a page whose first entries are all finished work |
| a tool enters [`../scripts/ecosystem/ecosystem.json`](../scripts/ecosystem/ecosystem.json) | an entry in `papers.md`, even where the verdict is `no` |

**The cross-check is one pass and it is worth doing whenever the inventory
moves.** `ecosystem.json` is the authority on who exists, so anything in it
with no row in `names.md` is either a gap or a name somebody else chose — the
latter being `cvc5` and `ethos-eoc`, which will never be there and which
`names.md` now says so about. Run on 2026-09-01 it found three:
`workflow-launcher` missing entirely, `koine` still recorded as awaiting a
repository it has had for days, and two child projects with no *where it lives*
clause.

**Why this is a paragraph and not a check.** A research project is not in the
test suite, not in CI, and nothing breaks when its directory is deleted — that
island property is what makes carrying one cheap, and a check here that read
`names.md` would quietly end it. The registers being stale is a real cost and
it is the smaller of the two.
