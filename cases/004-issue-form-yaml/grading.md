# Grading

Label: PASS

What improved:

- The output is YAML file content.
- It does not invent labels, project IDs, assignees, or contact links.
- It includes the core bug report fields and required validations.

Remaining risk:

- YAML parseability should be manually reviewed or checked with a YAML parser before copying into `.github/ISSUE_TEMPLATE/`.

Decision:

- Keep as public evidence after maintainer review.
