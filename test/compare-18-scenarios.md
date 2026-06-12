# oh-my-gh-writing — 18 场景双版对比（新仓库）

精选 18 个全新参考仓库，每场景按 skill 标准生成完整版+精简版，附真实参考链接。

> 仓库来源均不同于 `reference/` 中已有的案例。

---

## 场景1：Bug Report — vitest-dev/vitest

**参考链接**
- Issue 模板分类：https://github.com/vitest-dev/vitest/issues/new/choose
- Bug 模板 YAML：https://github.com/vitest-dev/vitest/blob/main/.github/ISSUE_TEMPLATE/bug_report.yml
- 实际 issue 示例：https://github.com/vitest-dev/vitest/issues/5000

### 完整版

````markdown
---
name: Bug report
about: Create a report to help us improve
title: '[vitest] '
labels: bug
assignees: ''
---

**Describe the bug**
A clear and concise description of what the bug is.

**To Reproduce**
Steps to reproduce the behavior:
1. Create config '...'
2. Create test file '...' with code '....'
3. Run `npx vitest --run`
4. See error

**Expected behavior**
A clear and concise description of what you expected to happen.

**Code**
```ts
// Minimal reproduction
import { describe, it, expect } from 'vitest'

describe('example', () => {
  it('should work', () => {
    expect(1 + 1).toBe(3) // this should pass
  })
})
```

**Environment**
- Vitest version: [e.g. 1.6.0]
- Vite version: [e.g. 5.2.0]
- Node version: [e.g. 20.12.0]
- OS: [e.g. macOS 14.4]
- CI: [e.g. GitHub Actions ubuntu-latest]

**Additional context**
- Does it happen with `--reporter=verbose`?
- Does it happen with `pool: 'forks'` vs `pool: 'threads'`?
- Reproduction repository link (preferred)
````text

### 精简版

````markdown
### Bug: vitest mockReset not clearing mock calls

**Steps:**
1. `mock.mockReset()` in `beforeEach`
2. `mock()` inside test
3. `expect(mock).toHaveBeenCalledTimes(1)` fails with 2

**Expected:** mockReset resets call count to 0
**Actual:** call count is 1 (not reset)

**Env:** vitest 1.6.0 / node 20.12 / macOS 14.4
**Repro:** https://github.com/me/repro
````text

---

## 场景2：Feature Request — vuejs/core

**参考链接**
- Feature Request 模板：https://github.com/vuejs/core/blob/main/.github/ISSUE_TEMPLATE/feature_request.yml
- 功能请求列表：https://github.com/vuejs/core/issues?q=label%3Afeature-request+

### 完整版

````markdown
---
name: Feature request
about: Suggest an idea for this project
title: '[feature] '
labels: feature-request
---

**Motivation**
What problem does this feature solve? Describe the pain point clearly.

Currently, when using `v-model` on a custom component, you can only bind
one `v-model` unless you use named `v-model:propName`. There's no way to
pass multiple two-way bindings concisely.

**Use cases**
1. Form components: `v-model:name`, `v-model:email`, `v-model:password` —
   three separate bindings in a form with 30 fields gets verbose.
2. Dialog component: `v-model:visible`, `v-model:loading`, `v-model:result`.

**Proposed API**
```vue
<Form v-model:object="formData" />
<!--
  Equivalent to:
  <Form :name="formData.name" @update:name="formData.name = $event"
        :email="formData.email" @update:email="formData.email = $event"
        ... />
-->
```

The component would receive a `modelObject` prop and emit update events
for each key automatically.

**Alternatives considered**
1. Use Pinia/Vuex instead of v-model — works but loses the declarative
   two-way binding benefit.
2. Prop getter/setter pattern — works at the component level but verbose.

**Compatibility**
Non-breaking additive change. Existing `v-model` and named `v-model:x`
continue to work identically.
````

### 精简版

````markdown
### Feature: v-model with object shorthand

**Problem:** Forms with many fields need multiple `v-model:xxx` bindings.

**Want:** `v-model:object="formData"` → auto-binds all keys as named v-model.

**Alternative:** Using Pinia, but it's heavier than needed for form state.
````

---

## 场景3：Enhancement — webpack/webpack

