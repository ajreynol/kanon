"""Offline regressions for hosted CI observations, especially false greens."""

import base64
import contextlib
import io
import json
from pathlib import Path
import subprocess
import tempfile
import unittest
from unittest.mock import patch
from urllib.error import HTTPError, URLError
from urllib.parse import parse_qs, urlsplit
from urllib.request import HTTPRedirectHandler

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


class TriggerDefinitions(unittest.TestCase):
    def test_scalar_list_mapping_and_quoted_on(self):
        for source, expected in (
            ("on: workflow_call", {"workflow_call"}),
            ("on: [workflow_call, push]", {"workflow_call", "push"}),
            ("on:\n  workflow_call:\n    inputs:\n      version:\n        type: string\n", {"workflow_call"}),
            ("'on': {schedule: [{cron: '0 6 * * 1'}], workflow_dispatch: {}}", {"schedule", "workflow_dispatch"}),
            ('"on":\n  push:\n    branches: [main]\n    paths: ["docs/**"]\n', {"push"}),
            ("events: &events [workflow_call, workflow_dispatch]\non: *events", {"workflow_call", "workflow_dispatch"}),
        ):
            with self.subTest(source=source):
                self.assertEqual(audit.workflow_events(source), expected)

    def test_comments_names_and_job_text_do_not_define_triggers(self):
        source = """name: push
# on: push
on: workflow_call
jobs:
  push:
    steps:
      - run: |
          on: push
"""
        self.assertEqual(audit.workflow_events(source), {"workflow_call"})

    def test_unknown_empty_malformed_or_duplicate_declarations_are_unverified(self):
        for source in ("on: [", "jobs: {}", "on:", "on: []", "on: {}", "on: 42",
                       "on: {puhs: {}}", "on: [{push: {}}]", "on: push\non: workflow_call",
                       "on: {push: {}, push: {}}", "on: {<<: {push: {}}}"):
            with self.subTest(source=source), self.assertRaises(audit.Unverified):
                audit.workflow_events(source)

    def test_missing_parser_is_actionable_and_never_an_exemption(self):
        with patch.object(audit, "yaml", None), self.assertRaisesRegex(audit.Unverified, "requirements.txt"):
            audit.workflow_events("on: workflow_call")


class RemoteAudit(unittest.TestCase):
    def setUp(self):
        self.calls = []
        self.workflows = [workflow()]
        self.runs = [run()]
        self.branch = "trunk"
        self.commits = [SHA, SHA]
        self.sources = {}

    def remote(self, endpoint):
        self.calls.append(endpoint)
        url = urlsplit(endpoint)
        query = parse_qs(url.query)
        if url.path == "repos/example/project":
            return {"default_branch": self.branch}
        if url.path.startswith("repos/example/project/commits/"):
            return {"sha": self.commits.pop(0)}
        if "/contents/" in url.path:
            self.assertEqual(query["ref"], [SHA])
            path = url.path.split("/contents/", 1)[1]
            source = self.sources.get(path, "on: push\n")
            return {"encoding": "base64", "content": base64.b64encode(source.encode()).decode()}
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

    def test_public_audit_works_without_gh_or_credentials(self):
        self.workflows.append(workflow(2))
        self.sources[workflow(2)["path"]] = "on: workflow_call"

        def request(req, timeout):
            self.assertEqual(timeout, 30)
            self.assertEqual(req.get_method(), "GET")
            self.assertIsNone(req.get_header("Authorization"))
            self.assertTrue(req.full_url.startswith("https://api.github.com/"))
            endpoint = req.full_url.removeprefix("https://api.github.com/")
            return io.BytesIO(json.dumps(self.remote(endpoint)).encode())

        with patch.dict(audit.os.environ, {}, clear=True), \
             patch.object(audit.subprocess, "run", side_effect=FileNotFoundError()), \
             patch.object(audit, "urlopen", side_effect=request):
            row = audit.inspect_repository(("project", ENTRY))
        self.assertEqual(row["state"], "pass")
        self.assertEqual(row["sha"], SHA)
        self.assertEqual(row["workflows"][1]["state"], "not_expected")

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

    def test_anoieu_reusable_only_workflow_does_not_require_a_standalone_run(self):
        self.workflows.append(workflow(2, name="policy"))
        self.sources[workflow(2)["path"]] = "on:\n  workflow_call:\n    inputs:\n      version:\n        type: string\n"
        row = self.inspect()
        self.assertEqual(row["state"], "pass")
        reusable = next(w for w in row["workflows"] if w["name"] == "policy")
        self.assertEqual(reusable["state"], "not_expected")
        self.assertIn("caller runs", reusable["detail"])
        with contextlib.redirect_stdout(io.StringIO()) as output:
            audit.render({"observed_at": "2026-09-20", "repositories": [row]})
        self.assertIn("policy: not_expected: reusable-only", output.getvalue())

    def test_eudaimonia_schedule_manual_absence_does_not_obscure_passing_ci(self):
        self.workflows.append(workflow(2, name="SMT semantics drift"))
        self.sources[workflow(2)["path"]] = "on:\n  schedule:\n    - cron: '0 6 * * 1'\n  workflow_dispatch:\n"
        row = self.inspect()
        self.assertEqual(row["state"], "pass")
        self.assertEqual(next(w["state"] for w in row["workflows"]
                              if w["name"] == "SMT semantics drift"), "not_expected")

    def test_reusable_with_push_and_filtered_push_still_need_evidence(self):
        self.workflows.append(workflow(2))
        for source in ("on: [workflow_call, push]", "on: {push: {paths: ['tools/euthyna/**']}}"):
            self.sources[workflow(2)["path"]] = source
            self.commits = [SHA, SHA]
            row = self.inspect()
            self.assertEqual(row["state"], "unverified")
            self.assertIn("push trigger present", row["workflows"][1]["detail"])

    def test_an_actual_non_push_failure_is_never_exempted(self):
        self.runs[0].update(event="schedule", conclusion="failure")
        self.sources[workflow()["path"]] = "on: {schedule: [{cron: '0 6 * * 1'}]}"
        self.assertEqual(self.inspect()["state"], "fail")
        self.assertFalse(any("/contents/" in call for call in self.calls))

    def test_only_expected_absences_do_not_establish_passing_ci(self):
        self.runs = []
        self.sources[workflow()["path"]] = "on: workflow_call"
        row = self.inspect()
        self.assertEqual(row["state"], "unverified")
        self.assertIn("no standalone CI results", row["note"])

    def test_unreadable_source_or_bad_yaml_cannot_hide_a_known_failure(self):
        self.workflows.append(workflow(2))
        self.runs[0]["conclusion"] = "failure"
        remote = self.remote
        for failure in ("network", "malformed", "base64"):
            self.commits = [SHA, SHA]
            def request(endpoint):
                if "/contents/" in endpoint:
                    if failure == "network":
                        raise audit.Unverified("HTTP 403")
                    if failure == "base64":
                        return {"encoding": "base64", "content": "%%%"}
                    return {"encoding": "base64", "content": base64.b64encode(b"on: [").decode()}
                return remote(endpoint)
            with self.subTest(failure=failure), patch.object(audit, "api", side_effect=request):
                row = audit.inspect_repository(("project", ENTRY))
            self.assertEqual(row["state"], "fail")
            self.assertEqual(row["workflows"][1]["state"], "unverified")


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
        bad = [subprocess.TimeoutExpired("gh", 30),
               subprocess.CompletedProcess([], 1, "", "gh auth login required"),
               subprocess.CompletedProcess([], 0, "not json", "")]
        for result in bad:
            kwargs = {"side_effect": result} if isinstance(result, Exception) else {"return_value": result}
            with patch.object(audit.subprocess, "run", **kwargs), self.assertRaises(audit.Unverified):
                audit.api("repos/example/project")


