---
scenario: Release Notes
mode: concise
case-sources: https://github.com/astral-sh/ruff, https://github.com/biomejs/biome
input-prompt: ../../prompts/14-release-notes.md
---

# zzz v2.0.0

## Highlights
- **Breaking:** Config format changed from JSON to YAML (`.zzzrc.json` → `.zzzrc.yaml`)
- **New:** Multi-environment profiles (`dev`, `staging`, `production`)
- **New:** Plugin system for custom countdown behaviors

## Breaking Changes
- `.zzzrc.json` no longer read by default. Rename to `.zzzrc.yaml` and
  convert JSON keys to YAML format
- `--profile` flag now uses `profiles/` directory instead of inline config

## New Features
- Environments: `zzz --env production 30 -- deploy.sh`
- Plugins: `zzz --plugin notify -- 10 -- echo done`
