#!/usr/bin/env python3
"""Audit recorded tooling, without executing it or changing its inventory.

ecosystem.json supplies repositories and footings; ecosystem_tooling.json
supplies tool boundaries, entry points, documentation and coverage exclusions.
Directory discovery suggests inventory gaps; it cannot decide what is a tool.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path, PurePosixPath
import re
import stat
import subprocess
import sys
import textwrap
import urllib.parse
import urllib.request

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT))
from tools.stathmos.audits import status_audit

INVENTORY = ROOT / "scripts/ecosystem/ecosystem_tooling.json"
# These directories already have purposes in docs/policy.md's layout table.
SHARED = frozenset({"docs", "scripts", "test", "tests", "examples", "cmake", "include",
                    "licenses", "prompts", "deps", "scratch", "tools"})
# Foundations supply tooling too. These are inventory observations, never a
# policy check or a new obligation on the repository being described.
REPOSITORIES = frozenset(status_audit.OWN_REPO) | {"foundation"}


def relative_path(value, *, root=False):
    """Canonical repository-relative paths; never commands, URLs or traversal."""
    return (isinstance(value, str) and bool(value.strip())
            and (value == "." and root or
                 not value.startswith("/") and "\\" not in value
                 and all(part not in ("", ".", "..") for part in value.split("/"))))


def read_json(path):
    def unique(pairs):
        result = {}
        for key, value in pairs:
            if key in result:
                raise ValueError(f"duplicate JSON key: {key}")
            result[key] = value
        return result

    value = json.loads(Path(path).read_text(encoding="utf-8"), object_pairs_hook=unique)
    if not isinstance(value, dict):
        raise ValueError(f"{path}: expected a JSON object")
    return value


def owner_location(owner, ecosystem):
    """Resolve a repository or child owner to its repository and layout root."""
    if not isinstance(owner, str) or owner not in ecosystem:
        raise ValueError("owner must name an ecosystem repository or child project")
    project = ecosystem[owner]
    if project.get("status") in REPOSITORIES:
        return owner, ""
    if project.get("status") == "child":
        parent, path = project.get("parent"), project.get("path")
        if (isinstance(parent, str) and parent in ecosystem
                and ecosystem[parent].get("status") in REPOSITORIES
                and relative_path(path)):
            return parent, path
        raise ValueError(f"child owner {owner!r} needs an eligible parent repository and a relative project path")
    raise ValueError(f"{owner!r} is outside the tooling audit's scope")


def within_owner(path, prefix):
    """A repository-relative path measured from the owning project's root."""
    return str(PurePosixPath(path).relative_to(prefix or "."))


def well_formed(inventory, ecosystem):
    """Validate records only: CI needs no sibling checkout and no network."""
    bad = []
    entries, excluded = inventory.get("tools"), inventory.get("exclude", {})
    if not isinstance(entries, dict) or not isinstance(excluded, dict):
        return ["`tools` and `exclude` must be objects"]
    locations = {}
    for name, entry in entries.items():
        if not name.strip() or not isinstance(entry, dict):
            bad.append(f"{name}: expected a named tool object")
            continue
        if entry.get("kind", "tool") not in ("tool", "artifact"):
            bad.append(f"{name}: `kind` must be tool or artifact")
        repo = entry.get("repo")
        if not isinstance(repo, str) or repo not in ecosystem or ecosystem[repo].get("status") not in REPOSITORIES:
            bad.append(f"{name}: `repo` must name an ecosystem member, president, associate, candidate or foundation repository")
        try:
            owner_repo, prefix = owner_location(entry.get("owner", repo), ecosystem)
            if owner_repo != repo:
                bad.append(f"{name}: owner belongs to {owner_repo!r}, not repository {repo!r}")
        except ValueError as exc:
            bad.append(f"{name}: {exc}")
            prefix = ""
        if not isinstance(entry.get("what"), str) or not entry["what"].strip():
            bad.append(f"{name}: needs a nonempty `what`")
        path = entry.get("path")
        if not relative_path(path, root=True):
            bad.append(f"{name}: `path` must be a relative directory (or . for the repository root)")
        elif isinstance(repo, str):
            key = (repo, path)
            if key in locations:
                bad.append(f"{name}: shares its primary directory with {locations[key]}")
            locations[key] = name
        for field in ("entrypoints", "docs", "also", "files"):
            optional = field in ("also", "files") or (field == "entrypoints" and entry.get("kind") == "artifact")
            values = entry.get(field, [] if optional else None)
            if not isinstance(values, list) or not all(relative_path(p) for p in values):
                bad.append(f"{name}: `{field}` must be a list of repository-relative paths")
            elif len(values) != len(set(values)):
                bad.append(f"{name}: duplicate `{field}` paths")
        if prefix:
            paths = [path, *(entry.get("also") if isinstance(entry.get("also"), list) else [])]
            for implementation in paths:
                if relative_path(implementation, root=True):
                    try:
                        within_owner(implementation, prefix)
                    except ValueError:
                        bad.append(f"{name}: implementation {implementation!r} is outside its owner at {prefix!r}")
        if "layout_note" in entry and (not isinstance(entry["layout_note"], str) or not entry["layout_note"].strip()):
            bad.append(f"{name}: `layout_note` must be nonempty text")
    for owner, paths in excluded.items():
        try:
            owner_location(owner, ecosystem)
        except ValueError as exc:
            bad.append(f"{owner}: invalid exclusion owner: {exc}")
        if not isinstance(paths, dict):
            bad.append(f"{owner}: exclusions must map top-level directories to reasons")
            continue
        for path, reason in paths.items():
            if not relative_path(path) or "/" in path or path.startswith(".") or path in SHARED:
                bad.append(f"{owner}: exclusion {path!r} must name a non-shared top-level directory")
            if not isinstance(reason, str) or not reason.strip():
                bad.append(f"{owner}/{path}: exclusion needs a reason")
    if not bad:
        for owner, paths in excluded.items():
            repo, prefix = owner_location(owner, ecosystem)
            covered = covered_directories(entries, repo, prefix)
            for path in paths.keys() & covered:
                bad.append(f"{owner}/{path}: both tooling and excluded")
    return bad


