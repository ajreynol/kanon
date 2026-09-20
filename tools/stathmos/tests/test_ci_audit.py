"""Offline regressions for hosted CI observations, especially false greens."""

import contextlib
import io
import json
from pathlib import Path
import subprocess
import tempfile
import unittest
from unittest.mock import patch
from urllib.parse import parse_qs, urlsplit

from stathmos_support import ROOT
from tools.stathmos.audits import ci_audit as audit

SHA = "a" * 40
ENTRY = {"status": "member", "url": "https://github.com/example/project"}


def workflow(wid=1, **changes):
    return {"id": wid, "name": f"checks-{wid}", "path": f".github/workflows/checks-{wid}.yml",
            "state": "active", "html_url": f"https://github.com/example/project/actions/workflows/{wid}",
            **changes}


def run(wid=1, **changes):
    return {"id": wid, "workflow_id": wid, "head_sha": SHA, "head_branch": "trunk",
            "event": "push", "run_number": 1, "run_attempt": 1,
            "status": "completed", "conclusion": "success",
            "html_url": f"https://github.com/example/project/actions/runs/{wid}", **changes}


class Verdicts(unittest.TestCase):
    def results(self, workflows=None, runs=None):
        return audit.workflow_results(workflows if workflows is not None else [workflow()],
                                      runs if runs is not None else [run()], "trunk", SHA)

    def test_only_matching_commit_and_branch_runs_count(self):
        for changes in ({"head_sha": "b" * 40}, {"head_branch": "feature"},
                        {"event": "pull_request"}, {"event": "pull_request_target"},
                        {"event": "merge_group"}):
            with self.subTest(changes=changes):
                rows = self.results(runs=[run(**changes)])
                self.assertEqual(audit.aggregate(w["state"] for w in rows), "unverified")
                self.assertIn("no run", rows[0]["detail"])

    def test_each_active_workflow_needs_evidence_even_with_duplicate_names(self):
        rows = self.results([workflow(name="tests"), workflow(2, name="tests"),
                             workflow(3, state="disabled_manually")])
        self.assertEqual([w["state"] for w in rows], ["pass", "unverified"])
        self.assertEqual(audit.aggregate(w["state"] for w in rows), "unverified")
        self.assertEqual(audit.aggregate([]), "unverified")

    def test_latest_run_wins_over_an_older_rerun_in_any_order(self):
        older = run(run_attempt=5, updated_at="2026-09-20T15:00:00Z")
        newer = run(id=9, run_number=2, conclusion="failure", updated_at="2026-09-20T14:00:00Z")
        for runs in ([older, newer], [newer, older]):
            self.assertEqual(self.results(runs=runs)[0]["state"], "fail")
        retry = {**newer, "run_attempt": 2, "conclusion": "success"}
        self.assertEqual(self.results(runs=[retry, newer])[0]["state"], "pass")

    def test_successful_manual_event_does_not_hide_push_failure(self):
        rows = self.results(runs=[run(conclusion="failure"),
                                  run(id=2, run_number=2, event="workflow_dispatch")])
        self.assertEqual(audit.aggregate(w["state"] for w in rows), "fail")
        self.assertEqual(len(rows), 2)

    def test_conclusions_and_in_progress_reruns(self):
        for conclusion, expected in [("success", "pass"), ("failure", "fail"),
                                     ("cancelled", "fail"), ("timed_out", "fail"),
                                     ("action_required", "fail"), ("skipped", "unverified"),
                                     ("neutral", "unverified"), (None, "unverified"),
                                     ("unknown", "unverified")]:
            with self.subTest(conclusion=conclusion):
                self.assertEqual(audit.run_state(run(conclusion=conclusion)), expected)
        for status in ("in_progress", "queued", "waiting", "pending", "requested"):
            self.assertEqual(audit.run_state(run(status=status, conclusion=None)), "pending")
        self.assertEqual(audit.aggregate(["pass", "unverified", "pending", "fail"]), "fail")


