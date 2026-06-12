# CHANGELOG — 经典案例

---

## 精细版（完整变更日志）

### 案例 1：psf/requests (54k⭐) — HISTORY.md

**来源：** https://raw.githubusercontent.com/psf/requests/main/HISTORY.md

Requests 使用 `HISTORY.md` 作为 changelog，Keep a Changelog 风格：

```markdown
Release History
===============

2.34.2 (2026-05-14)
-------------------
- Moved `headers` input type back to `Mapping`.

2.34.1 (2026-05-13)
-------------------
**Bugfixes**
- Widened `json` input type from `dict` and `list` to `Mapping` and `Sequence`.
- Changed `headers` input type to MutableMapping.
- `Response.reason` moved from `str | None` to `str`.

2.34.0 (2026-05-11)
-------------------
**Announcements**
- Requests 2.34.0 introduces inline types, replacing those provided by typeshed.

**Improvements**
- Digest Auth hashing algorithms added `usedforsecurity=False`.
- Requests added support for Python 3.15 based on beta1.
- Requests added support for Python 3.14t.

**Bugfixes**
- `Response.history` no longer contains a reference to itself.
- Requests no longer performs greedy matching on no_proxy domains.
```

**特点：** RST 格式 + 分类（Announcements / Improvements / Bugfixes / Security）+ 版本/日期行 + 清晰标题。

---

### 案例 2：facebook/jest (45k⭐) — CHANGELOG.md

**来源：** https://raw.githubusercontent.com/facebook/jest/main/CHANGELOG.md

```markdown
## main

### Features
- `[@jest/expect-utils, jest-mock]` Add `mockFn.whenCalledWith(...args)`.
- `[jest-resolve]` Bump `unrs-resolver` to 1.12.1.

### Fixes
- `[expect]` Widen `toMatchObject` parameter type.

### Chore & Maintenance
- `[jest-haste-map]` Refactor massive class into multiple files.
- `[jest-haste-map]` Drop `walker` dependency; replace with `fdir`.

## 30.4.2

### Fixes
- `[jest-runtime]` Fix named imports from CJS modules.

## 30.4.1

### Features
- `[jest-config]` Allow custom runner configuration options via tuple format.

### Fixes
- `[jest-runtime]` Align CJS-from-ESM default export with Node.
```

**特点：** Markdown 格式 + `[package-name]` 前缀 + 三级分类（Features / Fixes / Chore & Maintenance）+ `main` 作为未发布版本标题+ PR #链接。

---

### 案例 3：hashicorp/vagrant (27k⭐) — CHANGELOG.md

**来源：** https://raw.githubusercontent.com/hashicorp/vagrant/main/CHANGELOG.md

```markdown
## 2.4.10.dev (UNRELEASED)

FEATURES:
- provider/virtualbox: Add support for LSI Logic SAS storage controller [GH-13692]

IMPROVEMENTS:
- provisioner/ansible: Add support for dynamically selecting ansible-playbook
  inventory argument [GH-13740]

BUG FIXES:
- core: Fix issue with missing translations [GH-13747]
- provider/hyperv: Preserve primary disk when resizing disks [GH-13748]

## 2.4.9 (August 21, 2025)

FEATURES:
- provider/virtualbox: Add support for VirtualBox 7.2 [GH-13709]

BUG FIXES:
- provisioner/ansible: Fix OS version detection [GH-13701]
```

**特点：** 大写的分类标题（FEATURES / IMPROVEMENTS / BUG FIXES）+ `[GH-xxxxx]` 引用格式 + `UNRELEASED` 标记 + 英文日期格式。

---

## 普通版（变更日志）

### 案例 4：material-components/material-web (10k⭐)

```markdown
# Changelog

## [2.4.1](https://github.com/.../v2.4.0...v2.4.1) (2025-10-27)

### Bug Fixes
* **radio:** also move sibling uncheck logic ([6010e52])
* **tokens:** `@material/web/tokens/v*` moved ([60c0cfa])

## [2.4.0](https://github.com/.../v2.3.0...v2.4.0) (2025-08-21)

### Features
* **button:** add disabled link support ([c3c4848])
```

**特点：** 自动生成 changelog（`conventional-changelog` 工具链）+ 版本间 diff 链接 + 组件作用域标签（`**radio:**`）+ commit hash 链接。

---

### 案例 5：h5bp/html5-boilerplate (57k⭐)

```markdown
# Changelog

## 9.0.1 (April 11, 2024)
- Fixed tests on Windows, adds Windows Testing Action [#3110]
- Upgrade to Gulp 5 [#3100]

## 9.0.0 (December 6, 2023)
- Removing tile images [#3023]
- Drop Normalize.css [#2960]
- Farewell Internet Explorer! [#2773]
```

**特点：** 极简无序列表 + `[#NNNN]` 引用 + 大版本有戏剧性标注（"Farewell Internet Explorer!"）。

---

### 案例 6：pallets/flask (69k⭐) — CHANGES.rst

```rst
Version 3.2.0
-------------
- Drop support for Python 3.9. :pr:`5730`
- ``redirect`` returns a ``303`` status code by default. :issue:`5895`

Version 3.1.3
-------------
Released 2026-02-18
- The session is marked as accessed for operations that only access
  the keys. :ghsa:`68rp-wp8r-4726`

Version 3.1.2
-------------
Released 2025-08-19
- ``stream_with_context`` does not fail inside async views. :issue:`5774`
```

**特点：** RST 格式 + `:pr:` / `:issue:` / `:ghsa:` 角色引用 + 发布日期单独行 + 简洁分类。

---

> 收集日期：2026-06-12