def top_directories(paths, prefix=""):
    """Immediate directory names beneath a project root, excluding the root."""
    result = set()
    for path in paths:
        try:
            relative = within_owner(path, prefix)
        except ValueError:
            continue
        if relative != ".":
            result.add(relative.split("/")[0])
    return result


def covered_directories(entries, repo, prefix=""):
    paths = [p for entry in entries.values() if entry["repo"] == repo
             for p in [entry["path"], *entry.get("also", [])]]
    return top_directories(paths, prefix)


class Tree:
    """A local working tree or one remote Git tree, never an installed tool."""

    def __init__(self, files, directories, source, root=None):
        self.files = set(files)
        self.directories = set(directories) | {"."}
        self.source = source
        self.root = root
        self.errors = set()

    def has(self, path, directory=False):
        if self.root is None:
            return path in (self.directories if directory else self.files)
        try:
            target = self.root / path
            # A symlink outside the checkout must not make a recorded path pass.
            if not target.resolve().is_relative_to(self.root):
                return False
            mode = target.stat().st_mode
            return stat.S_ISDIR(mode) if directory else stat.S_ISREG(mode)
        except (FileNotFoundError, NotADirectoryError):
            return False
        except (OSError, RuntimeError) as exc:
            self.errors.add(f"{path}: {exc}")
            return None


def local_tree(repo):
    location = status_audit.locate(repo["repo"])
    if not location:
        raise OSError("no checkout; set ANOIEU_REPOS or scripts/repos.local")
    root = Path(location).resolve()
    top = subprocess.run(["git", "-C", str(root), "rev-parse", "--show-toplevel"],
                         capture_output=True, text=True, check=True)
    if Path(top.stdout.strip()).resolve() != root:
        raise ValueError("resolved directory is not the repository root")
    result = subprocess.run(["git", "-C", str(root), "ls-files", "-z"],
                            capture_output=True, check=True)
    paths = result.stdout.decode("utf-8").split("\0")
    # Discovery uses tracked directories only: build outputs and local caches
    # are not prospective tools. Recorded paths are checked in the working tree.
    directories = {str(parent) for path in paths if path
                   for parent in PurePosixPath(path).parents if str(parent) != "."}
    tree = Tree(paths, directories, f"{root} @ {status_audit.git('rev-parse', '--short', 'HEAD', cwd=root) or '?'} (working tree)", root)
    tree.directories = {p for p in tree.directories if tree.has(p, directory=True)}
    return tree


def remote_tree(repo):
    """One default-branch tree per repository; no clone and no source execution."""
    match = re.fullmatch(r"https://github\.com/([^/]+)/([^/]+?)(?:\.git)?/?", repo["url"])
    if not match:
        raise ValueError("online inspection supports https://github.com/OWNER/REPO URLs")
    owner, name = (urllib.parse.quote(part, safe="") for part in match.groups())
    request = urllib.request.Request(
        f"https://api.github.com/repos/{owner}/{name}/git/trees/HEAD?recursive=1",
        headers={"Accept": "application/vnd.github+json", "User-Agent": "eo_tooling_audit"})
    with urllib.request.urlopen(request, timeout=20) as response:
        payload = json.load(response)
    if (not isinstance(payload, dict) or payload.get("truncated")
            or not isinstance(payload.get("tree"), list) or not payload.get("sha")):
        raise ValueError("remote tree is incomplete; coverage cannot be established")
    files, directories = set(), set()
    for item in payload["tree"]:
        if not isinstance(item, dict):
            raise ValueError("remote tree contains an invalid entry")
        path, kind = item.get("path"), item.get("type")
        if not relative_path(path) or kind not in ("blob", "tree", "commit"):
            raise ValueError("remote tree contains an invalid entry")
        if kind == "tree":
            directories.add(path)
        elif kind == "blob" and item.get("mode") != "120000":
            files.add(path)
    return Tree(files, directories, f"{repo['url']} @ tree {payload['sha']} (default branch)")


