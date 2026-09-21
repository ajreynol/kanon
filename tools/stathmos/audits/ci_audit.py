#!/usr/bin/env python3
"""Report GitHub Actions for each member's current default-branch commit.

Reads kanon's register and GitHub through authenticated `gh`; changes nothing.
A pass needs successful observed runs and no missing push-triggered workflows.
For an absent workflow, read its definition at the observed commit: reusable-only
workflows and workflows without a push trigger are not expected on every commit.
Reusable workflow results belong to callers, whose runs are checked normally.
Missing push-triggered runs, skipped and neutral results remain unverified.
Branch and path filters are not evaluated; an absent filtered push run remains
unverified. Unreadable or unrecognized trigger definitions are also unverified.
Disabled workflows, pull-request runs and CI outside GitHub Actions are outside
this report. Children share the containing member repository's CI.

For each workflow and event, use the newest run (and its latest attempt), not
the most recently updated older run. Different events remain separate so that
a successful manual run cannot hide a failed push run at the same commit.
"""

from __future__ import annotations

import argparse
import base64
from collections import Counter
from concurrent.futures import ThreadPoolExecutor
import datetime
import json
import os
from pathlib import Path
import re
import subprocess
import sys
from urllib.parse import quote, urlencode

try:
    import yaml
except ImportError:
    yaml = None

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT))
from tools.stathmos.audits.status_audit import INVENTORY, MEMBERS

STATES = ("fail", "pending", "unverified", "pass")
FAILURES = {"failure", "cancelled", "timed_out", "action_required", "startup_failure", "stale"}
PENDING = {"queued", "in_progress", "waiting", "pending", "requested"}
# Unknown events stay unverified instead of a typo or new trigger granting an
# exemption. Keep this list with GitHub's documented workflow-trigger events.
EVENTS = set("""branch_protection_rule check_run check_suite create delete
deployment deployment_status discussion discussion_comment fork gollum
issue_comment issues label merge_group milestone page_build public pull_request
pull_request_review pull_request_review_comment pull_request_target push
registry_package release repository_dispatch schedule status watch workflow_call
workflow_dispatch workflow_run""".split())


class Unverified(Exception):
    """An observation could not be established; never a CI failure or pass."""


def api(endpoint):
    """Only GET requests, with a bounded wait and no interactive prompts."""
    try:
        result = subprocess.run(
            ["gh", "api", "--hostname", "github.com", "--method", "GET", endpoint],
            input="", capture_output=True, text=True, timeout=30,
            env={**os.environ, "GH_PROMPT_DISABLED": "1"})
    except FileNotFoundError as exc:
        raise Unverified("install GitHub CLI and run gh auth login") from exc
    except subprocess.TimeoutExpired as exc:
        raise Unverified("GitHub request timed out after 30 seconds") from exc
    except OSError as exc:
        raise Unverified(f"cannot run gh: {exc}") from exc
    if result.returncode:
        detail = " ".join(result.stderr.split())[:500]
        raise Unverified(detail or f"gh exited {result.returncode}")
    try:
        return json.loads(result.stdout)
    except ValueError as exc:
        raise Unverified("GitHub returned invalid JSON") from exc


def collection(endpoint, key, *, capped=False):
    """Read every page; the filtered Actions runs API has a 1,000-result cap."""
    items = []
    page = 1
    separator = "&" if "?" in endpoint else "?"
    while True:
        response = api(f"{endpoint}{separator}per_page=100&page={page}")
        batch, total = response[key], response["total_count"]
        if (not isinstance(batch, list) or not all(isinstance(x, dict) for x in batch)
                or not isinstance(total, int) or total < 0):
            raise Unverified(f"invalid GitHub {key} response")
        if capped and total > 1000:
            raise Unverified("GitHub's 1,000-run search limit prevents a complete audit")
        items.extend(batch)
        if len(items) >= total:
            return items
        if not batch:
            raise Unverified(f"incomplete GitHub {key} response")
        page += 1


def aggregate(states):
    states = set(states)
    return next((state for state in STATES if state in states), "unverified")


def run_state(run):
    if run.get("status") in PENDING:
        return "pending"
    if run.get("status") == "completed":
        if run.get("conclusion") == "success":
            return "pass"
        if run.get("conclusion") in FAILURES:
            return "fail"
    return "unverified"


