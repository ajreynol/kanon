# The documentation

**Every page in `docs/`, and what each one settles.** Grouped the way
[`../README.md`](../README.md) groups them: the documents written for every
repository in the ecosystem, the documents that record this term, and the ones
that have been demoted.

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

## Demoted

[`policy.md`](policy.md#the-layout) defines `docs/misc/` as optional background.
These pages remain available for the record; keeping one here is not a reason
to postpone deciding whether it should be updated, merged or removed.

| document | what it is |
| --- | --- |
| [`misc/brainstorm-offices.md`](misc/brainstorm-offices.md) | the internal office structure that was proposed and **deferred on 2026-09-15** as premature. Optional background |
| [`misc/conversation.md`](misc/conversation.md) | the verbatim transcript of the session that primed this repository, 2026-09-02. Housed here, and not required reading |
| [`misc/initial-objections.md`](misc/initial-objections.md) | the objections entered when the office was offered and before it was held, recorded then because reservations get remembered as milder than they were |

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
