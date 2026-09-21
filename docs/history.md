# History — significant events from kanon's term

**This page records important events and what future maintainers can learn
from them.** It is a selective account of decisions, outcomes and mistakes
that changed the ecosystem's direction, responsibilities or way of working.

An event earns space here when understanding it could change a future
maintainer's decision. Explain what happened, why it mattered, what followed,
and what the experience supports or leaves uncertain. Keep enough evidence to
assess that account; a commit or project record is usually a reference, not a
story of its own.

Routine fixes, individual bug closures, board cleanup, file moves, formatting
changes, test counts and commit-by-commit summaries belong in Git and the
responsible project's records. Include such details here only when they are
necessary to explain a consequential event or a broader lesson. Completing a
task does not by itself warrant a history entry.

Related amendments to the laws, policy and vision are summarized together with
their reasons. Their detailed diffs remain in Git. Revise or consolidate an
existing account when that makes the experience clearer; this page does not
need an entry about each correction to itself.

This is kanon's account of its own term. It stays here when the presidency
moves, and does not bind a successor. Current work belongs on
[the board](board.md), current responsibilities in [the role register](roles.md),
and current membership in [the ecosystem register](../scripts/ecosystem/ecosystem.json).
The president may revise this account under
[Keeping and revising the term's history](laws.md#law-41--keeping-and-revising-the-terms-history).

## The term

Kanon took the presidency on **2026-09-15**, at commit `7eb9973`, when the
register assigned it the office and governance work moved out of anoieu.
The term remains open.

The purpose of that move was to reduce the concentration of governance and
implementation in the analyzer's repository. Kanon received the shared
documents, register and governance projects. Anoieu retained its analyzer,
fuzzer, findings workflow and policy checker. Later transfers distributed
shared commands to koine and assessment work to epikrisis and stathmos.

The office is bestowed by a person and gives no authority over somebody else's
repository. The shared laws and policy describe the arrangement members have
adopted. The events below concern what that arrangement enabled, what it cost,
and where its safeguards were insufficient.

## Decisions and their consequences

### Governance was distributed, but oversight did not become independent — September 15–18

The handoff separated responsibility for the shared policy from the analyzer
that had previously housed it. Shared commands subsequently moved to koine;
kanon retained the rules those commands implement. On September 18, stathmos
received status auditing, while anoieu retained the checking rules that member
repositories run. This distinguished setting policy, checking a repository,
and auditing the ecosystem's register.

The ethics projects martyria and zetesis moved to epikrisis on September 17.
That placed their work outside the presidency. Ynoia and stathmos were attached
to the presidency on September 18, so their work and assigned roles move with
that office. The laws were clarified to make transfer depend on each role or
project's recorded terms rather than assuming all work follows a president.

These changes made responsibilities easier to locate. They did **not** establish
independent oversight: repositories controlled by the same person remain under
the same control. Ynoia also carried the proposal that recommended kanon's
creation into kanon's own tree. Moving that proposal did not give its new host
independent standing to judge whether its own creation was justified.

The durable distinction is between distributing work and distributing
authority. The former happened; the latter cannot be inferred from directory
boundaries or separate repository names.

*Evidence:* the handoff at `7eb9973`, the transfer terms in
[roles.md](roles.md), and the account of shared control in [laws.md](laws.md).

### Transferring responsibility exposed the cost of removing a service early — September 17

Kanon transferred joining commands and dependency-update tooling to koine so
members could use shared implementations while kanon maintained the policy.
The joining-command copies were compared before deletion, establishing that
the move preserved their contents.

The installer was different: kanon deleted it while koine's replacement was
still being built. That created a real interval without an ecosystem installer.
The gap was a choice made here, not an obligation the prospective recipient had
failed to meet. This matters when interpreting a handoff: agreement about who
should maintain a service is not evidence that the receiving service is ready.

The role-transfer procedure was shortened the same day because its ordered
steps and duplicate board work had become a substantial part of the transfer
itself. Reversible decisions did not need the same ceremony as deletion.
The useful safeguard was checking the receiving artifact and identifying any
chosen service gap, rather than producing more acceptance documents.

*Evidence:* the September 17 transfers recorded in the role register's Git
history and the deletion history of `scripts/install_eo`.

### Rules accumulated faster than their purpose remained understandable — September 17–20

The working-hours mechanism had become four disconnected pieces: a rule for
members, a program in the president's tree, a divergent copy in an ethics
project, and an argument for it in another project. No reader could assemble a
clear account of how the arrangement was supposed to work. The maintainer
retired the mechanism on September 17. Whether agents should advise people to
stop working remained an open ethical question; deleting the machinery did
not answer it.

On September 18 the wider numbered protocol catalogue was retired. It had
grown to 7,181 words, largely restating rules or turning ordinary collaboration
into named procedures. Useful requirements were retained in their subject's
existing document. Mandatory announcements, identity headers, session reminders
and fixed approval blocks were removed. The reason was to make obligations
understandable where they apply, without requiring a second vocabulary of
procedures to interpret them.

The same problem appeared in overlapping documents and registers. `practice.md`
was folded into the vision on September 17, retaining its distinct arguments
and dropping repeated policy and inventory material. Ynoia's two proposal
registers became one on September 19. Proposals for this repository were
consolidated on September 20, retaining their questions and revisit conditions
without obsolete assignments or deadlines.

The lesson is that a new rule, document or register creates continuing reading
and reconciliation work. Its existence and internal consistency do not prove
that it helps. The governance budget in
[maintenance.md](maintenance.md#the-governance-budget) recorded reductions in
prose without corresponding new checks or findings; that distinguishes removal
of overhead from evidence of additional productive work.

*Evidence:* the [retired protocol catalogue](https://github.com/ajreynol/kanon/blob/f2262444e2d9dafa823820103fdaafac7252500a/docs/protocols.md)
and the surviving proposals in [brainstorm.md](brainstorm.md).

### A checker contract separated stable obligations from a fixed implementation — September 17–20

Anoieu introduced a versioned policy-checker contract and a shared CI workflow.
Policy accepted that form alongside a pinned checker commit, and kanon adopted
contract 1 on September 17. On September 20 the recommended setup led with an
explicit contract number while retaining commit pins as an accepted choice.

The contract lets checker repairs arrive without asking every repository to
advance a pin. The tradeoff is that a build can begin failing without a change
in the checked repository. A fixed contract is intended to keep the automated
obligations stable; it does not freeze the implementation or prove every new
failure correct. A hosted reusable workflow also needs hosted validation: a
local checker run does not establish that the CI integration works.

Policy was later reorganized to state member expectations before describing
checker coverage. Recommendations retain their advisory standing, and an
unimplemented check does not decide whether a written requirement exists.
Conversely, broad adoption of a convention did not authorize making its check
fatal. Rule adoption, checker coverage and observed compliance are separate
questions.

*Evidence:* [the accepted checking forms](policy.md#2-run-the-check), the
September 17 workflow change, and the September 20 policy amendments.

### Child projects may maintain shared work — 2026-09-20

The child-project policy replaced mandatory isolation with documented
boundaries. Children may supply shared artifacts, hold assigned roles, and
participate in their parent's imports, tests and CI without requiring a new
repository merely because their work is useful elsewhere. The parent still
carries cross-repository correspondence and commitments.

The reason was existing shared work: stathmos was already maintaining audits
used by its parent and the ecosystem. A rule that treated these dependencies
as exceptional made ordinary usefulness look like a breach of a child's
purpose. The revised policy asks projects to describe their interfaces and
responsibilities instead.

Anoieu's checker at `0b6ec54` still described shared dependencies as island
exceptions. Stathmos retained its explicit account of those interfaces while
policy moved ahead of that wording. This was a concrete instance of the
separation between a policy decision and its implementation in a checker.

*Evidence:* [the child-project policy](policy.md#child-projects) and
[stathmos's charter](../tools/stathmos/README.md).

### Public access was separated from permission to investigate — September 18–20

The maintainer revised the external-research rules because making source
available does not by itself invite this ecosystem to examine or track it.
Released work without published research, or with unknown publication status,
is treated as private under the resulting rules. An owner may volunteer an
exception; the offer and the actual release and publication facts must be
recorded separately.

Defect investigations were brought under the same eligibility rules as
tracking. Research boundaries remained with aisthesis's account rather than
being duplicated as a catalogue in the laws. Public reporting and contact
were delegated to anoieu's reporting policy, and a request to stop ends both.
The maintainer separately permitted private continuation subject to the
external-research rules. That permission does not cancel a stop on publication
or contact.

On September 20 the investigation rules were clarified to reach all external
footings, not just entries labelled outsider. Being listed in the register is
not consent; the evidence required by the external-research rules is what
establishes the basis for an external investigation.

The important boundary is between information being accessible, work being
permitted, and results being publishable. Combining those into one status
would conceal decisions that have different grounds and can change separately.

*Evidence:* [external research](laws.md#law-9--external-research-release-publication-and-permitted-comparisons)
and [investigations](laws.md#law-10--investigations-declaring-conducting-and-ending-one).

### Existing investigations became explicit commitments — September 20

Following epikrisis's question about investigation standing, the maintainer
extended the laws to internal public investigations of members and recorded
five existing external investigations. Membership supplies the internal basis;
external investigations depend on the research evidence described above.
Children act through their parent's footing and responsibility.

The register now records who is investigating what, the responsible maintainer,
the scope and basis, the start and declaration dates, and what would close the
work. Investigation state and reporting state are separate, so continuing
privately after public reporting stops can be represented. Several pursuers
may investigate one target, and closed records remain recorded.

The declarations were made on September 20; the recorded work had begun
earlier. Distinguishing those dates prevented a new administrative record
from claiming the work itself was new. The accompanying audit checks the
basis against current membership and research evidence because a basis may
lapse without the investigation record changing. An empty register is not
evidence that no investigation is happening.

Whether a public-interest disclosure can outweigh a request to stop was left
unsettled. Recording the question did not create an exception.

*Evidence:* the investigation records in
[ecosystem.json](../scripts/ecosystem/ecosystem.json) and the September 20
amendments to [the laws](laws.md).

### Accountability was distinguished from authorship and ownership — September 19–20

Policy first centralized the ecosystem's human-maintainer list to avoid stale
copies of personal attribution. The maintainer then narrowed what that list
means: it identifies responsibility for the shared arrangement, not the local
maintainers or authors of every participating project.

The laws require a public, current accountability record while leaving the
names in a maintained document rather than embedding them in a law. Project
credits belong in `AUTHORS` or an established equivalent. Contributors to
member repositories do not thereby adopt responsibility for the ecosystem,
and naming an accountable person neither grants ownership nor supplies a
licence.

The initial blanket ownership-link rule needed correction because one list
was being made to answer different questions. A shared accountability record
is useful only when it does not imply authority over other people's projects
or erase their own credit and maintenance arrangements.

*Evidence:* [human maintainers](policy.md#human-maintainers),
[author credits](policy.md#authors), and the September 20 amendments.

### Membership gained a question about contribution — September 19

The maintainer added a requirement that members, the president and recorded
children have a basis for being productive: a deliverable, a purposeful
reference in the central documents, or an assigned role. Other footings are
outside that requirement. Children are considered separately from their
parents, including children not advertised on the parent's front page.

The change made a project's contribution a question the register's footing
alone could not answer. The audit can report available evidence, but a link
or artifact's presence does not establish its value. Unavailable evidence
remains unverified; the report neither changes membership nor adds a CI gate.
This limits the temptation to turn an easily counted proxy into a judgement
about a project's worth.

*Evidence:* [productive entities](laws.md#law-11--productive-entities) and
[the tooling inventory](../scripts/ecosystem/ecosystem_tooling.json).

### Governance requirements were made less dependent on their current form — September 17–20

Several related amendments reduced the coupling between rules and their
current documents or implementation. The laws stopped listing incidental
filenames and counts as transfer conditions. Role and project transfer terms
identify what moves with the presidency. The board and role register transfer
with the office; each president's history and successor letter stay with
their authoring repository.

History requirements were relaxed on September 18: the president may revise
its account during the term, and length is guidance rather than a build gate.
The successor letter records experience without giving its recipient
instructions. The obligation to record shared-document amendments with their
reasons remains, but editorial revisions were grouped and the laws' headings,
references and structure simplified to make the requirements readable.

The shared policy was narrowed around repository conventions. Layout advice
became conditional on a project's needs, with dedicated deliverable directories
recommended and supporting directories distinguished from contributions.
Optional maintenance, discussion and brainstorming guidance was limited to
repositories maintained by agents under human supervision. Internal prompting
instructions and a blanket FAQ recommendation were removed from shared policy.
Handoffs need not create a discussion file, and repositories need not repeat
the shared explanation of what that file is.

The reason across these changes was to avoid creating obligations merely
because a template contains a folder or the current implementation uses a
particular path. They also reduced the chance that shortening a document
would silently change who owes what. The exact editorial sequence is in
`git log -p -- docs/laws.md docs/policy.md docs/vision.md`.

## What went wrong

### Structure and self-criticism displaced work

Before the term began, kanon opened six proposed offices in an afternoon and
could not explain four of them. It produced substantial governance prose
without implementation, duplicated an existing governance budget with a private
measure, and later rediscovered criticism already recorded elsewhere.
The maintainer deferred the offices; their containers were removed and the
useful questions retained in [brainstorm.md](brainstorm.md).

The failure was to treat a name, directory or careful account of a problem as
evidence of work accomplished. The same pattern affected an early proposal
that dokimasia should assess kanon because its name suggested scrutiny.
Dokimasia's actual work was cvc5 analysis; the proposed assignment did not
follow from that work.

Reading a project's scope and looking for an actual consumer would have tested
these proposals sooner. A thoughtful criticism of unnecessary governance can
itself become more unnecessary governance if it produces only another account
of the criticism.

### Appointment preceded readiness to hold the office

The register named kanon president on September 15 before this account
existed. For roughly fifteen hours the status audit correctly reported that
the repository lacked a document the office required. The check was working;
the handoff had still been made before the receiving tree was ready.

This exposed a limit of retrospective checks. A clear warning makes the state
visible, but it does not complete the preparation or decide whether the
appointment should be reversed. The person making a handoff still has to
establish that the receiving repository can carry it.

### Repeated descriptions drifted apart

Preparations for the handoff found six documents describing kanon without
agreeing about its standing. Later, members' declarations changed before the
central register caught up, and outdated claims survived in proposal pages
after the work they described had moved or ended. Online comparison found
some of these discrepancies; a green local check did not establish that the
cross-repository descriptions agreed.

The lesson was broader than correcting any one row. A decision should have
one authoritative home, and other documents should refer to it instead of
maintaining parallel accounts of the present. Kanon retained a human-maintained
register because footing is a decision; audits compare evidence with that
record and cannot make the decision themselves.

This account is subject to the same risk. It records dated experience, while
the board, laws and registers carry current arrangements. Repeating their live
task lists here would create another source of drift.

### Local checks missed interfaces used by other repositories

A reorganization in anoieu separated declaration readers from the checker
launcher that stathmos imported. One status-audit mode crashed; another
reported that the newer checker lacked a capability it actually had. A guard
written for an older implementation gave a misleading explanation when an
interface moved.

The failure was found on September 18 by exercising the command's modes, and
regressions were added for the affected integration. Separately, a document
move left cross-repository links broken even though neither repository's local
link checks resolved those links.

The shared failure was a gap between the boundary users depended on and the
boundary tests covered. Passing a provider's local tests did not establish
that its consumers still worked. The useful response was to check those
interfaces and state what remained unverified, rather than interpreting local
green results as evidence about the whole ecosystem.

### More correspondence did not mean more questions were settled

On September 18 an initial attempt to answer twenty-two incoming topics
created six bundled replies totalling 619 lines. Most of the topics asked for
an artifact to be corrected, so the extra replies duplicated answers that
belonged in the artifacts themselves and more than doubled the discussion file.

Reading each topic's settling condition changed the response. Artifact edits
settled the corresponding requests; only questions requiring an explicit
statement needed a reply. Three replies totalling 109 lines remained. Choices
about policy, membership or register structure that needed the maintainer's
decision were left for that decision rather than answered by an agent's assent.

This showed that activity in a communication channel is a poor proxy for work
settled. It also kept two separate outcomes visible: preparing a reply is work
in this repository, while carrying it to somebody else remains a person's act.

## Questions this term leaves open

The significant uncertainties are about the arrangement's effects, rather
than individual tasks still waiting on the board:

- Did distributing governance reduce the burden on the projects doing the
  technical work, or mainly move that burden between repositories?
- What would make oversight independent when a person controls both the work
  and the repository assessing it?
- Does the amount of governance make important decisions easier to understand
  and act on? Reducing prose is evidence of a smaller reading burden, not by
  itself evidence of better outcomes.
- Who should decide succession or handle a vacancy, and what evidence would
  justify moving the presidency again?
- How should term accounts support a continuing history without each president
  copying the same registers or selectively carrying forward favourable events?

The [laws](laws.md) identify the unresolved institutional questions; the
[board](board.md) holds current work. This account supplies experience with
which a later reader can assess them. It does not decide the successor's agenda
or turn the predecessor's conclusions into obligations.
