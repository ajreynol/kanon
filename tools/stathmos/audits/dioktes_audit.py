#!/usr/bin/env python3
"""Stathmos's dioktes audit, run through scripts/eo_dioktes_audit.

**What is this ecosystem looking for defects in, on whose authority, and is
that authority still good?** `docs/laws.md` LAW 10 makes a person declare an
investigation and record it; this reads those records back and asks the one
question the declaration cannot answer by itself.

    scripts/eo_dioktes_audit            # the table
    scripts/eo_dioktes_audit --verbose  # and the scope and closing condition
    scripts/eo_dioktes_audit --check    # well formed, and does every basis hold

**A basis lapses without anybody touching the record.** LAW 10.4 rests on the
target being a member, and a member may leave at any time under LAW 2.1 --
which changes one line in somebody else's register entry and leaves a live
investigation standing on nothing. The declaration still reads as it did the
day it was written. That is the failure this command exists to catch, and it
is why the footing is re-derived on every run rather than copied into the
record at declaration time.

**It reports and changes nothing.** Ending an investigation, like starting one,
is a person's act.
"""

from __future__ import annotations

import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))
sys.path.insert(0, ROOT)
from tools.stathmos.audits.status_audit import (
    INVENTORY, PURSUIT_BASES, footing_of, outsider_trackable,
    pursuits_well_formed)


def load() -> tuple[dict, list]:
    """The register split into the entries and the investigations."""
    with open(INVENTORY, encoding="utf-8") as f:
        raw = json.load(f)
    pursuits = raw.get("_pursuits", [])
    return ({k: v for k, v in raw.items() if not k.startswith("_")},
            pursuits if isinstance(pursuits, list) else [])


def basis_holds(inv: dict, record: dict) -> str:
    """Empty where the declared basis is still good, else why it is not.

    Separate from `pursuits_well_formed`, which asks whether the record is
    written correctly. This asks whether it is still *true*, and the two
    answers come apart precisely when somebody else's footing moved.
    """
    basis, target = record.get("basis", ""), record.get("target", "")
    if basis not in PURSUIT_BASES:
        return f"`{basis}` is not a basis LAW 10 knows"
    if target not in inv:
        return f"`{target}` has no entry to take a footing from"
    footing = footing_of(inv, target)
    if footing not in PURSUIT_BASES[basis]:
        return (f"declared on the {basis!r} basis, and `{target}` is a "
                f"{footing or '(none)'} entry today -- the basis has lapsed")
    # LAW 9's evidence is a live requirement, not a fact checked once: an entry
    # can lose `published` in an edit, and LAW 10.1 stops applying when it does.
    if basis == "external":
        e = inv[target]
        if e.get("status") == "child":
            e = inv.get(e.get("parent", ""), {})
        if not outsider_trackable(e):
            return (f"`{target}` no longer records the release and publication "
                    "LAW 9 requires, so LAW 10.1 no longer permits it")
    return ""


def rows(inv: dict, pursuits: list) -> list[tuple]:
    out = []
    for p in pursuits:
        if not isinstance(p, dict):
            continue
        state = p.get("state", "?")
        if state == "closed" and p.get("closed"):
            state = f"closed {p['closed']}"
        out.append((p.get("pursuer", "?"), p.get("target", "?"),
                    p.get("basis", "?"), state, p.get("reporting", "?"),
                    p.get("started", "?"), basis_holds(inv, p), p))
    # Live work first, and within it the quiet ones first: a `stopped` row is
    # the one carrying an obligation somebody can still breach.
    order = {"public": 1, "stopped": 0}
    return sorted(out, key=lambda r: (r[3].startswith("closed"),
                                      order.get(r[4], 2), r[0], r[1]))


def render(inv: dict, pursuits: list, verbose: bool) -> str:
    table = rows(inv, pursuits)
    if not table:
        return ("No investigation is recorded.\n"
                "-- an empty record is not evidence that nobody is "
                "investigating anything (LAW 10)")
    head = ("pursuer", "target", "basis", "state", "reporting", "started")
    widths = [max(len(head[i]), max(len(str(r[i])) for r in table))
              for i in range(len(head))]
    out = ["  ".join(h.ljust(w) for h, w in zip(head, widths)).rstrip()]
    for r in table:
        out.append("  ".join(str(r[i]).ljust(widths[i])
                             for i in range(len(head))).rstrip())
        if r[6]:
            out.append(f"    !! {r[6]}")
        if verbose:
            p = r[7]
            out.append(f"    scope     {p.get('scope', '?')}")
            out.append(f"    closes    {p.get('closes', '?')}")
            out.append(f"    declared  {p.get('declared', '?')} by "
                       f"{p.get('responsible', '?')}")
    stopped = [r for r in table if r[4] == "stopped" and not r[3].startswith("closed")]
    if stopped:
        out.append("")
        out.append(f"-- {len(stopped)} investigation(s) continue with public "
                   "reporting and contact ended on request (LAW 10.2/10.3)")
    lapsed = sum(1 for r in table if r[6])
    out.append("")
    out.append(f"-- {len(table)} recorded, "
               f"{sum(1 for r in table if not r[3].startswith('closed'))} active, "
               f"{lapsed} whose basis no longer holds")
    if not verbose:
        out.append("-- --verbose adds the scope, the closing condition and who "
                   "is responsible")
    return "\n".join(out)


def check(inv: dict, pursuits: list) -> int:
    """`--check`: the records are well formed, and every basis still holds."""
    bad = list(pursuits_well_formed(inv, pursuits))
    for p in pursuits:
        if isinstance(p, dict):
            why = basis_holds(inv, p)
            if why:
                bad.append(f"{p.get('pursuer', '?')} -> "
                           f"{p.get('target', '?')}: {why}")
    for b in bad:
        print(f"FAIL {b}")
    print(f"-- {len(pursuits)} investigation(s), {len(bad)} failure(s)")
    if bad:
        print("-- a lapsed basis is ended or re-declared by a person; "
              "nothing here changes a record")
    return 1 if bad else 0


def main() -> int:
    if "--help" in sys.argv or "-h" in sys.argv:
        print(__doc__.strip())
        return 0
    inv, pursuits = load()
    if "--check" in sys.argv:
        return check(inv, pursuits)
    print(render(inv, pursuits, "--verbose" in sys.argv))
    return 0


if __name__ == "__main__":
    sys.exit(main())
