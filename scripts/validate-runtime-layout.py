#!/usr/bin/env python3
"""Validate the minimal runtime layout and documented install safeguards."""

from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RUNTIME = ("SKILL.md", "INDEX.md", "VERSION", "references")
REQUIRED_REFERENCE_FILES = (
    "references/target-repository.md",
    "references/mermaid.md",
)
REQUIRED_RUNTIME_GUIDANCE = (
    "read `references/target-repository.md`",
    "read `references/mermaid.md`",
)
README_FILES = (ROOT / "README.md", ROOT / "README.zh-CN.md")
REQUIRED_GUIDE_TEXT = (
    'npx skills add PINKIIILQWQ/oh-my-gh-writing -g',
    'staging="$(mktemp -d "$parent/.oh-my-gh-writing.new.XXXXXX")"',
    'git -C "$repo" sparse-checkout set --no-cone /SKILL.md /INDEX.md /VERSION /references/',
    'cp -R "$repo/SKILL.md" "$repo/INDEX.md" "$repo/VERSION" "$repo/references" "$staging/"',
    'test -f "$staging/VERSION"',
    'if [ -e "$target" ]; then',
    'mv "$target" "$backup"',
    'mv "$staging" "$target"',
)
README_LANGUAGE_TEXT = {
    "README.md": "copies the full repository",
    "README.zh-CN.md": "完整仓库",
}
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

    for name in REQUIRED_REFERENCE_FILES:
        if not (ROOT / name).is_file():
            fail(f"missing runtime reference {name}")

    if (ROOT / "agents").exists():
        fail("agents/ must not be part of the minimal runtime distribution")

    skill_text = (ROOT / "SKILL.md").read_text(encoding="utf-8").casefold()
    for needle in REQUIRED_RUNTIME_GUIDANCE:
        if needle.casefold() not in skill_text:
            fail(f"SKILL.md missing runtime guidance: {needle}")

    for readme in README_FILES:
        text = readme.read_text(encoding="utf-8")
        for needle in REQUIRED_GUIDE_TEXT:
            if needle not in text:
                fail(f"{readme.name} missing runtime install rule: {needle}")
        language_needle = README_LANGUAGE_TEXT[readme.name]
        if language_needle not in text:
            fail(f"{readme.name} missing full-repository install disclosure: {language_needle}")
        for needle in FORBIDDEN_GUIDE_TEXT:
            if needle in text:
                fail(f"{readme.name} contains non-runtime install content: {needle}")

    print("runtime layout and install guide are valid")


if __name__ == "__main__":
    main()
