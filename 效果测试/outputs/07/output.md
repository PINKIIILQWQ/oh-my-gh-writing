## Refactor: Consolidate utility files into structured utils/

### Refactoring goal
The `src/` directory had 15 standalone utility files at root level,
making imports fragile and discoverability poor. Goal is to group
related utilities without changing any behavior.

### Before
```
src/
  formatDate.ts
  parseCSV.ts
  validateEmail.ts
  validatePhone.ts
  debounce.ts
  throttle.ts
  memoize.ts
  localStorage.ts
  cookie.ts
  sleep.ts
  retry.ts
  logger.ts
  hashPassword.ts
  generateToken.ts
  encrypt.ts
```

### After
```
src/utils/
  format.ts        # date, CSV, validators
  perform.ts       # debounce, throttle, memoize, sleep, retry
  storage.ts       # localStorage, cookie
  auth.ts          # hash, token, encrypt
  logger.ts        # standalone (no grouping needed)
```

### Invariant assertions
- All public exports re-exported from new barrel files
- No function signatures changed
- No dependencies added or removed

### Test verification
- [x] `npm run test` passes (47 tests)
- [x] `npm run build` passes (TypeScript strict mode)
- [x] Import correctness verified via `tsc --noEmit`
