## Refactor: Consolidate utility functions into src/utils/

**Goal**
Reduce file fragmentation at root level. 15 standalone utility files merged into 4 domain-organized files.

**Before**
```
src/
  formatDate.ts  parseCSV.ts  validateEmail.ts  debounce.ts
  throttle.ts  memoize.ts  localStorage.ts  cookie.ts  sleep.ts
  retry.ts  logger.ts  hashPassword.ts  generateToken.ts  encrypt.ts
```

**After**
```
src/utils/
  format.ts      # date, CSV, validators
  perform.ts     # debounce, throttle, memoize, sleep, retry
  storage.ts     # localStorage, cookie
  auth.ts        # hash, token, encrypt
  logger.ts      # standalone (no grouping needed)
```

**Invariant**
All exports preserved. No function signatures changed. No new dependencies.

**Verification (to run)**
- `npm test` passes (existing test suite)
- `tsc --noEmit` — no import errors
- Check that barrel re-exports match original API
