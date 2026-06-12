# Documentation PR — 经典案例

---


> 格式：**Markdown**（GitHub PR Template）

## 精细版（完整 PR 模板）

### 案例 1：ionic-team/ionic-framework (51k⭐)

**仓库：** https://github.com/ionic-team/ionic-framework
**PR 模板：** https://raw.githubusercontent.com/ionic-team/ionic-framework/main/.github/PULL_REQUEST_TEMPLATE.md

```markdown
Issue number: resolves #

<!-- Please do not submit updates to dependencies unless it fixes an issue. -->
<!-- Please try to limit your pull request to one type (bugfix, feature, etc). -->

## What is the current behavior?
<!-- Please describe the current behavior that you are modifying. -->

## What is the new behavior?
<!-- Please describe the behavior or changes that are being added by this PR. -->

-

## Does this introduce a breaking change?
- [ ] Yes
- [ ] No

## Other information
<!-- Any other information that is important to this PR such as screenshots of
     how the component looks before and after the change. -->
```

---

### 案例 2：DefinitelyTyped/DefinitelyTyped (49k⭐)

**仓库：** https://github.com/DefinitelyTyped/DefinitelyTyped
**PR 模板：** https://raw.githubusercontent.com/DefinitelyTyped/DefinitelyTyped/master/.github/PULL_REQUEST_TEMPLATE.md

TypeScript 类型定义的文档化 PR 模板，按操作类型分三类：

**通用 checklist：**
- [ ] Use a meaningful title
- [ ] Test the change in your own code
- [ ] Add or edit tests to reflect the change
- [ ] Follow the advice from the readme
- [ ] Run `pnpm test <package to test>`

**新增类型定义：**
- [ ] The package does not already provide its own types
- [ ] Match the npm package name
- [ ] Create it with `dts-gen --dt`
- [ ] Represents shape of module/library correctly
- [ ] `tsconfig.json` has `noImplicitAny`, `strictNullChecks`, `strictFunctionTypes`

**修改已有定义：**
- [ ] Provide a URL to documentation or source code for context

**删除声明：**
- [ ] If a package was never on Definitely Typed, no action needed

---

### 案例 3：git/git (53k⭐)

**仓库：** https://github.com/git/git
**PR 模板：** https://raw.githubusercontent.com/git/git/master/.github/PULL_REQUEST_TEMPLATE.md

```markdown
Thanks for taking the time to contribute to Git! Please be advised that the
Git community does not use github.com for their contributions. Instead, we use
a mailing list (git@vger.kernel.org) for code submissions, code reviews, and
bug reports. Nevertheless, you can use GitGitGadget to conveniently send your
Pull Requests commits to our mailing list.

For a single-commit pull request, please *leave the pull request description
empty*: your commit message itself should describe your changes.
```

**特点：** 特殊的工作流说明——Git 项目通过邮件列表而非 GitHub PR 进行审查。文档变更直接通过 commit message 描述。

---

## 普通版（简洁 PR 模板）

### 案例 4：angular/angular-cli (27k⭐)

**仓库：** https://github.com/angular/angular-cli
**PR 模板：** https://raw.githubusercontent.com/angular/angular-cli/main/.github/PULL_REQUEST_TEMPLATE.md

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

### 案例 5：forem/forem (22k⭐)

**仓库：** https://github.com/forem/forem
**PR 模板：** https://raw.githubusercontent.com/forem/forem/main/.github/PULL_REQUEST_TEMPLATE.md

```markdown
## What type of PR is this?
- [ ] Refactor / [ ] Feature / [ ] Bug Fix
- [ ] Optimization / [ ] Documentation Update

## Description

## Related Tickets & Documents
- Related Issue #
- Closes #

## QA Instructions, Screenshots, Recordings
```

### 案例 6：kubernetes/ingress-nginx (17k⭐)

**仓库：** https://github.com/kubernetes/ingress-nginx
**PR 模板：** https://raw.githubusercontent.com/kubernetes/ingress-nginx/main/.github/PULL_REQUEST_TEMPLATE.md

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

---

> 收集日期：2026-06-12
