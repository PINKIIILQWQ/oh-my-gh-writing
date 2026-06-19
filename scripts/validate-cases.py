#!/usr/bin/env python3
"""Validate public case evidence structure.

This intentionally avoids third-party dependencies. It checks file layout and
review metadata, not Markdown or YAML semantic correctness.
"""

from __future__ import annotations

import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CASES = ROOT / "cases"

REQUIRED = {
    "input.md",
    "source.md",
    "baseline-summary.md",
    "grading.md",
    "attribution.md",
}

LABELS = {
    "PASS",
    "PASS_AFTER_CLEANUP",
    "ROUTING_FAIL",
    "FORMAT_FAIL",
    "FACT_CHECK_REQUIRED",
    "DRAFT_ONLY",
}


def fail(message: str) -> None:
    raise SystemExit(f"case validation failed: {message}")


def main() -> None:
    if not CASES.is_dir():
        fail("cases/ directory is missing")

    case_dirs = sorted(
        path for path in CASES.iterdir() if path.is_dir() and re.match(r"^\d{3}-", path.name)
    )
    if not case_dirs:
        fail("no numbered case directories found")

    for case_dir in case_dirs:
        names = {path.name for path in case_dir.iterdir() if path.is_file()}
        missing = sorted(REQUIRED - names)
        if missing:
            fail(f"{case_dir.name}: missing required files: {', '.join(missing)}")

        with_skill = sorted(name for name in names if name.startswith("with-skill."))
        if not with_skill:
            fail(f"{case_dir.name}: missing with-skill.md or with-skill.<target-extension>")

        grading = (case_dir / "grading.md").read_text(encoding="utf-8")
        match = re.search(r"^Label:\s*([A-Z_]+)\s*$", grading, re.MULTILINE)
        if not match:
            fail(f"{case_dir.name}: grading.md missing Label")
        label = match.group(1)
        if label not in LABELS:
            fail(f"{case_dir.name}: unsupported grading label {label!r}")

        baseline = (case_dir / "baseline-summary.md").read_text(encoding="utf-8")
        if "Status: TODO" in baseline and label == "PASS":
            fail(f"{case_dir.name}: baseline is TODO, so label must not be PASS")

    print("case evidence fixtures are valid")


if __name__ == "__main__":
    main()
