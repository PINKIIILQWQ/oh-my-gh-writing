# CHANGELOG — 经典案例

---

## 精细版（完整变更日志）

### 案例 1：psf/requests (54k⭐) — HISTORY.md

Requests 使用 RST 格式 + Keep a Changelog 风格：

```rst
Release History
===============

2.34.2 (2026-05-14)
-------------------
- Moved `headers` input type back to `Mapping`.

2.34.1 (2026-05-13)
-------------------
**Bugfixes**
- Widened `json` input type from `dict` and `list` to `Mapping`.
- `Response.reason` moved from `str | None` to `str`.

2.34.0 (2026-05-11)
-------------------
**Announcements**
- Requests 2.34.0 introduces inline types.
**Improvements**
- Digest Auth hashing added `usedforsecurity=False`.
**Bugfixes**
- `Response.history` no longer contains a reference to itself.
```

---

### 案例 2：facebook/jest (45k⭐) — CHANGELOG.md

```markdown
## main
### Features
- `[@jest/expect-utils]` Add `mockFn.whenCalledWith(...args)`.
### Fixes
- `[expect]` Widen `toMatchObject` parameter type.
### Chore & Maintenance
- `[jest-haste-map]` Drop `walker` dependency.

## 30.4.2
### Fixes
- `[jest-runtime]` Fix named imports from CJS modules.
```

特点：Markdown + `[package-name]` 前缀 + 三级分类 + PR #链接 + `main` 作为未发布版本。

---

### 案例 3：hashicorp/vagrant (27k⭐) — CHANGELOG.md

```markdown
## 2.4.10.dev (UNRELEASED)

FEATURES:
- provider/virtualbox: Add support for LSI Logic SAS [GH-13692]

IMPROVEMENTS:
- provisioner/ansible: Add dynamic inventory selection [GH-13740]

BUG FIXES:
- core: Fix missing translations [GH-13747]
```

特点：大写分类（FEATURES/IMPROVEMENTS/BUG FIXES）+ `[GH-xxxxx]` 引用 + UNRELEASED 标记。

---

### 附加参考

**twbs/bootstrap (170k⭐)** — CHANGELOG.md 语义版本分类，Breaking changes 高亮。
**npm/cli (25k⭐)** — 混合风格：版本+日期+分类，合并次要变更减少噪声。
**astral-sh/ruff (78k⭐)** — 简洁但完整，每个版本含 Features / Fixes / Notes。
**denoland/deno (110k⭐)** — 涵盖所有 LTS 版本的完整 changelog，SemVer 严格。

---

## 普通版（简洁变更日志）

### 案例 4：material-components/material-web (10k⭐)

```markdown
## [2.4.1](compare/v2.4.0...v2.4.1) (2025-10-27)
### Bug Fixes
* **radio:** move root assignment to mirror hostDisconnected ([adb8d10])
* **tokens:** migrated to `versions/v*` ([60c0cfa])
```

特点：自动生成 + 版本间 diff 链接 + 组件作用域标签 + commit hash 链接。

---

### 案例 5：h5bp/html5-boilerplate (57k⭐)

```markdown
## 9.0.1 (April 11, 2024)
- Fixed tests on Windows, adds Windows Testing Action [#3110]
- Upgrade to Gulp 5 [#3100]

## 9.0.0 (December 6, 2023)
- Drop Normalize.css [#2960]
- Farewell Internet Explorer! [#2773]
```

特点：极简无序列表 + `[#NNNN]` 引用 + 大版本戏剧性标注。

---

### 案例 6：pallets/flask (69k⭐) — CHANGES.rst

```rst
Version 3.2.0
-------------
- Drop support for Python 3.9. :pr:`5730`
- ``redirect`` returns ``303`` by default. :issue:`5895`

Version 3.1.3
-------------
Released 2026-02-18
- Session marked as accessed for ``in`` and ``len``. :ghsa:`68rp-wp8r-4726`
```

特点：RST + `:pr:` / `:issue:` / `:ghsa:` 角色引用 + 发布日期单独行。

---

> 收集日期：2026-06-12