**参考链接**
- Enhancement issues：https://github.com/webpack/webpack/issues?q=label%3Aenhancement
- Feature 分类：https://github.com/webpack/webpack/issues?q=label%3Akind-feature

### 完整版

````markdown
### Enhancement: Thread-loader progress reporting

**Current limitation**
`thread-loader` spawns worker pools but provides no visibility into
what each worker is doing. When a build hangs or slows down, you can't
tell which worker is bottlenecked.

**Proposed change**
Expose a `progress` callback from `thread-loader` that reports:
- Active worker count / total workers
- Current module being processed per worker
- Queued module count

```js
// config
module.exports = {
  module: {
    rules: [
      {
        test: /\.js$/,
        use: [
          {
            loader: 'thread-loader',
            options: {
              workers: 4,
              onProgress: (stats) => {
                console.log(`[${stats.active}/${stats.total}] ${stats.current}`)
              }
            }
          },
          'babel-loader'
        ]
      }
    ]
  }
}
```

**Compatibility**
Additive change. Existing `thread-loader` configs with no `onProgress`
continue working identically. No breaking changes.
````

### 精简版

````markdown
### Enhancement: thread-loader progress

**Current:** No visibility into worker pool progress during build.

**Want:** `onProgress` callback reporting active workers + current module.

**No breakage.** Additive config option.
````

---

## 场景4：Discussion — fastify/fastify

**参考链接**
- Discussions 页面：https://github.com/fastify/fastify/discussions
- 示例讨论：https://github.com/fastify/fastify/discussions/categories/ideas

### 完整版

````markdown
### Discussion: Should Fastify adopt ESM-only plugins from v6?

**Background**
Fastify v5 supports both CJS and ESM. The Node.js ecosystem is moving
toward ESM-first — Express 5 ships ESM examples, Hono is ESM-native.

**Options considered**

| Option | Pros | Cons |
|--------|------|------|
| A) Mixed (current) | Zero migration, all plugins work | Slower startup, dual-package tax |
| B) ESM-only v6 | Aligns with ecosystem, faster | Breaks CJS plugins, big migration |
| C) CJS wrappers | Graceful deprecation | Maintenance burden |

**Questions for community**
1. What % of your plugins are ESM vs CJS?
2. Would you accept a major version bump for this change?
3. Is there a tooling gap that blocks ESM adoption?
````

### 精简版

````markdown
### Discussion: ESM-only in v6?

**Current:** CJS + ESM mixed support.
**Proposal:** Drop CJS in Fastify v6.
**Key question:** How many of your plugins would break?

See options table in fastify/fastify#discussions.
````

---

## 场景5：Feature PR — microsoft/playwright

**参考链接**
- PR 模板：https://github.com/microsoft/playwright/blob/main/.github/PULL_REQUEST_TEMPLATE.md
- Feature PRs：https://github.com/microsoft/playwright/pulls?q=label%3Afeature+

### 完整版

````markdown
## Motivation
Add `page.updateURL()` method to programmatically change browser URL
without navigation. Closes #31200.

## Design
```ts
interface Page {
  /** Updates address bar URL without triggering navigation */
  updateURL(url: string): Promise<void>;
}
```
Internally uses `history.pushState` via CDP `Page.navigateToHistoryEntry`.
Works across Chromium/Firefox/WebKit.

## Implementation
- `src/page.ts`: add `updateURL()` calling into browser context
- `src/browser/*.ts`: add CDP/Firefox/WebKit protocol handlers
- `tests/page-update-url.spec.ts`: 3 test cases

## Tests
- [x] Unit tests for URL validation
- [x] Integration: update → verify address bar via `page.url()`
- [x] Cross-browser: Chromium + Firefox + WebKit
- [x] Error case: invalid URL throws

## Checklist
- [x] `npm run build` passes
- [x] `npm run test` passes
- [x] Breaking change: NO
- [x] Documentation updated in `docs/src/api/`
````

### 精简版

````markdown
### Feature: page.updateURL()

