"""Shared fixtures for kanon's regressions: module loaders and document helpers.

Not a test module. `unittest discover` collects only `test*.py`, so this is
imported by the suites rather than run as one.
"""

import importlib.machinery
import importlib.util
from pathlib import Path
import json
import re
import sys


ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))


def load(name, path):
    loader = importlib.machinery.SourceFileLoader(name, str(ROOT / path))
    spec = importlib.util.spec_from_loader(name, loader)
    module = importlib.util.module_from_spec(spec)
    loader.exec_module(module)
    return module


import policy_check  # scripts/ is on the path, set just above

ecosystem = load("ecosystem_under_test", "tools/stathmos/scripts/status_audit.py")


def register() -> dict:
    """The register itself, read the way every reader of it reads it.

    The installer used to supply this, and the document tests borrowed it from
    there. It went to koine on 2026-09-17, and reading the file is what those
    tests were always doing through it.
    """
    with open(ROOT / "scripts/ecosystem/ecosystem.json", encoding="utf-8") as f:
        return {k: v for k, v in json.load(f).items() if not k.startswith("_")}

# Loaded here so every suite shares one instance; importing them is also the
# cheapest check that each still parses against the current tree.


def prose(text):
    return re.sub(r"^(```|~~~).*?^\1[^\n]*$", "", text, flags=re.M | re.S)


def anchors(path):
    text = prose(path.read_text())
    found, counts = set(), {}
    for heading in re.findall(r"^#{1,6}\s+(.+?)\s*$", text, re.M):
        slug = re.sub(r"[`*_]", "", heading.lower())
        slug = re.sub(r"[^\w\s-]", "", slug)
        slug = re.sub(r"\s", "-", slug)
        suffix = counts.get(slug, 0)
        found.add(f"{slug}-{suffix}" if suffix else slug)
        counts[slug] = suffix + 1
    found.update(re.findall(r'(?:id|name)=[\"\']([^\"\']+)', text))
    return found
