"""The commands behave offline: the checker launcher, the status reader
and the register audit.

No real assistants, no clones, no network.
"""

import contextlib
import datetime
import io
import json
import os
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from stathmos_support import ROOT, ecosystem, policy_check

class Commands(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix="kanon-handoff-")
        self.addCleanup(self.temp.cleanup)
        self.base = Path(self.temp.name)
        self.source = self.base / "checker checkout"
        self.checker = self.source / "scripts/policy_check.py"
        self.checker.parent.mkdir(parents=True)
        self.checker.write_text(
            "import sys\n"
            "def declaration_in(text): return []\n"
            "def note_in(text): return []\n"
            "def affiliation_in(text): return []\n"
            "if __name__ == '__main__':\n"
            "    print('ok   fixture checker ' + ' '.join(sys.argv[1:]))\n"
        )
        self.env = {**os.environ, "ANOIEU_ROOT": str(self.source),
                    "ANOIEU_REPOS_FILE": str(self.base / "repos.local"),
                    "ANOIEU_REPOS": str(self.base), "PYTHONDONTWRITEBYTECODE": "1"}

    def command(self, *args, env=None):
        return subprocess.run(args, cwd=ROOT, env=env or self.env,
                              capture_output=True, text=True, timeout=30)

    def test_checker_launcher_defaults_to_kanon(self):
        result = subprocess.run(
            [sys.executable, str(ROOT / "tools/stathmos/scripts/policy_check.py")],
            cwd=self.base, env=self.env, capture_output=True, text=True, timeout=30)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn(f"--root {ROOT}", result.stdout)

    def test_legacy_checker_location(self):
        legacy = self.source / "tools/policy_check.py"
        legacy.parent.mkdir()
        self.checker.rename(legacy)
        result = self.command(sys.executable, "tools/stathmos/scripts/policy_check.py",
                              "--root", str(self.base))
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn(f"--root {self.base}", result.stdout)

    def test_missing_checker_is_unverified(self):
        env = {**self.env, "ANOIEU_ROOT": str(self.base / "missing")}
        result = self.command(sys.executable, "tools/stathmos/scripts/policy_check.py", env=env)
        self.assertEqual(result.returncode, 2)
        self.assertIn("UNVERIFIED", result.stderr)
        with patch.dict(os.environ, env):
            verdict, detail = ecosystem.check(str(ROOT))
        self.assertEqual(verdict, "unverified")
        self.assertIn("ANOIEU_ROOT", detail[0])

    def test_checker_failures_preserve_the_count(self):
        self.checker.write_text("print('ok   a passing check')\nprint('     unrelated note')\n"
                                "print('FAIL a real failure')\nprint('     its cause')\n"
                                "print('skip something else')\nprint('     another note')\n"
                                "raise SystemExit(1)\n")
        with patch.dict(os.environ, self.env):
            verdict, detail = ecosystem.check(str(ROOT))
        self.assertEqual((verdict, detail), ("1 failing", ["a real failure", "its cause"]))

    def test_checker_crash_after_partial_output_is_unverified(self):
        self.checker.write_text("print('FAIL partial result')\nraise SystemExit(2)\n")
        with patch.dict(os.environ, self.env):
            verdict, detail = ecosystem.check(str(ROOT))
        self.assertEqual(verdict, "unverified")
        self.assertIn("partial result", detail[0])

    def test_checker_failure_without_indented_detail_is_visible(self):
        self.checker.write_text("print('FAIL missing declaration')\nraise SystemExit(1)\n")
        with patch.dict(os.environ, self.env):
            self.assertEqual(ecosystem.check(str(ROOT)),
                             ("1 failing", ["missing declaration"]))

    def test_online_declaration_reader_uses_anoieu(self):
        with patch.dict(os.environ, self.env), patch.object(ecosystem, "readme_of", return_value=("member", "")):
            # Keep this test independent of any previous cached module load.
            ecosystem.policy_checker.cache_clear()
            try:
                self.assertEqual(ecosystem.still_true({"example": {"status": "member", "url": "unused"}}), ([], []))
            finally:
                ecosystem.policy_checker.cache_clear()

    def test_online_flag_without_check_is_not_silently_ignored(self):
        result = self.command("scripts/eo_status_audit", "--online")
        self.assertEqual(result.returncode, 2)
        self.assertIn("--online requires --check", result.stderr)

    def test_audit_launcher_reads_its_own_checkout_from_another_directory(self):
        checkout = self.base / "kanon checkout"
        for relative in ("scripts/eo_status_audit", "tools/stathmos/scripts/policy_check.py",
                         "tools/stathmos/scripts/status_audit.py",
                         "tools/stathmos/scripts/child_listing.py"):
            target = checkout / relative
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(ROOT / relative, target)
        inventory = checkout / "scripts/ecosystem/ecosystem.json"
        inventory.parent.mkdir(parents=True)
        inventory.write_text(json.dumps({"example": {
            "status": "member", "repo": "example",
            "url": "https://example.invalid/example", "what": "fixture",
        }}))
        board = checkout / "docs/board.md"
        board.parent.mkdir()
        for entity, code in (("example", 0), ("unregistered", 1)):
            with self.subTest(entity=entity):
                board.write_text(f"**Entities:** `{entity}`\n")
                result = subprocess.run(
                    [str(checkout / "scripts/eo_status_audit"), "--check"],
                    cwd=self.base, env=self.env, capture_output=True,
                    text=True, timeout=30)
                self.assertEqual(result.returncode, code, result.stderr)
                self.assertIn("1 entries", result.stdout)
                if code:
                    self.assertIn("addresses `unregistered`", result.stdout)
                else:
                    self.assertIn("0 failure(s)", result.stdout)

    def test_search_roots_preserve_spaces_and_colons(self):
        # ANOIEU_REPOS is colon-separated and its entries may contain spaces.
        # A bash launcher used to split it with IFS; that launcher is gone and
        # the Python reader of the same variable is what is left to guard.
        first, second = self.base / "first root", self.base / "second root"
        (second / "anoieu" / "scripts").mkdir(parents=True)
        (second / "anoieu" / "scripts" / "policy_check.py").write_text("")
        # The mapping file is consulted before the search roots, so point it
        # at nothing: this is a test of the roots, not of the mapping.
        env = {"ANOIEU_REPOS": f"{first}:{second}",
               "ANOIEU_REPOS_FILE": str(self.base / "no-such-map")}
        with patch.dict(os.environ, env, clear=False):
            os.environ.pop("ANOIEU_ROOT", None)
            found = policy_check.checkout()
        self.assertEqual(found, (second / "anoieu").resolve())

