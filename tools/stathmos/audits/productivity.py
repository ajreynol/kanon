"""Evidence for productive entities under LAW 11, without judging its quality.

Reuse the tooling audit's local inspection rather than treating an inventory
entry as proof that a deliverable exists. Central references and current role
assignments come from the president's documents, not a second register.
"""

from pathlib import Path
import posixpath
import re
from typing import NamedTuple
from urllib.parse import unquote, urlsplit

from tools.stathmos.audits import tooling_audit


ROOT = Path(__file__).resolve().parents[3]
ENTITIES = frozenset({"president", "member", "child"})
CENTRAL_DOCUMENTS = ("docs/laws.md", "docs/policy.md", "docs/vision.md")


class Result(NamedTuple):
    value: str
    reasons: list[str]


def prose_lines(text):
    """Numbered prose, excluding comments, code examples and block quotes."""
    text = re.sub(r"<!--.*?(?:-->|\Z)",
                  lambda match: "\n" * match[0].count("\n"), text, flags=re.S)
    fence = ""
    for number, line in enumerate(text.splitlines(), 1):
        if fence:
            if re.fullmatch(r" {0,3}" + re.escape(fence[0]) +
                            "{" + str(len(fence)) + r",}\s*", line):
                fence = ""
            continue
        opening = re.match(r"^ {0,3}(`{3,}|~{3,})", line)
        if opening:
            fence = opening[1]
        elif not re.match(r"^(?: {4}|\t| {0,3}>)", line):
            yield number, line


def linked_entity(target, ecosystem):
    """Identify the project a link names, rather than a homonymous language.

    Links into a recorded child identify that child, not its containing repo.
    Local links in these central documents are relative to the president's docs/.
    """
    url = urlsplit(target.strip("<>"))
    if not url.scheme and not url.netloc:
        path = posixpath.normpath("docs/" + unquote(url.path))
        if path.startswith("../") or path.startswith("/"):
            return None
        repo = next((name for name, entry in ecosystem.items()
                     if entry.get("status") == "president"), None)
    else:
        address = url._replace(query="", fragment="").geturl().rstrip("/")
        repo, path = None, ""
        for name, entry in ecosystem.items():
            base = entry.get("url", "").rstrip("/")
            if not base:
                continue
            if address == base:
                repo = name
                break
            if address.startswith(base + "/"):
                # GitHub links to a file or directory on a named revision.
                match = re.fullmatch(r"(?:blob|tree)/[^/]+/(.*)", address[len(base) + 1:])
                if match:
                    repo, path = name, unquote(match[1]).rstrip("/")
                    break
    if repo is None:
        return None
    for name, entry in ecosystem.items():
        prefix = entry.get("path", "").rstrip("/")
        if (entry.get("status") == "child" and entry.get("parent") == repo and prefix
                and (path == prefix or path.startswith(prefix + "/"))):
            return name
    return repo


def central_references(lines, ecosystem):
    definitions = {}
    for _, line in lines:
        definition = re.match(r"^ {0,3}\[([^\]]+)\]:\s*(\S+)", line)
        if definition:
            definitions[definition[1].casefold()] = definition[2]
    for number, line in lines:
        if re.match(r"^ {0,3}(?:#{1,6}\s|\[[^\]]+\]:)", line):
            continue
        targets = re.findall(r"\]\(([^\s)]+)(?:\s+[^)]*)?\)", line)
        for label, reference in re.findall(r"\[([^\]]+)\](?:\[([^\]]*)\])?", line):
            target = definitions.get((reference or label).casefold())
            if target:
                targets.append(target)
        for target in targets:
            name = linked_entity(target, ecosystem)
            if name:
                yield name, number


def assess(ecosystem):
    """Map entity IDs to yes/no/?; other footings are outside this requirement.

    A project link in a central document is observable; whether its surrounding
    text explains the purpose adequately remains a person's review. A missing
    observation produces '?' only when no other alternative establishes 'yes'.
    """
    entities = {name: entry for name, entry in ecosystem.items()
                if entry.get("status") in ENTITIES}
    evidence = {name: [] for name in entities}
    uncertain = {name: [] for name in entities}
    missing = {name: [] for name in entities}
    if not entities:
        return {}

    for name, entry in entities.items():
        if entry["status"] == "president":
            evidence[name].append("ecosystem.json: assigned presidency")

    for relative in (*CENTRAL_DOCUMENTS, "docs/roles.md"):
        try:
            lines = list(prose_lines((ROOT / relative).read_text(encoding="utf-8")))
        except (OSError, UnicodeError) as exc:
            for reasons in uncertain.values():
                reasons.append(f"{relative}: unverified: {exc}")
            continue
        if relative in CENTRAL_DOCUMENTS:
            found = set()
            for name, number in central_references(lines, ecosystem):
                if name in entities and name not in found:
                    evidence[name].append(f"{relative}:{number}: reference to {name}")
                    found.add(name)
        else:
            role = ""
            for number, line in lines:
                if re.match(r"^#{1,6}\s", line):
                    heading = re.match(r"^### (R\d+)\s+[—–-]\s+(.+)", line)
                    role = heading[1] if heading else ""
                holders = re.match(r"^\*\*Held by:\*\*\s*(.+)", line)
                if role and holders:
                    for holder in re.findall(r"`([^`]+)`", holders[1]):
                        if holder in entities:
                            evidence[holder].append(f"{relative}:{number}: holds {role}")

    try:
        inventory = tooling_audit.read_json(tooling_audit.INVENTORY)
        failures = tooling_audit.well_formed(inventory, ecosystem)
        if failures:
            raise ValueError("; ".join(failures))
    except (OSError, ValueError) as exc:
        for reasons in uncertain.values():
            reasons.append(f"tooling inventory unverified: {exc}")
    else:
        rows, gaps, unseen, _, _ = tooling_audit.inspect(inventory, ecosystem)
        for tool, kind, owner, repo, available, _, _, _ in rows:
            if owner not in entities or kind not in tooling_audit.KINDS:
                continue
            if available == "present":
                evidence[owner].append(f"eo_tooling_audit: {tool} ({kind}) present")
            elif available == "unverified":
                detail = "; ".join(note for note in unseen if note.startswith(f"{repo}:"))
                uncertain[owner].append(f"eo_tooling_audit: {tool} unverified" +
                                        (f"; {detail}" if detail else ""))
            else:
                missing[owner].extend(f"eo_tooling_audit: {gap}" for gap in gaps
                                      if gap.startswith(f"{tool}:"))

    return {name: Result("yes", reasons) if reasons else
            Result("?", uncertain[name] + missing[name]) if uncertain[name] else
            Result("no", missing[name] or ["no deliverable, central reference or assigned role found"])
            for name, reasons in evidence.items()}
