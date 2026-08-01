from __future__ import annotations

import json
from pathlib import Path
import subprocess
import sys
import unittest


PLUGIN_ROOT = Path(__file__).resolve().parents[1]
HOOK = PLUGIN_ROOT / "hooks" / "subagent_stop.py"
HOOKS_CONFIG = PLUGIN_ROOT / "hooks" / "hooks.json"


class SubagentStopHookTests(unittest.TestCase):
    def run_hook(self, payload: object) -> dict[str, object] | None:
        text = payload if isinstance(payload, str) else json.dumps(payload)
        result = subprocess.run(
            [sys.executable, "-B", str(HOOK)],
            input=text,
            text=True,
            capture_output=True,
            check=False,
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(result.stderr, "")
        return json.loads(result.stdout) if result.stdout else None

    def assert_allowed(self, payload: object) -> None:
        self.assertIsNone(self.run_hook(payload))

    def assert_blocked(self, payload: object) -> dict[str, object]:
        output = self.run_hook(payload)
        self.assertIsNotNone(output)
        assert output is not None
        self.assertEqual(output.get("decision"), "block")
        self.assertIsInstance(output.get("reason"), str)
        return output

    def test_accepts_complete_contracts_for_all_agents(self) -> None:
        messages = {
            "context-scout": (
                "## Capability decision\n- research can change component structure\n"
                "## Context gaps\n- missing wheel structure\n## Decision brief\n- tire, rim, spokes\n"
                "## Evidence\n- source\n## Plan implications\n- establish wheel anchors first"
            ),
            "evidence-researcher": "## Findings\n- fact\n\n## Evidence\n- source",
            "independent-brancher": (
                "## Approach\n- option\n## Assumptions\n- one\n## Plan\n1. step\n"
                "## Strengths\n- one\n## Failure conditions\n- one\n## Validation\n- check"
            ),
            "execution-verifier": (
                "## Verification target\n- claim\n## Checks executed\n- check\n"
                "## Evidence result\n- supports-claim"
            ),
            "skeptical-evaluator": (
                "## Hard-constraint verdict\n- pass\n## Comparative judgment\n- keep\n"
                "## Decisive evidence\n- result"
            ),
        }
        for agent, message in messages.items():
            with self.subTest(agent=agent):
                self.assert_allowed(
                    {
                        "agent_type": f"capability-harness:{agent}",
                        "last_assistant_message": message,
                    }
                )

    def test_accepts_case_insensitive_exact_headings(self) -> None:
        self.assert_allowed(
            {
                "agent_type": "capability-harness:evidence-researcher",
                "last_assistant_message": "## FINDINGS\n- fact\n## evidence\n- source",
            }
        )

    def test_accepts_blocked_brief_for_agents_with_blocked_contracts(self) -> None:
        for agent in ("context-scout", "evidence-researcher", "independent-brancher", "skeptical-evaluator"):
            with self.subTest(agent=agent):
                self.assert_allowed(
                    {
                        "agent_type": f"capability-harness:{agent}",
                        "last_assistant_message": (
                            "## Blocked brief\n- missing boundary\n"
                            "## Required next input\n- provide boundary"
                        ),
                    }
                )

    def test_context_scout_can_skip_when_no_bounded_task_context_is_available(self) -> None:
        self.assert_allowed(
            {
                "agent_type": "capability-harness:context-scout",
                "last_assistant_message": (
                    "## Capability decision\n- direct route\n"
                    "## Skip reason\n- no external context can change the fixed output"
                ),
            }
        )

    def test_accepts_unverified_execution_result(self) -> None:
        self.assert_allowed(
            {
                "agent_type": "capability-harness:execution-verifier",
                "last_assistant_message": (
                    "## Verification target\n- runtime claim and current artifact\n"
                    "## Checks executed\n- None; the host did not authorize execution\n"
                    "## Evidence result\n- unverified; no runtime evidence was obtained"
                ),
            }
        )

    def test_blocks_missing_headings(self) -> None:
        output = self.assert_blocked(
            {
                "agent_type": "capability-harness:evidence-researcher",
                "last_assistant_message": "## Findings\n- fact",
            }
        )
        self.assertIn("## Evidence", str(output["reason"]))

    def test_blocks_empty_required_sections(self) -> None:
        output = self.assert_blocked(
            {
                "agent_type": "capability-harness:evidence-researcher",
                "last_assistant_message": "## Findings\n\n## Evidence\n",
            }
        )
        self.assertIn("Empty sections", str(output["reason"]))

    def test_blocks_required_headings_out_of_order(self) -> None:
        output = self.assert_blocked(
            {
                "agent_type": "capability-harness:evidence-researcher",
                "last_assistant_message": "## Evidence\n- source\n## Findings\n- fact",
            }
        )
        self.assertIn("out of order", str(output["reason"]))

    def test_blocks_incomplete_blocked_contract(self) -> None:
        output = self.assert_blocked(
            {
                "agent_type": "capability-harness:evidence-researcher",
                "last_assistant_message": "## Blocked brief\n- missing boundary",
            }
        )
        self.assertIn("blocked contract", str(output["reason"]))

    def test_blocks_blocked_contract_with_normal_success_sections(self) -> None:
        output = self.assert_blocked(
            {
                "agent_type": "capability-harness:evidence-researcher",
                "last_assistant_message": (
                    "## Blocked brief\n- missing boundary\n"
                    "## Required next input\n- provide boundary\n"
                    "## Findings\n- fact\n## Evidence\n- source"
                ),
            }
        )
        self.assertIn("normal success contract", str(output["reason"]))

    def test_blocks_context_skip_with_normal_discovery_sections(self) -> None:
        output = self.assert_blocked(
            {
                "agent_type": "capability-harness:context-scout",
                "last_assistant_message": (
                    "## Capability decision\n- direct route\n"
                    "## Skip reason\n- no bounded source\n"
                    "## Evidence\n- source"
                ),
            }
        )
        self.assertIn("normal discovery sections", str(output["reason"]))

    def test_blocks_context_skip_with_blocked_contract(self) -> None:
        output = self.assert_blocked(
            {
                "agent_type": "capability-harness:context-scout",
                "last_assistant_message": (
                    "## Capability decision\n- missing boundary\n"
                    "## Skip reason\n- no bounded source\n"
                    "## Blocked brief\n- missing boundary\n"
                    "## Required next input\n- provide boundary"
                ),
            }
        )
        self.assertIn("blocked contract", str(output["reason"]))

    def test_blocks_empty_context_skip_contract(self) -> None:
        output = self.assert_blocked(
            {
                "agent_type": "capability-harness:context-scout",
                "last_assistant_message": "## Capability decision\n\n## Skip reason\n",
            }
        )
        self.assertIn("skip contract", str(output["reason"]))

    def test_blocks_heading_names_embedded_in_prose(self) -> None:
        self.assert_blocked(
            {
                "agent_type": "capability-harness:evidence-researcher",
                "last_assistant_message": (
                    "This sentence mentions ## Findings and ## Evidence but returns no structured result."
                ),
            }
        )

    def test_blocks_headings_inside_fenced_code(self) -> None:
        for fence in ("```", "~~~"):
            with self.subTest(fence=fence):
                self.assert_blocked(
                    {
                        "agent_type": "capability-harness:evidence-researcher",
                        "last_assistant_message": (
                            f"{fence}markdown\n## Findings\n- placeholder\n"
                            f"## Evidence\n- placeholder\n{fence}"
                        ),
                    }
                )

    def test_blocks_headings_formatted_as_quotes_lists_or_indented_code(self) -> None:
        for prefix in ("> ", "- ", "    "):
            with self.subTest(prefix=prefix):
                self.assert_blocked(
                    {
                        "agent_type": "capability-harness:evidence-researcher",
                        "last_assistant_message": (
                            f"{prefix}## Findings\n- fact\n{prefix}## Evidence\n- source"
                        ),
                    }
                )

    def test_allows_retry_to_stop_when_stop_hook_is_already_active(self) -> None:
        self.assert_allowed(
            {
                "agent_type": "capability-harness:evidence-researcher",
                "stop_hook_active": True,
                "last_assistant_message": "still incomplete",
            }
        )

    def test_ignores_unknown_agent_and_malformed_input(self) -> None:
        self.assert_allowed({"agent_type": "other:agent", "last_assistant_message": "anything"})
        self.assert_allowed("not-json")
        self.assert_allowed([])

    def test_plugin_registers_prompt_and_leaf_agent_hooks(self) -> None:
        config = json.loads(HOOKS_CONFIG.read_text(encoding="utf-8"))
        self.assertEqual(set(config["hooks"]), {"UserPromptSubmit", "SubagentStop"})
        for hook_group in config["hooks"].values():
            for registration in hook_group:
                self.assertEqual(registration["hooks"][0]["args"][0], "-B")
        self.assertTrue((PLUGIN_ROOT / "hooks" / "user_prompt_submit.py").exists())
        self.assertFalse((PLUGIN_ROOT / "hooks" / "stop.py").exists())

    def test_plugin_registers_context_scout_agent(self) -> None:
        config = json.loads(HOOKS_CONFIG.read_text(encoding="utf-8"))
        matcher = config["hooks"]["SubagentStop"][0]["matcher"]
        self.assertIn("context-scout", matcher)
        self.assertTrue((PLUGIN_ROOT / "agents" / "context-scout.md").exists())


if __name__ == "__main__":
    unittest.main()
