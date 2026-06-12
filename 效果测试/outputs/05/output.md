## Feature: Custom block support for .vue files

**Motivation**
Vue SFCs support custom blocks (`<docs>`, `<i18n>`) but Vite's plugin-vue doesn't expose them. Users must write custom SFC parsers.

**Design**
Add `customBlocks` option to `@vitejs/plugin-vue`:
```ts
vue({ customBlocks: ['docs', 'i18n'] })
```
Each custom block becomes available as `?customBlock` query.

**Implementation**
- `packages/plugin-vue/src/index.ts`: parse `customBlocks` option
- `packages/plugin-vue/src/script.ts`: extract blocks during SFC parse
- `packages/plugin-vue/src/hmr.ts`: HMR for custom block changes

**Verification (to run)**
- Unit: custom block extraction per type (markdown, JSON, YAML)
- Integration: `?customBlock` query returns correct content
- HMR: change triggers re-render without full page reload
- Edge: no `customBlocks` option (backward compatible)
