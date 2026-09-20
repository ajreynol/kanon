"""The documents check themselves: labels against the register, and every link.

Offline. Reads the tree and contacts nothing.
"""

import re
import subprocess
import unittest
from urllib.parse import unquote, urlsplit

from support import ROOT, anchors, prose, register


class Documents(unittest.TestCase):
    def test_glossary_project_labels_match_inventory(self):
        text = (ROOT / "docs/glossary.md").read_text()
        labels = re.findall(r"^[ \t]*(?:[-*+] )?\*\*(.+?)\*\* \(Eunoia ([^;]+);", text, re.M)
        # a label may cross-link its parent: "child project of [x](#x)"
        unlink = lambda s: re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", s)
        actual = {name.casefold(): unlink(label) for name, label in labels}
        self.assertEqual(len(actual), len(labels), "duplicate glossary project entries")
        expected = {
            name.casefold(): (f"child project of {entry['parent']}"
                              if entry["status"] == "child" else entry["status"])
            for name, entry in register().items()
        }
        self.assertEqual(actual, expected)

    def test_relative_links_and_anchors(self):
        failures = []
        for path in ROOT.rglob("*.md"):
            if any(part.startswith(".") for part in path.relative_to(ROOT).parts):
                continue
            text = prose(path.read_text())
            targets = re.findall(r"\]\(([^\s)]+)\)", text)
            targets += re.findall(r"^\s*\[[^\]]+\]:\s+(\S+)", text, re.M)
            for target in targets:
                url = urlsplit(target.strip("<>"))
                if url.scheme or url.netloc:
                    continue
                dest = (path.parent / unquote(url.path)).resolve() if url.path else path
                if not dest.exists():
                    failures.append(f"{path.relative_to(ROOT)}: missing {target}")
                elif url.fragment and dest.suffix == ".md":
                    if unquote(url.fragment) not in anchors(dest):
                        failures.append(f"{path.relative_to(ROOT)}: missing heading {target}")
        self.assertEqual(failures, [])

    def test_housed_projects_match_inventory(self):
        inv = register()
        projects = [p for p in (ROOT / "tools").iterdir() if (p / "README.md").is_file()]
        self.assertTrue(projects)
        for path in projects:
            with self.subTest(project=path.name):
                self.assertEqual(inv[path.name]["status"], "child")
                self.assertEqual(inv[path.name]["parent"], "kanon")
                self.assertEqual(inv[path.name]["path"], path.relative_to(ROOT).as_posix())
        # and nothing claims to be housed here that is not on disk
        housed = {n for n, e in inv.items()
                  if e.get("status") == "child" and e.get("parent") == "kanon"}
        self.assertEqual(housed, {p.name for p in projects})

    def test_shell_syntax(self):
        for path in [ROOT / "scripts/eo_status_audit", ROOT / "scripts/eo_tooling_audit",
                     ROOT / "scripts/eo_dioktes_audit", ROOT / "scripts/eo_ci_audit"]:
            with self.subTest(script=path.name):
                result = subprocess.run(["bash", "-n", str(path)], capture_output=True, text=True)
                self.assertEqual(result.returncode, 0, result.stderr)
