# Commands

Use Python 3.10 or newer, Bash and Git. All commands below run from kanon's
checkout. Commands under `prompts/` launch an assistant unless passed
`--show-prompt`; that flag prints the prompt without launching one.

## Local commands

| Command | What it does |
| --- | --- |
| `scripts/status_eo --check` | Validates the inventory offline |
| `scripts/status_eo` | Reads checkout policy results and topics addressed to kanon |
| `scripts/status_eo --verbose` | Adds the reasons behind policy results |
| `scripts/status_eo --check --online` | Also reads remote membership declarations |
| `scripts/status_eo --protocol` | Reports on the proposed associate protocol |
| `scripts/status_eo --health` | Summarizes policy, discussion and working-hours indicators |
| `scripts/install_eo --dry-run` | Prints the planned clones |
| `scripts/install_eo` | Clones missing repositories and records their locations |
| `scripts/install_eo --status` | Reads the checkouts on this machine |
| `python3 scripts/policy_check.py --root .` | Runs anoieu's checker against this tree |
| `python3 scripts/bump_check.py --root . --dry-run` | Prints the query for the pinned **anoieu** commit; omit `--dry-run` to query CI |
| `python3 scripts/transfer_check.py TARGET` | Reports pending role markers and destination; CI remains unverified |
| `python3 scripts/ready_check.py NAME --stub-root PATH` | Checks the local name register and a source repository's stub |

`ready_check.py` is the temporary stub check inherited from anoieu. Anoieu
removed the kanon stub in `eeafbcc`, so checking that name now reports no stub;
there is no ready job for it in kanon. Use `--stub-root PATH` only when a
source repository still holds a stub for a future creation.
Completed transfers no longer have pending role markers, so
`transfer_check.py kanon` should report that no transfer is pending.
Neither helper establishes that both repositories' CI passed.

## Checkouts and the checker

The installer defaults to siblings of kanon. `--root PATH` or `EO_ROOT` selects
another installation directory. It stores checkout locations in the untracked
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

## Prompt previews

```sh
prompts/init_eo new --show-prompt
prompts/join_eo --show-prompt
prompts/check_join_eo --show-prompt ../anoieu
prompts/confirm_eo --show-prompt ../anoieu
prompts/welcome_eo --show-prompt anoieu ../anoieu
prompts/global_audit --show-prompt
prompts/process_discussion --show-prompt ../anoieu
```

`init_eo` and `join_eo` run in the receiving repository when actually launched.
The other prompts run in kanon. A topic id passed to `process_discussion`
authorizes work on that topic; a preview or a call with no topic id authorizes
no reply. Policy-reading previews require the anoieu checker too.

## Validation

```sh
python3 -m unittest discover -s tests -v
scripts/status_eo --check
python3 scripts/policy_check.py --root .
```

The regression suite checks document links, transferred project locations,
installer behavior, checker discovery and unavailable-checker reporting, and
prompt previews. It uses temporary fixtures and does not launch assistants,
clone repositories or contact the network. CI runs it alongside inventory
validation. The separate policy job keeps the existing anoieu checker pin.

`scripts/anoieu_dependency.py` supplies checkout discovery for the local
launcher and status readers. `scripts/ecosystem/ecosystem.py` implements
`status_eo`; `scripts/ecosystem/near.py` checks likely spelling mistakes in
repository ids. The root `run_handoff` and `run_handoff_anoieu` files record the
one-time transfer commands and are not installation or verification commands.
