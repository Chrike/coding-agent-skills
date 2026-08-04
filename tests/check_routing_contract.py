#!/usr/bin/env python3
"""Check current routing-contract ownership without ranking or runtime execution."""

from __future__ import annotations

import argparse
import re
from pathlib import Path
from typing import Dict, Iterable, List, Set, Tuple

ROOT = Path(__file__).resolve().parents[1]
SKILLS_DIR = ROOT / "skills"
ROUTING_FILE = ROOT / "tests" / "routing-contract.md"
README_FILE = ROOT / "README.md"
BACKTICK = re.compile(r"`([^`]+)`")
SLUG = re.compile(r"[a-z][a-z0-9]*(?:-[a-z0-9]+)+\Z")
WORD = re.compile(r"[a-z][a-z0-9-]{2,}")
STOPWORDS = {
    "active",
    "already",
    "and",
    "are",
    "asks",
    "also",
    "before",
    "build",
    "concrete",
    "design",
    "evidence",
    "explicit",
    "explicitly",
    "for",
    "from",
    "has",
    "implementation",
    "identified",
    "its",
    "may",
    "not",
    "only",
    "ordinary",
    "owner",
    "performance",
    "request",
    "requests",
    "review",
    "runtime",
    "the",
    "this",
    "use",
    "user",
    "when",
    "with",
    "work",
}
NON_SKILL_SLUGS = {
    "adaptive-long-horizon",
    "code-review",
    "code-simplify",
    "deprecation-and-migration",
    "finish-branch",
    "needs-review",
    "spec-authoring",
}
REQUIRED_HEADINGS = (
    "## Source Of Truth",
    "## Core Routing",
    "## Expected Composition",
    "## Test-Strategy Cross-Cutting Boundaries",
    "## Maintenance Use",
)


def skill_names() -> Set[str]:
    if not SKILLS_DIR.is_dir():
        return set()
    return {
        path.name
        for path in SKILLS_DIR.iterdir()
        if path.is_dir() and (path / "SKILL.md").is_file()
    }


def parse_description(path: Path) -> str:
    text = path.read_text(encoding="utf-8")
    marker = re.match(r"\A---\s*\n(.*?)\n---\s*(?:\n|\Z)", text, re.S)
    if marker is None:
        return ""
    for line in marker.group(1).splitlines():
        if line.startswith("description:"):
            return line.split(":", 1)[1].strip().strip("'\"")
    return ""


def referenced_owners(text: str, names: Iterable[str]) -> Set[str]:
    return {
        name
        for name in names
        if re.search(rf"(?<![a-z0-9-]){re.escape(name)}(?![a-z0-9-])", text)
    }


def unresolved_slug_tokens(text: str, names: Set[str]) -> Set[str]:
    tokens = set(BACKTICK.findall(text))
    return {
        token
        for token in tokens
        if SLUG.fullmatch(token)
        and token not in names
        and token not in NON_SKILL_SLUGS
    }


def lexical_words(text: str) -> Set[str]:
    return {word for word in WORD.findall(text.lower()) if word not in STOPWORDS}


def lexical_overlaps(descriptions: Dict[str, str]) -> List[Tuple[str, str, List[str]]]:
    names = sorted(descriptions)
    overlaps: List[Tuple[str, str, List[str]]] = []
    words = {name: lexical_words(text) for name, text in descriptions.items()}
    for index, left in enumerate(names):
        for right in names[index + 1 :]:
            shared = sorted(words[left] & words[right])
            if len(shared) >= 3:
                overlaps.append((left, right, shared))
    return overlaps


def run(verbose: bool = False) -> int:
    errors: List[str] = []
    infos: List[str] = []
    names = skill_names()
    if not names:
        errors.append("skills directory has no readable Skill folders")
    if not ROUTING_FILE.is_file():
        errors.append("tests/routing-contract.md is missing")
        print("\n".join(f"ERROR: {message}" for message in errors))
        print(f"FAILED: {len(errors)} error(s)")
        return 1

    routing = ROUTING_FILE.read_text(encoding="utf-8")
    for heading in REQUIRED_HEADINGS:
        if heading not in routing:
            errors.append(f"routing contract is missing {heading}")

    missing_from_routing = sorted(names - referenced_owners(routing, names))
    errors.extend(f"routing contract does not mention owner {name}" for name in missing_from_routing)
    missing_from_readme = sorted(names - referenced_owners(README_FILE.read_text(encoding="utf-8"), names))
    errors.extend(f"README does not mention installed owner {name}" for name in missing_from_readme)

    unknown = sorted(unresolved_slug_tokens(routing, names))
    errors.extend(f"routing contract references unresolved owner-like token {token}" for token in unknown)

    descriptions = {
        name: parse_description(SKILLS_DIR / name / "SKILL.md")
        for name in sorted(names)
    }
    for left, right, shared in lexical_overlaps(descriptions):
        infos.append(f"lexical overlap (informational): {left} / {right}: {', '.join(shared)}")

    for message in errors:
        print(f"ERROR: {message}")
    if verbose:
        for message in infos:
            print(f"INFO: {message}")
    print(f"{'PASSED' if not errors else 'FAILED'}: {len(errors)} error(s), {len(infos)} informational overlap(s)")
    return 1 if errors else 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--verbose", action="store_true", help="print informational lexical-overlap observations")
    args = parser.parse_args()
    return run(verbose=args.verbose)


if __name__ == "__main__":
    raise SystemExit(main())
