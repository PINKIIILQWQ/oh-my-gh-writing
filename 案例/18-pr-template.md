# PR Template — 经典案例（完整原文）

> 格式：**Markdown**（GitHub PR 模板的强制格式）

---

## 精细版（完整 PR 模板原文）

### 案例 1：apache/flink (24k⭐)

**仓库：** https://github.com/apache/flink
**模板来源：** https://raw.githubusercontent.com/apache/flink/master/.github/PULL_REQUEST_TEMPLATE.md

```markdown
<!--
*Thank you very much for contributing to Apache Flink - we are happy that you want to help us improve Flink. *
*Please provide a description of your PR. Please also fill in the checklist below.*

*This template is a guideline, not a strict requirement - adapt it as needed.*
-->

## What is the purpose of the change

<!-- For example: Fixes #1234, provides a new feature, addresses a design issue, etc. -->

## Brief change log

<!-- Please describe the changes and how they were tested. -->

## Verifying this change

<!--
Please verify the change with a test:
- New test added (unit/integration/e2e)
- Existing tests cover the change
- Manual verification was done
-->

## Does this pull request potentially affect one of the following parts:

- Dependencies (does it add or upgrade a dependency): (yes / no)
- Public API (changes to public API): (yes / no)
- Runtime compatibility (changes that might break existing jobs): (yes / no)

## Documentation

- Does this pull request introduce a new feature? (yes / no)
- If yes, how is the documentation implemented? (not needed / markdown / javadoc)
```

**特点：** 4 大部分（Purpose / Changelog / Verification / Impact）+ 8 项 checklist，覆盖依赖/API/兼容性/文档。

---

### 案例 2：apache/rocketmq (21k⭐)

**仓库：** https://github.com/apache/rocketmq
**模板来源：** https://raw.githubusercontent.com/apache/rocketmq/master/.github/PULL_REQUEST_TEMPLATE.md

```markdown
<!-- Please make sure the target branch is right. In most case,
     the target branch should be `develop`. -->

## What is the purpose of the change

## Brief changelog

## Verifying this change

<!-- Follow this checklist to help us incorporate your contribution quickly: -->

- [ ] Make sure there is a [GitHub_issue](https://github.com/apache/rocketmq/issues)
      filed for the change (usually before you start working on it).
      Trivial changes like typos do not necessitate a GitHub issue.
- [ ] Each commit in the pull request should have a meaningful subject line and body.
- [ ] Format the pull request title according to our guidelines.
- [ ] Run `mvn clean install -DskipTests=false` to make sure unit tests pass.
- [ ] Add new unit tests if the change is new code.
- [ ] Make sure any change to the `conf` folder has corresponding documentation.
```

**特点：** 6 项 checklist + Maven 构建验证 + 强调每个 commit 质量 + 配置变更必须带文档。

---

### 案例 3：kubernetes/kompose (9k⭐)

**仓库：** https://github.com/kubernetes/kompose
**模板来源：** https://raw.githubusercontent.com/kubernetes/kompose/main/.github/PULL_REQUEST_TEMPLATE.md

```markdown
#### What type of PR is this?

<!--
Add one of the following kinds:
/kind bug
/kind cleanup
/kind enhancement
/kind documentation
/kind feature

Optionally add one or more of the following kinds if applicable:
/kind api-change
/kind deprecation
/kind failing-test
/kind flake
/kind regression
-->

#### What this PR does / why we need it:

#### Which issue this PR fixes:

#### Special notes for your reviewer:

#### Does this PR introduce a user-facing change?

<!--
If no, just write "NONE" in the release-note block below.
If yes, a release note is required:
-->

```release-note
```

#### Additional documentation
```

**特点：** Kubernetes 社区的 `/kind` 标签系统 + release note 区块 + 审查者备注。

---

## 简洁写法（简洁 PR 模板）

### 案例 4：Homebrew/brew (42k⭐)

**仓库：** https://github.com/Homebrew/brew
**模板来源：** https://raw.githubusercontent.com/Homebrew/brew/master/.github/PULL_REQUEST_TEMPLATE.md

```markdown
- [ ] Have you followed the guidelines in our Contributing document?
- [ ] Have you checked to ensure there aren't other open PRs for the same change?
- [ ] Have you added an explanation of what your changes do and why?
- [ ] Have you written new tests for your changes?
- [ ] Have you successfully run `brew lgtm` with your changes locally?
- [ ] AI was used to generate or assist with generating this PR.
```

**特点：** 6 项简洁 checklist + AI 披露 + 一键验证命令。

### 案例 5：docker/compose (34k⭐)

**仓库：** https://github.com/docker/compose
**模板来源：** https://raw.githubusercontent.com/docker/compose/main/.github/PULL_REQUEST_TEMPLATE.md

```markdown
**What I did**

**Related issue**
<!-- If this is a bug fix, make sure your description includes
     "fixes #xxxx", or "closes #xxxx" -->

**(not mandatory) A picture of a cute animal, if possible in relation to what you did**
```

**特点：** 3 字段极简 + Docker 标志性可爱动物文化。

### 案例 6：microsoft/terminal (96k⭐)

**仓库：** https://github.com/microsoft/terminal
**模板来源：** https://raw.githubusercontent.com/microsoft/terminal/main/.github/PULL_REQUEST_TEMPLATE.md

```markdown
## Summary of the Pull Request

## References and Relevant Issues

## Detailed Description of the Pull Request / Additional comments

## Validation Steps Performed

## PR Checklist
- [ ] Closes #xxx
- [ ] Tests added/passed
- [ ] Documentation updated
- [ ] Schema updated (if necessary)
```

---

### 参考仓库链接

- https://github.com/apache/flink — `.github/PULL_REQUEST_TEMPLATE.md`
- https://github.com/apache/rocketmq — `.github/PULL_REQUEST_TEMPLATE.md`
- https://github.com/kubernetes/kompose — `.github/PULL_REQUEST_TEMPLATE.md`
- https://github.com/Homebrew/brew — `.github/PULL_REQUEST_TEMPLATE.md`
- https://github.com/docker/compose — `.github/PULL_REQUEST_TEMPLATE.md`
- https://github.com/microsoft/terminal — `.github/PULL_REQUEST_TEMPLATE.md`

---

> 收集日期：2026-06-12
