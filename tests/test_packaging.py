"""Distribution checks; these do not measure model behavior."""

from pathlib import Path
import re
import shutil
import subprocess
import sys
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[1]
SKILLS = ("frame-agent-task", "execute-agent-task")


class PackagingTests(unittest.TestCase):
    def test_repository_contract_is_in_sync(self):
        result = subprocess.run(
            [sys.executable, str(ROOT / "scripts/sync_contract.py"), "--check"],
            capture_output=True, text=True,
        )
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_each_skill_has_self_contained_markdown_references(self):
        for name in SKILLS:
            with self.subTest(skill=name), tempfile.TemporaryDirectory() as temp:
                package = Path(temp) / name
                shutil.copytree(ROOT / "skills" / name, package)
                for document in package.rglob("*.md"):
                    links = re.findall(r"\[[^\]]*\]\(([^)]+)\)", document.read_text())
                    for link in links:
                        if "://" in link or link.startswith("#"):
                            continue
                        target = (document.parent / link.split("#", 1)[0]).resolve()
                        self.assertTrue(target.is_relative_to(package.resolve()), link)
                        self.assertTrue(target.exists(), f"Missing reference: {link}")

    def test_check_detects_drift_without_writing_and_sync_repairs_it(self):
        with tempfile.TemporaryDirectory() as temp:
            copy = Path(temp) / "repo"
            shutil.copytree(ROOT, copy, ignore=shutil.ignore_patterns(".git", "__pycache__"))
            contract = copy / "skills/frame-agent-task/references/task-contract.md"
            contract.write_text("Local drift\n")
            script = copy / "scripts/sync_contract.py"
            result = subprocess.run(
                [sys.executable, str(script), "--check"], capture_output=True, text=True,
            )
            self.assertNotEqual(result.returncode, 0)
            self.assertEqual(contract.read_text(), "Local drift\n")
            self.assertIn("frame-agent-task", result.stderr)
            repaired = subprocess.run(
                [sys.executable, str(script)], capture_output=True, text=True,
            )
            self.assertEqual(repaired.returncode, 0, repaired.stderr)
            second = copy / "skills/execute-agent-task/references/task-contract.md"
            self.assertEqual(contract.read_text(), second.read_text())
            self.assertIn((copy / "shared/task-contract.md").read_text(), contract.read_text())


if __name__ == "__main__":
    unittest.main()
