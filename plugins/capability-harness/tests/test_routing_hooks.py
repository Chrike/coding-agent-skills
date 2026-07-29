from __future__ import annotations

import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest


PLUGIN_ROOT = Path(__file__).resolve().parents[1]
USER_PROMPT_HOOK = PLUGIN_ROOT / "hooks" / "user_prompt_submit.py"
STOP_HOOK = PLUGIN_ROOT / "hooks" / "stop.py"


class RoutingHookTests(unittest.TestCase):
    def run_hook(self, script: Path, payload: object) -> dict[str, object] | None:
        text = payload if isinstance(payload, str) else json.dumps(payload)
        result = subprocess.run(
            [sys.executable, "-B", str(script)],
            input=text,
            text=True,
            capture_output=True,
            check=False,
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(result.stderr, "")
        return json.loads(result.stdout) if result.stdout else None

    def setUp(self) -> None:
        self.temp_dir = tempfile.TemporaryDirectory()
        self.project = Path(self.temp_dir.name)
        self.transcript = self.project / "transcript.jsonl"
        self.transcript.write_text("", encoding="utf-8")
        self.base_event = {
            "session_id": "routing-test",
            "cwd": str(self.project),
            "transcript_path": str(self.transcript),
        }

    def tearDown(self) -> None:
        self.temp_dir.cleanup()

    def submit(self, prompt: str) -> dict[str, object] | None:
        event = dict(self.base_event)
        event["prompt"] = prompt
        return self.run_hook(USER_PROMPT_HOOK, event)

    def stop(self, **extra: object) -> dict[str, object] | None:
        event = dict(self.base_event)
        event.update(extra)
        return self.run_hook(STOP_HOOK, event)

    def state(self) -> dict[str, object]:
        state_path = self.project / ".claude" / "capability-harness" / "state" / "routing-test.json"
        return json.loads(state_path.read_text(encoding="utf-8"))

    def append_tools(self, *names: str) -> None:
        with self.transcript.open("a", encoding="utf-8") as stream:
            for name in names:
                stream.write(json.dumps({"type": "tool_use", "name": name}) + "\n")

    def test_substantive_prompt_persists_classification_and_routing_context(self) -> None:
        output = self.submit("Implement the current version-specific API behavior in this project and verify it.")
        self.assertIsNotNone(output)
        assert output is not None
        context = output["hookSpecificOutput"]["additionalContext"]
        self.assertIn("project_inspection", context)
        self.assertIn("observable_check", context)
        self.assertIn("current_or_version_specific", context)

        state = self.state()
        self.assertTrue(state["classification"]["substantive"])
        self.assertTrue(state["requirements"]["project_inspection"])
        self.assertTrue(state["requirements"]["observable_check"])
        self.assertTrue(state["classification"]["current_or_version_specific"])

    def test_visual_artifact_is_quality_work_even_when_prompt_is_short(self) -> None:
        output = self.submit("请生成一个 SVG 插画，重点是视觉质量和构图。")
        self.assertIsNotNone(output)
        assert output is not None
        context = output["hookSpecificOutput"]["additionalContext"]
        self.assertIn("visual_or_artifact", context)
        self.assertIn("independent_branch_or_evaluation", context)
        self.assertIn("context_enrichment", context)

        state = self.state()
        self.assertTrue(state["classification"]["substantive"])
        self.assertTrue(state["classification"]["visual_or_artifact"])
        self.assertTrue(state["classification"]["quality_sensitive"])
        self.assertTrue(state["requirements"]["observable_check"])
        self.assertTrue(state["requirements"]["independent_branch_or_evaluation"])
        self.assertTrue(state["requirements"]["context_enrichment"])
        self.assertTrue(state["requirements"]["focused_web_guidance"])
        self.assertFalse(state["requirements"]["project_inspection"])

    def test_visual_artifact_requests_context_web_without_external_question(self) -> None:
        self.submit("请生成一个 SVG 插画，重点是视觉质量和构图。")
        state = self.state()
        self.assertTrue(state["requirements"]["focused_web_guidance"])
        output = self.stop()
        self.assertIsNotNone(output)
        assert output is not None
        self.assertIn("focused WebSearch/WebFetch", output["reason"])
        self.assertIn("Context Pack", output["reason"])

    def test_fully_specified_visual_task_can_remain_direct(self) -> None:
        self.submit("生成一个 24x24 SVG 红色圆形图标，固定尺寸和颜色，不需要视觉创新。")
        state = self.state()
        self.assertTrue(state["classification"]["fully_specified"])
        self.assertFalse(state["requirements"]["context_enrichment"])
        self.assertFalse(state["requirements"]["focused_web_guidance"])

    def test_visual_reference_request_prefers_focused_web_guidance(self) -> None:
        self.submit("设计一个 SVG 插画方案，参考当前优秀案例并推荐最佳构图。")
        state = self.state()
        self.assertTrue(state["requirements"]["focused_web_guidance"])
        output = self.stop()
        self.assertIsNotNone(output)
        assert output is not None
        self.assertIn("focused WebSearch/WebFetch", output["reason"])

    def test_low_complexity_prompt_is_direct_and_does_not_block(self) -> None:
        output = self.submit("hello")
        self.assertIsNotNone(output)
        assert output is not None
        self.assertIn("Answer directly", output["hookSpecificOutput"]["additionalContext"])
        self.assertIsNone(self.stop())

    def test_opt_out_does_not_create_state_or_context(self) -> None:
        output = self.submit("Implement this project change. [harness:off]")
        self.assertIsNone(output)
        state_dir = self.project / ".claude" / "capability-harness" / "state"
        self.assertFalse(state_dir.exists())

    def test_stop_blocks_missing_checks_once(self) -> None:
        self.submit("Implement a change in this project and run the relevant checks.")
        output = self.stop()
        self.assertIsNotNone(output)
        assert output is not None
        self.assertEqual(output["decision"], "block")
        self.assertIn("inspect", output["reason"])
        self.assertIn("observable", output["reason"])
        self.assertEqual(self.state()["stop_blocks"], 1)
        self.assertIsNone(self.stop())

    def test_stop_allows_matching_project_and_execution_evidence(self) -> None:
        self.submit("Implement a change in this project and run the relevant checks.")
        self.append_tools("Read", "Bash")
        self.assertIsNone(self.stop())

    def test_browser_observation_counts_as_execution_evidence(self) -> None:
        self.submit("Implement a change and verify it with a browser.")
        self.append_tools("Read", "playwright:browser_screenshot")
        self.assertIsNone(self.stop())

    def test_current_claim_requires_current_evidence(self) -> None:
        self.submit("What is the current version and documented behavior of this API?")
        output = self.stop()
        self.assertIsNotNone(output)
        assert output is not None
        self.assertIn("focused WebSearch/WebFetch", output["reason"])

    def test_quality_tradeoff_requires_independent_evidence(self) -> None:
        self.submit("Recommend the best architecture for this design trade-off.")
        output = self.stop()
        self.assertIsNotNone(output)
        assert output is not None
        self.assertIn("named Harness agent", output["reason"])
        self.assertIn("focused WebSearch", output["reason"])

    def test_quality_tradeoff_is_satisfied_by_agent_evidence(self) -> None:
        self.submit("Recommend the best architecture for this design trade-off.")
        self.append_tools(
            "WebSearch",
            "capability-harness:context-scout",
            "capability-harness:skeptical-evaluator",
        )
        self.assertIsNone(self.stop())

    def test_stop_records_reported_route_without_selecting_one(self) -> None:
        self.submit("Recommend the best architecture for this design trade-off.")
        self.append_tools(
            "WebSearch",
            "capability-harness:context-scout",
            "capability-harness:skeptical-evaluator",
        )
        self.assertIsNone(
            self.stop(
                last_assistant_message=(
                    "Route: capability-harness:skeptical-evaluator\n"
                    "Harness: used\n"
                    "Reason: the quality trade-off needed an independent judgment"
                )
            )
        )
        state = self.state()
        self.assertEqual(state["route"], "capability-harness:skeptical-evaluator")
        self.assertEqual(state["harness"], "used")
        self.assertIn("quality trade-off", state["route_reason"])


if __name__ == "__main__":
    unittest.main()
