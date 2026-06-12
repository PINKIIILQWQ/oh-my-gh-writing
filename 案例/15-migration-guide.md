# Migration Guide — 经典案例（完整原文）

> 格式：Markdown · 迁移指南文件

---

## 精细版（完整迁移指南原文）

### 案例 1：mui/material-ui (95k⭐)

**仓库：** https://github.com/mui/material-ui
**迁移指南 v4→v5：** https://mui.com/material-ui/migration/migration-v4/

MUI 的 v4→v5 迁移指南是业界标杆，完整结构如下：

```markdown
# Migration from v4 to v5

## Introduction
This guide describes the changes needed to migrate Material-UI from v4 to v5.

## Getting Started
1. Update React to at least v17
2. Update Material-UI packages:
```bash
npm install @mui/material @mui/styles @emotion/react @emotion/styled
```

## Breaking Changes

### 1. JSS to Emotion
Material-UI v4 used JSS for styling. v5 uses Emotion by default.

**Before (v4):**
```jsx
import { makeStyles } from '@material-ui/core/styles';
const useStyles = makeStyles({ root: { color: 'red' } });
```

**After (v5):**
```jsx
import { styled } from '@mui/material/styles';
const Root = styled('div')({ color: 'red' });
```

### 2. Core package renamed
**Before:** `@material-ui/core`
**After:** `@mui/material`

### 3. Component imports restructured
```diff
- import { Button, TextField } from '@material-ui/core';
+ import Button from '@mui/material/Button';
+ import TextField from '@mui/material/TextField';
```

### 4. Theme structure changes
- `theme.palette.type` → `theme.palette.mode`
- `theme.shadows` array length changed
- `theme.spacing()` now returns `px` values by default

## Codemod
Run the preset-safe codemod to automate migration:
```bash
npx @mui/codemod v5.0.0/preset-safe
```

## New Features in v5
- `sx` prop for inline styling
- Styled engine agnostic (use Emotion or styled-components)
- Improved TypeScript support

## Deprecations
- `@material-ui/styles` is deprecated (use Emotion)
- `makeStyles` and `withStyles` will be removed in v6
```

---

### 案例 2：remix-run/react-router (53k⭐)

**仓库：** https://github.com/remix-run/react-router
**迁移指南 v5→v6：** https://reactrouter.com/en/main/upgrading/v5

```markdown
# Upgrading from v5 to v6

React Router v6 introduces several breaking changes from v5.
This guide will help you migrate your application.

## Breaking: `<Switch>` is replaced with `<Routes>`

**Before (v5):**
```jsx
<Switch>
  <Route exact path="/" component={Home} />
  <Route path="/about" component={About} />
</Switch>
```

**After (v6):**
```jsx
<Routes>
  <Route path="/" element={<Home />} />
  <Route path="/about" element={<About />} />
</Routes>
```

## Breaking: `component` prop → `element` prop
All route rendering now uses `element` instead of `component` or `render`.

## Breaking: `useHistory` → `useNavigate`

**Before:**
```jsx
const history = useHistory();
history.push('/home');
```

**After:**
```jsx
const navigate = useNavigate();
navigate('/home');
```

## New Features
- Relative routes and links
- Nested routing with `<Outlet>`
- `useParams` now supports wildcard routes
- `Route` path patterns with `:param` and `*`

## Automatic Migration
Use the `react-router-dom-v5-compat` package for gradual migration.
```

---

### 案例 3：emberjs/ember.js (22k⭐)

**仓库：** https://github.com/emberjs/ember.js
**迁移指南：** https://deprecations.emberjs.com/

Ember 的迁移指南强调渐进式迁移：

```markdown
# Ember 3.x → 4.x Migration

## Deprecation Guide
Each deprecated API has a dedicated deprecation guide page:

1. `Ember.Component` → `@glimmer/component`
2. `Ember.Object` → native ES classes
3. `this.get()` / `this.set()` → native property access

## Codemods Available
Ember provides automated codemods via `ember-cli-update`:
```bash
npx ember-cli-update
npx ember-cli-update --run-codemods
```

## Timeline
| Version | Status | End of Life |
|---------|--------|-------------|
| 3.x LTS | Maintenance | Dec 2022 |
| 4.x LTS | Active | Dec 2023 |
| 5.x     | Latest | Active |

## Octane vs Classic
Ember Octane (2021+) introduced modern patterns:
- Glimmer components instead of Classic components
- Tracked properties instead of computed properties
- Native classes instead of Ember.Object

## Rollback
If migration fails, revert to previous Ember CLI version:
```bash
npm install ember-cli@3.28 --save-dev
```
```

---

## 简洁写法（简洁迁移指南）

### 案例 4：angular/components (25k⭐)

**仓库：** https://github.com/angular/components
**升级指南：** https://github.com/angular/components/blob/main/guides/UPGRADE.md

Angular Material 升级指南分类结构：

```
## Upgrading to v15

### Breaking Changes
- [list individual breaking changes with before/after]

### New deprecations
- [deprecated APIs and replacements]

### Removed APIs
- [fully removed APIs with migration path]
```

### 案例 5：styled-components/styled-components (34k⭐)

**仓库：** https://github.com/styled-components/styled-components

简洁迁移结构：

- **API Changes**: Old API → New API + Reason
- **Migration Steps**: 具体操作步骤
- **Rollback**: 如何回退到迁移前状态
- **Timeline**: 废弃的时间线

### 案例 6：reduxjs/redux-toolkit (11k⭐)

**仓库：** https://github.com/reduxjs/redux-toolkit

精简迁移：

```
## Migrating from Redux Core to Redux Toolkit

### configureStore replaces createStore
### createSlice replaces switch-case reducers
### createAsyncThunk replaces manual thunks
```

---

### 参考仓库链接

- https://github.com/mui/material-ui — Migration Guide v4→v5
- https://github.com/remix-run/react-router — Upgrade v5→v6
- https://github.com/emberjs/ember.js — 3.x→4.x Migration
- https://github.com/angular/components — Upgrade Guide
- https://github.com/styled-components/styled-components — Migration
- https://github.com/reduxjs/redux-toolkit — RTK Migration

---

> 收集日期：2026-06-12
