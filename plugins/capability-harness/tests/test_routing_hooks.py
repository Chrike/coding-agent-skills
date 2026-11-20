from __future__ import annotations

import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest


PLUGIN_ROOT = Path(__file__).resolve().parents[1]
USER_PROMPT_HOOK = PLUGIN_ROOT / "hooks" / "user_prompt_submit.py"


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
        hook_output = output.get("hookSpecificOutput")
        self.assertIsInstance(hook_output, dict)
        assert isinstance(hook_output, dict)
        return str(hook_output["additionalContext"])

    def test_all_other_nonempty_requests_get_the_same_fixed_prompt(self) -> None:
        prompts = (
            "Fix a typo in this file.",
            "What is the latest release of this package?",
            "Design an unfamiliar product architecture with unresolved trade-offs.",
            "Please summarize this text; no-search, no-network, and no-agent.",
            "这段代码有什么问题？",
        )
        contexts = [self.context_for(prompt) for prompt in prompts]
        self.assertEqual(len(set(contexts)), 1)

        context = contexts[0]
        lines = context.splitlines()
        self.assertGreaterEqual(len(lines), 5)
        self.assertLessEqual(len(lines), 8)
        self.assertTrue(all(line.startswith("- ") for line in lines[1:]))
        for route in ("Direct:", "Project inspection:", "evidence-researcher", "context-scout"):
            with self.subTest(route=route):
                self.assertIn(route, context)
        self.assertIn("briefly state your route and why", context)
        self.assertIn("at most one route", context)
        self.assertIn("Honor explicit no-search, no-network, and no-agent limits", context)
        for private_data in ("private prompts", "project data", "source code", "identifiers", "secrets"):
            with self.subTest(private_data=private_data):
                self.assertIn(private_data, context)
        self.assertIn("external services", context)

    def test_unquoted_opt_out_silences_prompt_hook(self) -> None:
        for prompt in (
            "Fix this project change. [harness:off]",
            "Fix this project change [HaRnEsS:OfF].",
        ):
            with self.subTest(prompt=prompt):
                self.assertIsNone(self.submit(prompt))

    def test_marker_inside_quotes_backticks_or_fenced_code_does_not_disable(self) -> None:
        literals = (
            '"[harness:off]"',
            "'[harness:off]'",
            "“[harness:off]”",
            "‘[harness:off]’",
            "`[harness:off]`",
            "``[harness:off]``",
            "```text\n[harness:off]\n```",
            "~~~text\n[harness:off]\n~~~",
        )
        for literal in literals:
            with self.subTest(literal=literal):
                context = self.context_for(
                    f"Explain this ordinary request; the literal is documentation:\n{literal}\nContinue with the answer."
                )
                self.assertIn("briefly state your route and why", context)

    def test_unquoted_marker_after_quoted_or_fenced_literal_still_disables(self) -> None:
        for prompt in (
            'Explain the literal "[harness:off]" and then disable [harness:off].',
            "```text\n[harness:off]\n```\n[harness:off]",
        ):
            with self.subTest(prompt=prompt):
                self.assertIsNone(self.submit(prompt))

    def test_embedded_marker_is_not_a_standalone_opt_out(self) -> None:
        self.assertIsNotNone(self.submit("Explain the text prefix[harness:off]suffix in this example."))

    def test_only_exact_pure_greetings_are_silent(self) -> None:
        for greeting in ("hi", "HELLO!", "Hey.", "thanks", "Thank you!", "okay", "你好。", "谢谢！"):
            with self.subTest(greeting=greeting):
                self.assertIsNone(self.submit(greeting))

        for request in ("hello there", "thanks for the help; now explain this", "yes, please continue"):
            with self.subTest(request=request):
                self.assertIsNotNone(self.submit(request))

    def test_known_host_commands_are_silent_only_at_the_start(self) -> None:
        for command in (
            "/security-review",
            "  /security-review this change",
            "/code-review --help",
            "/adaptive-long-horizon improve this plan",
        ):
            with self.subTest(command=command):
                self.assertIsNone(self.submit(command))

        for request in (
            "Please run /security-review on this PR.",
            "The /code-review command would help.",
            "/security-review/report.md is the relevant file.",
            "/docs/review-guide.md",
            "/unknown-command do something",
        ):
            with self.subTest(request=request):
                self.assertIsNotNone(self.submit(request))

    def test_empty_or_malformed_input_is_silent(self) -> None:
        for payload in ("", "  \n", "not-json", "[]", "null"):
            with self.subTest(payload=payload):
                self.assertIsNone(self.run_hook(payload))

    def test_prompt_hook_creates_no_runtime_state(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            output = self.submit("Implement a small change in the current project.", cwd=directory)
            self.assertIsNotNone(output)
            self.assertEqual(list(Path(directory).iterdir()), [])


if __name__ == "__main__":
    unittest.main()
