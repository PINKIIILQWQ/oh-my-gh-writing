---
scenario: Documentation PR
mode: concise
case-sources: https://github.com/ionic-team/ionic-framework, https://github.com/angular/angular-cli
input-prompt: ../../prompts/08-documentation-pr.md
---

### Docs: Add best-practice examples to Vue Router navigation guards

**Location**
`docs/guide/advanced/navigation-guards.md`, lines 89-145

**Change**
Added practical examples for the three in-component guards:

```vue
<script setup>
// beforeRouteEnter — access component instance via next(vm => {})
// beforeRouteUpdate — reuse on param change without full reload
// beforeRouteLeave — confirm unsaved changes
</script>
```

Each example includes loading state, error handling, and TypeScript types.
