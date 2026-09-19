# Evidence for the report card

**Recorded 2026-09-19, before writing the corresponding
[report card](report-card.md).** [evidence.json](evidence.json) holds full commit
pins, counts, tooling observations and size subsets. This page records what was
measured and what the sources establish; grades belong in the other file.

## Sources and scope

The starting evidence is epikrisis's September 19 [history note][history-note],
[history figures][history-figures] and [LOC report][loc-report], read at
`447ddb1657ed55a7c974d00a5279cb07eccc1945`. Its September 18
[historical assessment][history-assessment] explains governance-heavy activity,
project migrations and the limits of matching prose to changes.

The September 19 published census covers fourteen repositories. This update
also includes iogos and measures the fifteen fixed local revisions below, using
epikrisis's [history instrument][history-tool] and [LOC instrument][loc-tool]
at that same implementation commit. These are **new local measurements using
epikrisis**, not figures claimed to appear in its published report. No report
was written into epikrisis and its published snapshots were not changed.

The cutoff is **2026-09-19 15:53:09 UTC**. Revisions were captured before this
report was edited. They are checked-out branch heads, not a claim about latest
upstream: ethos is on `rmDeprecated`, logos on `housekeep-0918`, the others on
`main`. In particular, the local cvc5 pin is older than epikrisis's September 19
cvc5 pin. Uncommitted changes in anoieu, dokimasia, ethos, eunoia, iogos and
paideia are excluded. All fifteen Git histories were available without shallow
history truncation.

The tooling inventory and audit implementation are kanon's
`443cc8d7909ebab58cb4fc042569c0dfbcb43091`. The audit's `inspect` function was
given committed Git trees at the same pins as the measurements, instead of
its ordinary live working trees.

## Activity and size

Activity uses epikrisis's stretch-two interval:
**2026-09-15 16:15:46 -05:00 through the cutoff**. It counts reachable commits
selected by Git's committer-date filter, including merges. It is a rough
indicator of current attention and importance, not effort, usefulness, authorship
or adoption. A short window underweights mature dependencies; a move between
repositories is not new ecosystem output. No AI-authorship estimate is made.

LOC uses epikrisis's counting rules v2: physical lines including blanks and
comments, tests, generated code and vendored source. Documentation includes
docs, prompts, licenses and recognized document filenames. JSON/JSONL,
`.github/`, metadata and unrecognized data/text are ignored; binaries,
symlinks and submodules are not counted. No additional exclusions were applied.
These are maintenance and reading surfaces, not runtime, token or labor costs.
Documentation can itself be the intended tutorial or research output.

| repository, fixed revision | footing | stretch commits | implementation LOC | documentation LOC |
| --- | --- | ---: | ---: | ---: |
| [aisthesis `262c93d`][aisthesis] | member | 10 | 0 | 2,281 |
| [anoieu `4f1fb0a`][anoieu] | member | 28 | 15,850 | 8,085 |
| [cvc5 `a07d513`][cvc5] | foundation | 7 | 1,038,850 | 15,509 |
| [dokimasia `54983f1`][dokimasia] | member | 23 | 9,943 | 6,799 |
| [epikrisis `447ddb1`][epikrisis] | member | 27 | 4,403 | 4,932 |
| [eschaton `7729239`][eschaton] | member | 17 | 0 | 2,552 |
| [ethos `9aed682`][ethos] | candidate | 3 | 48,261 | 5,752 |
| [eudaimonia `b465b9d`][eudaimonia] | member | 33 | 28,868 | 13,398 |
| [eunoia `8cfb3ac`][eunoia] | member | 8 | 1,591 | 6,422 |
| [iogos `e716d73`][iogos] | associate | 6 | 84 **incomplete** | 586 |
| [kanon `443cc8d`][kanon] | president | 119 | 3,322 | 12,236 |
| [koine `98e9179`][koine] | member | 42 | 7,059 | 2,335 |
| [logos `e8fa244`][logos] | member | 5 | 814,910 | 6,923 |
| [paideia `8240ce9`][paideia] | member | 12 | 1,079 | 9,200 |
| [tachyon `e400a97`][tachyon] | member | 39 | 5,703 | 7,396 |

There are **379 commits**, of which **363** belong to members or the president.
Kanon accounts for **119/363 = 32.8%** of that attention. Koine (42), tachyon
(39) and eudaimonia (33) follow it within this group. These figures support
prioritizing review of those projects; they do not establish that a cvc5 or
ethos commit matters less. Repository totals are **1,979,923 implementation
and 104,406 documentation lines**, with the iogos omission below.

