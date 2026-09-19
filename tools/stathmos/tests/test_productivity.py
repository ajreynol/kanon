"""Productivity evidence, using the real tooling inspection with fixture trees."""

import contextlib
import io
import json
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch

from stathmos_support import ecosystem as status
from tools.stathmos.audits import productivity, tooling_audit


class Productivity(unittest.TestCase):
    def setUp(self):
        temporary = tempfile.TemporaryDirectory(prefix="kanon-productivity-")
        self.addCleanup(temporary.cleanup)
        self.root = Path(temporary.name)
        (self.root / "docs").mkdir()
        for document in (*productivity.CENTRAL_DOCUMENTS, "docs/roles.md"):
            (self.root / document).write_text("# Fixture\n", encoding="utf-8")
        self.ecosystem = {
            "host": {"status": "member", "repo": "host",
                     "url": "https://example.invalid/host", "what": "parent"},
            "child": {"status": "child", "parent": "host", "path": "tools/child",
                      "what": "child project"},
        }
        self.inventory = self.root / "tooling.json"
        self.inventory.write_text('{"tools": {}}')
        self.tree = tooling_audit.Tree(set(), set(), "fixture")
        for replacement in (
            patch.object(productivity, "ROOT", self.root),
            patch.object(tooling_audit, "INVENTORY", self.inventory),
            patch.object(tooling_audit, "local_tree", side_effect=lambda repo: self.tree),
        ):
            replacement.start()
            self.addCleanup(replacement.stop)

    def deliverable(self, owner="host", kind="tool", **changes):
        directory = "reports" if owner == "host" else "tools/child/reports"
        entry = {"repo": "host", "owner": owner, "kind": kind, "path": directory,
                 "what": "Example contribution", "docs": ["docs/usage.md"]}
        field = "files" if kind in tooling_audit.CONTENT_KINDS else "entrypoints"
        entry[field] = [f"{directory}/content"]
        entry.update(changes)
        self.inventory.write_text(json.dumps({"tools": {"contribution": entry}}))
        self.tree = tooling_audit.Tree({f"{directory}/content", "docs/usage.md"},
                                       {directory, "tools", "docs"}, "fixture")

    def assess(self):
        return productivity.assess(self.ecosystem)

    def test_every_tool_and_artifact_kind_can_supply_a_deliverable(self):
        for kind in tooling_audit.KINDS:
            with self.subTest(kind=kind):
                self.deliverable(kind=kind)
                result = self.assess()["host"]
                self.assertEqual(result.value, "yes")
                self.assertIn(f"contribution ({kind}) present", " ".join(result.reasons))

    def test_deliverables_belong_only_to_the_recorded_owner(self):
        for owner, other in (("host", "child"), ("child", "host")):
            with self.subTest(owner=owner):
                self.deliverable(owner)
                results = self.assess()
                self.assertEqual(results[owner].value, "yes")
                self.assertEqual(results[other].value, "no")
        inventory = json.loads(self.inventory.read_text())
        del inventory["tools"]["contribution"]["owner"]
        self.inventory.write_text(json.dumps(inventory))
        self.assertEqual(self.assess()["host"].value, "yes")
        self.assertEqual(self.assess()["child"].value, "no")

    def test_missing_paths_or_required_metadata_do_not_prove_productivity(self):
        self.deliverable()
        self.tree.files.remove("reports/content")
        result = self.assess()["host"]
        self.assertEqual(result.value, "no")
        self.assertIn("missing entrypoints file", " ".join(result.reasons))
        self.deliverable(kind="database", files=[])
        self.assertEqual(self.assess()["host"].value, "no")

    def test_layout_and_other_inventory_gaps_do_not_erase_a_deliverable(self):
        self.deliverable(layout_note="Existing implementation spans its owner's root")
        self.tree.directories.add("archive")
        self.assertEqual(self.assess()["host"].value, "yes")
        inventory = json.loads(self.inventory.read_text())
        inventory["exclude"] = {"host": {"archive": "Old experiments"}}
        self.inventory.write_text(json.dumps(inventory))
        self.assertEqual(self.assess()["host"].value, "yes")
        inventory["tools"] = {}
        self.inventory.write_text(json.dumps(inventory))
        self.assertEqual(self.assess()["host"].value, "no")

    def test_unavailable_tooling_is_unverified_but_another_basis_can_suffice(self):
        self.deliverable()
        with patch.object(tooling_audit, "local_tree", side_effect=OSError("no checkout")):
            result = self.assess()["host"]
            self.assertEqual(result.value, "?")
            self.assertIn("no checkout", " ".join(result.reasons))
            # The child owns no recorded tool; an unavailable parent's tool
            # is not an unknown contribution of the child.
            self.assertEqual(self.assess()["child"].value, "no")
            (self.root / "docs/laws.md").write_text("[HOST](https://example.invalid/host) maintains the research boundaries.\n")
            self.assertEqual(self.assess()["host"].value, "yes")

    def test_unreadable_or_invalid_inventory_is_not_silently_empty(self):
        for contents in (None, "{", '{"tools": []}',
                         '{"tools": {"bad": {"repo": "absent"}}}'):
            with self.subTest(contents=contents):
                if contents is None:
                    self.inventory.unlink()
                else:
                    self.inventory.write_text(contents)
                with patch.object(tooling_audit, "inspect") as inspect:
                    self.assertEqual(self.assess()["host"].value, "?")
                inspect.assert_not_called()
                self.ecosystem["host"]["status"] = "president"
                self.assertEqual(self.assess()["host"].value, "yes")
                self.ecosystem["host"]["status"] = "member"

    def test_central_references_exclude_examples_comments_and_partial_names(self):
        decoys = ("# host\n\nhost-extra and ghost are different names.\n"
                  "<!-- host\nchild -->\n"
                  "```md\nhost\n```\n~~~~\nhost\n~~~~\n"
                  "    host\n> host\n[host]: https://example.invalid/host\n")
        for relative in productivity.CENTRAL_DOCUMENTS:
            (self.root / relative).write_text(decoys)
        (self.root / "docs/glossary.md").write_text("host does something.\n")
        self.assertEqual(self.assess()["host"].value, "no")
        for relative in productivity.CENTRAL_DOCUMENTS:
            with self.subTest(relative=relative):
                (self.root / relative).write_text(decoys + "[HOST](https://example.invalid/host) maintains the account.\n")
                result = self.assess()["host"]
                self.assertEqual(result.value, "yes")
                self.assertTrue(any(reason.startswith(relative + ":") for reason in result.reasons))
                (self.root / relative).write_text(decoys)

    def test_links_identify_entities_without_confusing_names_or_parents(self):
        self.ecosystem["eunoia"] = {"status": "member", "repo": "eunoia",
                                    "url": "https://example.invalid/eunoia"}
        law = self.root / "docs/laws.md"
        law.write_text("Eunoia is the ecosystem and a language.\n"
                       "The host's child is useful.\n"
                       "[eunoia](https://example.invalid/different) describes a language.\n"
                       "[unused]: https://example.invalid/eunoia\n")
        self.assertEqual(self.assess()["eunoia"].value, "no")
        self.assertEqual(self.assess()["host"].value, "no")
        law.write_text("[This research][work] informs the policy.\n"
                       "[work]: https://example.invalid/host/blob/main/tools/child/README.md\n")
        self.assertEqual(self.assess()["child"].value, "yes")
        self.assertEqual(self.assess()["host"].value, "no")
        self.ecosystem["host"]["status"] = "president"
        law.write_text("[This research](../tools/child/docs/results.md) informs the policy.\n")
        self.assertEqual(self.assess()["child"].value, "yes")

    def test_missing_central_document_is_unverified_without_another_basis(self):
        (self.root / "docs/vision.md").unlink()
        self.assertEqual(self.assess()["host"].value, "?")
        self.deliverable()
        self.assertEqual(self.assess()["host"].value, "yes")

    def test_current_roles_count_but_proposals_and_empty_sections_do_not(self):
        role_page = self.root / "docs/roles.md"
        role_page.write_text("## host\n\n## child\n\n"
                             "> ### R1 — proposed\n> **Held by:** `host`\n"
                             "<!--\n### R2 — removed\n**Held by:** `host`\n-->\n"
                             "```md\n### R3 — example\n**Held by:** `host`\n```\n")
        self.assertEqual(self.assess()["host"].value, "no")
        role_page.write_text(role_page.read_text() +
                             "### R4 — current responsibility\n**Held by:** `child`\n")
        self.assertEqual(self.assess()["host"].value, "no")
        self.assertEqual(self.assess()["child"],
                         productivity.Result("yes", ["docs/roles.md:16: holds R4"]))
        role_page.write_text("### R4 — shared responsibility\n**Held by:** `host`, `child`\n")
        self.assertTrue(all(result.value == "yes" for result in self.assess().values()))

    def test_other_footings_have_no_productivity_requirement(self):
        self.ecosystem = {name: {"status": name} for name in
                          ("candidate", "associate", "foundation", "outsider")}
        with patch.object(tooling_audit, "inspect") as inspect:
            self.assertEqual(self.assess(), {})
        inspect.assert_not_called()

    def test_status_table_and_verbose_evidence_follow_child_visibility(self):
        self.deliverable("child", "tutorial")
        child = self.root / "tools/child"
        child.mkdir(parents=True)
        (child / "README.md").write_text("**Footing:** `unadvertised-child`\n")
        self.ecosystem["foundation"] = {"status": "foundation", "repo": "foundation",
                                       "url": "https://example.invalid/foundation", "what": "base"}
        inventory = self.root / "ecosystem.json"
        inventory.write_text(json.dumps(self.ecosystem))
        for args in ([], ["--all"], ["--all-children"], ["--all", "--verbose"]):
            with self.subTest(args=args), patch.object(status, "INVENTORY", str(inventory)), \
                 patch.object(status, "locate", return_value=str(self.root)), \
                 patch.object(status, "check", return_value=("ok", [])), \
                 patch.object(sys, "argv", ["eo_status_audit", *args]), \
                 contextlib.redirect_stdout(io.StringIO()) as output:
                self.assertEqual(status.main(), 0)
                text = output.getvalue()
                rows = {parts[0]: parts for line in text.splitlines()
                        if (parts := line.split()) and parts[0] in self.ecosystem}
                self.assertEqual(rows["host"][3], "no")
                self.assertEqual(rows["foundation"][3], "-")
                if args:
                    self.assertEqual(rows["child"][3], "yes")
                    self.assertIn("1 of 2 shown entities productive", text)
                else:
                    self.assertNotIn("child", rows)
                    self.assertNotIn("contribution", text)
                    self.assertIn("0 of 1 shown entities productive", text)
                if "--verbose" in args:
                    self.assertIn("child: productive yes: eo_tooling_audit: contribution (tutorial) present", text)
                    self.assertIn("host: productive no:", text)


if __name__ == "__main__":
    unittest.main()
