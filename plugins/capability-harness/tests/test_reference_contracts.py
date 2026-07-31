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

    def test_contract_reference_keeps_execution_verifier_evidence_only(self) -> None:
        contracts = (REFERENCE_ROOT / "capability-contracts.md").read_text(encoding="utf-8")
        self.assertIn("It does not modify source files, repair defects, assign severity, recommend a fix", contracts)
        self.assertNotIn("## Results", contracts)

    def test_installation_reference_is_project_scoped(self) -> None:
        installation = (REFERENCE_ROOT / "installation.md").read_text(encoding="utf-8")
        self.assertIn("--scope local", installation)
        self.assertIn("does not install or modify `C:\\Users\\wang\\.claude`", installation)
        self.assertNotIn("scripts/install_claude.py", installation)


if __name__ == "__main__":
    unittest.main()
