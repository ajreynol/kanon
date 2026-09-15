"""Locate the checker that remains in anoieu after the governance handoff."""

from functools import lru_cache
import importlib.util
import os
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent


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


def checker_path() -> Path:
    root = checkout()
    for rel in ("scripts/policy_check.py", "tools/policy_check.py"):
        if (root / rel).is_file():
            return root / rel
    raise FileNotFoundError(f"no policy checker in {root}")


@lru_cache(maxsize=1)
def policy_checker():
    """Load declaration readers from the same checker the command runs."""
    spec = importlib.util.spec_from_file_location("anoieu_policy_check", checker_path())
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module
