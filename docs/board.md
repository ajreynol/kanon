# The board

**Outstanding work across the Eunoia ecosystem, in priority order.** Each
item names the next action and who can take it. Stable ids survive reordering;
the maintenance notes are at the bottom.

**Set by the maintainer on 2026-11-05, from an ecosystem review of 2026-11-04.**
The chain from cvc5 into logos comes first, then the work that feeds it, then
decisions about what to park. Figures come from that review at the named
revisions. Its scratch runs are not committed, so re-take a figure before
relying on it.

## B45 — check the full logos proof, and report its axioms

**Task:** make a scheduled job establish what logos's soundness claim rests on.
**Entities:** `logos`
**Status:** ready — read 2026-11-05 at logos `75c7ee67`. `scripts/run-ci.sh`
builds 3 of the 607 rule files (`Refl`, `Contra`, `Trans`). No `#print axioms`
exists anywhere in the tree. `native_decide` appears on 611 lines in 205 files
and `scripts/check-proof-hygiene.sh` does not look for it, so the compiler is
trusted by the proofs as well as by the executable. The review's 607-of-609
rule figure is a text scan for `sorry`, not a build, and no full build was run
at this revision. #491 patched rule files right after #489, which may mean
breakage got past CI; that is unconfirmed.
**Channel:** **upstream, by a person**.
**Next:** run the full rule build once at a recorded revision, then schedule it
with `#print axioms correct___logos_check_proof` in its output.
**Prompt — `logos`:** add a scheduled job that builds every rule file and
`Cpc.ApiCorrect`, records the commit, and prints the theorem's axioms. Keep the
axiom list visible and decide whether to allowlist it.
**HUMAN FEEDBACK:**

## B46 — state exactly what `correct` establishes

**Task:** correct logos's documents where they say more or less than the code.
**Entities:** `logos`
**Status:** ready — read 2026-11-05 at logos `75c7ee67`. `reference` is ignored
(`Logos/Parser/Core.lean`, comment: *the input problem is not checked against*),
so `correct` covers the proof's own assumptions and not an input file. The
README's wording is accurate but easy to misread. `Cpc/SmtModel.lean` is
generated from the signature by the compiler that generates the checker, while
the README and `docs/smt-lib-conformance.md` call it independent. Those two pages
also predate #489's handling of uninterpreted-sort cardinality. `native_decide`
is undocumented. `scripts/run-ci.sh` and `scripts/check-checker-soundness.sh`
still say 591 rule files.
**Channel:** **upstream, by a person**.
**Next:** decide whether `reference` should be honoured or the limit only stated.
**Prompt — `logos`:** correct these statements against the code, and state the
trusted base in one place: Lean's kernel and compiler, the unverified parser and
the generated specification.
**HUMAN FEEDBACK:**

## B47 — run real cvc5 proofs through logos on a schedule

**Task:** protect the end-to-end path, which nothing runs automatically today.
**Entities:** `cvc5`, `logos`
**Status:** ready — read 2026-11-05. cvc5's `cpc_logos.yml` checks signature sync
and that logos's CI passed at the pin; it does not pass `--tester cpc-logos`.
cvc5's logos pin (`contrib/get-logos-checker`) is `a4ab2f8`, 9 logos commits
behind `75c7ee67` and before #484 and #489. A one-off run on 2026-11-04, with a
modified safe-mode cvc5 build, returned `correct` on 709 of 758 applicable
regressions; 711 of the 1,469 `unsat` files were not applicable. Ethos passed
757, and logos accepted nothing ethos rejected.
**Channel:** **upstream, by a person**. cvc5 owes this ecosystem nothing; this is
its maintainers' decision.
**Next:** repeat the run on an unmodified safe-mode build and record the result.
**Prompt — `cvc5`:** consider a nightly safe-mode job running
`--tester cpc-logos`, and moving the logos pin past #489.
**Prompt — `logos`:** say which revision is ready to be pinned.
**HUMAN FEEDBACK:**

## B48 — triage the parser disagreements from the 09-25 fuzz campaign

