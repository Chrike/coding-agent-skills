from __future__ import annotations

import json
import re
import sys
from typing import Any


def read_stdin_json() -> dict[str, Any]:
    try:
        raw = sys.stdin.read()
        data = json.loads(raw or "{}")
        return data if isinstance(data, dict) else {}
    except Exception:
        return {}


def json_output(data: dict[str, Any]) -> None:
    sys.stdout.write(json.dumps(data, ensure_ascii=False))


def has_harness_opt_out(prompt: str) -> bool:
    token = "[harness:off]"
    quote: str | None = None
    code_ticks = 0
    fence: tuple[str, int] | None = None
    index = 0

    while index < len(prompt):
        if index == 0 or prompt[index - 1] == "\n":
            line_end = prompt.find("\n", index)
            if line_end < 0:
                line_end = len(prompt)
            line = prompt[index:line_end]
            if fence is not None:
                marker, length = fence
                closing = re.match(rf" {{0,3}}{re.escape(marker)}{{{length},}}[ \t\r]*$", line)
                if closing:
                    fence = None
                index = line_end + (line_end < len(prompt))
                continue
            if quote is None and not code_ticks:
                opening = re.match(r" {0,3}(`{3,}|~{3,})", line)
                if opening:
                    run = opening.group(1)
                    fence = (run[0], len(run))
                    index = line_end + (line_end < len(prompt))
                    continue

        character = prompt[index]
        if code_ticks:
            if character == "`":
                end = index + 1
                while end < len(prompt) and prompt[end] == "`":
                    end += 1
                if end - index == code_ticks:
                    code_ticks = 0
                index = end
            else:
                index += 1
            continue

        if quote is not None:
            if character == "\\":
                index += 2
            else:
                if character == quote:
                    quote = None
                index += 1
            continue

        if character == "`":
            end = index + 1
            while end < len(prompt) and prompt[end] == "`":
                end += 1
            code_ticks = end - index
            index = end
            continue
        if character in {'"', "“", "‘"}:
            quote = {"“": "”", "‘": "’"}.get(character, character)
            index += 1
            continue
        if character == "'":
            previous = prompt[index - 1] if index else ""
            following = prompt[index + 1] if index + 1 < len(prompt) else ""
            if not previous.isalnum() and not following.isalnum():
                quote = character
                index += 1
                continue

        if prompt[index : index + len(token)].casefold() == token:
            previous = prompt[index - 1] if index else ""
            following_index = index + len(token)
            following = prompt[following_index] if following_index < len(prompt) else ""
            if not (previous.isalnum() or previous == "_") and not (following.isalnum() or following == "_"):
                return True
        index += 1
    return False
