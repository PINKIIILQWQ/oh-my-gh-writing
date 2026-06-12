# Feature Request — 经典案例

---


> 格式：**YAML**（GitHub Issue Form）

## 精细版（完整模板）

### 案例 1：apache/dubbo (40k⭐)

**仓库：** https://github.com/apache/dubbo
**模板来源：** https://raw.githubusercontent.com/apache/dubbo/main/.github/ISSUE_TEMPLATE/feature_request.yaml

Apache Dubbo 的 Feature Request YAML 模板：

```yaml
name: Feature Request
description: Suggest an idea for Apache Dubbo
title: "[Feature] "
labels: ["kind/enhancement"]
body:
  - type: textarea
    attributes:
      label: Feature Description
      description: A clear and concise description of the feature
    validations:
      required: true
  - type: textarea
    attributes:
      label: Motivation
      description: Why is this feature needed? What problem does it solve?
    validations:
      required: true
  - type: textarea
    attributes:
      label: Alternative Solutions
      description: Workarounds or alternatives considered and why they are insufficient
    validations:
      required: false
```

---

### 案例 2：microsoft/typescript (100k⭐)

**仓库：** https://github.com/microsoft/typescript

TypeScript 使用著名的建议模板：

```markdown
## Search Terms
[搜索关键词]

## Suggestion
[一句话描述建议]

## Use Cases
[详细用例，含代码示例]

## Examples
[期望的 API 用法示例]

## Checklist
- [ ] My suggestion meets these guidelines
- [ ] I've checked existing issues
```

每个 Use Case 都详细描述用户操作流程，API 草案常用 TypeScript 类型签名。Playground Link 用于运行示例代码。

---

### 案例 3：apache/hadoop (15k⭐)

**仓库：** https://github.com/apache/hadoop

Hadoop Feature Request 通过 JIRA 管理，模板：

```markdown
## Feature Description
A written overview of the feature.

## Use Case(s)
Describe the use case(s) and deployment environments.

## Proposed API
If applicable, describe the proposed API changes.

## Compatibility
Impact on existing features and backward compatibility.
```

---

## 简洁写法（较短模板）

### 案例 4：grafana/grafana (66k⭐)

**仓库：** https://github.com/grafana/grafana

Grafana 的 Feature Request 风格：

```markdown
#### What would you like to be added?

#### Why is this needed?

#### Describe the solution you'd like
```

---

### 案例 5：apache/rocketmq (see 18-pr-template) (21k⭐)

**仓库：** https://github.com/apache/rocketmq (see 18-pr-template)

RocketMQ 通过 RIP（RocketMQ Improvement Proposal）流程：

```
## Motivation
## Proposed Change
## Compatibility, Deprecation, and Migration Plan
## Rejected Alternatives
```

---

### 案例 6：apache/spark (40k⭐)

**仓库：** https://github.com/apache/spark

Spark 的 Feature Request 通过 JIRA + 邮件列表：

```
## Problem Description
## Proposed Solution
## Alternative Solutions
## Compatibility Impact
```

---

> 收集日期：2026-06-12