**Task:** decide which logos and ethos disagreements are defects.
**Entities:** `anoieu`, `logos`, `ethos`
**Status:** ready — read 2026-11-04. The gitignored campaign
`fuzz-findings/20260925-mixed` in anoieu's checkout (12,000 cases, 37 buckets) was
never triaged. Replayed with a logos built 10-16 and an ethos built 09-25, 30
buckets still disagree: 21 where logos refuses, 8 where logos accepts what ethos
refuses, 1 ethos fatal. Five of the 8 were read: parser laxity on assumption sets
that really are contradictory, such as `(step -1 ...)`, not soundness failures.
Three remain unread. Bucket `ty-bbdf0a` matches a row withdrawn as a shrinker
artefact and needs another look.
**Channel:** **findings**, through anoieu and carried by a person.
**Next:** rebuild both checkers, replay, and read the remaining 3 buckets.
**Prompt — `anoieu`:** promote what survives into the bug database with its
reproducer and recorded revisions.
**Prompt — `logos`:** decide whether step ids and declarations should be parsed
strictly, since the parser is trusted code.
**Prompt — `ethos`:** assess any bucket that survives as an ethos defect.
**HUMAN FEEDBACK:**

## B49 — measure logos beyond the regression suite

**Task:** learn what logos handles on real benchmark families.
**Entities:** `logos`, `cvc5`
**Status:** not started — read 2026-11-04. Only regressions have been measured,
and no SMT-LIB family figures exist. In that run `fp` passed 0 of 26 and `ho` 0 of
51, with 29 skips for lambdas and 3 likely timeouts. One file is rejected by logos
alone, `regress1/quantifiers/dd.binary_trees.adb_1105_16_loop_invariant_init_1.smt2`
(*stuck while loading assumption 2*, mutual datatypes). Its cause is undiagnosed.
18 cvc5 regressions are disabled for logos as taking over 600 s. Eight carry a
*parametric datatypes unsupported* comment that may predate #484.
**Channel:** **upstream, by a person**.
**Next:** diagnose the `dd.binary_trees` rejection.
**Prompt — `logos`:** diagnose that rejection, then sweep safe-mode logics for
timing and rejection rates with a recorded baseline.
**Prompt — `cvc5`:** re-check whether the disabled regressions' comments still
apply after #484.
**HUMAN FEEDBACK:**

## B50 — write the logos and ethos-eoc paper