def workflow_events(source):
    """Parse data only. BaseLoader preserves the YAML key `on` as a string."""
    if yaml is None:
        raise Unverified("trigger inspection needs PyYAML; run python3 -m pip install -r tools/stathmos/audits/requirements.txt from kanon's root")

    class WorkflowLoader(yaml.BaseLoader):
        def construct_mapping(self, node, deep=False):
            result = {}
            for key, value in self.construct_pairs(node, deep=deep):
                if not isinstance(key, str) or key in result:
                    raise Unverified("workflow YAML has a duplicate or non-string mapping key")
                result[key] = value
            return result

    try:
        document = yaml.load(source, Loader=WorkflowLoader)
    except yaml.YAMLError as exc:
        raise Unverified("cannot parse workflow YAML") from exc
    if not isinstance(document, dict) or "on" not in document:
        raise Unverified("workflow has no readable on declaration")
    triggers = document["on"]
    if isinstance(triggers, str):
        events = [triggers]
    elif isinstance(triggers, dict):
        events = list(triggers)
    elif isinstance(triggers, list):
        events = triggers
    else:
        raise Unverified("unrecognized workflow trigger declaration")
    if not events or any(not isinstance(event, str) or event not in EVENTS for event in events):
        raise Unverified("empty or unrecognized workflow trigger declaration")
    return set(events)


def missing_workflow(base, workflow, sha):
    """Explain absences from the committed definition, never a local checkout."""
    try:
        path = quote(workflow["path"], safe="/")
        response = api(f"{base}/contents/{path}?ref={sha}")
        if response["encoding"] != "base64":
            raise Unverified("workflow source is unavailable")
        source = base64.b64decode("".join(response["content"].split()), validate=True).decode("utf-8")
        events = workflow_events(source)
        if events == {"workflow_call"}:
            return "not_expected", "reusable-only workflow; results belong to caller runs"
        if "push" not in events:
            return "not_expected", f"no push trigger ({', '.join(sorted(events))}); no run expected on every commit"
        return "unverified", "no run for this commit; push trigger present (branch/path filters not evaluated)"
    except (Unverified, KeyError, TypeError, ValueError, AttributeError) as exc:
        return "unverified", f"no run for this commit; trigger inspection unavailable: {exc}"


def workflow_results(workflows, runs, branch, sha, missing=None):
    latest = {}
    for run in runs:
        event = run["event"]
        if (run["head_sha"] != sha or run["head_branch"] != branch
                or event.startswith("pull_request") or event == "merge_group"):
            continue
        key = (run["workflow_id"], event)
        # updated_at would let a rerun of an older run hide a newer failure.
        order = lambda item: (item["run_number"], item.get("run_attempt", 1), item["id"])
        if key not in latest or order(run) > order(latest[key]):
            latest[key] = run

    results = []
    for workflow in sorted(workflows, key=lambda w: (w["name"], w["id"])):
        if workflow["state"] != "active":
            continue
        matching = sorted((event, run) for (wid, event), run in latest.items()
                          if wid == workflow["id"])
        base = {"name": workflow["name"], "path": workflow["path"]}
        if not matching:
            state, detail = missing(workflow) if missing else ("unverified", "no run for this commit")
            results.append({**base, "event": "", "state": state,
                            "detail": detail, "url": workflow.get("html_url", "")})
        for event, run in matching:
            results.append({**base, "event": event, "state": run_state(run),
                            "detail": run.get("conclusion") or run.get("status") or "unknown result",
                            "url": run["html_url"]})
    return results


