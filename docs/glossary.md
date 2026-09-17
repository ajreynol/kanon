# Glossary

The dictionary of Eunoia’s project names, footings, and distinctive concepts,
and **the authoritative name register for the ecosystem**. This page records
names in use, what they mean, and which work they identify.
Each entry gives its kind and part of speech; project names give their footing
or parent. Statuses and assessment terms describe conditions, activities, or
judgements, not tools or projects.

**Maintained by the president of eo.** The president keeps the definitions
current and hands this file to the next president with the
[office’s shared documents](laws.md#what-the-office-carries).

Ynoia [argues about names](../tools/ynoia/proposals.md#arguing-about-names)
and proposes alternatives; it keeps no separate register and reserves no names
by proposing them. When a name enters use, the president records it here with
its meaning and source.
Absence from this page is not proof that a name is free: check the project
trees as well. The [inventory](../scripts/ecosystem/ecosystem.json) remains the
authority for membership and checkout locations; keep project labels here in
step with it.

Keep entries alphabetized without regard to case, spaces, or punctuation.
Include every existing child project, advertised or unadvertised, checking
the parent trees as well as the [inventory](../scripts/ecosystem/ecosystem.json).
Omit unused or merely reserved names, command and configuration identifiers,
operational protocols, AI and session-management terminology, and ordinary
English used in its usual sense. Locally named procedures belong in their
working documents, not this dictionary. Give a short definition and a source,
and distinguish an existing research project from an implemented tool.

Project descriptions and labels reflect the inventory and available project
READMEs read on **2026-09-17**. Including an unadvertised child here does not
change its listing preference. The linked sources govern their subjects;
outside projects listed for comparison did not ask to be measured and owe the
ecosystem nothing.

## A

**Alethe** (proof format; *proper noun*): A format for recording the proofs
SMT solvers produce, defined and maintained outside this ecosystem by its own
maintainers. Within the ecosystem it is **apodeixis**’s proposed target for
testing whether eudaimonia can support a calculus designed elsewhere, and that
work is paused pending its maintainers’ collaboration and permission.
[Apodeixis’s charter](https://github.com/ajreynol/eudaimonia/blob/main/tools/apodeixis/README.md)
records the ecosystem’s interest in it.

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

**arete** (assessment term; *noun*): Excellence in performing a thing’s function; in the report card,
what a tool does well and what others should learn from it. From Greek ἀρετή,
“excellence.” See [the report card](../tools/stathmos/report-card.md).

**associate** (footing; *noun*): A tool acknowledged as useful to the ecosystem without being
held to its policy. The proposed associate footing remains undecided and is held by
nobody. See [the associate protocol](policy.md#the-associate-protocol).

**autarkeia** (status; *noun*): The proposed state in which an ecosystem can develop a verified
SMT proof checker from one prompt naming the calculus and its purpose, without further
human intervention, with its proof obligations discharged and trusted base stated.
From Greek αὐτάρκεια, “self-sufficiency.” See
[eudaimonia’s definition](https://github.com/ajreynol/eudaimonia/blob/main/docs/autarkeia.md).

## C

**candidate** (footing; *noun*): The footing for a repository the ecosystem would like to join,
but which has not joined and owes nothing. It records our interest, not their consent.
See [the footings](policy.md#the-footings).

**candidate laws** (governance rules; *plural noun*): The voluntarily followed rules about footings and
the presidency. They are maintained by the party they bind and are not mechanically
enforced. See [the laws](laws.md).

**carcara** (Eunoia outsider; *proper noun*): An outside proof checker and elaborator
for Alethe, tracked for comparison. [Register](../scripts/ecosystem/ecosystem.json).

**child project** (project type; *noun*): Also **research project**: work on a potential tool housed
within a parent repository. It has its own purpose and inherits its parent’s footing.
See [child projects](policy.md#child-projects).

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

**dioktes** (status; *noun*): The state of a repository actively pursuing defects
in an outside tool, used in the phrase “in dioktes.” Declared by a person with a
closing condition; the pursuit ends if the target’s maintainers ask. It describes
the pursuing repository’s activity. From Greek διώκτης, “pursuer.” See [LAW
10](laws.md#law-10--in-dioktes-when-we-go-looking-for-defects-in-somebody-elses-tool).

**dokimasia** (Eunoia member; *proper noun*): The analyzer of cvc5’s proof-production code for
work with no proof step behind it. From Greek δοκιμασία, “scrutiny before office.”
[Register](../scripts/ecosystem/ecosystem.json).

## E

**elleipsis** (assessment term; *noun*): A shortcoming, with the evidence that establishes it; the
report-card field paired with arete and parainesis. From Greek ἔλλειψις, “a falling
short.” See [the report card](../tools/stathmos/report-card.md).

**empeiria** (Eunoia child project of dokimasia; *proper noun*): The project working on
cvc5 bug reports and learning from maintainer responses to improve the next fix.
[Charter](https://github.com/ajreynol/dokimasia/blob/main/tools/empeiria/README.md).

**eo** (abbreviation; *proper noun*): Short for Eunoia or the Eunoia ecosystem, according to context.
See [the front page](../README.md).

**epikrisis** (Eunoia member; *proper noun*): The auditor of how repositories change
over time, using evidence another reader can re-derive.
[Register](../scripts/ecosystem/ecosystem.json).

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

**footing** (ecosystem relationship; *noun*): A tool's recorded relationship to the ecosystem: member,
associate, president, candidate, foundation, child, or outsider. These describe
different obligations and claims, not ranks. See [the laws](laws.md) and [the
register](../scripts/ecosystem/ecosystem.json).

**foundation** (footing; *noun*): The footing for a project the ecosystem exists to serve. It
joins nothing, owes nothing, and is subject to no constraint imposed by this
arrangement. See [the footings](policy.md#the-footings).

## H

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

## I

**IsaRARE** (Eunoia outsider; *proper noun*): An outside tool that generates Isabelle
lemmas from RARE rewrite rules, tracked for comparison.
[Register](../scripts/ecosystem/ecosystem.json).

## K

**kanon** (Eunoia president; *proper noun*): The keeper of the ecosystem’s governance,
policy, vision, laws and registers, including what joining costs. From Greek κανών,
“the measuring rod.” [Register](../scripts/ecosystem/ecosystem.json).

**kanon-ball** (presidential request; *noun*): A request backed by the laws and addressed by kanon to one tool
in its discussion file. The name is the president's front-page joke, not an additional
power over the recipient. See [the joke](../README.md#a-joke-about-the-name).

**koine** (Eunoia member; *proper noun*): The keeper of the tooling no other tool
wants to maintain: the ecosystem’s bug database, the history-review tool, and the
commands that start and join a repository. From Greek κοινή, “the common tongue.”
[Register](../scripts/ecosystem/ecosystem.json).

## L

**Lean** (proof assistant; *proper noun*): The proof assistant used to express and
check the ecosystem’s formal proofs. See [logos’s roles](roles.md#logos).

**lean-smt** (Eunoia outsider; *proper noun*): An outside tool for discharging Lean
proof goals through SMT solvers, tracked for comparison.
[Register](../scripts/ecosystem/ecosystem.json).

**LFSC** (Eunoia outsider; *proper noun*): An outside proof checker tracked for
comparison. The register records its authors’ statement that it is deprecated.
[Register](../scripts/ecosystem/ecosystem.json).

**logos** (Eunoia member; *proper noun*): The Lean development containing the verified
CPC checker and its semantics. The L in the name denotes Lean.
[Register](../scripts/ecosystem/ecosystem.json).

## M

**martyria** (Eunoia child project of epikrisis; *proper noun; also noun*): 1. The project
taking stances on particular ethical situations from evidence of conduct. 2. A dated,
contradictable piece of that evidence. From Greek μαρτυρία, “testimony.”
[Charter](https://github.com/ajreynol/epikrisis/blob/main/tools/martyria/README.md).

**member** (footing; *noun*): A repository that has chosen to adopt eo’s shared policy and
approach. Membership carries obligations and may be left. See
[the footings](policy.md#the-footings).

**metagraphe** (Eunoia child project of tachyon; *proper noun*): The search for missing
cvc5 rewrites and simplifications for strings and bit-vectors, with small reproducible
examples.
[Charter](https://github.com/ajreynol/tachyon/blob/main/tools/metagraphe/README.md).

**mimesis** (Eunoia child project of eudaimonia; *proper noun*): Case studies and tutorials
teaching how to write Eunoia signatures and bring them into logos. From
Greek μίμησις, “imitation.”
[Charter](https://github.com/ajreynol/eudaimonia/blob/main/tools/mimesis/README.md).

**murxla** (Eunoia outsider; *proper noun*): An outside fuzzer that exercises SMT
solvers through their APIs, tracked for comparison.
[Register](../scripts/ecosystem/ecosystem.json).

## N

**noesis** (Eunoia child project of eudaimonia; *proper noun*): Research toward a verified
Eunoia compiler written in Lean, with explicit statements of what each pass preserves.
From Greek νόησις, “the act of understanding.”
[Charter](https://github.com/ajreynol/eudaimonia/blob/main/tools/noesis/README.md).

## O

**outsider** (footing; *noun*): A tool outside the ecosystem that is tracked for comparison and
is not proposed for promotion. Its released artifact and published contribution are
recorded separately, and neither imposes obligations on it. See [LAW
9](laws.md#law-9--released-is-not-published-and-tracking-respects-the-difference).

## P

**parainesis** (assessment term; *noun*): Counsel following an assessment: what should follow from a
tool’s strengths and shortcomings. From Greek παραίνεσις, “counsel.” See [the report
card](../tools/stathmos/report-card.md).

**president** (office; *noun*): The human maintainer of the repository recorded as holding the
presidency. The office is bestowed for a stretch, sets direction, maintains shared
governance including this glossary, and confers no control over another tree. See [LAW
3](laws.md#law-3--there-is-a-president).

## R

**research project** (project type; *noun*): Another name for a **child project**.

## S

**sapheneia** (Eunoia child project of kanon; *proper noun*): An account of Eunoia as a
language independent of one checker’s manual; ethos’s manual remains authoritative.
From Greek σαφήνεια, “clarity of an account.” [Charter](../tools/sapheneia/README.md).

**SMT-LIB** (language; *proper noun*): The shared language and theory vocabulary used
for solver inputs and the semantics modeled by logos. Eunoia uses its syntax to express
the formulas appearing in solver proofs. See [the language
account](../tools/sapheneia/manual.md#1-what-eunoia-is) and [the Lean model
role](roles.md#r18--the-model-of-smt-lib-semantics-in-lean).

**stathmos** (Eunoia child project of kanon; *proper noun*): The author of the report
card and keeper of its evidence. From Greek σταθμός, “a standard weight.”
[Charter](../tools/stathmos/README.md).

**stretch** (term of office; *noun*): The period for which a repository holds the presidency, also
called its term. The office expires with it; the account is kept during it. The laws
prescribe no fixed duration. See [LAW 3](laws.md#law-3--there-is-a-president).

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

## V

**vaporware** (status; *noun*): The vision's default status for a tool until a human chooses to
take responsibility for it. Existing code and a passing build do not make that decision.
See [the tenet](vision.md#4-until-a-human-decides-otherwise-the-tool-is-vaporware).

## W

**wishue** (project aspiration; *noun*): The goal a child project would pursue if the work went unusually
well, explicitly without committing to it. It belongs in the charter when there is one.
See [child projects](policy.md#child-projects).

**workflow-launcher** (Eunoia child project of eudaimonia; *proper noun*): The study of
the first hour of a new tool’s life: the decisions needed before a repository exists and
how to turn them into a useful starting point.
[Charter](https://github.com/ajreynol/eudaimonia/blob/main/tools/workflow-launcher/README.md).

## Y

**ynoia** (Eunoia child project of kanon; *proper noun*): The inquiry into whether the
ecosystem’s arrangement earns its machinery and what it lacks. Its name contracts “why
Eunoia.” [Charter](../tools/ynoia/README.md).

## Z

**zetesis** (Eunoia child project of epikrisis; *proper noun*): The inquiry into ethical standards
drawn from outside the ecosystem and whether its record could demonstrate that they were
met. From Greek ζήτησις, “inquiry.” [Charter](https://github.com/ajreynol/epikrisis/blob/main/tools/zetesis/README.md).
