# Public Launch Readiness Audit

## Existing

- README: present.
- License: present.

## Recommended

- CONTRIBUTING.md — explains setup, test, branch, and PR expectations before outside contributors arrive.
- .github/ISSUE_TEMPLATE/bug_report.yml — standardizes defect reports with reproduction, expected behavior, actual behavior, and environment fields.
- .github/ISSUE_TEMPLATE/feature_request.yml — separates future capability requests from bug reports and keeps motivation, use cases, and alternatives visible.
- .github/pull_request_template.md — gives contributors a consistent place for summary, testing, risk, and related issues.
- .github/workflows/validate.yml, if `scripts/test.sh` should run on GitHub — lets contributors and maintainers run the same check before review.
- CHANGELOG.md, if releases are versioned — gives users a stable place to understand changes across versions.

## Optional

- SECURITY.md — useful only if private vulnerability reporting is supported.
- CODE_OF_CONDUCT.md — useful if the project welcomes broad community participation.
- CODEOWNERS — useful if review ownership is shared or maintainers want automatic review routing.

## Next steps

- Confirm which recommended files to prepare.
- Draft target files only after maintainer confirmation.
