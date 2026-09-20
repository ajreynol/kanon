#!/usr/bin/env python3
"""Report GitHub Actions for each member's current default-branch commit.

Reads kanon's register and GitHub through authenticated `gh`; changes nothing.
A pass needs a successful run of every active workflow at the observed commit.
Missing, skipped and neutral results are unverified, including workflows whose
path filters, schedules or manual triggers mean they need not run on each push.
Reusable-only workflows also lack standalone runs; caller results are not
attributed to them, so they remain unverified in this workflow-level report.
Disabled workflows, pull-request runs and CI outside GitHub Actions are outside
this report. Children share the containing member repository's CI.

For each workflow and event, use the newest run (and its latest attempt), not
the most recently updated older run. Different events remain separate so that
a successful manual run cannot hide a failed push run at the same commit.
"""

from __future__ import annotations

import argparse
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

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT))
from tools.stathmos.audits.status_audit import INVENTORY, MEMBERS

STATES = ("fail", "pending", "unverified", "pass")
FAILURES = {"failure", "cancelled", "timed_out", "action_required", "startup_failure", "stale"}
PENDING = {"queued", "in_progress", "waiting", "pending", "requested"}


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


def workflow_results(workflows, runs, branch, sha):
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
            results.append({**base, "event": "", "state": "unverified",
                            "detail": "no run for this commit", "url": workflow.get("html_url", "")})
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
        row["workflows"] = workflow_results(workflows, runs, branch, sha)
        row["state"] = aggregate(w["state"] for w in row["workflows"])
        if not row["workflows"]:
            row["note"] = "no active GitHub Actions workflows"
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
                print(f"    {workflow['name']}{event}: {workflow['detail']}")
                if workflow["url"]:
                    print(f"      {workflow['url']}")
    counts = Counter(r["state"] for r in rows)
    print("\n-- " + ", ".join(f"{counts[state]} {state}" for state in reversed(STATES)))
    print("-- Children share their parent's CI. Active workflows only; missing or skipped runs are unverified.")
    print("-- GitHub Actions only; this does not establish branch-protection requirements or external CI.")


def main(argv=None):
    parser = argparse.ArgumentParser(prog="eo_ci_audit", description=__doc__,
                                     epilog="Requires Python 3 and GitHub CLI authenticated with gh auth login.",
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
