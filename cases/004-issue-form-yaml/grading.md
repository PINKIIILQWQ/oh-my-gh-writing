# Grading

Label: PASS_AFTER_CLEANUP

What improved:

- The output is YAML file content.
- It does not invent labels, project IDs, assignees, or contact links.
- It includes the core bug report fields and required validations.

Remaining risk:

- Validation not run: YAML parseability still needs a parser check before copying into `.github/ISSUE_TEMPLATE/`.

Decision:

- README excerpt type: shortened.
- Keep as public evidence after maintainer review.
