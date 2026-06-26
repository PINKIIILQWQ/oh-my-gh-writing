# GitHub Form YAML Standard

## Use When

Use when creating or revising GitHub Issue Forms under `.github/ISSUE_TEMPLATE/*.yml` or GitHub Discussion Category Forms under `.github/DISCUSSION_TEMPLATE/*.yml`.

## Output Boundary

Form YAML must be valid GitHub form schema for the target location. Do not wrap a single target file in explanatory Markdown when the file is meant to be written to disk. Do not copy repository-specific labels, issue types, projects, assignees, teams, SIGs, discussion category slugs, or version lists from unrelated projects.

## Standard Structure

For Issue Forms, use GitHub-supported top-level fields:

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

Supported Issue Form top-level keys:

- Required: `name`, `description`, `body`.
- Optional with repository evidence: `title`, `labels`, `projects`, `assignees`, `type`.

For Discussion Category Forms, use `.github/DISCUSSION_TEMPLATE/<category-slug>.yml`. The file name must match an existing discussion category slug.

```yaml
title: "[Idea] "
body:
  - type: textarea
    id: proposal
    attributes:
      label: Proposal
      description: What should the community discuss?
    validations:
      required: true
```

Supported Discussion Form top-level keys:

- Required: `body` with at least one non-`markdown` field.
- Optional with repository evidence: `title`, `labels`.

Recommended inputs:

- `textarea` for descriptions, reproduction, logs, and context.
- `input` for versions, package names, links, or short values.
- `dropdown` only when valid options are known.
- `checkboxes` for confirmations and checklist items.
- `markdown` for short instructions.
- `upload` only when file attachments are useful and the target form supports that workflow.

Form element rules:

- `type` must be one of `checkboxes`, `dropdown`, `input`, `markdown`, `textarea`, or `upload`.
- `id` is optional but useful for URL query prefills; use only alphanumeric characters, `-`, and `_`, and keep IDs unique.
- `render` is valid on `textarea` when submitted text should render as code.
- `dropdown.default` is a zero-based index; do not include a `None` or `n/a` option when setting a default.
- `validations.required` should be used only for information maintainers truly need. Do not make policy confirmations required unless the target repository has that policy.

## Good Output Shape

Issue Form:

```yaml
name: Bug report
description: Report a reproducible problem
title: "[Bug]: "
body:
  - type: textarea
    id: reproduction
    attributes:
      label: Steps to reproduce
    validations:
      required: true
```

Discussion Category Form:

```yaml
title: "[Question] "
body:
  - type: textarea
    id: context
    attributes:
      label: Context
      description: What should the community know before discussing this?
    validations:
      required: true
```

## Common Failure

- Adding `labels`, `projects`, `assignees`, `type`, category slugs, or SIG fields copied from another repository.
- Making optional policy confirmations required without maintainer input.
- Wrapping a single YAML file in explanatory Markdown.
- Creating a Discussion Category Form with a file name that does not match an existing discussion category slug.

## Missing Information

- If labels, issue type, projects, assignees, default title, category slug, or options are unknown, omit them or mark them `TBD` instead of inventing.
- If a required field cannot be answered safely, ask the user before setting `validations.required: true`.

## Do Not Invent

- Do not invent labels, issue types, projects, assignees, discussion category slugs, SIGs, versions, required checkboxes, or support policies.
- Do not add YAML comments that GitHub will show awkwardly unless requested.
- Do not include unsupported GitHub form fields.
- Do not assume that a label will be created automatically. GitHub only applies existing labels.

## Strong Sources

| Source | Useful Pattern |
|--------|----------------|
| GitHub Issue Forms docs | Valid issue-form top-level fields and submission behavior |
| GitHub form schema docs | Supported input types, validations, IDs, dropdown defaults, and uploads |
| GitHub Discussion Category Forms docs | `.github/DISCUSSION_TEMPLATE/` path and category-slug requirement |
| React / TypeScript templates | Reproduction and environment fields |
| Kubernetes templates | Area/component boundaries |

## Checklist

- [ ] YAML parses.
- [ ] Target path is correct for Issue Forms or Discussion Category Forms.
- [ ] Only supported GitHub form fields are used.
- [ ] Discussion form file names match known category slugs.
- [ ] Required fields are truly required.
- [ ] Labels, issue types, projects, assignees, category slugs, and options are repository-specific or omitted.
