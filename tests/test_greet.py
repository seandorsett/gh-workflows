import subprocess
import sys
import unittest
from pathlib import Path

SCRIPT = Path(__file__).resolve().parents[1] / "src" / "greet.py"


def run_cli(*args):
    return subprocess.run(
        [sys.executable, str(SCRIPT), *args],
        capture_output=True,
        text=True,
    )


class GreetCliTests(unittest.TestCase):
    def test_default_greeting(self):
        result = run_cli()
        self.assertEqual(result.returncode, 0)
        self.assertEqual(result.stdout, "Hello, World!\n")

    def test_custom_recipient(self):
        result = run_cli("--recipient", "Ada")
        self.assertEqual(result.returncode, 0)
        self.assertEqual(result.stdout, "Hello, Ada!\n")

    def test_help_lists_recipient_option(self):
        result = run_cli("--help")
        self.assertEqual(result.returncode, 0)
        self.assertIn("--recipient", result.stdout)

    def test_unknown_argument_fails(self):
        result = run_cli("--bogus")
        self.assertEqual(result.returncode, 2)
        self.assertIn("unrecognized arguments", result.stderr)

    def test_missing_recipient_value_fails(self):
        result = run_cli("--recipient")
        self.assertEqual(result.returncode, 2)
        self.assertEqual(result.stdout, "")


if __name__ == "__main__":
    unittest.main()
