#!/usr/bin/env python3
"""Validate that public release references match the runtime VERSION file."""

from __future__ import annotations

import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
VERSION_FILE = ROOT / "VERSION"
README_FILES = (ROOT / "README.md", ROOT / "README.zh-CN.md")
PACKAGE_REFERENCES = (
    "version-release.md",
    "project-launch.md",
    "contribution-setup.md",
    "bug-fix-workflow.md",
    "proposal-to-implementation.md",
    "breaking-change-package.md",
    "docs-overhaul.md",
)
VERSION_PATTERN = re.compile(r"(?:0|[1-9]\d*)\.(?:0|[1-9]\d*)\.(?:0|[1-9]\d*)")
MANIFEST_VERSION_LINE = "- Generator: `oh-my-gh-writing` version from `VERSION`."
UPDATE_COMMAND = "npx skills update oh-my-gh-writing -g"


def fail(message: str) -> None:
    raise SystemExit(f"release version validation failed: {message}")


def main() -> None:
    if not VERSION_FILE.is_file():
        fail("missing VERSION")

    version = VERSION_FILE.read_text(encoding="utf-8").strip()
    if not VERSION_PATTERN.fullmatch(version):
        fail("VERSION must contain only a semantic version such as 0.1.2")

    tag = f"v{version}"
    for readme in README_FILES:
        text = readme.read_text(encoding="utf-8")
        for needle in (f"Skill-{tag}", f"releases/tag/{tag}"):
            if needle not in text:
                fail(f"{readme.name} missing release reference: {needle}")
        if UPDATE_COMMAND not in text:
            fail(f"{readme.name} missing single-skill update command")

    changelog = (ROOT / "CHANGELOG.md").read_text(encoding="utf-8")
    if f"## [{version}]" not in changelog:
        fail(f"CHANGELOG.md missing release heading for {version}")

    skill = (ROOT / "SKILL.md").read_text(encoding="utf-8")
    if "`VERSION` is the local runtime version source." not in skill:
        fail("SKILL.md missing runtime version guidance")

    for name in PACKAGE_REFERENCES:
        text = (ROOT / "references" / name).read_text(encoding="utf-8")
        if MANIFEST_VERSION_LINE not in text:
            fail(f"references/{name} missing package manifest version rule")

    print(f"release version references are consistent: {tag}")


if __name__ == "__main__":
    main()
