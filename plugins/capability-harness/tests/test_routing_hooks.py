from __future__ import annotations

import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest


PLUGIN_ROOT = Path(__file__).resolve().parents[1]
USER_PROMPT_HOOK = PLUGIN_ROOT / "hooks" / "user_prompt_submit.py"
HOOKS_CONFIG = PLUGIN_ROOT / "hooks" / "hooks.json"


class RoutingHookTests(unittest.TestCase):
    def run_hook(self, payload: object) -> dict[str, object] | None:
        text = payload if isinstance(payload, str) else json.dumps(payload)
        result = subprocess.run(
            [sys.executable, "-B", str(USER_PROMPT_HOOK)],
            input=text,
            text=True,
            capture_output=True,
            check=False,
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(result.stderr, "")
        return json.loads(result.stdout) if result.stdout else None

    def submit(self, prompt: str, **extra: object) -> dict[str, object] | None:
        event: dict[str, object] = {"session_id": "routing-test", "cwd": "C:/example/project", "prompt": prompt}
        event.update(extra)
        return self.run_hook(event)

    def context_for(self, prompt: str) -> str:
        output = self.submit(prompt)
        self.assertIsNotNone(output)
        assert output is not None
        return str(output["hookSpecificOutput"]["additionalContext"])

    def test_project_prompt_selects_project_inspection_before_external_guidance(self) -> None:
        context = self.context_for(
            "Implement the current version-specific API behavior in this project and verify it."
        )
        self.assertIn("selected pre-action route: project inspection", context)
        self.assertIn("inspect the relevant current files", context)
        self.assertIn("evidence-researcher", context)
        self.assertNotIn("context-scout once", context)

    def test_open_ended_quality_artifact_selects_context_discovery_before_generation(self) -> None:
        context = self.context_for("请生成一个 SVG 插画，重点是视觉质量和构图。")
        self.assertIn("selected pre-action route: bounded context discovery", context)
        self.assertIn("invoke capability-harness:context-scout once", context)
        self.assertIn("direct, component, and adjacent-principle", context)
        self.assertIn("direct-route skip", context)

    def test_open_ended_recommendation_selects_context_discovery_without_visual_keywords(self) -> None:
        context = self.context_for("Recommend the best architecture for a new knowledge-intensive product.")
        self.assertIn("selected pre-action route: bounded context discovery", context)
        self.assertIn("invoke capability-harness:context-scout once", context)

    def test_fully_specified_visual_task_suppresses_optional_context_discovery(self) -> None:
        context = self.context_for("生成一个 24x24 SVG 红色圆形图标，固定尺寸和颜色，不需要视觉创新。")
        self.assertIn("adequately specified for a direct path", context)
        self.assertNotIn("context-scout", context)
        self.assertNotIn("evidence-researcher", context)

    def test_current_external_question_selects_focused_evidence_research(self) -> None:
        context = self.context_for("What is the current official API behavior for this product?")
        self.assertIn("selected pre-action route: focused evidence research", context)
        self.assertIn("invoke capability-harness:evidence-researcher once", context)
        self.assertIn("official-or-primary source scope", context)
        self.assertIn("Findings/Evidence return", context)

    def test_conversational_chinese_now_does_not_imply_current_evidence(self) -> None:
        context = self.context_for("现在下一步怎么做？")
        self.assertIn("adequately specified for a direct path", context)
        self.assertNotIn("evidence-researcher", context)

    def test_explicit_no_search_prevents_context_discovery(self) -> None:
        context = self.context_for("设计一个高质量的产品方案，不要搜索网络。")
        self.assertIn("adequately specified for a direct path", context)
        self.assertNotIn("context-scout", context)

    def test_explicit_no_search_overrides_current_external_evidence_route(self) -> None:
        context = self.context_for("当前官方 API 版本是什么？不要搜索网络。")
        self.assertIn("adequately specified for a direct path", context)
        self.assertNotIn("evidence-researcher", context)

    def test_low_complexity_prompt_is_direct(self) -> None:
        context = self.context_for("hello")
        self.assertIn("adequately specified for a direct path", context)
        self.assertNotIn("preflight", context)

    def test_opt_out_does_not_create_context_or_runtime_state(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            output = self.submit(
                "Implement this project change. [harness:off]",
                cwd=directory,
            )
            self.assertIsNone(output)
            self.assertFalse((Path(directory) / ".claude" / "capability-harness").exists())

    def test_substantive_prompt_does_not_write_runtime_state(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            output = self.submit(
                "Implement the current version-specific API behavior in this project and verify it.",
                cwd=directory,
            )
            self.assertIsNotNone(output)
            self.assertFalse((Path(directory) / ".claude" / "capability-harness").exists())

    def test_plugin_registers_prompt_and_leaf_agent_hooks_only(self) -> None:
        config = json.loads(HOOKS_CONFIG.read_text(encoding="utf-8"))
        self.assertEqual(set(config["hooks"]), {"UserPromptSubmit", "SubagentStop"})
        self.assertTrue((PLUGIN_ROOT / "hooks" / "user_prompt_submit.py").exists())
        self.assertFalse((PLUGIN_ROOT / "hooks" / "stop.py").exists())


if __name__ == "__main__":
    unittest.main()
