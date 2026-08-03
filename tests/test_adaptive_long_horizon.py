from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
SOURCE = (ROOT / "workflows" / "adaptive-long-horizon.js").read_text(encoding="utf-8")
README = (ROOT / "workflows" / "README.md").read_text(encoding="utf-8")
TRIGGER_MATRIX = (ROOT / "tests" / "trigger-matrix.md").read_text(encoding="utf-8")


class AdaptiveLongHorizonContractTests(unittest.TestCase):
    def test_workflow_shape_and_prompt_boundary_are_explicit(self) -> None:
        self.assertIn("name: 'adaptive-long-horizon'", SOURCE)
        self.assertIn("prompt-constrained", SOURCE)
        self.assertIn("The host must enforce tool restrictions separately", SOURCE)
        self.assertNotIn("tools:", SOURCE)
        self.assertNotIn("disallowedTools:", SOURCE)

    def test_input_and_evidence_limits_are_present(self) -> None:
        for marker in (
            "maxAgents: 4",
            "MAX_TEXT_LENGTH = 2000",
            "MAX_ACCEPTANCE_CRITERIA = 32",
            "MAX_RESULT_ITEMS = 32",
            "MAX_TOTAL_CANDIDATE_EVIDENCE = 64",
            "MAX_NEXT_QUESTION_LENGTH = 1000",
        ):
            self.assertIn(marker, SOURCE)

    def test_location_and_question_guards_are_present(self) -> None:
        self.assertIn("Number.isSafeInteger(start)", SOURCE)
        self.assertIn("start >= 1", SOURCE)
        self.assertIn("end >= start", SOURCE)
        self.assertIn("state.askedQuestions.some", SOURCE)
        self.assertIn("state.askedQuestions.push(nextQuestion)", SOURCE)

    def test_candidate_reference_guards_remain_intact(self) -> None:
        for marker in (
            "Verifier cited evidence ${reference.id} outside the candidate evidence set.",
            "candidate.criterionIds.includes(criterionDefinition.id)",
            "candidate.polarity !== 'support'",
            "MAX_TOTAL_CANDIDATE_EVIDENCE",
        ):
            self.assertIn(marker, SOURCE)

    def test_source_has_no_direct_side_effect_api(self) -> None:
        for marker in ("import fs", "child_process", "fetch(", "process."):
            self.assertNotIn(marker, SOURCE)

    def test_docs_and_matrix_preserve_runtime_evidence_boundary(self) -> None:
        self.assertIn("not proof that the installed host has technically denied", README)
        self.assertIn("project-level `.claude/workflows/`", README)
        self.assertIn("no host-enforced worker tool boundary", TRIGGER_MATRIX)
        self.assertIn("UNVERIFIED", TRIGGER_MATRIX)


if __name__ == "__main__":
    unittest.main()
