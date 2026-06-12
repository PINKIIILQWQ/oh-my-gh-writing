# 07 Refactor PR 测试

## Summary

Consolidates scattered utility helpers under a shared `utils/` directory and updates imports to use the new structure.

Based on the provided prompt, this is intended to be behavior-preserving. No external API or runtime behavior change is expected.

## Motivation

Utility functions were previously spread across multiple locations, which made imports harder to discover and increased the chance of duplicate helper logic.

Centralizing them under `utils/` should make the internal structure easier to navigate and maintain.

## What Changed

- Moved existing utility functions into a unified `utils/` directory.
- Updated internal import paths to point to the new location.
- Kept the same helper behavior and call sites conceptually unchanged.

## Behavior Invariants

The following are based on the user's description and should be verified against the actual diff before merge:

- Public API behavior is unchanged.
- Helper return values are unchanged.
- Runtime side effects are unchanged.
- Only import paths and file organization changed.

## Before / After

```text
Before:
helpers were distributed across several feature or support files

After:
helpers live under utils/
callers import helpers from the consolidated location
```

## Verification to Run

- [ ] Run the existing unit test suite.
- [ ] Run typecheck or build validation.
- [ ] Run lint/import validation if the project has import-order or no-restricted-imports rules.
- [ ] Confirm no public exports changed unless they were intentionally re-exported from the new location.

## Notes for Reviewers

I do not have a real diff in this test prompt, so this PR description does not claim specific file counts, path names, test results, or CI status.
