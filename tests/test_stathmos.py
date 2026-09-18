"""Include stathmos's own regressions in kanon's test run."""

from pathlib import Path
import unittest


def load_tests(loader, tests, pattern):
    start = Path(__file__).resolve().parents[1] / "tools/stathmos/tests"
    return unittest.TestLoader().discover(str(start), pattern=pattern or "test*.py")
