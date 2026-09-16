# Coherence

**If you are an agent working on this repository, start here.** This is the
maintenance entry point: what this repository is responsible for, which of that
may not be changed without asking, and what the open technical work is. Read it
before editing anything; everything else is reachable from it.

It is deliberately **not linked from the front page**. `README.md` is for
somebody deciding whether the tool is worth their attention, and a page about
how the work is run is noise to them — see *The front page* in
[`../docs/vision.md`](vision.md). It is linked instead from the things a
maintainer opens: the front page's index, and the headers of the programs that
write the record.

*Coherence* is the property this page exists to protect, in one sentence: **the
record, the documents and the tree do not disagree with each other.** A finding
that is open in one file and closed in another, a verdict resting on a fix that
never landed, a document describing an arrangement the code stopped using —
each is a coherence failure, and each has happened here.

## Before you start: a prompt may not be for this tree

**Check that the prompt you were handed is about the repository you are
standing in.** These trees are deliberately alike and several sit side by side
on one disk. A path that is not here, a role this repository does not hold, a
register kept elsewhere, or a question about anoieu's own standing are the
signs, and *"I don't think this prompt is meant for me"* is an acceptable
answer — say which repository it looks meant for, say what said so, and stop.

**In moderation.** Stop only if you can name the repository it was meant for;
if you cannot, it is for you, so do the work and do not narrate the check. The
full rule, and the incident that produced it, are in
[`policy.md`](policy.md#a-prompt-may-not-be-for-this-repository).

## What this repository is responsible for

**[`maintenance.md`](maintenance.md) is the entry point** and carries the
boundary table, where to start, and what you do. This page is the depth behind
it: the protocols, and the rules that govern changing anything a member is held
to.

## Protocols, and how they are labelled

**A protocol here is a named exchange with a shape somebody has to follow.**
There are a dozen, they are scattered across seven pages, and until now they
had no common label — so a document could refer to *the joining protocol* and a
reader could not tell whether that was a defined thing or a phrase.

**The scheme is `PROTO-n`, and the ugliness is the point.** A bare letter would
collide: `R` already means both a role and a request, `P` is a proposal, `D` a
discussion topic, and prose is full of stray capitals. `PROTO-7` cannot be
mistaken for anything, reads unambiguously and **greps unambiguously**.

**The number is permanent and is never reused.** A protocol that is retired
keeps its id in this table with a line saying so, because other pages cite it.

**They stay where they live.** This is a register, not a home: a protocol is
defined on whichever page owns its subject, and moving them all here would put
the definition further from the work. What this table adds is that they can be
named.

| id | protocol | between | defined in |
| --- | --- | --- | --- |
| `PROTO-17` | **the emergency protocol** — one word stops the direction; recency alone justifies a rollback, and a rollback is a forward change that never rewrites history | person → agent | [`interface.md`](interface.md) |
| `PROTO-1` | response clarification — *your answer was too hard to follow* | person → agent | [`interface.md`](interface.md) |
| `PROTO-2` | prompt clarification — *do not act on what you do not understand* | agent → person | [`interface.md`](interface.md) |
| `PROTO-3` | going off the deep end — *this cannot be checked from here* | agent → person | [`interface.md`](interface.md) |
| `PROTO-4` | temporal session coherence — the session's open ask survives its branches | agent → person | [`interface.md`](interface.md) |
| `PROTO-5` | the context protocol — say concretely what changed, not what it means | agent → person | [`interface.md`](interface.md) |
| `PROTO-6` | the reporting workflow — a defect carried to whoever owns the file | repository → repository | [`reporting-workflow.md`](https://github.com/ajreynol/anoieu/blob/main/docs/reports/reporting-workflow.md) |
| `PROTO-7` | the discussion file — everything that is not a defect report | repository → repository | [`policy.md`](policy.md) |
| `PROTO-8` | joining, and its soft and affiliating forms | repository → ecosystem | [`policy.md`](policy.md) |
| `PROTO-9` | retired, 2026-09-15 | — | no active protocol |
| `PROTO-10` | the role handoff — a responsibility changes hands, keeping its id | tool → tool | [`roles.md`](roles.md) |
| `PROTO-11` | the documentation handoff — a launch moves a description to its source | page → page | this page |
| `PROTO-12` | updating the report card | agent → person | `tools/stathmos/protocol.md` |
| `PROTO-13` | the mid-stream commit note — a commit taken while work moved | agent → record | this page |
| `PROTO-18` | **the sleep protocol** — outside the human's declared window the agent says *take a break*, once, and does the work anyway. Binds every member and changes nothing in anybody's tree | agent → human | [`interface.md`](interface.md) |
| `PROTO-19` | retired, 2026-09-15 | — | no active protocol |
| `PROTO-20` | **the handoff protocol** — a stub is deleted only once a spawned repository has proved it is what it claims. CI green on both sides, non-negotiable; any hint of fraud, reject | spawned repo → anoieu | this page |
| `PROTO-21` | **the identify protocol** — **every** response opens with the entity the agent acts for, its mission, and **which AI is answering, by name**. The long form at session start and on request | agent → human | [`interface.md`](interface.md) |
| `PROTO-22` | **the misc protocol** — a document too expensive to clean up now is demoted to `docs/misc/` rather than deleted or left misrepresenting itself. Discouraged, and a growing `misc/` is a symptom | page → layout | this page |
| `PROTO-23` | **the downstream refresh** — fetch and read another repository before making a claim about it, and say how far behind you were | us → downstream | this page |
| `PROTO-24` | **the upstream refresh** — a member makes its copy of the shared arrangements current before relying on them, and only onto a green commit | member → us | this page |
| `PROTO-25` | **the joke protocol** — humour lives on the president's front page and nowhere a machine parses or a stranger reads for instructions. Any tool may say *that's not funny*, meaning *you are confusing everyone*, and it ends there | any tool → any tool | this page |
| `PROTO-26` | **transferring roles** — a role moves when it is marked, the target exists, and **both** repositories' CI is green. Theirs is a person's check, not a job | us → another project | this page |
| `PROTO-27` | retired, 2026-09-15 | — | no active protocol |

**`PROTO-18` is the first entry addressed to every member rather than to
anoieu**, because the thing it is about — a person working at four in the
morning — does not happen in one repository. **It is also the entry that asks
least of them: its whole content is one sentence said to a person, and a member
that honours it changes no file.** The mechanism is maintained by
[martyria](../tools/martyria/README.md), which is where its ethics are argued
and its schedule lives.

## `PROTO-26` — transferring roles to another project

**Roles move when both repositories are in order, and *both* is the word doing
the work.** Ours and theirs. The check is `scripts/transfer_check.py`, and CI
carries it as a **report** rather than a gate.

### What has to be true

1. **The role is marked.** A role destined for another project carries a
   `Destined for` line in [`roles.md`](roles.md). **A transfer nobody wrote
   down is an intention, not a pending move**, and the marker is what the check
   reads.
2. **The target exists.** In the inventory, with a repository. **A stub is not
   a destination** — it is a note saying one is expected.
3. **Our CI is green**, which the job enforces by depending on the others: it
   cannot report while anything else is red.
4. **Their CI is green**, which **cannot be established from here.**

### Why the fourth is a person's step and not a job

**Asking GitHub about somebody else's build from inside our build would make
our CI fail for reasons in somebody else's tree.** [`policy.md`](policy.md)
names that as how a suite becomes noise, and it applies to us first. So the
check reports *unverified from here* and a person runs it with `--online`
before anything moves.

**Unverified is its own outcome and is not a pass**, with its own exit code,
for the same reason the bump gate has three: *we asked and it is wrong* and *we
could not ask* are different facts.

### Why it reports rather than gates

**Not every proposed transfer is ready**, so a job that failed on that would be
red while a human decision or handoff is still pending. **A check that is red
for months trains everybody to ignore red**, and then the checks that matter
are ignored too. The job is named for what it does: it produces a report, and
**a green tick on it means only that we looked.**

**It becomes a gate the day it can pass**, and that day is the day the roles
move.

## `PROTO-25` — the joke protocol

**A president keeps a joke about its own name on its front page, and that is
where humour stops.** [LAW 6](laws.md) puts it there; this protocol keeps it
there.

**Why the vision says to enjoy this.** The ecosystem requires every president
to keep that joke for a whole term and gives any tool a veto over it. **Those
two rules only make sense if enjoying this is a goal**, and a goal that governs
rules belongs in the vision. The practical reading: work that is no fun is work
somebody does briefly and then stops doing carefully. **A project nobody enjoys
does not fail loudly; it stops being maintained**, and every other tenet fails
quietly with it. **Have fun where it costs nothing, and nowhere else.**

**Any tool may say *that's not funny*, and that ends it.** The objection is
never about taste — it means **you are confusing everyone**: a reader arrived,
met a joke, and left less sure what the tool does. It is honoured without
argument, by whoever put the joke there, and **nobody explains the joke**. The
objector owes no evidence, because one confused reader is the whole of the case
and is the only person who can report it. An objection that turns out to be
wrong has cost one joke; **an unraised one costs every reader after it.**

**Where humour may not go at all**, not subject to judgement and not to a good
enough joke: anything a machine parses; anything a stranger reads to find out
what to do, since **a joke in a diagnostic costs somebody a debugging session**
and they will never know it was a joke; the policy, the checks, and any
document a member is held to; and anything about somebody else, which this
protocol never covered.

**The one that earns its place** is the joke that *is* the description. anoieu
is *eunoia* backwards and reads as *annoy you*, which tells a stranger what the
tool does in three words. **If removing the joke loses nothing, it was never
doing any work.**

## `PROTO-23` — the downstream refresh

**Before saying anything about another repository, make your copy of it
current.** Fetch, check how far behind you are, and read the tree rather than
your own notes about the tree.

**The failure this catches is confident and wrong.** A claim about somebody
else's tree, made from a stale checkout or from a sentence we wrote about them
last week, reads exactly like a claim made from reading it — and this
repository has already published one. `noesis` sat in our register as *free to
take* while eudaimonia was running it, and the register said so for as long as
nobody looked.

**Three things, and it is a minute's work.**

1. **Fetch, and say how far behind you were.** `0` is a result worth reporting;
   it is the difference between *checked* and *assumed*.
2. **Read the thing itself**, not our summary of it. Their README argues its
   own case, and it may argue against what you are about to propose — as
   epikrisis's does.
3. **Say when you could not.** A repository not on this machine is a gap in the
   claim, not a detail. **Not checkable and checked-and-fine are different
   facts**, and only one of them is a pass.

**It applies hardest when the claim is critical.** Proposing that somebody
reorganise their tree, reporting a defect against them, or recording their
status in our inventory are all claims about a thing we do not control.

## `PROTO-24` — the upstream refresh

**The mirror, and it is a member's protocol rather than ours.** Before relying
on the ecosystem's shared arrangements, a member makes its copy of *them*
current: pull the policy, re-run the checker, and check whether the commit it
pins is still the one it means.

**Its own failure mode is the more expensive of the two.** A member acting on a
policy that moved is not merely out of date — **it is complying with a rule
nobody publishes any more**, and it will pass its own checks while doing so.

**What it costs us, which is the part that is ours.** A member cannot refresh
against a moving target. **Every change we publish is a refresh somebody else
has to perform**, and that is the real price of an edit to a shared page —
argued in [`policy.md`](policy.md). Keep changes reviewable and avoid
unnecessary churn for members.

**And a member may only bump to a commit where our build is green**, which is
where this protocol meets [`PROTO-20`](#proto-20--the-handoff-protocol) and the
handoff standard: **refreshing onto a red commit spreads a failure instead of
adopting a change.**

## `PROTO-22` — the misc protocol

**`docs/misc/` is where a document goes when cleaning it up properly would cost
more than it is worth today.** Demotion, not deletion: the page keeps working,
every link to it keeps resolving, and **nothing is lost.**

**It is a discouraged practice and the page says so.** The good outcome is that
a document is cleaned up, merged into the page it should have been part of, or
argued out of existence. `misc/` is what you do when none of those will happen
this week and the alternative is leaving the front of the documentation
misrepresenting what is load-bearing.

**What demotion means.** The document is still maintained, still linked, still
checked. **What changes is the claim the layout makes about it**: it is no
longer offered as one of the places a question is answered.

**What it must never be.** A place to put something to avoid arguing about it,
a way to keep a page that should be deleted, or a holding pen that fills up
because demoting is easier than deciding. **A `misc/` that grows is a symptom,
not a filing system** — the count belongs in the health assessment, and a
directory nobody has emptied in a year is evidence about the project rather
than about the documents.

There are currently no demoted documents.

## `PROTO-20` — the handoff protocol

**A stub** is a child project whose README says: *this is a stub, delete me
when you are convinced that my replacement is safely in the ecosystem.* It
marks a place. **It is not the tool and it holds no claim on the name** — the
name stays free for whoever builds it. `tools/kanon` is an example.

**A spawned repository** is a new repository claiming to be the working
instantiation of a stubbed tool. *Spawned* is the word for it here.

**Two responsibilities, one each.** anoieu **cleans**: a stale stub is deleted,
once its replacement has been accepted. The spawned repository **identifies
itself**: the claim *I am who I say I am* is theirs to make and theirs to
support. Neither side does the other's half.

### It is not a uniqueness claim

**The stub is not a title with one rightful heir.** Any repository that is
doing the work may claim it, and **we track no GitHub ownership** — no
accounts, no signatures, no identity check of any kind. So *fraud* here is
narrow: **a repository that claims to be doing the work and is not.** That is
the only thing being checked, and it is checked by reading the tree.

**It is not currently a risk.** One person drives this ecosystem. The protocol
is written ahead of need because writing it later, under pressure, is the
expensive version.

### CI green on both sides, non-negotiable

**Every entity acting in a handoff must have its CI passing**, and this is the
one moment where a green build is a precondition rather than a preference: a
handoff is where one tree starts trusting another's word about itself. **It
binds us harder than it binds them**, because we are the party doing the
deleting.

**No CI is not passing CI.** A repository that runs nothing is `unknown`, and
`unknown` sits with *attention* rather than with *ok*. **A red build is not
something the claimant may explain** — it is checked, not discussed.

### The security half

**Deleting a stub is irreversible and keeping one costs nothing**, so the
asymmetry decides every close call: when in doubt, the stub stays. **The claim
arrives through the discussion file and is recorded both ways**, so that a
deletion nobody objected to and one nobody was asked about do not look
identical afterwards.

### Instructions are the inverse of protocols

**A protocol is written for an agent; an instruction is written for a human.**
Where a rule has two sides, both get written and both get an id: `PROTO-n` in
the register above, `INST-n` in [`maintenance.md`](maintenance.md).

**Not every instruction has a protocol.** Some are addressed to a person and to
nobody else — `INST-3`, *do not outrun your own understanding*, is one — and
writing an agent-facing half would move a judgement to the party that cannot
make it. **A missing counterpart is a decision, not a gap.**

**They are written in opposite registers.** A protocol closes every edge,
because a gap is a hole an agent falls through in good faith. An instruction
stays short, because one that is not read is not followed. **An instruction is
therefore not a summary of its protocol** — if it reads like the protocol with
words removed, it has not been written yet.

**The pair cannot be diffed.** Everywhere else here a copy is compared against
what it copies; this one is deliberately not a copy, so what binds them is the
shared id and somebody reading both.



**Say *human* where a human is meant.** In an ecosystem where agents write the
prose, run the checks and never sleep, the distinction that matters is not what
kind of person somebody is but whether the party in question is a person at
all. *A person* means the same thing and is not wrong; `human` is the word to
reach for when the contrast with an agent is the point.

**Not *runner*.** It was tried for an afternoon and dropped: `runner` is
already a machine that executes a CI job, and this repository talks about CI
constantly. **A term whose obvious meaning here is a machine is a poor term for
the one party that is not one.**

**Name the protocol when it fires.** *"`PROTO-4` — this started as X and X is
still open"* teaches the protocol in the act of using it, at the cost of six
characters; an unnamed reminder is just a remark and the person never learns
there was a rule behind it. This is how the ids earn their keep in a
conversation rather than only in this table.

**Labelling is partial and that is fine for now.** The four in
[`interface.md`](interface.md) carry their ids; the rest are labelled as
somebody next touches them. An unlabelled protocol is not a defect — a protocol
that has drifted from this row is.

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

## What happens when we add a new tool to the ecosystem

A new tool is a decision, and `welcome_eo` is what turns the decision into the
files. The sequence, which nothing enforces:

1. Somebody creates the repository, and [`init_eo`](../prompts/init_eo) gives
   it a README. **There are two ways a tool arrives here and the script makes
   you say which**, because there is no default that is safe: `init_eo new` for
   a repository with nothing in it, and `init_eo from-child <path>` when the
   tool already exists as a child project in somebody's tree and a person has
   decided it graduates — the first of the three endings a child project can
   have. The second is not the first with an extra file to read. It writes the
   README from that directory's charter and from its record of what it
   delivered, because **that record is the reason the repository exists**, and
   it is told not to move the child's own front page across: a child project's
   README is written to say the work is speculative and depended on by nobody,
   which is the opposite of what graduating means. The register is what the
   name is checked against in both, rather than where the scope comes from in
   either.
2. [`welcome_eo <id> <path>`](../prompts/welcome_eo) is run here, once there is
   something worth reading. It records the checkout in `scripts/repos.local` —
   the file every other script resolves an id through — **and syncs the
   ecosystem's own list**, by running `scripts/install_eo --status <id>` and
   printing what comes back, before it reads the tree and drafts a first
   message.
3. That sync reports and never edits. If the tool is not in
   [`../scripts/ecosystem/ecosystem.json`](../scripts/ecosystem/ecosystem.json)
   it says a status is owed, and a person adds the entry: `status`, `repo`,
   `url`, `what` — plus `vetted` and `why` where the footing is `associate`,
   because a footing that rests on our judgement carries the date somebody made
   it and what they made it about. Membership is a decision a person makes,
   which is why no script writes that file. **A child project** — a tool inside
   somebody else's tree, like `ethos-eoc` at `ethos/tools/eoc` — takes `status:
   child` with `parent` and `path` instead of a `repo` and a `url`: nothing
   clones it, it arrives with its parent, and its id still resolves to the
   parent's checkout so the other scripts can take it. Where the child's
   current work is on another branch of the parent, `branch` says which. A
   child is **listed** by `status_eo` and the installer's generated summaries
   according to its local README introduction's `**Eunoia listing:**
   advertised` or `unadvertised` declaration. For advertised children the
   installer repeats the branch advice without acting on it. An absent
   declaration means advertised, while IDs still resolve to the parent. [The
   listing rules](commands.md#child-project-listings) describe the choice and
   the explicit `--all-children` inspection view. A *name* with no work behind
   it does not earn a row — the register in
   [`../tools/ynoia/names.md`](../tools/ynoia/names.md) is where those live,
   and an install that advertised them would be a list of things to go and not
   find.
4. **The entry is the whole of the work.** `install_eo` derives what to clone
   from the inventory, so a new repository appears in the dump, in `--status`,
   and in `scripts/repos.local` on the next machine with nothing else edited.
   Outsiders are never cloned; children choose whether to appear in generated
   listings through their own README declaration.
   [`../scripts/ecosystem/checkouts.json`](../scripts/ecosystem/checkouts.json)
   carries only what cannot be derived — a clone flag, or a tree nobody should
   fetch unasked. The ordinary case needs none of it.
5. `join_eo` and `check_join_eo` come later, or never. Joining is its owner's
   choice, and a tool that never joins is still in the inventory.

**What the sync is there to prevent** is a tool that exists only on the machine
of whoever welcomed it: recorded in `repos.local`, absent from the inventory,
and missing from every other checkout. `welcome_eo` is where it is caught
because that is the one moment somebody is already thinking about the new tool.

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

## A finding is about `main`

We report a defect against what a project ships. Every ref in
[`../scripts/deps.json`](https://github.com/ajreynol/anoieu/blob/main/scripts/deps.json)
is a branch somebody else's users get, and a finding measured on a topic branch
is one its owner can close by deleting the branch.

That is not hypothetical. `logos-2` was measured against `updateCompiler` and
held open for four days, because the accepted fix sat in a working tree on a
branch level with `main`. The branch was then deleted, and with it any way of
asking what the report had been a report of. The finding had in fact landed;
the row survived the confusion only because its id had been written down.

**The exception is ethos-eoc, and the branch is `ethosEoc3`.** ethos-eoc is not
a repository: it is a **child project in the ethos tree**, at `tools/eoc`, and
it is developed on `ethosEoc3`. The compiler and the semantics sets the
ecosystem is built on are there and are not on ethos's `main`, so that branch
*is* the shipped thing for that tool — which is the test an exception has to
pass. It is not an exception for being where the work is convenient to read.
ethos's own `main` is still where the Eunoia manual is read from, and findings
against the checker are against `main`. `ethosEoc3` contains `main` in full, so
measuring the tree there measures `main` and the compiler work on top of it;
when the branch merges, the ref in
[`../scripts/deps.json`](https://github.com/ajreynol/anoieu/blob/main/scripts/deps.json)
becomes `main` and the exception is gone rather than renegotiated.

**And the exception does not reach `install_eo`, which installs a default
branch and nothing else.** Every command it prints is a plain `git clone`: no
`-b`, no checkout, no branch switch. A child project is not a checkout
obligation — it is a directory in somebody else's tree and it arrives when that
tree does — so ethos installs normally and the install *says* that the copy of
`ethos-eoc` on the default branch is the older one, with the command that gets
the newer:

git -C ethos checkout ethosEoc3          # or a worktree, to keep both

Which is the whole of the accommodation: a fact stated where somebody will read
it, and a branch nobody is put on without choosing it. The branch is recorded
on the **child** in
[`../scripts/ecosystem/ecosystem.json`](../scripts/ecosystem/ecosystem.json),
because it is a fact about the child rather than about the repository — ethos's
own default branch is not wrong, and a checker finding is still measured there.

A second exception is a decision, and it is written down here with its reason
or it is not made. A branch named in somebody's *reply* — `anoieu-findings`,
say — is where a fix is read before it lands; it is never what a finding is
measured against, and [what closes a
row](https://github.com/ajreynol/anoieu/blob/main/docs/reports/reporting-workflow.md#what-closes-a-row-and-what-does-not)
is a separate question with its own answer.

## The primary scope, and what follows from it

**[`vision.md`](vision.md) states it in one line: a solver as fast as cvc5,
statically verified to be correct.** The argument is here because that page
takes claims and not their justifications.

**It is the sharpest thing this ecosystem has said about itself**, and it is
sharp in the way that matters: **it can fail.** A solver that is verified and
slow does not meet it. A solver that is fast and unverified does not meet it.
**Both halves at once is the whole of the difficulty**, and it is why
[`pathos`](../tools/ynoia/tools.md) — a checker that is both — is named in the
register and unbuilt.

**Everything else here is instrumental to that, including this page.** The
analyzer, the fuzzer, the policy, the protocols, the offices, the laws: none of
them is the point. **They exist because the point is far away and somebody has
to keep the path legible in the meantime.**

**What the scope excludes, which is the useful half.** Work that makes the
documentation better without making the solver faster or more verified is
overhead — justified overhead, sometimes, and still overhead. **A stretch that
produced 1.54 MB of markdown and no movement on either axis has spent itself on
the instrument rather than the subject**, which is the measurement the incoming
president attached to its own term.

**And it explains the standing debt.** cvc5 is seventeen years and 14,064
commits of solver. **We are proposing to match it and prove it**, which is
either a long project or the wrong project, and the honest position today is
that we do not know which. **Nothing in this repository has yet made a solver
faster.**

## Promoting a document: when a change becomes an event

**Most documents here change constantly and none of it matters to anybody
else.** A few change and somebody outside has to do something about it. **The
difference is not importance and it is not length — it is whether anybody
depends on the page.**

**A document is promoted when something outside this repository rests on it.**
That is the whole criterion, and it is close enough to checkable to argue with:

- **Another repository is held to it.** `policy.md` is the case — a member's CI
  runs the checker that decides it.
- **Another repository quotes it.** `reporting-policy.md` is shared with
  dokimasia, so a change there changes a position somebody else publishes.
- **A tool consumes it as ground truth.** The joining prompt in `policy.md` is
  compared against its executable copy by the suite.
- **Or it governs everything else here**, which is `vision.md` and `laws.md`
  and nothing else.

**Promotion is recorded when it happens, and is rarer than it sounds.** No
document has been promoted yet; the four tiers above were assigned by looking
at what already depends on what. **The first real promotion will be a page
nobody depended on acquiring a consumer**, and that is the moment to notice,
not whenever a page feels significant.

### The code documentation that qualifies, and the rest that does not

**One thing, and it is not prose: the set of checks a member's CI runs.**
`scripts/policy_check.py` executes in three other repositories. **Adding a
check changes what somebody else's build does, and removing one changes what it
stops catching** — both are events in the ordinary sense, and neither is
visible in a document unless we write it down.
[`checks.md`](https://github.com/ajreynol/anoieu/blob/main/docs/checks.md) is
generated from the registry, so the page is not the event; **the check is.**

**What does not qualify, and would clog the record if it did:**
[`usage.md`](https://github.com/ajreynol/anoieu/blob/main/docs/usage.md) and
[`fuzzing.md`](https://github.com/ajreynol/anoieu/blob/main/docs/fuzzing.md)
describe an interface nobody outside runs;
[`notes.md`](https://github.com/ajreynol/anoieu/blob/main/docs/notes.md) is
miscellany by construction; [`interface.md`](interface.md),
[`coherence.md`](coherence.md) and this ecosystem's protocol register change
most weeks and are read by agents working here rather than by anybody depending
on them. **A protocol added is worth an aggregate line in a stretch and never
its own.**

**The honest risk of all of this:** a tier system invites promotion by feeling
important, and **the pages most likely to be argued into the top tier are the
ones this repository is proudest of.** The dependency criterion exists to make
that argument lose.

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

## Defending the infrastructure

The policy, the checker, the joining flow, the discussion protocol, the pin and
the proposal audit are **not a proposal any more.** They have been used, by a
repository other than this one, and the record of what they did is short enough
to state and specific enough to argue with.

**A second repository adopted the policy and runs the check in its own CI.**
dokimasia declared membership, wired the workflow, and went red — on a defect
in *our* checker, not in their tree: twenty-two link failures, every one
spurious, caused by a rule of ours that resolved a child project's own
documentation from the wrong root. They declined to work around it, cited the
sentence on our own page that says a check firing on a non-problem is ours to
fix, and left the links alone. We fixed it, added a regression test, and their
build went green without them changing anything.

That episode is the strongest evidence available that the arrangement works,
and it is worth being precise about why: **the first outside run of the checker
found a defect in the checker**, surfaced it through the channel built for it,
and cost the other party an afternoon that we then owed them. Every part of
that was designed and every part of it fired.

**Four topics have come through the protocol, and three changed what we do.**
The link resolution. The joining step, which pinned nothing and made every
member's build a function of a repository they do not own — the sharpest
sentence anyone has sent us is theirs, that a build which can turn *green*
without a commit cannot be evidence that a commit was good. And the naming
convention, which was a hard failure that every real candidate failed and was,
on inspection, a suggestion about readability. The fourth produced an audited
proposal, an approved repository and a name.

### What defending it means

**Removing a piece is a decision with a burden of proof, not a tidy-up.** The
cases are on record; if a rule is in the way, name the case, because there is
now a place to put that argument and somebody on the other end who will answer
it.

**The pieces interlock, and that is not decoration.** A declaration is
worthless without a check; an unpinned check can change a member's build
without a commit in their tree; a pin identifies the exact checker adopted; and
the discussion protocol gives members a way to challenge a check.

**The failure mode is treating this as overhead during a rush.** Infrastructure
is cheapest to delete at the moment it is most load-bearing, and an agent under
time pressure is well placed to make that trade badly and describe it as
simplification.

### And the honest limit

**Adoption is still small.** The
[inventory](../scripts/ecosystem/ecosystem.json) records current membership,
and [the history](history.md) records each change to it. Experience with this
group does not establish that the arrangement coordinates forty repositories,
and each adopter so far has found things the ones before it did not.

**It has not been free.**
[`report-card.md`](https://github.com/ajreynol/anoieu/blob/main/docs/report-card.md)
records that the stretch of work which produced most of this changed nothing
about what the analyzer finds, and introduced two silent defects into the
fuzzer — one of which would have let CI pass while verifying nothing at all.
Defending the infrastructure is not claiming it was cheap, and the case for it
rests on what it has done for other repositories rather than on what it has
done for this one.

## Adding a check

The checker is the one thing here that runs on other people's builds, so a
check is not a change to this repository — it is a change to theirs. It lands
permanently, it fires at moments nobody chose, and it is nearly never deleted.
Four conditions before one goes in.

**It is decidable without an opinion.** If answering it requires judgement, it
belongs in [`vision.md`](vision.md) and must never acquire a checker.

**It has been run against a tree we did not write.** Every false positive so
far was found by somebody else's repository and none by ours, which is not
luck: this is the one repository shaped like the checker's assumptions. Run a
new check against every candidate checked out on the machine before it lands. A
check that has only ever seen this tree has not been tested.

**Its message names the fix.** A failure a maintainer has to interpret costs
more than the defect it found, and they are reading it in a red build on
somebody else's schedule.

**It stays true without curation.** The expensive kind is the check whose
*data* rots — a list of vendor names, a registry of tools, anything that must
be updated as the world changes rather than as the tree does. There is one of
those already, the vendor list, and it is the check most likely to be wrong a
year from now. Prefer checks whose only input is the repository in front of
them.

### Why this is a limit and not a ritual

The failure mode is drifting into maintenance mode: a set of checks large
enough that keeping it honest is the work, and forward progress stops. Three
things make that happen, and they are worth naming because each looks like
diligence.

**A check that fires wrongly costs more than it can ever save.** It costs
somebody else an afternoon, and it costs us the credibility of the whole set —
a maintainer who has been sent one spurious failure reads the next one
differently, including the true ones.

**Every check is a migration.** A repository that passes today and fails
tomorrow has to do work it did not ask for, at a moment it did not choose.
Pinning makes that survivable; it does not make it free, and *we do not pay
it.*

**Checks accumulate and are almost never removed.** So the question at the
point of adding one is not *is this true* but *will I defend this in a year, on
somebody else's repository, when it fails inconveniently.* If the answer is
anything short of yes, it belongs in the minor tier, which is what that tier is
for — the naming convention is the worked example, a hard failure that every
real candidate failed and that was, on inspection, a suggestion about being
readable.

**And there is a stopping rule.** A check earns its place by finding something.
The anchor check found three dead links on its first run. A check that has
never fired on anything is either perfect or pointless, and the second is the
way to bet.

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

## The record's invariants, which are anoieu's to build

**Planning, not built, and not ours.** The findings record is edited mostly by
an assistant, and that has already gone wrong: a verdict of *fixed upstream*
was recorded three times for a fix that never happened, and nothing noticed for
months. The question the failure raises is not *how do we stop an agent editing
the record* but **what must remain true of it after any edit, whoever made it,
and which of those a machine can check.**

**The answer that matters is cheaper than enforcement.** Most of these
properties do not need a check so much as **not offering the chance to get them
wrong** — a script the agent is told to use, rather than a table it edits by
hand. A ledger command that moves a row and writes the verdict is the first
thing to build, and it removes the class of error rather than reporting it.

**The record, the ledger and the prompts that edit them live in
[anoieu](https://github.com/ajreynol/anoieu)**, and so does this work. It is
recorded here because kanon found the shape of it, and it is stated in a
paragraph rather than a design because **a design for somebody else's CI,
written in our tree and built by nobody, is the kind of page this repository
exists to stop accumulating.**
