"""Keep simplify-ignore blocks out of bounded Read/Edit/Write hook flows."""

from __future__ import annotations

import hashlib
import json
import os
import shutil
import stat
import sys
import tempfile
from pathlib import Path
from typing import Dict, Iterable, Optional, Tuple

START = "simplify-ignore-start"
END = "simplify-ignore-end"
CACHE_RELATIVE = Path(".claude") / ".simplify-protected-blocks"
MAX_INPUT_BYTES = 1_000_000


Mapping = Dict[str, Dict[str, str]]


def project_root() -> Path:
    return Path(os.environ.get("CLAUDE_PROJECT_DIR") or Path.cwd()).resolve()


def within_root(root: Path, path: Path) -> bool:
    try:
        path.relative_to(root)
    except ValueError:
        return False
    return True


def safe_path(root: Path, raw_path: object, require_file: bool = True) -> Optional[Path]:
    if not isinstance(raw_path, str) or not raw_path:
        return None
    candidate = Path(raw_path)
    if not candidate.is_absolute():
        candidate = root / candidate
    if candidate.is_symlink():
        return None
    try:
        resolved = candidate.resolve(strict=False)
    except OSError:
        return None
    if not within_root(root, resolved) or resolved == root:
        return None
    if resolved == (root / CACHE_RELATIVE).resolve(strict=False):
        return None
    if require_file and (not resolved.exists() or not resolved.is_file()):
        return None
    if resolved.exists() and not resolved.is_file():
        return None
    return resolved


def cache_dir(root: Path) -> Optional[Path]:
    parent = root / ".claude"
    cache = root / CACHE_RELATIVE
    if parent.exists() and parent.is_symlink():
        return None
    if cache.exists() and cache.is_symlink():
        return None
    try:
        cache.mkdir(parents=True, exist_ok=True)
        resolved = cache.resolve(strict=True)
    except OSError:
        return None
    return resolved if within_root(root, resolved) else None


def state_paths(root: Path, path: Path) -> Optional[Dict[str, Path]]:
    cache = cache_dir(root)
    if cache is None:
        return None
    relative = path.relative_to(root).as_posix()
    identifier = hashlib.sha256(relative.encode("utf-8")).hexdigest()[:24]
    return {
        "backup": cache / f"{identifier}.bak",
        "mapping": cache / f"{identifier}.json",
        "path": cache / f"{identifier}.path",
        "lock": cache / f"{identifier}.lock",
    }


def read_text(path: Path) -> Optional[str]:
    try:
        with path.open("r", encoding="utf-8", newline="") as handle:
            return handle.read()
    except (OSError, UnicodeError):
        return None


def atomic_write(path: Path, content: str, mode_source: Optional[Path] = None) -> None:
    mode = None
    if mode_source is not None and mode_source.exists():
        mode = stat.S_IMODE(mode_source.stat().st_mode)
    fd, temporary = tempfile.mkstemp(prefix=f".{path.name}.", dir=str(path.parent), text=True)
    try:
        with os.fdopen(fd, "w", encoding="utf-8", newline="") as handle:
            handle.write(content)
        if mode is not None:
            os.chmod(temporary, mode)
        os.replace(temporary, path)
    finally:
        try:
            os.unlink(temporary)
        except FileNotFoundError:
            pass


def atomic_copy(source: Path, destination: Path, mode_source: Optional[Path] = None) -> None:
    mode = None
    if mode_source is not None and mode_source.exists():
        mode = stat.S_IMODE(mode_source.stat().st_mode)
    fd, temporary = tempfile.mkstemp(prefix=f".{destination.name}.", dir=str(destination.parent))
    os.close(fd)
    try:
        shutil.copyfile(source, temporary)
        if mode is not None:
            os.chmod(temporary, mode)
        os.replace(temporary, destination)
    finally:
        try:
            os.unlink(temporary)
        except FileNotFoundError:
            pass


def reason_for(line: str, start: int, end: int) -> str:
    raw = line[start + len(START) : end].strip()
    if raw.startswith(":"):
        raw = raw[1:].strip()
    return " ".join(raw.split())


def make_placeholder(first_line: str, start: int, end_line: str, end: int, token: str) -> str:
    reason = reason_for(first_line, start, len(first_line))
    suffix = f": {reason}" if reason else ""
    return first_line[:start] + token + suffix + end_line[end + len(END) :]


def filter_text(text: str) -> Tuple[str, Mapping, Iterable[str]]:
    lines = text.splitlines(keepends=True)
    output = []
    mapping: Mapping = {}
    warnings = []
    index = 0

    while index < len(lines):
        line = lines[index]
        start = line.find(START)
        if start < 0:
            output.append(line)
            index += 1
            continue

        end = line.find(END, start + len(START))
        end_index = index
        if end < 0:
            for candidate in range(index + 1, len(lines)):
                candidate_end = lines[candidate].find(END)
                if candidate_end >= 0:
                    end_index = candidate
                    end = candidate_end
                    break
            if end < 0:
                warnings.append(f"unclosed marker at line {index + 1}")
                output.extend(lines[index:])
                break

        block = "".join(lines[index : end_index + 1])
        token = "BLOCK_" + hashlib.sha256(f"{index}\0{block}".encode("utf-8")).hexdigest()[:8]
        placeholder = make_placeholder(lines[index], start, lines[end_index], end, token)
        mapping[token] = {"block": block, "placeholder": placeholder}
        output.append(placeholder)
        index = end_index + 1

    return "".join(output), mapping, warnings


