---
scenario: CHANGELOG
mode: full-detail
case-sources: https://github.com/hashicorp/vagrant, https://github.com/pallets/flask
input-prompt: ../../prompts/13-changelog.md
---

# Changelog

## [2.1.0] - 2026-06-12

### Features
- **Dark mode**: Full dark mode support with `prefers-color-scheme` detection.
  Use `ThemeProvider` component to control theme at app level. See
  [dark mode guide](https://example.com/docs/dark-mode) for migration.
- **useTheme hook**: New React hook for accessing and toggling theme:
  ```tsx
  const { theme, toggleTheme } = useTheme();
  ```
  Returns 'light' | 'dark' | 'system' based on current state.

### Bug Fixes
- **Modal**: Focus trap now correctly restores focus to the triggering element
  when modal is closed. Previously focus was lost to document.body.
- **Button**: Loading state now properly disables click events and shows
  spinner animation. Fixed race condition on rapid double-click.
- **Select**: Dropdown clipping on small viewports resolved by switching
  from fixed positioning to auto-placement via Floating UI.

### Deprecation
- **Button `theme` prop**: Deprecated in favor of `ThemeProvider` context.
  The prop continues to work in v2.1.x but will be removed in v3.0.0.
  Migration: wrap app in `<ThemeProvider>` and remove `theme` prop from
  individual Button instances.
