# Issue Form YAML Standard

## Use When

Use when creating or revising GitHub Issue Forms under `.github/ISSUE_TEMPLATE/*.yml`.

## Output Boundary

Issue Form YAML must be valid GitHub issue-form YAML. Do not wrap a single target file in explanatory Markdown when the file is meant to be written to disk. Do not copy repository-specific labels, teams, SIGs, or version lists from unrelated projects.

## Standard Structure

Use GitHub-supported fields:

```yaml
name: Bug report
description: Report a reproducible problem
title: "[Bug]: "
# labels omitted until repository label conventions are known
body:
  - type: markdown
    attributes:
      value: "Thanks for taking the time to report this."
  - type: textarea
    id: current-behavior
    attributes:
      label: Current behavior
      description: What happened?
    validations:
      required: true
```

Recommended inputs:

- `textarea` for descriptions, reproduction, logs, and context.
- `input` for versions, package names, links, or short values.
- `dropdown` only when valid options are known.
- `checkboxes` for confirmations and checklist items.
- `markdown` for short instructions.

## Missing Information

- If labels, default title, or options are unknown, omit them instead of inventing.
- If a required field cannot be answered safely, ask the user before setting `validations.required: true`.

## Do Not Invent

- Do not invent labels, projects, assignees, SIGs, versions, required checkboxes, or support policies.
- Do not add YAML comments that GitHub will show awkwardly unless requested.
- Do not include unsupported GitHub form fields.

## Strong Sources

| Source | Useful Pattern |
|--------|----------------|
| GitHub Issue Forms docs | Valid syntax and supported input types |
| React / TypeScript templates | Reproduction and environment fields |
| Kubernetes templates | Area/component boundaries |

## Checklist

- [ ] YAML parses.
- [ ] Only supported GitHub issue-form fields are used.
- [ ] Required fields are truly required.
- [ ] Labels/options are repository-specific or omitted.