def load_mapping(state: Dict[str, Path]) -> Optional[Mapping]:
    try:
        data = json.loads(state["mapping"].read_text(encoding="utf-8"))
    except (OSError, UnicodeError, json.JSONDecodeError):
        return None
    if not isinstance(data, dict):
        return None
    return data


def parse_payload() -> dict:
    try:
        raw = sys.stdin.read(MAX_INPUT_BYTES)
        value = json.loads(raw or "{}")
    except (OSError, UnicodeError, json.JSONDecodeError):
        return {}
    return value if isinstance(value, dict) else {}


def file_path_from_payload(payload: dict) -> object:
    tool_input = payload.get("tool_input")
    if not isinstance(tool_input, dict):
        return None
    return tool_input.get("file_path") or tool_input.get("path")


def acquire(lock: Path) -> bool:
    try:
        lock.mkdir()
        return True
    except FileExistsError:
        return False
    except OSError:
        return False


def release(lock: Path) -> None:
    try:
        lock.rmdir()
    except OSError:
        pass


def remove_state(state: Dict[str, Path]) -> None:
    for key in ("backup", "mapping", "path"):
        try:
            state[key].unlink()
        except FileNotFoundError:
            pass
        except OSError:
            pass
    release(state["lock"])


def protect_file(root: Path, path: Path) -> None:
    state = state_paths(root, path)
    if state is None or state["backup"].exists():
        return
    text = read_text(path)
    if text is None:
        return
    filtered, mapping, warnings = filter_text(text)
    for warning in warnings:
        print(f"simplify-protected-blocks: {path.relative_to(root)}: {warning}", file=sys.stderr)
    if not mapping:
        return
    if not acquire(state["lock"]):
        return
    try:
        atomic_write(state["backup"], text)
        atomic_write(state["mapping"], json.dumps(mapping, ensure_ascii=False, indent=2) + "\n")
        atomic_write(state["path"], path.relative_to(root).as_posix() + "\n")
        atomic_write(path, filtered, path)
    except (OSError, UnicodeError, ValueError):
        remove_state(state)
    finally:
        release(state["lock"])


def expand_text(text: str, mapping: Mapping) -> Tuple[str, Iterable[str]]:
    warnings = []
    expanded = text
    for token, entry in mapping.items():
        if not isinstance(entry, dict) or not isinstance(entry.get("block"), str):
            warnings.append(f"invalid state for {token}")
            continue
        block = entry["block"]
        placeholder = entry.get("placeholder")
        if isinstance(placeholder, str) and placeholder in expanded:
            expanded = expanded.replace(placeholder, block, 1)
        elif token in expanded:
            expanded = expanded.replace(token, block, 1)
        else:
            warnings.append(f"placeholder {token} is missing")
    return expanded, warnings


def update_file(root: Path, path: Path) -> None:
    state = state_paths(root, path)
    if state is None or not state["backup"].exists():
        return
    mapping = load_mapping(state)
    if mapping is None or not acquire(state["lock"]):
        return
    try:
        current = read_text(path)
        if current is None:
            return
        expanded, warnings = expand_text(current, mapping)
        for warning in warnings:
            print(f"simplify-protected-blocks: {path.relative_to(root)}: {warning}", file=sys.stderr)
        filtered, new_mapping, filter_warnings = filter_text(expanded)
        for warning in filter_warnings:
            print(f"simplify-protected-blocks: {path.relative_to(root)}: {warning}", file=sys.stderr)
        if not new_mapping:
            atomic_write(path, expanded, path)
            remove_state(state)
            return
        atomic_write(path, filtered, path)
        atomic_write(state["backup"], expanded)
        atomic_write(state["mapping"], json.dumps(new_mapping, ensure_ascii=False, indent=2) + "\n")
    except (OSError, UnicodeError, ValueError):
        return
    finally:
        release(state["lock"])


def recovered_path(path: Path) -> Path:
    candidate = path.with_name(path.name + ".recovered")
    index = 1
    while candidate.exists():
        candidate = path.with_name(f"{path.name}.recovered.{index}")
        index += 1
    return candidate


def restore_all(root: Path) -> None:
    cache = cache_dir(root)
    if cache is None:
        return
    for path_file in cache.glob("*.path"):
        identifier = path_file.stem
        state = {
            "backup": cache / f"{identifier}.bak",
            "mapping": cache / f"{identifier}.json",
            "path": path_file,
            "lock": cache / f"{identifier}.lock",
        }
        try:
            relative = path_file.read_text(encoding="utf-8").strip()
        except (OSError, UnicodeError):
            continue
        destination = safe_path(root, relative, require_file=False)
        if destination is None or not state["backup"].is_file():
            continue
        try:
            if destination.exists():
                atomic_copy(state["backup"], destination, destination)
            else:
                destination.parent.mkdir(parents=True, exist_ok=True)
                recovered = recovered_path(destination)
                atomic_copy(state["backup"], recovered)
                print(
                    f"simplify-protected-blocks: restored moved file to {recovered.relative_to(root)}",
                    file=sys.stderr,
                )
            remove_state(state)
        except OSError:
            continue


def main(argv: list[str]) -> int:
    if len(argv) != 2 or argv[1] not in {"read", "write", "stop"}:
        return 0
    root = project_root()
    if argv[1] == "stop":
        restore_all(root)
        return 0
    payload = parse_payload()
    path = safe_path(root, file_path_from_payload(payload))
    if path is None:
        return 0
    if argv[1] == "read":
        protect_file(root, path)
    else:
        update_file(root, path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
