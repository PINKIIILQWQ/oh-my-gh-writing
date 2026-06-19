# Grading

Label: PASS_AFTER_CLEANUP

What improved:

- The output stays draft-only and does not publish, push tags, or open PRs.
- It records version, missing release date, prompt-provided source, and release scope.
- It uses `## File: ...` headings to represent the local `.github-writing/version-release/v1.2.0/` package.
- It separates the manifest, changelog draft, and release notes draft.

Remaining risk:

- Release date, compare URL, and tag URL remain `TBD`.
- Baseline behavior has not been collected yet.

Decision:

- Keep as public evidence after maintainer review; do not describe it as a validated comparison case until baseline behavior is collected.
