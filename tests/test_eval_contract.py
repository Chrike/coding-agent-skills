import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CONTRACT = ROOT / "tests" / "eval-contract.md"


class EvalContractTests(unittest.TestCase):
    def test_contract_defines_three_evidence_tiers(self):
        text = CONTRACT.read_text(encoding="utf-8")
        self.assertIn("### Tier 1: deterministic structure", text)
        self.assertIn("### Tier 2: routing contract", text)
        self.assertIn("### Tier 3: behavior and runtime evidence", text)
        for state in ("complete", "failed", "blocked", "skipped", "unverified"):
            self.assertIn(f"`{state}`", text)

    def test_contract_keeps_ownerless_cases_out_of_catalog(self):
        text = CONTRACT.read_text(encoding="utf-8")
        self.assertIn("ownerless negative cases", text)
        self.assertIn("ownerless negative remains explicitly out of catalog", text)
        self.assertIn("stale owner-like tokens", text)

    def test_contract_keeps_high_side_effect_evidence_out_of_ordinary_maintenance(self):
        text = CONTRACT.read_text(encoding="utf-8").lower()
        for marker in (
            "headless-agent executors",
            "browser cases",
            "network fetches",
            "hosted ci",
            "external graders",
            "evals/results",
        ):
            self.assertIn(marker, text)


if __name__ == "__main__":
    unittest.main()
