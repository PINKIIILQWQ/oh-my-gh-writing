---
scenario: Feature PR
mode: full-detail
case-sources: https://github.com/freeCodeCamp/freeCodeCamp, https://github.com/facebook/react-native, https://github.com/tauri-apps/tauri
input-prompt: ../../prompts/05-feature-pr.md
---

## Feature: Custom block support in Vite Vue plugin

### Motivation
Vue Single File Components can contain custom blocks beyond `<template>`,
`<script>`, `<style>`:
<docs>Custom block</docs>
Vite's `@vitejs/plugin-vue` currently ignores these. Users must write
custom SFC parsers to extract them.

### Design
Add `customBlocks` option to plugin configuration:

```ts
// vite.config.ts
export default defineConfig({
  plugins: [
    vue({
      customBlocks: ['docs', 'i18n']
    })
  ]
})
```

### Implementation
1. `packages/plugin-vue/src/index.ts`: add `customBlocks` option parsing
2. `packages/plugin-vue/src/script.ts`: extract custom blocks during SFC
3. `packages/plugin-vue/src/hmr.ts`: HMR support for custom block changes

### Tests
- [x] Unit: custom block extraction per block type
- [x] Integration: block content available via ?customBlock query
- [x] HMR: changing custom block triggers re-render
- [x] Edge: no customBlocks option (backward compatible)

### Checklist
- [x] Build passes: `pnpm build`
- [x] Tests pass: `pnpm test`
- [x] No breaking changes
- [x] Docs updated
