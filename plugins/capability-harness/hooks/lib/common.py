from __future__ import annotations

import json
import re
import sys
from typing import Any, Iterable


CURRENT_PATTERNS = [
    r"\b(?:latest|newest|current|today(?:'s)?|recent|currently|as of)\b(?:\s+\w+){0,4}\s+\b(?:version|release|price|pricing|api|behavior|documentation|docs?|model|context window|limit|compatib\w*)\b",
    r"\b(?:supported|installed)\s+(?:version|release|api|model)\b",
    r"\b(?:what|which)\s+(?:is\s+)?(?:the\s+)?current\s+(?:version|release)\b",
    r"\b(?:what|which)\s+(?:version|release)\s+is\s+(?:currently\s+)?(?:supported|installed|available)\b",
    r"\b(?:what|which)\s+(?:version|release)\s+(?:does|is)\s+(?:this|the|it)\b",
    r"\b(?:version|release)\s+(?:of|for|used by|supported by)\b",
    r"\b(?:api|model|product|library|package|tool|server)\s+version\b",
    r"\b(release notes?|price|pricing|context window|model limits?|api behavior|compatib\w*|official (?:docs?|documentation))\b",
    r"(?:最新|当前|目前|现在|截至|今天|最近|支持的|安装的)(?:.{0,12})(?:版本|发布|价格|定价|API|接口|行为|文档|模型参数|上下文窗口|兼容性)",
    r"(?:版本号|版本更新|发布说明|定价|价格|模型参数|上下文窗口|兼容性|官方(?:最新)?文档|(?:API|模型|软件|工具|库)(?:的)?版本)",
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
    r"\b(?:this|current|existing|our)\s+(?:repo(?:sitory)?|project|codebase|file|module|package|configuration|config|test suite)\b",
    r"\b(?:in|within|from|against)\s+(?:this|the current|our|existing)\s+(?:repo(?:sitory)?|project|codebase)\b",
    r"\b(?:repo(?:sitory)?|codebase)\s+(?:files?|history|configuration|conventions?|state)\b",
    r"\b(?:package\.json|pyproject\.toml|tsconfig\.json|cargo\.toml|go\.mod|pom\.xml)\b",
    r"(?:当前|本|这个|现有|已有)(?:项目|仓库|代码库|文件|模块|配置|测试(?:套件|集)?)",
    r"(?:项目|仓库|代码库)(?:中的|里的)(?:文件|模块|配置|测试|约定|历史|状态)",
]
NO_PROJECT_CONTEXT_PATTERNS = [
    r"\b(?:without|no) (?:a )?(?:repo(?:sitory)?|project|codebase) context\b",
    r"\bnot tied to (?:a )?(?:repo(?:sitory)?|project|codebase)\b",
    r"(无|没有|不涉及|不依赖)(?:当前)?(?:项目|仓库|代码库)(?:上下文|背景)?",
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
    r"\b(fixed dimensions?|fixed color|exactly|no (?:visual )?(?:exploration|innovation|reference))\b",
    r"(固定尺寸|固定颜色|精确生成|仅生成|只需|无需参考|不需要参考|不需要视觉创新|不要视觉创新)",
]
# These are explicit per-prompt source constraints, not a global search policy.
NO_EXTERNAL_DISCOVERY_PATTERNS = [
    r"\b(do not (?:use )?search|don't (?:use )?search|do not browse(?: the web)?|don't browse(?: the web)?|without browsing(?: the web)?|no web|no internet|no external sources|do not use external sources)\b",
    r"(不需要搜索|无需搜索|不要搜索|不搜索|不要联网|不联网|不要浏览(?:网页|网络)?|不浏览(?:网页|网络)?|仅使用本地资料|只使用本地资料|仅限本地资料)",
]
OPEN_ENDED_PATTERNS = [
    r"\b(unfamiliar|novel|complex|non-trivial|open-ended|unresolved|ambiguous|difficult|hard|deep|in-depth|trade-?off|unknown|design|recommend|architecture|strategy|compare|optimi[sz]e)\b",
    r"(陌生|新颖|复杂|困难|开放式|未解决|不明确|未知|深入|取舍|权衡|推荐|设计|架构|策略|比较|优化)",
]
CONTROLLER_OWNED_PATTERNS = [
    r"(?:already|currently) selected (?:implementation|domain|test|review) workflow",
    r"(?:workflow|controller) already owns",
    r"(?:do not|don't|without) add (?:a )?(?:supplementary|additional|extra) (?:quality|harness|review) pass",
    r"(?:不要|无需|不需要).*(?:额外|补充|新增).*(?:Harness|审查|质量|流程|代理)",
]
# A leading slash is not ownership evidence here: real command expansion has
# its own Claude Code lifecycle, while slash-prefixed natural language may be
# an endpoint, path, or part of the user's task.
EXPLICIT_HARNESS_PATTERNS = [
    r"(?:/capability-harness(?::capability-harness)?\b|capability-harness:capability-harness\b)",
]


