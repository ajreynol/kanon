# The protocols

**A protocol here is a named exchange with a shape somebody has to follow**,
and this is the register of them. They bind a member the way
[`policy.md`](policy.md) does, and they are separate from it for one reason:
**the policy says how a tree is arranged, and a protocol says how an exchange
is conducted.** A program can decide the first from a tree and can decide
almost none of the second.

**This is where a rule about what a president *does* goes.**
[`laws.md`](laws.md) governs the office and, by its own statement, the record
it keeps — so the ecosystem had a place for rules about a president's *record*
and none for rules about its *work*. These are those rules.

**`PROTO-1` to `PROTO-5`, `PROTO-17`, `PROTO-18` and `PROTO-21` are not here.**
They govern how a person directs an agent and live in
[`interface.md`](interface.md), which is one register in two files because the
audiences differ. **The numbers are a single namespace across both**, which is
most of the reason the scheme exists.

**Nothing on this page is checked.** A protocol is a shape an exchange takes,
and whether one was followed is a judgement. [`maintenance.md`](maintenance.md)
is where a person starts; this is the depth behind it.

## The scheme

**They are scattered across several pages and need a common label**, so that a
document referring to *the joining protocol* names a defined thing rather than
a phrase.

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
[`maintenance.md`](maintenance.md) and this register change most weeks and are
read by agents working here rather than by anybody depending on them. **A
protocol added is worth an aggregate line in a stretch and never its own.**

**The honest risk of all of this:** a tier system invites promotion by feeling
important, and **the pages most likely to be argued into the top tier are the
ones this repository is proudest of.** The dependency criterion exists to make
that argument lose.

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