def layout(entry, prefix=""):
    path = within_owner(entry["path"], prefix)
    if entry.get("layout_note"):
        return "exception", entry["layout_note"]
    if entry.get("also"):
        return "split", "implementation spans multiple directories"
    if path == ".":
        return "root", "implementation spans its owner's root"
    if "/" in path:
        return "nested", "implementation is below a top-level directory"
    if path in SHARED:
        if entry.get("kind") == "artifact" and path == "docs":
            return "shared", ""
        return "shared", "implementation uses a shared layout directory"
    return "top-level", ""


def inspect(inventory, ecosystem, online=False):
    rows, gaps, unseen, notes = [], [], [], []
    trees = {}
    for name, repo in sorted(ecosystem.items()):
        if repo.get("status") not in REPOSITORIES:
            continue
        try:
            trees[name] = remote_tree(repo) if online else local_tree(repo)
        except (OSError, ValueError, RuntimeError, subprocess.SubprocessError) as exc:
            trees[name] = None
            unseen.append(f"{name}: {exc}")
    for name, entry in sorted(inventory["tools"].items()):
        tree = trees[entry["repo"]]
        problems = []
        owner = entry.get("owner", entry["repo"])
        _, prefix = owner_location(owner, ecosystem)
        form, explanation = layout(entry, prefix)
        if explanation:
            notes.append(f"{name}: layout gap: {explanation} ({entry['repo']}/{entry['path']})")
        kind = entry.get("kind", "tool")
        for field in ("docs", "files" if kind == "artifact" else "entrypoints"):
            if not entry.get(field):
                problems.append(f"no {field} recorded")
        if tree:
            for path in [entry["path"], *entry.get("also", [])]:
                if tree.has(path, directory=True) is False:
                    problems.append(f"missing implementation directory {path}")
            for field in ("entrypoints", "docs", "files"):
                for path in entry.get(field, []):
                    if tree.has(path) is False:
                        problems.append(f"missing {field} file {path}")
        gaps.extend(f"{name}: {problem}" for problem in problems)
        state = f"{len(problems)} gap(s)" if problems else (
            "present" if tree and not tree.errors else "unverified")
        rows.append((name, kind, owner, entry["repo"], state, form, entry["path"],
                     textwrap.shorten(entry["what"], width=60, placeholder="…")))
    # Repositories are always scanned. A child's layout becomes a discovery
    # scope when tooling or an explicit exclusion names it as an owner.
    owners = set(trees) | set(inventory.get("exclude", {})) | {
        entry.get("owner", entry["repo"]) for entry in inventory["tools"].values()}
    for owner in sorted(owners):
        repo, prefix = owner_location(owner, ecosystem)
        tree = trees[repo]
        excluded = inventory.get("exclude", {}).get(owner, {})
        for path, reason in sorted(excluded.items()):
            location = str(PurePosixPath(prefix) / path)
            present = tree.has(location, directory=True) if tree else None
            state = "unverified" if present is None else "present" if present else "missing"
            rows.append((f"{owner}/{path}", "excluded", owner, repo, state,
                         "non-compliant", location,
                         textwrap.shorten(reason, width=60, placeholder="…")))
            gaps.append(f"{owner}/{path}: intentionally excluded; non-compliant inventory coverage: {reason}")
            if present is False:
                gaps.append(f"{owner}/{path}: stale exclusion; directory is missing")
        if tree is None:
            continue
        candidates = {p for p in top_directories(tree.directories, prefix) if not p.startswith(".")}
        unknown = candidates - SHARED - covered_directories(inventory["tools"], repo, prefix) - excluded.keys()
        gaps.extend(f"{owner}/{path}: unregistered directory; record tooling or an exclusion with a reason"
                    for path in sorted(unknown))
    for repo, tree in trees.items():
        if tree and tree.errors:
            unseen.append(f"{repo}: " + "; ".join(sorted(tree.errors)))
    return rows, gaps, unseen, notes, trees


