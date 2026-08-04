#!/usr/bin/env python3
"""Deterministic maintenance checks for the current Skill suite."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from typing import Dict, Iterable, List, Tuple

ROOT = Path(__file__).resolve().parents[1]
SKILLS_DIR = ROOT / "skills"
CATALOG_FILE = ROOT / "skills.sh.json"
CONTRACT_FILES = (
    ROOT / "tests" / "routing-contract.md",
    ROOT / "tests" / "trigger-matrix.md",
    ROOT / "tests" / "non-trigger-cases.md",
)
FRONTMATTER = re.compile(r"\A---\s*\n(?P<body>.*?)\n---\s*(?:\n|\Z)", re.S)
LOCAL_LINK = re.compile(r"\[[^\]]*\]\(([^)]+)\)")
FENCE = re.compile(r"^(`{3,}|~{3,}).*?^\1\s*$", re.M | re.S)


def parse_frontmatter(text: str) -> Dict[str, str] | None:
    match = FRONTMATTER.match(text)
    if match is None:
        return None
    values: Dict[str, str] = {}
    for line in match.group("body").splitlines():
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        values[key.strip()] = value.strip().strip("'\"")
    return values


def prose(text: str) -> str:
    return FENCE.sub("", text)


def local_link_targets(path: Path, text: str) -> Iterable[Tuple[str, Path]]:
    for raw in LOCAL_LINK.findall(prose(text)):
        target = raw.strip().split("#", 1)[0].split("?", 1)[0]
        if not target or target.startswith(("http://", "https://", "mailto:", "<")):
            continue
        if target.startswith("/"):
            resolved = ROOT / target.lstrip("/")
        else:
            resolved = path.parent / target
        yield target, resolved.resolve()


def validate_skills() -> Tuple[List[str], List[str]]:
    errors: List[str] = []
    warnings: List[str] = []
    if not SKILLS_DIR.is_dir():
        return ["skills directory is missing"], warnings

    for directory in sorted(p for p in SKILLS_DIR.iterdir() if p.is_dir()):
        skill_file = directory / "SKILL.md"
        if not skill_file.is_file():
            errors.append(f"{directory.name}: missing SKILL.md")
            continue
        try:
            text = skill_file.read_text(encoding="utf-8")
        except OSError as exc:
            errors.append(f"{directory.name}: cannot read SKILL.md: {exc}")
            continue
        frontmatter = parse_frontmatter(text)
        if frontmatter is None:
            errors.append(f"{directory.name}: missing or malformed frontmatter")
            continue
        if frontmatter.get("name") != directory.name:
            errors.append(
                f"{directory.name}: frontmatter name does not match directory"
            )
        description = frontmatter.get("description", "")
        if not description:
            errors.append(f"{directory.name}: missing description")
        elif len(description) > 1024:
            errors.append(f"{directory.name}: description exceeds 1024 characters")
        for target, resolved in local_link_targets(skill_file, text):
            if not resolved.exists():
                errors.append(f"{directory.name}: broken local link {target}")

    return errors, warnings


def validate_catalog() -> Tuple[List[str], List[str]]:
    errors: List[str] = []
    warnings: List[str] = []
    try:
        data = json.loads(CATALOG_FILE.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        return [f"skills.sh.json: cannot parse catalog: {exc}"], warnings

    groups = data.get("groupings")
    if not isinstance(groups, list):
        return ["skills.sh.json: groupings must be an array"], warnings

    known = {p.name for p in SKILLS_DIR.iterdir() if p.is_dir()}
    listed: List[str] = []
    for index, group in enumerate(groups):
        if not isinstance(group, dict) or not isinstance(group.get("skills"), list):
            errors.append(f"skills.sh.json: grouping {index} has no skills array")
            continue
        listed.extend(item for item in group["skills"] if isinstance(item, str))

    duplicates = sorted({name for name in listed if listed.count(name) > 1})
    errors.extend(f"skills.sh.json: duplicate skill {name}" for name in duplicates)
    errors.extend(
        f"skills.sh.json: unknown skill {name}"
        for name in sorted(set(listed) - known)
    )
    for name in sorted(known - set(listed)):
        warnings.append(f"skills.sh.json: skill {name} is not in a presentation grouping")

    return errors, warnings


def validate_contracts() -> Tuple[List[str], List[str]]:
    missing = [str(path.relative_to(ROOT)) for path in CONTRACT_FILES if not path.is_file()]
    return ([f"missing maintenance contract {path}" for path in missing], [])


def run(strict: bool = False) -> int:
    errors: List[str] = []
    warnings: List[str] = []
    for check in (validate_skills, validate_catalog, validate_contracts):
        check_errors, check_warnings = check()
        errors.extend(check_errors)
        warnings.extend(check_warnings)

    effective_errors = errors + (warnings if strict else [])
    for message in errors:
        print(f"ERROR: {message}")
    for message in warnings:
        print(f"WARN: {message}")
    status = "PASSED" if not effective_errors else "FAILED"
    print(f"{status}: {len(effective_errors)} error(s), {len(warnings)} warning(s)")
    return 1 if effective_errors else 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--strict", action="store_true", help="treat catalog omissions as errors")
    args = parser.parse_args()
    return run(strict=args.strict)


if __name__ == "__main__":
    raise SystemExit(main())
