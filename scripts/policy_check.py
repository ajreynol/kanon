#!/usr/bin/env python3
"""Run anoieu's policy checker. The implementation and its version stay there.

Without --root, check kanon. ANOIEU_ROOT selects the anoieu checkout; otherwise
use scripts/repos.local, ANOIEU_REPOS, or the sibling anoieu directory.
"""

from pathlib import Path
import subprocess
import sys

from anoieu_dependency import checker_path


def main() -> int:
    try:
        checker = checker_path()
    except OSError as exc:
        print(f"UNVERIFIED: {exc}", file=sys.stderr)
        return 2
    args = sys.argv[1:]
    if "--root" not in args:
        args = ["--root", str(Path(__file__).resolve().parent.parent), *args]
    return subprocess.run([sys.executable, str(checker), *args]).returncode


if __name__ == "__main__":
    sys.exit(main())
