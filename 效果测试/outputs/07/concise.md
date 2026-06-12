---
scenario: Refactor PR
mode: concise
case-sources: https://github.com/spring-projects/spring-boot, https://github.com/scikit-learn/scikit-learn
input-prompt: ../../prompts/07-refactor-pr.md
---

### Refactor: Consolidate utility functions into utils/ directory

**Goal**
Reduce file fragmentation. 15 standalone utility files consolidated
into 3 domain-organized files under `src/utils/`.

**Invariant**
No behavior changes. All exports preserved. Import paths updated.

**Changes**
- `src/formatDate.ts`, `src/parseCSV.ts`, `src/validateEmail.ts` → `src/utils/format.ts`
- `src/localStorage.ts`, `src/cookie.ts` → `src/utils/storage.ts`
- `src/debounce.ts`, `src/throttle.ts`, `src/memoize.ts` → `src/utils/perform.ts`

**Tests**
- [x] All 47 existing tests pass (no new tests needed — behavior invariant)