**Known coverage defect:** the classifier does not recognize Isabelle `.thy`.
Iogos's `Cpc/Cpc_Checker.thy`, `Cpc/Cpc_Spec.thy` and
`Cpc/Soundness/Soundness.thy` total **2,276,986 bytes** and were ignored.
The JSON records their paths and Git object IDs. Its 84 reported implementation
lines cannot support a favorable frugality grade. The older history report's
prose ratios use a different classifier and are not comparable to this table.
In particular, raw benchmark text is not counted as prose here.

## What the tooling audit establishes

At the recorded commits, **all 32 entries are present: 23 tools and 9 artifacts**.
There are no inventory gaps, intentional exclusions or unverified repositories.
The one advisory layout gap is `ethos_eoc`: the Python driver is under
`tools/eoc/` and the C++ implementation is shared across `plugins/`.
This is presence and inventory coverage, not a build or a correctness result.
Discovery skips reserved directories and cannot discover every nested tool.

| repository | registered tools | registered artifacts |
| --- | --- | --- |
| aisthesis | — | — |
| anoieu | analyzer, fuzzer, policy checker | bug database |
| cvc5 | solver | proof signatures |
| dokimasia | analyzer | bug database |
| epikrisis | history analyzer, LOC analyzer | report webpage |
| eschaton | — | — |
| ethos | checker, eoc compiler, plugins | — |
| eudaimonia | checker generator; euthyna's measurement tool | euthyna's webpage |
| eunoia | formatter | mimesis's tutorials |
| iogos | experimental Isabelle checker | — |
| kanon | stathmos's audits | — |
| koine | bug database manager, ecosystem commands | — |
| logos | Cpc checker, CpcMini checker library, parser, installer | — |
| paideia | — | bootcamp tutorial |
| tachyon | job launcher, statistics profiler | heuresis's and elaphros's webpages |

Child ownership remains distinct: euthyna, mimesis, stathmos, heuresis and
elaphros own their listed contributions. A hosting repository gets credit for
making them available, not a second count of the same output. Stathmos and the
previously assessed ethos-eoc retain separate report-card entries; their sizes
are subsets of their hosts. No new child is separately graded in this round.
Sapheneia's documentation supports eunoia's purpose but is not tooling.
Webpages present results; generators are their recorded entry points.

