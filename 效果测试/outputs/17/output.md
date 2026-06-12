# 17 Issue Form YAML 测试

## File: `.github/ISSUE_TEMPLATE/bug_report.yml`

```yaml
name: Bug report
description: Report a reproducible problem with the component library.
labels:
  - "status: waiting for maintainer"
body:
  - type: markdown
    attributes:
      value: |
        Thanks for taking the time to report a bug. Please search existing issues before submitting a new one.

  - type: input
    id: search-keywords
    attributes:
      label: Search keywords
      description: List the keywords you used when searching for existing issues.
      placeholder: "button focus ring, dialog scroll lock, ..."
    validations:
      required: true

  - type: checkboxes
    id: latest-version
    attributes:
      label: Latest version
      options:
        - label: I have tested the latest version.
          required: true

  - type: dropdown
    id: package
    attributes:
      label: Affected package
      options:
        - Material UI
        - MUI System
        - Joy UI
        - Other / not sure
    validations:
      required: true

  - type: textarea
    id: steps-to-reproduce
    attributes:
      label: Steps to reproduce
      description: Provide a minimal reproduction and exact steps.
      value: |
        Steps:
        1. Open this reproduction:
        2.
        3.
    validations:
      required: true

  - type: textarea
    id: current-behavior
    attributes:
      label: Current behavior
      description: What happened?
    validations:
      required: true

  - type: textarea
    id: expected-behavior
    attributes:
      label: Expected behavior
      description: What did you expect to happen?
    validations:
      required: true

  - type: textarea
    id: context
    attributes:
      label: Context
      description: What are you trying to build, and why does this matter?

  - type: textarea
    id: environment
    attributes:
      label: Environment
      description: Run `npx @mui/envinfo` and paste the output. Include browser information when relevant.
      value: |
        <details>
          <summary><code>npx @mui/envinfo</code></summary>

        ```text
        Paste output here.
        ```
        </details>
    validations:
      required: true
```

## File: `.github/ISSUE_TEMPLATE/feature_request.yml`

```yaml
name: Feature request
description: Suggest an improvement or new capability for the component library.
labels:
  - "status: waiting for maintainer"
body:
  - type: markdown
    attributes:
      value: |
        Thanks for suggesting an improvement. Please search existing issues and explain the user problem before proposing an API.

  - type: input
    id: search-keywords
    attributes:
      label: Search keywords
      description: List the keywords you used when searching for existing issues.
      placeholder: "data grid column pinning, date picker range, ..."
    validations:
      required: true

  - type: checkboxes
    id: latest-version
    attributes:
      label: Latest version
      options:
        - label: I have tested the latest version.
          required: true

  - type: dropdown
    id: package
    attributes:
      label: Target package
      options:
        - Material UI
        - MUI System
        - Joy UI
        - Other / not sure
    validations:
      required: true

  - type: textarea
    id: summary
    attributes:
      label: Summary
      description: Describe the behavior or API you would like to see.
    validations:
      required: true

  - type: textarea
    id: use-cases
    attributes:
      label: Use cases
      description: Explain who needs this and what workflow it unlocks.
      placeholder: |
        1. As a ...
        2. I want ...
        3. So that ...
    validations:
      required: true

  - type: textarea
    id: examples
    attributes:
      label: Examples or prior art
      description: Link to design specs, other implementations, screenshots, or code examples when available.

  - type: textarea
    id: alternatives
    attributes:
      label: Alternatives considered
      description: Describe current workarounds and why they are not enough.
```
