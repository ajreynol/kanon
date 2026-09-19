"""Tooling inventory regressions: no network, real tools or sibling checkouts."""

import contextlib
import copy
import io
import json
import os
from pathlib import Path
import subprocess
import tempfile
import unittest
from unittest.mock import patch
import urllib.error

from stathmos_support import ROOT
from tools.stathmos.audits import tooling_audit as audit


class ToolingAudit(unittest.TestCase):
    def setUp(self):
        self.ecosystem = {"sample": {"status": "member", "repo": "sample",
                                      "url": "https://github.com/example/sample"}}
        self.entry = {"repo": "sample", "path": "analyzer", "what": "Analyze inputs",
                      "entrypoints": ["scripts/analyze"], "docs": ["docs/usage.md"]}
        self.inventory = {"tools": {"analyzer": self.entry}, "exclude": {}}
        self.tree = audit.Tree({"scripts/analyze", "docs/usage.md"},
                               {"analyzer", "scripts", "docs"}, "fixture")

    def inspect(self, tree=None):
        with patch.object(audit, "local_tree", return_value=tree or self.tree):
            return audit.inspect(self.inventory, self.ecosystem)

    def run_main(self, *args, tree=None, error=None):
        output = io.StringIO()
        with patch.object(audit, "read_json", side_effect=[self.inventory, self.ecosystem]), \
             patch.object(audit, "local_tree", return_value=tree or self.tree, side_effect=error), \
             contextlib.redirect_stdout(output):
            code = audit.main(list(args))
        return code, output.getvalue()

    def test_inventory_validation_needs_no_checkouts_or_network(self):
        with patch.object(audit, "read_json", side_effect=[self.inventory, self.ecosystem]), \
             patch.object(audit, "local_tree") as local, \
             patch.object(audit, "remote_tree") as remote, \
             contextlib.redirect_stdout(io.StringIO()):
            self.assertEqual(audit.main(["--check"]), 0)
        local.assert_not_called()
        remote.assert_not_called()

    def test_bad_records_are_rejected_before_inspection(self):
        changes = [{"repo": "absent"}, {"path": "../escape"}, {"path": "/absolute"},
                   {"path": "a//b"}, {"path": "a/./b"}, {"path": "a\\b"},
                   {"what": " "}, {"entrypoints": "scripts/analyze"},
                   {"entrypoints": ["../outside"]}, {"docs": [None]},
                   {"also": ["/outside"]}, {"layout_note": []}]
        for change in changes:
            with self.subTest(change=change):
                inventory = copy.deepcopy(self.inventory)
                inventory["tools"]["analyzer"].update(change)
                self.assertTrue(audit.well_formed(inventory, self.ecosystem))
        self.entry["repo"] = "absent"
        with patch.object(audit, "remote_tree") as remote:
            code, output = self.run_main("--check", "--online")
        self.assertEqual(code, 1)
        self.assertIn("FAIL", output)
        remote.assert_not_called()

    def test_duplicate_locations_and_conflicting_exclusions(self):
        self.inventory["tools"]["duplicate"] = dict(self.entry)
        self.assertIn("shares its primary", " ".join(audit.well_formed(self.inventory, self.ecosystem)))
        del self.inventory["tools"]["duplicate"]
        self.inventory["exclude"] = {"sample": {"analyzer": "not a tool"}}
        self.assertIn("both tooling and excluded", " ".join(audit.well_formed(self.inventory, self.ecosystem)))

    def test_repo_field_requires_a_repository_footing(self):
        for status in ("child", "outsider"):
            with self.subTest(status=status):
                self.ecosystem["excluded"] = {"status": status, "repo": "excluded"}
                with patch.object(audit, "local_tree", return_value=self.tree) as local:
                    audit.inspect(self.inventory, self.ecosystem)
                local.assert_called_once_with(self.ecosystem["sample"])
                self.entry["repo"] = "excluded"
                self.assertTrue(audit.well_formed(self.inventory, self.ecosystem))
                self.entry["repo"] = "sample"

    def test_foundation_tooling_is_inspected_without_a_policy_check(self):
        self.ecosystem["sample"]["status"] = "foundation"
        self.assertEqual(audit.well_formed(self.inventory, self.ecosystem), [])
        with patch.object(audit.status_audit, "check") as policy:
            code, output = self.run_main("--check", "--local")
            self.assertEqual(code, 0, output)
            with patch.object(audit, "remote_tree", return_value=self.tree) as remote:
                result = audit.inspect(self.inventory, self.ecosystem, online=True)
            remote.assert_called_once_with(self.ecosystem["sample"])
            self.assertFalse(result[1] or result[2])
        policy.assert_not_called()
        self.assertEqual(self.ecosystem["sample"]["status"], "foundation")

    def child_owner(self):
        self.ecosystem["child"] = {"status": "child", "parent": "sample", "path": "tools/child"}
        self.entry.update(owner="child", path="tools/child/audits")
        self.tree.directories.update({"tools", "tools/child", "tools/child/audits",
                                      "tools/child/docs", "tools/child/tests"})
        self.tree.directories.remove("analyzer")

    def test_child_tool_is_top_level_with_shared_repository_entrypoints(self):
        self.child_owner()
        self.assertEqual(audit.well_formed(self.inventory, self.ecosystem), [])
        code, output = self.run_main("--check", "--local")
        self.assertEqual(code, 0, output)
        row = next(line for line in output.splitlines() if line.startswith("analyzer "))
        self.assertEqual(row.split()[:7], ["analyzer", "tool", "child", "sample",
                                         "present", "top-level", "tools/child/audits"])
        self.assertIn("0 layout gap(s)", output)

    def test_child_layout_discovery_and_exclusions_use_child_root(self):
        self.child_owner()
        self.tree.directories.update({"tools/child/extra", "tools/child/data", "tools/other/elsewhere",
                                      "tools/child/examples", "tools/child/test",
                                      "tools/child/cmake", "tools/child/include"})
        self.inventory["exclude"] = {"child": {"data": "archived evidence", "removed": "old evidence"}}
        rows, gaps, *_ = self.inspect()
        self.assertEqual(len(gaps), 4, gaps)
        self.assertTrue(any("child/extra: unregistered" in gap for gap in gaps))
        self.assertTrue(any("child/removed: stale exclusion" in gap for gap in gaps))
        excluded = next(row for row in rows if row[0] == "child/data")
        self.assertEqual(excluded[1:7], ("excluded", "child", "sample", "present",
                                        "non-compliant", "tools/child/data"))
        self.inventory["exclude"]["child"]["audits"] = "not tooling"
        self.assertIn("both tooling and excluded", " ".join(audit.well_formed(self.inventory, self.ecosystem)))

    def test_child_owner_must_match_repository_and_contain_implementation(self):
        self.child_owner()
        self.ecosystem["other"] = {**self.ecosystem["sample"], "repo": "other"}
        for changes in ({"owner": "absent"}, {"owner": []}, {"repo": "other"},
                        {"path": "tools/childish/audits"}, {"path": "."},
                        {"also": ["elsewhere"]}):
            with self.subTest(changes=changes):
                inventory = copy.deepcopy(self.inventory)
                inventory["tools"]["analyzer"].update(changes)
                self.assertTrue(audit.well_formed(inventory, self.ecosystem))
        original = dict(self.ecosystem["child"])
        for changes in ({"parent": "absent"}, {"parent": "child"},
                        {"path": "../escape"}, {"path": "."}, {"path": ""}):
            with self.subTest(child=changes):
                self.ecosystem["child"] = {**original, **changes}
                self.assertTrue(audit.well_formed(self.inventory, self.ecosystem))

    def test_child_nested_layout_and_missing_paths_still_report_gaps(self):
        self.child_owner()
        self.entry["path"] = "tools/child/audits/nested"
        code, output = self.run_main("--check", "--local")
        self.assertEqual(code, 1, output)
        self.assertIn("missing implementation directory tools/child/audits/nested", output)
        self.assertIn("implementation is below a top-level directory", output)

    def test_child_online_audit_reads_only_parent_repository_once(self):
        self.child_owner()
        self.inventory["tools"]["parent_tool"] = {"repo": "sample", "path": "parent_tool",
            "what": "Another tool", "entrypoints": ["scripts/analyze"], "docs": ["docs/usage.md"]}
        self.tree.directories.add("parent_tool")
        with patch.object(audit, "remote_tree", return_value=self.tree) as remote:
            rows, gaps, unseen, notes, trees = audit.inspect(self.inventory, self.ecosystem, online=True)
        remote.assert_called_once_with(self.ecosystem["sample"])
        self.assertEqual(len(rows), 2)
        self.assertFalse(gaps or unseen or notes)

    def test_artifact_needs_content_and_docs_but_no_executable(self):
        self.entry.update(kind="artifact", files=["analyzer/bugs.json", "analyzer/bugs.md"])
        del self.entry["entrypoints"]
        self.tree.files.update(self.entry["files"])
        self.assertEqual(audit.well_formed(self.inventory, self.ecosystem), [])
        code, output = self.run_main("--check", "--local", "--verbose")
        self.assertEqual(code, 0, output)
        self.assertIn("0 tools, 1 artifacts", output)
        self.assertIn("files: analyzer/bugs.json, analyzer/bugs.md", output)
        self.assertNotIn("no entrypoints", output)
        self.tree.files.remove("analyzer/bugs.json")
        code, output = self.run_main("--check", "--local")
        self.assertEqual(code, 1, output)
        self.assertIn("missing files file analyzer/bugs.json", output)

    def test_artifact_records_cannot_hide_absent_content_or_documentation(self):
        self.entry.update(kind="artifact", files=[], docs=[])
        code, output = self.run_main("--check", "--local")
        self.assertEqual(code, 1, output)
        self.assertIn("no files recorded", output)
        self.assertIn("no docs recorded", output)
        for changes in ({"kind": "unknown"}, {"files": "bugs.json"}, {"files": ["../escape"]}):
            with self.subTest(changes=changes):
                inventory = copy.deepcopy(self.inventory)
                inventory["tools"]["analyzer"].update(changes)
                self.assertTrue(audit.well_formed(inventory, self.ecosystem))

    def test_missing_files_unknown_directories_and_stale_exclusions_are_gaps(self):
        self.tree.files.remove("scripts/analyze")
        self.tree.directories.update({"new_tool", "data", ".cache", "tools", "tests",
                                      "examples", "test", "cmake", "include"})
        self.inventory["exclude"] = {"sample": {"data": "fixtures", "removed": "old fixtures"}}
        rows, gaps, unseen, notes, trees = self.inspect()
        self.assertEqual(len(gaps), 5, gaps)
        self.assertIn("missing entrypoints file scripts/analyze", gaps[0])
        self.assertTrue(any("sample/new_tool: unregistered" in gap for gap in gaps))
        self.assertTrue(any("sample/removed: stale exclusion" in gap for gap in gaps))
        self.assertFalse(unseen)
        self.assertEqual(self.run_main("--check", "--local")[0], 1)
        self.assertEqual(self.run_main()[0], 0)

    def test_intentional_exclusions_are_visible_and_fail_requested_comparisons(self):
        self.tree.directories.add("data")
        self.inventory["exclude"] = {"sample": {"data": "Archived inputs, intentionally outside tooling"}}
        for flags in ((), ("--check", "--local"), ("--check", "--online")):
            with self.subTest(flags=flags), patch.object(audit, "remote_tree", return_value=self.tree):
                code, output = self.run_main(*flags)
            self.assertEqual(code, 1 if flags else 0, output)
            self.assertIn("sample/data", output)
            self.assertIn("non-compliant inventory coverage: Archived inputs", output)
            self.assertIn("1 tools, 0 artifacts, 1 intentional exclusions", output)
            self.assertNotIn("sample/data: unregistered", output)
        # The structural check still validates the document alone.
        self.assertEqual(self.run_main("--check")[0], 0)

    def test_exclusions_stay_visible_when_checkout_is_unavailable(self):
        self.inventory["exclude"] = {"sample": {"data": "Archived inputs"}}
        code, output = self.run_main("--check", "--local", error=OSError("offline"))
        self.assertEqual(code, 1, output)
        row = next(line for line in output.splitlines() if line.startswith("sample/data "))
        self.assertIn("unverified", row)
        self.assertIn("non-compliant", row)
        self.assertNotIn("stale exclusion", output)
        self.assertIn("UNVERIFIED sample: offline", output)

    def test_empty_metadata_is_reported_even_without_a_checkout(self):
        self.entry["entrypoints"] = []
        self.entry["docs"] = []
        self.assertEqual(audit.well_formed(self.inventory, self.ecosystem), [])
        code, output = self.run_main("--check", "--local", error=OSError("offline"))
        self.assertEqual(code, 1)
        self.assertIn("no entrypoints recorded", output)
        self.assertIn("no docs recorded", output)
        self.assertIn("UNVERIFIED sample", output)

    def test_unavailable_checkout_is_not_a_missing_implementation(self):
        code, output = self.run_main("--check", "--local", error=OSError("no checkout"))
        self.assertEqual(code, 2)
        self.assertIn("unverified", output)
        self.assertNotIn("missing implementation", output)
        self.assertNotIn("present", output)

    def test_layout_exceptions_are_visible_but_do_not_fail(self):
        for path in ("tools/analyzer", ".", "scripts"):
            with self.subTest(path=path):
                self.entry["path"] = path
                self.entry["also"] = ["analyzer"]
                self.tree.directories.add(path)
                self.entry["layout_note"] = "Uses the parent build"
                code, output = self.run_main("--check", "--local", "--verbose")
                self.assertEqual(code, 0, output)
                self.assertIn("layout gap: Uses the parent build", output)
                self.assertIn("entrypoints: scripts/analyze", output)
                self.assertIn("source: sample: fixture", output)

    def test_root_tool_does_not_hide_unregistered_directories(self):
        self.entry["path"] = "."
        self.assertTrue(any("sample/analyzer: unregistered" in gap for gap in self.inspect()[1]))

    def test_unreadable_paths_are_unverified_not_missing(self):
        tree = audit.Tree([], [], "fixture", Path("/unavailable"))
        with patch.object(Path, "stat", side_effect=PermissionError("unreadable")):
            code, output = self.run_main("--check", "--local", tree=tree)
        self.assertEqual(code, 2, output)
        self.assertIn("UNVERIFIED sample", output)
        self.assertNotIn("missing", output)

    def test_additional_implementation_directory_is_a_layout_gap(self):
        self.entry["also"] = ["support"]
        self.tree.directories.add("support")
        code, output = self.run_main("--check", "--local")
        self.assertEqual(code, 0, output)
        self.assertIn("implementation spans multiple directories", output)

    def test_local_tree_uses_mapping_and_ignores_untracked_build_directories(self):
        with tempfile.TemporaryDirectory(prefix="tooling audit ") as temp:
            root = Path(temp) / "checkout with spaces"
            root.mkdir()
            subprocess.run(["git", "init", "-q", str(root)], check=True)
            for path in ("analyzer/main.py", "scripts/analyze", "docs/usage.md"):
                dest = root / path
                dest.parent.mkdir(exist_ok=True)
                dest.write_text("fixture\n")
            subprocess.run(["git", "-C", str(root), "add", "."], check=True)
            (root / "build").mkdir()
            (root / "build/cache").write_text("ignored")
            mapping = Path(temp) / "repos.local"
            mapping.write_text(f"sample {root}\n")
            with patch.object(audit.status_audit, "REPOS_FILE", str(mapping)):
                tree = audit.local_tree(self.ecosystem["sample"])
            self.assertNotIn("build", tree.directories)
            self.assertTrue(tree.has("scripts/analyze"))
            (root / "scripts/analyze").unlink()
            self.assertFalse(tree.has("scripts/analyze"))
            outside = Path(temp) / "outside"
            outside.write_text("not in the repository")
            (root / "scripts/analyze").symlink_to(outside)
            self.assertFalse(tree.has("scripts/analyze"))
            with patch.object(audit.status_audit, "locate", return_value=str(root / "analyzer")):
                with self.assertRaisesRegex(ValueError, "not the repository root"):
                    audit.local_tree(self.ecosystem["sample"])

    def test_remote_tree_is_fetched_once_per_repo_and_truncation_is_unverified(self):
        self.inventory["tools"]["second"] = {**self.entry, "path": "second"}
        payload = {"sha": "abc123", "truncated": False, "tree": [
            {"path": p, "type": "tree"} for p in ("analyzer", "second", "scripts", "docs")
        ] + [{"path": p, "type": "blob", "mode": "100644"}
             for p in ("scripts/analyze", "docs/usage.md")]}
        with patch.object(audit.urllib.request, "urlopen", return_value=io.StringIO(json.dumps(payload))) as request:
            rows, gaps, unseen, notes, trees = audit.inspect(self.inventory, self.ecosystem, online=True)
        request.assert_called_once()
        self.assertTrue(request.call_args.args[0].full_url.endswith("/git/trees/HEAD?recursive=1"))
        self.assertFalse(gaps or unseen)
        payload["truncated"] = True
        with patch.object(audit.urllib.request, "urlopen", return_value=io.StringIO(json.dumps(payload))):
            rows, gaps, unseen, notes, trees = audit.inspect(self.inventory, self.ecosystem, online=True)
        self.assertFalse(gaps)
        self.assertIn("incomplete", unseen[0])

    def test_online_failure_and_actual_gap_have_distinct_exit_codes(self):
        for error, expected in ((urllib.error.URLError("offline"), 2), (None, 1)):
            with self.subTest(error=error):
                empty = audit.Tree([], [], "remote")
                with patch.object(audit, "remote_tree", return_value=empty, side_effect=error):
                    code, output = self.run_main("--check", "--online")
                self.assertEqual(code, expected, output)

    def test_json_load_errors_are_actionable(self):
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp) / "inventory.json"
            for contents in ('{"tools": {}, "tools": {}}', '[1, 2]', '{'):
                path.write_text(contents)
                with self.subTest(contents=contents), patch.object(audit, "INVENTORY", path), \
                     contextlib.redirect_stdout(io.StringIO()) as output:
                    self.assertEqual(audit.main(["--check"]), 1)
                    self.assertIn("FAIL", output.getvalue())

    def test_launcher_works_from_another_directory_and_rejects_bad_flags(self):
        with tempfile.TemporaryDirectory() as temp:
            for args, expected in [(["--check"], 0), (["--help"], 0),
                                   (["--online"], 2), (["--local"], 2),
                                   (["--check", "--local", "--online"], 2), (["--typo"], 2)]:
                with self.subTest(args=args):
                    result = subprocess.run([str(ROOT / "scripts/eo_tooling_audit"), *args],
                                            cwd=temp, env={**os.environ, "PYTHONDONTWRITEBYTECODE": "1"},
                                            capture_output=True, text=True, timeout=30)
                    self.assertEqual(result.returncode, expected, result.stderr)


if __name__ == "__main__":
    unittest.main()
