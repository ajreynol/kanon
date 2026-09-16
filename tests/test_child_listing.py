"""Child listing choices, using temporary checkouts and no network or clones."""

import contextlib
import io
import json
import os
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch

from test_handoff import ecosystem, installer
from child_listing import declaration, read_listing


class Declarations(unittest.TestCase):
    def test_only_introductory_metadata_advertises(self):
        marker = "**Eunoia listing:** advertised"
        cases = [
            (f"# Example\n\n{marker}\n\n## Charter\n", "advertised"),
            ("**Eunoia listing:** unadvertised\n", "unadvertised"),
            ("This project is advertised and is not an island.\n", "unadvertised"),
            (f"```markdown\n{marker}\n```\n", "unadvertised"),
            (f"~~~~\n{marker}\n~~~~\n", "unadvertised"),
            (f"<!--\n{marker}\n-->\n", "unadvertised"),
            (f"> {marker}\n", "unadvertised"),
            (f"    {marker}\n", "unadvertised"),
            (f"## Example\n{marker}\n", "unadvertised"),
            (f"```\n## Example\n```\n{marker}\n", "advertised"),
            ("**Eunoia listing:** yes\n", "unverified"),
            (f"{marker}\n**Eunoia listing:** unadvertised\n", "unverified"),
            (f"{marker}\n{marker}\n", "unverified"),
        ]
        for text, state in cases:
            with self.subTest(text=text):
                self.assertEqual(declaration(text).state, state)

    def test_unavailable_or_outside_readme_does_not_advertise(self):
        with tempfile.TemporaryDirectory(prefix="kanon-listing-") as temp:
            base = Path(temp)
            parent = base / "parent"
            parent.mkdir()
            outside = base / "outside"
            outside.mkdir()
            (outside / "README.md").write_text("**Eunoia listing:** advertised\n")
            (parent / "linked").symlink_to(outside, target_is_directory=True)
            for root, path in [("", "tools/example"), (str(parent), "missing"),
                               (str(parent), ""), (str(parent), str(outside)),
                               (str(parent), "../outside"), (str(parent), "linked")]:
                with self.subTest(root=root, path=path):
                    self.assertEqual(read_listing(root, path).state, "unverified")
            child = parent / "child"
            child.mkdir()
            (child / "README.md").write_bytes(b"\xff")
            self.assertEqual(read_listing(str(parent), "child").state, "unverified")


