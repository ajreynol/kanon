# The board

**Outstanding work across the Eunoia ecosystem, in priority order.** Each
item names the next action and who can take it. Stable ids survive reordering;
the maintenance notes are at the bottom.

## B3 — resolve the remaining unreported ethos diagnostic

**Task:** decide whether `(include "no-such-file.eo")` should report the source
location of the include command.
**Entities:** `ethos`, `anoieu`
**Status:** ready — source reviewed 2026-09-30 at ethos `08e4aa40`.
[`FileInput`](https://github.com/cvc5/ethos/blob/08e4aa40c4f8a6e00833f10e8d8985777e424027/src/input.cpp)
still handles an open failure with `EO_FATAL()` and the filename. The runtime
diagnostic has not been rechecked against a build of this revision. This is the
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
  their ids. Never reuse an id. **The next unused id is `B45`.**
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
