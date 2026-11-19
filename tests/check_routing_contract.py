#!/usr/bin/env python3
"""Check maintained routing owners and retired-skill reference closure."""

from __future__ import annotations

import argparse
import re
from pathlib import Path
from typing import Dict, Iterable, List, Set, Tuple

ROOT = Path(__file__).resolve().parents[1]
SKILLS_DIR = ROOT / "skills"
ROUTING_FILE = ROOT / "tests" / "routing-contract.md"
README_FILE = ROOT / "README.md"
EXPECTED_SKILLS = {
    "agent-workflow",
    "reliability-check",
    "memory-handoff",
    "markdown-memory",
    "skill-refactorer",
}
RETIRED_SKILL_SLUGS = {
    "browser-testing-with-devtools",
    "ci-cd-and-automation",
    "context-engineering",
    "debug-systematically",
    "decision-map",
    "design-codebase",
    "finish-branch",
    "frontend-ui-engineering",
    "idea-refine",
    "interview-me",
    "issue-workflow",
    "observability-and-instrumentation",
    "performance-optimization",
    "plan-work",
    "review-and-finish",
    "security-and-hardening",
    "shipping-and-launch",
    "test-strategy",
}
RETIRED_REFERENCE_ROOTS = (
    ROOT / "prompts",
    ROOT / "README.md",
    ROOT / "README.zh-CN.md",
    ROOT / "skills.sh.json",
    ROOT / "workflows",
    ROOT / "tests" / "routing-contract.md",
    ROOT / ".claude" / "commands" / "grow-skill.md",
)
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
}
REQUIRED_HEADINGS = (
    "## Source Of Truth",
    "## Maintained Skills",
    "## Default Safety And Evidence Boundaries",
    "## Expected Composition",
    "## Retired Branch-Workflow Case Disposition",
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


def retired_references(text: str) -> Set[str]:
    return {
        name
        for name in RETIRED_SKILL_SLUGS
        if re.search(rf"(?<![a-z0-9-]){re.escape(name)}(?![a-z0-9-])", text)
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


def maintained_reference_files() -> List[Path]:
    files: List[Path] = []
    for root in RETIRED_REFERENCE_ROOTS:
        if root.is_file():
            files.append(root)
        elif root.is_dir():
            files.extend(
                path
                for path in root.rglob("*")
                if path.is_file() and path.suffix.lower() in {".md", ".json", ".py", ".js"}
            )
    if SKILLS_DIR.is_dir():
        for name in EXPECTED_SKILLS:
            skill_root = SKILLS_DIR / name
            if skill_root.is_dir():
                files.extend(
                    path
                    for path in skill_root.rglob("*")
                    if path.is_file() and path.suffix.lower() in {".md", ".json", ".py", ".js"}
                )
    return sorted(set(files))


def run(verbose: bool = False) -> int:
    errors: List[str] = []
    infos: List[str] = []
    names = skill_names()
    if not names:
        errors.append("skills directory has no readable Skill folders")
    if names != EXPECTED_SKILLS:
        missing = sorted(EXPECTED_SKILLS - names)
        unexpected = sorted(names - EXPECTED_SKILLS)
        errors.append(
            "skills directory does not match the retained five-skill surface: "
            f"missing={missing}, unexpected={unexpected}"
        )
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

    for path in maintained_reference_files():
        try:
            text = path.read_text(encoding="utf-8")
        except (OSError, UnicodeError) as exc:
            errors.append(f"cannot inspect maintained reference {path.relative_to(ROOT)}: {exc}")
            continue
        for name in sorted(retired_references(text)):
            errors.append(f"retired skill reference remains in {path.relative_to(ROOT)}: {name}")

    descriptions = {
        name: parse_description(SKILLS_DIR / name / "SKILL.md")
        for name in sorted(names)
        if (SKILLS_DIR / name / "SKILL.md").is_file()
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
