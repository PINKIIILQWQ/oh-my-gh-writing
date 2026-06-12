# PR Template — 经典案例

---

## 精细版（完整 PR 模板）

### 案例 1：apache/flink (24k⭐)

**来源：** `.github/PULL_REQUEST_TEMPLATE.md`

```markdown
<!--
*Thank you very much for contributing to Apache Flink - we are happy to receive your PR!*

Please provide a description of your PR. Please also fill in the checklist below.
This template is a guideline, not a strict requirement - adapt it as needed.
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

**特点：** Apache Flink 工业化 PR 模板——4 大部分 + 8 项 checklist，覆盖依赖/API/兼容性/文档，适合大型分布式系统项目。

---

### 案例 2：apache/rocketmq (21k⭐)

**来源：** `.github/PULL_REQUEST_TEMPLATE.md`

```markdown
## What is the purpose of the change

## Brief changelog

## Verifying this change
<!-- Follow this checklist to help us incorporate your contribution quickly and easily: -->

- [ ] Make sure there is a [GitHub_issue](https://github.com/apache/rocketmq/issues) filed for the change.
- [ ] Each commit in the pull request should have a meaningful subject line and body.
- [ ] Format the pull request title according to our guidelines.
- [ ] Run `mvn clean install -DskipTests=false` to make sure unit tests pass.
- [ ] Add new unit tests if the change is new code.
- [ ] Make sure any change to the `conf` folder has corresponding documentation.
```

**特点：** 6 项 checklist + Maven 构建验证 + 强调每个 commit 的 subject 和 body 质量。

---

### 案例 3：kubernetes/kompose (9k⭐)

**来源：** `.github/PULL_REQUEST_TEMPLATE.md`

```markdown
<!-- Description of the change and what it does. -->

## Proposed changes

- [ ] Bug fix (non-breaking)
- [ ] New feature (non-breaking)
- [ ] Breaking change
- [ ] Documentation change
- [ ] Refactor

## Verification

<!-- Steps to verify the changes. -->

## Additional information

<!-- Any other context. -->
```

**特点：** Kubernetes 家族的标准化 PR 分类 + 验证步骤。

---

## 普通版（简洁 PR 模板）

### 案例 4：freeCodeCamp/freeCodeCamp (412k⭐)

**字段：** 4 项 checklist（贡献指南 + PR 指南 + main 分支 + 本地测试）+ `Closes #XXXXX`

### 案例 5：microsoft/terminal (96k⭐)

**字段：** Summary → References → Description → Validation → Checklist（close/tests/docs/schema）

### 案例 6：docker/compose (34k⭐)

**字段：** `What I did` + `Related issue` + `(optional) A picture of a cute animal`

**特点：** Docker 标志性文化——可爱的动物图，降低 PR 提交的心理门槛。

---

> 收集日期：2026-06-12
