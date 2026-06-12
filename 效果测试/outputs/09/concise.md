---
scenario: Code Review
mode: concise
case-sources: https://github.com/google/eng-practices, https://github.com/swiftlang/swift
input-prompt: ../../prompts/09-code-review.md
---

### Review: JWT token refresh in auth module

**File:** `src/auth/jwt.ts:45-78`

**Issue (blocking)**
```ts
// Line 52: refresh token stored in localStorage
const refreshToken = localStorage.getItem('refresh_token');
```
LocalStorage is accessible via XSS. Use httpOnly cookie instead.

**Issue (important)**
```ts
// Line 71: no expiration check before decode
const payload = jwt.decode(token);
```
`jwt.decode()` does not verify signature or expiration. Use `jwt.verify()`.

**Nit**
```ts
// Line 33: console.log left in production code
console.log('Token refreshed successfully');
```
Remove before merge.
