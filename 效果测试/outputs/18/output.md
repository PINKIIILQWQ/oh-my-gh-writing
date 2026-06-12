# 18 PR Template 测试

## Summary

<!-- What does this PR change? Keep this focused on one bug fix, feature, documentation update, or refactor. -->

## Motivation

<!-- Why is this change needed? Link an issue only when one exists. -->

Fixes #

## Changes

<!-- Describe the implementation at a reviewer-friendly level. -->

<!-- Add a short bullet list of the main changes. -->

## Testing

<!-- Check only the commands you actually ran. The commands below are used by fd's Cargo.toml or CICD workflow. -->

- [ ] `cargo fmt -- --check`
- [ ] `cargo clippy --all-targets --all-features -- -Dwarnings`
- [ ] `cargo test --locked --all-features`
- [ ] `cargo test --locked`
- [ ] Manual test:

## User-Facing Impact

<!-- Describe changes to CLI behavior, output, flags, performance, or platform support. Write "None" only when this is internal-only. -->

## Documentation

- [ ] README or help text updated, if user-facing behavior changed.
- [ ] CHANGELOG entry added, if this should be called out in a release.
- [ ] No documentation change needed.

## Compatibility

<!-- Note any impact on supported platforms, shell completions, packaging, or minimum supported Rust version. -->

## Checklist

- [ ] This PR is scoped to a single change.
- [ ] I did not pre-check boxes for work that has not been done.
- [ ] I included tests or explained why tests are not applicable.
- [ ] I updated docs for user-facing changes.
- [ ] I avoided unrelated formatting or dependency churn.
