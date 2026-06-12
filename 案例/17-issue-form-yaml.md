# Issue Form YAML — 经典案例（完整原文）

---

## 精细版（完整 YAML 表单原文）

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
        Please provide as much info as possible. Not doing so may result in your bug not being addressed in a timely manner.
        If this matter is security related, please disclose it privately via https://kubernetes.io/security
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
      value: |
        <details>
        </details>
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
        # paste output here
        $ uname -a
        # paste output here
        # On Windows:
        C:\\> wmic os get Caption, Version, BuildNumber, OSArchitecture
        # paste output here
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

### 案例 2：apache/echarts (62k⭐)

**仓库：** https://github.com/apache/echarts
**模板来源：** https://raw.githubusercontent.com/apache/echarts/master/.github/ISSUE_TEMPLATE/bug_report.yml

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
      For usage questions, please use docs or Stack Overflow.
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
      Provide a link to Official Editor, JSFiddle, CodeSandbox, or GitHub repo.
      The reproduction should be minimal.
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

---

### 案例 3：prisma/prisma (43k⭐)

**仓库：** https://github.com/prisma/prisma
**模板来源：** https://raw.githubusercontent.com/prisma/prisma/main/.github/ISSUE_TEMPLATE/bug_report.yml

```yaml
name: Bug Report
description: File a bug report
title: "[Bug]: "
labels: ["bug"]
body:
  - type: markdown
    attributes:
      value: |
        Thanks for taking the time to fill out this bug report!
  - type: textarea
    id: description
    attributes:
      label: Description
      description: A clear and concise description of what the bug is.
    validations:
      required: true
  - type: textarea
    id: reproduction
    attributes:
      label: Reproduction
      description: |
        Provide a link to a repo or step-by-step guide that reproduces the problem.
        Minimal reproductions are required for us to investigate bugs.
    validations:
      required: true
  - type: textarea
    id: logs
    attributes:
      label: Logs
      description: Include any relevant logs or error messages.
      render: shell
  - type: textarea
    id: env
    attributes:
      label: Environment
      description: Run `prisma info` and paste the output.
      render: shell
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

## 普通版（精简 YAML/模板）

### 案例 4：prometheus/prometheus (56k⭐)

**仓库：** https://github.com/prometheus/prometheus
**模板来源：** https://raw.githubusercontent.com/prometheus/prometheus/main/.github/ISSUE_TEMPLATE/bug_report.md

```markdown
---
name: Bug Report
about: Report a bug in Prometheus
---

### Bug Description

### Steps to Reproduce

### Expected vs Actual Behavior

### Environment
- Prometheus version:
- OS:
- Deployment (Docker/K8s/binary):
```

### 案例 5：hashicorp/consul (28k⭐)

**仓库：** https://github.com/hashicorp/consul
**模板来源：** https://raw.githubusercontent.com/hashicorp/consul/main/.github/ISSUE_TEMPLATE/bug_report.md

```markdown
---
name: Bug Report
about: Report a bug in Consul
---

#### Overview of the Issue

#### Reproduction Steps

### Consul info for both Client and Server
<details>
  <summary>Client info</summary>
```
Output from client 'consul info' command here
```
</details>

#### Operating system and Environment details

#### Log Fragments
```

### 案例 6：hashicorp/nomad (15k⭐)

**仓库：** https://github.com/hashicorp/nomad
**模板来源：** https://raw.githubusercontent.com/hashicorp/nomad/main/.github/ISSUE_TEMPLATE/bug_report.md

```markdown
---
name: Bug Report
about: Let us know about an unexpected error, a crash, or incorrect behavior
---

#### Overview of the Issue

#### Reproduction Steps
1. Create a cluster...
2. Run `nomad job run ...`
3. View error

#### Nomad info for both Client and Server
<details>
  <summary>Client info</summary>
```
nomad node status
```
</details>

#### Operating system and Environment details

#### Log Fragments
```

---

> 收集日期：2026-06-12