class RemoteAudit(unittest.TestCase):
    def setUp(self):
        self.calls = []
        self.workflows = [workflow()]
        self.runs = [run()]
        self.branch = "trunk"
        self.commits = [SHA, SHA]

    def remote(self, endpoint):
        self.calls.append(endpoint)
        url = urlsplit(endpoint)
        query = parse_qs(url.query)
        if url.path == "repos/example/project":
            return {"default_branch": self.branch}
        if url.path.startswith("repos/example/project/commits/"):
            return {"sha": self.commits.pop(0)}
        if url.path.endswith("/actions/workflows"):
            values, key = self.workflows, "workflows"
        elif url.path.endswith("/actions/runs"):
            self.assertEqual(query["head_sha"], [SHA])
            self.assertEqual(query["branch"], [self.branch])
            values, key = self.runs, "workflow_runs"
        else:
            self.fail(f"unexpected request: {endpoint}")
        self.assertEqual(query["per_page"], ["100"])
        start = (int(query["page"][0]) - 1) * 100
        return {"total_count": len(values), key: values[start:start + 100]}

    def inspect(self):
        with patch.object(audit, "api", side_effect=self.remote):
            return audit.inspect_repository(("project", ENTRY))

    def test_fetches_all_workflow_and_run_pages(self):
        self.workflows = [workflow(n) for n in range(1, 102)]
        self.runs = [run(n) for n in range(1, 102)]
        self.runs[-1]["conclusion"] = "failure"
        row = self.inspect()
        self.assertEqual(row["state"], "fail")
        self.assertEqual(len(row["workflows"]), 101)
        self.assertTrue(any("workflows?" in c and "page=2" in c for c in self.calls))
        self.assertTrue(any("runs?" in c and "page=2" in c for c in self.calls))

    def test_default_branch_is_discovered_and_url_encoded(self):
        self.branch = "release/stable"
        self.runs[0]["head_branch"] = self.branch
        row = self.inspect()
        self.assertEqual(row["state"], "pass")
        self.assertEqual(row["sha"], SHA)
        self.assertTrue(any(c.endswith("commits/release%2Fstable") for c in self.calls))

    def test_branch_advancing_cannot_report_current_green(self):
        self.commits[-1] = "b" * 40
        row = self.inspect()
        self.assertEqual(row["state"], "unverified")
        self.assertIn("changed during", row["note"])

    def test_absent_and_disabled_workflows_do_not_pass(self):
        for workflows in ([], [workflow(state="disabled_inactivity")]):
            self.workflows, self.commits = workflows, [SHA, SHA]
            self.assertEqual(self.inspect()["state"], "unverified")

    def test_inaccessible_repository_and_bad_responses_are_unverified(self):
        for value in (audit.Unverified("HTTP 403: rate limited"), {}, None):
            kwargs = {"side_effect": value} if isinstance(value, Exception) else {"return_value": value}
            with patch.object(audit, "api", **kwargs):
                row = audit.inspect_repository(("project", ENTRY))
            self.assertEqual(row["state"], "unverified")
            self.assertTrue(row["note"])

    def test_bad_repository_url_does_not_make_requests(self):
        with patch.object(audit, "api") as request:
            row = audit.inspect_repository(("project", {**ENTRY, "url": "https://other.example/a/b"}))
        request.assert_not_called()
        self.assertEqual(row["state"], "unverified")

    def test_invalid_branch_and_commit_are_printable_unverified_rows(self):
        for responses in ([{"default_branch": 123}],
                          [{"default_branch": "trunk"}, {"sha": 123}]):
            with patch.object(audit, "api", side_effect=responses):
                row = audit.inspect_repository(("project", ENTRY))
            with contextlib.redirect_stdout(io.StringIO()) as output:
                audit.render({"observed_at": "2026-09-20", "repositories": [row]})
            self.assertEqual(row["state"], "unverified")
            self.assertIn("unverified", output.getvalue())

    def test_api_cap_and_incomplete_pagination_never_pass(self):
        for response in ({"total_count": 1001, "workflow_runs": [run()]},
                         {"total_count": 1, "workflow_runs": []}):
            with patch.object(audit, "api", return_value=response), self.assertRaises(audit.Unverified):
                audit.collection("repos/example/project/actions/runs", "workflow_runs", capped=True)


