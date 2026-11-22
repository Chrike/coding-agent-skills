#!/usr/bin/env python3
from __future__ import annotations

import re
import shlex
from pathlib import Path
import sys
LIB = Path(__file__).resolve().parent / "lib"
sys.path.insert(0, str(LIB))

from common import json_output, read_stdin_json  # noqa: E402  # type: ignore[reportMissingImports]

RESEARCH_AGENT = "capability-harness:research-scout"
HANDOFF_AGENTS = {
    "capability-harness:research-scout",
    "capability-harness:execution-verifier",
    "capability-harness:skeptical-evaluator",
}
# Allow only plain tokens: expansions, escapes, quotes, and shell control syntax are rejected.
SHELL_SYNTAX = re.compile(r"[;&|<>`$\\{}\[\]*?!~()\n\r\"']")
API_SCHEME = re.compile(r"^[a-z][a-z0-9+.-]*:")
HEADING = re.compile(r"^#{2,3}\s+(.+?)\s*#*\s*$")
FENCE = re.compile(r"^\s*(`{3,}|~{3,})")
GIT_BLOCKED_FLAGS = {"-c", "--config", "--output", "-o", "--upload-pack", "--receive-pack", "--ext-diff", "--textconv", "--no-index"}


def executable_name(value: str) -> str:
    normalized = value.casefold()
    return normalized.removesuffix(".exe") if normalized in {"gh", "gh.exe", "git", "git.exe"} else ""


def command_tokens(command: object) -> list[str]:
    if not isinstance(command, str) or not command.strip() or SHELL_SYNTAX.search(command):
        return []
    try:
        return shlex.split(command, posix=False)
    except ValueError:
        return []


def has_write_flag(tokens: list[str], flags: set[str]) -> bool:
    for token in tokens:
        normalized = token.casefold().split("=", 1)[0]
        if normalized in flags or any(
            normalized.startswith(flag) for flag in ("-o", "-c") if flag in flags
        ) or any(flag.startswith(normalized) for flag in flags if flag.startswith("--")):
            return True
    return False


def is_read_only_gh(tokens: list[str]) -> bool:
    if len(tokens) < 2 or executable_name(tokens[0]) != "gh":
        return False
    group = tokens[1].casefold()
    if group == "api":
        path_seen = False
        index = 2
        while index < len(tokens):
            token = tokens[index].casefold()
            if token in {"-x", "--method"}:
                if path_seen or index + 1 >= len(tokens) or tokens[index + 1].casefold() != "get":
                    return False
                index += 2
                continue
            if token.startswith("--method="):
                if path_seen or token.split("=", 1)[1] != "get":
                    return False
            elif token.startswith("-") or path_seen or token.startswith("//") or API_SCHEME.match(token):
                return False
            else:
                path_seen = True
            index += 1
        return path_seen
    if len(tokens) < 3:
        return False
    action = tokens[2].casefold()
    if group not in {"issue", "pr", "release", "repo"} or action not in {"view", "list", "diff"}:
        return False
    return not any(
        token.casefold().split("=", 1)[0] in {"--web", "-w", "--open", "--edit", "--delete"}
        or token.casefold().startswith(("--jq", "-q", "--template", "-t"))
        or (token.startswith("-") and not token.startswith("--") and len(token) > 2)
        for token in tokens[3:]
    )


def is_read_only_git(tokens: list[str]) -> bool:
    if len(tokens) < 2 or executable_name(tokens[0]) != "git":
        return False
    action_index = 1
    guarded_options: set[str] = set()
    while action_index < len(tokens) and tokens[action_index].startswith("-"):
        option = tokens[action_index].casefold()
        if option == "-c" and action_index + 1 < len(tokens) and tokens[action_index + 1].casefold() == "core.fsmonitor=false":
            guarded_options.add("fsmonitor")
            action_index += 2
        elif option in {"--no-optional-locks", "--no-pager"}:
            guarded_options.add(option)
            action_index += 1
        else:
            return False
    if not {"fsmonitor", "--no-optional-locks", "--no-pager"}.issubset(guarded_options):
        return False
    if action_index >= len(tokens) or tokens[action_index].casefold() not in {"log", "status", "diff", "show"}:
        return False

    action = tokens[action_index].casefold()
    arguments = tokens[action_index + 1 :]
    # Git implicitly treats external path pairs as no-index; `--` disambiguates dash-leading paths.
    if action == "diff" and ("--" in arguments or sum(not token.startswith("-") for token in arguments) > 1):
        return False
    if action in {"log", "diff", "show"} and not {"--no-ext-diff", "--no-textconv"}.issubset(
        {token.casefold() for token in arguments}
    ):
        return False
    return not has_write_flag(arguments, GIT_BLOCKED_FLAGS)


def is_read_only_command(command: object) -> bool:
    tokens = command_tokens(command)
    return is_read_only_gh(tokens) or is_read_only_git(tokens)


def has_report_sections(message: object) -> bool:
    if not isinstance(message, str) or not message.strip():
        return False

    sections: list[list[str]] = []
    current: list[str] | None = None
    fence_char = ""
    fence_length = 0
    for line in message.splitlines():
        fence = FENCE.match(line)
        if fence_char:
            if fence and fence.group(1)[0] == fence_char and len(fence.group(1)) >= fence_length:
                fence_char = ""
                fence_length = 0
            continue
        if fence:
            fence_char = fence.group(1)[0]
            fence_length = len(fence.group(1))
            continue

        heading = HEADING.match(line)
        if heading:
            if current is not None and "\n".join(current).strip():
                sections.append(current)
            title = re.sub(r"[*_`]", "", heading.group(1)).rstrip(":：").strip()
            current = [] if title else None
        elif current is not None:
            current.append(line)

    if current is not None and "\n".join(current).strip():
        sections.append(current)
    substantive = [
        body for body in sections
        if len(re.sub(r"\s", "", "\n".join(body))) >= 12
    ]
    return len(substantive) >= 2


def deny(reason: str) -> None:
    json_output(
        {
            "hookSpecificOutput": {
                "hookEventName": "PreToolUse",
                "permissionDecision": "deny",
                "permissionDecisionReason": reason,
            }
        }
    )


def main() -> int:
    event = read_stdin_json()
    if not event:
        deny("Unable to parse the matched PreToolUse event; blocking because the policy input is unavailable.")
        return 0

    tool_name = event.get("tool_name")
    agent_type = event.get("agent_type")
    tool_input = event.get("tool_input")

    if tool_name == "Bash" and agent_type == RESEARCH_AGENT:
        command = tool_input.get("command") if isinstance(tool_input, dict) else None
        if is_read_only_command(command):
            return 0
        deny("research-scout may run only read-only gh or git commands; gh output filters are blocked to prevent process-environment disclosure.")
    elif tool_name == "SubagentHandback" and isinstance(agent_type, str) and agent_type in HANDOFF_AGENTS:
        message = tool_input.get("message") if isinstance(tool_input, dict) else None
        if has_report_sections(message):
            return 0
        deny("请在交接报告中提供至少两个有正文的 H2/H3 结构区块，再提交 SubagentHandback。")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
