# Release Notes — 经典案例

---

## 精细版（完整发布公告）

### 案例 1：astral-sh/ruff (40k⭐)

**来源：** GitHub Releases（v0.9.0）

Ruff 的 Release Notes 采用 Highlights + 分类详情的结构：

```markdown
## v0.9.0

### Highlights

**Breaking changes**
- Python 3.8 support has been dropped
- The deprecated `--format` CLI flag has been removed

**New rules**
- `ruff rule --generate-docs` now generates documentation for all rules
- New `flake8-tidy-imports` rules (TID251, TID252)

### Changes

#### Configuration
- `[tool.ruff]` → `[tool.ruff.lint]` migration complete
- New `exclude` default patterns added

#### Preview features
- `ruff format` now supports Python 3.13 pattern matching

## Contributors

Thanks to @alice, @bob, @charlie!
```

**特点：** Breaking Changes 前置 → New Features 居中 → 分类变更 → 贡献者致谢。

---

### 案例 2：biomejs/biome (20k⭐)

Biome 的 Release Notes 强调视觉效果和社区参与：

- 版本号 + 发布日期为 H1
- Highlights 放在最前（含 GIF 演示）
- Breaking Changes 单独章节 + 迁移说明
- 每个新特性带代码示例（before/after）
- 贡献者致谢列表
- Full Changelog 链接指向 GitHub

**结构模板：**
```
# vx.x.x

## Highlights

### Feature name
[GIF/description]
[code example]

## Breaking Changes
- Description + migration steps

## Other Changes
- ...

## Contributors
@username1, @username2...

## Full Changelog
https://github.com/.../vx.x.x
```

---

### 案例 3：NixOS/nix (12k⭐)

Nix 的 Release Notes 采用用户导向结构：

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
- `builtins.fetchTree` supports Git LFS

## Improvements
- Performance: 25% faster evaluation
- Memory: 30% less allocation

## Fixed
- `nix flake show` lock file handling
- macOS sandbox compatibility
```

---

## 普通版（简洁发布注释）

### 案例 4：astral-sh/uv (35k⭐)

uv 的 Release Notes 采用列表式+分类：

```markdown
# v0.6.0

## Highlights
- New `uv tool` interface for running tools
- `uv add` supports `--raw-sources`

## Breaking
- Minimum Python 3.9

## Fixes
- Resolution with git dependencies
- Lock file format v2

## Full Changelog
```

**特点：** Highlights → Breaking → Fixes 三段式，每条变更一句话+PR 链接。

---

### 案例 5：zed-industries/zed (20k⭐)

Zed 的 Release 公告结合社区特色：

- 幽默开场（表情符）
- 新功能列表（每个带简短描述）
- Bug 修复列表
- 社区贡献鸣谢

```markdown
# Zed v0.150.0 🎉

## What's new
- Inline git blame
- Vim mode improvements
- New rust-analyzer features

## Fixes
- Crashes on large files
- Theme reloading

## Thank you
@contributor1, @contributor2
```

---

### 案例 6：dagger/dagger (18k⭐)

Dagger 的 Release Notes 突出用户可见变更：

- 每个新功能附 `dagger call` 示例代码
- Breaking 变更含迁移代码片段
- 升级指南链接

**示例结构：**
```markdown
## 🔥 Breaking
- `dagger.json` format v2 migration

## 🚀 New
- `dagger develop` now generates client libraries

## ✨ Improvements
- Module loading 40% faster

## Full Changelog
```

---

> 收集日期：2026-06-12