class ChildCommands(unittest.TestCase):
    def setUp(self):
        temp = tempfile.TemporaryDirectory(prefix="kanon-child-commands-")
        self.addCleanup(temp.cleanup)
        self.base = Path(temp.name)
        self.parent = self.base / "host-tree"
        (self.parent / ".git").mkdir(parents=True)
        self.entries = {
            "host": {"status": "member", "repo": "host-tree",
                     "url": "https://example.invalid/host", "what": "parent"},
        }
        self.choices = {"published": "advertised", "quiet": "unadvertised",
                        "implicit": None, "broken": "yes", "missing": None}
        for name, choice in self.choices.items():
            self.entries[name] = {"status": "child", "parent": "host",
                                  "path": f"tools/{name}", "what": "child project",
                                  "branch": f"{name}-work"}
            if name != "missing":
                child = self.parent / "tools" / name
                child.mkdir(parents=True)
                text = f"# {name}\n\n"
                if choice is not None:
                    text += f"**Eunoia listing:** {choice}\n"
                (child / "README.md").write_text(text)
        self.inventory = self.base / "inventory.json"
        self.inventory.write_text(json.dumps(self.entries))
        self.checkouts = self.base / "checkouts.json"
        self.checkouts.write_text("{}")
        mapping = self.base / "repos.local"
        mapping.write_text(f"host-tree {self.parent}\nquiet {self.parent}\n")
        patches = [
            patch.object(ecosystem, "INVENTORY", str(self.inventory)),
            patch.object(installer, "INVENTORY", str(self.inventory)),
            patch.object(installer, "CHECKOUTS", str(self.checkouts)),
            patch.object(ecosystem, "REPOS_FILE", str(mapping)),
            patch.object(installer, "REPOS_FILE", str(mapping)),
            patch.dict(os.environ, {"ANOIEU_REPOS": str(self.base)}),
            patch.object(ecosystem, "check", return_value=("ok", [])),
            patch.object(ecosystem, "age", return_value="today"),
            patch.object(installer, "age", return_value="today"),
            patch.object(installer, "deps", return_value={}),
            patch.object(installer, "git", return_value=(0, "")),
            patch.object(installer, "execute", side_effect=AssertionError("unexpected clone")),
        ]
        for p in patches:
            p.start()
            self.addCleanup(p.stop)

    def status(self, *args):
        out = io.StringIO()
        with patch.object(sys, "argv", ["status_eo", *args]), contextlib.redirect_stdout(out):
            self.assertEqual(ecosystem.main(), 0)
        return out.getvalue()

    def install(self, *args):
        out = io.StringIO()
        argv = ["install_eo", "--root", str(self.base), "--no-repos-local", *args]
        with patch.object(sys, "argv", argv), contextlib.redirect_stdout(out):
            self.assertEqual(installer.main(), 0)
        return out.getvalue()

    def assert_only_advertised(self, output):
        self.assertIn("published", output)
        for name in ("quiet", "implicit", "broken", "missing"):
            self.assertNotIn(name, output)
        self.assertIn("child listing preference unverified", output)

    def test_status_filters_rows_and_counts(self):
        output = self.status()
        self.assert_only_advertised(output)
        self.assertIn("1 child", output)
        self.assertNotIn("5 children", output)

    def test_all_children_includes_preferences_and_unverified_reads(self):
        output = self.status("--all-children")
        self.assertIn("5 children", output)
        self.assertIn("published: Eunoia listing: advertised", output)
        self.assertIn("quiet: Eunoia listing: unadvertised", output)
        self.assertIn("implicit: Eunoia listing: unadvertised (no declaration; default)", output)
        self.assertIn("broken: Eunoia listing: unverified", output)
        self.assertIn("missing: Eunoia listing: unverified", output)

    def test_missing_parent_is_reported_without_advertising_children(self):
        with patch.object(ecosystem, "locate", return_value=""):
            output = self.status()
        for name in self.choices:
            self.assertNotIn(name, output)
        self.assertIn("parent checkout unavailable", output)

    def test_installer_views_and_branch_advice_share_the_preference(self):
        for mode in ("--dry-run", "--status", "--run"):
            with self.subTest(mode=mode):
                self.assert_only_advertised(self.install(mode))

    def test_unadvertised_ids_still_resolve_and_are_mapped(self):
        output = self.install("--dry-run", "quiet")
        self.assertIn("git clone https://example.invalid/host host-tree", output)
        self.assertNotIn("so nothing here fetches it", output)
        self.assertNotIn("quiet", output)
        repos = installer.plan()
        self.assertEqual(installer.unknown(repos, list(self.choices)), [])
        rows = installer.repos_local_rows(str(self.base), repos)
        mapped = {name: path for name, path, live in rows if live}
        for name in self.choices:
            self.assertEqual(mapped[name], str(self.parent))

    def test_branch_observation_does_not_name_an_unadvertised_child(self):
        def git(path, *args):
            return (0, "quiet-work" if args == ("rev-parse", "--abbrev-ref", "HEAD") else "")

        with patch.object(installer, "git", side_effect=git), \
             patch.object(installer, "default_branch", return_value="main"):
            _, notes, _ = installer.observe(str(self.parent), installer.plan()[0], False)
        self.assertNotIn("quiet's current work", "\n".join(notes))

    def test_clone_reads_the_declaration_after_checkout_arrives(self):
        destination = self.base / "fresh"

        def clone(cmd, cwd):
            child = Path(cwd) / "host-tree" / "tools" / "published"
            child.mkdir(parents=True)
            (child / "README.md").write_text("**Eunoia listing:** advertised\n")
            return 0

        out = io.StringIO()
        with patch.object(installer, "execute", side_effect=clone), contextlib.redirect_stdout(out):
            repos = installer.plan()
            self.assertEqual(installer.run(str(destination), repos, repos, False), 0)
        self.assert_only_advertised(out.getvalue())


if __name__ == "__main__":
    unittest.main()
