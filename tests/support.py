"""Shared fixtures for kanon's regressions: module loaders and document helpers.

Not a test module. `unittest discover` collects only `test*.py`, so this is
imported by the suites rather than run as one.
"""

import importlib.machinery
import importlib.util
from pathlib import Path
import re
import sys


ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
import sleep as working_hours


def load(name, path):
    loader = importlib.machinery.SourceFileLoader(name, str(ROOT / path))
    spec = importlib.util.spec_from_loader(name, loader)
    module = importlib.util.module_from_spec(spec)
    loader.exec_module(module)
    return module


ecosystem = load("ecosystem_under_test", "scripts/ecosystem/ecosystem.py")
installer = load("installer_under_test", "scripts/install_eo")
dependency = load("dependency_under_test", "scripts/anoieu_dependency.py")

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


