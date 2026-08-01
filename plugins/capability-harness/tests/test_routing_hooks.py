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

    def test_open_ended_artifact_selects_context_discovery_before_generation(self) -> None:
        context = self.context_for(
            "Create a non-trivial visual artifact with unresolved structural and composition decisions."
        )
        self.assertIn("selected pre-action route: bounded context discovery", context)
        self.assertIn("invoke capability-harness:context-scout once", context)
        self.assertIn("direct, component, and adjacent-principle", context)
        self.assertIn("Pre-action Decision Brief", context)
        self.assertIn("do not require advance proof", context)
        self.assertNotIn("Validation-cues", context)

    def test_open_ended_unfamiliar_domain_selects_context_discovery(self) -> None:
        context = self.context_for(
            "Explain a difficult unfamiliar domain problem and propose a practical solution with the important caveats."
        )
        self.assertIn("selected pre-action route: bounded context discovery", context)
        self.assertIn("Pre-action Decision Brief", context)

    def test_open_ended_chinese_question_selects_context_discovery(self) -> None:
        context = self.context_for("分析一个复杂技术问题，并给出可执行的解决策略和重要限制。")
        self.assertIn("selected pre-action route: bounded context discovery", context)

    def test_open_ended_recommendation_selects_context_discovery_without_visual_keywords(self) -> None:
        context = self.context_for("Recommend the best architecture for a new knowledge-intensive product.")
        self.assertIn("selected pre-action route: bounded context discovery", context)
        self.assertIn("invoke capability-harness:context-scout once", context)

    def test_fully_specified_artifact_task_suppresses_optional_context_discovery(self) -> None:
        self.assertIsNone(
            self.submit("Create a 24x24 red circular icon with fixed dimensions and color, without visual innovation.")
        )

    def test_current_external_question_selects_focused_evidence_research(self) -> None:
        context = self.context_for("What is the current official API behavior for this product?")
        self.assertIn("selected pre-action route: focused evidence research", context)
        self.assertIn("invoke capability-harness:evidence-researcher once", context)
        self.assertIn("official-or-primary source scope", context)
        self.assertIn("Findings/Evidence return", context)

    def test_conversational_chinese_now_does_not_imply_current_evidence(self) -> None:
        self.assertIsNone(self.submit("现在下一步怎么做？"))

    def test_explicit_no_search_prevents_context_discovery(self) -> None:
        self.assertIsNone(self.submit("设计一个高质量的产品方案，不要搜索网络。"))

    def test_explicit_no_search_overrides_current_external_evidence_route(self) -> None:
        self.assertIsNone(self.submit("当前官方 API 版本是什么？不要搜索网络。"))

    def test_low_complexity_prompt_is_direct(self) -> None:
        self.assertIsNone(self.submit("hello"))

    def test_simple_spelling_fix_is_silent(self) -> None:
        self.assertIsNone(self.submit("Fix this obvious spelling mistake in one Markdown heading."))

    def test_known_bug_with_existing_plan_is_silent(self) -> None:
        self.assertIsNone(
            self.submit("Fix this coherent bug. The cause and exact focused regression test are already known.")
        )

    def test_explicit_workflow_ownership_is_silent(self) -> None:
        self.assertIsNone(
            self.submit("The workflow already owns this localized fix; follow its existing plan without adding another pass.")
        )

    def test_explicit_slash_command_is_controller_owned_without_hardcoded_names(self) -> None:
        self.assertIsNone(self.submit("/quality-check Design a focused review plan for this change."))

    def test_explicit_harness_slash_command_keeps_harness_routing(self) -> None:
        context = self.context_for(
            "/capability-harness:capability-harness Create a non-trivial visual artifact with unresolved composition decisions."
        )
        self.assertIn("selected pre-action route: bounded context discovery", context)

    def test_no_project_context_does_not_trigger_project_inspection(self) -> None:
        self.assertIsNone(self.submit("Implement a change without repository context."))

    def test_generic_terms_with_no_project_context_and_no_browsing_stay_direct(self) -> None:
        for prompt in (
            "Explain version control without repository context and without browsing.",
            "Explain package management without project context and without browsing.",
        ):
            with self.subTest(prompt=prompt):
                self.assertIsNone(self.submit(prompt))

    def test_project_without_external_discovery_stays_local(self) -> None:
        context = self.context_for("In the current project, implement the API. Do not use external sources.")
        self.assertIn("use local project evidence only", context)
        self.assertNotIn("evidence-researcher", context)

    def test_no_browsing_phrases_are_silent(self) -> None:
        for prompt in (
            "Design this without browsing the web.",
            "Analyze this using no external sources.",
            "仅使用本地资料分析，不需要外部搜索。",
        ):
            with self.subTest(prompt=prompt):
                self.assertIsNone(self.submit(prompt))

    def test_offline_first_domain_does_not_mean_no_external_discovery(self) -> None:
        context = self.context_for(
            "Design an offline-first architecture for a mobile product with unresolved structural trade-offs."
        )
        self.assertIn("selected pre-action route: bounded context discovery", context)

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

    def test_context_route_requires_plan_integration_not_validation(self) -> None:
        context = self.context_for("Design a high-quality unfamiliar-domain solution with important structural trade-offs.")
        self.assertIn("Feed the returned Brief into the construction or selection plan", context)
        self.assertNotIn("Validation-cues return", context)

    def test_plugin_registers_prompt_and_leaf_agent_hooks_only(self) -> None:
        config = json.loads(HOOKS_CONFIG.read_text(encoding="utf-8"))
        self.assertEqual(set(config["hooks"]), {"UserPromptSubmit", "SubagentStop"})
        for hook_group in config["hooks"].values():
            for registration in hook_group:
                command_hook = registration["hooks"][0]
                self.assertEqual(command_hook["command"], "python")
                self.assertEqual(command_hook["args"][0], "-B")
        self.assertTrue((PLUGIN_ROOT / "hooks" / "user_prompt_submit.py").exists())
        self.assertFalse((PLUGIN_ROOT / "hooks" / "stop.py").exists())


if __name__ == "__main__":
    unittest.main()
