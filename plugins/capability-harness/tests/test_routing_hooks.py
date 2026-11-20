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
sys.path.insert(0, str(PLUGIN_ROOT / "hooks" / "lib"))
from common import classify_prompt


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
        self.assertIn("inspect only the current files", context)
        self.assertIn("evidence-researcher", context)
        self.assertNotIn("context-scout once", context)

    def test_open_ended_artifact_selects_context_discovery_before_generation(self) -> None:
        context = self.context_for(
            "Create a non-trivial visual artifact with unresolved structural and composition decisions."
        )
        self.assertIn("selected pre-action route: bounded context discovery", context)
        self.assertIn("selected pre-action route, not a generic suggestion", context)
        self.assertIn("invoke capability-harness:context-scout once", context)
        self.assertIn("direct, component, and adjacent-principle", context)
        self.assertIn("Pre-action Decision Brief", context)
        self.assertIn("authorizes public, non-sensitive discovery", context)
        self.assertIn("upper bound rather than a target", context)
        self.assertIn("do not require advance proof", context)
        self.assertIn("acceptance seed", context)
        self.assertIn("minimum observable signal", context)
        self.assertIn("not a new worker or completion gate", context)
        self.assertNotIn("Validation-cues", context)

    def test_open_ended_unfamiliar_domain_selects_context_discovery(self) -> None:
        context = self.context_for(
            "Explain a difficult unfamiliar domain problem and propose a practical solution with the important caveats."
        )
        self.assertIn("selected pre-action route: bounded context discovery", context)
        self.assertIn("Pre-action Decision Brief", context)

    def test_open_ended_chinese_question_selects_context_discovery(self) -> None:
        context = self.context_for("分析一个复杂技术问题，其中核心约束尚未解决，并给出可执行的解决策略和重要限制。")
        self.assertIn("selected pre-action route: bounded context discovery", context)

    def test_open_ended_recommendation_selects_context_discovery_without_visual_keywords(self) -> None:
        context = self.context_for("Recommend the best architecture for a new knowledge-intensive product.")
        self.assertIn("selected pre-action route: bounded context discovery", context)
        self.assertIn("invoke capability-harness:context-scout once", context)

    def test_unfamiliar_implementation_selects_context_discovery(self) -> None:
        context = self.context_for(
            "Implement a parser for an unfamiliar calendrical notation with unresolved domain rules."
        )
        self.assertIn("selected pre-action route: bounded context discovery", context)

    def test_short_strong_context_gap_selects_context_discovery(self) -> None:
        context = self.context_for("Implement an unfamiliar codec.")
        self.assertIn("selected pre-action route: bounded context discovery", context)

    def test_quality_sensitive_artifact_still_selects_context_discovery(self) -> None:
        context = self.context_for("Create a high-quality visual artifact with coherent composition.")
        self.assertIn("selected pre-action route: bounded context discovery", context)

    def test_explicit_external_standard_can_select_context_discovery(self) -> None:
        context = self.context_for("Compare against a standard.")
        self.assertIn("selected pre-action route: bounded context discovery", context)

    def test_generic_quality_and_comparison_terms_stay_direct(self) -> None:
        for prompt in (
            "Optimize this logic and compare two options.",
            "Optimize it.",
            "Compare options.",
            "Improve this.",
            "Design this.",
            "Recommend one.",
            "Best option?",
            "Architecture?",
            "Strategy?",
            "优化一下。",
            "比较选项。",
            "设计这个。",
            "推荐一个。",
            "最好选项？",
            "架构？",
            "策略？",
            "优化这个逻辑并比较两个选项，然后按现有要求选择更好的方案，同时保持当前输入和输出不变即可。",
        ):
            with self.subTest(prompt=prompt):
                self.assertIsNone(self.submit(prompt))

    def test_fully_specified_artifact_task_suppresses_optional_context_discovery(self) -> None:
        self.assertIsNone(
            self.submit("Create a 24x24 red circular icon with fixed dimensions and color, without visual innovation.")
        )

    def test_fixed_scope_words_do_not_hide_open_ended_tradeoffs(self) -> None:
        for prompt in (
            "Design an exactly-once delivery system with unresolved trade-offs.",
            "帮我设计一个复杂系统，只需考虑核心架构权衡。",
            "帮我设计一个全新的微服务架构方案",
            "设计一个复杂系统，服务边界尚未解决，只需生成架构建议，并指出关键权衡和风险。",
        ):
            with self.subTest(prompt=prompt):
                context = self.context_for(prompt)
                self.assertIn("selected pre-action route: bounded context discovery", context)

    def test_artifact_keyword_alone_stays_direct(self) -> None:
        self.assertIsNone(self.submit("Create a blue circle SVG."))

    def test_review_request_without_context_gap_stays_direct(self) -> None:
        self.assertIsNone(self.submit("Review this supplied function for correctness."))

    def test_long_fixed_transformation_without_context_gap_stays_direct(self) -> None:
        self.assertIsNone(
            self.submit(
                "Summarize the supplied passage into three bullets, preserve every date and proper noun, "
                "and use neutral language with no added commentary."
            )
        )

    def test_completed_observable_claim_does_not_trigger_context_discovery(self) -> None:
        self.assertIsNone(
            self.submit(
                "The implementation is complete, but the final claim depends on one bounded observable runtime "
                "behavior that has not been checked."
            )
        )

    def test_current_external_question_selects_focused_evidence_research(self) -> None:
        context = self.context_for("What is the current official API behavior for this product?")
        self.assertIn("selected pre-action route: focused evidence research", context)
        self.assertIn("invoke capability-harness:evidence-researcher once", context)
        self.assertIn("authorizes public, non-sensitive research", context)
        self.assertIn("own contract supplies its return format and stop condition", context)

    def test_version_specific_qualifier_selects_focused_evidence_research(self) -> None:
        context = self.context_for("What version is currently supported by this product?")
        self.assertIn("selected pre-action route: focused evidence research", context)

    def test_conversational_chinese_now_does_not_imply_current_evidence(self) -> None:
        self.assertIsNone(self.submit("现在下一步怎么做？"))

    def test_explicit_no_search_prevents_context_discovery(self) -> None:
        self.assertIsNone(self.submit("设计一个高质量的产品方案，不要搜索网络。"))

    def test_explicit_no_search_overrides_current_external_evidence_route(self) -> None:
        self.assertIsNone(self.submit("当前官方 API 版本是什么？不要搜索网络。"))

    def test_chinese_external_search_constraints_suppress_guidance_and_routing(self) -> None:
        prompt = "不要用外部搜索，分析一下当前的最新API版本。"
        self.assertIsNone(self.submit(prompt))
        classification = classify_prompt(prompt)
        self.assertTrue(classification["external_discovery_disallowed"])
        self.assertFalse(classification["external_guidance"])

    def test_explicit_no_delegation_suppresses_agent_route(self) -> None:
        self.assertIsNone(
            self.submit("What is the current official API behavior? Do not delegate to an agent.")
        )

    def test_explicit_chinese_no_delegation_suppresses_agent_route(self) -> None:
        self.assertIsNone(self.submit("当前官方 API 行为是什么？不要调用子代理。"))

    def test_low_complexity_prompt_is_direct(self) -> None:
        self.assertIsNone(self.submit("hello"))

    def test_simple_spelling_fix_is_silent(self) -> None:
        self.assertIsNone(self.submit("Fix this obvious spelling mistake in one Markdown heading."))

    def test_isolated_file_and_unqualified_price_or_production_terms_stay_direct(self) -> None:
        for prompt in (
            "Fix the typo in this file.",
            "请帮我修改当前文件里的一个拼写错误。",
            "Fix a production typo in the footer.",
            "What is the price field type in our JSON schema?",
        ):
            with self.subTest(prompt=prompt):
                self.assertIsNone(self.submit(prompt))

    def test_current_module_security_review_selects_local_project_inspection(self) -> None:
        context = self.context_for("Review the current module for security issues.")
        self.assertIn("selected pre-action route: project inspection", context)
        self.assertNotIn("focused evidence research", context)

    def test_local_function_security_review_keeps_external_evidence_route(self) -> None:
        for prompt in (
            "Fix a security vulnerability in this function.",
            "检查一下这段代码的内存安全漏洞。",
        ):
            with self.subTest(prompt=prompt):
                context = self.context_for(prompt)
                self.assertIn("selected pre-action route: focused evidence research", context)

    def test_explicit_host_commands_bypass_pre_action_routes(self) -> None:
        for prompt in (
            "/security-review on this PR",
            "Run /security-review on this PR.",
            "/code-review",
            "Run /adaptive-long-horizon on this codebase.",
        ):
            with self.subTest(prompt=prompt):
                self.assertIsNone(self.submit(prompt))

    def test_known_bug_with_existing_plan_is_silent(self) -> None:
        self.assertIsNone(
            self.submit("Fix this coherent bug. The cause and exact focused regression test are already known.")
        )

    def test_explicit_workflow_ownership_is_silent(self) -> None:
        self.assertIsNone(
            self.submit("The workflow already owns this localized fix; follow its existing plan without adding another pass.")
        )

    def test_explicit_controller_ownership_is_silent_without_command_name_heuristics(self) -> None:
        self.assertIsNone(
            self.submit("The selected review workflow already owns this change; do not add another controller.")
        )

    def test_selected_workflow_without_another_controller_is_silent(self) -> None:
        self.assertIsNone(
            self.submit(
                "A workflow is already selected for this localized security review in the current project; "
                "follow it without adding another controller."
            )
        )

    def test_slash_prefixed_natural_language_is_not_assumed_controller_owned(self) -> None:
        context = self.context_for("/api Design a new visual system with unresolved composition decisions.")
        self.assertIn("selected pre-action route: bounded context discovery", context)

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

    def test_stable_concept_terms_do_not_trigger_current_or_project_routes(self) -> None:
        for prompt in (
            "Explain version control in a simple way.",
            "Explain package management for a new developer.",
        ):
            with self.subTest(prompt=prompt):
                self.assertIsNone(self.submit(prompt))

    def test_greenfield_project_concept_does_not_trigger_local_inspection(self) -> None:
        context = self.context_for(
            "Design a new project architecture for a greenfield product with unresolved trade-offs."
        )
        self.assertIn("selected pre-action route: bounded context discovery", context)
        self.assertNotIn("selected pre-action route: project inspection", context)

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

    def test_quoted_or_backticked_opt_out_literal_does_not_disable_routing(self) -> None:
        for literal in ('"[harness:off]"', "'[harness:off]'", "`[harness:off]`", "```\n[harness:off]\n```", "prefix[harness:off]suffix"):
            with self.subTest(literal=literal):
                context = self.context_for(
                    f"Explain a difficult unfamiliar domain problem with unresolved trade-offs; the literal {literal} is documentation."
                )
                self.assertIn("selected pre-action route: bounded context discovery", context)

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
