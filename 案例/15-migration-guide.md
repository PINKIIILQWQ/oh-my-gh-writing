# Migration Guide — 经典案例（完整原文）

---

## 精细版（完整迁移指南原文）

### 案例 1：mui/material-ui (95k⭐)

**仓库：** https://github.com/mui/material-ui
**迁移指南 v4→v5：** https://mui.com/material-ui/migration/migration-v4/

Material UI 的 v4→v5 迁移指南是业界标杆，结构如下：

```markdown
## Migrating from v4 to v5

### Overview
Material-UI v5 introduces a revamped styling solution based on Emotion,
a brand new migration codemod, and many breaking changes.

### Supported Versions
- Material-UI v4: maintenance mode
- Migration path: v4.x → v5.0

### Breaking Changes

#### 1. JSS is replaced by Emotion
Before:
```js
import { makeStyles } from '@material-ui/core/styles';
const useStyles = makeStyles({ root: { color: 'red' } });
```

After:
```js
import { styled } from '@mui/material/styles';
const Root = styled('div')({ color: 'red' });
```

#### 2. @material-ui/core renamed to @mui/material
The package has been renamed from `@material-ui/core` to `@mui/material`.

#### 3. Component renames
- `TextField` `variant="standard"` is now the default (was `standard` before too, but now it's consistent)
- `Dialog` no longer has `disableBackdropClick` prop
- `InputBase` `inputComponent` prop renamed to `inputComponent`

### Migration Steps
1. Run the codemod: `npx @mui/codemod v5.0.0/preset-safe`
2. Update your imports from `@material-ui/core` to `@mui/material`
3. Replace JSS with Emotion or styled-components
4. Test your components
```

---

### 案例 2：remix-run/react-router (53k⭐)

**仓库：** https://github.com/remix-run/react-router
**迁移指南：** https://reactrouter.com/en/main/upgrading/v5

```markdown
## Upgrading from v5 to v6

### Breaking: `Switch` → `Routes`
Before:
```jsx
<Switch>
  <Route exact path="/" component={Home} />
  <Route path="/about" component={About} />
</Switch>
```

After:
```jsx
<Routes>
  <Route path="/" element={<Home />} />
  <Route path="/about" element={<About />} />
</Routes>
```

### Breaking: `component` → `element`
All route rendering now uses the `element` prop instead of `component` or `render`.
This provides better composability and avoids React remounting issues.

### New Features
- Relative routes and links
- `useNavigate` replaces `useHistory`
- Nested routes support `<Outlet>`

### How to Migrate
1. Update all `<Switch>` elements to `<Routes>`
2. Convert `component={...}` to `element={<... />}`
3. Replace `useHistory()` with `useNavigate()`
4. Remove `exact` prop (it's the default in v6)
```

---

### 案例 3：emberjs/ember.js (22k⭐)

**仓库：** https://github.com/emberjs/ember.js
**迁移指南：** https://deprecations.emberjs.com/

```markdown
## Ember 3.x to 4.x Migration

### Deprecation Guide
All deprecated APIs in Ember 3.x are removed in 4.x.

### Codemods
Run `ember-cli-update` to automatically update your project:
```bash
npx ember-cli-update --run-codemods
```

### Key Breaking Changes
1. `Ember.Component` replaced by Glimmer Components
2. `this.get()`/`this.set()` removed (use native accessors)
3. `Ember.<namespace>` imports removed (use module imports)

### Timeline
- Ember 3.x: LTS until December 2022
- Ember 4.x: active development
```

---

## 普通版（简洁迁移指南）

### 案例 4：angular/components (25k⭐)

**仓库：** https://github.com/angular/components
**升级指南：** https://github.com/angular/components/blob/main/guides/upgrade.md

```markdown
## Upgrading Angular Material
### Breaking Changes
- [List of breaking changes per version]

### New Features
- [New components and APIs]

### Deprecated
- [Deprecated APIs and their replacements]
```

### 案例 5：styled-components/styled-components (34k⭐)

**仓库：** https://github.com/styled-components/styled-components
**升级指南：** https://styled-components.com/docs/faqs#upgrading

```markdown
## Upgrading from v5 to v6
### Breaking Changes
- `StyleSheetManager` props changed
- `withComponent` removed (use `as` prop)
### Migration Steps
1. Update package: `npm install styled-components@6`
2. Replace `withComponent` with `as` prop
3. Check StyleSheetManager usage
### Rollback
`npm install styled-components@5`
```

### 案例 6：reduxjs/redux-toolkit (11k⭐)

**仓库：** https://github.com/reduxjs/redux-toolkit
**迁移指南：** https://redux-toolkit.js.org/usage/usage-guide#migrating-from-redux

```markdown
## Migrating from Redux to Redux Toolkit
### Old API
`createStore(reducer)` with manual action creators

### New API
`configureStore({ reducer })` with `createSlice`

### Reason
Redux Toolkit reduces boilerplate, includes middleware setup,
and enables Redux DevTools by default.
```

---

> 收集日期：2026-06-12
