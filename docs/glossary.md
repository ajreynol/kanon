# Glossary

The dictionary of Eunoia’s project names, footings, and distinctive concepts,
and **the authoritative name register for the ecosystem**. This page records
names in use, what they mean, and which work they identify.
Each entry gives its kind and part of speech; project names give their footing
or parent. Statuses and assessment terms describe conditions, activities, or
judgements, not tools or projects.

**Maintained by the president of eo.** The president keeps the definitions
current and hands this file to the next president with the
[office’s shared documents](laws.md#law-32--transfers-with-the-office).

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

<a id="aisthesis"></a>
**aisthesis** (Eunoia member; *proper noun*): Two documents about the practice
of building this ecosystem rather than about the calculus: how that practice
relates to the state of the art, and where writing about the future stops being
a plan. From Greek αἴσθησις, “perception.”
[Repository](https://github.com/ajreynol/aisthesis).

<a id="alethe"></a>
**Alethe** (proof format; *proper noun*): A format for recording the proofs SMT
solvers produce, defined and maintained outside this ecosystem by its own
maintainers. Within the ecosystem it is **[apodeixis](#apodeixis)**’s proposed
target for testing whether [eudaimonia](#eudaimonia) can support a calculus
designed elsewhere, and that work is paused pending its maintainers’
collaboration and permission.
[Apodeixis’s charter](https://github.com/ajreynol/eudaimonia/blob/main/tools/apodeixis/README.md)
records the ecosystem’s interest in it.

<a id="anakrisis"></a>
**anakrisis** (Eunoia child project of [dokimasia](#dokimasia); *proper noun*):
The project reviewing [cvc5](#cvc5) pull requests through proof-completeness
analyses before and after a change.
[Charter](https://github.com/ajreynol/dokimasia/blob/main/tools/anakrisis/README.md).

<a id="anoieu"></a>
**anoieu** (Eunoia member; *proper noun*): The static analyzer, fuzzer, findings
system, and policy checker. Its name is [Eunoia](#eunoia) read backwards.
[Repository](https://github.com/ajreynol/anoieu).

<a id="apodeixis"></a>
**apodeixis** (Eunoia child project of [eudaimonia](#eudaimonia); *proper noun*):
The project testing whether [eudaimonia](#eudaimonia) can support a calculus
designed elsewhere, with [Alethe](#alethe) as its proposed target. Paused
pending collaboration and permission from Alethe’s maintainers.
[Charter](https://github.com/ajreynol/eudaimonia/blob/main/tools/apodeixis/README.md).

<a id="arete"></a>
**arete** (assessment term; *noun*): Excellence in performing a thing’s
function; in the report card, what a tool does well and what others should learn
from it. From Greek ἀρετή, “excellence.” See
[the report card](../tools/stathmos/report-card.md).

<a id="associate"></a>
**associate** ([footing](#footing); *noun*): A repository carrying no
front-page membership declaration, which **owes this ecosystem nothing** and
may record on its own `docs/maintenance.md` what it holds itself to. Its tree
is checked and the result printed as `N tracked` rather than `N failing`:
**a measurement, not a shortfall, with nobody at fault and nobody asked to
fix it.** `unadvertised-child` is the counterpart for a child its parent's
front page does not name. See [the footings](policy.md#the-footings).

<a id="autarkeia"></a>
**autarkeia** (status; *noun*): The proposed state in which an ecosystem can
develop a verified SMT proof checker from one prompt naming the calculus and its
purpose, without further human intervention, with its proof obligations
discharged and trusted base stated. From Greek αὐτάρκεια, “self-sufficiency.”
See
[eudaimonia’s definition](https://github.com/ajreynol/eudaimonia/blob/main/docs/autarkeia.md).

## C

<a id="candidate"></a>
**candidate** (footing; *noun*): The [footing](#footing) for a repository the
ecosystem would like to join, but which has not joined and owes nothing. It
records our interest, not their consent. See
[the footings](policy.md#the-footings).

<a id="candidate-laws"></a>
**candidate laws** (governance rules; *plural noun*): The voluntarily followed
rules about footings and the presidency. They are maintained by the party they
bind and are not mechanically enforced. See [the laws](laws.md).

<a id="carcara"></a>
**carcara** (Eunoia outsider; *proper noun*): An outside proof checker and
elaborator for [Alethe](#alethe), tracked for comparison.
[Repository](https://github.com/ufmg-smite/carcara).

<a id="child-project"></a>
**child project** (project type; *noun*): Also
**research project**: work on a potential tool housed
within a parent repository. It has its own purpose and inherits its parent’s
[footing](#footing). See [child projects](policy.md#child-projects).

<a id="cpc"></a>
**CPC** (proof calculus; *proper noun*): The **Cooperating Proof Calculus**,
maintained as a [Eunoia](#eunoia) signature in [cvc5](#cvc5). Its signature,
semantics, and verification development have different owners. See
[the calculus role](roles.md#r8--cpc-the-calculus).

<a id="cvc5"></a>
**cvc5** (Eunoia foundation; *proper noun*): The SMT solver that produces the
proofs and owns [CPC](#cpc). The ecosystem exists to serve it and asks it for
nothing. [Repository](https://github.com/cvc5/cvc5).

<a id="cvc6"></a>
**cvc6** (Eunoia child project of [eschaton](#eschaton); *proper noun*): An
unadvertised proposal to retain [cvc5](#cvc5)’s design and automate its
refactoring and upkeep. A working title for research notes; nothing is built,
and it is not an announced successor from the cvc5 project.
[Charter](https://github.com/ajreynol/eschaton/blob/main/tools/cvc6/README.md).

## D

<a id="ddsmt"></a>
**ddSMT** (Eunoia outsider; *proper noun*): An outside tool for reducing
[SMT-LIB](#smt-lib) benchmarks to smaller cases that preserve the behaviour
under investigation. [Repository](https://github.com/ddsmt/ddSMT).

<a id="dioktes"></a>
**dioktes** (status; *noun*): The state of a repository actively pursuing
defects in an outside tool, used in the phrase “in dioktes.” Declared by a
person with a closing condition under
[LAW 10.1](laws.md#law-101--declaring-a-pursuit); the pursuit ends if the
target’s maintainers ask under
[LAW 10.3](laws.md#law-103--ending-a-pursuit-on-request).
It describes the pursuing repository’s activity. From Greek διώκτης, “pursuer.”

<a id="dokimasia"></a>
**dokimasia** (Eunoia member; *proper noun*): The analyzer of [cvc5](#cvc5)’s
proof-production code for work with no proof step behind it. From Greek
δοκιμασία, “scrutiny before office.”
[Repository](https://github.com/ajreynol/dokimasia).

## E

<a id="elleipsis"></a>
**elleipsis** (assessment term; *noun*): A shortcoming, with the evidence that
establishes it; the report-card field paired with [arete](#arete) and
[parainesis](#parainesis). From Greek ἔλλειψις, “a falling short.” See
[the report card](../tools/stathmos/report-card.md).

<a id="empeiria"></a>
**empeiria** (Eunoia child project of [dokimasia](#dokimasia); *proper noun*):
The project working on [cvc5](#cvc5) bug reports and learning from maintainer
responses to improve the next fix.
[Charter](https://github.com/ajreynol/dokimasia/blob/main/tools/empeiria/README.md).

<a id="eo"></a>
**eo** (abbreviation; *proper noun*): Short for [Eunoia](#eunoia) or the Eunoia
ecosystem, according to context. See [the front page](../README.md).

<a id="epikrisis"></a>
**epikrisis** (Eunoia member; *proper noun*): The auditor of how repositories
change over time, using evidence another reader can re-derive.
[Repository](https://github.com/ajreynol/epikrisis).

<a id="eschaton"></a>
**eschaton** (Eunoia member; *proper noun*): The
[research project](#child-project) comparing approaches to better-founded SMT
solvers and the costs of trying them. From Greek ἔσχατον, “the last thing” —
which its own README reads as the finished proof, the end the design question
is asked backwards from.
[Repository](https://github.com/ajreynol/eschaton).

<a id="ethos"></a>
**ethos** (Eunoia candidate; *proper noun*): The fast C++ proof checker and home
of the authoritative [Eunoia](#eunoia) manual. Proposed as an
[associate](#associate); it has not joined as a [member](#member).
[Repository](https://github.com/cvc5/ethos).

<a id="ethos-eoc"></a>
**ethos-eoc** (Eunoia child project of [ethos](#ethos); *proper noun*): The
[Eunoia](#eunoia) compiler: turns a calculus and its semantics into a proof
checker and the obligations needed to establish its soundness.
[Charter](https://github.com/cvc5/ethos/blob/ethosEoc3/tools/eoc/README.md).

<a id="eudaimonia"></a>
**eudaimonia** (Eunoia member; *proper noun*): The calculus template that takes
a signature and supplies a checker and its proof development.
[Repository](https://github.com/ajreynol/eudaimonia).

<a id="eunoia"></a>
**Eunoia** (language; *proper noun*): The language for defining calculi and
checking solver proofs around which the ecosystem is built. From Greek εὔνοια,
“good thinking.” See
[the language account](../tools/sapheneia/manual.md#1-what-eunoia-is).

<a id="euthyna"></a>
**euthyna** (Eunoia child project of [eudaimonia](#eudaimonia); *proper noun*):
The study of what [logos](#logos)’s proof development is made of and where its
weight sits. From Greek εὔθυνα, “the audit at end of term.”
[Charter](https://github.com/ajreynol/eudaimonia/blob/main/tools/euthyna/README.md).

## F

<a id="footing"></a>
**footing** (ecosystem relationship; *noun*): A tool's recorded relationship to
the ecosystem: [member](#member), [associate](#associate),
[president](#president), [candidate](#candidate), [foundation](#foundation),
child, or [outsider](#outsider). These describe different obligations and
claims, not ranks. See
[the footings table (LAW 1)](laws.md#law-1--the-ecosystem-is-a-set-of-footings-and-member-is-only-one-of-them).

<a id="foundation"></a>
**foundation** (footing; *noun*): The [footing](#footing) for a project the
ecosystem exists to serve. It joins nothing, owes nothing, and is subject to no
constraint imposed by this arrangement. See
[the footings](policy.md#the-footings).

## H

<a id="hawkeye"></a>
**hawkeye** (Eunoia child project of [eschaton](#eschaton); *proper noun*): An
unadvertised proposal to build a new SMT solver from nothing, mostly through
autonomous agents. An intention recorded in a page; nothing is built.
[Charter](https://github.com/ajreynol/eschaton/blob/main/tools/hawkeye/README.md).

<a id="hermeneia"></a>
**hermeneia** (Eunoia child project of [eudaimonia](#eudaimonia); *proper noun*):
The study of how results about embedded [SMT-LIB](#smt-lib) formulas can become
statements in [Lean](#lean)’s own logic. From Greek ἑρμηνεία, “interpretation.”
[Charter](https://github.com/ajreynol/eudaimonia/blob/main/tools/hermeneia/README.md).

<a id="heuresis"></a>
**heuresis** (Eunoia child project of [tachyon](#tachyon); *proper noun*): The
investigation of quantified benchmarks where z3 is much faster than
[cvc5](#cvc5), recording shortcomings worth a human’s attention.
[Charter](https://github.com/ajreynol/tachyon/blob/main/tools/heuresis/README.md).

## I

<a id="iogos"></a>
**iogos** (Eunoia associate; *proper noun*): The Isabelle/HOL counterpart of
[logos](#logos) — an executable checker for [CPC](#cpc) and the soundness
scaffolding a proof development about it starts from. Holds the
[associate](#associate) footing by its own marker: held to the shared policy by
its own choice, owing this ecosystem nothing. **Its own README warns it is a
research scaffold and not for use**, with no soundness proof and a generated,
unverified checker. From [logos](#logos), with the Greek article.
[Repository](https://github.com/ajreynol/iogos).

<a id="isarare"></a>
**IsaRARE** (Eunoia outsider; *proper noun*): An outside tool that generates
Isabelle lemmas from RARE rewrite rules, tracked for comparison.
[Repository](https://github.com/cvc5/IsaRARE).

## K

<a id="kanon"></a>
**kanon** (Eunoia president; *proper noun*): The keeper of the ecosystem’s
governance, policy, vision, laws and registers, including what joining costs.
From Greek κανών, “the measuring rod.”
[Repository](https://github.com/ajreynol/kanon).

<a id="kanon-ball"></a>
**kanon-ball** (presidential request; *noun*): A request backed by the laws and
addressed by [kanon](#kanon) to one tool in its discussion file. The name is the
[president](#president)'s front-page joke, not an additional power over the
recipient. See [the joke](../README.md#a-joke-about-the-name).

<a id="koine"></a>
**koine** (Eunoia member; *proper noun*): The keeper of the tooling no other
tool wants to maintain: the ecosystem’s bug database tooling
and the commands that start and join a repository. From Greek κοινή, “the common
tongue.” [Repository](https://github.com/ajreynol/koine).

## L

<a id="lean"></a>
**Lean** (proof assistant; *proper noun*): The proof assistant used to express
and check the ecosystem’s formal proofs. See [logos’s roles](roles.md#logos).

<a id="lean-smt"></a>
**lean-smt** (Eunoia outsider; *proper noun*): An outside tool for discharging
[Lean](#lean) proof goals through SMT solvers, tracked for comparison.
[Repository](https://github.com/ufmg-smite/lean-smt).

<a id="lfsc"></a>
**LFSC** (Eunoia outsider; *proper noun*): An outside proof checker tracked for
comparison. The register records its authors’ statement that it is deprecated.
[Repository](https://github.com/cvc5/LFSC).

<a id="logos"></a>
**logos** (Eunoia member; *proper noun*): The [Lean](#lean) development
containing the verified [CPC](#cpc) checker and its semantics. The L in the name
denotes Lean. [Repository](https://github.com/cvc5/logos).

## M

<a id="martyria"></a>
**martyria** (Eunoia child project of [epikrisis](#epikrisis); *proper noun; also noun*):
The project taking stances on particular ethical situations from evidence of
conduct.
[Charter](https://github.com/ajreynol/epikrisis/blob/main/tools/martyria/README.md).

<a id="member"></a>
**member** (footing; *noun*): A repository that has chosen to adopt [eo](#eo)’s
shared policy and approach. Membership carries obligations and may be left. See
[the footings](policy.md#the-footings).

<a id="metagraphe"></a>
**metagraphe** (Eunoia child project of [tachyon](#tachyon); *proper noun*): The
search for missing [cvc5](#cvc5) rewrites and simplifications for strings and
bit-vectors, with small reproducible examples.
[Charter](https://github.com/ajreynol/tachyon/blob/main/tools/metagraphe/README.md).

<a id="mimesis"></a>
**mimesis** (Eunoia child project of [eudaimonia](#eudaimonia); *proper noun*):
Case studies and tutorials teaching how to write [Eunoia](#eunoia) signatures
and bring them into [logos](#logos). From Greek μίμησις, “imitation.”
[Charter](https://github.com/ajreynol/eudaimonia/blob/main/tools/mimesis/README.md).

<a id="murxla"></a>
**murxla** (Eunoia outsider; *proper noun*): An outside fuzzer that exercises
SMT solvers through their APIs, tracked for comparison.
[Repository](https://github.com/murxla/murxla).

## N

<a id="noesis"></a>
**noesis** (Eunoia child project of [eudaimonia](#eudaimonia); *proper noun*):
Research toward a verified [Eunoia](#eunoia) compiler written in [Lean](#lean),
with explicit statements of what each pass preserves. From Greek νόησις, “the
act of understanding.”
[Charter](https://github.com/ajreynol/eudaimonia/blob/main/tools/noesis/README.md).

## O

<a id="outsider"></a>
**outsider** (footing; *noun*): A tool outside the ecosystem that is tracked for
[comparison](laws.md#what-tracking-is) and is not proposed for promotion. Its
released artifact and published contribution are recorded separately under
[LAW 9.1](laws.md#law-91--release-and-publication), and neither imposes
obligations on it.

## P

<a id="parainesis"></a>
**parainesis** (assessment term; *noun*): Counsel following an assessment: what
should follow from a tool’s strengths and shortcomings. From Greek παραίνεσις,
“counsel.” See [the report card](../tools/stathmos/report-card.md).

<a id="president"></a>
**president** (office; *noun*): The human maintainer of the repository recorded
as holding the presidency. The office is bestowed for a [stretch](#stretch),
sets direction, maintains shared governance including this glossary, and confers
[no control over another tree](laws.md#law-31--authority-over-members).
See [LAW 3](laws.md#law-3--there-is-a-president).

## S

<a id="sapheneia"></a>
**sapheneia** (Eunoia child project of [kanon](#kanon); *proper noun*): An
account of [Eunoia](#eunoia) as a language independent of one checker’s manual;
[ethos](#ethos)’s manual remains authoritative. From Greek σαφήνεια, “clarity of
an account.” [Charter](../tools/sapheneia/README.md).

<a id="smt-lib"></a>
**SMT-LIB** (language; *proper noun*): The shared language and theory vocabulary
used for solver inputs and the semantics modeled by [logos](#logos).
[Eunoia](#eunoia) uses its syntax to express the formulas appearing in solver
proofs. See
[the language account](../tools/sapheneia/manual.md#1-what-eunoia-is) and
[the Lean model role](roles.md#r18--the-model-of-smt-lib-semantics-in-lean).

<a id="stathmos"></a>
**stathmos** (Eunoia child project of [kanon](#kanon); *proper noun*): The
maintainer of ecosystem status auditing, author of the report card and keeper
of its evidence. Mechanical checks and human grades remain separate. From
Greek σταθμός, “a standard weight.” [Charter](../tools/stathmos/README.md).

<a id="stretch"></a>
**stretch** (term of office; *noun*): The period for which a repository holds
the presidency, also called its term. The office expires with it; the account is
[kept during it](laws.md#law-42--keeping-the-account-current). The laws
prescribe no fixed duration. See
[LAW 3](laws.md#law-3--there-is-a-president).

## T

<a id="tachyon"></a>
**tachyon** (Eunoia member; *proper noun*): The search for improvements to
[cvc5](#cvc5)’s performance through reproducible benchmark experiments.
[Repository](https://github.com/ajreynol/tachyon).

<a id="tekmerion"></a>
**tekmerion** (Eunoia child project of [anoieu](#anoieu); *proper noun*): The
study of the evidence behind claims in documentation. From Greek τεκμήριον,
“conclusive evidence rather than a mere sign.”
[Charter](https://github.com/ajreynol/anoieu/blob/main/tools/tekmerion/README.md).

<a id="telos"></a>
**telos** (Eunoia child project of [eschaton](#eschaton); *proper noun*):
Research toward a solver designed around proofs from the start, retaining
[cvc5](#cvc5)’s calculus and parts of its checker while replacing the search.
Research notes; nothing is built.
[Charter](https://github.com/ajreynol/eschaton/blob/main/tools/telos/README.md).

## V

<a id="vaporware"></a>
**vaporware** (status; *noun*): The vision's default status for a tool until a
human chooses to take responsibility for it. Existing code and a passing build
do not make that decision. See
[the tenet](vision.md#4-until-a-human-decides-otherwise-the-tool-is-vaporware).

## W

<a id="wishue"></a>
**wishue** (project aspiration; *noun*): The goal a
[child project](#child-project) would pursue if the work went unusually well,
explicitly without committing to it. It belongs in the charter when there is
one. See [child projects](policy.md#child-projects).

<a id="workflow-launcher"></a>
**workflow-launcher** (Eunoia child project of [eudaimonia](#eudaimonia); *proper noun*):
The study of the first hour of a new tool’s life: the decisions needed before a
repository exists and how to turn them into a useful starting point.
[Charter](https://github.com/ajreynol/eudaimonia/blob/main/tools/workflow-launcher/README.md).

## Y

<a id="ynoia"></a>
**ynoia** (Eunoia child project of [kanon](#kanon); *proper noun*): The inquiry
into whether the ecosystem’s arrangement earns its machinery and what it lacks.
Its name contracts “why [Eunoia](#eunoia).” [Charter](../tools/ynoia/README.md).

## Z

<a id="zetesis"></a>
**zetesis** (Eunoia child project of [epikrisis](#epikrisis); *proper noun*):
The inquiry into ethical standards drawn from outside the ecosystem and whether
its record could demonstrate that they were met. From Greek ζήτησις, “inquiry.”
[Charter](https://github.com/ajreynol/epikrisis/blob/main/tools/zetesis/README.md).
