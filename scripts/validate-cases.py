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
CASE_INDEX = CASES / "README.md"
README_FILES = [
    ROOT / "README.md",
    ROOT / "README.zh-CN.md",
]

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
README_FORBIDDEN_LABELS = {
    "ROUTING_FAIL",
    "FORMAT_FAIL",
    "FACT_CHECK_REQUIRED",
    "DRAFT_ONLY",
}

ALLOWED_WITH_SKILL_SUFFIXES = {".md", ".yml", ".yaml"}
EXCERPT_TYPES = {"exact", "shortened", "paraphrased"}


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

    if not CASE_INDEX.is_file():
        fail("cases/README.md is missing")

    case_index_text = CASE_INDEX.read_text(encoding="utf-8")
    for case_dir in case_dirs:
        if f"`{case_dir.name}/`" not in case_index_text:
            fail(f"{case_dir.name}: missing from cases/README.md Current Cases table")

    current_match = re.search(r"^Current:\s*(\d+)\s+review-draft cases\.\s*$", case_index_text, re.MULTILINE)
    if not current_match:
        fail("cases/README.md missing Current case count")
    current_count = int(current_match.group(1))
    if current_count != len(case_dirs):
        fail(f"cases/README.md Current count is {current_count}, expected {len(case_dirs)}")

    for case_dir in case_dirs:
        names = {path.name for path in case_dir.iterdir() if path.is_file()}
        missing = sorted(REQUIRED - names)
        if missing:
            fail(f"{case_dir.name}: missing required files: {', '.join(missing)}")

        with_skill = sorted(name for name in names if name.startswith("with-skill."))
        if not with_skill:
            fail(f"{case_dir.name}: missing with-skill.md or with-skill.<target-extension>")
        unsupported = sorted(
            name for name in with_skill if Path(name).suffix not in ALLOWED_WITH_SKILL_SUFFIXES
        )
        if unsupported:
            fail(f"{case_dir.name}: unsupported with-skill suffix: {', '.join(unsupported)}")

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

    known_cases = {case_dir.name for case_dir in case_dirs}
    for readme in README_FILES:
        if not readme.is_file():
            continue
        text = readme.read_text(encoding="utf-8")
        referenced_cases = sorted(set(re.findall(r"cases/(\d{3}-[A-Za-z0-9_-]+)/?", text)))
        for case_name in referenced_cases:
            if case_name not in known_cases:
                fail(f"{readme.name}: references missing case {case_name}")
            attribution = (CASES / case_name / "attribution.md").read_text(encoding="utf-8")
            if "README citation status: allowed" not in attribution:
                fail(f"{case_name}: README citation is not explicitly allowed")
            grading = (CASES / case_name / "grading.md").read_text(encoding="utf-8")
            label_match = re.search(r"^Label:\s*([A-Z_]+)\s*$", grading, re.MULTILINE)
            if not label_match:
                fail(f"{case_name}: grading.md missing Label")
            if label_match.group(1) in README_FORBIDDEN_LABELS:
                fail(f"{case_name}: README must not cite label {label_match.group(1)}")
            excerpt_match = re.search(
                r"^- README excerpt type:\s*(exact|shortened|paraphrased)\.\s*$",
                grading,
                re.MULTILINE,
            )
            if not excerpt_match:
                allowed = ", ".join(sorted(EXCERPT_TYPES))
                fail(f"{case_name}: grading.md must declare README excerpt type ({allowed})")
            showcase_match = re.search(
                r"^- README showcase status:\s*approved\.\s*$",
                grading,
                re.MULTILINE,
            )
            if not showcase_match:
                fail(f"{case_name}: grading.md must declare approved README showcase status")

    print("case evidence fixtures are valid")


if __name__ == "__main__":
    main()
