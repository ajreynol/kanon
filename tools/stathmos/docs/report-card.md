# The report card

**Graded 2026-09-19 against the five tenets of
[vision.md](../../../docs/vision.md).** Stathmos's assessment now starts from
what the [tooling audit](evidence.md#what-the-tooling-audit-establishes) actually
lists, epikrisis's history reports, and its LOC measurements. The
[evidence](evidence.md) was assembled first; [evidence.json](evidence.json)
records the fixed revisions and measurements behind every entry.

**This is a judgment, not a build step.** Counts are mechanical; grades are
argued. A person may overrule any paragraph without giving a reason. The card
neither changes membership nor reports a code defect through another project's
findings process. A foundation or candidate owes no compliance to this page.

This edition replaces the September 16 assessment. It covers fifteen
repositories and retains the two separately assessed projects, ethos-eoc and
stathmos. Other children's contributions are credited within their hosts without
separate grades or double-counted size. The assessed revisions precede this
patch; it does not award itself credit for its own corrections.

## How to read the grades

The bands remain **excellent, good, fair, poor**. *Fair* marks a gap or an early
contribution. *Poor* requires evidence of a negative contribution, not merely
missing tooling, many lines or little recent activity. **Unrated** means the
available evidence cannot support a judgment on that axis.

- **Delivered:** usable tools, artifacts or a central contribution, with stronger
  credit for demonstrated use by another project. A tutorial or database counts;
  an inventory entry alone does not establish quality or adoption.
- **Legible:** a newcomer can find the contributions and understand their limits.
- **Checkable:** the claims have recorded inputs, reproducible procedures and
  explicit verification boundaries. A documented test is not a passed run here.
- **Frugal:** the implementation and reading burden are proportionate to the
  delivered purpose. LOC makes that burden visible; it does not set a quota.
  Proofs, tests, tutorials, generated examples and governance have different uses.

**Activity is a rough signal of importance and where to spend review attention.**
It is not a fifth quality grade. In the current stretch, kanon has 119 of the
363 member/president commits (32.8%), followed by koine (42), tachyon (39) and
eudaimonia (33). That makes the president's cost and those active interfaces
immediate review priorities. Five recent Logos commits or seven cvc5 commits
cannot capture those mature projects' importance to their consumers.

The tooling audit finds **23 tools and 9 artifacts present**, with no inventory
gaps and one advisory split-layout exception in ethos. That clears several old
criticisms; it proves neither that every artifact works nor that every entity
has a deliverable. LAW 11's mechanical `productive` result is a separate question.

## The standing

All rows were graded on September 19 at the [recorded versions](evidence.md#activity-and-size).

| project | delivered | legible | checkable | frugal | main reason |
| --- | --- | --- | --- | --- | --- |
| cvc5 | excellent | good | good | unrated | solver and signatures underpin the ecosystem; size needs a solver-specific comparison |
| ethos | excellent | good | good | fair | reusable checker; experimental tooling shares a substantial implementation |
| ethos-eoc | good | good | good | unrated | selected-rule generation exists; shared plugins prevent isolated size attribution |
| anoieu | good | good | good | fair | eleven other policy integrations; outcome records need separate interpretation |
| logos | excellent | good | good | fair | four contributions; proof size and slow full builds constrain feedback |
| eudaimonia | good | fair | good | fair | generator plus measurement and presentation; a large entry surface |
| dokimasia | good | good | fair | fair | analyzer and database exist; observations are not all reproduced bugs |
| koine | good | good | good | good | two shared tools and concrete consumer pins |
| kanon | good | good | fair | fair | executable audits now exist; governance still dominates recent attention |
| tachyon | good | good | good | fair | launch, profiling and two webpages; raw results are untracked |
| eschaton | fair | excellent | fair | fair | active proposals, with no deliverable or alternative productive basis yet |
| epikrisis | good | good | good | good | current reports support this review; Isabelle LOC is a demonstrated blind spot |
| aisthesis | good | good | fair | good | a central research contribution, appropriately made of documents |
| eunoia | good | fair | fair | good | formatter and tutorials exist; the front page denies having programs |
| paideia | good | good | fair | good | bootcamp is a tutorial artifact; learner outcomes remain unestablished |
| iogos | fair | good | fair | unrated | checker scaffold is explicit about limits; LOC misses the checker itself |
| stathmos | good | good | fair | fair | real audits; the assessed card and evidence had different dates |

Read across each row. These projects have different purposes, and the table is
not a league table. Each entry has **arete** (what works), **elleipsis** (the
supported shortfall or uncertainty), and **parainesis** (what follows). Human
maintained projects receive observations; agent maintained projects receive
instructions, following their own maintenance statements. Mixed projects retain
their stated experimental boundaries.

## cvc5

**Arete.** The solver and proof-signature artifact are both present. The other
projects' documented consumption of CPC makes cvc5 foundational even with only
seven commits in this local stretch window. Its delivery is established by
those interfaces and consumers, not by its position in an activity ranking.

**Elleipsis.** The 1,038,850 implementation lines include tests and a broad solver;
this review has no comparable scope or performance evidence with which to call
that frugal or wasteful. No solver build was run here. The old unverified
`cvc5-1` criticism supplies no current evidence and is retired from this card.

**Parainesis.** A useful next comparison would isolate proof-production changes,
consumer compatibility and measured cost. This foundation's value is clearer
from those dependencies than from a whole-repository line count.

## ethos

**Arete.** The checker, compiler and plugins are actual contributions. The front
page clearly distinguishes checking a proof against supplied rules from proving
those rules sound. Its human maintained checker remains a reference point for
other implementations despite only three commits in the measured local window.

**Elleipsis.** Of 48,261 implementation lines, 17,338 are in shared plugins and
9,348 in `tools/eoc/`. Treating all of that as the small trusted checker would
hide the experimental surface. The split compiler layout is the tooling audit's
one advisory exception; neither that exception nor candidate status is a defect.

**Parainesis.** Separate measurements of checker cost and experimental compiler
cost would make future frugality claims meaningful. The explicit boundary in
its README is worth preserving in downstream descriptions.

## ethos-eoc

**Arete.** The current README documents per-rule VC generation and selected-rule
Lean generation. The old adverse claim about needing to compile everything is
stale. The driver and compiler plugins support concrete downstream generation
workflows described by Logos and eudaimonia.

**Elleipsis.** Its directory's 9,348 implementation and 2,756 documentation lines
are only part of its cost: shared plugins cannot be attributed exclusively to
this compiler. The generated package still needs handwritten destination
components; generation is not a completed soundness proof. Nothing was compiled
in this assessment.

**Parainesis.** A timed selected-rule run, with its input and downstream revision,
would establish the feedback improvement more directly than a claim about
agility. Isolating that run's dependencies would also support a frugality grade.

## anoieu

**Arete.** The analyzer, fuzzer, policy checker and bug database are all present.
Eleven other repositories configure its policy checker, a concrete integration
signal. Its database records 82 findings or observations and 25 closures with
commit coordinates. The old blanket statement that nothing was filed is removed.

**Elleipsis.** A configured workflow is not evidence of a green run, and a closure
record is not independent confirmation of an upstream fix caused by the tool.
At 15,850 implementation and 8,085 documentation lines, the three tools carry a
substantial reading burden; policy uptake alone cannot establish analyzer or
fuzzer impact.

**Parainesis.** In the next assessment, separate policy adoption from one
reproduced analyzer/fuzzer outcome with the consumer's resolution. Reuse the
existing database evidence and shared koine workflow instead of adding another
parallel narrative of findings.

## logos

**Arete.** The inventory now credits Cpc, CpcMini, the parser and the installer.
A library is a contribution without a standalone executable. The README makes
proof and parser boundaries explicit; the installer is part of keeping the
checker aligned with its supplied CPC source.

**Elleipsis.** There are 814,910 implementation lines, including 631,795 in
`Cpc/Proofs/RuleSupport/` and `Cpc/Proofs/Rules/`. Proof volume is not automatically
waste. The concrete feedback constraint is the README's report of full builds
over two hours and CI checking a representative subset. Those builds and timings
were not repeated here, so the old blanket excellent checkability grade narrows.

**Parainesis.** Published measurements of proof structure, rebuild cost and what
the CI subset covers would make the burden assessable. Euthyna now provides
measurement infrastructure for that conversation; line deletion alone would
not establish an improvement.

## eudaimonia

**Arete.** The checker generator is joined by euthyna's measurement tool and
webpage. Those are three present contributions with separate purposes. The
front page now states the limits of generated checkers explicitly, so the
previous instruction to surface that warning has been satisfied.

**Elleipsis.** The repository has 28,868 implementation and 13,398 documentation
lines, including generated examples and child work. The 632-line front README
is a substantial entry cost. Euthyna presents measurements; neither its presence
nor generated Lean proves that every emitted checker has discharged its obligations.

**Parainesis.** Keep the front page focused on choosing and running a contribution,
with detailed contracts in the existing documentation. Use euthyna's dated
measurements to demonstrate one reduction in downstream proof or rebuild cost.

## dokimasia

**Arete.** The analyzer and database are delivered artifacts, and the shared koine
integration is pinned. The database has 197 records, so the previous picture of
an almost empty reporting pipeline no longer describes this version.

**Elleipsis.** The records include static observations; one records closure with
a commit. Neither 197 records nor 23 recent commits establishes 197 bugs or a
corresponding number of fixes. This review did not reproduce a C++ finding.
The 9,943 implementation and 6,799 documentation lines make careful prioritization
more useful than another broad catalogue.

**Parainesis.** Take one high-value open observation through reproduction and a
recorded consumer disposition. Report that outcome separately from database
size, including a reasoned rejection if that is what the evidence supports.

## koine

**Arete.** There are two tools, `bug_db_manager/` and `eo_cmd/`. Anoieu and dokimasia
both pin the shared database manager, and its ownership boundary is clear:
koine supplies machinery while consumers own records. The old one-script
assessment is obsolete.

**Elleipsis.** Its 42 stretch commits make it the busiest member after the
president, but its two observed database consumers pin an older commit than
the assessed head. That limits what recent activity proves about adoption.
The current 7,059 implementation lines serve two jobs; keeping them shared is
a stronger frugality case than simply keeping them few.

**Parainesis.** Demonstrate one current command or database change at a consumer's
chosen revision. Keep common behavior here and user-specific records in their
owners; a third customer is not an arbitrary requirement for a better grade.

## kanon

*Self-assessment: stathmos lives in this repository.*

**Arete.** The status and tooling audits now exist under stathmos, and this review
uses the inventory they inspect. The claim that kanon ships no instrument is
withdrawn. Its central rules and presidency also have a purpose independent of
owning an executable.

**Elleipsis.** It accounts for 119 of 363 member/president stretch commits and
12,236 documentation lines against 3,322 implementation lines. Those figures
identify an attention and reading cost, not proof of waste. A concrete place
to review is the 2,643 lines in `docs/misc/`. The stale card/evidence pair at
this pin shows that documentation volume has not ensured currency.

**Parainesis.** Review the miscellaneous discussions for material already settled
or owned elsewhere. For the next governance addition, name the decision it
clarifies or the reading it removes, then compare the resulting LOC at a fixed
revision. Moving prose into a child or another repository is not an ecosystem
saving by itself.

## tachyon

**Arete.** The job launcher and statistics profiler are real tools, and heuresis
and elaphros each present research through a webpage. Its 39 stretch commits
are accompanied by concrete outputs, correcting the earlier delivery grade
based only on whether a result had reached cvc5.

**Elleipsis.** The repository carries 5,703 implementation and 7,396 documentation
lines. Raw benchmark outputs stay on the execution host or in ignored working
space, so a committed
presentation is not enough to replay every claim from this checkout. This review
establishes neither an upstream speedup nor who acted on the results.

**Parainesis.** Tie one prominent presented result to the exact inputs, raw-output
location, revision and interpretation needed to repeat it. Prefer that complete
example over expanding the research queue, and use it to justify further reporting
surface.

## eschaton

**Arete.** The front page is unusually clear that there is no solver and no tested
claim yet. Its 17 commits and 2,552 documentation lines are explicitly proposals,
so readers can distinguish activity from an implemented result.

**Elleipsis.** There is no registered tool or artifact, nor an alternative
qualifying central reference or role at the recorded pin. The LAW 11 gap and
the limited delivery evidence agree here; the absence of code alone is not
what determines the grade.

**Parainesis.** Produce one small, reproducible experiment from an existing
proposal, or bring the intended central research purpose to a person for an
explicit decision. Do not invent a tooling entry for ordinary documentation
merely to turn the productive indicator green.

## epikrisis

**Arete.** The history analyzer, LOC analyzer and report webpage all exist. The
September 19 reports have fourteen-source coverage and are used by this card;
the old missing-census criticism is stale. A shared measurement instrument with
4,403 implementation lines and an actual consumer is a good frugality case.

**Elleipsis.** Replaying a classifier faithfully does not establish complete
coverage. This round found that it ignores iogos's three Isabelle theories,
reporting only 84 implementation lines for that repository. Historical lexical
matches also need interpretation, as its own report explains. The 4,932 document
lines include research children and cannot all be charged to the two analyzers.

**Parainesis.** Recognize Isabelle sources in the LOC classifier and recount the
same revisions before making an iogos size comparison. Keep source coverage,
classification changes and historical migrations explicit in subsequent reports.

## aisthesis

**Arete.** Its readings and assessments serve the central research purpose named
by LAW 8. The 2,281 documentation lines are the contribution; adding an invented
program or registering ordinary docs as tooling would not improve it.

**Elleipsis.** Ten recent commits show attention, not that the literature
judgments are correct or that a project changed direction because of them.
This review did not independently read the external papers behind those judgments.

**Parainesis.** In the next review, connect one assessment to a specific ecosystem
decision and the source passage supporting it. Keep speculative scenarios visibly
separate from established research and keep the central account concise.

## eunoia

**Arete.** The formatter is a concrete 1,093-line implementation, and mimesis's
tutorials are an artifact. Housing language work together makes these
contributions easier to find in principle; sapheneia need not be listed as a tool.

**Elleipsis.** The assessed README still says nothing here is a program, despite
containing `eo_format/`. That is a specific entry-point failure. Its 6,422 document
lines and eight commits partly reflect projects moving here, so they are not
measures of newly created output. Formatter behavior was not exercised here.

**Parainesis.** Put the formatter's purpose, invocation and check mode on the
front page, alongside the tutorials and language documents. Remove the stale
no-program claim and demonstrate one consumer using the formatter.

## paideia

**Arete.** Bootcamp is a registered tutorial artifact. Its 7,790 lines explain
most of the repository's 9,200 documentation lines and are intended output,
not evidence that a tutorial should have been a program. The source baseline
and exercise limitations are visible.

**Elleipsis.** Twelve recent commits and source-linked chapters do not establish
that a newcomer can complete an exercise. This review did not execute the
bootcamp paths or observe a learner's result; delivery is available material,
not established educational effectiveness.

**Parainesis.** Record one end-to-end exercise attempt against its source baseline,
including where instructions were insufficient. Use that result to shorten or
repair a chapter before treating more chapters as the next improvement.

## iogos

**Arete.** The generated Isabelle checker and obligations are present, and its
README states the missing soundness proof, model, parser and standalone runner.
That makes an experimental scaffold legible without claiming a finished checker.

**Elleipsis.** Six commits establish early work, not an independently usable proof
checking path. The reported 84 implementation LOC exclude three `.thy` files
containing 2,276,986 bytes, so frugality is unrated. The documented generation
path also depends on an older compiler revision.

**Parainesis.** Demonstrate one reproducible generation-and-checking example with
its precise compiler revision and unresolved obligations. Revisit the size grade
only after epikrisis's classifier covers the actual Isabelle implementation.

## stathmos

*Self-assessment: the project writing this page, already separately assessed.*

**Arete.** Its executable audits now support inventory and productivity review.
They provide the 32-entry tooling evidence used here; this is a delivered tool,
not only a role or a paragraph. Its 3,154 implementation lines include its tests
and are already counted inside kanon.

**Elleipsis.** At the fixed kanon revision, the evidence was dated September 2 and
the card September 16. The 756 documentation lines did not form a current,
consistent assessment. This update addresses that defect but is outside the
assessed revision; writing it cannot retroactively improve the grade.

**Parainesis.** Keep future evidence and assessments in the same review, name the
fixed pins, and check classifier coverage before interpreting totals. Reuse
epikrisis's instruments instead of growing another history or LOC implementation.
The next round can judge whether this edition actually made a decision easier.

## How to get a paragraph changed

Say which claim or inference is wrong. A new recorded version can replace stale
evidence; no issue, membership change or automatic grade follows. The most
uncertain judgments here concern unexecuted pipelines, independently unverified
outcomes and iogos's incomplete LOC coverage. The evidence page names those limits
so they can be resolved rather than carried forward as undated allegations.
