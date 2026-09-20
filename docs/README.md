# The documentation

**Every page in `docs/`, and what each one settles.** Grouped the way
[`../README.md`](../README.md) groups them: the documents written for every
repository in the ecosystem, the documents that record this term, and ideas
kept for consideration.

## Shared — written for every repository, not just this one

| document | what it settles |
| --- | --- |
| [`policy.md`](policy.md) | repository layout, ownership, maintenance, child projects and membership requirements |
| [`vision.md`](vision.md) | the five tenets this development aims at, the argument for them, and what follows for anything that leaves the repository. Argued, and never checked |
| [`laws.md`](laws.md) | the candidate laws — the footings, the presidency, and what the office owes |
| [`glossary.md`](glossary.md) | the authoritative name register and alphabetized dictionary of eo's terms, maintained by the president |

## The office, and this term's work

| document | what it records |
| --- | --- |
| [`history.md`](history.md) | the term record — what it is for, what changed, what went wrong, what crosses to the next president, and what the next term should be for |
| [`board.md`](board.md) | what is being maintained across the ecosystem, in priority order, each item with its next step and whose it is |
| [`roles.md`](roles.md) | every responsibility, who holds it, and what is deliberately not part of it |
| [`maintenance.md`](maintenance.md) | **start here to maintain this tree**: what this repository is responsible for, what it checks, and what is outstanding |

[`discussion.md`](discussion.md)

## Ideas for consideration

| document | what it is |
| --- | --- |
| [`brainstorm.md`](brainstorm.md) | `X<N>` proposals for offices, comparisons and working practices, with status, revisit conditions and an item template; no assignment or commitment implied |

## What is not here

**Nothing in `docs/` is generated.** Every page above is written by hand, which
is why none of them carries a generated-file banner and why anything a tool
produces belongs somewhere else.

**No page here documents the commands.** Each one says what it takes and prints
at the top of its own file, and `eo_status_audit --help` carries the key to the
table — which is where a reader who is about to run something already looks.

**The child projects under [`../tools/`](../tools) keep their own documentation
indexes.** This index covers kanon's `docs/`; each child documents its work at
its source. `scripts/eo_status_audit --all-children` lists every recorded child.
Links to advertised children's shared work follow the parent's
[listing preference](policy.md#child-projects).