def inspect_repository(item):
    name, entry = item
    row = {"name": name, "repository": "", "branch": "", "sha": "",
           "state": "unverified", "workflows": [], "note": ""}
    try:
        match = re.fullmatch(r"https://github\.com/([\w.-]+/[\w.-]+?)(?:\.git)?/?", entry.get("url", ""))
        if not match:
            raise Unverified("register entry needs a GitHub repository URL")
        repo = row["repository"] = match[1]
        base = f"repos/{repo}"
        branch = api(base)["default_branch"]
        if not isinstance(branch, str) or not branch:
            raise Unverified("repository has no default branch")
        row["branch"] = branch
        commit_endpoint = f"{base}/commits/{quote(branch, safe='')}"
        sha = api(commit_endpoint)["sha"]
        if not isinstance(sha, str) or not re.fullmatch(r"[0-9a-f]{40}", sha):
            raise Unverified("default-branch commit is unavailable")
        row["sha"] = sha
        workflows = collection(f"{base}/actions/workflows", "workflows")
        query = urlencode({"branch": branch, "head_sha": sha})
        runs = collection(f"{base}/actions/runs?{query}", "workflow_runs", capped=True)
        row["workflows"] = workflow_results(
            workflows, runs, branch, sha, lambda workflow: missing_workflow(base, workflow, sha))
        row["state"] = aggregate(w["state"] for w in row["workflows"])
        if not row["workflows"]:
            row["note"] = "no active GitHub Actions workflows"
        elif all(w["state"] == "not_expected" for w in row["workflows"]):
            row["note"] = "no standalone CI results for this commit; expected absences alone do not establish a pass"
        # Do not announce a green current branch if it advanced during the audit.
        if api(commit_endpoint)["sha"] != sha:
            raise Unverified("default branch changed during the audit; run again")
    except (Unverified, KeyError, TypeError, ValueError, AttributeError) as exc:
        row["state"] = "unverified"
        row["note"] = str(exc) if isinstance(exc, Unverified) else f"invalid GitHub response: {exc}"
    return row


def render(report, verbose=False):
    print(f"GitHub Actions observed {report['observed_at']}")
    rows = report["repositories"]
    width = max([len("member"), *(len(r["name"]) for r in rows)])
    print(f"{'member':<{width}}  {'CI':<10}  {'commit':<12}  branch")
    for row in rows:
        print(f"{row['name']:<{width}}  {row['state']:<10}  {(row['sha'] or '-')[:12]:<12}  {row['branch'] or '-'}")
        if row["note"]:
            print(f"    {row['note']}")
        for workflow in row["workflows"]:
            if verbose or workflow["state"] != "pass":
                event = f" ({workflow['event']})" if workflow["event"] else ""
                label = "not_expected: " if workflow["state"] == "not_expected" else ""
                print(f"    {workflow['name']}{event}: {label}{workflow['detail']}")
                if workflow["url"]:
                    print(f"      {workflow['url']}")
    counts = Counter(r["state"] for r in rows)
    print("\n-- " + ", ".join(f"{counts[state]} {state}" for state in reversed(STATES)))
    print("-- Children share their parent's CI. Absent non-push workflows are not expected on every commit.")
    print("-- Missing push runs, unknown triggers and skipped runs remain unverified; branch/path filters are not evaluated.")
    print("-- GitHub Actions only; this does not establish branch-protection requirements or external CI.")


def main(argv=None):
    parser = argparse.ArgumentParser(prog="eo_ci_audit", description=__doc__,
                                     epilog="Requires Python 3 and authenticated gh; PyYAML is needed to inspect absent workflows' triggers.",
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--repo", action="append", metavar="NAME",
                        help="limit to a member's register name; repeat for several")
    parser.add_argument("--verbose", action="store_true", help="include every workflow and run link")
    parser.add_argument("--json", action="store_true", help="print structured observations")
    parser.add_argument("--check", action="store_true",
                        help="exit 0 if all pass, 1 for observed failures, 2 if otherwise incomplete; default: report only")
    args = parser.parse_args(argv)
    try:
        with open(INVENTORY, encoding="utf-8") as handle:
            inventory = json.load(handle)
        if not isinstance(inventory, dict):
            raise ValueError("register must be a JSON object")
        members = {name: entry for name, entry in inventory.items()
                   if not name.startswith("_") and isinstance(entry, dict)
                   and entry.get("status") in MEMBERS}
        if args.repo:
            unknown = set(args.repo) - members.keys()
            if unknown:
                raise ValueError(f"not registered members: {', '.join(sorted(unknown))}")
            members = {name: members[name] for name in args.repo}
        if not members:
            raise ValueError("no member repositories in the register")
    except (OSError, ValueError) as exc:
        print(f"UNVERIFIED: {exc}", file=sys.stderr)
        return 2
    with ThreadPoolExecutor(max_workers=4) as pool:
        rows = list(pool.map(inspect_repository, sorted(members.items())))
    report = {"observed_at": datetime.datetime.now(datetime.timezone.utc).isoformat(timespec="seconds"),
              "state": aggregate(row["state"] for row in rows), "repositories": rows}
    if args.json:
        print(json.dumps(report, indent=2))
    else:
        render(report, args.verbose)
    return {"pass": 0, "fail": 1, "pending": 2, "unverified": 2}[report["state"]] if args.check else 0


if __name__ == "__main__":
    sys.exit(main())
