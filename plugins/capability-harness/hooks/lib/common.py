#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import os
import re
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any, Iterable


SCHEMA_VERSION = 1
STATE_ROOT = Path(".claude") / "capability-harness" / "state"

CURRENT_PATTERNS = [
    r"\b(latest|current|today|now|version|release|price|pricing|context window|model limit|api behavior|compatib)\b",
    r"(最新|当前|现在|今天|版本|发布|价格|上下文|模型参数|兼容|官方文档)",
]
IMPLEMENT_PATTERNS = [
    r"\b(implement|build|create|modify|change|fix|debug|refactor|migrate|write code|patch|deploy)\b",
    r"(实现|构建|创建|生成|绘制|制作|产出|渲染|修改|改动|修复|调试|重构|迁移|写代码|部署)",
]
QUALITY_PATTERNS = [
    r"\b(best|better|quality|design|architecture|recommend|compare|optimi[sz]e|strategy|review|improve|trade-?off)\b",
    r"(最好|更好|质量|设计|架构|推荐|比较|优化|策略|审查|改进|取舍)",
]
ARTIFACT_PATTERNS = [
    r"\b(svg|vector|illustration|image|visual|render|ui|ux|icon|poster|animation|artifact|mockup)\b",
    r"(插画|图像|图片|视觉|界面|图标|海报|动画|图形|渲染|截图|设计稿|原型)",
]
EXTERNAL_GUIDANCE_PATTERNS = [
    r"\b(recommend|best|architecture|design|strategy|optimi[sz]e|compare|standard|guidance|reference|benchmark|inspiration)\b",
    r"(推荐|最好|架构|设计|策略|优化|比较|规范|标准|指导|参考|基准|灵感|调研|搜索)",
]
PROJECT_PATTERNS = [
    r"\b(repo|repository|project|codebase|file|module|package|configuration|config|test suite)\b",
    r"(项目|仓库|代码库|文件|模块|配置|测试)",
]
HIGH_CONSEQUENCE_PATTERNS = [
    r"\b(security|vulnerability|legal|medical|financial|production|data loss|privacy|compliance)\b",
    r"(安全|漏洞|法律|医疗|金融|生产环境|数据丢失|隐私|合规)",
]
TRIVIAL_PATTERNS = [
    r"^(hi|hello|thanks|thank you|ok|okay|yes|no)[.! ]*$",
    r"^(你好|谢谢|好的|可以|是|否)[。！! ]*$",
]
FIXED_SCOPE_PATTERNS = [
    r"\b(fixed dimensions?|fixed color|exactly|no (?:visual )?(?:exploration|innovation|reference|search))\b",
    r"(固定尺寸|固定颜色|精确生成|仅生成|只需|无需参考|不需要参考|不需要搜索|不需要视觉创新|不要视觉创新)",
]


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


def read_stdin_json() -> dict[str, Any]:
    try:
        raw = sys.stdin.read()
        data = json.loads(raw or "{}")
        return data if isinstance(data, dict) else {}
    except Exception:
        return {}


def json_output(data: dict[str, Any]) -> None:
    sys.stdout.write(json.dumps(data, ensure_ascii=False))


def project_path(value: Any) -> Path:
    candidate = Path(str(value or Path.cwd())).expanduser()
    try:
        return candidate.resolve()
    except OSError:
        return candidate.absolute()


def state_dir(cwd: Any) -> Path:
    return project_path(cwd) / STATE_ROOT


def safe_session_id(value: Any) -> str:
    text = str(value or "unknown")
    return re.sub(r"[^A-Za-z0-9_.-]", "_", text)[:160] or "unknown"


def state_path(session_id: Any, cwd: Any) -> Path:
    return state_dir(cwd) / f"{safe_session_id(session_id)}.json"


