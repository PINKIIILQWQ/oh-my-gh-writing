# Enhancement — 经典案例

---

## 精细版（详尽 Enhancement 模板）

### 案例 1：kubernetes/community (10k⭐)

**仓库：** https://github.com/kubernetes/community
**KEP 模板：** https://raw.githubusercontent.com/kubernetes/enhancements/master/keps/NNNN-kep-template/README.md

KEP（Kubernetes Enhancement Proposal）是最系统化的 enhancement 流程之一，每个 KEP 包含：

```
# KEP-NNNN: Your Enhancement Proposal Title

## Summary
[1-2 句提案核心——方便其他人快速判断是否相关]

## Motivation
### User Stories
- 作为 [用户角色]，我想要 [能力]，以便 [收益]
- 作为 [用户角色]，我想要 [能力]，以便 [收益]

### Goals
- [明确的范围目标，KEP 完成时要达成的具体结果]

### Non-Goals
- [明确的不在范围内事项，避免 scope creep]

## Design Details
[详细设计，含 API 签名、数据结构、流程图]

## Test Plan
[单元测试、集成测试、端到端测试策略]

## Graduation Criteria
- Alpha: [基础功能 + feature gate]
- Beta: [性能测试 + 用户反馈]
- Stable: [生产验证 + 文档完备]

## Production Readiness Review
[可观测性、回滚方案、安全影响分析]
```

**特点：** 书级文档（5k-10k 词），Provisional → Implementable → Implemented → Rejected 四阶段状态流转，每个 stage 有明确验收标准。

---

### 案例 2：django/django (80k⭐)

**仓库：** https://github.com/django/django
**Trac Ticket 系统：** https://code.djangoproject.com

Django 通过 Trac Ticket 管理 enhancement，模板结构：

```
## Current behavior
[当前功能的不足或限制]

## Expected behavior
[改进后的行为]

## Use case
[具体的使用场景和用户故事]

## Implementation suggestion
[可选——对实现方式的初步想法]

## Backwards compatibility
[对现有 API 的破坏程度分析]
```

**特点：** 每个 enhancement 必须附带清晰 use case + 兼容性分析，否则会被关闭。Ticket 驱动的渐进式改进流程。

---

### 案例 3：jekyll/jekyll (50k⭐)

**仓库：** https://github.com/jekyll/jekyll
**Issues：** https://github.com/jekyll/jekyll/issues

Jekyll 的 enhancement 模板：

```markdown
### Why
[当前功能不足，用户痛点。为什么这个改进是必要的？]

### How
[改进后的行为，含具体配置或代码示例]
```yaml
# 改进后的配置示例
```

### Alternatives
[已考虑的备选方案及不采纳原因]

### Backwards compatibility
[对已有配置/主题/插件的影响]
```

---

## 普通版（简洁 Enhancement）

### 案例 4：Netflix/zuul (14k⭐)

**仓库：** https://github.com/Netflix/zuul

Zuul 的 enhancement 通过 GitHub Issues：

```markdown
## Current Behavior
## Proposed Behavior  
## Compatibility
```

### 案例 5：apache/cassandra (9k⭐)

**仓库：** https://github.com/apache/cassandra

Cassandra 通过 JIRA 管理 enhancement：

```
Description: [改进描述]
Motivation: [为什么需要这个改进]
Changes: [具体实现变更]
```

### 案例 6：cloudfoundry/cli (3k⭐)

**仓库：** https://github.com/cloudfoundry/cli

Cloud Foundry CLI 使用 `enhancement` label：

```markdown
## Problem
[当前 CLI 的不足]

## Solution
[建议的改进方案]

## Alternatives
[其他考虑过的方案]
```

---

> 收集日期：2026-06-12
