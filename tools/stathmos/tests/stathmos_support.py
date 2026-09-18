"""Load stathmos's commands for its offline regression suite."""

import importlib.machinery
import importlib.util
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT))


def load(name, path):
    loader = importlib.machinery.SourceFileLoader(name, str(ROOT / path))
    spec = importlib.util.spec_from_loader(name, loader)
    module = importlib.util.module_from_spec(spec)
    loader.exec_module(module)
    return module


from tools.stathmos.scripts import policy_check

ecosystem = load("ecosystem_under_test", "tools/stathmos/scripts/status_audit.py")
