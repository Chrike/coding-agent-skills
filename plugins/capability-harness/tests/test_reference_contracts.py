from __future__ import annotations

from pathlib import Path
import unittest


PLUGIN_ROOT = Path(__file__).resolve().parents[1]
REFERENCE_ROOT = PLUGIN_ROOT / "references"
SKILL_PATH = PLUGIN_ROOT / "skills" / "capability-harness" / "SKILL.md"

EXPECTED_REFERENCES = {
    "architecture.md",
    "routing-policy.md",
    "capability-contracts.md",
    "evidence-policy.md",
    "evaluation-policy.md",
    "failure-recovery.md",
    "installation.md",
    "design-intent.md",
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
        routing = (REFERENCE_ROOT / "routing-policy.md").read_text(encoding="utf-8")
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
        self.assertIn("tools: Read, Grep, Glob, Bash", verifier)
        self.assertIn("exact command or action", verifier)
        self.assertIn("Host permission prompts and policy remain authoritative", verifier)

    def test_installation_reference_is_project_scoped(self) -> None:
        installation = (REFERENCE_ROOT / "installation.md").read_text(encoding="utf-8")
        self.assertIn("--scope local", installation)
        self.assertIn("does not install or modify the user's global Claude Code configuration", installation)
        self.assertNotIn("C:\\Users\\wang\\.claude", installation)
        self.assertNotIn("scripts/install_claude.py", installation)


if __name__ == "__main__":
    unittest.main()
