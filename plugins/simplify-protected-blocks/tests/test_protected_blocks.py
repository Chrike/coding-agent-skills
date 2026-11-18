import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parents[1] / "hooks"))

import protected_blocks


class ProtectedBlockTests(unittest.TestCase):
    def test_filter_and_expand_preserve_block_and_surrounding_code(self):
        source = "before\n// simplify-ignore-start: reason\nsecret()\n// simplify-ignore-end\nafter\n"
        filtered, mapping, warnings = protected_blocks.filter_text(source)

        self.assertFalse(list(warnings))
        self.assertEqual(len(mapping), 1)
        self.assertIn("before\n", filtered)
        self.assertIn("after\n", filtered)
        self.assertNotIn("secret()", filtered)

        expanded, expand_warnings = protected_blocks.expand_text(filtered, mapping)
        self.assertFalse(list(expand_warnings))
        self.assertEqual(source, expanded)

    def test_missing_placeholder_keeps_original_backup_until_restore(self):
        originals = {
            "single": "before\n// simplify-ignore-start: keep one\nsecret_one()\n// simplify-ignore-end\nafter\n",
            "multiple": (
                "before\n// simplify-ignore-start: keep one\nsecret_one()\n// simplify-ignore-end\n"
                "middle\n// simplify-ignore-start: keep two\nsecret_two()\n// simplify-ignore-end\nafter\n"
            ),
        }
        for case, original in originals.items():
            with self.subTest(case=case), tempfile.TemporaryDirectory() as temporary:
                root = Path(temporary)
                path = root / "example.js"
                path.write_text(original, encoding="utf-8")
                protected_blocks.protect_file(root, path)

                state = protected_blocks.state_paths(root, path)
                self.assertIsNotNone(state)
                mapping = protected_blocks.load_mapping(state)
                self.assertTrue(mapping)
                placeholder = next(iter(mapping.values()))["placeholder"]
                with path.open("r", encoding="utf-8", newline="") as handle:
                    current = handle.read()
                self.assertIn(placeholder, current)
                with path.open("w", encoding="utf-8", newline="") as handle:
                    handle.write(current.replace(placeholder, "", 1))

                protected_blocks.update_file(root, path)

                self.assertEqual(original, state["backup"].read_text(encoding="utf-8"))
                protected_blocks.restore_all(root)
                self.assertEqual(original, path.read_text(encoding="utf-8"))
                self.assertFalse(state["backup"].exists())

    def test_unclosed_block_is_not_hidden(self):
        source = "before\n// simplify-ignore-start\nsecret()\n"
        filtered, mapping, warnings = protected_blocks.filter_text(source)

        self.assertEqual(source, filtered)
        self.assertFalse(mapping)
        self.assertTrue(list(warnings))

    def test_safe_path_rejects_outside_and_symlink_paths(self):
        with (
            tempfile.TemporaryDirectory() as temporary,
            tempfile.TemporaryDirectory() as outside_temporary,
        ):
            root = Path(temporary)
            inside = root / "inside.js"
            outside = Path(outside_temporary) / "outside.js"
            inside.write_text("x", encoding="utf-8")
            outside.write_text("x", encoding="utf-8")
            link = root / "link.js"
            try:
                link.symlink_to(outside)
            except (OSError, NotImplementedError):
                link = None

            self.assertIsNotNone(protected_blocks.safe_path(root, str(inside)))
            self.assertIsNone(protected_blocks.safe_path(root, str(outside)))
            if link is not None:
                self.assertIsNone(protected_blocks.safe_path(root, str(link)))


if __name__ == "__main__":
    unittest.main()