**Task:** publish the construction, with its theorem stated exactly.
**Entities:** `logos`, `ethos-eoc`
**Status:** blocked on `B45` and `B46`, which supply the statement the paper must
open with. [Ynoia's assessment](../tools/ynoia/docs/papers.md#logos-and-ethos-eoc--one-result-two-trees)
gives the argument; the repositories' own stance on publishing remains unstated.
Where it lives is theirs to decide.
**Channel:** **upstream, by a person**.
**Next:** decide whether to write it, and in which tree.
**Prompt — `logos`:** outline what the theorem covers, what it trusts and what
regeneration costs, using `docs/smt-model-definitions.pdf` as the starting point.
**Prompt — `ethos-eoc`:** outline the compilation it would need to describe.
**HUMAN FEEDBACK:**

## B51 — decide the licences

**Task:** give outsiders a clear right to reuse this work.
**Entities:** `kanon`, `logos`
**Status:** waiting on the maintainer — read 2026-11-05. Of the 16 checkouts on the
maintainer's machine, only ethos licenses its own code; logos's `licenses/` covers
lean-smt alone. Choosing a licence is a person's decision, and for a repository
with other contributors it is not one person's alone.
**Channel:** **internal** decision, then each repository's own.
**Next:** choose a licence for logos first, because the paper depends on it, then
for tutorials and the rest.
**Prompt — `kanon`:** policy states no licence requirement; do not add one as part
of this item.
**Prompt — `logos`:** once chosen, add the licence alongside the existing lean-smt
notice.
**HUMAN FEEDBACK:**

## B52 — turn the two red members green

**Task:** repair dokimasia's tests and tachyon's policy check.
**Entities:** `dokimasia`, `tachyon`
**Status:** ready — read 2026-11-04. dokimasia's `checks` run on `b9102ba` failed.
`tests/test_pin.py` fails at that commit and passes with the uncommitted link
cleanup in the maintainer's checkout applied to a scratch copy; the `ratchets` job
needs a cvc5 checkout and was not run. tachyon's local check fails one link,
`tools/heuresis/docs/progress.md` to `directions.md#the-reference`. Its hosted
result was not read, because the API limit was reached.
**Channel:** **internal** to each repository.
**Next:** commit dokimasia's cleanup after review, and read both hosted runs.
**Prompt — `dokimasia`:** review and commit the uncommitted cleanup.
**Prompt — `tachyon`:** repair that link.
**HUMAN FEEDBACK:**

## B53 — bring anoieu's bug database up to date

**Task:** rerun closure against current checkers.
**Entities:** `anoieu`
**Status:** ready — read 2026-11-04 at anoieu `cde5672`. Row `d88112e3` (logos
accepted a wrong `contra` conclusion) no longer reproduces after logos #481. Nine
`accepted and fixed` rows are marked awaiting landing though their fixes are on
ethos main. `48d0d199` has changed behaviour, and `4bdbda42`'s note that `forall`
also fails is stale. The fuzzer's default logos binary predates logos #471, so it
can report defects that are already fixed.
**Channel:** **findings**, carried by a person where another owner is involved.
**Next:** rebuild both checkers, set `$LOGOS` and `$ETHOS`, and run closure.
**Prompt — `anoieu`:** run `prompts/close_bug_db` against those builds and stop
defaulting to a stale binary.
**HUMAN FEEDBACK:**

## B54 — finish the two cvc5 candidates one step from done

**Task:** carry a measured rewrite and an unfiled crash to a decision.
**Entities:** `metagraphe`, `heuresis`, `tachyon`, `cvc5`
**Status:** ready — read 2026-11-04. Metagraphe's `M-25`
(`str.replace_re_all x (re.* re.allchar) "" -> ""`) records one input going from a
60 s timeout to 4 ms at cvc5 `40a4bb7e`. It is not implemented, and a probe on a
current binary still times out at 15 s. Heuresis's segfault on 2 benchmarks has
never been filed and was not re-run. Tachyon has landed nothing in cvc5 so far.
**Channel:** **upstream, by a person**.
**Next:** reproduce the segfault on current cvc5 main.
**Prompt — `metagraphe`:** implement `M-25` beside `str-replace-re-all-none` and
measure the `lan-rep-all` family.
**Prompt — `heuresis`:** re-run the segfault on current main, then prepare the
report already drafted in `docs/upstream-questions.md`.
**Prompt — `tachyon`:** no action beyond hosting these two.
**Prompt — `cvc5`:** assess whichever of these arrives with a reproducer.
**HUMAN FEEDBACK:**

## B55 — decide which quiet projects to park

**Task:** record which quiet projects are parked, so their documents stop implying
work is under way.
**Entities:** `kanon`, `paideia`, `tachyon`, `eudaimonia`, `eschaton`, `iogos`
**Status:** waiting on the maintainer — read 2026-11-04. Since 10-10 only logos and
ethos have moved. The review recommends keeping anoieu's fuzzer and dokimasia,
which feed `B48` and `B53`, and parking the following with a one-line status each:
anakrisis and empeiria (no real PR or bug handled), elaphros (no experiments),
noesis, hermeneia, apodeixis and workflow-launcher (no consumer found), eschaton's
children (proposals only) and iogos (no soundness proof, and no consumer found).
dokimasia needs a refresh if kept: it is 67 cvc5 commits behind, and cvc5 #13035
overtook its `set.choose` candidate. `tekton`, a stub on GitHub, is in no register.
**Channel:** **internal** decision; each parent records its own status.
**Next:** accept, change or reject that list.
**Prompt — `kanon`:** after the decision, record the outcome where each parent
carries it. Parking changes no footing.
**HUMAN FEEDBACK:**

## B56 — freeze governance, and settle what the freeze leaves open

**Task:** stop new governance work, and decide the leftovers an agent cannot.
**Entities:** `kanon`, `stathmos`
**Status:** waiting on the maintainer — read 2026-11-05. Four decisions remain:
- **LAW 10.** It says every investigation is recorded and that a governance review
  is one, yet the report card, epikrisis's audits and euthyna have no records.
  Either declare them or narrow the law.
- **The report card.** It was graded 2026-09-19 and cites `docs/misc/`, which no
  longer exists. It may take a dated caveat or a new round, and it is first on the
  [supervision ladder](maintenance.md#the-supervision-ladder).
- **Discussion files.** Across the checkouts, 80 live topics remain and the last
  parsed reply is from 09-20. The gate requires a person to name each topic acted
  on. That includes `D31`, on logos's cache key: the key is unchanged and logos
  keeps no discussion file to receive it.
- **Rules no one has exercised.** Candidates include limbo, the volunteered-owner
  route and the kanon-ball mark. Removing them is a person's choice.
**Channel:** **internal**.
**Next:** decide whether to record a rule that no new governance is added without
a real incident.
**Prompt — `kanon`:** make only the changes the maintainer names. This item is not
licence for another governance pass.
**Prompt — `stathmos`:** regrade only if asked.
**HUMAN FEEDBACK:**

## B3 — resolve the remaining unreported ethos diagnostic

**Task:** decide whether `(include "no-such-file.eo")` should report the source
location of the include command.
**Entities:** `ethos`, `anoieu`
**Status:** ready — source reread 2026-11-05 at ethos `6cfb7ba7`.
`src/input.cpp` still handles an open failure with `EO_FATAL()` and the filename.
The runtime diagnostic has not been rechecked against a build of this revision.
This is the
remaining path from the historical `ethos-9` observation; the other accepted
diagnostics need no new report.
**Channel:** **findings**, through anoieu and carried by a person.
**Next:** reproduce the missing-include diagnostic with a build at a recorded
revision, then file it or withdraw the observation with a reason.
**Prompt — `ethos`:** assess whether a missing-include diagnostic should carry
the include command's source location, using the confirmed reproducer.
**Prompt — `anoieu`:** prepare the remaining diagnostic through the current
[bug database](https://github.com/ajreynol/anoieu/blob/e5c0dca77da5beced6fa3c4c267d2335bdbf2d7d/bug_db/README.md)
and reporting policy. Record the revision and reproducer before recommending
a report or withdrawal.
**HUMAN FEEDBACK:** raised 2026-08-31: these are real defects and nothing is
stopping us filing them.

## B33 — update the ethos user manual from sapheneia's advice

**Task:** correct the remaining supported issues in ethos's `user_manual.md`.
**Entities:** `ethos`, `sapheneia`
**Status:** ready — rechecked 2026-09-30 against
[ethos `08e4aa40`](https://github.com/cvc5/ethos/blob/08e4aa40c4f8a6e00833f10e8d8985777e424027/user_manual.md)
and [sapheneia's ledger at eunoia `8115ed7`](https://github.com/ajreynol/eunoia/blob/8115ed761649fdd038b050b525b4e7e9d7d04f4d/tools/sapheneia/docs/feedback.md).
`EOM-01` and `EOM-02` remain fixed. The six observations `EOM-03`, `04`, `06`,
`07`, `11` and `15` remain visible: undocumented forms, datatype operations,
nil-terminator wording and `eo::nil` arity. The seven judgement entries
(`EOM-05`, `08`, `09`, `10`, `12`, `13`, `14`) still need a language-aware review.
**Channel:** **upstream, by a person** — sapheneia is reached through eunoia.
**Next:** prepare corrections for the six confirmed entries for ethos's review.
**Prompt — `ethos`:** review the supported manual corrections and record which
are applied, declined or require a language decision.
**Prompt — `sapheneia`:** prepare those six corrections against the named
manual revision. Keep the seven judgement entries explicit as unreviewed
questions; they need not delay the supported corrections.
**HUMAN FEEDBACK:**

## B43 — align the ownership check with ecosystem accountability

**Task:** bring anoieu's ownership-link check into agreement with the
[ecosystem-maintainer scope](policy.md#human-maintainers) and
[author-credit convention](policy.md#authors).
**Entities:** `kanon`, `anoieu`
**Status:** ready — rechecked 2026-09-30 at anoieu `e5c0dca`.
[`check_owner_unadvertised`](https://github.com/ajreynol/anoieu/blob/e5c0dca77da5beced6fa3c4c267d2335bdbf2d7d/policy_check/checker.py)
still requires the shared link in `docs/maintenance.md` and rejects personal
`Owner` lines. The policy already distinguishes ecosystem accountability,
local maintenance and author credit; implementation remains in anoieu.
**Channel:** **discussion**, carried by a person to anoieu.
**Next:** prepare the specific checker correction against the clarified policy.
**Prompt — `kanon`:** identify where the check conflates ecosystem
accountability with project ownership. Keep the correction within its existing
home-only scope; broader automated obligations need a separate decision.
**Prompt — `anoieu`:** revise the home-only check to respect the distinction
between ecosystem maintainers, local maintainers and author credits.
**HUMAN FEEDBACK:** 2026-09-20: name human maintainers for the ecosystem;
keep personal author credits in `AUTHORS`, not on front READMEs.

## B44 — verify the investigation records and their evidence

**Task:** resolve the evidence gaps in the five declared investigations.
**Entities:** `kanon`, `anoieu`, `dokimasia`, `tachyon`
**Status:** ready — reviewed 2026-09-30. LAW 10 and the five
[`_pursuits` records](../scripts/ecosystem/ecosystem.json) are already adopted.
Ethos's publication reference remains incomplete, and the recorded `scope`,
`started` and `closes` still need the responsible maintainers' evidence.
**Channel:** **internal** review; a person carries any requests for evidence.
**Next:** locate the full ethos IJCAR 2026 reference for the register.
**Prompt — `kanon`:** check the records against maintainer evidence. `started`
records when work began, while `declared` records when the declaration was
written; do not reconstruct a start date without that evidence. Review whether
heuresis and elaphros need declarations on the same basis as metagraphe.
**Prompt — `anoieu`:** supply evidence for the scope, start and closing
conditions of your three recorded investigations.
**Prompt — `dokimasia`:** supply that evidence for the cvc5 investigation.
**Prompt — `tachyon`:** supply that evidence for metagraphe and clarify whether
heuresis or elaphros also qualify for declaration.
**HUMAN FEEDBACK:**

## B39 — clarify whether discussion links advertise an unadvertised child

**Task:** align the written advertising rule and the checker's coverage.
**Entities:** `kanon`, `eudaimonia`, `anoieu`
**Status:** waiting on the maintainer — rechecked 2026-09-30. The
[policy](policy.md#child-projects) forbids links inward from anything a user
reads. At anoieu `e5c0dca`, `check_child_unadvertised` checks the parent's
README; `shared_surfaces` also observes its documentation index. Neither
settles discussion links. `D23` records the unresolved question.
**Channel:** **internal** decision, then **discussion** if implementation
needs to change in anoieu.
**Next:** decide whether the parent's discussion may link to an unadvertised
child, and state the resulting policy and checker coverage consistently.
**Prompt — `kanon`:** resolve the concrete question about discussion links
before asking for broader checking.
**Prompt — `eudaimonia`:** the question remains open; no new correspondence
format or status field is needed to decide it.
**Prompt — `anoieu`:** after the policy decision, align the check or its stated
coverage with that decision.
**HUMAN FEEDBACK:**

---

## How to maintain this page

- Order items by priority, highest first. Move whole items without changing
  their ids. Never reuse an id. **The next unused id is `B57`.**
- Keep at most 24 active items. Remove completed or abandoned work; Git and
  the relevant project records preserve the outcome. Review the cap when the
  entity count changes, recording any increase and its reason in
  [`history.md`](history.md).
- Keep items for concrete unresolved work. Optional notices and extra
  bookkeeping alone do not need an open item.
- A person may edit any field. **HUMAN FEEDBACK** takes precedence over the
  other fields; leave it empty until feedback is given.

Use these fields in order:

| field | what it holds |
| --- | --- |
| **Task** | the work in one sentence |
| **Entities** | involved ids from [`ecosystem.json`](../scripts/ecosystem/ecosystem.json) |
| **Status** | `ready`, `in progress`, `waiting on <entity>`, `blocked on <what>`, `not started`, or `parked`, with a date or reason |
| **Channel** | `internal`, `discussion`, `findings`, or `upstream, by a person` |
| **Next** | one next action |
| **Prompt — `<entity>`** | a draft request for each entity involved |
| **HUMAN FEEDBACK** | the maintainer's direction |

**Prompts are drafts.** A person carries anything outside this repository.
Use `discussion` where the recipient keeps a discussion file, `findings` for
defects through [anoieu's bug database](https://github.com/ajreynol/anoieu/blob/e5c0dca77da5beced6fa3c4c267d2335bdbf2d7d/bug_db/README.md)
and [reporting policy](https://github.com/ajreynol/anoieu/blob/e5c0dca77da5beced6fa3c4c267d2335bdbf2d7d/bug_db/reporting-policy.md),
and `upstream, by a person` for other external messages. Check the recipient's
tree; child projects are reached through their parent. `internal` work stays
here.

Close an item when its work is complete or no longer worth pursuing.
Delivery alone does not resolve the underlying work. Role handoffs follow
[`roles.md`](roles.md#how-a-role-is-handed-off); a board item is not a prerequisite.
