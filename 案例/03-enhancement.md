# Enhancement — 经典案例

---

## 精细版（详尽模板）

### 案例 1：ansible/ansible (64k⭐) — Feature Idea（含 Enhancement）

ansible-core 的 Feature Idea 模板同时覆盖 enhancement 场景——改进已有功能而非新增能力。关键结构：

- **Summary** — 明确描述当前功能的不足
- **Component Name** — 要改进的具体模块
- **Additional Information** — before/after 对比、兼容性分析
- 要求提供当前 workaround 为什么不够好

> 完整内容见 `.github/ISSUE_TEMPLATE/feature_request.yml`

---

### 案例 2：hashicorp/consul (28k⭐) — Feature Request（含 Enhancement）

Consul 的模板直接支持 enhancement 类变更：

```markdown
#### Feature Description

A written overview of the feature and why this feature solves challenges
that you are facing today.

#### Use Case(s)

Describe the use case for this feature (i.e. Service Mesh, Service Discovery,
KV, API Gateway) and deployment environments (K8s, VMs, Nomad, ECS, Lambda).
```

enhancement 与 feature request 共用此模板，通过标签区分。

---

### 案例 3：prisma/prisma (43k⭐)

Prisma 的 Feature Request 模板同样适用于 enhancement：

- **Problem / Motivation** — 当前功能的限制或痛点
- **Suggested Solution** — 改进方案 + API 示例
- **Alternatives** — 已考虑的 workaround

典型的增量改进适用此模板。

> 完整内容：`.github/ISSUE_TEMPLATE/feature_request.yml`

---

## 普通版（较短模板）

### 案例 4：hashicorp/nomad (15k⭐)

**来源：** `.github/ISSUE_TEMPLATE/feature_request.md`

```markdown
---
name: Feature Request
about: If you have something you think Nomad could improve or add support for.
---

#### Feature Description

A written overview of the feature and why this feature solves challenges
that you are facing today.

#### Use Case(s)

Describe the use case for this feature and deployment environments
(K8s, VMs, Nomad, ECS, Lambda).
```

适用于 enhancement：改进已有功能时填写"当前不足 + 改进效果"。

---

### 案例 5：apache/echarts (62k⭐)

ECharts 的 enhancement 类 issue 通过 `[Feature]` 标签标识，但模板侧重"Motivation + API Design"：

- **What problem does this feature solve?** — 当前功能不足描述
- **What does the proposed API look like?** — 改进后的 API 设计

适合已有功能的 API 增强场景。

---

### 案例 6：jestjs/jest (45k⭐)

Jest 通过 Feature Proposal 标签处理 enhancement：

```yaml
- type: textarea
  attributes:
    label: '🚀 Feature Proposal'
    description: A clear and concise description of what the feature is.
  validations:
    required: true
- type: textarea
  attributes:
    label: Motivation
    description: Outline your motivation for the proposal.
  validations:
    required: true
- type: textarea
  attributes:
    label: Example
    description: Describe how this feature would be used.
```

> 完整内容：`.github/ISSUE_TEMPLATE/feature.yml`

---

> 收集日期：2026-06-12
