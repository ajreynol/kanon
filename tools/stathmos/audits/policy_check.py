#!/usr/bin/env python3
"""Stathmos's launcher for anoieu's policy checker: locate it and run it.

**The implementation and its version stay in anoieu**, which holds `R31`. This
locates a checkout and runs what is there; it decides nothing about compliance
and carries no copy of the rules.

    python3 tools/stathmos/audits/policy_check.py              # check kanon
    python3 tools/stathmos/audits/policy_check.py --root PATH  # another checkout

`ANOIEU_ROOT` selects the checkout; otherwise `scripts/repos.local`,
`ANOIEU_REPOS`, a sibling `anoieu/`, then `$HOME`. An unavailable checker is
`UNVERIFIED` with exit code 2, which is not a pass.

**The command and the readers are two different files, and they come apart.**
`main` is what a run invokes; `declaration_in` and its siblings are what the
status audit imports to read somebody's README. anoieu moved the
implementation into `policy_check/` and left `scripts/policy_check.py` a
launcher exporting `main` alone, so a loader that reads only the command's
path silently returns a module with no readers on it -- which is how
`--protocol` started raising `AttributeError` instead of printing a table.
So `policy_checker()` looks for the readers by name and says which paths it
tried when it cannot find them.

**Locating the checker and running it are one job**, and one file: nothing
wants the locator without the runner, and splitting them makes every importer
learn two names for it. Which file inside anoieu each half reaches for is
anoieu's arrangement and is read here rather than assumed.
"""

from functools import lru_cache
import importlib.util
import os
from pathlib import Path
import subprocess
import sys


ROOT = Path(__file__).resolve().parents[3]


def checkout() -> Path:
    """Use an explicit checkout, the shared mapping, or a sibling checkout."""
    explicit = os.environ.get("ANOIEU_ROOT")
    if explicit:
        candidates = [Path(explicit).expanduser()]
    else:
        candidates = []
        mapping = Path(os.environ.get("ANOIEU_REPOS_FILE", ROOT / "scripts/repos.local"))
        if mapping.is_file():
            for line in mapping.read_text().splitlines():
                parts = line.strip().split(None, 1)
                if len(parts) == 2 and parts[0] == "anoieu":
                    candidates.append(Path(parts[1]).expanduser())
        candidates.extend(Path(p).expanduser() / "anoieu"
                          for p in os.environ.get("ANOIEU_REPOS", "").split(os.pathsep) if p)
        candidates.extend([ROOT.parent / "anoieu", Path.home() / "anoieu"])
    for path in candidates:
        if any((path / rel).is_file() for rel in
               ("scripts/policy_check.py", "tools/policy_check.py")):
            return path.resolve()
    raise FileNotFoundError(
        "anoieu's policy checker is unavailable; clone anoieu beside kanon "
        "or set ANOIEU_ROOT to its checkout")


#: Where the readers have lived, newest arrangement first. The first entry is
#: the package anoieu moved them into; the other two are the older layouts, so
#: an older checkout keeps working.
READER_PATHS = ("policy_check/checker.py", "scripts/policy_check.py",
                "tools/policy_check.py")

#: The reader every caller needs. A module without it is the launcher rather
#: than the implementation, whatever it is called.
READER = "declaration_in"


def checker_path() -> Path:
    root = checkout()
    for rel in ("scripts/policy_check.py", "tools/policy_check.py"):
        if (root / rel).is_file():
            return root / rel
    raise FileNotFoundError(f"no policy checker in {root}")


def _load(path: Path):
    spec = importlib.util.spec_from_file_location("anoieu_policy_check", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


@lru_cache(maxsize=1)
def policy_checker():
    """The module carrying the declaration readers, from the anoieu checkout.

    Not necessarily the file the command runs: see the note at the top.
    """
    root = checkout()
    tried = []
    for rel in READER_PATHS:
        path = root / rel
        if not path.is_file():
            continue
        tried.append(rel)
        module = _load(path)
        if hasattr(module, READER):
            return module
    raise ImportError(
        f"no {READER} in {root}: read {', '.join(tried) or 'nothing'}. "
        f"The readers have moved; add the new path to READER_PATHS")


def main() -> int:
    try:
        checker = checker_path()
    except OSError as exc:
        print(f"UNVERIFIED: {exc}", file=sys.stderr)
        return 2
    args = sys.argv[1:]
    if "--root" not in args:
        args = ["--root", str(ROOT), *args]
    return subprocess.run([sys.executable, str(checker), *args]).returncode


if __name__ == "__main__":
    sys.exit(main())
