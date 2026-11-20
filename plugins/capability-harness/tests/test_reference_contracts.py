from __future__ import annotations

import json
from pathlib import Path
import unittest


PLUGIN_ROOT = Path(__file__).resolve().parents[1]
REFERENCE_ROOT = PLUGIN_ROOT / "references"
SKILL_PATH = PLUGIN_ROOT / "skills" / "capability-harness" / "SKILL.md"
README_PATH = PLUGIN_ROOT / "README.md"
EVALS_PATH = PLUGIN_ROOT / "skills" / "capability-harness" / "evals" / "evals.json"

EXPECTED_REFERENCES = {
    "capability-contracts.md",
    "routing-and-operations.md",
    "evidence-evaluation-recovery.md",
}

MINIMUM_CONTRACTS = {
    "Context scout": [
        "## Capability decision",
        "## Context gaps",
        "## Decision brief",
        "## Evidence",
        "## Plan implications",
    ],
    "Evidence researcher": ["## Findings", "## Evidence"],
    "Independent brancher": [
        "## Approach",
        "## Assumptions",
        "## Plan",
        "## Strengths",
        "## Failure conditions",
        "## Validation",
    ],
    "Execution verifier": [
        "## Verification target",
        "## Checks executed",
        "## Evidence result",
    ],
    "Skeptical evaluator": [
        "## Hard-constraint verdict",
        "## Comparative judgment",
        "## Decisive evidence",
    ],
}


class ReferenceContractTests(unittest.TestCase):
    def test_reference_inventory_is_complete(self) -> None:
        actual = {path.name for path in REFERENCE_ROOT.glob("*.md")}
        self.assertEqual(actual, EXPECTED_REFERENCES)

    def test_skill_links_all_reference_documents(self) -> None:
        skill = SKILL_PATH.read_text(encoding="utf-8")
        for name in EXPECTED_REFERENCES:
            self.assertIn(f"../../references/{name}", skill)

    def test_readme_links_all_reference_documents(self) -> None:
        readme = README_PATH.read_text(encoding="utf-8")
        for name in EXPECTED_REFERENCES:
            self.assertIn(f"references/{name}", readme)

    def test_hook_route_reminder_is_documented_as_uniform_context(self) -> None:
        skill = SKILL_PATH.read_text(encoding="utf-8")
        readme = README_PATH.read_text(encoding="utf-8")
        for text in (skill, readme):
            self.assertIn("same brief route reminder", text)
            self.assertNotIn("recognized prompt signals", text)
            self.assertNotIn("must not receive extra hook context", text)

    def test_contract_reference_matches_current_agent_minimums(self) -> None:
        contracts = (REFERENCE_ROOT / "capability-contracts.md").read_text(encoding="utf-8")
        for role, headings in MINIMUM_CONTRACTS.items():
            self.assertIn(f"## {role}", contracts)
            for heading in headings:
                self.assertIn(heading, contracts)

    def test_search_contracts_inherit_public_scope_and_stop_on_information_value(self) -> None:
        context_scout = (PLUGIN_ROOT / "agents" / "context-scout.md").read_text(encoding="utf-8")
        evidence_researcher = (PLUGIN_ROOT / "agents" / "evidence-researcher.md").read_text(encoding="utf-8")
        contracts = (REFERENCE_ROOT / "capability-contracts.md").read_text(encoding="utf-8")

        for content in (context_scout, evidence_researcher):
            self.assertIn("does not need to repeat a network-authorization sentence", content)
        self.assertIn("upper bound rather than a target", context_scout)
        self.assertIn("clearly diminishing", context_scout)
        self.assertIn("information value", context_scout)
        self.assertIn("upper bound rather than a target", contracts)
        self.assertNotIn("3-5", contracts)

    def test_acceptance_seed_is_controller_owned_and_not_a_leaf_gate(self) -> None:
        skill = SKILL_PATH.read_text(encoding="utf-8")
        contracts = (REFERENCE_ROOT / "capability-contracts.md").read_text(encoding="utf-8")
        routing = (REFERENCE_ROOT / "routing-and-operations.md").read_text(encoding="utf-8")
        verifier = (PLUGIN_ROOT / "agents" / "execution-verifier.md").read_text(encoding="utf-8")
        context_scout = (PLUGIN_ROOT / "agents" / "context-scout.md").read_text(encoding="utf-8")

        self.assertIn("## Acceptance Seed", skill)
        self.assertIn("Outcome and target/scope", skill)
        self.assertIn("Minimum observable signal", contracts)
        self.assertIn("not a leaf-agent return contract", contracts)
        self.assertIn("`defined`", contracts)
        self.assertIn("This is not a fifth route or a required form.", routing)
        self.assertIn("not as permission or an overall completion verdict", verifier)
        self.assertIn("If the controller supplies an Acceptance Seed", context_scout)

    def test_contract_reference_keeps_execution_verifier_evidence_only(self) -> None:
        contracts = (REFERENCE_ROOT / "capability-contracts.md").read_text(encoding="utf-8")
        self.assertIn("It does not modify source files, repair defects, assign severity, recommend a fix", contracts)
        self.assertNotIn("## Results", contracts)

    def test_execution_verifier_requires_an_exact_authorized_check(self) -> None:
        verifier = (PLUGIN_ROOT / "agents" / "execution-verifier.md").read_text(encoding="utf-8")
        self.assertIn("tools: Read, Grep, Glob, Bash, LSP", verifier)
        self.assertIn("exact command or action", verifier)
        self.assertIn("Host permission prompts and policy remain authoritative", verifier)

    def test_installation_reference_is_project_scoped(self) -> None:
        operations = (REFERENCE_ROOT / "routing-and-operations.md").read_text(encoding="utf-8")
        self.assertIn("claude plugin marketplace add . --scope local", operations)
        self.assertIn("claude plugin install capability-harness@coding-agent-skills --scope local", operations)
        self.assertIn(r"claude --plugin-dir .\plugins\capability-harness", operations)
        self.assertIn("does not modify global Claude Code configuration", operations)
        self.assertNotRegex(operations, r"C:\\Users\\[^\\]+\\.claude")
        self.assertNotIn("scripts/install_claude.py", operations)


    def test_direct_calibration_cases_allow_uniform_hook_context(self) -> None:
        evals = json.loads(EVALS_PATH.read_text(encoding="utf-8"))["evals"]
        cases = {case["id"]: case for case in evals}
        for case_id in (4, 5, 7):
            with self.subTest(case_id=case_id):
                case = cases[case_id]
                text = case["expected_output"] + " " + " ".join(case["assertions"])
                self.assertIn("uniform Hook context may be present", text)
                self.assertIn("direct route", text)
                self.assertIn("unrelated agents", text)
                self.assertIn("duplicate controllers", text)
                self.assertNotIn("Hook emits no additional context", text)


if __name__ == "__main__":
    unittest.main()
