---
scenario: Documentation PR
mode: full-detail
case-sources: https://github.com/DefinitelyTyped/DefinitelyTyped, https://github.com/vuejs/core
input-prompt: ../../prompts/08-documentation-pr.md
---

## Docs: Add best-practice navigation guard examples

### Location
`packages/docs/guide/advanced/navigation-guards.md`

### Original
```md
The `beforeRouteEnter` guard does NOT have access to `this`,
because the guard is called before the navigation is confirmed.
You can access the component instance by passing a callback to `next`.
```

### Updated
Added full worked example for each guard type:

- **beforeRouteEnter**: Access component via `next(vm => vm.loadData())`
- **beforeRouteUpdate**: Reuse on `:id` param changes without full remount
- **beforeRouteLeave**: Confirm dialog for unsaved form data

Each example includes:
- Loading state management
- Error boundary handling
- TypeScript generics for typed route params
- Abort controller pattern for cancelling in-flight requests

### No code changes
This is a pure documentation improvement.
