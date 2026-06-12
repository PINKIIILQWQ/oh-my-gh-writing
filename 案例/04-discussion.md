# Discussion — 经典案例

---

## 精细版（完整模板）

### 案例 1：apache/echarts (62k⭐)

ECharts 使用 GitHub Discussions 进行功能讨论和社区交流。Discussion 模板风格：

- **Category:** Ideas / Q&A / Show and Tell
- **Title:** 清晰的讨论主题
- **Body:** 
  - 背景说明（当前状况）
  - 提议方案（多个选项对比）
  - 社区征求意见点

ECharts 在 issue 模板中明确引导：
> "For usage questions, please use [Stack Overflow](https://stackoverflow.com/questions/tagged/echarts)"
> "For non-technical support, email dev@echarts.apache.org"

这形成了清晰的分类漏斗：bug/feature → issue，用法问题 → Stack Overflow，社区讨论 → Discussions。

---

### 案例 2：ansible/ansible (64k⭐)

Ansible 的 Discussion 文化体现在多个渠道的明确分层：

- **Bug / Feature Request** → GitHub Issues（bot 驱动）
- **Community Help** → [Ansible Forum](https://forum.ansible.com/c/help/6)
- **Proposals** → [ansible/proposals](https://github.com/ansible/proposals) 仓库
- **General Discussion** → Mailing list / IRC

issue 模板中明确写着：
> "If seeking community support, users are directed to the Ansible forum"

Discussion 模板规范（从提案模板提取）：
```
#### Problem Description
[当前问题和背景]

#### Proposed Change
[方案描述和示例]

#### Alternatives Considered
[备选方案及优缺点]

#### Impact
[对现有用户/API 的影响]
```

---

### 案例 3：prisma/prisma (43k⭐)

Prisma 使用 GitHub Discussions 作为社区讨论平台：

- **模板结构：**
  - 讨论主题分类（Ideas / Q&A / General）
  - 清晰的标题
  - 附加上下文（schema/query/expected behavior）

Prisma 的 issue 模板也引导去 Discussions：
> "For questions about using Prisma, please use Discussions instead of filing an issue."

---

## 普通版（简化模板）

### 案例 4：hashicorp/consul (28k⭐)

Consul 的 Discussion 风格——通过 feature request 模板间接实现：

```markdown
#### Feature Description
A written overview and why this solves challenges.

#### Use Case(s)
Describe the use case and deployment environments.
```

开放式讨论场景只需扩展 `Use Case(s)` 部分为多方案对比即可。

---

### 案例 5：hashicorp/nomad (15k⭐)

Nomad 同样使用 GitHub Discussions，典型模板结构：

- 简短标题
- 背景 / 动机（2-3 句）
- 1-2 个开放性问题征求社区意见
- 无固定字段，自由格式

---

### 案例 6：jestjs/jest (45k⭐)

Jest 使用 Discussion 进行分类讨论：

```yaml
labels: [':rocket: Feature Request']
```

对于有争议的设计决策，Jest 社区通过 issue 中的开放式讨论达成共识——模板中明确列出哪些不会进入 core 以减少讨论噪音：
- 新 matchers → `jest-extended` 社区包
- 默认 reporter 变更 → 自定义 reporter
- 测试环境变更 → 自定义环境

---

> 收集日期：2026-06-12
