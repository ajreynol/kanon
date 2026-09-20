# Brainstorm

**Proposals for consideration, with no assignment or commitment implied.**
Current responsibilities are in [roles.md](roles.md), active work is on
[the board](board.md), and adopted requirements are in [policy.md](policy.md)
and [laws.md](laws.md). The [maintenance instructions](#how-to-maintain-this-page)
explain the item format and when an idea leaves this page.

<a id="earlier-structure-proposal"></a>

## X1 — internal offices

**Status:** deferred
**Idea:** Organize recurring work into research, correspondence, safety and
ethics offices if those divisions make the work easier to own and use.
**Why:** Distinct responsibilities could help readers find an appropriate
reviewer or an answer, but extra directories can also duplicate the role
register and board.
**Open questions:** What output would each office provide, who would use it,
and which existing responsibility or document would it replace?
**Revisit when:** Recurring work exposes an ownership gap that the existing
role register and board cannot handle, and the maintainer reopens the proposal.

Kanon has no established internal offices. Child projects can remain directly
under `tools/`. The proposed range of three to five offices is deferred too;
any count would need a reason grounded in the work. A proposal would distinguish
organization that lasts for one term from services that continue across terms.

| possible office | question it would address | evidence that it would help |
| --- | --- | --- |
| Research | What should the ecosystem investigate, and who can answer it? | A question reaches the project with relevant evidence, without duplicating its analysis. |
| Correspondence | What are we sending, and what answer would settle it? | A reader can find the request, its recipient and its outcome. |
| Safety | How could documents or procedures lead to the wrong action? | A concrete scenario exposes a failure that can be reproduced or explained. |
| Ethics | What does this repository's conduct cost other people? | A record names the cost, the affected party and who could dispute the account. |

Research coordination would need a purpose beyond
[ynoia's inquiry](../tools/ynoia/README.md). Housing a project does not give an
office authority to decide its answers. Correspondence tracking could help a
sender choose its next step, but an unanswered question creates no duty to
reply and does not call for automatic nudges.

Safety review would concern procedures and documents, leaving code analysis to
the tools doing that work. Ethics review could examine self-assessment,
handoffs that change a directory without changing control, and costs imposed
on people who did not choose a process. Usability matters to both: an audit
nobody knows how to request can fail to affect decisions while working as built.

### Scenarios

These possible failure modes could give a safety office concrete work. They
are not claims that every mode is happening now or requirements for new controls.

| mode | how it could happen | what to examine |
| --- | --- | --- |
| Misinterpretation | A prompt targets another checkout, or two plausible documents disagree. | Can the reader identify the intended repository, the governing source and the conflict? |
| Deadlock | Two individually reasonable conditions each require the other to be satisfied first. | Trace the dependency cycle and identify who can decide how to resolve it. |
| Misappropriation | An account misstates who produced work, or a CI change makes unlike results appear comparable. | Check attribution, source revisions and what each recorded build established. |
| Exhaustion | Individually defensible additions produce more material than a maintainer can review. | Compare the review burden with the useful work the material supports. |
| Obfuscation | The text requires many unexplained identifiers or cross-references to understand. | Ask a reader to explain the action and its authority without reconstructing the whole ecosystem. |

Public history makes claims inspectable but does not by itself prove authorship
or correctness. In particular, a changed workflow can change what a green
result means. A useful review would distinguish changes in the work from
changes in the measurement, using recorded inputs, checker revisions and policy
contracts where relevant.

## X2 — make prompt intent and scope easier to establish

**Status:** exploring
**Idea:** Use clear repository names and a short statement of intent to reduce
mistakes when a maintainer works across similar checkouts and multiple sessions.
**Why:** A prompt can address another tree, and an agent can have the facts
right while misunderstanding what the tool is for. Conversation, the written
record and later recollection can diverge.
**Open questions:** Which signals reliably identify the intended scope, and
what evidence would show that an extra instruction helps?
**Revisit when:** A concrete routing or scope mistake reveals a gap in the
existing [prompting advice](maintenance.md#prompting-advice).

Possible signals include paths absent from the checkout, a role held elsewhere,
and a request concerning another project's register. Naming the target in the
first line may help; the useful question is what lets the maintainer resolve a
conflict, not how many instructions can be added.

A related concern is asking a project to argue for its own promotion, role or
publication. Asking what it could accept, with another party assessing the
proposal, may produce a more useful account. Connecting a small tool to a wider
ecosystem need not expand its responsibilities. These are working-practice
ideas, not a shared prompt banner or a new permission gate.

## X3 — resolve procedural deadlocks

**Status:** exploring
**Idea:** Examine interacting procedures for conditions that prevent any
participant from making progress, and describe possible ways to resolve them.
**Why:** An unavailable reviewer, an unverified observation and a rejected
proposal are different situations. Treating them as the same refusal can hide
a dependency cycle or leave no useful next step.
**Open questions:** Who has authority over each blocking condition, what
information is missing, and would an override or a revised procedure help?
**Revisit when:** A specific blocked workflow supplies a case to trace.

An override mechanism is one possibility to examine. A proposal would need to
say which decisions it covers, who may make them, what is recorded, and how
repeated overrides lead to revising the procedure. This page grants no general
power to bypass another repository's requirements.

<a id="synkrisis"></a>

## X4 — compare conflicting research agendas

**Status:** deferred
**Idea:** Describe conflicting agendas and useful connections between projects,
with each account grounded in their stated aims at named revisions.
**Why:** Work can overlap or pull in incompatible directions without the
relationship being clear to either project or to a prospective user.
**Open questions:** Can ynoia's existing inquiry answer these questions, and
would a separate comparison deliverable have a consumer?
**Revisit when:** A concrete comparison needs sustained work beyond the existing
inquiry, and a maintainer wants to consider a separate project.

*Synkrisis*, σύγκρισις — setting two things side by side — is a proposed name,
not an active child project or a claim on the name. The description would be
the deliverable. An opinion would be labelled separately, supported by the
account, and confer no authority over the projects being compared.

Starting questions to recheck against current sources:

- What do `telos`, `cvc6` and the proposed `pathos` each aim to deliver, and
  which aims actually compete?
- Do `noesis` and `ethos-eoc` offer complementary routes, overlapping
  implementations, or an intended replacement? What do their maintainers say?
- Could a presidency that starts without prior work have enough evidence of
  competence, and what shared services would need to stay elsewhere?
- Does a predecessor's suggested agenda help a successor understand the work,
  or make its conclusions too hard to question?

## How to maintain this page

Use one `## X<N> — <proposal>` heading per idea. Keep the fields in the template
below and add supporting reasoning only where it helps someone assess the
proposal. **The next unused id is `X5`.**

- Allocate ids above the highest ever used, including removed items in Git
  history. Reorder whole items as useful; never renumber or reuse an id.
- Use `exploring` for an idea being examined, `deferred` when its revisit
  condition is not met, and `ready for decision` when the proposal and its
  tradeoffs are concrete enough for a maintainer to assess. A status assigns
  no work and authorizes no action.
- Keep the open questions and revisit condition current. Date claims about
  other projects and distinguish observations from hypotheses.
- When an idea is accepted, record the decision in the document it governs
  and put any active work on the board. Remove settled, abandoned or superseded
  items; Git history preserves the discussion. Record policy amendments in
  [history.md](history.md).

### Item template

```markdown
## X<N> — <proposal>

**Status:** exploring | deferred | ready for decision
**Idea:** <the proposed change or inquiry>
**Why:** <the problem or opportunity, and who would benefit>
**Open questions:** <uncertainty, alternatives and tradeoffs>
**Revisit when:** <evidence or a condition that would make a decision useful>

<Only the supporting reasoning or references needed to assess the idea.>
```
