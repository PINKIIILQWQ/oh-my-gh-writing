---
scenario: Issue Form YAML
mode: full-detail
case-sources: https://github.com/microsoft/playwright, https://github.com/hashicorp/terraform, https://github.com/apache/echarts
input-prompt: ../../prompts/17-issue-form-yaml.md
---

# Issue Form YAML — Component Library

## File: `.github/ISSUE_TEMPLATE/bug_report.yml`

```yaml
name: Bug Report
description: Report a bug in the component library
title: "[Bug]: "
labels: ["bug", "needs-triage"]
body:
  - type: markdown
    attributes:
      value: |
        ## Thanks for reporting a bug!
        Please fill out this form completely. Issues missing required fields
        will be closed automatically.

  - type: textarea
    id: description
    attributes:
      label: Description
      description: A clear and concise description of the bug
      placeholder: |
        When I click the button in dark mode, the text is invisible
        because the color contrast is too low.
    validations:
      required: true

  - type: textarea
    id: steps
    attributes:
      label: Steps to reproduce
      description: How can we reproduce this issue?
      placeholder: |
        1. Open Storybook in dark mode
        2. Navigate to Button component
        3. Click on the primary button
        4. Notice the text is invisible
    validations:
      required: true

  - type: textarea
    id: expected
    attributes:
      label: Expected behavior
    validations:
      required: true

  - type: textarea
    id: actual
    attributes:
      label: Actual behavior
    validations:
      required: true

  - type: input
    id: version
    attributes:
      label: Version
      description: Which version of the library are you using?
      placeholder: e.g. 2.1.0
    validations:
      required: true

  - type: dropdown
    id: browser
    attributes:
      label: Browser
      description: Which browser(s) are affected?
      multiple: true
      options:
        - Chrome
        - Firefox
        - Safari
        - Edge
    validations:
      required: true

  - type: textarea
    id: logs
    attributes:
      label: Console logs
      description: Any relevant console output
      render: shell
    validations:
      required: false
```

## File: `.github/ISSUE_TEMPLATE/feature_request.yml`

```yaml
name: Feature Request
description: Suggest a new feature or improvement
title: "[Feature]: "
labels: ["enhancement"]
body:
  - type: textarea
    id: problem
    attributes:
      label: Problem
      description: What problem does this feature solve?
    validations:
      required: true
  - type: textarea
    id: solution
    attributes:
      label: Proposed solution
      description: What should the API look like?
    validations:
      required: true
  - type: textarea
    id: alternatives
    attributes:
      label: Alternatives considered
    validations:
      required: false
```