class HttpTransport(unittest.TestCase):
    def test_missing_gh_and_login_required_use_http(self):
        for result in (FileNotFoundError(),
                       subprocess.CompletedProcess([], 4, "", "gh auth login required")):
            kwargs = {"side_effect": result} if isinstance(result, Exception) else {"return_value": result}
            with self.subTest(result=result), \
                 patch.object(audit.subprocess, "run", **kwargs), \
                 patch.object(audit, "http_api", return_value={"default_branch": "main"}) as request:
                self.assertEqual(audit.api("repos/example/project"), {"default_branch": "main"})
            request.assert_called_once_with("repos/example/project")

    def test_tokens_are_optional_prioritized_and_not_forwarded_on_redirect(self):
        for env, expected in (({}, None), ({"GH_TOKEN": "first", "GITHUB_TOKEN": "second"}, "first"),
                              ({"GITHUB_TOKEN": "second"}, "second")):
            with self.subTest(env=env), patch.dict(audit.os.environ, env, clear=True), \
                 patch.object(audit, "urlopen", return_value=io.BytesIO(b'{"ok": true}')) as request:
                self.assertEqual(audit.http_api("repos/example/project"), {"ok": True})
            req = request.call_args.args[0]
            self.assertEqual(req.full_url, "https://api.github.com/repos/example/project")
            self.assertEqual(req.get_method(), "GET")
            self.assertEqual(request.call_args.kwargs["timeout"], 30)
            self.assertEqual(req.get_header("Authorization"), f"Bearer {expected}" if expected else None)
            redirected = HTTPRedirectHandler().redirect_request(
                req, None, 302, "Found", {}, "https://example.invalid/redirect")
            self.assertIsNone(redirected.get_header("Authorization"))

    def test_http_failures_remain_unverified_and_explain_recovery(self):
        url = "https://api.github.com/repos/example/project"
        cases = [(HTTPError(url, 403, "Forbidden", {"X-RateLimit-Remaining": "0"}, None), "rate limit"),
                 (HTTPError(url, 429, "Too many requests", {}, None), "rate limit"),
                 (HTTPError(url, 401, "Unauthorized", {}, None), "authentication"),
                 (HTTPError(url, 403, "Forbidden", {}, None), "read access"),
                 (HTTPError(url, 404, "Not found", {}, None), "read access"),
                 (HTTPError(url, 503, "Unavailable", {}, None), "HTTP 503"),
                 (URLError("offline"), "cannot reach GitHub"),
                 (TimeoutError(), "timed out")]
        for error, detail in cases:
            with self.subTest(error=error), patch.dict(audit.os.environ, {}, clear=True), \
                 patch.object(audit.subprocess, "run", side_effect=FileNotFoundError()), \
                 patch.object(audit, "urlopen", side_effect=error):
                row = audit.inspect_repository(("project", ENTRY))
            self.assertEqual(row["state"], "unverified")
            self.assertIn(detail, row["note"])
            if detail == "rate limit":
                self.assertIn("GH_TOKEN", row["note"])

    def test_invalid_json_is_unverified(self):
        with patch.object(audit, "urlopen", return_value=io.BytesIO(b'not json')), \
             self.assertRaisesRegex(audit.Unverified, "invalid JSON"):
            audit.http_api("repos/example/project")


if __name__ == "__main__":
    unittest.main()