**Why:** Programmatic URL change without navigation (#31200)

**What:** `page.updateURL(url: string): Promise<void>`

**Test:** 3 spec files, all 3 engines. Build + test pass. No breaking change.
````

---

## 场景6：Bug Fix PR — axios/axios

**参考链接**
- PRs 列表：https://github.com/axios/axios/pulls
- 修复 PR 示例：https://github.com/axios/axios/pulls?q=label%3Abug+

### 完整版

````markdown
### Fix: CancelToken.signal aborted but never resolved

**Root cause**
When using `CancelToken.source()` with `signal`, calling `cancel()`
sets the abort signal but never resolves `promise`. The caller can't
`await` cancellation completion.

**Fix**
```diff
- // CancelToken constructor
- this.promise = new Promise(resolve => { this.resolvePromise = resolve })
+ // CancelToken constructor
+ this.promise = new Promise(resolve => {
+   this.resolvePromise = resolve
+   if (this.abortController) {
+     this.abortController.signal.addEventListener('abort', () => resolve())
+   }
+ })

- // CancelToken.cancel
- if (reason) this._listeners.forEach(l => l(reason))
+ // CancelToken.cancel
+ if (reason) {
+   this._listeners.forEach(l => l(reason))
+   this.resolvePromise(reason)
+ }
```

**Test**
```ts
test('cancel() resolves promise', async () => {
  const source = axios.CancelToken.source()
  setTimeout(() => source.cancel('manual'), 10)
  await expect(source.token.promise).resolves.toBe('manual')
})
```

**Fixes #6543**
````

### 精简版

````markdown
### Fix: CancelToken promise never resolves

**Root cause:** `cancel()` sets signal but skips `resolvePromise`.

**Fix:** Call `this.resolvePromise(reason)` inside `cancel()`.

**Test:** Added unit test — `cancel()` → promise resolves with reason.

**Fixes #6543**
````

---

## 场景7：Refactor PR — expressjs/express

**参考链接**
- PRs 列表：https://github.com/expressjs/express/pulls
- 重构 PRs：https://github.com/expressjs/express/pulls?q=label%3Arefactor

### 完整版

````markdown
### Refactor: Replace callback chains with async/await in router

**Goal**
Improve readability and error handling of the route matching pipeline.
No behavior changes.

**Invariant**
- All route matching rules identical
- Error handling continues to delegate to `next(err)`
- `req.params`, `req.query`, `req.route` unchanged

**Before (callback chain)**
```js
Layer.prototype.handle_request = function (req, res, next) {
  var fn = this.handle
  if (fn.length > 3) return next()
  try {
    fn(req, res, next)
  } catch (err) {
    next(err)
  }
}
```

**After (async)**
```js
Layer.prototype.handle_request = async function (req, res, next) {
  try {
    await this.handle(req, res, next)
  } catch (err) {
    next(err)
  }
}
```

**Tests**
- Full pass of existing test suite (847 tests)
- No new tests needed — behavior invariant

**Fixes** (none)
**Breaking:** NO
````

### 精简版

````markdown
### Refactor: Router layer async/await

**Goal:** Replace callback chain with async/await. No behavior change.

**Change:** `Layer.prototype.handle_request` → async wrapper.

**Test:** 847 existing tests pass. Breaking: NO.
````

---

## 场景8：Documentation PR — vuejs/core

**参考链接**
- 文档 PR 列表：https://github.com/vuejs/core/pulls?q=label%3Adocumentation
- Vue 文档仓库：https://github.com/vuejs/docs

### 完整版

````markdown
### Docs: Clarify `defineModel()` usage with TypeScript

**Location**
`packages/docs/guide/components/v-model.md` lines 120-145

**Original**
```
Using defineModel with TypeScript requires a generic type parameter.
```

**Updated**
```
Using `defineModel()` with TypeScript requires a generic type parameter
to specify the model value type:

```vue
<script setup lang="ts">
const count = defineModel<number>('count', { default: 0 })
//         ^^^^^^^^ type parameter required
</script>
```

You can also use an interface for complex model values:

```vue
<script setup lang="ts">
interface UserForm {
  name: string
  email: string
}

const form = defineModel<UserForm>('form', { required: true })
</script>
```

**No code changes**
This is a pure documentation improvement. No source code was modified.
````

### 精简版

````markdown
### Docs: defineModel() TypeScript examples

**Where:** `v-model.md` defineModel section

**Change:** Added `defineModel<number>()` and `defineModel<UserForm>()`
working examples with type parameter explained.

**No code change.**
````

---

## 场景9：Code Review — hashicorp/vault

**参考链接**
- PR Reviews：https://github.com/hashicorp/vault/pulls
- 代码审查指南：https://github.com/hashicorp/vault/blob/main/contributing.md#code-review-process

### 完整版

````markdown
### Review: `vault/barrier.go` — seal wrapping refactor

**File:** `vault/barrier.go:312-335`

**Issue (blocking)**
```go
func (b *Barrier) wrapSeal(ctx context.Context) error {
    // Missing context cancellation check
    data, err := b.seal.Encrypt(ctx, plaintext)
    // err is swallowed on line 318
    return nil
}
```
The function returns `nil` even when `b.seal.Encrypt` fails. This will
cause callers to proceed with unencrypted data, believing it's sealed.

**Suggested fix**
```go
func (b *Barrier) wrapSeal(ctx context.Context) error {
    select {
    case <-ctx.Done():
        return ctx.Err()
    default:
    }
    data, err := b.seal.Encrypt(ctx, plaintext)
    if err != nil {
        return fmt.Errorf("seal encrypt: %w", err)
    }
    // ... continue
}
```

**Severity:** BLOCKING — data corruption risk
````

### 精简版

````markdown
### Review: barrier.go wrapSeal error swallowed

**Line 312-318:** `b.seal.Encrypt()` error is discarded, returns nil.

**Fix:** Check `err`, return `fmt.Errorf("seal encrypt: %w", err)`.

**Severity:** BLOCKING
````

---

## 场景10：Standard Commit — gin-gonic/gin

**参考链接**
- Commit 历史：https://github.com/gin-gonic/gin/commits/master
- 贡献指南：https://github.com/gin-gonic/gin/blob/master/CONTRIBUTING.md

### 完整版

````
fix(context): prevent concurrent map read/write on Keys

The `Keys` map in `Context` is accessed from multiple goroutines
(one per middleware handler) but lacks synchronization. When one
handler writes `c.Set("key", val)` while another reads `c.Get("key")`,
it triggers a fatal `concurrent map read and map write` panic.

Use `sync.RWMutex` to protect `Keys` access:
- `Get()` acquires `RLock`
- `Set()` acquires `Lock`
- No performance impact for read-heavy workloads (RWMutex optimizes
  for concurrent reads)

Fixes #4123
````

### 精简版

````
fix(context): protect Keys map with sync.RWMutex

Prevents fatal concurrent map read/write panic when middleware
runs in parallel. Fixes #4123.
````

---

## 场景11：README — vercel/hyper

**参考链接**
- Hyper README：https://github.com/vercel/hyper

### 完整版

````markdown
# Hyper

[![Build](https://img.shields.io/github/actions/workflow/status/vercel/hyper/ci.yml?branch=main)](https://github.com/vercel/hyper/actions)
[![Release](https://img.shields.io/github/v/release/vercel/hyper)](https://github.com/vercel/hyper/releases)
[![License](https://img.shields.io/badge/license-MIT-blue)](https://github.com/vercel/hyper/blob/main/LICENSE)

> A terminal built on web technologies.

## Features

- **GPU-accelerated rendering** — smooth 60fps even with massive output
- **Plugin ecosystem** — 50+ plugins via `.hyper.js`
- **Split panes** — `Cmd+D` to split, `Cmd+Shift+D` to close
- **Cross-platform** — macOS / Windows / Linux

## Quick Start

```bash
# macOS
brew install --cask hyper

# Windows (winget)
winget install Hyper

# Linux (deb)
curl -LO https://releases.hyper.is/.../hyper.deb
sudo dpkg -i hyper.deb
```

## Configuration

Edit `~/.hyper.js` to customize shell, font, colors, and plugins:

```js
module.exports = {
  config: {
    shell: '/bin/zsh',
    fontSize: 14,
    fontFamily: '"Fira Code", "Hack", monospace',
    cursorColor: '#52bd68',
    css: ''
  },
  plugins: ['hyper-search', 'hyper-tabs']
}
```

## Documentation

- [Getting Started](https://hyper.is/docs)
- [Plugin API](https://hyper.is/docs/plugins)
- [Contributing](https://github.com/vercel/hyper/blob/canary/CONTRIBUTING.md)

## License

MIT
````

### 精简版

````markdown
# Hyper

> A terminal built on web technologies.

```bash
brew install --cask hyper
```

GPU-accelerated · Plugin ecosystem · Cross-platform

[Contributing](https://github.com/vercel/hyper/blob/canary/CONTRIBUTING.md) · MIT
````

---

## 场景12：CONTRIBUTING — tensorflow/tensorflow

**参考链接**
- CONTRIBUTING.md：https://github.com/tensorflow/tensorflow/blob/master/CONTRIBUTING.md
- 开发者指南：https://www.tensorflow.org/community/contribute

### 完整版

````markdown
# Contributing to TensorFlow

We welcome contributions — bug fixes, documentation, new ops, and more.

## Code of Conduct

This project follows [TensorFlow Code of Conduct](https://github.com/tensorflow/tensorflow/blob/master/CODE_OF_CONDUCT.md).

## Getting Started

1. **Fork** the repository
2. **Set up** development environment:
   ```bash
   git clone https://github.com/your-username/tensorflow.git
   cd tensorflow
   pip install -r requirements-dev.txt
   python configure.py
   ```
3. **Create a branch**: `git checkout -b my-feature-branch`

## Contribution Workflow

1. File an **Issue** describing the change
2. Wait for **triage** — a TensorFlow team member will label it
3. Write the **code** following the style guide
4. Add **tests** — Python (`tf.test`) or C++ (`gtest`)
5. Run **CI** locally: `bazel test //tensorflow/python/...`
6. Submit a **Pull Request** referencing the issue

## Code Style

- **Python**: follow [PEP 8](https://peps.python.org/pep-0008/) with 80-char limit
- **C++**: follow [Google C++ Style Guide](https://google.github.io/styleguide/cppguide.html)
- Run `pylint` and `clang-format` before committing

## PR Checklist

- [ ] Code compiles (`bazel build //tensorflow/...`)
- [ ] Tests pass (`bazel test //tensorflow/python/...`)
- [ ] Documentation updated (docstrings + external docs)
- [ ] Breaking changes labeled in PR description
- [ ] GPU/CPU compatibility verified

## Review Process

- At least one **code owner** review required
- CI must be green
- Rebase before merge (no merge commits)
````

### 精简版

````markdown
# Contributing to TensorFlow

1. Fork → branch → develop
2. `bazel test //tensorflow/python/...` before committing
3. PR checklist: build → test → docs → breaking
4. One owner review + green CI → merge

See [CONTRIBUTING.md](https://github.com/tensorflow/tensorflow/blob/master/CONTRIBUTING.md) for full guide.
````

---

## 场景13：CHANGELOG — webpack/webpack

**参考链接**
- CHANGELOG.md：https://github.com/webpack/webpack/blob/main/CHANGELOG.md
- v5.90.0 release：https://github.com/webpack/webpack/releases/tag/v5.90.0

### 完整版

````markdown
## [5.90.0] - 2024-03-01

### Breaking Changes
- Minimum Node.js version raised to 18.12.0
- Dropped `experiments.css` flag (CSS support is now stable)

### Features
- New `output.ecmaVersion` option for targeting specific ES versions
- `module.parser.javascript.url` now supports `"relative"` mode
- Tree-shaking improvements for `export * from` re-exports

### Bug Fixes
- Fix crash when `splitChunks` returns empty name
- Fix incorrect source map generation for CSS modules
- Fix HMR not updating when re-exporting from intermediate modules

### Performance
- Improved chunk graph traversal for large projects (15% faster builds)
- Cache `resolve.alias` lookups to reduce filesystem calls

### Internal
- Migrate CI from Azure Pipelines to GitHub Actions
- TypeScript migration: `lib/` now 60% typed
````

### 精简版

````markdown
## [5.90.0] - 2024-03-01

**Breaking:** Node 18.12+ required, `experiments.css` removed (stable).

**Features:** `output.ecmaVersion`, `url: "relative"`, tree-shake re-exports.

**Fixes:** splitChunks crash, CSS source maps, HMR re-export updates.

**Perf:** 15% faster builds via chunk graph optimization.
````

---

## 场景14：Release Notes — microsoft/playwright

**参考链接**
- Releases 页面：https://github.com/microsoft/playwright/releases
- 示例 Release：https://github.com/microsoft/playwright/releases/tag/v1.40.0

### 完整版

````markdown
# Playwright v1.44.0

[![npm](https://img.shields.io/npm/v/playwright)](https://www.npmjs.com/package/playwright)

## Highlights

### New `locator.or()` for fallback matching

```ts
await page.getByText('Submit').or(page.getByText('Save')).click()
```

### Trace Viewer improvements
- Network request previews (response body, headers)
- Source map support for stack traces

### Experimental: Android automation

Full Android device control via `android.launch()`:
```ts
const device = await android devices[0]
await device.shell('am start -a android.intent.action.VIEW -d https://example.com')
```

## Breaking Changes

- Minimum Node.js version is now 18
- Deprecated `page.waitForNavigation()` removed (use `page.waitForURL()`)

## Full Changelog

https://github.com/microsoft/playwright/releases/tag/v1.44.0

## Contributors

Thanks to @alice, @bob, @charlie for their contributions!
````

### 精简版

````markdown
# Playwright v1.44.0

**Highlights:** `locator.or()` for fallback matching · Trace Viewer network previews · Experimental Android

**Breaking:** Node 18+ · `waitForNavigation` removed (use `waitForURL`)

[Full changelog](https://github.com/microsoft/playwright/releases/tag/v1.44.0)
````

---

## 场景15：Migration Guide — webpack/webpack

**参考链接**
- Webpack 5 迁移文档：https://webpack.js.org/migrate/5/
- 迁移指南仓库：https://github.com/webpack/webpack/issues?q=label%3Amigration

### 完整版

````markdown
# Migrating from webpack 4 to 5

## Overview

webpack 5 removes deprecated features from v4 and introduces persistent
caching, named chunk IDs, and tree-shaking improvements.

## Breaking Changes

### 1. Node.js polyfills removed

webpack 4 auto-polyfilled Node.js modules (`crypto`, `buffer`, `path`).
In v5 you must install them explicitly:

```bash
npm install crypto-browserify buffer path-browserify --save-dev
```

```js
// webpack.config.js
resolve: {
  fallback: {
    crypto: require.resolve('crypto-browserify'),
    buffer: require.resolve('buffer'),
    path: require.resolve('path-browserify')
  }
}
```

### 2. `json` loader removed

```diff
- import data from './data.json'
+ import data from './data.json' assert { type: 'json' }
```

JSON files are now handled natively — remove any `json-loader` rules.

### 3. Automatic entry point IDs removed

```diff
- output: { filename: '[name].js' }
+ output: { filename: '[name].[contenthash].js' }
```

Use `optimization.chunkIds: 'named'` for readable chunk names in dev.

## Rollback

If migration fails, revert to webpack 4:
```bash
npm install webpack@4 webpack-cli@3 --save-dev
```
Restore old `webpack.config.js` from backup.

## Timeline

- webpack 4: continued to receive security patches until Dec 2023
- webpack 5: actively maintained
````

### 精简版

````markdown
# Webpack 4 → 5 Migration

**Main changes:**
- Node polyfills: install `crypto-browserify`, `buffer`, `path-browserify`
- JSON: remove `json-loader`, use `assert { type: 'json' }`
- Content hash: use `[contenthash]` for long-term caching

**Rollback:** `npm install webpack@4`

**Timeline:** v4 security patches ended Dec 2023.
````

---

## 场景16：RFC — vuejs/core

**参考链接**
- Vue RFCs 仓库：https://github.com/vuejs/rfcs
- 示例 RFC：https://github.com/vuejs/rfcs/blob/master/active-rfcs/0000-template.md

### 完整版

````markdown
# RFC: Provide/Inject with Type Safety

## Summary
Add typed `provide`/`inject` that surfaces type mismatches at compile time.

## Motivation
Current `provide`/`inject` is fully dynamic — if a parent provides
`number` and child injects it as `string`, there's no warning.

## Detailed Design

### New API
```ts
import { createProvideKey } from 'vue'

const userKey = createProvideKey<User>('user')

// Provider
provide(userKey, currentUser) // ✅ type-checked

// Consumer
const user = inject(userKey) // ✅ user is User | undefined
const user2 = inject(userKey, defaultUser) // ✅ user is User
```

### Implementation
- `createProvideKey<T>(name: string): InjectionKey<T>`
- Returns a symbol-based key carrying the type
- `inject` overload checks key type against the returned generic

### Prior Art
- React Context with `createContext<T>()`
- Angular `InjectionToken<T>`

## Drawbacks
- Adds ~50 lines to runtime
- Existing code unaffected (backward compatible)

## Unresolved Questions
- Should `createProvideKey` accept an optional default value?
- Deep readonly: should `inject` return `DeepReadonly<T>`?
````

### 精简版

````markdown
# RFC: Typed Provide/Inject

**Problem:** `provide`/`inject` has no type checking across components.

**Solution:** `createProvideKey<T>(name)` returns `InjectionKey<T>`.
`provide(key, val)` and `inject(key)` are now type-safe.

**Prior art:** React `createContext<T>`, Angular `InjectionToken<T>`.

**No breaking change.**
````

---

## 场景17：Issue Form YAML — microsoft/playwright

**参考链接**
- Bug 表单 YAML：https://github.com/microsoft/playwright/blob/main/.github/ISSUE_TEMPLATE/bug.yml
- Issues 分类：https://github.com/microsoft/playwright/issues/new/choose

### 完整版

````yaml
name: Bug Report
description: File a bug report for Playwright
title: '[Bug]: '
labels: [bug, needs-triage]
body:
  - type: markdown
    attributes:
      value: |
        Thanks for reporting! Please fill out the form below.

  - type: textarea
    id: description
    attributes:
      label: Description
      description: A clear description of the bug
      placeholder: |
        When I run `page.click('button')`, the click never reaches...
    validations:
      required: true

  - type: textarea
    id: reproduction
    attributes:
      label: Reproduction
      description: Minimum code to reproduce
      render: typescript
      placeholder: |
        import { test, expect } from '@playwright/test';
        test('example', async ({ page }) => {
          await page.goto('...');
          await page.click('button');
        });
    validations:
      required: true

  - type: dropdown
    id: browser
    attributes:
      label: Browser
      multiple: true
      options:
        - Chromium
        - Firefox
        - WebKit
    validations:
      required: true

  - type: input
    id: version
    attributes:
      label: Playwright version
      placeholder: 'e.g., 1.44.0'
    validations:
      required: true

  - type: dropdown
    id: os
    attributes:
      label: OS
      options:
        - macOS
        - Windows
        - Linux
    validations:
      required: true
````

### 精简版

````yaml
name: Bug Report
description: File a bug report
title: '[Bug]: '
labels: [bug]
body:
  - type: textarea
    id: description
    attributes:
      label: Description
      placeholder: What happened?
    validations:
      required: true

  - type: textarea
    id: reproduction
    attributes:
      label: Code
      render: typescript
    validations:
      required: true

  - type: input
    id: version
    attributes:
      label: Version
    validations:
      required: true
````

---

## 场景18：PR Template — vitest-dev/vitest

**参考链接**
- PR 模板：https://github.com/vitest-dev/vitest/blob/main/.github/PULL_REQUEST_TEMPLATE.md

### 完整版

````markdown
## Description

Please include a summary of the change and which issue is fixed.

Fixes # (issue)

## Type of change

- [ ] Bug fix (non-breaking change which fixes an issue)
- [ ] New feature (non-breaking change which adds functionality)
- [ ] Breaking change (fix or feature that would break existing functionality)
- [ ] Documentation update

## How Has This Been Tested?

- [ ] `pnpm test` passes
- [ ] `pnpm lint` passes  
- [ ] Added new unit tests for the change
- [ ] Updated existing tests if needed

## Configuration impact

- [ ] New config option added (documented in `docs/config/`)
- [ ] Existing config behavior changed (migration note required)
- [ ] No config changes

## Checklist

- [ ] My code follows the project's style guidelines
- [ ] I have performed a self-review of my own code
- [ ] I have commented my code where necessary
- [ ] I have updated the documentation accordingly
- [ ] My changes generate no new warnings

## Additional context

Add any other context or screenshots about the pull request here.
````

### 精简版

````markdown
## Description

Fixes #.

## Type

- [ ] Bug fix / [ ] Feature / [ ] Breaking / [ ] Docs

## Checklist

- [ ] `pnpm test` passes
- [ ] `pnpm lint` passes
- [ ] Self-reviewed
````

---

*Generation date: 2026-06-11*
*Skill: oh-my-gh-writing (18 场景双版对比)*
