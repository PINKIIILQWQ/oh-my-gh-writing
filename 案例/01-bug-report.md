# Bug Report — 经典案例


> 格式：**YAML**（GitHub Issue Form）
> Markdown 模板（旧格式）也可用，但 YAML 是当前最佳实践

> 18 场景 × 6 案例（3精细 + 3普通），来源均为不同 GitHub 仓库。

---

## 精细版（完整模板）

### 案例 1：kubernetes/kubernetes (112k⭐)

**仓库：** https://github.com/kubernetes/kubernetes
**模板来源：** https://raw.githubusercontent.com/kubernetes/kubernetes/master/.github/ISSUE_TEMPLATE/bug-report.yaml

```yaml
name: Bug Report
description: Report a bug encountered while operating Kubernetes
labels: kind/bug
body:
  - type: textarea
    id: problem
    attributes:
      label: What happened?
      description: |
        Please provide as much info as possible. Not doing so may result in
        your bug not being addressed in a timely manner.
        If this matter is security related, please disclose it privately
        via https://kubernetes.io/security
    validations:
      required: true
  - type: textarea
    id: expected
    attributes:
      label: What did you expect to happen?
    validations:
      required: true
  - type: textarea
    id: repro
    attributes:
      label: How can we reproduce it (as minimally and precisely as possible)?
    validations:
      required: true
  - type: textarea
    id: additional
    attributes:
      label: Anything else we need to know?
  - type: textarea
    id: kubeVersion
    attributes:
      label: Kubernetes version
      value: |
        <details>
        ```console
        $ kubectl version
        # paste output here
        ```
        </details>
    validations:
      required: true
  - type: textarea
    id: cloudProvider
    attributes:
      label: Cloud provider
    validations:
      required: true
  - type: textarea
    id: osVersion
    attributes:
      label: OS version
      value: |
        <details>
        ```console
        # On Linux:
        $ cat /etc/os-release
        $ uname -a
        # On Windows:
        C:\\> wmic os get Caption, Version, BuildNumber, OSArchitecture
        ```
        </details>
  - type: textarea
    id: installer
    attributes:
      label: Install tools
  - type: textarea
    id: runtime
    attributes:
      label: Container runtime (CRI) and version (if applicable)
  - type: textarea
    id: plugins
    attributes:
      label: Related plugins (CNI, CSI, ...) and versions (if applicable)
```

---

### 案例 2：prisma/prisma (43k⭐)

**仓库：** https://github.com/prisma/prisma
**模板来源：** https://raw.githubusercontent.com/prisma/prisma/main/.github/ISSUE_TEMPLATE/bug_report.yml

必填字段：
- **Description** (textarea, required)：清晰描述 Bug
- **Reproduction** (textarea, required)：链接到最小可重现仓库或逐步指南
- **Logs** (textarea, optional, render: shell)：相关日志
- **Environment** (textarea, required) ：运行 `prisma info` 并粘贴输出
- **Additional checks** (checkbox, required)：确认理解 issue 将自动关闭

---

### 案例 3：ansible/ansible (64k⭐)

**仓库：** https://github.com/ansible/ansible
**模板来源：** https://raw.githubusercontent.com/ansible/ansible/devel/.github/ISSUE_TEMPLATE/bug_report.yml

Ansible 的 Bug Report 由 bot（ansibot）驱动，10 个必填字段：

1. **Summary** — 描述问题、环境、如何出错
2. **Issue Type** — 固定 Bug Report（bot 标记）
3. **Component Name** — 模块/插件名称
4. **Ansible Version** — `ansible --version` 输出
5. **Configuration** — `ansible-config dump --only-changed`
6. **OS / Environment** — 目标 OS 等信息
7. **Steps to Reproduce** — 最小可重现用例
8. **Expected Results**
9. **Actual Results** — 带上 `-vvvv` 详细输出
10. **Code of Conduct**

---

## 普通版（较短模板）

### 案例 4：jestjs/jest (45k⭐)

**仓库：** https://github.com/jestjs/jest
**模板来源：** https://raw.githubusercontent.com/jestjs/jest/main/.github/ISSUE_TEMPLATE/bug.yml

```yaml
name: Bug Report 🪲
labels: ['Bug Report', 'Needs Triage']
body:
  - type: markdown
    attributes:
      value: |
        ## Troubleshoot
        If Jest is not behaving the way you expect, look at the documentation
        and search the issue tracker.
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
      placeholder: |
        1. Clone repo
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

---

### 案例 5：hashicorp/nomad (15k⭐)

**仓库：** https://github.com/hashicorp/nomad
**模板来源：** https://raw.githubusercontent.com/hashicorp/nomad/main/.github/ISSUE_TEMPLATE/bug_report.md

```markdown
---
name: Bug Report
about: Let us know about an unexpected error, a crash, or an incorrect behavior
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

---

### 案例 6：hashicorp/consul (28k⭐)

**仓库：** https://github.com/hashicorp/consul
**模板来源：** https://raw.githubusercontent.com/hashicorp/consul/main/.github/ISSUE_TEMPLATE/bug_report.md

```markdown
---
name: Bug Report
about: You're experiencing an issue with Consul that is different than the documented behavior.
---

#### Overview of the Issue

#### Reproduction Steps

Steps to reproduce this issue:
1. Create a cluster with n client nodes n and n server nodes
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
Use `-log-level=TRACE` to capture the maximum log detail.
```

---

> 收集日期：2026-06-12
