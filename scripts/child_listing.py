"""Read a parent's choice to advertise a child from the child's README.

An exact, standalone declaration in the introduction (before the first section
heading) sets the choice. Examples, comments and ordinary prose do not count.
Missing declarations default to advertised; unreadable or invalid ones are
unverified. This module reads local files only and never changes the inventory.
"""

from collections import Counter
from pathlib import Path
import re
from typing import NamedTuple


class Listing(NamedTuple):
    state: str
    reason: str = ""

    @property
    def advertised(self) -> bool:
        return self.state == "advertised"


def declaration(text: str) -> Listing:
    text = re.sub(r"<!--.*?(?:-->|\Z)", "", text, flags=re.S)
    values = []
    fence = ""
    for line in text.splitlines():
        if fence:
            if re.fullmatch(r" {0,3}" + re.escape(fence[0]) +
                            "{" + str(len(fence)) + r",}\s*", line):
                fence = ""
            continue
        opening = re.match(r"^ {0,3}(`{3,}|~{3,})", line)
        if opening:
            fence = opening[1]
            continue
        if re.match(r"^ {0,3}#{2,6}(?:\s|$)", line):
            break
        if line.startswith("**Eunoia listing:**"):
            values.append(line[len("**Eunoia listing:**"):].strip())
    if not values:
        return Listing("advertised", "no declaration; default")
    if len(values) != 1:
        return Listing("unverified", "multiple Eunoia listing declarations")
    if values[0] not in ("advertised", "unadvertised"):
        return Listing("unverified", "expected advertised or unadvertised")
    return Listing(values[0])


def read_listing(parent: str, child_path: str) -> Listing:
    if not parent or not Path(parent).is_dir():
        return Listing("unverified", "parent checkout unavailable")
    if not child_path or Path(child_path).is_absolute():
        return Listing("unverified", "child needs a relative path")
    try:
        root = Path(parent).resolve()
        readme = (root / child_path / "README.md").resolve()
        if not readme.is_relative_to(root):
            return Listing("unverified", "child README is outside its parent")
        return declaration(readme.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, RuntimeError):
        return Listing("unverified", "child README unavailable or unreadable")


def unverified_note(parent: str, listings: list[Listing]) -> str:
    """Report incomplete reads by parent without advertising hidden child names."""
    reasons = Counter(s.reason for s in listings if s.state == "unverified")
    if not reasons:
        return ""
    count = sum(reasons.values())
    detail = "; ".join(f"{reason} ({n})" for reason, n in reasons.items())
    return (f"{parent}: child listing preference unverified for {count} "
            f"project{'s' if count != 1 else ''}: {detail}")
