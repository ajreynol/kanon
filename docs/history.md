# History — kanon's term

**kanon's account of its own term holding the presidency of the Eunoia
ecosystem.** It stays in this tree. It does not travel to whoever holds the
office next, and kanon inherited no such page from anyone: the accounts scatter,
one per repository that has held the office.

**It is kept current while the term runs, not written at the end from memory.**
A summary composed afterwards is a reconstruction, and a reconstruction by the
party being described is the weakest document this ecosystem produces.

## What you need to know to read this page, and nothing more

**The Eunoia ecosystem is a handful of repositories built around one proof
calculus**, each with a human maintainer who is the authority over it. A
repository's **footing** says what it owes the ecosystem and what the ecosystem
says about it. A **member** has declared, on its own front page, that it is part
of the ecosystem and runs the shared policy checker in its own CI. A
**candidate** has not joined; the policy is addressed to it and binds it to
nothing. The other footings do not appear on this page.

**The presidency is one member that also holds an office, for a stretch.** It
sets direction and nothing more — it cannot require anything of a member the
shared policy does not already require, and it confers nothing over anybody's
repository. It is bestowed by a person, it expires with the stretch, and handing
it on is the point.

**One file decides who holds it**, and it is
[`../scripts/ecosystem/ecosystem.json`](../scripts/ecosystem/ecosystem.json):
the repository whose entry reads `status: president` is the president. Anything
else that says so — a front page, a letter, this page — is downstream, and where
one of them disagrees with that file, that file is right.

**Everything below is a fact somebody else can check.** Every commit named here
is public, and the command that re-derives each figure is given beside it. A
number only kanon can produce would be the party being described choosing the
numbers that describe it, and does not go on this page.

## What this page covers today, and what it is expected to become

**Today it records membership changes and nothing else.** That is a deliberate
starting scope rather than the finished shape of a term record: it is the part
most likely to be wrong if nobody writes it down as it happens, and the part
that is cheapest to keep honest, because every entry is a dated commit in a
public tree.

**The rest of a term record is drafted and not yet carried here.** Its other
fields — what the term was for, how long it ran, what became true, what went
wrong across the whole stretch, what is handed on — are kept as a draft in
[`../working-summary.md`](../working-summary.md). They move here as they stop
being drafts. That page is optional depth; this one is meant to stand alone.

**An earlier entry may be corrected, and never silently.** The burden is on
whoever edits it to show that the earlier text was wrong or can be bettered, and
the demonstration goes in the edit. *It was unclear* is not a demonstration;
*this figure disagrees with the commit history, here* is. Corrections are
collected at the foot of this page.

## The term

**It began at kanon `7eb9973`, 2026-09-15 16:15:45 −05:00** — the commit in
which the registry first recorded `status: president` against kanon. The office
is bestowed by a person editing that line, so that commit is the start of the
term and not an approximation of it.

**It has not ended.**

**The registry itself moved in the same minute.** anoieu deleted its copy at
`ca58216`, 16:14:44, and this tree created the one that replaced it at
`7eb9973`, 16:15:45 — so for sixty-one seconds no repository anywhere held the
file that decides who the president is. Nothing depended on it during that
minute and nothing was harmed by it. It is here because a gap in the one record
that is supposed to have no gaps is exactly what a later reader would have no
way to find.

*Re-derive:* `git log -S'"status": "president"' -- scripts/ecosystem/ecosystem.json`
in this repository, and `git log --diff-filter=D -- scripts/ecosystem/ecosystem.json`
in anoieu.

## Membership changes during this term

Each row names the commit in the joining repository's **own** tree where the
declaration landed, the commit here where the register caught up, and the
commit of the repository that held the shared policy at that moment — which is
the coordinate the register keeps in its `joined` field.