def main(argv=None):
    parser = argparse.ArgumentParser(
        prog="eo_tooling_audit",
        description="Audit ecosystem tools and artifacts: locations, documentation and inventory coverage.",
        epilog="""The table reports availability from local working trees, not build quality or
installation. owner is the repository or child project responsible for a tool;
repo is its containing repository and path is relative to that repository.
kind distinguishes tools (programs or importable libraries) from artifacts such
as bug databases. Tool entrypoints may be command launchers or public library
modules; artifacts need recorded content files. Both need documentation.
All file paths remain repository-relative.
Document artifacts in their owner's docs/ use shared layout without a layout gap.
Layout gaps are advisory: top-level means a dedicated directory within the owner;
nested, root, shared, split and exception describe other arrangements. Missing files,
empty required metadata, unregistered tracked top-level directories and
stale exclusions are inventory gaps. Discovery scans repositories and child
owners named in the tooling inventory, skipping hidden and shared layout
directories within each. It cannot find every tool inside scripts/, tools/ or
an owner's root. Record those explicitly; child registration alone is not tooling.
Every explicit exclusion is listed with kind excluded, its reason and a
non-compliant layout marker. These are gaps in our inventory coverage, even
when deliberate; --check --local/--online returns 1 while they remain. A missing
checkout leaves presence unverified without hiding the recorded exclusion.
Foundations are included as tooling providers, without policy checks or new
obligations. Outsiders remain outside this audit; footings are never changed.

--check alone reads only the two inventories. --local reads checkouts resolved
by eo_status_audit (ANOIEU_REPOS_FILE, scripts/repos.local, ANOIEU_REPOS, siblings,
then home). --online reads GitHub default-branch trees, which may differ from
local work or a child's development branch. No tools or assistants are run.
Exit 0: table, valid inventory, or complete comparison; 1: invalid inventory or
observed inventory gaps; 2: bad options or incomplete verification. Observed
gaps take precedence over unavailable trees. Layout notes alone never fail.
""", formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--verbose", action="store_true", help="include source revisions, entry points, artifact files and documentation")
    parser.add_argument("--check", action="store_true", help="validate inventory; no checkouts needed unless requested")
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--local", action="store_true", help="with --check, also compare local trees")
    mode.add_argument("--online", action="store_true", help="with --check, also compare GitHub default branches")
    args = parser.parse_args(argv)
    if (args.local or args.online) and not args.check:
        parser.error("--local and --online require --check")
    try:
        inventory = read_json(INVENTORY)
        ecosystem = {k: v for k, v in read_json(status_audit.INVENTORY).items() if not k.startswith("_")}
        if any(not isinstance(e, dict) or not isinstance(e.get("repo"), str) or not isinstance(e.get("url"), str)
               for e in ecosystem.values() if not isinstance(e, dict) or e.get("status") in REPOSITORIES):
            raise ValueError("invalid ecosystem repository; run eo_status_audit --check")
        failures = well_formed(inventory, ecosystem)
    except (OSError, ValueError) as exc:
        failures = [str(exc)]
    if failures:
        for failure in failures:
            print(f"FAIL {failure}")
        return 1
    if args.check and not (args.local or args.online):
        print(f"-- tooling inventory: {len(inventory['tools'])} entries, 0 failure(s)")
        print("-- structure only; --local or --online compares recorded paths and coverage")
        return 0
    rows, gaps, unseen, notes, trees = inspect(inventory, ecosystem, args.online)
    headings = ("tooling", "kind", "owner", "repo", "availability", "layout", "path", "purpose")
    widths = [max(len(row[i]) for row in [headings, *rows]) + 2 for i in range(len(headings))]
    for row in [headings, *rows]:
        print("".join(value.ljust(width) for value, width in zip(row, widths)).rstrip())
    print("\n-- columns and limits: eo_tooling_audit --help")
    for label, messages in (("GAP", gaps), ("UNVERIFIED", unseen), ("NOTE", notes)):
        for message in messages:
            print(f"{label} {message}")
    if args.verbose:
        for name, tree in trees.items():
            if tree:
                print(f"source: {name}: {tree.source}")
        for name, entry in sorted(inventory["tools"].items()):
            content = (f"files: {', '.join(entry.get('files', [])) or '(none)'}"
                       if entry.get("kind") == "artifact" else
                       f"entrypoints: {', '.join(entry['entrypoints']) or '(none)'}")
            print(f"{name}: {content}; "
                  f"docs: {', '.join(entry['docs']) or '(none)'}")
    artifacts = sum(entry.get("kind") == "artifact" for entry in inventory["tools"].values())
    exclusions = sum(len(paths) for paths in inventory.get("exclude", {}).values())
    print(f"\n{len(inventory['tools']) - artifacts} tools, {artifacts} artifacts, "
          f"{exclusions} intentional exclusions; "
          f"{len(gaps)} inventory gap(s); {len(notes)} layout gap(s); "
          f"{sum(tree is not None and not tree.errors for tree in trees.values())} repositories inspected, "
          f"{len(unseen)} unverified.")
    return (1 if gaps else 2 if unseen else 0) if args.check else 0


if __name__ == "__main__":
    sys.exit(main())
