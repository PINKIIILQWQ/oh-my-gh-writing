## Fix: CancelToken.cancel() does not resolve token promise

**Root cause**
`source.cancel(reason)` fires the abort signal and all registered listeners but never calls `this.resolvePromise`, leaving `source.token.promise` in a pending state indefinitely.

**Change**
```diff
  CancelToken.prototype.cancel = function (reason) {
    if (this._listeners) {
      this._listeners.forEach(function (listener) { listener(reason); });
    }
+   this.reason = reason;
+   this.resolvePromise(reason);
  };
```

**Verification (to run)**
- Unit: `source.cancel('test')` → `source.token.promise` resolves with `'test'`
- Integration: fetch cancelled with `signal` does not hang
- Edge: double cancel does not throw

**Fixes #TODO**
