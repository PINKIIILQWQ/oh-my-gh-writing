# Documentation PR — 经典案例

---

## 精细版（完整 PR 模板）

### 案例 1：ionic-team/ionic-framework (51k⭐)

**来源：** `.github/PULL_REQUEST_TEMPLATE.md`

```markdown
Issue number: resolves #

<!-- Please try to limit your pull request to one type (bugfix, feature, etc). -->

## What is the current behavior?

## What is the new behavior?

## Does this introduce a breaking change?
- [ ] Yes
- [ ] No

## Other information

Screenshots of how the component looks before and after the change.
```

**特点：** 行为对比（before/after）+ breaking change 标注 + 截图建议，适合 UI 框架的文档 PR。

---

### 案例 2：DefinitelyTyped/DefinitelyTyped (49k⭐)

**来源：** `.github/PULL_REQUEST_TEMPLATE.md`

TypeScript 类型定义的文档化 PR 模板，按操作类型分三类：

**新增类型定义：**
- [ ] 包不提供自己的类型，无法通过 `--declaration` 生成
- [ ] 名称匹配 npm 包名
- [ ] 使用 `dts-gen --dt` 创建
- [ ] `tsconfig.json` 包含 `noImplicitAny`、`strictNullChecks` 等

**修改已有定义：**
- [ ] 提供文档或源码 URL 作为变更上下文

**删除声明：**
- [ ] 确认包不在 Definitely Typed 上

**特点：** 按操作类型（新增/修改/删除）分流的 checklist，减少维护者沟通成本。

---

### 案例 3：git/git (53k⭐)

**来源：** `.github/PULL_REQUEST_TEMPLATE.md`

```markdown
Thanks for taking the time to contribute to Git! Please be advised that the
Git community does not use github.com for their contributions. Instead, we use
a mailing list (git@vger.kernel.org) for code submissions, code reviews, and
bug reports.

For a single-commit pull request, please *leave the pull request description
empty*: your commit message itself should describe your changes.
```

**特点：** 特殊的工作流说明——Git 项目通过邮件列表而非 GitHub PR 进行代码审查。PR 只作为镜像。

---

## 普通版（较短模板）

### 案例 4：angular/angular-cli (27k⭐)

**来源：** `.github/PULL_REQUEST_TEMPLATE.md`

```markdown
## PR Checklist
- [ ] The commit message follows our guidelines
- [ ] Tests for the changes have been added
- [ ] Docs have been added / updated

## PR Type
- [ ] Bugfix / [ ] Feature / [ ] Code style update
- [ ] Refactoring / [ ] Build / [ ] CI / [ ] Documentation content changes

## What is the current behavior?
Issue Number: N/A

## What is the new behavior?

## Does this PR introduce a breaking change?
- [ ] Yes / [ ] No
```

**特点：** 6 种 PR Type 分类，文档变更有明确 `Documentation content changes` 选项。

---

### 案例 5：forem/forem (22k⭐)

**来源：** `.github/PULL_REQUEST_TEMPLATE.md`

```markdown
## What type of PR is this?
- [ ] Refactor / [ ] Feature / [ ] Bug Fix / [ ] Optimization / [ ] Documentation Update

## Description

## Related Tickets & Documents
- Related Issue #
- Closes #

## QA Instructions, Screenshots, Recordings
```

**特点：** 5 种 PR 类型 + QA 截图/录制要求，适合 UI 密集型社区平台。

---

### 案例 6：kubernetes/ingress-nginx (17k⭐)

**来源：** `.github/PULL_REQUEST_TEMPLATE.md`

```markdown
## What this PR does / why we need it:

## Types of changes
- [ ] Bug fix / [ ] New feature / [ ] CVE Report
- [ ] Breaking change / [ ] Documentation only

## Which issue/s this PR fixes

## How Has This Been Tested?

## Checklist:
- [ ] My change requires a change to the documentation.
- [ ] I have updated the documentation accordingly.
```

**特点：** `Documentation only` 类型 + 文档变更联动检查，Kubernetes 项目的工业化流程。

---

> 收集日期：2026-06-12
