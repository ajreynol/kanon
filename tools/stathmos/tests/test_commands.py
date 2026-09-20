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

from stathmos_support import ROOT, dioktes, ecosystem, policy_check

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
            [sys.executable, str(ROOT / "tools/stathmos/audits/policy_check.py")],
            cwd=self.base, env=self.env, capture_output=True, text=True, timeout=30)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn(f"--root {ROOT}", result.stdout)

    def test_legacy_checker_location(self):
        legacy = self.source / "tools/policy_check.py"
        legacy.parent.mkdir()
        self.checker.rename(legacy)
        result = self.command(sys.executable, "tools/stathmos/audits/policy_check.py",
                              "--root", str(self.base))
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn(f"--root {self.base}", result.stdout)

    def test_missing_checker_is_unverified(self):
        env = {**self.env, "ANOIEU_ROOT": str(self.base / "missing")}
        result = self.command(sys.executable, "tools/stathmos/audits/policy_check.py", env=env)
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

    def test_readers_are_found_when_the_command_is_only_a_launcher(self):
        """anoieu's command and its readers are different files, and were split.

        `scripts/policy_check.py` became a launcher exporting `main` alone
        while `declaration_in` and its siblings moved into `policy_check/`.
        A loader that reads the command's path returns a module with no
        readers on it, which crashed `--protocol` rather than reporting.
        """
        package = self.source / "policy_check"
        package.mkdir()
        (package / "checker.py").write_text(
            "def declaration_in(text): return []\n"
            "def note_in(text): return []\n"
            "def affiliation_in(text): return []\n"
            "def associate_in(text): return []\n")
        self.checker.write_text("from policy_check.checker import main\n")
        with patch.dict(os.environ, self.env):
            policy_check.policy_checker.cache_clear()
            try:
                module = policy_check.policy_checker()
                self.assertTrue(hasattr(module, "declaration_in"))
                self.assertTrue(hasattr(module, "note_in"))
            finally:
                policy_check.policy_checker.cache_clear()

    def test_a_checker_with_no_readers_anywhere_says_so(self):
        """The failure names the paths it read, so the next move is obvious."""
        self.checker.write_text("def main(): return 0\n")
        with patch.dict(os.environ, self.env):
            policy_check.policy_checker.cache_clear()
            try:
                with self.assertRaises(ImportError) as caught:
                    policy_check.policy_checker()
            finally:
                policy_check.policy_checker.cache_clear()
        self.assertIn("declaration_in", str(caught.exception))
        self.assertIn("scripts/policy_check.py", str(caught.exception))

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
        for relative in ("scripts/eo_status_audit", "tools/stathmos/audits/policy_check.py",
                         "tools/stathmos/audits/status_audit.py",
                         "tools/stathmos/audits/child_listing.py"):
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
            self.assertEqual(ecosystem.topics_for(temp, "koine"), "3 for us")
            (docs / "discussion.md").write_text("## D1 — theirs\n\n**To:** koine\n")
            self.assertEqual(ecosystem.topics_for(temp, "koine"), "yes")
            (docs / "discussion.md").unlink()
            self.assertEqual(ecosystem.topics_for(temp, "koine"), "none")

    def test_our_own_broadcasts_are_not_topics_owed_to_us(self):
        # A global announcement enumerates every member, and this office is a
        # member, so our own outbox named us twice and the summary reported two
        # topics owed to us that nobody could act on.
        with tempfile.TemporaryDirectory() as temp:
            docs = Path(temp) / "docs"
            docs.mkdir()
            (docs / "discussion.md").write_text(
                "## D1 — a notice to every member\n\n**To:** anoieu, kanon, koine\n\n"
                "## D2 — another\n\n**To:** kanon, tachyon\n")
            self.assertEqual(ecosystem.topics_for(temp, "kanon"), "yes")
            self.assertEqual(ecosystem.topics_for(temp, "koine"), "2 for us")

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
                     patch.object(ecosystem, "check") as check, \
                     patch.object(sys, "argv", ["eo_status_audit"]), \
                     contextlib.redirect_stdout(out):
                    self.assertEqual(ecosystem.main(), 0)
                for reader in (locate, topics, check):
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
                     patch.object(ecosystem, "check") as check, \
                     patch.object(sys, "argv", ["eo_status_audit"]), \
                     contextlib.redirect_stdout(out):
                    self.assertEqual(ecosystem.main(), 0)
                check.assert_not_called()
                if eligible:
                    locate.assert_called_once_with("example")
                    topics.assert_called_once_with(temp, "example")
                    self.assertIn("not held", out.getvalue())
                else:
                    for reader in (locate, topics):
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


