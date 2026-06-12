---
scenario: CHANGELOG
mode: concise
case-sources: https://github.com/psf/requests, https://github.com/facebook/jest
input-prompt: ../../prompts/13-changelog.md
---

# Changelog

## [2.1.0] - 2026-06-12

### Added
- Dark mode support with system preference detection
- New `ThemeProvider` component for theme inheritance
- `useTheme()` hook for accessing current theme

### Fixed
- Modal focus trap not restoring focus on close (#203)
- Button loading state not disabling click events (#198)
- Select component dropdown clipping on small screens (#195)

### Changed
- Deprecated `theme` prop on `Button` (use `ThemeProvider` instead)
- Upgraded internal dependencies to latest versions
