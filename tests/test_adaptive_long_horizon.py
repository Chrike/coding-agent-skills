from pathlib import Path
import json
import shutil
import subprocess
import unittest
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
SOURCE_PATH = ROOT / "workflows" / "adaptive-long-horizon.js"
SOURCE = SOURCE_PATH.read_text(encoding="utf-8")
README = (ROOT / "workflows" / "README.md").read_text(encoding="utf-8")
TRIGGER_MATRIX = (ROOT / "tests" / "trigger-matrix.md").read_text(encoding="utf-8")
NODE = shutil.which("node")

NODE_RUNNER = r"""
const fs = require('node:fs');
const source = fs.readFileSync(process.argv[1], 'utf8');
const options = JSON.parse(process.argv[2]);
const body = source.replace(/^export const meta = \{[\s\S]*?\}\s*/, '');
const AsyncFunction = Object.getPrototypeOf(async function () {}).constructor;
const run = new AsyncFunction('args', 'agent', body);
const criteria = options.criteria || ['Criterion one', 'Criterion two'];
const ids = criteria.map((_, i) => `C${i + 1}`);
const version = options.version || '0123456789abcdef0123456789abcdef01234567';
const evidence = (indexes) => indexes.map((i) => ({
  criterionIds: [ids[i]], kind: 'source', path: 'README.md', scope: criteria[i],
  version, location: `lines:${(i + 1) * 10}`, polarity: 'support', claim: `${criteria[i]} is supported`,
}));
const calls = [];
const collected = [];
let nextEvidence = 1;
const agent = async (_prompt, { label }) => {
  calls.push(label);
  if (label === 'adaptive completion verification') {
    return {
      status: 'verified', conclusion: 'All criteria verified.', blocker: '',
      criterionEvidence: criteria.map((criterion, i) => {
        const candidate = collected.find((item) => item.criterionIds.includes(ids[i]));
        return { criterion, evidence: candidate ? [{ id: candidate.id, path: candidate.path, version: candidate.version, location: candidate.location }] : [] };
      }),
    };
  }
  const round = calls.filter((item) => item.startsWith('adaptive evidence round')).length;
  let indexes;
  let status;
  if (options.mode === 'rounds' && round === 1) {
    indexes = [0]; status = 'evidence';
  } else if (options.mode === 'rounds' && round === 2) {
    indexes = [1]; status = 'complete';
  } else {
    indexes = ids.map((_, i) => i); status = 'complete';
  }
  for (const item of evidence(indexes)) collected.push({ id: `E${nextEvidence++}`, ...item });
  return {
    status, conclusion: 'Candidate conclusion.', candidateEvidence: evidence(indexes),
    supportedCriteria: indexes.map((i) => criteria[i]), activeHypothesis: '',
    failedOrRuledOutPaths: [], contradictions: [], resolvedContradictions: [],
    resolvedQuestion: `Inspected round ${round}.`, nextQuestion: status === 'evidence' ? 'Inspect the remaining criterion.' : '', blocker: '',
  };
};
run({ task: 'Verify the stated criteria.', acceptanceCriteria: criteria, limits: options.limits }, agent)
  .then((result) => console.log(JSON.stringify({ result, calls })))
  .catch((error) => { console.error(error); process.exitCode = 1; });
"""


@unittest.skipUnless(NODE, "Node.js is required for workflow execution tests")
class AdaptiveLongHorizonExecutionTests(unittest.TestCase):
    def run_workflow(self, **options: object) -> dict[str, Any]:
        result = subprocess.run(
            [NODE or "node", "-e", NODE_RUNNER, str(SOURCE_PATH), json.dumps(options)],
            text=True,
            capture_output=True,
            check=False,
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        return json.loads(result.stdout)

    def test_agent_budget_reserves_completion_verifier(self) -> None:
        cases = (
            ({"maxRounds": 2, "maxAgents": 2}, "complete", 2),
            ({"maxRounds": 3, "maxAgents": 3}, "rounds", 3),
        )
        for limits, mode, expected_calls in cases:
            with self.subTest(limits=limits):
                outcome = self.run_workflow(limits=limits, mode=mode)
                self.assertEqual(outcome["result"]["status"], "complete", outcome["result"])
                self.assertEqual(len(outcome["calls"]), expected_calls)
                self.assertEqual(outcome["calls"][-1], "adaptive completion verification")

    def test_completion_uses_criteria_accumulated_across_rounds(self) -> None:
        outcome = self.run_workflow(limits={"maxRounds": 3, "maxAgents": 4}, mode="rounds")
        self.assertEqual(outcome["result"]["status"], "complete", outcome["result"])
        self.assertEqual(outcome["result"]["materialState"]["supportedCriteria"], ["Criterion one", "Criterion two"])
        self.assertEqual(len(outcome["result"]["verifiedEvidence"]), 2)

    def test_only_immutable_commit_versions_are_accepted(self) -> None:
        commit = "0123456789abcdef0123456789abcdef01234567"
        for version in (commit, f"sha:{commit}", f"commit:{commit}", "current unversioned working tree"):
            with self.subTest(version=version):
                outcome = self.run_workflow(version=version, limits={"maxRounds": 1, "maxAgents": 2})
                self.assertEqual(outcome["result"]["status"], "complete", outcome["result"])
        for version in ("HEAD", "main", "2026-11-20", "ref:main", "refs/heads/main", "refs/tags/v1.0.0", "v1.2.3", "commit:abcdef"):
            with self.subTest(version=version):
                outcome = self.run_workflow(version=version, limits={"maxRounds": 1, "maxAgents": 2})
                self.assertEqual(outcome["result"]["status"], "blocked", outcome["result"])


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