class Command(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.inventory = Path(self.temp.name) / "ecosystem.json"
        self.inventory.write_text(json.dumps({"member": ENTRY,
            "president": {**ENTRY, "status": "president"},
            "associate": {**ENTRY, "status": "associate"},
            "foundation": {**ENTRY, "status": "foundation"},
            "candidate": {**ENTRY, "status": "candidate"},
            "outsider": {**ENTRY, "status": "outsider"},
            "child": {"status": "child", "parent": "member"}, "_comment": []}))

    def invoke(self, *args, states=None):
        states = states or {}
        seen = []
        def inspect(item):
            name, _ = item
            seen.append(name)
            return {"name": name, "repository": "example/project", "branch": "trunk", "sha": SHA,
                    "state": states.get(name, "pass"), "workflows": [], "note": ""}
        with patch.object(audit, "INVENTORY", self.inventory), \
             patch.object(audit, "inspect_repository", side_effect=inspect), \
             contextlib.redirect_stdout(io.StringIO()) as output, \
             contextlib.redirect_stderr(io.StringIO()) as error:
            code = audit.main(list(args))
        return code, output.getvalue(), error.getvalue(), seen

    def test_membership_selection_and_json(self):
        code, output, _, seen = self.invoke("--json", "--check")
        self.assertEqual(code, 0)
        self.assertEqual(set(seen), {"member", "president"})
        report = json.loads(output)
        self.assertEqual(report["state"], "pass")
        self.assertIn("observed_at", report)
        self.assertEqual([r["name"] for r in report["repositories"]], ["member", "president"])

    def test_exit_codes_distinguish_failure_from_incomplete(self):
        for state, expected in (("pass", 0), ("fail", 1), ("pending", 2), ("unverified", 2)):
            self.assertEqual(self.invoke("--check", states={"member": state})[0], expected)
            self.assertEqual(self.invoke(states={"member": state})[0], 0)
        self.assertEqual(self.invoke("--check", states={"member": "fail", "president": "unverified"})[0], 1)

    def test_filters_reject_nonmembers_and_empty_register(self):
        self.assertEqual(self.invoke("--repo", "president")[3], ["president"])
        for name in ("outsider", "child", "typo"):
            code, _, error, seen = self.invoke("--repo", name)
            self.assertEqual(code, 2)
            self.assertIn("not registered members", error)
            self.assertFalse(seen)
        for contents in ("{}", "[]", "{invalid"):
            self.inventory.write_text(contents)
            self.assertEqual(self.invoke("--check")[0], 2)

    def test_launcher_is_independent_of_cwd_and_validates_flags_offline(self):
        for args, expected in ((["--help"], 0), (["--typo"], 2)):
            result = subprocess.run([str(ROOT / "scripts/eo_ci_audit"), *args],
                                    cwd=self.temp.name, capture_output=True, text=True, timeout=10)
            self.assertEqual(result.returncode, expected, result.stderr)

    def test_transport_is_get_only_and_handles_missing_auth_timeout_and_bad_json(self):
        good = subprocess.CompletedProcess([], 0, '{"default_branch":"main"}', "")
        with patch.object(audit.subprocess, "run", return_value=good) as request:
            self.assertEqual(audit.api("repos/example/project")["default_branch"], "main")
        self.assertEqual(request.call_args.args[0],
                         ["gh", "api", "--hostname", "github.com", "--method", "GET", "repos/example/project"])
        self.assertEqual(request.call_args.kwargs["timeout"], 30)
        bad = [FileNotFoundError(), subprocess.TimeoutExpired("gh", 30),
               subprocess.CompletedProcess([], 1, "", "gh auth login required"),
               subprocess.CompletedProcess([], 0, "not json", "")]
        for result in bad:
            kwargs = {"side_effect": result} if isinstance(result, Exception) else {"return_value": result}
            with patch.object(audit.subprocess, "run", **kwargs), self.assertRaises(audit.Unverified):
                audit.api("repos/example/project")


if __name__ == "__main__":
    unittest.main()
