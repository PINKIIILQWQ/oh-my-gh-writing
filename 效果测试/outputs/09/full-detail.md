---
scenario: Code Review
mode: full-detail
case-sources: https://github.com/google/eng-practices, https://github.com/rails/rails
input-prompt: ../../prompts/09-code-review.md
---

## Review: PR #42 — JWT token refresh

### File: `src/auth/jwt.ts`

#### Line 45-50: Token storage (BLOCKING)
```ts
localStorage.setItem('access_token', token);
localStorage.setItem('refresh_token', refreshToken);
```
**Problem:** LocalStorage is accessible via XSS. Any injected script can
exfiltrate tokens.
**Fix:** Store `refresh_token` in httpOnly secure cookie. Store
`access_token` in memory only (JavaScript variable), not in storage.

#### Line 71-73: Token verification (BLOCKING)
```ts
const payload = jwt.decode(token);
if (payload.exp < Date.now() / 1000) { ... }
```
**Problem:** `jwt.decode()` does NOT verify the signature. An attacker
can forge tokens with arbitrary expiration.
**Fix:** Use `jwt.verify(token, secret)` which validates signature
AND expiration automatically.

#### Line 33: Development artifact (NIT)
```ts
console.log('Token refreshed successfully');
```
Remove before production merge.

#### Line 81-85: Error handling (IMPORTANT)
```ts
catch (e) {
  return null; // silently ignores all errors
}
```
**Problem:** Silent catch hides network errors, rate limiting, etc.
**Fix:** Log the error, differentiate between auth failure and system error.

### Summary
3 blocking issues (token storage, signature verification, silent catch)
must be fixed before merge. 1 nit (console.log).
