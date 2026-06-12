# Discussion — 经典案例

---

## 精细版（完整 Discussion 框架）

### 案例 1：mozilla/rr (10k⭐)

**仓库：** https://github.com/mozilla/rr
**Discussions：** https://github.com/mozilla/rr/discussions

rr 项目的 Discussion 模板聚焦技术设计讨论，适用于功能方向讨论：

```markdown
### Problem
[当前系统的问题或限制。描述你在使用 rr 时遇到的具体障碍]

### Proposed Solution
[提议的方案。尽可能详细，含伪代码或架构变更示意]

### Alternatives Considered
[其他被考虑的方案及不选择的理由]
1. [方案 A] - [被拒绝的原因]
2. [方案 B] - [不选择的原因]

### Open Questions
[尚未确定的点，需要社区输入]
1. [问题 1]
2. [问题 2]
```

---

### 案例 2：jenkinsci/jenkins (23k⭐)

**仓库：** https://github.com/jenkinsci/jenkins
**JIRA：** https://issues.jenkins.io

Jenkins 通过 JIRA + 邮件列表 + GitHub Discussions 进行社区讨论：

```
## [DISCUSS] 讨论标题

### Background
[当前状况和背景信息。为什么需要讨论？]

### Proposal
[具体提案]
- 动机
- 方案细节
- 影响范围

### Open questions
[需要社区回答的问题]

### Vote
[讨论结束后的投票决定]
[ ] +1 (同意)
[ ] +0 (中立)
[ ] -1 (反对及理由)
```

---

### 案例 3：chef/chef (8k⭐)

**仓库：** https://github.com/chef/chef
**RFC 仓库：** https://github.com/chef/chef-rfc

Chef 的 RFC 讨论流程结构：

```markdown
## Motivation
[为什么需要这个变更？当前的问题是什么？]

## Specification
[详细的规范描述，含行为变更说明]

## Compatibility
[向后兼容性分析]
- 对现有 API 的影响
- 对已有配置的影响
- 迁移路径

## Rollback
[如果实施后发现问题，如何回滚]

## Reference Implementation
[参考实现的链接或关键代码片段]
```

---

## 普通版（简洁 Discussion 框架）

### 案例 4：hashicorp/vault (35k⭐)

**仓库：** https://github.com/hashicorp/vault

Vault 的 Feature Description 可用作 Discussion 框架：

```markdown
#### Feature Description
A written overview of the feature and why this feature solves challenges
that you are facing today.

#### Use Case(s)
Describe the use case for this feature (i.e. Secret Storage, Encryption,
Access Control) and deployment environments (K8s, VMs, Nomad, ECS).
```

### 案例 5：hashicorp/terraform-provider-aws (10k⭐)

**仓库：** https://github.com/hashicorp/terraform-provider-aws

Terraform Provider 的讨论结构：

```markdown
## Feature Request / Discussion
### Current Limitations
[当前提供商的局限]

### Proposed Enhancement  
[建议的增强]

### Use Cases
[使用场景描述]
```

### 案例 6：nixos/nixpkgs (18k⭐)

**仓库：** https://github.com/NixOS/nixpkgs
**RFC 仓库：** https://github.com/NixOS/rfcs

Nixpkgs RFC 讨论结构：

```markdown
## Motivation
## Design
## Alternatives
## Breaking Impact
## Unresolved Questions
```

---

> 收集日期：2026-06-12