def read_stdin_json() -> dict[str, Any]:
    try:
        raw = sys.stdin.read()
        data = json.loads(raw or "{}")
        return data if isinstance(data, dict) else {}
    except Exception:
        return {}


def json_output(data: dict[str, Any]) -> None:
    sys.stdout.write(json.dumps(data, ensure_ascii=False))


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
    external_discovery_disallowed = any_match(stripped, NO_EXTERNAL_DISCOVERY_PATTERNS)
    explicit_harness = any_match(stripped, EXPLICIT_HARNESS_PATTERNS)
    controller_owned = any_match(stripped, CONTROLLER_OWNED_PATTERNS) and not explicit_harness
    project = any_match(stripped, PROJECT_PATTERNS) and not any_match(stripped, NO_PROJECT_CONTEXT_PATTERNS)
    high_consequence = any_match(stripped, HIGH_CONSEQUENCE_PATTERNS)
    open_ended_signal = len(stripped) >= 40 and any_match(stripped, OPEN_ENDED_PATTERNS)
    substantive = not trivial and (
        len(stripped) >= 100
        or current
        or implementation
        or artifact
        or quality
        or project
        or high_consequence
        or open_ended_signal
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
        "external_discovery_disallowed": external_discovery_disallowed,
        "project_dependent": project,
        "high_consequence": high_consequence,
        "open_ended_signal": open_ended_signal,
        "controller_owned": controller_owned,
        "explicit_harness": explicit_harness,
    }


def candidate_actions(classification: dict[str, bool]) -> dict[str, bool]:
    """Return possible actions; the controller decides whether any are worth their cost."""
    quality = classification.get("quality_sensitive", False)
    fully_specified = classification.get("fully_specified", False)
    artifact = classification.get("visual_or_artifact", False)
    open_ended = bool(
        classification.get("substantive")
        and not classification.get("implementation")
        and not classification.get("project_dependent")
        and not classification.get("current_or_version_specific")
        and not classification.get("high_consequence")
    )
    return {
        "current_evidence": bool(classification.get("current_or_version_specific")),
        "project_inspection": bool(classification.get("project_dependent")),
        "context_discovery": bool(
            not fully_specified
            and not classification.get("external_discovery_disallowed", False)
            and (
                (artifact and quality)
                or (quality and classification.get("external_guidance", False))
                or open_ended
            )
        ),
        "observable_check": bool(classification.get("implementation") or artifact),
        "independent_comparison": bool(quality and not fully_specified),
        "high_consequence_review": bool(classification.get("high_consequence")),
    }


def select_pre_action_route(classification: dict[str, bool]) -> tuple[str, str]:
    """Choose the strongest safe default before the controller starts material work.

    The hook is intentionally conservative: it only selects a route when prompt
    signals make the next source of evidence clear. The active controller still
    owns the task and may continue directly only after a selected leaf worker
    returns a bounded skip or the requested evidence is unavailable.
    """
    if not classification.get("substantive"):
        return "direct", "The request is low-complexity."
    if classification.get("controller_owned"):
        return "direct", "An explicit controller boundary owns this invocation."

    candidates = candidate_actions(classification)
    if candidates["project_inspection"]:
        return "project_inspection", "Local project facts can control the first decision."
    if classification.get("external_discovery_disallowed"):
        return "direct", "The user explicitly disallowed external discovery."
    if candidates["current_evidence"] or candidates["high_consequence_review"]:
        return "evidence_research", "A current or consequential external fact can change the result."
    if candidates["context_discovery"]:
        return "context_discovery", "Omitted domain or task context can change the construction or selection plan."
    if classification.get("fully_specified"):
        return "direct", "The request is sufficiently fixed for a direct path."
    return "direct", "No strong pre-action route was identified; proceed without Harness context injection."