class Verification(unittest.TestCase):

    def test_distinct_projects_can_have_similar_names(self):
        inv = {
            "eschaton": {"status": "member", "repo": "eschaton",
                         "url": "https://example.invalid/eschaton", "what": "research"},
            "cvc5": {"status": "foundation", "repo": "cvc5",
                     "url": "https://example.invalid/cvc5", "what": "solver"},
            "cvc6": {"status": "child", "parent": "eschaton",
                     "path": "tools/cvc6", "what": "research position"},
        }
        with patch.object(ecosystem, "board_entities", return_value=set()):
            self.assertEqual(ecosystem.well_formed(inv), [])

    def test_online_audit_distinguishes_mismatch_from_unverified(self):
        for failures, unseen, code in [([], [], 0), (["stale"], [], 1),
                                      ([], ["offline"], 2), (["stale"], ["offline"], 1)]:
            with self.subTest(failures=failures, unseen=unseen):
                out = io.StringIO()
                with patch.object(ecosystem, "still_true", return_value=(failures, unseen)), \
                     contextlib.redirect_stdout(out):
                    self.assertEqual(ecosystem.audit(True), code)
                if unseen:
                    self.assertIn("UNVERIFIED offline", out.getvalue())
                    self.assertNotIn("is current", out.getvalue())

    def test_invalid_inventory_stops_before_remote_reads(self):
        with patch.object(ecosystem, "well_formed", return_value=["missing parent"]), \
             patch.object(ecosystem, "still_true") as remote, \
             contextlib.redirect_stdout(io.StringIO()):
            self.assertEqual(ecosystem.audit(True), 1)
        remote.assert_not_called()

    def test_proposed_associate_is_not_an_unreachable_remote(self):
        checker = unittest.mock.Mock()
        checker.declaration_in.return_value = ["no declaration"]
        checker.note_in.return_value = ["no maintenance note"]
        with patch.object(ecosystem, "policy_checker", return_value=checker), \
             patch.object(ecosystem, "readme_of", return_value=("README", "")):
            self.assertEqual(ecosystem.still_true({"example": {
                "status": "candidate", "proposed": "associate", "url": "unused"}}), ([], []))

    def test_a_topic_naming_several_tools_is_still_addressed_to_us(self):
        # The channel column counted the string `**To:** kanon`, so a notice
        # addressed to every member at once was not counted for anybody but the
        # first name on it -- and a tool whose name merely starts with ours was
        # counted twice over.
        with tempfile.TemporaryDirectory() as temp:
            docs = Path(temp) / "docs"
            docs.mkdir()
            (docs / "discussion.md").write_text(
                "## D1 — for us\n\n**To:** kanon\n\n"
                "## D2 — a notice to everybody\n\n**To:** anoieu, kanon, koine\n\n"
                "## D3 — two of us\n\n**To:** koine, kanon\n\n"
                "## D4 — not for us\n\n**To:** koine\n\n"
                "## D5 — somebody else entirely\n\n**To:** kanonikos\n")
            self.assertEqual(ecosystem.topics_for(temp), "3 for us")
            (docs / "discussion.md").write_text("## D1 — theirs\n\n**To:** koine\n")
            self.assertEqual(ecosystem.topics_for(temp), "yes")
            (docs / "discussion.md").unlink()
            self.assertEqual(ecosystem.topics_for(temp), "none")

    def associate_seen_as(self, pages, **readers):
        """`--check --online` over one recorded associate, with its remote
        pages and the checker's readers supplied."""
        checker = unittest.mock.Mock()
        checker.declaration_in.return_value = ["no declaration"]
        # The affiliating note says a repository is **not** held to the policy,
        # so an associate has no reason to carry one and the real one does not.
        # Reading the README for it is the mistake these tests keep out.
        checker.affiliation_in.return_value = ["README.md has no maintenance note"]
        checker.associate_in.return_value = []
        for name, value in readers.items():
            getattr(checker, name).return_value = value
        with patch.object(ecosystem, "policy_checker", return_value=checker), \
             patch.object(ecosystem, "remote_file",
                          side_effect=lambda url, rel, *a: (pages.get(rel, ""), "")):
            return ecosystem.still_true({"example": {
                "status": "associate", "url": "unused",
                "vetted": "2026-09-17", "why": "its marker says so"}})

    def test_an_associate_is_read_from_its_own_maintenance_page(self):
        stale, unseen = self.associate_seen_as(
            {"README.md": "a front page that declares nothing",
             "docs/maintenance.md": "**Footing:** `associate`"})
        self.assertEqual((stale, unseen), ([], []))

    def test_a_missing_marker_is_our_record_going_stale(self):
        stale, _ = self.associate_seen_as(
            {"README.md": "a front page", "docs/maintenance.md": "# Maintaining"},
            associate_in=["no `**Footing:**` line"])
        self.assertEqual(len(stale), 1)
        self.assertIn("docs/maintenance.md", stale[0])
        self.assertIn("Ours to re-read", stale[0])

    def test_an_associate_that_has_joined_outright_is_a_mismatch(self):
        stale, _ = self.associate_seen_as(
            {"README.md": "part of the Eunoia ecosystem"}, declaration_in=[])
        self.assertEqual(len(stale), 1)
        self.assertIn("it has joined", stale[0])

    def test_a_checker_too_old_to_read_the_marker_is_unverified(self):
        checker = unittest.mock.Mock(spec=["declaration_in", "affiliation_in", "note_in"])
        checker.declaration_in.return_value = ["no declaration"]
        with patch.object(ecosystem, "policy_checker", return_value=checker), \
             patch.object(ecosystem, "remote_file", return_value=("", "")):
            stale, unseen = ecosystem.still_true({"example": {
                "status": "associate", "url": "unused",
                "vetted": "2026-09-17", "why": "its marker says so"}})
        self.assertEqual(stale, [])
        self.assertIn("cannot read an associate's footing marker", unseen[0])

    def status_of(self, statuses, verdict):
        with tempfile.TemporaryDirectory() as temp:
            inv = Path(temp) / "inventory.json"
            inv.write_text(json.dumps({
                s: {"status": s, "what": "example", "published": "Example paper, 2026",
                    "released": "https://example.invalid/source"}
                for s in statuses
            }))
            out = io.StringIO()
            with patch.object(ecosystem, "INVENTORY", str(inv)), \
                 patch.object(ecosystem, "locate", return_value=temp), \
                 patch.object(ecosystem, "age", return_value="?"), \
                 patch.object(ecosystem, "check", return_value=verdict) as checker, \
                 patch.object(sys, "argv", ["eo_status_audit"]), contextlib.redirect_stdout(out):
                self.assertEqual(ecosystem.main(), 0)
            return out.getvalue(), checker

    def test_status_never_policy_checks_an_outsider(self):
        output, checker = self.status_of(["outsider"], ("ok", []))
        checker.assert_not_called()
        self.assertIn("not held", output)

    def test_unpublished_outsiders_are_not_inspected(self):
        for publication in ("none", "unknown", "", None):
            with self.subTest(publication=publication), tempfile.TemporaryDirectory() as temp:
                inv = Path(temp) / "inventory.json"
                entry = {"status": "outsider", "what": "example"}
                if publication is not None:
                    entry["published"] = publication
                inv.write_text(json.dumps({"example": entry}))
                out = io.StringIO()
                with patch.object(ecosystem, "INVENTORY", str(inv)), \
                     patch.object(ecosystem, "locate") as locate, \
                     patch.object(ecosystem, "topics_for") as topics, \
                     patch.object(ecosystem, "age") as age, \
                     patch.object(ecosystem, "check") as check, \
                     patch.object(sys, "argv", ["eo_status_audit"]), \
                     contextlib.redirect_stdout(out):
                    self.assertEqual(ecosystem.main(), 0)
                for reader in (locate, topics, age, check):
                    reader.assert_not_called()
                self.assertIn("treated as private", out.getvalue())

    def test_outsider_eligibility_controls_validation_and_checkout_reads(self):
        offer = {"date": "2026-09-18", "owner": "Example maintainer",
                 "evidence": "The owner volunteered this tool for tracking."}
        cases = [
            ("published", {}, True),
            ("unpublished", {"published": "none"}, False),
            ("unknown publication", {"published": "unknown"}, False),
            ("unreleased", {"released": "none"}, False),
            ("unknown release", {"released": "unknown"}, False),
            ("volunteered unpublished", {"published": "none", "volunteered": offer}, True),
            ("volunteered unknown", {"published": "unknown", "volunteered": offer}, True),
            ("volunteered unreleased", {"released": "none", "volunteered": offer}, True),
            ("volunteered neither", {"released": "none", "published": "none",
                                     "volunteered": offer}, True),
            ("empty publication", {"published": "", "volunteered": offer}, False),
            ("missing publication", {"published": None, "volunteered": offer}, False),
            ("empty release", {"released": "", "volunteered": offer}, False),
            ("offer flag", {"published": "none", "volunteered": True}, False),
            ("no owner", {"published": "none", "volunteered": {**offer, "owner": " "}}, False),
            ("no evidence", {"published": "none", "volunteered": {**offer, "evidence": ""}}, False),
            ("invalid date", {"published": "none", "volunteered": {**offer, "date": "2026-02-30"}}, False),
            ("missing date", {"published": "none", "volunteered": {"owner": "Example maintainer",
                                                                     "evidence": "Owner's offer"}}, False),
        ]
        for label, changes, eligible in cases:
            with self.subTest(case=label), tempfile.TemporaryDirectory() as temp:
                entry = {"status": "outsider", "repo": "example", "what": "fixture",
                         "url": "https://example.invalid/example", "vetted": "2026-09-18",
                         "why": "context for our work", "published": "Example paper, 2026",
                         "released": "https://example.invalid/example", **changes}
                inventory = {"example": entry}
                with patch.object(ecosystem, "board_entities", return_value=set()):
                    errors = ecosystem.well_formed(inventory)
                self.assertEqual(not errors, eligible, errors)

                inv = Path(temp) / "inventory.json"
                inv.write_text(json.dumps(inventory))
                out = io.StringIO()
                with patch.object(ecosystem, "INVENTORY", str(inv)), \
                     patch.object(ecosystem, "locate", return_value=temp) as locate, \
                     patch.object(ecosystem, "topics_for", return_value="-") as topics, \
                     patch.object(ecosystem, "age", return_value="?") as age, \
                     patch.object(ecosystem, "check") as check, \
                     patch.object(sys, "argv", ["eo_status_audit"]), \
                     contextlib.redirect_stdout(out):
                    self.assertEqual(ecosystem.main(), 0)
                check.assert_not_called()
                if eligible:
                    locate.assert_called_once_with("example")
                    topics.assert_called_once_with(temp)
                    age.assert_called_once_with(temp)
                    self.assertIn("not held", out.getvalue())
                else:
                    for reader in (locate, topics, age):
                        reader.assert_not_called()
                    self.assertIn("treated as private", out.getvalue())

    def test_an_associate_is_checked_but_is_never_at_fault(self):
        # It owes us nothing, so the number is a measurement. `tracked` rather
        # than `failing` is the whole of what keeps it one.
        output, checker = self.status_of(["associate"], ("2 failing", ["a", "b"]))
        checker.assert_called_once()
        row = next(l for l in output.splitlines() if l.startswith("associate "))
        self.assertIn("2 tracked", row)
        self.assertNotIn("failing", row)
        self.assertNotIn("Theirs to fix", output)
        # and it is not counted against anybody
        self.assertIn("0 of 0 repositories held to the policy", output)

    def test_a_passing_associate_reads_the_same_as_anybody(self):
        output, _ = self.status_of(["associate"], ("ok", []))
        self.assertIn("ok", output)
        self.assertNotIn("tracked", output)