class Pursuits(unittest.TestCase):
    """`_pursuits` read against `docs/laws.md` LAW 10."""

    inventory = {
        "kanon": {"status": "president", "repo": "kanon",
                  "url": "https://example.invalid/kanon", "what": "the policy"},
        "logos": {"status": "member", "repo": "logos",
                  "url": "https://example.invalid/logos", "what": "a checker"},
        "outside": {"status": "outsider", "repo": "outside", "vetted": "2026-09-01",
                    "url": "https://example.invalid/outside", "what": "a tool",
                    "why": "comparison data",
                    "released": "https://example.invalid/outside",
                    "published": "A paper, 2026. https://example.invalid/paper"},
        "ethos": {"status": "candidate", "repo": "ethos",
                  "url": "https://example.invalid/ethos", "what": "a checker"},
        "stathmos": {"status": "child", "parent": "kanon",
                     "path": "tools/stathmos", "what": "the audits"},
    }

    record = {"pursuer": "kanon", "target": "outside", "basis": "external",
              "responsible": "the maintainer", "scope": "the signatures",
              "started": "2026-09-01", "declared": "2026-09-20",
              "closes": "the campaign is retired", "state": "active",
              "reporting": "public"}

    def errors(self, *pursuits, **changes):
        inv = {k: dict(v) for k, v in self.inventory.items()}
        for name, fields in changes.items():
            inv[name].update(fields)
        return ecosystem.pursuits_well_formed(inv, list(pursuits))

    def test_a_complete_external_record_passes(self):
        self.assertEqual(self.errors(self.record), [])

    def test_every_field_is_required(self):
        for field in ecosystem.PURSUIT_FIELDS:
            with self.subTest(field=field):
                short = {k: v for k, v in self.record.items() if k != field}
                self.assertIn(f"needs `{field}`", " ".join(self.errors(short)))

    def test_an_external_target_still_needs_law_9_evidence(self):
        blind = {"released": "", "published": ""}
        self.assertIn("LAW 9's evidence", " ".join(self.errors(self.record, outside=blind)))

    def test_every_footing_outside_the_ecosystem_is_reachable(self):
        # LAW 10.1 reaches a foundation, candidate, associate and outsider
        # alike, and LAW 9's evidence rather than the footing permits each one.
        evidence = {"released": "https://example.invalid/e",
                    "published": "A paper, 2026. https://example.invalid/p"}
        record = {**self.record, "target": "ethos"}
        for footing in ecosystem.PURSUIT_BASES["external"]:
            with self.subTest(footing=footing):
                self.assertIn("LAW 9's evidence",
                              " ".join(self.errors(record, ethos={"status": footing})))
                self.assertEqual(
                    self.errors(record, ethos={**evidence, "status": footing}), [])

    def test_a_member_is_out_of_reach_of_the_external_basis(self):
        # LAW 9 does not track a member, so `external` has no evidence to rest
        # on; LAW 10.4 is the only way to one.
        self.assertIn("does not reach",
                      " ".join(self.errors({**self.record, "target": "logos"})))

    def test_membership_is_the_standing_for_a_member_target(self):
        member = {**self.record, "target": "logos", "basis": "member"}
        self.assertEqual(self.errors(member), [])
        # and it is the only basis that reaches one: a member is not tracked
        # under LAW 9, so `outsider` has no evidence to rest on.
        wrong = {**self.record, "target": "logos"}
        self.assertIn("does not reach", " ".join(self.errors(wrong)))

    def test_a_child_is_reached_on_its_parents_footing(self):
        # LAW 1 gives a child its parent's footing, so the basis and LAW 9's
        # evidence are both read off the parent.
        target = {**self.record, "target": "stathmos", "basis": "member"}
        self.assertEqual(self.errors(target), [])
        self.assertIn("through `kanon`",
                      " ".join(self.errors({**target, "basis": "external"})))

    def test_a_child_pursues_on_its_parents_footing(self):
        # metagraphe pursuing cvc5 is tachyon's standing and responsibility.
        self.assertEqual(self.errors({**self.record, "pursuer": "stathmos"}), [])
        # and a child of a non-member has no standing to lend it
        stray = {"stray": {"status": "child", "parent": "ethos",
                           "path": "tools/stray", "what": "a child"}}
        self.assertIn("only a member of this ecosystem investigates",
                      " ".join(ecosystem.pursuits_well_formed(
                          {**self.inventory, **stray},
                          [{**self.record, "pursuer": "stray"}])))

    def test_both_ends_are_in_the_register(self):
        for end in ("target", "pursuer"):
            with self.subTest(end=end):
                self.assertIn("no row in this file",
                              " ".join(self.errors({**self.record, end: "nobody"})))

    def test_a_record_cannot_predate_the_work_it_records(self):
        early = {**self.record, "declared": "2026-08-01"}
        self.assertIn("cannot predate", " ".join(self.errors(early)))
        for field in ("started", "declared"):
            with self.subTest(field=field):
                self.assertIn("not a YYYY-MM-DD date",
                              " ".join(self.errors({**self.record, field: "last spring"})))

    def test_private_continuation_is_representable(self):
        # LAW 10.3 after a LAW 10.2 request: the work goes on, the reporting
        # stops. Collapsing the two states would lose exactly this row.
        quiet = {**self.record, "reporting": "stopped"}
        self.assertEqual(self.errors(quiet), [])

    def test_a_closed_investigation_keeps_its_dated_closure(self):
        closed = {**self.record, "state": "closed", "closed": "2026-09-19"}
        self.assertEqual(self.errors(closed), [])
        undated = {**self.record, "state": "closed"}
        self.assertIn("keeps the date it closed", " ".join(self.errors(undated)))
        self.assertIn("`closed` is set",
                      " ".join(self.errors({**self.record, "closed": "2026-09-19"})))

    def test_one_target_may_have_several_pursuers(self):
        second = {**self.record, "pursuer": "logos"}
        self.assertEqual(self.errors(self.record, second), [])
        # but one pursuer twice over is two records of one investigation
        self.assertIn("same pursuer", " ".join(self.errors(self.record, dict(self.record))))
        # and a closed record beside a live one is the retained history
        done = {**self.record, "state": "closed", "closed": "2026-09-10"}
        self.assertEqual(self.errors(done, self.record), [])

    def test_the_old_per_entry_field_is_rejected_rather_than_ignored(self):
        inv = {**self.inventory, "outside": {**self.inventory["outside"],
                                             "dioktes": "2026-09-01 -- a fix lands"}}
        with patch.object(ecosystem, "board_entities", return_value=set()):
            self.assertIn("`_pursuits`", " ".join(ecosystem.well_formed(inv)))

    def test_a_pursuits_value_that_is_not_a_list_fails(self):
        self.assertIn("records investigations in a list",
                      " ".join(ecosystem.pursuits_well_formed(self.inventory, {})))


