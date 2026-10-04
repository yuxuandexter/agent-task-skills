#!/usr/bin/env python3
"""Package one canonical task contract inside each independently usable skill."""

import argparse
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[1]
SKILLS = ("frame-agent-task", "execute-agent-task")
NOTICE = "<!-- Generated from shared/task-contract.md; edit the canonical source. -->\n\n"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="Check without writing")
    args = parser.parse_args()
    expected = NOTICE + (ROOT / "shared/task-contract.md").read_text(encoding="utf-8")
    mismatches = []
    for skill in SKILLS:
        target = ROOT / "skills" / skill / "references/task-contract.md"
        actual = target.read_text(encoding="utf-8") if target.exists() else None
        if actual == expected:
            continue
        if args.check:
            mismatches.append(str(target.relative_to(ROOT)))
        else:
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_text(expected, encoding="utf-8")
            print(f"Updated {target.relative_to(ROOT)}")
    if mismatches:
        print("Contract copies differ: " + ", ".join(mismatches), file=sys.stderr)
        return 1
    print("Contract copies match the canonical source.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
