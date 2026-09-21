# Projects worth attention

**Where the ecosystem should spend attention next, and whether a project's home
helps that work.** Reviewed on **2026-09-21**, following the maintainer's interest
in separate repositories for metagraphe and heuresis, and their assessment that
noesis is becoming stale because other work has priority.

This is a selective list of recommendations. Project queues remain at their
sources; this page records the next useful decision, not a second backlog.
[New tool ideas](tools.md) and [paper prospects](papers.md) have their own pages.
A repository move remains a human decision; none is approved by this review.

## Where attention goes

| project | recommendation | next useful result or decision |
| --- | --- | --- |
| [metagraphe](#metagraphe) | First candidate for a separate repository; continue the rewrite work. | A concrete separation plan for its database, tools and parent-level material. |
| [heuresis](#heuresis) | Give the measured performance questions attention; consider a separate repository with an explicit shared-tool boundary. | One focused attribution result, plus a decision on how it would consume tachyon's experiment tools. |
| [noesis](#noesis) | Keep the purpose and prototype; defer substantial work while attention is elsewhere. | A short restart point and, when resumed, one bounded preservation result or a precise obstacle. |

## Metagraphe

**Why attention is warranted.** It already has a distinct artifact: a
[rewrite database][meta-db] with exact candidates, conditions, validity and
availability assessments, evidence, and RARE drafts. Its [work queue][meta-queue]
records candidates from both an issue survey and executable benchmark probes.
That is material a cvc5 developer can assess without adopting the rest of
tachyon. Candidate records are not claims that fixes have landed.

**Repository case.** Of these three, this is the clearest first separation:
its discovery purpose, database and filing tools form a recognizable project.
A separate repository could give that work its own entry point, issue history
and maintenance cycle. The benefit needs to justify moving material currently
outside the child: the issue survey and two launch prompts, as its
[charter][meta] records.

**Next useful work.** Prepare that boundary and choose one promising rewrite
whose evidence would most help a developer decide whether to use it. Preserve
candidate identities and their history. Independence need not wait for an
upstream patch, which is outside the project's discovery remit.

## Heuresis

**Why attention is warranted.** It has a fixed quantified benchmark subject,
measured comparisons, option experiments and an evidence ledger. Its
[charter][heur] identifies a missing per-benchmark attribution table: the
opportunity is to explain a measured gap well enough that a developer can
choose a response. Its [queue][heur-queue] already names bounded investigations;
there is no need to reproduce their ranking here.

**Repository case.** A separate home is plausible for a sustained research
program with its own reports and audience. The boundary is less compact than
metagraphe's: experiments use tachyon's shared job launcher, and the parent's
site builder and tests participate in publishing its results. Moving the
directory alone would leave that arrangement incomplete.

**Next useful work.** Take one measured question through attribution, such as
the mechanism behind central equality mode's observed effect, with the baseline,
corpus and limits recorded. In parallel, decide how an independent repository
would run experiments and publish reports using the shared infrastructure.
The maintainer's interest in a move is recorded; it is not yet a migration plan.

<a id="p3--the-semantics-and-the-compiler-defined-in-lean"></a>

## Noesis

**Purpose retained, attention deferred.** A verified Eunoia-to-Lean compiler
still addresses a real question. The maintainer's assessment here is that other
priorities are crowding it out, not that the purpose has failed.

The [project][noesis] already contains a Lean definition of a core semantics
fragment and a check script. Its code last changed on 2026-09-16 in the local
history read for this review; later edits include documentation and layout.
Its charter reports 23 guards, not a verified compiler. The old P3 account that
the implementation had been written zero times is obsolete.

**Recommendation.** Keep it as a child of eudaimonia and preserve a small restart
point: what the prototype establishes, the compiler and Lean versions to
recheck, and one next question. When attention returns, rerun the existing
check and revisit the charter's first compiler probe, a preservation theorem
for `linear_patterns`, or record precisely why it cannot yet be stated.
The [semantics notes][noesis-eos] also identify smaller work, but broadening the
plan now would not supply the missing attention. This review neither retires
the project nor changes its charter.

**Repository case: not now.** Reconsider when a concrete compiler result has a
consumer and a separate home would help maintain or deliver it. The historical
**P3** review recommended eudaimonia as its initial home; its original
prerequisites and authority fork are in the [earlier assessment][previous].
They are background to revisit, not newly imposed conditions for resuming work.

## The standard

Judge an attention or repository proposal by five practical questions:

1. What artifact exists, and who can use it?
2. What bounded result would make the next period of attention worthwhile?
3. What does a separate repository improve over the present child project?
4. What moves, what stays shared, and who maintains each part afterward?
5. What evidence would make us defer the work or revise the recommendation?

For both tachyon candidates, the default separation to examine leaves general
job-launching and profiling tools with tachyon and project-specific evidence,
queues and reporting with the project. Specify how shared tools are obtained
and versioned, and account for launchers, site publishing and tests.
A useful child need not graduate; a new repository does not itself produce a
result. An attention shortage should be recorded as such.

## Earlier proposals

The [previous 811-line page][previous] preserves the full audits, naming
alternatives and seven older wishes. Those wishes are removed from the active
list, not recorded as completed or assigned to their formerly suggested homes.
Reopen one when a current consumer and a next deliverable make it useful.

### P1 — central tooling for reporting

Completed as **koine**, whose delivered work is shared database tooling and
ecosystem commands. The originally proposed reporting loop was retired.
The naming discussion and original reasoning remain in the earlier assessment.

### P2 — the ecosystem's governance, out of the analyzer

Completed with a split: kanon holds policy and the register, anoieu the policy
checker, and koine the shared commands. The proposal is history, not work still
waiting to start. P3's current assessment is under [noesis](#noesis).

## Keeping this short

Review an entry when its evidence, consumer or maintainer priority changes.
Keep the artifact, recommendation, next result and repository boundary; link
to the project's own queue. Remove settled entries, preserving a short outcome
only when another document still cites it. Read sources at named revisions
and distinguish a maintainer's priorities from this page's recommendations.

**Sources read:** tachyon `a80fe6e` and eudaimonia `1abe181`, on 2026-09-21.
These sources establish the recorded work; the recommendations above are
ynoia's assessment.

[meta]: https://github.com/ajreynol/tachyon/blob/a80fe6e31a449ca153f25047a993d39dcb231d5e/tools/metagraphe/README.md
[meta-db]: https://github.com/ajreynol/tachyon/blob/a80fe6e31a449ca153f25047a993d39dcb231d5e/tools/metagraphe/rewrite_db/README.md
[meta-queue]: https://github.com/ajreynol/tachyon/blob/a80fe6e31a449ca153f25047a993d39dcb231d5e/tools/metagraphe/docs/todo.md
[heur]: https://github.com/ajreynol/tachyon/blob/a80fe6e31a449ca153f25047a993d39dcb231d5e/tools/heuresis/README.md
[heur-queue]: https://github.com/ajreynol/tachyon/blob/a80fe6e31a449ca153f25047a993d39dcb231d5e/tools/heuresis/docs/todo.md
[noesis]: https://github.com/ajreynol/eudaimonia/blob/1abe18131b40d334aab42ab062c9778bbc85823b/tools/noesis/README.md
[noesis-eos]: https://github.com/ajreynol/eudaimonia/blob/1abe18131b40d334aab42ab062c9778bbc85823b/tools/noesis/docs/eos-in-lean.md
[previous]: https://github.com/ajreynol/kanon/blob/93ee96620519110700e16d239eea10a52eb3efdd/tools/ynoia/docs/proposals.md