[LAW 11](../../../docs/laws.md#law-11--productive-entities) permits a central
purpose or a special role instead of tooling. Aisthesis's purpose is referenced
by LAW 8; kanon holds the presidency. Eschaton has no registered deliverable or
qualifying central reference/role at this pin. These observations are not
quality grades and do not change anybody's footing.

## Reading behind the assessment

The measurements table links to each fixed front README. These observations
add specific evidence, without presuming that a documented command passed in
this session.

- **cvc5:** the solver, APIs and proof signatures are concrete contributions.
  Logos, ethos, eudaimonia and the analyzers describe consuming this proof
  infrastructure. The old card's unverified `cvc5-1` claim was not reproduced
  and supplies no current adverse evidence. A million implementation lines
  across a general-purpose solver and its tests is not itself evidence of waste.
- **ethos and ethos-eoc:** the checker README distinguishes checking supplied
  rules from establishing their soundness, and identifies experimental plugins
  and tools. The [eoc README][eoc] documents selected-rule Lean and VC generation,
  including `vc ... RULE` and `lean ... RULE1 RULE2`; the old claim that only a
  whole-signature loop exists is stale. `tools/eoc/` contains 9,348 implementation
  and 2,756 documentation lines; `plugins/` adds 17,338 and 206 shared lines,
  which cannot all be attributed exclusively to eoc. No compiler build or
  backend equivalence proof was attempted.
- **anoieu:** its three tools and database are present. **Eleven other
  repositories** configure anoieu policy checking: aisthesis, dokimasia,
  epikrisis, eschaton, eudaimonia, eunoia, kanon, koine, logos, paideia and tachyon.
  Evidence is `.github/workflows/anoieu.yml` in each pinned tree except
  dokimasia's `.github/workflows/policy.yml`. Configuration proves integration,
  not a successful CI run. [Its database][anoieu-db] has 82 records, 25 carrying
  closure dates and commit coordinates. These are owner-recorded outcomes;
  upstream fixes and causal attribution were not independently reverified.
  The former blanket claim that nothing was filed is not retained.
- **dokimasia:** [its database][dokimasia-db] has 197 records, one carrying a
  closure date and commit coordinate. Records include static observations;
  their count is not a count of reproduced bugs or accepted upstream changes.
  The analyzer and persistent database replace the old card's account of a
  nearly empty findings pipeline.
- **koine:** `bug_db_manager/` and `eo_cmd/` are two distinct contributions.
  Anoieu's [reporting lock][anoieu-koine] and dokimasia's
  [scripts lock][dokimasia-koine] both select
  `8efe59ca20b5d684d8d00fce330b6a6968444493`. These are concrete consumer
  integrations. The present koine revision is newer than those consumer pins;
  adoption of every new change is not established.
- **logos:** its front page describes both checker libraries, parser and
  regeneration workflow, and distinguishes the theorem from parsing and
  unproved obligations. `Cpc/` contains 751,932 implementation lines, including
  352,795 in `Proofs/RuleSupport/` and 279,000 in `Proofs/Rules/`. The README
  reports full builds exceeding two hours and CI using a representative subset;
  these are documented limits, not fresh timings. This edition does not repeat
  the unverified allegation that its installer lacks drift control.
- **eudaimonia:** `new_checker/` accounts for 21,220 implementation lines.
  Euthyna's measurement and presentation directories contribute another 4,594
  and 826. The 632-line README explicitly limits generated-checker guarantees.
  Generated examples contribute to the code count; the full 28,868 lines are
  not all handwritten generator logic. Measurement infrastructure is a delivered
  contribution without claiming that all proof obligations are solved.
- **eunoia:** `eo_format/eo_format.py` is 1,093 implementation lines and mimesis
  has tutorials. The same fixed README still says that nothing here is a
  program: it does not yet describe the formatter it contains. Migration of
  mimesis and sapheneia explains part of its size and new-repository activity;
  it is not eight commits of wholly new ecosystem work.
- **paideia:** 7,790 of its 9,200 documentation lines are in `bootcamp/`.
  They are the tutorial artifact, not incidental governance. Its front page
  records a source-reading baseline and states the limits of exercise
  validation. This review did not execute every tutorial path or establish
  that a new contributor completed it unaided.
- **tachyon:** the two tools and two child webpages exist. The launcher is
  1,063 implementation lines and profiler 1,306; the repository total includes
  more scripts and presentation code. Its README keeps raw benchmark outputs
  on the execution host or in ignored working space. Presentations and recorded jobs establish
  research output, not an independently replayed speedup in cvc5.
- **epikrisis:** its current paired history and LOC reports supply this
  assessment, an actual downstream use. The historical assessment warns about
  corpus changes and lexical claim matching; this round also found the concrete
  `.thy` coverage omission. A replayable count is not necessarily a complete
  measurement, and a matched word is not a verified historical claim.
- **aisthesis:** its 2,281 documentation lines hold readings, an assessment and
  explicitly speculative fiction. The central research role explains the
  absence of tooling. This review inspected the repository's account, not every
  external paper, and does not independently confirm its novelty judgments.
- **eschaton:** the README explicitly says there is no solver or tested claim
  yet. Seventeen stretch commits and 2,552 documentation lines establish active
  proposal work, not an implemented solver. Unlike aisthesis, the inventory has
  no alternative LAW 11 basis for this member at the recorded pin.
- **kanon and stathmos:** kanon now contains working audit implementations;
  the old statement that it ships no instrument is false. Stathmos accounts
  for 3,154 implementation and 756 documentation lines inside kanon's totals.
  Kanon's `docs/misc/` alone accounts for 2,643 documentation lines. At the
  assessed pin, stathmos's evidence is dated September 2 and its card September
  16. This patch repairs that mismatch, but is outside the graded pin and earns
  no retrospective credit. Both entries are self-assessments.

## Reproducing the measurements

Use the full pins in `evidence.json`, including the epikrisis implementation
pin, rather than whatever branch heads exist when repeating the review.
For each repository, use its checkout path and recorded commit:

```sh
git -C CHECKOUT rev-list --count \
  --since-as-filter=2026-09-15T16:15:46-05:00 \
  --until=2026-09-19T15:53:09+00:00 COMMIT
```

For LOC, export `loc_analyzer/bin/loc` with `git show` at the recorded epikrisis
commit and import that file with Python's `SourceFileLoader`. Pass each source
record to `count_tree(source, checkouts, [])`, where `checkouts/ID` is its Git
checkout. Concatenate records in the JSON source order. `write_run` writes the
corpus, file records, totals and report; `check_run(run_dir, checkouts)` replays
them. Its serialized per-file SHA-256 must match `method.loc_files_digest_sha256`
in our JSON. Every subset above is a sum by repository, path prefix and category.
The generated evidence was checked with `check_run` against the pinned trees.

For tooling, load both inventories and the audit implementation at the kanon pin.
Build `Tree` objects from `git ls-tree -r` at each source pin, with files and
their parent directories and `root=None`, and supply them to `inspect` through
`local_tree`. A normal `eo_tooling_audit --check --local` instead inspects current
working trees and may legitimately differ. Our JSON records the observed entries
and exceptions; the source inventory supplies their required entry points, files
and documentation.

This round did not rebuild cvc5, ethos, Logos or generated checkers, rerun remote
benchmarks, execute all tutorials, check deployed webpages, or verify upstream
issue outcomes. Those limits constrain the judgments: file presence, a workflow
declaration and a passed execution are distinct evidence.

[history-note]: https://github.com/ajreynol/epikrisis/blob/447ddb1657ed55a7c974d00a5279cb07eccc1945/history_analyzer/runs/eunoia-ecosystem-s2/2026-09-19/note.md
[history-figures]: https://github.com/ajreynol/epikrisis/blob/447ddb1657ed55a7c974d00a5279cb07eccc1945/history_analyzer/runs/eunoia-ecosystem-s2/2026-09-19/figures.json
[history-assessment]: https://github.com/ajreynol/epikrisis/blob/447ddb1657ed55a7c974d00a5279cb07eccc1945/history_analyzer/runs/eunoia-ecosystem-s2/2026-09-18/report.md
[loc-report]: https://github.com/ajreynol/epikrisis/blob/447ddb1657ed55a7c974d00a5279cb07eccc1945/loc_analyzer/runs/eunoia-ecosystem/2026-09-19/report.md
[history-tool]: https://github.com/ajreynol/epikrisis/blob/447ddb1657ed55a7c974d00a5279cb07eccc1945/history_analyzer/bin/epikrisis
[loc-tool]: https://github.com/ajreynol/epikrisis/blob/447ddb1657ed55a7c974d00a5279cb07eccc1945/loc_analyzer/bin/loc
[aisthesis]: https://github.com/ajreynol/aisthesis/blob/262c93d2c0bab8b527ab65bc7b63e44ac40a3524/README.md
[anoieu]: https://github.com/ajreynol/anoieu/blob/4f1fb0aac1c58541f2cd1a4cacfbf9411e6d31c6/README.md
[cvc5]: https://github.com/cvc5/cvc5/blob/a07d51307598ec718af427c4fb97645d2013ebb8/README.md
[dokimasia]: https://github.com/ajreynol/dokimasia/blob/54983f1bf19ea88dc555a2d4ff4b07d9640e5249/README.md
[epikrisis]: https://github.com/ajreynol/epikrisis/blob/447ddb1657ed55a7c974d00a5279cb07eccc1945/README.md
[eschaton]: https://github.com/ajreynol/eschaton/blob/772923914e9e4f62cc2744e203dba5c332d982fc/README.md
[ethos]: https://github.com/cvc5/ethos/blob/9aed6823725d6ed9c0cdcbfa73d623e47f57d8e8/README.md
[eudaimonia]: https://github.com/ajreynol/eudaimonia/blob/b465b9d954bb021992ff4ac6c28c9d72975f9894/README.md
[eunoia]: https://github.com/ajreynol/eunoia/blob/8cfb3ac5c3f6c01e453178de72200e265884a7bc/README.md
[iogos]: https://github.com/ajreynol/iogos/blob/e716d73c00c8e269f0d8aae65c69e9af0f04ec4e/README.md
[kanon]: https://github.com/ajreynol/kanon/blob/443cc8d7909ebab58cb4fc042569c0dfbcb43091/README.md
[koine]: https://github.com/ajreynol/koine/blob/98e917993425eb2fec0047da4fa9ac0a3730627d/README.md
[logos]: https://github.com/cvc5/logos/blob/e8fa24414aa69ede1f065f2cecf41fafb5aa05d8/README.md
[paideia]: https://github.com/ajreynol/paideia/blob/8240ce9e82c2ea5847b5884ceb621c15169c83e4/README.md
[tachyon]: https://github.com/ajreynol/tachyon/blob/e400a97fc9fd7138500996f3176871a2871bee3d/README.md
[eoc]: https://github.com/cvc5/ethos/blob/9aed6823725d6ed9c0cdcbfa73d623e47f57d8e8/tools/eoc/README.md
[anoieu-db]: https://github.com/ajreynol/anoieu/blob/4f1fb0aac1c58541f2cd1a4cacfbf9411e6d31c6/bug_db/bugs.json
[dokimasia-db]: https://github.com/ajreynol/dokimasia/blob/54983f1bf19ea88dc555a2d4ff4b07d9640e5249/bug_db/bugs.json
[anoieu-koine]: https://github.com/ajreynol/anoieu/blob/4f1fb0aac1c58541f2cd1a4cacfbf9411e6d31c6/anoieu_analyzer/reporting/config/koine.lock
[dokimasia-koine]: https://github.com/ajreynol/dokimasia/blob/54983f1bf19ea88dc555a2d4ff4b07d9640e5249/scripts/koine.lock
