# synkrisis

> **The name is proposed and not claimed.** `R22`, the register of names, is
> ynoia's, and a name is claimed when **a person approves one** — never by a
> document suggesting it. Until then this directory is cheap to rename and the
> entry in `names.md` is ynoia's to write. Carried as `A26`.

*σύγκρισις — setting two things side by side; the exercise of comparing.* The
register asks for a word for **what a tool does to its subject**, and this one
compares. It reaches both halves of the job: comparison across agendas finds the
**conflict**, comparison across tools finds the **connection**. *Alternatives
considered: `aporia` — the impasse — which names the conflict well and the
connection not at all; and `diaphora` — difference, and in Attic usage a dispute
— which names the thing found rather than the act of finding it.*

## What it does

**Finds where this ecosystem is pulling in two directions at once, and writes
the conflict down thoroughly enough that somebody else could take a side.**

**The description is the deliverable. The opinion is a bonus and is marked as
such.** Every entry carries an opinion because a description with no reading
attached is a filing cabinet — but the opinion is **uninformed by
construction**, offered by a tool that has not built any of the things it is
comparing and has not surveyed the field. **An entry whose opinion is longer
than its description has failed.**

**It also connects.** Two tools solving one problem in different trees is the
same finding as two agendas pulling apart, seen from the other side, and it is
usually the more useful one.

## Not this project

**Deciding.** `R23` — ynoia's — audits whether an idea deserves a repository and
attaches a verdict. `report-card.md` grades whether work is good and stays with
anoieu. This describes a disagreement; it does not resolve one, and **it has no
authority over anybody's agenda, including this ecosystem's own.**

## The verification agendas — `telos`, `cvc6`, `pathos`

**The conflict, as far as it can currently be stated:** three answers to *what
does this ecosystem ship, and what checks it*. `pathos` is reserved for an
efficient **verified** proof checker — the thing that would let the ecosystem
ship what it proves rather than maintain a second implementation. `telos` is
running. `cvc6` is a direction somebody is holding.

**And the first finding is that they cannot be compared yet, because they are
not recorded on comparable terms.**

- **`pathos`** is in `names.md` under *Reserved*, with an etymology and a
  sentence of scope. It has no repository. `roles.md` says of `R10` that being
  verified is **nobody's** role, and names `pathos` as the reserved answer.
- **`telos` is running and is in no register.** It is a child project with its
  own `docs/` — substantial enough that anoieu's link checker produced
  twenty-two spurious failures against it, recorded in `D6`. It appears in
  **neither** `ecosystem.json` **nor** `names.md`, not even under *In use
  elsewhere, and claimed by nobody*.
- **`cvc6` appears nowhere in anoieu at all.** Not in `vision.md`, not in
  `science-fiction.md`, not on the board, not in either register.

**Uninformed opinion:** the disagreement is probably not really three-way. Two
of these are positions about *the next solver*, and one is a position about
*what proves the current one*. **Until `telos` and `cvc6` are written down
somewhere a reader can find them, nobody outside the maintainer's head can tell
which pairs actually conflict** — and this is the third time this ecosystem has
found a tool that was running and unregistered, after `noesis` and `epikrisis`.
The `In use elsewhere` section of `names.md` exists because of the first two.

**Due diligence still owed:** who owns `telos`, which tree it is in, and what
`cvc6` means to the person holding it. All three are questions for people.

## The two compilers — `noesis` and `ethos-eoc`

**Not a conflict, a connection, and possibly a duplication.**

- **`ethos-eoc`** is *the Eunoia compiler, and the semantics sets it ships* — a
  child project of `ethos`, on branch `ethosEoc3`.
- **`noesis`** is *the semantics and the compiler defined **in** Lean rather
  than compiled into it: a verified Eunoia compiler* — started in `eudaimonia`,
  and found there rather than declared, which is how it moved out of the
  reserved list.

**Around them sit three more readings of the same language.** `ethos` holds
`R10`, the fast unverified C++ checker that *every other reading of the language
is compared to*, and `R11`, the manual, which is *by construction a manual for a
program*. `logos` holds the Lean development where the trust argument
terminates. `pathos` is reserved for the verified efficient checker nobody has
built.

**Uninformed opinion:** that is **five readings of what Eunoia is, in three
trees, two of which have joined nothing** — and the only one with authority is
a manual that its own register says describes a program rather than a language.
`sapheneia` exists precisely to separate those, which suggests the ecosystem has
already noticed. The question worth putting to somebody who knows: **do
`noesis` and `ethos-eoc` expect to converge, or is one of them the replacement
for the other?** Neither entry says, and both are *Started*.
