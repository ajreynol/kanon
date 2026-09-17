# Glossary

The dictionary of Eunoia’s names and shared vocabulary. Each entry gives its
part of speech; project names also give their footing or parent.

**Maintained by the president of eo.** The president keeps the definitions
current and hands this file to the next president with the
[office’s shared documents](laws.md#what-the-office-carries).

Keep entries alphabetized without regard to case, spaces, or punctuation.
Include every existing child project, advertised or unadvertised, checking
the parent trees as well as the [register](../scripts/ecosystem/ecosystem.json).
Omit unused or merely reserved names, command and configuration identifiers,
and general AI vocabulary. Give a short definition and a source, and distinguish
an existing research project from an implemented tool.

Project descriptions and labels reflect the register and available project
READMEs read on **2026-09-17**. Including an unadvertised child here does not
change its listing preference. The linked sources govern their subjects;
outside projects listed for comparison did not ask to be measured and owe the
ecosystem nothing.

## A

**advertised** (*adjective*): Included in normal ecosystem listings, as chosen by a
child project’s parent. The default when its readable README declares no preference. See
[listing rules](commands.md#child-project-listings).

**affiliating form** (*noun*): A maintenance note that names the Eunoia ecosystem while
explicitly declining its shared policy. It declares affiliation without membership. See
[affiliation](policy.md#the-soft-form-the-note-without-the-membership).

**Alethe** (proof format; *proper noun*): The proof format chosen as apodeixis’s
proposed test of whether eudaimonia can support a calculus designed elsewhere. See
[the project register](../scripts/ecosystem/ecosystem.json).

**anakrisis** (Eunoia child project of dokimasia; *proper noun*): The project reviewing
cvc5 pull requests through proof-completeness analyses before and after a change.
[Charter](https://github.com/ajreynol/dokimasia/blob/main/tools/anakrisis/README.md).

**anoieu** (Eunoia member; *proper noun*): The static analyzer, fuzzer, findings system,
and policy checker. Its name is Eunoia read backwards.
[Register](../scripts/ecosystem/ecosystem.json).

**apodeixis** (Eunoia child project of eudaimonia; *proper noun*): The project testing whether
eudaimonia can support a calculus designed elsewhere, with Alethe as its proposed
target. Paused pending collaboration and permission from Alethe’s maintainers.
[Charter](https://github.com/ajreynol/eudaimonia/blob/main/tools/apodeixis/README.md).

**approval block** (*noun*): A statement of the action a human is asked to approve and
the evidence supporting it. Reporting readiness does not grant approval. See [the
approval protocol](policy.md#the-approval-protocol).

**arete** (*noun*): Excellence in performing a thing’s function; in the report card,
what a tool does well and what others should learn from it. From Greek ἀρετή,
“excellence.” See [the report card](../tools/stathmos/report-card.md).

**associate** (*noun*): A tool acknowledged as useful to the ecosystem without being
held to its policy. The proposed associate footing remains undecided and is held by
nobody. See [the associate protocol](policy.md#the-associate-protocol).

## B

**bands** (*plural noun*): The report card's four judgements: **excellent**, **good**,
**fair**, and **poor**. Fair indicates room to improve; poor means the work runs against
the ecosystem's aims. There is no numerical formula. See [the
bands](../tools/stathmos/report-card.md#the-bands-the-axes-and-the-one-real-check).

**board** (*noun*): The ordered register of outstanding cross-repository work, with the
next step and the party whose move it is. Roles record responsibilities; the board
records work still to do. See [the board](board.md).

## C

**calculus** (*noun*): A system of symbols and proof rules expressed in a Eunoia
signature. CPC is the calculus around which much of this ecosystem is built. See [what
Eunoia is](../tools/sapheneia/manual.md#1-what-eunoia-is).

**candidate** (*noun*): 1. A repository invited to join that has not joined and owes
nothing. 2. An observation awaiting confirmation before it can be reported as a defect.
See [footings](policy.md#the-footings) and
[findings](vision.md#what-none-of-this-licenses).

**candidate laws** (*plural noun*): The voluntarily followed rules about footings and
the presidency. They are maintained by the party they bind and are not mechanically
enforced. See [the laws](laws.md).

**carcara** (Eunoia outsider; *proper noun*): An outside proof checker and elaborator
for Alethe, tracked for comparison. [Register](../scripts/ecosystem/ecosystem.json).

**charter** (*noun*): A child project's statement of its question, goals in order, any
wishue, and explicit limits. Starting the project or changing that scope is a human
decision. See [child projects](policy.md#child-projects).

**checkable** (*adjective*): Capable of having its claims re-derived by somebody who
does not trust their author; one of the report card’s three axes. See [the
axes](../tools/stathmos/report-card.md#the-bands-the-axes-and-the-one-real-check).

**child project** (*noun*): Also **research project**: work on a potential tool in a
parent's `tools/X/` directory. It is reached through its parent, inherits its footing,
and has its own charter. See [child projects](policy.md#child-projects).

**context protocol** (*noun*): The exchange in which an agent explains concretely what
changed so the human can follow the work. See [the
protocol](protocols.md#proto-5--the-context-protocol).

**CPC** (proof calculus; *proper noun*): The **Cooperating Proof Calculus**, maintained
as a Eunoia signature in cvc5. Its signature, semantics, and verification development
have different owners. See [the calculus role](roles.md#r8--cpc-the-calculus).

**cvc5** (Eunoia foundation; *proper noun*): The SMT solver that produces the proofs and
owns CPC. The ecosystem exists to serve it and asks it for nothing.
[Register](../scripts/ecosystem/ecosystem.json).

**cvc6** (Eunoia child project of eschaton; *proper noun*): An unadvertised proposal to
retain cvc5’s design and automate its refactoring and upkeep. A working title for
research notes; nothing is built, and it is not an announced successor from the cvc5
project. [Charter](https://github.com/ajreynol/eschaton/blob/main/tools/cvc6/README.md).

## D

**ddSMT** (Eunoia outsider; *proper noun*): An outside tool for reducing SMT-LIB
benchmarks to smaller cases that preserve the behaviour under investigation.
[Register](../scripts/ecosystem/ecosystem.json).

**delivered** (*adjective*): Having changed something outside the project through its
work; one of the report card’s three axes. See [the
axes](../tools/stathmos/report-card.md#the-bands-the-axes-and-the-one-real-check).

**demotion** (*noun*): Moving a document to `docs/misc/` when properly cleaning it up
costs more than it is worth now. Links remain usable, but the page is no longer
presented as a maintained answer. See [the misc
protocol](protocols.md#proto-22--the-misc-protocol).

**dioktes** (*noun*): A pursuit of defects in an outside tool, undertaken to test a
disputed claim. Declared by a person with a closing condition, it describes our activity
and ends if the target’s maintainers ask. From Greek διώκτης, “pursuer.” See [LAW
10](laws.md#law-10--in-dioktes-when-we-go-looking-for-defects-in-somebody-elses-tool).

**discussion file** (*noun*): The standing channel for requests, proposals, questions,
notices, and answers that are not defect reports. Topics have permanent ids and
settlement conditions; a person carries anything to another repository. See [the format
and rules](policy.md#the-discussion-file).

**distribution** (*noun*): The ecosystem's mission that no tool should hold what another
tool could. It concerns the allocation of responsibilities, rather than the number of
repositories alone. See [the vision](vision.md).

**dokimasia** (Eunoia member; *proper noun*): The analyzer of cvc5’s proof-production code for
work with no proof step behind it. From Greek δοκιμασία, “scrutiny before office.”
[Register](../scripts/ecosystem/ecosystem.json).

**downstream refresh** (*noun*): The practice of reading another repository’s current
state before making a claim about it, and stating how far behind the previous reading
was. See [the protocol](protocols.md#proto-23--the-downstream-refresh).

## E

**ecosystem** (*noun*): The tools built around Eunoia and their recorded relationships.
It includes more than members; dependencies used to build the tools are not
automatically part of it. See [the footings](policy.md#the-footings).

**elleipsis** (*noun*): A shortcoming, with the evidence that establishes it; the
report-card field paired with arete and parainesis. From Greek ἔλλειψις, “a falling
short.” See [the report card](../tools/stathmos/report-card.md).

**emergency protocol** (*noun*): The exchange in which a human stops the current
direction immediately and any rollback preserves the history of what happened. See [the
protocol](protocols.md#proto-17--the-emergency-protocol).

**empeiria** (Eunoia child project of dokimasia; *proper noun*): The project working on
cvc5 bug reports and learning from maintainer responses to improve the next fix.
[Charter](https://github.com/ajreynol/dokimasia/blob/main/tools/empeiria/README.md).

**eo** (*proper noun*): Short for Eunoia or the Eunoia ecosystem, according to context.
See [the front page](../README.md).

**epikrisis** (Eunoia member; *proper noun*): The auditor of how repositories change
over time, using evidence another reader can re-derive.
[Register](../scripts/ecosystem/ecosystem.json).

**escape hatch** (*noun*): A person's explicit, recorded override of a gate. The record
states what was overridden, what was known, and what would remove the need for the
override. An agent cannot take it independently. See [the
rule](policy.md#the-escape-hatch).

**eschaton** (Eunoia member; *proper noun*): The research project comparing approaches
to better-founded SMT solvers and the costs of trying them.
[Register](../scripts/ecosystem/ecosystem.json).

**ethos** (Eunoia candidate; *proper noun*): The fast C++ proof checker and home of the
authoritative Eunoia manual. Proposed as an associate; it has not joined as a member.
[Register](../scripts/ecosystem/ecosystem.json).

**ethos-eoc** (Eunoia child project of ethos; *proper noun*): The Eunoia compiler: turns
a calculus and its semantics into a proof checker and the obligations needed to
establish its soundness.
[Charter](https://github.com/cvc5/ethos/blob/ethosEoc3/tools/eoc/README.md).

**eudaimonia** (Eunoia member; *proper noun*): The calculus template that takes a
signature and supplies a checker and its proof development.
[Register](../scripts/ecosystem/ecosystem.json).

**Eunoia** (language; *proper noun*): The language for defining calculi and checking
solver proofs around which the ecosystem is built. From Greek εὔνοια, “good thinking.”
See [the language account](../tools/sapheneia/manual.md#1-what-eunoia-is).

**euthyna** (Eunoia child project of eudaimonia; *proper noun*): The study of what logos’s
proof development is made of and where its weight sits. From Greek εὔθυνα, “the audit at
end of term.”
[Charter](https://github.com/ajreynol/eudaimonia/blob/main/tools/euthyna/README.md).

## F

**finding** (*noun*): An observation produced by an analysis or check. A candidate
becomes suitable to carry as a defect report only after confirmation, reduction to a
small reproducer, and identification of the authority over the subject. See [reporting
limits](vision.md#what-none-of-this-licenses).

**folded** (*adjective*): Incorporated into its parent as the chosen ending of a child
project. See [child projects](policy.md#child-projects).

**footing** (*noun*): A tool's recorded relationship to the ecosystem: member,
associate, president, candidate, foundation, child, or outsider. These describe
different obligations and claims, not ranks. See [the laws](laws.md) and [the
register](../scripts/ecosystem/ecosystem.json).

**foundation** (*noun*): The footing for a project the ecosystem exists to serve. It
joins nothing, owes nothing, and is subject to no constraint imposed by this
arrangement. See [the footings](policy.md#the-footings).

**fruitful** (*adjective*): Useful to a named consumer outside the producing tool,
through an artifact the consumer can actually use. Evidence and negative results can
count; an artifact nobody consumes has not yet met the tenet. See [the fruitfulness
tenet](vision.md#1-evolve-to-be-fruitful-to-another-tool-as-quickly-as-possible).

## G

**genuine** (*adjective*): Constructed according to the shared policy from the
beginning, rather than brought into compliance afterwards; a judgement about history
that a person records. See [the register’s
definitions](../scripts/ecosystem/ecosystem.json).

**global announcement** (*noun*): A discussion topic about a change on the sender's
side, addressed explicitly to every member at that date. Its `Global` field says what is
owed; addressing the topic does not send it. See
[announcements](policy.md#pins-and-global-announcements).

**going off the deep end** (*verb phrase*): Pursuing an abstraction so far that the next
step cannot change anything concrete in a tree; the expression that names the protocol
for recognizing this drift. See [the
protocol](protocols.md#proto-3--going-off-the-deep-end).

**governance budget** (*noun*): The maintenance practice of measuring governance prose
against the technical work it displaces. It records evidence for later comparison rather
than setting a numerical page limit. See [maintenance](maintenance.md).

**graduation** (*noun*): A child project becoming a repository of its own, by human
decision. Its responsibilities transfer through a handoff and keep their role ids. See
[role handoffs](roles.md#how-a-role-is-handed-off).

## H

**handoff** (*noun*): A responsibility or artifact changing hands. A role keeps its id;
a launched tool receives its description at its source; a stub remains until its
replacement meets the handoff conditions. See [role
handoffs](roles.md#how-a-role-is-handed-off) and [the protocol
register](protocols.md#the-scheme).

**hawkeye** (Eunoia child project of eschaton; *proper noun*): An unadvertised proposal
to build a new SMT solver from nothing, mostly through autonomous agents. An intention
recorded in a page; nothing is built.
[Charter](https://github.com/ajreynol/eschaton/blob/main/tools/hawkeye/README.md).

**hermeneia** (Eunoia child project of eudaimonia; *proper noun*): The study of how
results about embedded SMT-LIB formulas can become statements in Lean’s own logic. From
Greek ἑρμηνεία, “interpretation.”
[Charter](https://github.com/ajreynol/eudaimonia/blob/main/tools/hermeneia/README.md).

**heuresis** (Eunoia child project of tachyon; *proper noun*): The investigation of quantified
benchmarks where z3 is much faster than cvc5, recording shortcomings worth a human’s
attention.
[Charter](https://github.com/ajreynol/tachyon/blob/main/tools/heuresis/README.md).

**history** (*noun*): The president's account of its own repository and stretch, kept
current in `docs/history.md`. It explains what commits alone cannot and remains in the
repository that wrote it. See [LAW
4](laws.md#law-4--the-president-writes-historymd-in-its-own-repository-and-a-letter-to-its-successor).

## I

**identify header** (*noun*): The opening line naming the entity an agent acts for, its
mission, and the AI model answering. It is a statement of the agent's understanding of
its role. See [the identify protocol](protocols.md#proto-21--the-identify-protocol).

**in dioktes** (*prepositional phrase*): Actively pursuing defects in an outside tool under
a declared investigation. See **dioktes**.

**in limbo** (*prepositional phrase*): Recorded as president while lacking the laws or term
account needed to carry out the office. See [the laws](laws.md#in-limbo).

**instruction** (*noun*): A rule addressed to the human directing the work, identified
as `INST-n`. Where an exchange has both human and agent duties, its instruction and
protocol describe the two sides. See [the maintenance
instructions](maintenance.md#what-you-do).

**inventory** (*noun*): The authoritative record of ecosystem projects and their
footings; also called the register or registry. See [the
inventory](../scripts/ecosystem/ecosystem.json).

**IsaRARE** (Eunoia outsider; *proper noun*): An outside tool that generates Isabelle
lemmas from RARE rewrite rules, tracked for comparison.
[Register](../scripts/ecosystem/ecosystem.json).

**island** (*noun*): The intended independence of a child project: it reads other work,
writes within its own directory, and can be removed without changing the parent's
behaviour or CI. Exceptions must be stated. See [child
projects](policy.md#child-projects).

## J

**joke protocol** (*noun*): The rule placing humour on the president’s front page,
outside machine interfaces and instructions, and ending a joke when a reader says it
confuses the work. See [the protocol](protocols.md#proto-25--the-joke-protocol).

## K

**kanon** (Eunoia president; *proper noun*): The keeper of the ecosystem’s governance, policy,
vision, laws, registers, and joining arrangements. From Greek κανών, “the measuring
rod.” [Register](../scripts/ecosystem/ecosystem.json).

**kanon-ball** (*noun*): A request backed by the laws and addressed by kanon to one tool
in its discussion file. The name is the president's front-page joke, not an additional
power over the recipient. See [the joke](../README.md#a-joke-about-the-name).

**koine** (Eunoia member; *proper noun*): The shared machinery of the reporting loop,
maintained so members need not implement it separately. From Greek κοινή, “the
common tongue.” [Register](../scripts/ecosystem/ecosystem.json).

## L

**law** (*noun*): A numbered statement about footings or the presidency in
`docs/laws.md`. The current laws are candidate laws: voluntarily followed and binding
people, not programs. See [the laws](laws.md).

**Lean** (proof assistant; *proper noun*): The proof assistant used to express and
check the ecosystem’s formal proofs. See [logos’s roles](roles.md#logos).

**lean-smt** (Eunoia outsider; *proper noun*): An outside tool for discharging Lean
proof goals through SMT solvers, tracked for comparison.
[Register](../scripts/ecosystem/ecosystem.json).

**ledger** (*noun*): A register of findings or candidate feedback, with the evidence and
state of each entry. A child's ledger remains local until a person carries an item
through the parent's reporting discipline. See [child
projects](policy.md#child-projects).

**legible** (*adjective*): Understandable to an arriving reader, beginning at the front
README; one of the report card’s three axes. See [the
axes](../tools/stathmos/report-card.md#the-bands-the-axes-and-the-one-real-check).

**letter to the successor** (*noun*): The outgoing president's account of what it got
wrong. It stays with its author's repository, is not governing documentation, and gives
the predecessor no authority over the successor. See [LAW
4](laws.md#law-4--the-president-writes-historymd-in-its-own-repository-and-a-letter-to-its-successor).

**LFSC** (Eunoia outsider; *proper noun*): An outside proof checker tracked for
comparison. The register records its authors’ statement that it is deprecated.
[Register](../scripts/ecosystem/ecosystem.json).

**limbo** (*noun*): The gap between bestowing the presidency and supplying the documents
needed to hold it. See **in limbo**.

**logos** (Eunoia member; *proper noun*): The Lean development containing the verified
CPC checker and its semantics. The L in the name denotes Lean.
[Register](../scripts/ecosystem/ecosystem.json).

## M

**maintenance note** (*noun*): The README section explaining how a repository is
maintained, including authorship, supervision, and any membership or affiliation
declaration. It is distinct from the fuller local `docs/maintenance.md`. See [the
policy](policy.md#the-maintenance-note).

**martyria** (Eunoia child project of kanon; *proper noun; also noun*): 1. The project
taking stances on particular ethical situations from evidence of conduct. 2. A dated,
contradictable piece of that evidence. From Greek μαρτυρία, “testimony.”
[Charter](../tools/martyria/README.md).

**member** (*noun*): A repository that declares adherence to the shared policy and runs
its pinned checker in CI. The footing also carries a judgement about sharing the vision,
which no program decides. Membership can be left. See [the
footings](policy.md#the-footings).

**metagraphe** (Eunoia child project of tachyon; *proper noun*): The search for missing
cvc5 rewrites and simplifications for strings and bit-vectors, with small reproducible
examples.
[Charter](https://github.com/ajreynol/tachyon/blob/main/tools/metagraphe/README.md).

**mid-stream commit note** (*noun*): A short note identifying commits taken while work
was still changing and what they actually contain. It explains a mismatch between a
commit message and its contents. See [the maintenance
contract](maintenance.md#the-supervision-ladder).

**mimesis** (Eunoia child project of eudaimonia; *proper noun*): Case studies and tutorials
teaching how to write Eunoia signatures and bring them into logos. From
Greek μίμησις, “imitation.”
[Charter](https://github.com/ajreynol/eudaimonia/blob/main/tools/mimesis/README.md).

**misc protocol** (*noun*): The practice of moving a document out of the maintained
account when cleaning it up is not worthwhile now. See **demotion** and [the
protocol](protocols.md#proto-22--the-misc-protocol).

**murxla** (Eunoia outsider; *proper noun*): An outside fuzzer that exercises SMT
solvers through their APIs, tracked for comparison.
[Register](../scripts/ecosystem/ecosystem.json).

## N

**noesis** (Eunoia child project of eudaimonia; *proper noun*): Research toward a verified
Eunoia compiler written in Lean, with explicit statements of what each pass preserves.
From Greek νόησις, “the act of understanding.”
[Charter](https://github.com/ajreynol/eudaimonia/blob/main/tools/noesis/README.md).

## O

**obfuscation** (*noun*): The failure mode in which the ecosystem's documents and
machinery become too hard for a human to understand. More written explanation can
contribute to the problem. See [the recorded inquiry](history.md).

**outsider** (*noun*): A tool outside the ecosystem that is tracked for comparison and
is not proposed for promotion. Its released artifact and published contribution are
recorded separately, and neither imposes obligations on it. See [LAW
9](laws.md#law-9--released-is-not-published-and-tracking-respects-the-difference).

## P

**parainesis** (*noun*): Counsel following an assessment: what should follow from a
tool’s strengths and shortcomings. From Greek παραίνεσις, “counsel.” See [the report
card](../tools/stathmos/report-card.md).

**policy** (*noun*): The shared rules about a repository's arrangement and declarations,
with mechanically decidable rules checked against its tree. Policy and its checker are
held separately. See [the policy](policy.md).

**policy checker** (*noun*): Anoieu's implementation of the mechanical policy checks,
pinned by members and invoked locally through kanon's launcher. It reports what it
cannot verify and does not grade the vision. See [the checker
role](roles.md#r31--the-policy-checker).

**president** (*noun*): The human maintainer of the repository recorded as holding the
presidency. The office is bestowed for a stretch, sets direction, maintains shared
governance including this glossary, and confers no control over another tree. See [LAW
3](laws.md#law-3--there-is-a-president).

**primary scope** (*noun*): The stated aim of a solver as fast as cvc5, statically
verified to be correct. Governance and tooling are means toward that aim. See [the scope
and its argument](protocols.md#the-primary-scope-and-what-follows-from-it).

**primed** (*adjective*): Prepared through conversation, with the repository’s purpose
documented before implementation; used especially of an incoming president. See [the
priming conversation](misc/conversation.md).

**promotion** (*noun*): For a child, graduation into a repository. For a document,
declaring that a change is significant enough for affected readers to be told, which
requires a human decision. See [document
promotion](protocols.md#promoting-a-document-when-a-change-becomes-an-event).

**prompt clarification** (*noun*): The exchange in which an agent identifies what it
does not understand before acting on a request. See [the
protocol](protocols.md#proto-2--the-prompt-clarification-protocol).

**proposal** (*noun*): In discussion, a suggestion made for the recipient's benefit. If
the sender wants something for its own benefit, it is a **request**. Research proposals
may also recommend a new tool without authorizing its creation. See [topic
kinds](policy.md#the-format).

**protocol** (*noun*): A named exchange with a defined shape, identified as `PROTO-n`.
Its permanent id is not reused after retirement. The register links each protocol to the
document that defines it. See [the protocols](protocols.md).

**published** (*adjective*): Made public as an intellectual contribution, as distinct
from releasing code. For outsider tracking, the contribution is recorded by citation.
See [LAW
9](laws.md#law-9--released-is-not-published-and-tracking-respects-the-difference).

## R

**register** (*noun*): A maintained account of a defined subject. “The register”
ordinarily means the ecosystem inventory; names, roles, and protocols have their own
registers. See [the inventory](../scripts/ecosystem/ecosystem.json).

**registry** (*noun*): Another name for the ecosystem’s **inventory** or **register**.

**released** (*adjective*): Made publicly available as code, whether or not its authors
have published an intellectual contribution. See [LAW
9](laws.md#law-9--released-is-not-published-and-tracking-respects-the-difference).

**report card** (*noun*): Stathmos's argued assessment of tools against the ecosystem's
tenets, with dated evidence and the fields arete, elleipsis, and parainesis. A person
may overrule it; it is not a mechanical check. See [the report-card
role](roles.md#r30--the-report-card).

**reporting loop** (*noun*): The process of recording, confirming, carrying, and
receiving answers to findings. Koine maintains shared machinery; the reporting tool
remains responsible for what it reports and what settles a finding. See [koine's
role](roles.md#koine) and [PROTO-6](protocols.md#the-scheme).

**request** (*noun*): A discussion topic asking another tool for something the sender
wants. The sender states its interest so the recipient can judge the cost and decline.
See [topic kinds](policy.md#the-format).

**research project** (*noun*): Another name for a **child project**.

**response clarification** (*noun*): The exchange in which a human says an answer was
too hard to follow and the agent restates it. See [the
protocol](protocols.md#proto-1--the-response-clarification-protocol).

**response gate** (*noun*): The discussion rule requiring a human to identify the topic
to act on, with the instruction and topic agreeing. Reading a discussion file does not
itself authorize a reply. See [the
gate](policy.md#the-gate-every-discussion-file-carries).

**retired in place** (*adjective phrase*): Ended as a child project, with a visible
account of what was learned and why the work stopped. See [child
projects](policy.md#child-projects).

**role** (*noun*): A responsibility with a permanent `R<n>` id, a holder, owned
artifacts, and explicit exclusions. It describes accountability; a child project
describes where work happens. See [the role register](roles.md).

## S

**same owner loophole** (*noun*): The limitation that dividing responsibilities among
repositories with the same owner does not divide authority among independent parties.
See [the laws' account](laws.md#the-same-owner-loophole).

**sapheneia** (Eunoia child project of kanon; *proper noun*): An account of Eunoia as a
language independent of one checker’s manual; ethos’s manual remains authoritative.
From Greek σαφήνεια, “clarity of an account.” [Charter](../tools/sapheneia/README.md).

**settles when** (*noun*): The discussion field stating what would close a topic. An
open topic requires an answerable condition, rather than an indefinite complaint. See
[the discussion format](policy.md#the-format).

**shared vision evolution** (*noun*): The process described in the priming conversation
in which a human teaches and corrects an agent's understanding of how a local tool
serves the wider purpose. This can protect a tool's narrow scope rather than expand it.
See [the conversation](misc/conversation.md).

**sleep protocol** (*noun*): The practice of reminding a human to take a break outside
their declared working window, once per session, while continuing to answer. See [the
protocol](protocols.md#proto-18--the-sleep-protocol).

**SMT** (*noun*): Satisfiability modulo theories, the class of reasoning problems
addressed by cvc5 and the solvers studied here. See [the
arrangement](../tools/ynoia/why-eunoia.md).

**SMT-LIB** (language; *proper noun*): The shared language and theory vocabulary used
for solver inputs and the semantics modeled by logos. Eunoia uses its syntax to express
the formulas appearing in solver proofs. See [the language
account](../tools/sapheneia/manual.md#1-what-eunoia-is) and [the Lean model
role](roles.md#r18--the-model-of-smt-lib-semantics-in-lean).

**soft form** (*noun*): A maintenance note that explains how a repository is maintained
without naming another project or declaring ecosystem membership. See [the soft
form](policy.md#the-soft-form-the-note-without-the-membership).

**spawned repository** (*noun*): A new repository claiming to implement a tool
represented by a stub. It must support that claim before the stub is removed; a reserved
name alone does not establish it. See [the handoff
protocol](protocols.md#proto-20--the-handoff-protocol).

**stance** (*noun*): Martyria's position on a particular ethical situation: what we
would do and what evidence supports it, or an explicit deferral. A stance does not send
a message or decide for another project. See [the charter](../tools/martyria/README.md).

**stathmos** (Eunoia child project of kanon; *proper noun*): The author of the report
card and keeper of its evidence. From Greek σταθμός, “a standard weight.”
[Charter](../tools/stathmos/README.md).

**stretch** (*noun*): The period for which a repository holds the presidency, also
called its term. The office expires with it; the account is kept during it. The laws
prescribe no fixed duration. See [LAW 3](laws.md#law-3--there-is-a-president).

**stub** (*noun*): A placeholder child whose README asks to be deleted when its working
replacement is safely in the ecosystem. It marks a place and holds no claim on a name.
See [the handoff protocol](protocols.md#proto-20--the-handoff-protocol).

**supervision ladder** (*noun*): The local ordering of changes by how much human
supervision they require, from vision changes through ordinary maintenance. It
identifies the decisions an agent does not make alone. See [the
ladder](maintenance.md#the-supervision-ladder).

## T

**tachyon** (Eunoia member; *proper noun*): The search for improvements to cvc5’s
performance through reproducible benchmark experiments.
[Register](../scripts/ecosystem/ecosystem.json).

**tekmerion** (Eunoia child project of anoieu; *proper noun*): The study of the evidence
behind claims in documentation. From Greek τεκμήριον, “conclusive evidence rather than a
mere sign.”
[Charter](https://github.com/ajreynol/anoieu/blob/main/tools/tekmerion/README.md).

**telos** (Eunoia child project of eschaton; *proper noun*): Research toward a solver
designed around proofs from the start, retaining cvc5’s calculus and parts of its
checker while replacing the search. Research notes; nothing is built.
[Charter](https://github.com/ajreynol/eschaton/blob/main/tools/telos/README.md).

**temporal session coherence** (*noun*): The practice of keeping the session's live request
visible and carrying it through side questions, without inventing additional work. See
[the protocol](protocols.md#proto-4--temporal-session-coherence).

**tenet** (*noun*): One of the five aims in the vision: be fruitful, move quickly with
CI, build clear self-contained tools, treat agent-built work as vaporware until a human
takes it on, and communicate. Tenets are argued, never mechanically graded. See [the
vision](vision.md#the-tenets).

**term** (*noun*): The period during which a repository holds the presidency; another
word for a **stretch**. See [LAW 3](laws.md#law-3--there-is-a-president).

**topic** (*noun*): One discussion entry with an addressee, kind, status, opening date,
and settlement condition. Standard ids are `D<n>` and are cited across repositories as
`<repo>-D<n>`. See [the format](policy.md#the-format).

## U

**unadvertised** (*adjective*): Omitted from normal ecosystem listings at the parent’s
choice. A child can still be inspected and appears in this dictionary. See [listing
rules](commands.md#child-project-listings).

**upstream refresh** (*noun*): The practice of bringing a member’s copy of shared
arrangements up to date before relying on them, using a version that passed its checks.
See [the protocol](protocols.md#proto-24--the-upstream-refresh).

## V

**vaporware** (*noun*): The vision's default status for a tool until a human chooses to
take responsibility for it. Existing code and a passing build do not make that decision.
See [the tenet](vision.md#4-until-a-human-decides-otherwise-the-tool-is-vaporware).

**vetted** (*adjective*): Examined by a person who stands behind a dated judgement of
what the tool is to the ecosystem. See [the footings](policy.md#the-footings).

**vision** (*noun*): The shared aims and argument for the ecosystem's development.
Policy is checked against a tree; vision is argued and no program may settle whether a
tool meets it. See [the distinction](vision.md#policy-is-checked-vision-is-argued).

## W

**wishue** (*noun*): The goal a child project would pursue if the work went unusually
well, explicitly without committing to it. It belongs in the charter when there is one.
See [child projects](policy.md#child-projects).

**workflow-launcher** (Eunoia child project of eudaimonia; *proper noun*): The study of
the first hour of a new tool’s life: the decisions needed before a repository exists and
how to turn them into a useful starting point.
[Charter](https://github.com/ajreynol/eudaimonia/blob/main/tools/workflow-launcher/README.md).

**working window** (*noun*): The hours a human declares for work, including any breaks,
used by the sleep protocol. The mechanism knows the clock, not how much work the person
has done. See [the instruction](maintenance.md#inst-1--your-working-window).

## Y

**ynoia** (Eunoia child project of kanon; *proper noun*): The inquiry into whether the
ecosystem’s arrangement earns its machinery and what it lacks. Its name contracts “why
Eunoia.” [Charter](../tools/ynoia/README.md).

## Z

**zetesis** (Eunoia child project of kanon; *proper noun*): The inquiry into ethical standards
drawn from outside the ecosystem and whether its record could demonstrate that they were
met. From Greek ζήτησις, “inquiry.” [Charter](../tools/zetesis/README.md).