| when | tool | change | declared, in their tree | recorded, here | policy at the time |
| --- | --- | --- | --- | --- | --- |
| 2026-09-15 16:15 | `kanon` | member → president | — | `7eb9973` | — |
| 2026-09-16 05:23 | `tachyon` | not in the register → member | `cbd8eb2` | `226d534`, 06:32 | `kanon 4c4a78a` |
| 2026-09-16 06:24 | `eschaton` | not in the register → candidate | — | `2a6aac1` | — |
| 2026-09-16 07:02 | `eschaton` | candidate → member | `50c780d` | `0c507d9`, 07:22 | `kanon c95ab21` |

**No repository left, and no footing was withdrawn.**

**Three of the four rows are somebody else joining; the first is the office
moving.** It is on the same table because the presidency is a footing in the
same register and moves by the same act — a person editing one line — and a
membership record that omitted the one change kanon made to its own row would be
the page's most obvious blind spot.

*Re-derive:* in the joining repository,
`git log -S'part of the **Eunoia ecosystem**' -- README.md` gives the
declaration commit and its date. Here,
`git log -S'"tachyon"' -- scripts/ecosystem/ecosystem.json` gives when the
register first carried that tool, and `git log -p` on the same file gives every
change to its footing. The policy commit is this repository's tip at the moment
the declaration landed, from `git log --format='%h %cI'`.

**Joins before this term are not here**, because this page is an account of this
term. Seven repositories were already on a membership footing when it opened —
six members, one of them kanon, and anoieu holding the office — and every one of
them joined while anoieu kept the policy. Six of their entries carry an `anoieu`
commit for the same reason the rows above carry a `kanon` one; anoieu's own
carries nothing, because that join was never recorded at the time. anoieu's
account covers that stretch, and this page does not restate it.

## What went wrong

**This page arrived about fifteen hours late.** The registry recorded kanon as
president at 16:15:45 on 2026-09-15; this page landed at about 07:30 the next
morning. In between, the tree could not hold the office — a named state, the
registry saying a repository is president while its tree does not carry the
files the office is kept in. One of the two was there from the start: the same
commit that moved the office carried `laws.md` and the check that reports the
state, so `../scripts/status_eo` printed it against kanon's row for the whole
fifteen hours, correctly, and this page was the only thing missing. It is
supposed to be fixed quickly. Fifteen hours is not quickly, and past some point
the honest repair stops being to write the account and becomes to put the
registry line back.

**Both joins were recorded after the fact rather than as they happened.**
tachyon declared at 05:23 and the register moved at 06:32, sixty-nine minutes
later. eschaton declared at 07:02 and the register moved at 07:22, twenty
minutes later. Neither lag did any damage, and neither was noticed by anybody
reading: eschaton's was found by `../scripts/status_eo --check --online`, which
reads each member's front page and fails when the register disagrees with it.
**That is the check working and the habit not**, and the check is the weaker of
the two, because it only ever runs when somebody runs it.

**The register is hand-maintained, and that is the design.** A footing is a
decision rather than a fact about a tree, so nothing derives this file and
nothing ever should. The cost is exactly the lag above, and the only mitigation
is somebody running the check.

## What this page does not settle

**Whether a membership record belongs here at all.** The law that creates this
page makes it an account of *this* repository, and who joined is a fact about
somebody else's repository as much as about ours.
[`laws.md`](laws.md) lists where that record lives among the things the laws do
not settle, and calls it the first gap to close. **This page is a provisional
answer to that question and not an amendment to anything**: the laws are the
maintainer's to change, and nothing here changes them.

**The weakness is structural and is worth stating rather than discovering
later.** This account does not travel, so a membership log kept here covers one
term and stops. A successor's page starts empty, and
[`../scripts/ecosystem/ecosystem.json`](../scripts/ecosystem/ecosystem.json)
stays the only place the whole picture lives. If the log turns out to be worth
keeping, that is an argument for putting it somewhere that travels — not for
copying it forward into each new president's tree, which is how a trail starts
getting flattering.

## Corrections

**None yet.** An entry corrected after the fact is listed here with the
demonstration that the earlier text was wrong.
