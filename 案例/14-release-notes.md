# Release Notes — 经典案例

---

## 精细版（完整发布公告）

### 案例 1：astral-sh/ruff (40k⭐)

**来源：** GitHub Releases

Ruff 的 Release Notes 结构（v0.9.0 示例）：

```markdown
## v0.9.0

### Highlights
**Breaking changes**
- Python 3.8 support dropped
- Deprecated `--format` CLI flag removed

**New rules**
- `ruff rule --generate-docs` generates docs for all rules
- New `flake8-tidy-imports` rules

### Changes
#### Configuration
- `[tool.ruff]` → `[tool.ruff.lint]` migration complete

#### Preview features
- `ruff format` supports Python 3.13 pattern matching
```

---

### 案例 2：biomejs/biome (20k⭐)

Biome 的 Release Notes 注重视觉呈现：

```
# vx.x.x
## Highlights
[GIF 演示新特性]
[代码示例 before/after]

## Breaking Changes
[迁移说明]

## Other Changes

## Contributors
@username1, @username2...

## Full Changelog
```

---

### 案例 3：NixOS/nix (12k⭐)

```markdown
# Nix 2.24 Release Notes

## Highlights
- New `nix profile` command
- Lazy trees feature (experimental)

## Breaking Changes
- `nix-env` deprecated
- `--no-link` removed

## New Features
- `nix build --json` includes drv path

## Improvements
- 25% faster evaluation

## Fixed
- `nix flake show` lock file handling
```

---

## 普通版（简洁发布注释）

### 案例 4：astral-sh/uv (35k⭐)

**结构：** Highlights → Breaking → Fixes → Full Changelog 三段式。

### 案例 5：zed-industries/zed (20k⭐)

**结构：** 幽默开场🎉 → 新功能列表 → Bug 修复 → 社区鸣谢。

### 案例 6：dagger/dagger (18k⭐)

**结构：** 🔥 Breaking → 🚀 New → ✨ Improvements → Full Changelog。每个功能附示例代码。

---

> 收集日期：2026-06-12
