# The office of safety for kanon

**How could this infrastructure be *persuaded* into failing?**

**The verb is the scope.** This ecosystem runs on agents reading documents and
following protocols, so its attack surface is **documents and procedures**, not
memory. An attacker here does not break a thing; they arrange for a correct
procedure, followed faithfully, to produce a wrong outcome. **Every defence
written down so far has that shape**, and so does every accident.

## The organising question

**Find every irreversible act, and check that a person is required for it.**

`PROTO-20` already states the pattern for one of them: *an agent never deletes a
stub. It gathers, it reports, and it refuses. A person deletes. No amount of
evidence moves this.* **That is the whole defence, and it works because no
argument can move it** — an agent that could be convinced by a sufficiently good
case is an agent that can be convinced by a sufficiently good forgery. This
office's standing job is to find where that pattern is **missing** and should
not be.

**The kinds of failure are in [`scenarios.md`](scenarios.md)** —
misinterpretation, deadlock, misappropriation, and exhaustion — with the
ownership stance audited at the end. **This page lists surfaces; that one lists
modes.**

## Six surfaces, all of them already documented

**None of these is a discovery and none is a criticism.** Each is a thing the
ecosystem has already written down, read as an attack rather than as an
incident.

1. **The pinned checker is a supply chain.** `policy_check.py` runs in **three
   members' CI**, fetched from a URL, at a commit each member pins. `D16`
   already mitigates part of it — *only move your pin to a commit where our CI
   is green*. **`P2` hands this to kanon**, which means the president is about
   to own the one thing that executes inside everybody else's build. That is the
   most consequential safety fact about kanon's own future and it is on the
   list as `A33`.
2. **A prompt can arrive in the wrong repository.** `D12` records it happening
   by accident and the rule written afterwards. The deliberate version is a
   prompt that merely *looks* like it came from the tool that governs you.
3. **Documentation is a vector.** `ai-novelty.md` names it already — *a
   misleading change to the documentation is a virus* — and names the mitigation
   in the same breath: **this repository can hide nothing.** Visibility is the
   defence, which is an argument against private working material and worth
   holding against this repository's own offices.
4. **Registers go stale, and staleness is exploitable.** A name has been
   reported free while in use **three times** — `noesis`, `epikrisis`, `telos`.
   Somebody who wants a name does not need to take it; they need the register to
   lag, which it does by default.
5. **A stub can be claimed by a repository that is not doing the work.**
   `PROTO-20`'s stated fraud model, with its defences already written: read the
   repository not the message, asking for more proof is not verification, any
   hint of fraud reject, and the asymmetry that sets the default to **no**.
6. **Layout is an unwritten contract.** Moving `prompts/` out of `scripts/` sent
   two published URLs to 404 with copies already distributed that could not be
   recalled — `A17`. An unwritten contract cannot be broken deliberately or
   otherwise, because nobody agreed to it.

## Not this office

**Finding bugs in anybody's code.** The analyzer does that, `dokimasia` asks
what no proof step covers in cvc5, and neither should be pulled upward into
this — the mistake `K7` records. **This office studies procedures being
persuaded, not programs being exploited**, and the moment it starts reviewing
somebody's C++ it has stopped doing its job and started doing theirs badly.

## Incoming: `science-fiction.md`

**The ecosystem's upper bound** — *the furthest this ecosystem allows itself to
plan* — and `coherence.md` calls it *a safety job rather than an essay*. It sets
a ceiling so that crossing it is **a decision somebody makes rather than a drift
nobody notices**, and it carries the one worked example of the ecosystem
assessing an outside party whose vision is close to its own and concluding **do
not trust it**. That is adversarial reasoning already done, and it is the
natural companion to everything above.

> **One thing to decide rather than drift into.** `coherence.md` records that
> `science-fiction.md` **stays where it is**, in the same breath as calling it a
> safety job. Moving it here reverses a decision that was written down.
> **kanon is not treating the maintainer's instruction as a mistake** — but the
> reversal should be explicit, because a page whose entire purpose is that
> crossings are decided rather than drifted into deserves not to move by drift.
> Carried as `A32`.

**The division, when it arrives:** `science-fiction.md` bounds what the
ecosystem may *plan*. This office studies how it could be *made to fail*. They
meet at first contact — an outside party engaging with a tree that has written
down how it would decide whether to trust one.
