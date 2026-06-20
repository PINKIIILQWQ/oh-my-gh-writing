#!/usr/bin/env python3
"""Validate the minimal runtime layout and documented install safeguards."""

from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RUNTIME = ("SKILL.md", "INDEX.md", "references")
README_FILES = (ROOT / "README.md", ROOT / "README.zh-CN.md")
REQUIRED_GUIDE_TEXT = (
    'git clone --depth 1 --filter=blob:none --sparse https://github.com/PINKIIILQWQ/oh-my-gh-writing.git "$target"',
    'git -C "$target" sparse-checkout set --no-cone /SKILL.md /INDEX.md /references/',
    'rm -rf "$target/.git"',
    'staging="$(mktemp -d "$parent/.oh-my-gh-writing.new.XXXXXX")"',
    'git -C "$repo" sparse-checkout set --no-cone /SKILL.md /INDEX.md /references/',
    'cp -R "$repo/SKILL.md" "$repo/INDEX.md" "$repo/references" "$staging/"',
    'if [ -e "$target" ]; then',
    'mv "$target" "$backup"',
    'mv "$staging" "$target"',
)
FORBIDDEN_GUIDE_TEXT = (
    'rm -rf "$target"',
    '$repo/agents',
    '$repo/assets',
    '/agents/ /assets/',
)


def fail(message: str) -> None:
    raise SystemExit(f"runtime validation failed: {message}")


def main() -> None:
    for name in RUNTIME:
        if not (ROOT / name).exists():
            fail(f"missing runtime entry {name}")

    if (ROOT / "agents").exists():
        fail("agents/ must not be part of the minimal runtime distribution")

    for readme in README_FILES:
        text = readme.read_text(encoding="utf-8")
        for needle in REQUIRED_GUIDE_TEXT:
            if needle not in text:
                fail(f"{readme.name} missing runtime install rule: {needle}")
        for needle in FORBIDDEN_GUIDE_TEXT:
            if needle in text:
                fail(f"{readme.name} contains non-runtime install content: {needle}")

    print("runtime layout and install guide are valid")


if __name__ == "__main__":
    main()
