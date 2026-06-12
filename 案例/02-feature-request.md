# Feature Request — 经典案例

---

## 精细版（完整 YAML/模板）

### 案例 1：prisma/prisma (43k⭐)

**来源：** `.github/ISSUE_TEMPLATE/feature_request.yml`

```yaml
name: Feature Request
description: Suggest an idea for Prisma
title: "[Feature]: "
labels: ["kind/feature"]
body:
  - type: markdown
    attributes:
      value: |
        Thanks for suggesting a feature! Please describe what you'd like to see added.
  - type: textarea
    id: problem
    attributes:
      label: Problem / Motivation
      description: What problem are you trying to solve? Why is this feature needed?
      placeholder: I'm always frustrated when...
    validations:
      required: true
  - type: textarea
    id: solution
    attributes:
      label: Suggested Solution
      description: What would you like to see implemented? Provide API examples if possible.
      placeholder: I'd like to be able to...
    validations:
      required: true
  - type: textarea
    id: alternatives
    attributes:
      label: Alternatives
      description: What workarounds have you considered?
    validations:
      required: false
```

---

### 案例 2：apache/echarts (62k⭐)

**来源：** `.github/ISSUE_TEMPLATE/feature_request.yml`

```yaml
name: Feature Request
description: Request a new feature from Apache ECharts
title: "[Feature] "
labels: [new-feature]
body:
- type: markdown
  attributes:
    value: |
      The issue list is reserved exclusively for bug reports and feature requests.
      For usage questions, please use [docs](https://echarts.apache.org/option.html)
      or [Stack Overflow](https://stackoverflow.com/questions/tagged/echarts)
- type: textarea
  attributes:
    label: What problem does this feature solve?
    description: |
      Explain your use case, context, and rationale behind this feature request. 
      More importantly, what is the end user experience you are trying to build?
      
      An important design goal of ECharts is keeping the API surface small.
      We only consider adding new features that solve a problem that cannot be 
      easily dealt with using existing APIs.
  validations:
    required: true
- type: textarea
  attributes:
    label: What does the proposed API look like?
    description: |
      Describe how you propose to solve the problem and provide code samples 
      of how the API would work once implemented.
  validations:
    required: true
```

**特点：** 双字段极简但深刻——"解决问题"+"API 设计"，强制提案者思考方案而非只提需求。

---

### 案例 3：ansible/ansible (64k⭐)

**来源：** `.github/ISSUE_TEMPLATE/feature_request.yml`

Ansible 的 Feature Request 由 bot 驱动，必填字段：

1. **Summary** (textarea, required) — 描述新功能/改进、解决什么问题、当前无法实现什么
2. **Issue Type** (dropdown, 固定 Feature Idea)
3. **Component Name** (input, required) — 模块/插件/任务名称
4. **Additional Information** (textarea, required) — 如何使用、为什么需要、解决什么
5. **Code of Conduct** (checkbox, required)

**特点：** 前置范围检查（core vs collection），XKCD 链接警示"每个变更都会破坏某些人的工作流"，要求搜索已有请求。

> 完整 URL：https://github.com/ansible/ansible/blob/devel/.github/ISSUE_TEMPLATE/feature_request.yml

---

## 普通版（较短的模板）

### 案例 4：jestjs/jest (45k⭐)

**来源：** `.github/ISSUE_TEMPLATE/feature.yml`

```yaml
name: Feature Proposal 🚀
title: '[Feature]: '
labels: [':rocket: Feature Request']
body:
  - type: textarea
    id: description
    attributes:
      label: '🚀 Feature Proposal'
      description: A clear and concise description of what the feature is.
    validations:
      required: true
  - type: textarea
    id: solution
    attributes:
      label: Motivation
      description: Outline your motivation for the proposal. How will it make Jest better?
    validations:
      required: true
  - type: textarea
    id: alternatives
    attributes:
      label: Example
      description: Describe how this feature would be used.
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

**特点：** 4 字段 + 明确说明哪些提案不会被 core 接受（新 matchers → jest-extended；reporter 变更 → 自定义 reporter）。

---

### 案例 5：hashicorp/nomad (15k⭐)

**来源：** `.github/ISSUE_TEMPLATE/feature_request.md`

```markdown
---
name: Feature Request
about: If you have something you think Nomad could improve or add support for.
---

#### Feature Description

A written overview of the feature and why it solves challenges you're facing today.

#### Use Case(s)

Describe the use case for this feature and deployment environments 
(K8s, VMs, Nomad, ECS, Lambda).
```

**特点：** 极简 2 段式——功能描述 + 用例场景，HashiCorp 系列标准模板。

---

### 案例 6：hashicorp/consul (28k⭐)

**来源：** `.github/ISSUE_TEMPLATE/feature_request.md`

```markdown
---
name: Feature Request
about: If you have something you think Consul could improve or add support for.
---

<!--- Please search the existing issues for relevant feature requests,
      and use the reaction feature to add upvotes to pre-existing requests. --->

#### Feature Description

A written overview of the feature and why this feature solves challenges
that you are facing today.

#### Use Case(s)

Describe the use case for this feature (i.e. Service Mesh, Service Discovery,
KV, API Gateway) and deployment environments (K8s, VMs, Nomad, ECS, Lambda).
```

**特点：** 明确要求先搜索已有请求 + 使用 reaction 投票，减噪机制好。

---

> 收集日期：2026-06-12
