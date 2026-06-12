# Standard Commit — 经典案例

---

## 精细版（完整 Commit 规范）

### 案例 1：semantic-release/semantic-release (21k⭐)

**来源：** https://github.com/semantic-release/semantic-release

semantic-release 使用 Angular Commit Message Conventions 自动确定版本号：

**Commit 类型与 Release 映射：**

| Commit 消息 | Release 类型 |
|---|---|
| `fix(pencil): stop graphite breaking when too much pressure applied` | Patch Release (fix) |
| `feat(pencil): add 'graphiteWidth' option` | Minor Release (feature) |
| `feat(pencil): remove graphiteWidth option` + `BREAKING CHANGE:` in footer | Major Release (breaking) |

**Commit 格式：**
```
<type>(<scope>): <subject>
<BLANK LINE>
<body>
<BLANK LINE>
<footer>
```

**默认 Release 规则：**
- `fix:` → Patch release
- `feat:` → Feature release
- `BREAKING CHANGE:` in footer → Major release
- `docs:`, `chore:`, `style:`, `refactor:`, `test:` → No release

---

### 案例 2：nestjs/nest (70k⭐)

**来源：** https://github.com/nestjs/nest

NestJS 的 Commit 消息规范：

**格式：**
```
<type>(<scope>): <subject>
<BLANK LINE>
<body>
<BLANK LINE>
<footer>
```

**Type（必选其一）：** `build`, `chore`, `ci`, `docs`, `feat`, `fix`, `perf`, `refactor`, `style`, `test`, `sample`

**Scope（受影响的包）：** `common`, `core`, `sample`, `microservices`, `express`, `fastify`, `socket.io`, `ws`, `testing`, `websockets`
- 多 scope 可用逗号分隔（如 `common,core`）
- 异常：`packaging`, `changelog`, `sample/#` 或空

**Subject 规则：**
- 祈使句现在时（"change" 而非 "changed" 或 "changes"）
- 首字母不大写
- 结尾不加句号

**Body：** 动机说明 + 与之前行为的对比

**Footer：**
- `BREAKING CHANGE:` 后跟描述
- `Closes #` 引用关闭的 issue

---

### 案例 3：conventional-changelog/commitlint (17k⭐)

**来源：** https://github.com/conventional-changelog/commitlint

Commitlint 定义的标准提交模式：

**格式：**
```
type(scope?): subject  # scope 可选
```

**常见 Type（Angular Convention）：**
`build`, `chore`, `ci`, `docs`, `feat`, `fix`, `perf`, `refactor`, `revert`, `style`, `test`

**真实示例：**
```
chore: run tests on travis ci
fix(server): send cors headers
feat(blog): add comment section
```

**配置方式：** `.commitlintrc` / `commitlint.config.js` / `package.json` 中的 `commitlint` 字段

---

## 普通版（Commit 工具/指南）

### 案例 4：commitizen/cz-cli (17.5k⭐)

**来源：** https://github.com/commitizen/cz-cli

Commitizen 是一个交互式 commit 工具，在提交时引导开发者：

```json
{
  "path": "cz-conventional-changelog",
  "disableScopeLowerCase": false,
  "disableSubjectLowerCase": false,
  "maxHeaderWidth": 100,
  "maxLineWidth": 100,
  "defaultType": "",
  "defaultScope": "",
  "defaultSubject": "",
  "defaultBody": "",
  "defaultIssues": ""
}
```

**Type 定义：**
- `feat`: A new feature
- `fix`: A bug fix
- `docs`: Documentation only changes
- `style`: Formatting changes
- `refactor`: Code change that neither fixes a bug nor adds a feature
- `perf`: Performance improvement
- `test`: Adding missing tests
- `build`: Build system changes
- `ci`: CI configuration changes
- `chore`: Other changes that don't modify src or test files

---

### 案例 5：conventional-changelog/conventional-changelog-angular (7.5k⭐)

Angular Commit Convention 定义：

```
<type>(<scope>): <subject>
<BLANK LINE>
<body>
<BLANK LINE>
<footer>
```

**Changelog 中的 type：** `feat`, `fix`, `perf` 出现在 changelog 中；`BREAKING CHANGE` 总是出现
**非 changelog type：** `build`, `ci`, `docs`, `style`, `refactor`, `test`

**Footer 中的 BREAKING CHANGE：**
```
BREAKING CHANGE: The graphiteWidth option has been removed.
```

**Revert 格式：**
```
revert: feat(pencil): add 'graphiteWidth' option
This reverts commit 667ecc1654a317a13331b17617d973392f415f02.
```

---

### 案例 6：commitizen/cz-conventional-changelog (0.8k⭐)

cz-cz-conventional-changelog 的 Type 定义与描述映射：

| Type | Title | Description |
|---|---|---|
| feat | Features | A new feature |
| fix | Bug Fixes | A bug fix |
| docs | Documentation | Documentation only changes |
| style | Styles | Formatting only |
| refactor | Code Refactoring | Neither fixes bug nor adds feature |
| perf | Performance Improvements | Performance improvement |
| test | Tests | Adding missing tests |
| build | Build System | Build system changes |
| ci | Continuous Integration | CI config changes |
| chore | Chores | Other changes |
| revert | Reverts | Reverts a previous commit |

---

> 收集日期：2026-06-12
