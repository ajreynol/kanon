# Commands

**`eo_status_audit` was `status_eo` until 2026-09-17.** The name says what is
left for this repository to do once the plain table is an installed command:
koine's `eo_status` reads the register and prints it, and what stays here is the
audit — `--check --online` against remote declarations, and `--protocol`.
**Today this command still does both**, because the audit shares its
register-loading and checker plumbing with the table; the name is ahead of the
split rather than describing it.

Use Python 3.10 or newer, Bash and Git. Every command below runs from kanon's
checkout; [the joining commands](#the-joining-commands) do not and are described
at the bottom. **Nothing here launches an assistant**: the commands that do are
installed, and each takes `--show-prompt` to print what it would hand one.

## Local commands

| Command | What it does |
| --- | --- |
| `scripts/eo_status_audit --check` | Validates inventory structure offline; does not read remote trees |
| `scripts/eo_status_audit` | Shows tool purposes, checkout policy results and topics addressed to kanon |
| `scripts/eo_status_audit --verbose` | Adds the reasons behind policy results |
| `scripts/eo_status_audit --all` | Shows every row the table can show, which today means every recorded child including the unadvertised ones |
| `scripts/eo_status_audit --all-children` | The same rows, and a note per child saying what listing it declared and why |
| `scripts/eo_status_audit --check --online` | Also reads remote membership declarations |
| `scripts/eo_status_audit --protocol` | Reports on the proposed associate protocol |
| `python3 scripts/sleep.py` | Reads the local working-hours schedule; returns 0 inside the window, 1 outside it or during a break, and 2 for a refused schedule |
| `python3 scripts/policy_check.py --root .` | Runs anoieu's checker against this tree |

`eo_status_audit --check --online` returns 0 when all requested README comparisons
succeed, 1 for invalid inventory or observed mismatches, and 2 when verification
is incomplete. A network failure is unverified, not evidence against a project.
The ordinary status table is a report, not a CI gate: inspect its policy column
and notes. Associates and outsiders are not checked against the policy.

The working-hours program reads `scripts/schedule.json`, beside it. **Nothing
else here reads either**: the summary that once folded working hours into the
status table was removed on 2026-09-17, so `sleep.py` now stands alone. Do not
run the clock-based reminder as a CI gate.

**This repository's pin is `anoieu.lock`, and `eo_bump` moves it.** That command
is koine's and is installed rather than kept here; `eo_bump.json` beside the lock
is its configuration. Unknown is not green — a run that cannot reach an answer
changes nothing — and `--force` is a person's decision that the run records.

## Checkouts and the checker

**Repositories marked `outsider` are never cloned**, whatever asks: they are
published work tracked for comparison, and cloning one would be this ecosystem
helping itself to somebody's tree. That rule belongs to whoever writes the
installer, and this page records it because the register is what it reads.
Checkout locations live in the untracked
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
not keep a duplicate. [`ecosystem.json`](../scripts/ecosystem/ecosystem.json) is
the inventory every reader of it shares, and
[`checkouts.json`](../scripts/ecosystem/checkouts.json) beside it holds the
installation exceptions — **nothing here reads that second file any more**, and
it is kept because it is the register's, not the installer's.
The `purpose` column in `eo_status_audit` reads an entry's optional `short` field,
falling back to `what`. Keep `short` around 60 characters or fewer; longer text
is shortened at a word boundary with an ellipsis. `what` keeps the full description.

## Child project listings

**A repository that declines to announce its membership is a different thing**,
and is not done here: it takes the `associate` footing, recorded on its own
maintenance page. It owes us nothing, its tree is checked anyway, and the row
reads `N tracked` because nobody is at fault for the number. See
[the footings](policy.md#the-footings).

**Advertised is the default, and a child that is advertised writes nothing.**
There is no line to add, no field to keep current, and a charter that says
nothing about listing has said the usual thing. Only the exception is written
down.

**To omit a child**, put the footing marker in its own `README.md` — the
current spelling, read exactly as anoieu's checker reads it:

```markdown
**Footing:** `unadvertised-child` — the parent's front page does not name it
```

`**Eunoia listing:** unadvertised` in the README introduction, before the first
`##` (or deeper) heading, predates the marker and still works. So does an
explicit `**Eunoia listing:** advertised`, which is accepted and does nothing
the default does not — **there is no reason to write one.** Code examples, HTML
comments, block quotes and ordinary prose do not count as declarations, an
unsupported value is unverified, and so is a README carrying two declarations
that disagree.

Both commands read the local parent checkout and the child's inventory `path`.
They read the currently checked-out version, without fetching or switching to
the child's recorded `branch`. A missing parent, missing path, or unreadable
README leaves the preference unverified; a note names the parent and the reason,
without listing the affected children.

`eo_status_audit --all-children` includes every recorded child with its preference and
any read error. Normal table counts include only displayed children. Inventory
validation, child ID resolution and `scripts/repos.local` mappings still use
the complete inventory. Choosing to advertise does not change a child's status
or promote it into a repository. Handwritten descriptions are not filtered.

Existing child READMEs without the declaration remain advertised. A parent can
opt individual children out by adding the declaration above. The choice is kept
only in that README, not copied into kanon's inventory.

## Working a discussion topic

`eo_process_discussion` reads another repository's discussion file and works
what is addressed to this one. It is koine's and installed rather than kept
here. **A topic id is what authorises acting**: with no id the run is read-only,
and `--show-prompt` prints what it would hand an assistant and launches
nothing.

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

`check_join_eo` and `global_audit` were removed on 2026-09-17, unused by any
person, job or other repository. **Both were assistant wrappers over commands
this repository already runs.** `check_join_eo` ran the checker and then asked
for a reading of it; `policy_check.py --root PATH` decides the mechanical half,
and `eo_status_audit` already reports the serious case — a repository that declares
membership while our checks fail on its tree — for every member on every run,
with no assistant and no turn spent. `global_audit` collected
`eo_status_audit --all --verbose` and asked somebody to read across it, which is what
reading it is. What went with them is the interpretive half, *whether a
maintenance note says anything or merely satisfies the check*: no program
decided that, and asking it does not need a stored launcher.

**Getting the ecosystem onto a machine is no longer done from here.**
`scripts/install_eo` was deleted on 2026-09-17; koine is building the
replacement, and until it lands there is no installer in this ecosystem.
`scripts/repos.local` is now written by hand — one `ID PATH` pair per line —
and registering a checkout has never changed anybody's membership.

The temporary `ready_check.py` and `transfer_check.py` were also removed: no CI
job used them, and neither established both repositories' CI at the commits
being transferred. Follow the [role-transfer protocol](protocols.md#proto-26--transferring-roles-to-another-project)
and inspect those runs directly. Presidency decisions remain with a person
under [the laws](laws.md).

## Validation

```sh
python3 -m unittest discover -s tests -v
scripts/eo_status_audit --check
python3 scripts/policy_check.py --root .
```

The regression suite checks document links, glossary project footings and parents,
transferred project locations,
checker discovery and unavailable-checker reporting, and
prompt previews. It uses temporary fixtures and does not launch assistants,
clone repositories or contact the network. CI runs it alongside inventory
validation. The separate policy job keeps the existing anoieu checker pin.

`scripts/policy_check.py` locates anoieu's checkout and runs the checker, and
supplies that discovery to the status readers. `scripts/ecosystem/ecosystem.py` implements
`eo_status_audit`. `scripts/child_listing.py` reads the README listing declaration
for both status and installation.
