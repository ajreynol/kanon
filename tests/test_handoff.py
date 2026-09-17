"""Offline regressions for the governance handoff; no real assistants or clones."""

import contextlib
import datetime
import importlib.machinery
import importlib.util
import io
import json
import os
from pathlib import Path
import re
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch
from urllib.parse import unquote, urlsplit


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
bump = load("bump_under_test", "scripts/bump_check.py")


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


class Documents(unittest.TestCase):
    def test_glossary_project_labels_match_inventory(self):
        text = (ROOT / "docs/glossary.md").read_text()
        labels = re.findall(r"^\*\*(.+?)\*\* \(Eunoia ([^;]+);", text, re.M)
        actual = {name.casefold(): label for name, label in labels}
        self.assertEqual(len(actual), len(labels), "duplicate glossary project entries")
        expected = {
            name.casefold(): (f"child project of {entry['parent']}"
                              if entry["status"] == "child" else entry["status"])
            for name, entry in installer.inventory().items()
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
        inv = installer.inventory()
        projects = [p for p in (ROOT / "tools").iterdir() if (p / "README.md").is_file()]
        self.assertTrue(projects)
        for path in projects:
            with self.subTest(project=path.name):
                self.assertEqual(inv[path.name]["parent"], "kanon")
                self.assertEqual(inv[path.name]["path"], path.relative_to(ROOT).as_posix())
                host = next(r for r in installer.plan() if path.name in
                            {c["name"] for c in r.children})
                self.assertEqual(host.key, "kanon")

    def test_shell_syntax(self):
        for path in [ROOT / "scripts/status_eo", *sorted((ROOT / "prompts").iterdir())]:
            with self.subTest(script=path.name):
                result = subprocess.run(["bash", "-n", str(path)], capture_output=True, text=True)
                self.assertEqual(result.returncode, 0, result.stderr)


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
        result = self.command(sys.executable, "scripts/policy_check.py")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn(f"--root {ROOT}", result.stdout)

    def test_legacy_checker_location(self):
        legacy = self.source / "tools/policy_check.py"
        legacy.parent.mkdir()
        self.checker.rename(legacy)
        result = self.command(sys.executable, "scripts/policy_check.py", "--root", str(self.base))
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn(f"--root {self.base}", result.stdout)

    def test_missing_checker_is_unverified(self):
        env = {**self.env, "ANOIEU_ROOT": str(self.base / "missing")}
        result = self.command(sys.executable, "scripts/policy_check.py", env=env)
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

    def test_installer_status_without_anoieu(self):
        env = {**self.env, "ANOIEU_ROOT": str(self.base / "missing")}
        result = self.command(sys.executable, "scripts/install_eo", "--status", "--root", str(self.base), env=env)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("absent", result.stdout)
        self.assertNotIn("Traceback", result.stderr)

    def test_installer_reads_report_pins_from_anoieu(self):
        (self.source / "scripts/deps.json").write_text(json.dumps({"example": {"ref": "pinned"}}))
        with patch.dict(os.environ, self.env):
            self.assertEqual(installer.deps(), {"example": {"ref": "pinned"}})

    def test_dry_run_has_no_side_effects(self):
        dest = self.base / "new destination"
        result = self.command(sys.executable, "scripts/install_eo", "--dry-run", "--root", str(dest), "kanon")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("git clone", result.stdout)
        self.assertFalse(dest.exists())
        self.assertFalse(Path(self.env["ANOIEU_REPOS_FILE"]).exists())

    def test_installer_never_clones_outsiders(self):
        outsiders = {name: entry for name, entry in installer.inventory().items()
                     if entry["status"] == "outsider"}
        self.assertTrue(outsiders)
        outsider_urls = {entry["url"] for entry in outsiders.values()}
        selections = [[], ["--with-optional"], ["--role", "outsider"],
                      list(outsiders), [entry["repo"] for entry in outsiders.values()]]
        for selection in selections:
            for dry_run in (False, True):
                with self.subTest(selection=selection, dry_run=dry_run):
                    argv = ["install_eo", "--root", str(self.base / "install"),
                            "--no-repos-local", *selection]
                    if dry_run:
                        argv.append("--dry-run")
                    out = io.StringIO()
                    with patch.object(sys, "argv", argv), \
                         patch.object(installer, "execute", return_value=0) as execute, \
                         contextlib.redirect_stdout(out):
                        self.assertEqual(installer.main(), 0)
                    for url in outsider_urls:
                        self.assertNotIn(url, out.getvalue())
                    cloned_urls = {call.args[0][-2] for call in execute.call_args_list}
                    self.assertTrue(cloned_urls.isdisjoint(outsider_urls))
                    if dry_run:
                        execute.assert_not_called()
                    elif selection in ([], ["--with-optional"]):
                        self.assertIn(installer.inventory()["kanon"]["url"], cloned_urls)
                    else:
                        execute.assert_not_called()

    def test_installer_status_still_lists_outsiders(self):
        result = self.command(sys.executable, "scripts/install_eo", "--status",
                              "--role", "outsider", "--root", str(self.base))
        self.assertEqual(result.returncode, 0, result.stderr)
        for name, entry in installer.inventory().items():
            if entry["status"] == "outsider":
                self.assertIn(f"{name} -- outsider", result.stdout)

    def test_prompt_previews(self):
        target = self.base / "example"
        (target / ".git").mkdir(parents=True)
        (target / "README.md").write_text("Example\n")
        cases = [("global_audit",),
                 ("check_join_eo", str(target)),
                 ("process_discussion", str(target))]
        for name, *args in cases:
            with self.subTest(prompt=name):
                result = self.command("bash", f"prompts/{name}", *args, "--show-prompt")
                self.assertEqual(result.returncode, 0, result.stderr)
                self.assertNotIn("Traceback", result.stdout + result.stderr)
                self.assertNotIn("can't open file", result.stdout + result.stderr)
                self.assertTrue(result.stdout.strip())
                if name == "process_discussion":
                    self.assertIn("To: names kanon", result.stdout)
        self.assertFalse(Path(self.env["ANOIEU_REPOS_FILE"]).exists())

    def test_prompt_refuses_unavailable_checker(self):
        env = {**self.env, "ANOIEU_ROOT": str(self.base / "missing")}
        result = self.command("bash", "prompts/check_join_eo", "--show-prompt", str(self.base), env=env)
        self.assertEqual(result.returncode, 2)
        self.assertIn("UNVERIFIED", result.stderr)

    def test_global_preview_preserves_unavailable_checks(self):
        env = {**self.env, "ANOIEU_ROOT": str(self.base / "missing")}
        Path(self.env["ANOIEU_REPOS_FILE"]).write_text(f"kanon {self.base}\n")
        result = self.command("bash", "prompts/global_audit", "--show-prompt", env=env)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("policy unverified", result.stdout)
        self.assertIn("anoieu's policy checker is unavailable", result.stdout)

    def test_online_flag_without_check_is_not_silently_ignored(self):
        result = self.command("scripts/status_eo", "--online")
        self.assertEqual(result.returncode, 2)
        self.assertIn("--online requires --check", result.stderr)

    def test_bump_arguments_fail_cleanly(self):
        for args in [("--rev",), ("--unknown",), ("--rev", "main"),
                     ("--rev", "abcdef0", "--root", ".")]:
            with self.subTest(args=args):
                result = self.command(sys.executable, "scripts/bump_check.py", *args)
                self.assertEqual(result.returncode, 2)
                self.assertNotIn("Traceback", result.stderr)

    def test_bump_dry_run_uses_the_workflow_pin(self):
        workflow = self.base / ".github/workflows/anoieu.yml"
        workflow.parent.mkdir(parents=True)
        workflow.write_text("env:\n  ANOIEU_REV: abcdef0123\n")
        result = self.command(sys.executable, "scripts/bump_check.py", "--root",
                              str(self.base), "--dry-run")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("/commits/abcdef0123/check-runs", result.stdout)

    def test_search_roots_preserve_spaces_and_colons(self):
        target = self.base / "second root" / "example"
        target.mkdir(parents=True)
        env = {**self.env, "ANOIEU_REPOS": f"{self.base / 'first root'}:{target.parent}"}
        result = self.command("bash", "prompts/process_discussion", "--show-prompt", "example", env=env)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn(str(target), result.stdout)



class Verification(unittest.TestCase):
    def test_health_uses_local_working_hours_after_ethics_move(self):
        schedule = json.loads((ROOT / "scripts/schedule.json").read_text())
        loaded = working_hours.load()
        self.assertEqual(loaded["source"], "schedule.json")
        self.assertEqual(loaded["available"], schedule["available"])
        self.assertEqual(loaded["set_on"], schedule["set_on"])
        fixed_time = datetime.datetime(2026, 9, 17, 12)
        with patch.object(working_hours, "now_local", return_value=fixed_time), \
             patch.object(ecosystem, "locate", side_effect=AssertionError("no checkout needed")):
            rows = ecosystem.health({})
            clock = working_hours.state()
        hours = next((value, verdict) for name, value, verdict in rows if name == "hours")
        self.assertEqual(hours, (working_hours.summary(clock),
                                 "ok" if clock["status"] == "awake" else "attention"))

    def test_moved_children_resolve_to_epikrisis(self):
        repos = installer.plan()
        with tempfile.TemporaryDirectory() as temp:
            (Path(temp) / "epikrisis/.git").mkdir(parents=True)
            locations = {name: path for name, path, live in installer.repos_local_rows(temp, repos)
                         if live}
        for name in ("martyria", "zetesis"):
            with self.subTest(project=name):
                self.assertEqual(locations[name], str(Path(temp) / "epikrisis"))

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

    def test_status_does_not_policy_check_associates_or_outsiders(self):
        with tempfile.TemporaryDirectory() as temp:
            inv = Path(temp) / "inventory.json"
            inv.write_text(json.dumps({
                status: {"status": status, "what": "example"}
                for status in ("associate", "outsider")
            }))
            out = io.StringIO()
            with patch.object(ecosystem, "INVENTORY", str(inv)), \
                 patch.object(ecosystem, "locate", return_value=temp), \
                 patch.object(ecosystem, "age", return_value="?"), \
                 patch.object(ecosystem, "check") as checker, \
                 patch.object(sys, "argv", ["status_eo"]), contextlib.redirect_stdout(out):
                self.assertEqual(ecosystem.main(), 0)
            checker.assert_not_called()
            self.assertEqual(out.getvalue().count("not held"), 2)

    def test_bump_requires_complete_check_run_response(self):
        success = {"name": "policy", "status": "completed", "conclusion": "success"}
        for data, verified in [({"total_count": 1, "check_runs": [success]}, True),
                               ({"total_count": 2, "check_runs": [success]}, False),
                               ({"check_runs": [success]}, False), ({}, False),
                               ({"total_count": 1, "check_runs": [None]}, False)]:
            with self.subTest(data=data):
                response = io.BytesIO(json.dumps(data).encode())
                with patch.object(bump.urllib.request, "urlopen", return_value=response):
                    runs, why = bump.ask("abcdef0")
                self.assertEqual(not why, verified)
                self.assertEqual(runs, [success] if verified else [])

    def test_bump_verdicts(self):
        for runs, code in [([], 2),
                           ([{"status": "in_progress"}], 2),
                           ([{"status": "completed", "conclusion": "failure"}], 1),
                           ([{"status": "completed", "conclusion": "success"}], 0)]:
            with self.subTest(runs=runs):
                self.assertEqual(bump.verdict(runs)[0], code)


if __name__ == "__main__":
    unittest.main()
