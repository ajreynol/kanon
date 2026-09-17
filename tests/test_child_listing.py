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

from support import ecosystem
from child_listing import declaration, read_listing

class Declarations(unittest.TestCase):
    def test_the_footing_marker_is_read_as_well_as_the_older_line(self):
        M = "**Footing:** `unadvertised-child` — anoieu's front page does not name it"
        cases = [
            (f"# x\n\n{M}\n", "unadvertised"),                      # the current spelling
            (f"# x\n\n{M}\n\n## Charter\n", "unadvertised"),
            (f"# x\n\n## Charter\n\n{M}\n", "unadvertised"),      # read past a heading
            (f"# x\n\n```\n{M}\n```\n", "advertised"),            # a fenced example is not one
            (f"# x\n\n<!--\n{M}\n-->\n", "advertised"),
            ("# x\n\n**Footing:** `child` — ordinary\n", "advertised"),
            (f"# x\n\n{M}\n**Eunoia listing:** unadvertised\n", "unadvertised"),
            (f"# x\n\n{M}\n**Eunoia listing:** advertised\n", "unverified"),
        ]
        for text, expected in cases:
            with self.subTest(text=text):
                self.assertEqual(declaration(text).state, expected)

    def test_only_introductory_metadata_changes_the_default(self):
        marker = "**Eunoia listing:** unadvertised"
        cases = [
            (f"# Example\n\n{marker}\n\n## Charter\n", "unadvertised"),
            ("**Eunoia listing:** advertised\n", "advertised"),
            ("This project is unadvertised and is an island.\n", "advertised"),
            (f"```markdown\n{marker}\n```\n", "advertised"),
            (f"~~~~\n{marker}\n~~~~\n", "advertised"),
            (f"<!--\n{marker}\n-->\n", "advertised"),
            (f"> {marker}\n", "advertised"),
            (f"    {marker}\n", "advertised"),
            (f"## Example\n{marker}\n", "advertised"),
            (f"```\n## Example\n```\n{marker}\n", "unadvertised"),
            ("**Eunoia listing:** yes\n", "unverified"),
            (f"{marker}\n**Eunoia listing:** advertised\n", "unverified"),
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
        mapping = self.base / "repos.local"
        mapping.write_text(f"host-tree {self.parent}\nquiet {self.parent}\n")
        patches = [
            patch.object(ecosystem, "INVENTORY", str(self.inventory)),
            patch.object(ecosystem, "REPOS_FILE", str(mapping)),
            patch.dict(os.environ, {"ANOIEU_REPOS": str(self.base)}),
            patch.object(ecosystem, "check", return_value=("ok", [])),
            patch.object(ecosystem, "age", return_value="today"),
        ]
        for p in patches:
            p.start()
            self.addCleanup(p.stop)

    def status(self, *args):
        out = io.StringIO()
        with patch.object(sys, "argv", ["eo_status_audit", *args]), contextlib.redirect_stdout(out):
            self.assertEqual(ecosystem.main(), 0)
        return out.getvalue()

    def assert_only_advertised(self, output):
        self.assertIn("published", output)
        self.assertIn("implicit", output)
        for name in ("quiet", "broken", "missing"):
            self.assertNotIn(name, output)
        self.assertIn("child listing preference unverified", output)

    def test_status_filters_rows_and_counts(self):
        self.entries["published"]["short"] = "Research notes"
        self.inventory.write_text(json.dumps(self.entries))
        output = self.status()
        self.assert_only_advertised(output)
        self.assertIn("2 children", output)
        self.assertNotIn("5 children", output)
        self.assertEqual(output.splitlines()[0].split(),
                         ["tool", "status", "policy", "channel", "moved", "where", "purpose"])
        for name, purpose in (("host", "parent"), ("published", "Research notes"),
                              ("implicit", "child project")):
            row = next(line for line in output.splitlines() if line.split()[:1] == [name])
            self.assertTrue(row.endswith(purpose), row)

    def test_the_summary_does_not_contradict_its_own_footing_counts(self):
        # The failure this catches: `members` is member *and* president, so the
        # sentence read "8 members ... 9 of 9 members pass".
        out = self.status()
        summary = out.splitlines()[-1]
        self.assertIn("repositories held to the policy", summary)
        self.assertNotIn("members pass", summary)

    def test_all_children_includes_preferences_and_unverified_reads(self):
        output = self.status("--all-children")
        self.assertIn("5 children", output)
        self.assertIn("published: Eunoia listing: advertised", output)
        self.assertIn("quiet: Eunoia listing: unadvertised", output)
        self.assertIn("implicit: Eunoia listing: advertised (no declaration; default)", output)
        self.assertIn("broken: Eunoia listing: unverified", output)
        self.assertIn("missing: Eunoia listing: unverified", output)

    def test_the_advertised_column_appears_only_on_a_widened_table(self):
        # In the default view every row is one the default view kept, so the
        # column would read `yes` all the way down and answer nothing.
        self.assertNotIn("advertised?", self.status())
        for flag in ("--all", "--all-children"):
            with self.subTest(flag=flag):
                self.assertIn("advertised?", self.status(flag))

    def test_the_column_says_what_each_child_declared(self):
        rows = {line.split()[0]: line for line in self.status("--all").splitlines()
                if line.split()[:1] and line.split()[0] in self.entries}
        self.assertIn("yes", rows["published"])     # declares advertised
        self.assertIn("yes", rows["implicit"])      # no declaration; the default
        self.assertIn("no", rows["quiet"])          # declares unadvertised
        self.assertIn("?", rows["broken"])          # unreadable declaration
        self.assertIn("-", rows["host"])            # a repository has no preference

    def test_all_widens_the_table_without_a_note_per_child(self):
        output = self.status("--all")
        self.assertIn("5 children", output)
        for name in self.choices:
            self.assertIn(name, output)
        self.assertNotIn("Eunoia listing:", output)

    def test_an_option_that_is_not_one_is_refused_rather_than_ignored(self):
        # The failure this catches: an unrecognised flag printed the default
        # table and looked exactly like a flag that had worked.
        out, err = io.StringIO(), io.StringIO()
        with patch.object(sys, "argv", ["eo_status_audit", "--alll"]), \
             contextlib.redirect_stdout(out), contextlib.redirect_stderr(err):
            self.assertEqual(ecosystem.main(), 2)
        self.assertIn("--alll", err.getvalue())
        self.assertIn("--all-children", err.getvalue())
        self.assertNotIn("children,", out.getvalue())

    def test_missing_parent_is_reported_without_advertising_children(self):
        with patch.object(ecosystem, "locate", return_value=""):
            output = self.status()
        for name in self.choices:
            self.assertNotIn(name, output)
        self.assertIn("parent checkout unavailable", output)
        row = next(line for line in output.splitlines() if line.split()[:1] == ["host"])
        self.assertTrue(row.endswith(self.entries["host"]["what"]), row)

if __name__ == "__main__":
    unittest.main()
