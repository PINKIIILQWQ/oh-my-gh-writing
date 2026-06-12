---
scenario: Bug Fix PR
mode: full-detail
case-sources: https://github.com/bitcoin/bitcoin, https://github.com/getsentry/sentry, https://github.com/ClickHouse/ClickHouse
input-prompt: ../../prompts/06-bug-fix-pr.md
---

## Fix: CancelToken promise never resolves after cancel()

### Root cause
In `lib/cancel/CancelToken.js`, the `cancel()` method fires all registered
listeners but does not call `resolvePromise`. This means any code awaiting
`source.token.promise` hangs indefinitely:

```js
const source = axios.CancelToken.source();
// source.token.promise never resolves after cancel()
```

### Before
```js
CancelToken.prototype.cancel = function (reason) {
  if (this._listeners) {
    this._listeners.forEach(function (listener) {
      listener(reason);
    });
  }
};
```

### After
```js
CancelToken.prototype.cancel = function (reason) {
  if (this._listeners) {
    this._listeners.forEach(function (listener) {
      listener(reason);
    });
  }
  this.reason = reason;
  this.resolvePromise(reason);
};
```

### Test coverage
```ts
describe('CancelToken', () => {
  it('should resolve the promise when cancelled', async () => {
    const source = axios.CancelToken.source();
    setTimeout(() => source.cancel('Operation cancelled'), 10);
    await expect(source.token.promise).resolves.toBe('Operation cancelled');
  });

  it('should reject with Cancel if request throws', () => {
    const source = axios.CancelToken.source();
    source.cancel();
    return source.token.promise.catch((cancel) => {
      expect(cancel.message).toBe('Request cancelled');
    });
  });
});
```

### Fixes #6543
