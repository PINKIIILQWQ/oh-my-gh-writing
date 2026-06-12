# 08 Documentation PR 测试

## Summary

Updates the Vue Router navigation guard documentation with practical guidance for:

- `beforeRouteEnter`
- `beforeRouteUpdate`
- `beforeRouteLeave`

The new content focuses on when each guard runs and how to use it safely in real application flows.

## Motivation

Navigation guards are easy to misuse because the three in-component guards run at different points in the component lifecycle.

The updated documentation should help readers choose the right guard for common cases such as fetching route-dependent data, reacting to parameter changes, and preventing accidental navigation away from unsaved work.

## Documentation Scope

This is a documentation-only PR draft based on the prompt. A real diff was not provided, so the exact documentation path, line numbers, preview URL, and screenshots are intentionally omitted.

Expected documentation topics:

- Use `beforeRouteEnter` for logic that must run before the component instance is available.
- Use `beforeRouteUpdate` when the same component instance is reused for a different route.
- Use `beforeRouteLeave` for cleanup, confirmation, or unsaved-change protection.
- Include examples that show guard-specific constraints rather than presenting the guards as interchangeable hooks.

## No Code Changes

This PR is intended to change documentation only.

## Verification to Run

- [ ] Build the documentation site.
- [ ] Check that all code samples render with the expected syntax highlighting.
- [ ] Confirm examples match the current Vue Router API.
- [ ] Check links and anchors in the updated navigation guard page.

## Review Notes

Please pay close attention to whether the examples explain lifecycle timing clearly, especially the difference between `beforeRouteEnter` and guards that can access the component instance directly.
