# Commands

Use Python 3.10 or newer, Bash and Git. Every command below runs from kanon's
checkout; [the joining commands](#the-joining-commands) do not and are described
at the bottom. Commands under `prompts/` launch an assistant unless passed
`--show-prompt`; that flag prints the prompt without launching one.

## Local commands

| Command | What it does |
| --- | --- |
| `scripts/status_eo --check` | Validates inventory structure offline; does not read remote trees |
| `scripts/status_eo` | Shows tool purposes, checkout policy results and topics addressed to kanon |
| `scripts/status_eo --verbose` | Adds the reasons behind policy results |
| `scripts/status_eo --all` | Shows every row the table can show, which today means every recorded child including the unadvertised ones |
| `scripts/status_eo --all-children` | The same rows, and a note per child saying what listing it declared and why |
| `scripts/status_eo --check --online` | Also reads remote membership declarations |
| `scripts/status_eo --protocol` | Reports on the proposed associate protocol |
| `scripts/status_eo --health` | Summarizes policy, discussion and working-hours indicators |
| `python3 scripts/sleep.py` | Reads the local working-hours schedule; returns 0 inside the window, 1 outside it or during a break, and 2 for a refused schedule |
| `scripts/install_eo --dry-run` | Prints the planned clones |
| `scripts/install_eo` | Clones missing repositories and records their locations |
| `scripts/install_eo --status` | Reads the checkouts on this machine |
| `python3 scripts/policy_check.py --root .` | Runs anoieu's checker against this tree |
| `python3 scripts/bump_check.py --root . --dry-run` | Prints the query for the pinned **anoieu** commit; omit `--dry-run` to query CI |

`status_eo --check --online` returns 0 when all requested README comparisons
succeed, 1 for invalid inventory or observed mismatches, and 2 when verification
is incomplete. A network failure is unverified, not evidence against a project.
The ordinary status table is a report, not a CI gate: inspect its policy column
and notes. Associates and outsiders are not checked against the policy.

The working-hours program reads `scripts/schedule.json`, beside it. Both stay
in kanon after martyria and zetesis moved to epikrisis; the health report does
not need an epikrisis checkout to read the schedule. Do not run the clock-based
reminder as a CI gate.

`bump_check.py` checks a commit hash, never a branch name. Missing, unfinished,
unavailable, or incomplete check-run results cannot authorize a bump. The query
requests up to 100 runs and refuses if GitHub reports more than it returns.

## Checkouts and the checker

The installer defaults to siblings of kanon. `--root PATH` or `EO_ROOT` selects
another installation directory. Repositories marked `outsider` are never cloned,
even when named explicitly or with `--with-optional`; `--status` still lists them.
It stores checkout locations in the untracked
`scripts/repos.local`, with one `ID PATH` pair per line. Existing mappings are
preserved. `ANOIEU_REPOS_FILE` selects a shared mapping file for both repositories;
`ANOIEU_REPOS` is a colon-separated list of search directories. Status and host
prompts also look beside kanon and in the user's home directory.

The checker implementation remains in anoieu. `ANOIEU_ROOT` explicitly selects
that checkout; otherwise kanon looks in the mapping, search directories, and
the sibling/home locations. Both the older `tools/policy_check.py` and newer
`scripts/policy_check.py` layouts are supported. The local launcher checks kanon
by default and reports `UNVERIFIED` with exit code 2 if the checker is unavailable.
It does not fetch or update the checkout.

Installation status can be read before anoieu is installed. When available,
anoieu's `scripts/deps.json` supplies its report dependency pins; kanon does
not keep a duplicate. The installer and status commands share
[`ecosystem.json`](../scripts/ecosystem/ecosystem.json) as their inventory.
The `purpose` column in `status_eo` reads an entry's optional `short` field,
falling back to `what`. Keep `short` around 60 characters or fewer; longer text
is shortened at a word boundary with an ellipsis. `what` keeps the full description.

## Child project listings

**A repository that declines to announce its membership is a different thing**,
and is not done here: it takes the `associate` footing, recorded on its own
maintenance page. It owes us nothing, its tree is checked anyway, and the row
reads `N tracked` because nobody is at fault for the number. See
[the footings](policy.md#the-footings).

A parent repository chooses which children to advertise. Children with a readable
README are advertised by default. To omit a child from `status_eo` and the
installer's generated child summaries and branch advice, put
this standalone line in the child's `README.md` introduction, before the first
`##` (or deeper) heading:

```markdown
**Eunoia listing:** unadvertised
```

Use `advertised` to explicitly opt in. A README without a declaration is
advertised by default. Code examples, HTML comments, block quotes and ordinary
prose do not count as declarations. Multiple declarations or an unsupported
value are unverified and do not opt in.

Both commands read the local parent checkout and the child's inventory `path`.
They read the currently checked-out version, without fetching or switching to
the child's recorded `branch`. A missing parent, missing path, or unreadable
README leaves the preference unverified; a note names the parent and the reason,
without listing the affected children. The installer reads from `--root` (or its
default), and reads again after cloning when producing branch advice.

`status_eo --all-children` includes every recorded child with its preference and
any read error. Normal table counts include only displayed children. Inventory
validation, child ID resolution and `scripts/repos.local` mappings still use
the complete inventory. Choosing to advertise does not change a child's status
or promote it into a repository. Handwritten descriptions are not filtered.

Existing child READMEs without the declaration remain advertised. A parent can
opt individual children out by adding the declaration above. The choice is kept
only in that README, not copied into kanon's inventory.

## Prompt previews

```sh
prompts/check_join_eo --show-prompt ../anoieu
prompts/global_audit --show-prompt
prompts/process_discussion --show-prompt ../anoieu
```

All three prompts here run in kanon. A topic id passed to `process_discussion`
authorizes work on that topic; a preview or a call with no topic id authorizes
no reply. `check_join_eo` runs the local checker even in preview and stops if it
cannot run. `global_audit` collects `status_eo --all --verbose`, preserving
unavailable checks in the report. Neither launches an assistant during preview;
both request read-only assessments when launched. They write no audit file,
discussion topic, or checkout mapping. Named discussion topics are worked here.

## The joining commands

`eo_init` and `eo_join` are not in this tree. They are the two commands that run
**inside the repository being started or joined**, they are `R35` in
[`roles.md`](roles.md), and [koine](https://github.com/ajreynol/koine) maintains
them. Install them onto a path with that repository's `install_eo_cmd` rather
than running them from here; `--show-prompt` prints what either would hand an
assistant.

What they ask of a repository is this repository's: [`policy.md`](policy.md) is
the authority, and `eo_init` reads [`glossary.md`](glossary.md) as the
authoritative name register, reporting any glossary entry or location update
owed to the president.

## Retired commands

`confirm_eo` and `welcome_eo` were removed. Confirmation repeated the joining
assessment, assigned subjective grades, and carried stale handoff instructions.
Welcoming mixed checkout registration with unsolicited topic drafting and assumed
the target had not joined. Neither is a necessary verification step.

Use `policy_check.py --root PATH` for mechanical checks and `check_join_eo PATH`
only when a read-only interpretation would help. Use `install_eo --status ID` to
inspect a checkout. For existing checkouts elsewhere, edit `scripts/repos.local`
with one `ID PATH` pair per line; registration does not change membership.

The temporary `ready_check.py` and `transfer_check.py` were also removed: no CI
job used them, and neither established both repositories' CI at the commits
being transferred. Follow the [role-transfer protocol](protocols.md#proto-26--transferring-roles-to-another-project)
and inspect those runs directly. Presidency decisions remain with a person
under [the laws](laws.md).

## Validation

```sh
python3 -m unittest discover -s tests -v
scripts/status_eo --check
python3 scripts/policy_check.py --root .
```

The regression suite checks document links, glossary project footings and parents,
transferred project locations,
installer behavior, checker discovery and unavailable-checker reporting, and
prompt previews. It uses temporary fixtures and does not launch assistants,
clone repositories or contact the network. CI runs it alongside inventory
validation. The separate policy job keeps the existing anoieu checker pin.

`scripts/anoieu_dependency.py` supplies checkout discovery for the local
launcher and status readers. `scripts/ecosystem/ecosystem.py` implements
`status_eo`. `scripts/child_listing.py` reads the README listing declaration
for both status and installation.
