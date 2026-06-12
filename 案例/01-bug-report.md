# Bug Report — 经典案例

> 18 场景 × 6 案例（3精细 + 3普通），来源均为不同仓库，共计 108 个独立仓库。

---

## 精细版（完整 YAML/模板）

### 案例 1：prisma/prisma (43k⭐)

**来源：** `.github/ISSUE_TEMPLATE/bug_report.yml`

```yaml
name: Bug Report
description: File a bug report
title: "[Bug]: "
labels: ["bug"]
body:
  - type: markdown
    attributes:
      value: |
        Thanks for taking the time to fill out this bug report! Please fill out the form below.
  - type: textarea
    id: description
    attributes:
      label: Description
      description: A clear and concise description of what the bug is.
      placeholder: Tell us what happened!
    validations:
      required: true
  - type: textarea
    id: reproduction
    attributes:
      label: Reproduction
      description: |
        Please provide a link to a repo or [step-by-step guide](https://stackoverflow.com/help/minimal-reproducible-example)
        that reproduces the problem. Include code snippets, schemas, and queries if relevant.
        Minimal reproductions are **required** for us to investigate bugs.
      placeholder: |
        1. Create a schema with...
        2. Run `prisma db push`
        3. See error...
    validations:
      required: true
  - type: textarea
    id: logs
    attributes:
      label: Logs
      description: Please include any relevant logs, error messages, or console output.
      render: shell
    validations:
      required: false
  - type: textarea
    id: env
    attributes:
      label: Environment
      description: |
        Please provide information about your environment.
        Run `prisma info` and paste the output.
      render: shell
      placeholder: |
        OS: macOS 14.0
        Node: 20.x
        Prisma: 5.x
    validations:
      required: true
  - type: checkboxes
    id: checks
    attributes:
      label: Additional checks
      options:
        - label: I understand that my issue will be automatically closed if I don't complete the required fields
          required: true
```

---

### 案例 2：ansible/ansible (64k⭐)

**来源：** `.github/ISSUE_TEMPLATE/bug_report.yml`

Ansible 的 Bug Report 模板极其详尽，包含 10 个必填字段，由 bot（ansibot）自动化处理：

1. **Summary** (textarea) — 描述问题、环境、如何出错
2. **Issue Type** (dropdown, 固定为 Bug Report) — bot 标记
3. **Component Name** (input, required) — 模块/插件名称
4. **Ansible Version** (textarea, required) — 粘贴 `ansible --version` 输出
5. **Configuration** (textarea, required) — 粘贴 `ansible-config dump --only-changed -t all`
6. **OS / Environment** (textarea, required) — 目标 OS、网络设备固件等
7. **Steps to Reproduce** (textarea, required) — 最小可重现用例
8. **Expected Results** (textarea, required)
9. **Actual Results** (textarea, required) — 带上 `-vvvv` 详细输出
10. **Code of Conduct** (checkbox, required)

**特点：** 机器人驱动、预填命令输出、强调最小可重现、权限提醒加密信息脱敏。

> 完整 URL：https://github.com/ansible/ansible/blob/devel/.github/ISSUE_TEMPLATE/bug_report.yml

---

### 案例 3：apache/echarts (62k⭐)

**来源：** `.github/ISSUE_TEMPLATE/bug_report.yml`

```yaml
name: Bug Report
description: Report a bug to Apache ECharts
title: "[Bug] "
labels: [bug]
body:
- type: markdown
  attributes:
    value: |
      The issue list is reserved exclusively for bug reports and feature requests.
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
    description: |
      Provide a link to [Official Editor](https://echarts.apache.org/examples/editor.html),
      [JSFiddle](https://jsfiddle.net/), [CodeSandbox](https://codesandbox.io/), or GitHub repo.
      The reproduction should be **minimal**.
    validations:
      required: true
- type: textarea
  attributes:
    label: Steps to Reproduce
    placeholder: |
      1. How to create the chart
      2. What's the chart option
      3. User interactions before the error
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
  validations:
    required: false
- type: textarea
  attributes:
    label: Any additional comments?
  validations:
    required: false
```

**特点：** 必填版本 + 在线可重现链接 + 精简 6 字段，适合前端可视化项目。

---

## 普通版（较短的模板）

### 案例 4：jestjs/jest (45k⭐)

**来源：** `.github/ISSUE_TEMPLATE/bug.yml`

Jest 的 Bug Report 使用 YAML 表单，核心字段：

- **Version** (input, required) — 正在使用的 Jest 版本
- **Steps to reproduce** (textarea, required) — 最小可重现仓库链接 + 操作步骤
- **Expected behavior** (textarea, required)
- **Actual behavior** (textarea, required)
- **Additional context** (textarea, optional)
- **Environment** (textarea, required) — `npx envinfo --preset jest` 输出

**特点：** 强调"没有最小可重现将被拒绝"；要求先阅读文档和搜索已有 issues；自动环境采集。

> 完整 URL：https://github.com/jestjs/jest/blob/main/.github/ISSUE_TEMPLATE/bug.yml

---

### 案例 5：hashicorp/nomad (15k⭐)

**来源：** `.github/ISSUE_TEMPLATE/bug_report.md`

```markdown
---
name: Bug Report
about: You're experiencing an issue that is different than the documented behavior.
---

#### Overview of the Issue

#### Reproduction Steps

Steps to reproduce this issue:
1. Create a cluster with n client nodes and n server nodes
2. Run `nomad job run ...`
3. View error

#### Nomad info for both Client and Server

<details>
  <summary>Client info</summary>
```
Output from client `nomad node status` here
```
</details>

#### Operating system and Environment details

#### Log Fragments
```

**特点：** 简洁但完整，HashiCorp 风格的分段结构。

---

### 案例 6：hashicorp/consul (28k⭐)

**来源：** `.github/ISSUE_TEMPLATE/bug_report.md`

```markdown
---
name: Bug Report
about: You're experiencing an issue with Consul
---

#### Overview of the Issue

#### Reproduction Steps

1. Create a cluster with n client nodes and n server nodes
2. Run `curl ...`
3. View error

### Consul info for both Client and Server

<details>
  <summary>Client info</summary>

```
Output from client 'consul info' command here
```

```
Client agent HCL config
```
</details>

#### Operating system and Environment details

#### Log Fragments

Use `-log-level=TRACE` on the client and server to capture the maximum log detail.
```

**特点：** 双节点视角（client + server），细节折叠，基础设施项目典型风格。

---

> 收集日期：2026-06-12