def atomic_write_json(path: Path, data: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    os.replace(tmp, path)


def load_state(session_id: Any, cwd: Any) -> dict[str, Any]:
    path = state_path(session_id, cwd)
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
        return data if isinstance(data, dict) else {}
    except (OSError, json.JSONDecodeError):
        return {}


def save_state(session_id: Any, cwd: Any, data: dict[str, Any]) -> None:
    data["updated_at"] = utc_now()
    atomic_write_json(state_path(session_id, cwd), data)


def prune_state(cwd: Any, days: int = 7) -> None:
    cutoff = datetime.now(timezone.utc) - timedelta(days=days)
    try:
        paths = state_dir(cwd).glob("*.json")
    except OSError:
        return
    for path in paths:
        try:
            modified = datetime.fromtimestamp(path.stat().st_mtime, timezone.utc)
            if modified < cutoff:
                path.unlink(missing_ok=True)
        except OSError:
            pass


def any_match(text: str, patterns: Iterable[str]) -> bool:
    return any(re.search(pattern, text, flags=re.IGNORECASE) for pattern in patterns)


def classify_prompt(prompt: str) -> dict[str, bool]:
    stripped = prompt.strip()
    trivial = len(stripped) <= 24 and any_match(stripped, TRIVIAL_PATTERNS)
    current = any_match(stripped, CURRENT_PATTERNS)
    implementation = any_match(stripped, IMPLEMENT_PATTERNS)
    artifact = any_match(stripped, ARTIFACT_PATTERNS)
    quality = any_match(stripped, QUALITY_PATTERNS) or artifact
    external_guidance = any_match(stripped, EXTERNAL_GUIDANCE_PATTERNS)
    fully_specified = any_match(stripped, FIXED_SCOPE_PATTERNS)
    # Do not gate context enrichment on explicit search words: implicit quality gaps are the primary use case.
    context_enrichment = bool(
        not trivial
        and not fully_specified
        and (
            (artifact and quality)
            or (quality and external_guidance)
        )
    )
    project = any_match(stripped, PROJECT_PATTERNS) or (implementation and not artifact)
    high_consequence = any_match(stripped, HIGH_CONSEQUENCE_PATTERNS)
    substantive = not trivial and (
        len(stripped) >= 100
        or current
        or implementation
        or artifact
        or quality
        or project
        or high_consequence
        or "\n" in stripped
    )
    return {
        "substantive": substantive,
        "current_or_version_specific": current,
        "implementation": implementation,
        "visual_or_artifact": artifact,
        "quality_sensitive": quality,
        "external_guidance": external_guidance,
        "fully_specified": fully_specified,
        "context_enrichment": context_enrichment,
        "project_dependent": project,
        "high_consequence": high_consequence,
    }


def derive_requirements(classification: dict[str, bool]) -> dict[str, bool]:
    return {
        "external_or_project_evidence": bool(
            classification.get("current_or_version_specific")
            or classification.get("quality_sensitive")
            or classification.get("external_guidance")
            or classification.get("context_enrichment")
            or classification.get("high_consequence")
            or classification.get("project_dependent")
        ),
        "project_inspection": bool(classification.get("project_dependent")),
        "observable_check": bool(
            classification.get("implementation") or classification.get("visual_or_artifact")
        ),
        "independent_branch_or_evaluation": bool(
            classification.get("quality_sensitive")
            and not classification.get("current_or_version_specific")
            and not classification.get("fully_specified")
        ),
        "context_enrichment": bool(classification.get("context_enrichment")),
        "focused_web_guidance": bool(
            classification.get("current_or_version_specific")
            or (
                classification.get("quality_sensitive")
                and classification.get("external_guidance")
            )
            or classification.get("context_enrichment")
            or classification.get("high_consequence")
        ),
    }


def hash_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8", errors="replace")).hexdigest()


def transcript_offset(path_text: Any) -> int:
    try:
        return Path(str(path_text)).expanduser().stat().st_size
    except OSError:
        return 0


def read_transcript_delta(path_text: Any, offset: int, max_bytes: int = 2_000_000) -> str:
    try:
        path = Path(str(path_text)).expanduser()
        size = path.stat().st_size
        start = min(max(0, int(offset)), size)
        if size - start > max_bytes:
            start = size - max_bytes
        with path.open("rb") as stream:
            stream.seek(start)
            return stream.read(max_bytes).decode("utf-8", errors="replace")
    except (OSError, ValueError):
        return ""


def extract_tool_names(raw_jsonl: str) -> set[str]:
    names: set[str] = set()
    for line in raw_jsonl.splitlines():
        try:
            obj = json.loads(line)
        except json.JSONDecodeError:
            continue
        stack: list[Any] = [obj]
        while stack:
            item = stack.pop()
            if isinstance(item, dict):
                if item.get("type") in {"tool_use", "tool_call"} and isinstance(item.get("name"), str):
                    names.add(item["name"])
                for key, value in item.items():
                    if key in {"subagent_type", "agent_type"} and isinstance(value, str):
                        names.add(value)
                    if key in {"tool_name", "name"} and isinstance(value, str):
                        if any(token in value.lower() for token in ["web", "search", "fetch", "read", "grep", "glob", "bash", "agent", "task", "browser", "playwright"]):
                            names.add(value)
                    if isinstance(value, (dict, list)):
                        stack.append(value)
            elif isinstance(item, list):
                stack.extend(item)
    return names


def normalized_tool_tokens(names: set[str]) -> set[str]:
    tokens: set[str] = set()
    for name in names:
        low = name.lower()
        if "context-scout" in low or "context_scout" in low:
            tokens.add("context")
        if "skeptical-evaluator" in low or "skeptical_evaluator" in low:
            tokens.add("evaluate")
        if "independent-brancher" in low or "independent_brancher" in low:
            tokens.add("branch")
        if "evidence-researcher" in low or "evidence_researcher" in low:
            tokens.add("evidence")
        if "websearch" in low or "web_search" in low or low.endswith("search") or "search_query" in low:
            tokens.add("web")
        if "webfetch" in low or "fetch" in low or "browser" in low:
            tokens.add("web")
        if low in {"read", "grep", "glob"} or any(x in low for x in ["read_file", "grep", "glob"]):
            tokens.add("inspect")
        if low in {"bash", "shell"} or any(x in low for x in ["bash", "terminal", "execute", "run_command"]):
            tokens.add("execute")
        if any(x in low for x in ["playwright", "browser", "render", "screenshot"]):
            tokens.add("execute")
        if low in {"agent", "task"} or any(x in low for x in ["subagent", "agent", "task"]):
            tokens.add("agent")
    return tokens


def route_report(message: str) -> dict[str, str]:
    report: dict[str, str] = {}
    keys = {"route": "route", "harness": "harness", "reason": "route_reason"}
    for raw_line in message.splitlines():
        line = raw_line.strip().lstrip("*#").strip()
        key, separator, value = line.partition(":")
        if not separator:
            continue
        normalized_key = key.strip().casefold()
        if normalized_key in keys and value.strip():
            report[keys[normalized_key]] = value.strip()[:500]
    return report
