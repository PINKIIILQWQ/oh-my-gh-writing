---
scenario: Bug Fix PR
mode: concise
case-sources: https://github.com/microsoft/terminal, https://github.com/Homebrew/brew
input-prompt: ../../prompts/06-bug-fix-pr.md
---

### Fix: CancelToken promise never resolves on cancel

**Root cause**
When calling `source.cancel('reason')`, the AbortController signal fires
but `this.resolvePromise` is never called, leaving the promise pending.

**Fix**
```diff
- // CancelToken.cancel
- if (reason) this._listeners.forEach(l => l(reason));
+ if (reason) {
+   this._listeners.forEach(l => l(reason));
+   this.resolvePromise(reason);
+ }
```

**Test**
```ts
test('cancel resolves promise', async () => {
  const source = axios.CancelToken.source();
  setTimeout(() => source.cancel('test'), 10);
  await expect(source.token.promise).resolves.toBe('test');
});
```

**Fixes #6543**
