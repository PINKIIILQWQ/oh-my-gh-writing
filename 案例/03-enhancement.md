# Enhancement — 经典案例

---

## 精细版（详尽模板）

### 案例 1：kubernetes/community (3k⭐)

KEP（Kubernetes Enhancement Proposal）是最系统的 enhancement 流程之一：

```
KEP Template:
- Summary (1-2句提案核心)
- Motivation (当前不足 + 用户故事)
- Design Details (完整设计)
- Test Plan (测试策略)
- Graduation Criteria (Alpha → Beta → Stable)
- Production Readiness Review
```

特点：书级文档（5k-10k词），Provisional → Implementable → Implemented 三阶段审查制。

---

### 案例 2：django/django (80k⭐)

Django 通过 Trac Ticket 管理 enhancement，模板结构：

```
Current behavior:
Expected behavior:
Use case:
Implementation suggestion:
Backwards compatibility:
```

特点：Ticket 驱动的渐进式改进，每个 issue 必须有清晰 use case + 兼容性分析。

---

### 案例 3：jekyll/jekyll (50k⭐)

Jekyll enhancement 模板：

```markdown
### Why
[当前功能不足，用户痛点]

### How
[改进后的行为，含代码示例]

### Alternatives
[已考虑的备选方案]

### Backwards compatibility
[对已有配置/主题的影响]
```

---

## 普通版（较短模板）

### 案例 4：Netflix/zuul (14k⭐)

Zuul 的 enhancement 通过 GitHub Issues：

```markdown
## Current Behavior
## Proposed Behavior
## Compatibility
```

---

### 案例 5：apache/cassandra (9k⭐)

Cassandra 通过 JIRA 管理 enhancement：

```
Description:
Motivation:
Changes:
```

JIRA 标签：`improvement` / `new feature`

---

### 案例 6：cloudfoundry/cli (3k⭐)

Cloud Foundry CLI 使用 `enhancement` label：

```markdown
## Problem
## Solution
## Alternatives
```

---

> 收集日期：2026-06-12
