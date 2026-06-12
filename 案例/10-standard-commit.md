# Standard Commit — 经典案例

---


> 格式：**Plain text**（`git commit -m` 字符串）

## 主案例

### 案例 1：semantic-release/semantic-release (21k⭐)

semantic-release 使用 Angular Commit Convention：

```
<type>(<scope>): <subject>
<BLANK LINE>
<body>
<BLANK LINE>
<footer>
```

**Release 规则：**

| Commit 消息 | Release 类型 |
|---|---|
| `fix(pencil): stop graphite breaking` | Patch (fix) |
| `feat(pencil): add 'graphiteWidth' option` | Minor (feature) |
| `BREAKING CHANGE:` in footer | Major (breaking) |
| `docs:`, `chore:`, `refactor:` | No release |

---

### 案例 2：nestjs/nest (70k⭐)

**格式：** `<type>(<scope>): <subject>`

**Type 可选值：** build, chore, ci, docs, feat, fix, perf, refactor, style, test, sample

**Scope：** common, core, microservices, express, fastify, websockets, testing...

**Subject 规则：** 祈使句现在时 + 首字母不大写 + 结尾不加句号。

**Footer：** `BREAKING CHANGE:` + 描述 | `Closes #` 引用。

---

### 案例 3：conventional-changelog/commitlint (17k⭐)

```
type(scope?): subject
```

**Type (Angular Convention)：** build, chore, ci, docs, feat, fix, perf, refactor, revert, style, test

**真实示例：**
```
chore: run tests on travis ci
fix(server): send cors headers
feat(blog): add comment section
```

---

## 补充案例

### 案例 4：commitizen/cz-cli (17.5k⭐)

交互式 commit 工具，提交时引导填写：
```
type(scope): subject
```
适配器系统（cz-conventional-changelog, cz-customizable, cz-git...）。

### 案例 5：conventional-changelog/conventional-changelog-angular (7.5k⭐)

Angular Commit Convention 完整定义：

- **Changelog type：** feat, fix, perf（出现于 changelog）
- **Non-changelog type：** build, ci, docs, style, refactor, test
- **Revert：** `revert: <header>` + `This reverts commit <hash>.`

### 案例 6：commitizen/cz-conventional-changelog (0.8k⭐)

| Type | Title | Description |
|---|---|---|
| feat | Features | A new feature |
| fix | Bug Fixes | A bug fix |
| docs | Documentation | Documentation only changes |
| style | Styles | Formatting only |
| refactor | Code Refactoring | Neither fixes bug nor adds feature |
| perf | Performance Improvements | A code change that improves performance |
| test | Tests | Adding missing tests |
| build | Build System | Changes to the build system |
| ci | Continuous Integration | CI config changes |
| chore | Chores | Other changes |

---

### 参考仓库链接

- https://github.com/semantic-release/semantic-release
- https://github.com/nestjs/nest
- https://github.com/conventional-changelog/commitlint
- https://github.com/commitizen/cz-cli
- https://github.com/conventional-changelog/conventional-changelog-angular
- https://github.com/commitizen/cz-conventional-changelog

> 收集日期：2026-06-12