class DioktesAudit(unittest.TestCase):
    """`scripts/eo_dioktes_audit`: the records read back against the register."""

    inventory = dict(Pursuits.inventory)
    record = dict(Pursuits.record)

    def audit(self, *pursuits, **changes):
        inv = {k: dict(v) for k, v in self.inventory.items()}
        for name, fields in changes.items():
            inv[name].update(fields)
        return inv, list(pursuits)

    def verdict(self, inv, pursuits) -> int:
        """`check`, without its report in the middle of the test output."""
        with contextlib.redirect_stdout(io.StringIO()):
            return dioktes.check(inv, pursuits)

    def test_a_good_basis_reports_nothing_against_the_row(self):
        inv, pursuits = self.audit(self.record)
        self.assertEqual(dioktes.basis_holds(inv, pursuits[0]), "")
        self.assertEqual(self.verdict(inv, pursuits), 0)

    def test_a_member_leaving_lapses_a_law_104_basis(self):
        # The failure the command exists for: LAW 2.1 is exercised in somebody
        # else's tree and the declaration here does not change by a character.
        member = {**self.record, "target": "logos", "basis": "member"}
        inv, pursuits = self.audit(member, logos={"status": "candidate"})
        self.assertIn("the basis has lapsed", dioktes.basis_holds(inv, pursuits[0]))
        self.assertEqual(self.verdict(inv, pursuits), 1)

    def test_losing_law_9_evidence_lapses_an_external_basis(self):
        inv, pursuits = self.audit(self.record, outside={"published": ""})
        self.assertIn("no longer records the release and publication",
                      dioktes.basis_holds(inv, pursuits[0]))

    def test_a_child_takes_its_parents_footing_both_ways(self):
        through = {**self.record, "pursuer": "stathmos", "target": "stathmos",
                   "basis": "member"}
        inv, pursuits = self.audit(through)
        self.assertEqual(dioktes.basis_holds(inv, pursuits[0]), "")
        # and the parent losing membership lapses the child's basis with it
        inv, pursuits = self.audit(through, kanon={"status": "candidate"})
        self.assertIn("the basis has lapsed", dioktes.basis_holds(inv, pursuits[0]))

    def test_a_stopped_row_is_called_out_and_sorted_first(self):
        quiet = {**self.record, "pursuer": "logos", "reporting": "stopped"}
        inv, pursuits = self.audit(self.record, quiet)
        out = dioktes.render(inv, pursuits, False)
        self.assertIn("reporting and contact ended on request", out)
        body = [l for l in out.splitlines() if l.startswith(("logos", "kanon"))]
        self.assertTrue(body[0].startswith("logos"), out)

    def test_an_empty_record_says_what_it_does_not_mean(self):
        out = dioktes.render(self.inventory, [], False)
        self.assertIn("not evidence that nobody is investigating", out)

    def test_verbose_adds_the_scope_and_the_closing_condition(self):
        inv, pursuits = self.audit(self.record)
        out = dioktes.render(inv, pursuits, True)
        self.assertIn(self.record["scope"], out)
        self.assertIn(self.record["closes"], out)

    def test_it_reads_the_registers_own_records(self):
        # The declarations in the tree are well formed and their bases hold.
        inv, pursuits = dioktes.load()
        self.assertTrue(pursuits, "the register records no investigation")
        self.assertEqual(self.verdict(inv, pursuits), 0)
