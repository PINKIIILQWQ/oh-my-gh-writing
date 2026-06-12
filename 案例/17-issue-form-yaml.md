# Issue Form YAML — 经典案例

---

## 精细版（完整 YAML 表单）

### 案例 1：jestjs/jest (45k⭐) — bug.yml

**来源：** `.github/ISSUE_TEMPLATE/bug.yml`

```yaml
name: Bug Report 🪲
description: Create a bug report to help us improve
title: '[Bug]: '
labels: ['Bug Report', 'Needs Triage']
body:
  - type: markdown
    attributes:
      value: |
        # Please follow these steps first:
        ## Troubleshoot
        If Jest is not behaving the way you expect, we'd ask you to look at the
        [documentation](https://jestjs.io/docs/getting-started) and search the issue tracker.
        
        ## Ask for help through appropriate channels
        Consider [StackOverflow](https://stackoverflow.com/questions/ask) or our
        [Discord channel](https://discord.gg/j6FKKQQrW9).
        
        ## Make a minimal reproduction
        Bug reports without a minimal reproduction will be rejected.
  - type: input
    id: version
    attributes:
      label: Version
      placeholder: ex. 27.0.6
    validations:
      required: true
  - type: textarea
    id: reproduction
    attributes:
      label: Steps to reproduce
      description: Link to a repository with a minimal reproduction.
      placeholder: |
        1. Clone my repo at https://github.com/<myuser>/example
        2. yarn install
        3. yarn test
    validations:
      required: true
  - type: textarea
    id: expected
    attributes:
      label: Expected behavior
    validations:
      required: true
  - type: textarea
    id: what-happened
    attributes:
      label: Actual behavior
    validations:
      required: true
  - type: textarea
    id: envinfo
    attributes:
      label: Environment
      description: Run `npx envinfo --preset jest`
      render: shell
    validations:
      required: true
```

**特点：** 7 字段 + 多层引导 markdown + 强制最小可重现 + 自动环境采集。

---

### 案例 2：jestjs/jest (45k⭐) — feature.yml

```yaml
name: Feature Proposal 🚀
title: '[Feature]: '
labels: [':rocket: Feature Request']
body:
  - type: textarea
    id: description
    attributes:
      label: '🚀 Feature Proposal'
    validations:
      required: true
  - type: textarea
    id: solution
    attributes:
      label: Motivation
    validations:
      required: true
  - type: textarea
    id: alternatives
    attributes:
      label: Example
    validations:
      required: false
  - type: textarea
    id: extra
    attributes:
      label: Pitch
      description: Why does this feature belong in the Jest core platform?
    validations:
      required: true
```

---

### 案例 3：apache/echarts (62k⭐) — bug_report.yml

```yaml
name: Bug Report
description: Report a bug to Apache ECharts
title: "[Bug] "
labels: [bug]
body:
- type: markdown
  attributes:
    value: |
      For usage questions, please use [docs](https://echarts.apache.org/option.html)
      or [Stack Overflow](https://stackoverflow.com/questions/tagged/echarts)
- type: input
  attributes:
    label: Version
    placeholder: e.g. 5.2.2
  validations:
    required: true
- type: input
  attributes:
    label: Link to Minimal Reproduction
    description: Provide a link to CodeSandbox, JSFiddle, or GitHub repo.
  validations:
    required: true
- type: textarea
  attributes:
    label: Steps to Reproduce
  validations:
    required: true
- type: textarea
  attributes:
    label: Current Behavior
  validations:
    required: true
- type: textarea
  attributes:
    label: Expected Behavior
  validations:
    required: true
- type: textarea
  attributes:
    label: Environment
    value: |
      - OS:
      - Browser:
      - Framework:
    render: markdown
```

**特点：** 7 字段 + 在线编辑器链接必填 + 环境字段预填格式。

---

## 普通版（精简 YAML 表单）

### 案例 4：prisma/prisma (43k⭐) — bug_report.yml

**字段：** Description (req) → Reproduction (req) → Logs → Environment (req) → Additional checks (checkbox)

**特点：** 极简 5 字段 + 完整验证。

### 案例 5：ansible/ansible (64k⭐) — bug_report.yml

**字段（10 个）：** Summary → Issue Type (dropdown/Bug Report) → Component Name → Ansible Version → Configuration → OS/Environment → Steps → Expected → Actual → Code of Conduct

**特点：** bot 驱动、预填命令、全必填。

### 案例 6：hashicorp/nomad (15k⭐) — bug_report.md

**Markdown 格式，非 YAML：**

```markdown
---
name: Bug Report
about: You're experiencing an issue different than documented.
---

#### Overview of the Issue

#### Reproduction Steps

#### Nomad info for both Client and Server

#### Operating system and Environment details

#### Log Fragments
```

---

> 收集日期：2026-06-12
