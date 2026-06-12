# Issue Form YAML — 经典案例

> 格式：**YAML**（GitHub Issue Forms 的强制格式）
>
> 这是一个结构化的 YAML 文件，GitHub 将其渲染为带输入框/下拉框/复选框的 Web 表单，而不是纯文本编辑器。

---

## 精细版（完整 YAML 表单）

### 案例 1：microsoft/playwright (70k⭐)

**仓库：** https://github.com/microsoft/playwright
**模板来源：** https://raw.githubusercontent.com/microsoft/playwright/main/.github/ISSUE_TEMPLATE/bug.yml

```yaml
name: Bug Report 🪲
description: Create a bug report to help us improve
title: '[Bug]: '
body:
  - type: markdown
    attributes:
      value: |
        # Please follow these steps first:
  - type: markdown
    attributes:
      value: |
        ## Troubleshoot
        If Playwright is not behaving the way you expect, we'd ask you to look at
        the [documentation](https://playwright.dev/docs/intro) and search the issue
        tracker for evidence supporting your expectation.
        Please make reasonable efforts to troubleshoot and rule out issues with
        your code, the configuration, or any 3rd party libraries you might be using.
        Playwright offers [several debugging tools](https://playwright.dev/docs/debug)
        that you can use to troubleshoot your issues.
  - type: markdown
    attributes:
      value: |
        ## Ask for help through appropriate channels
        If you feel unsure about the cause of the problem, consider asking for help
        on for example [StackOverflow](https://stackoverflow.com/questions/ask) or
        our [Discord channel](https://aka.ms/playwright/discord) before posting a
        bug report. The issue tracker is not a help forum.
  - type: markdown
    attributes:
      value: |
        ## Make a minimal reproduction
        To file the report, you will need a GitHub repository with a minimal (but
        complete) example and simple/clear steps on how to reproduce the bug.
        The simpler you can make it, the more likely we are to successfully verify
        and fix the bug. You can create a new project with
        `npm init playwright@latest new-project` and then add the test code there.
  - type: input
    id: version
    attributes:
      label: Version
      description: |
        The version of Playwright you are using.
        Is it the [latest](https://github.com/microsoft/playwright/releases)?
      placeholder: ex. 1.44.0
    validations:
      required: true
  - type: textarea
    id: reproduction
    attributes:
      label: Steps to reproduce
      description: Please link to a repository with a minimal reproduction.
      placeholder: |
        1. Clone my repo at https://github.com/<myuser>/example
        2. npm install
        3. npx playwright test
        4. You should see the error come up
    validations:
      required: true
  - type: textarea
    id: expected
    attributes:
      label: Expected behavior
      description: A description of what you expect to happen.
      placeholder: I expect to see X or Y
    validations:
      required: true
  - type: textarea
    id: what-happened
    attributes:
      label: Actual behavior
      description: A clear and concise description of the unexpected behavior.
      placeholder: A bug happened!
    validations:
      required: true
  - type: textarea
    id: context
    attributes:
      label: Additional context
      description: Anything else that might be relevant
    validations:
      required: false
  - type: textarea
    id: envinfo
    attributes:
      label: Environment
      description: |
        Please paste the output of running `npx envinfo --preset playwright`.
        This will be automatically formatted as a code block, so no need for backticks.
      render: shell
    validations:
      required: true
```

**特点：** 3 层 markdown 引导（Troubleshoot → Help → Minimal reproduction）+ 6 个字段（Version/Steps/Expected/Actual/Context/Environment）+ 全部必填。

---

### 案例 2：hashicorp/terraform (45k⭐)

**仓库：** https://github.com/hashicorp/terraform
**模板来源：** https://raw.githubusercontent.com/hashicorp/terraform/main/.github/ISSUE_TEMPLATE/bug_report.yml

Terraform 的 YAML Issue Form 极其详尽，包含：

```yaml
name: Bug Report
description: Let us know about an unexpected error, a crash, or an incorrect behavior.
labels: ["bug", "new"]
body:
  - type: markdown
    attributes:
      value: |
        ## Filing a bug report
        To fix problems, we need clear reproduction cases - we need to be able to
        see it happen locally. A reproduction case is ideally something a Terraform
        Core engineer can git-clone or copy-paste and run immediately.

        * A short example can be directly copy-pasteable
        * Please include all needed context
        * Set defaults on (or omit) any variables
        * If multiple steps are required, consider scripting it
        * Omit any unneeded complexity
        * When possible, use the null resource provider

  - type: textarea
    id: tf-version
    attributes:
      label: Terraform Version
      description: Run `terraform version` to show the version
      render: shell
    validations:
      required: true

  - type: textarea
    id: tf-config
    attributes:
      label: Terraform Configuration Files
      description: Paste relevant parts of your Terraform configuration
    validations:
      required: true

  - type: textarea
    id: tf-debug
    attributes:
      label: Debug Output
      description: Full debug output from `TF_LOG=trace`
    validations:
      required: true

  - type: textarea
    id: tf-expected
    attributes:
      label: Expected Behavior
    validations:
      required: true

  - type: textarea
    id: tf-actual
    attributes:
      label: Actual Behavior
    validations:
      required: true

  - type: textarea
    id: tf-steps
    attributes:
      label: Steps to Reproduce
    validations:
      required: true

  - type: textarea
    id: tf-additional
    attributes:
      label: Additional Information
```

**特点：** 8 字段 + 前置多层引导（区分 bug 与 provider 问题）+ 最小可重现指南。

---

### 案例 3：apache/echarts (62k⭐)

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
      For usage questions, please use the docs or Stack Overflow.
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
      Provide a link to CodeSandbox, JSFiddle, or GitHub repo.
      The reproduction should be **minimal**.
  validations:
    required: true
- type: textarea
  attributes:
    label: Steps to Reproduce
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
```

**特点：** 7 字段 + 在线编辑器链接必填 + 环境字段预填格式。

---

## 普通版

### 案例 4：microsoft/playwright feature.yml

Playwright 的 Feature Request YAML 与 bug 同结构，核心字段：Feature Proposal → Motivation → Example → Pitch

### 案例 5：hashicorp/terraform feature_request.yml

Terraform 的 Feature Request YAML：Problem → Solution → Alternatives → Compatibility

### 案例 6：apache/echarts feature_request.yml

```yaml
name: Feature Request
description: Request a new feature from Apache ECharts
title: "[Feature] "
labels: [new-feature]
body:
- type: textarea
  attributes:
    label: What problem does this feature solve?
  validations:
    required: true
- type: textarea
  attributes:
    label: What does the proposed API look like?
  validations:
    required: true
```

---

### 参考仓库链接

- https://github.com/microsoft/playwright — `.github/ISSUE_TEMPLATE/bug.yml`
- https://github.com/hashicorp/terraform — `.github/ISSUE_TEMPLATE/bug_report.yml`
- https://github.com/apache/echarts — `.github/ISSUE_TEMPLATE/bug_report.yml`

---

> 收集日期：2026-06-12
