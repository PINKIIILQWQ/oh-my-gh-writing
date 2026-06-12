---
scenario: Issue Form YAML
mode: concise
case-sources: https://github.com/microsoft/playwright, https://github.com/hashicorp/terraform
input-prompt: ../../prompts/17-issue-form-yaml.md
---

# .github/ISSUE_TEMPLATE/bug_report.yml

```yaml
name: Bug Report
description: Report a bug in the component library
title: "[Bug]: "
labels: ["bug", "needs-triage"]
body:
  - type: markdown
    attributes:
      value: |
        Thanks for reporting! Please fill out the form below.
  - type: textarea
    id: description
    attributes:
      label: Description
      description: What happened?
    validations:
      required: true
  - type: textarea
    id: reproduction
    attributes:
      label: Reproduction
      description: Steps or link to minimal reproduction
    validations:
      required: true
  - type: input
    id: version
    attributes:
      label: Version
      placeholder: e.g. 2.1.0
    validations:
      required: true
  - type: dropdown
    id: browser
    attributes:
      label: Browser
      options: [Chrome, Firefox, Safari, Edge]
    validations:
      required: true
```

# .github/ISSUE_TEMPLATE/config.yml

```yaml
blank_issues_enabled: false
contact_links:
  - name: Documentation
    url: https://example.com/docs
    about: Check docs before filing an issue
```
