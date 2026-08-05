import contextlib
import io
import unittest

import check_routing_contract as routing


class RoutingContractTests(unittest.TestCase):
    def test_unresolved_slug_tokens_are_reported(self):
        self.assertEqual(
            routing.unresolved_slug_tokens("`unknown-owner` `code-review`", {"known-owner"}),
            {"unknown-owner"},
        )

    def test_lexical_overlap_is_informational_data(self):
        overlaps = routing.lexical_overlaps(
            {"one-owner": "Build stable module boundaries contract", "two-owner": "Build stable API boundaries contract"}
        )
        self.assertEqual(overlaps, [("one-owner", "two-owner", ["boundaries", "contract", "stable"])])

    def test_current_contract_passes_without_ranking_gate(self):
        output = io.StringIO()
        with contextlib.redirect_stdout(output):
            result = routing.run()
        self.assertEqual(result, 0)
        self.assertIn("PASSED: 0 error(s)", output.getvalue())

    def test_security_review_boundary_is_bilingual(self):
        english = routing.README_FILE.read_text(encoding="utf-8")
        chinese = (routing.ROOT / "README.zh-CN.md").read_text(encoding="utf-8")
        contract = routing.ROUTING_FILE.read_text(encoding="utf-8")

        self.assertIn("current-diff vulnerability review", english)
        self.assertIn("当前 diff 的漏洞审查", chinese)
        self.assertIn("current-diff vulnerability review", contract)


if __name__ == "__main__":
    unittest.main()
