import contextlib
import io
import json
import tempfile
import unittest
from pathlib import Path

import validate_suite as suite


class ValidateSuiteTests(unittest.TestCase):
    def setUp(self):
        self.original_skills = suite.SKILLS_DIR
        self.original_catalog = suite.CATALOG_FILE
        self.original_contracts = suite.CONTRACT_FILES
        self.temp_dir = tempfile.TemporaryDirectory()
        self.root = Path(self.temp_dir.name)
        suite.SKILLS_DIR = self.root / "skills"
        suite.CATALOG_FILE = self.root / "skills.sh.json"
        suite.CONTRACT_FILES = tuple(self.root / name for name in ("routing.md", "trigger.md", "negative.md"))

    def tearDown(self):
        suite.SKILLS_DIR = self.original_skills
        suite.CATALOG_FILE = self.original_catalog
        suite.CONTRACT_FILES = self.original_contracts
        self.temp_dir.cleanup()

    def write_skill(self, name, body=""):
        directory = suite.SKILLS_DIR / name
        directory.mkdir(parents=True, exist_ok=True)
        (directory / "SKILL.md").write_text(
            f"---\nname: {name}\ndescription: A maintained skill.\n---\n{body}",
            encoding="utf-8",
        )

    def test_frontmatter_and_local_links_are_checked(self):
        self.write_skill("alpha", "See [notes](notes.md).\n")
        (suite.SKILLS_DIR / "alpha" / "notes.md").write_text("notes\n", encoding="utf-8")
        errors, warnings = suite.validate_skills()
        self.assertEqual(errors, [])
        self.assertEqual(warnings, [])

    def test_catalog_reports_duplicates_unknowns_and_omissions(self):
        self.write_skill("alpha")
        self.write_skill("idea-refine")
        suite.CATALOG_FILE.write_text(
            json.dumps({"groupings": [{"skills": ["alpha", "alpha", "missing"]}]}),
            encoding="utf-8",
        )
        errors, warnings = suite.validate_catalog()
        self.assertIn("skills.sh.json: duplicate skill alpha", errors)
        self.assertIn("skills.sh.json: unknown skill missing", errors)
        self.assertIn("skills.sh.json: skill idea-refine is not in a presentation grouping", warnings)

    def test_strict_mode_fails_for_warnings(self):
        self.write_skill("alpha")
        suite.CATALOG_FILE.write_text(json.dumps({"groupings": [{"skills": []}]}), encoding="utf-8")
        for path in suite.CONTRACT_FILES:
            path.write_text("contract\n", encoding="utf-8")
        output = io.StringIO()
        with contextlib.redirect_stdout(output):
            result = suite.run(strict=True)
        self.assertEqual(result, 1)
        self.assertIn("FAILED: 1 error(s), 1 warning(s)", output.getvalue())


if __name__ == "__main__":
    unittest.main()
