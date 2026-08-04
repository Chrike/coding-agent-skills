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

    def test_unclosed_block_is_not_hidden(self):
        source = "before\n// simplify-ignore-start\nsecret()\n"
        filtered, mapping, warnings = protected_blocks.filter_text(source)

        self.assertEqual(source, filtered)
        self.assertFalse(mapping)
        self.assertTrue(list(warnings))

    def test_safe_path_rejects_outside_and_symlink_paths(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            inside = root / "inside.js"
            outside = root.parent / "outside.js"
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
