from __future__ import annotations

import json
import re
import sys
from typing import Any, Iterable


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
        "project_dependent": project,
        "high_consequence": high_consequence,
    }


def candidate_actions(classification: dict[str, bool]) -> dict[str, bool]:
    """Return possible actions; the controller decides whether any are worth their cost."""
    quality = classification.get("quality_sensitive", False)
    fully_specified = classification.get("fully_specified", False)
    artifact = classification.get("visual_or_artifact", False)
    return {
        "current_evidence": bool(classification.get("current_or_version_specific")),
        "project_inspection": bool(classification.get("project_dependent")),
        "context_discovery": bool(
            not fully_specified
            and ((artifact and quality) or (quality and classification.get("external_guidance", False)))
        ),
        "observable_check": bool(classification.get("implementation") or artifact),
        "independent_comparison": bool(quality and not fully_specified),
        "high_consequence_review": bool(classification.get("high_consequence")),
    }
