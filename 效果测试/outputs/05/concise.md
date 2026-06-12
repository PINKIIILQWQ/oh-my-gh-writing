---
scenario: Feature PR
mode: concise
case-sources: https://github.com/freeCodeCamp/freeCodeCamp, https://github.com/tauri-apps/tauri
input-prompt: ../../prompts/05-feature-pr.md
---

### Feature: Custom block support for .vue files in Vite plugin

**Motivation**
Vue SFC supports `<docs>`, `<i18n>` custom blocks but Vite plugin
ecosystem lacks standardized extraction API.

**Implementation**
- New `resolveCustomBlock()` hook in plugin context
- Extract blocks by language type during SFC parse
- Register via `configResolved` plugin hook

**Checklist**
- [x] Tests added for markdown, i18n, JSON custom blocks
- [x] Docs updated in `plugin-vue/README.md`
- [x] No breaking changes

**Closes #412**
