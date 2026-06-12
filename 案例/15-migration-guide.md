# Migration Guide — 经典案例

---

## 精细版（完整迁移指南）

### 案例 1：mui/material-ui (95k⭐)

MUI 的迁移指南 v4→v5 是业界标杆之一：

```markdown
## Migrating from v4 to v5

### Breaking Changes (逐个列出)
#### 1. JSS → Emotion
- Before: `import { makeStyles } from '@material-ui/core'`
- After: `import { styled } from '@mui/material/styles'`

#### 2. Component renames
- `@material-ui/core` → `@mui/material`
- `TextField` API changes

### New Features
- Styled engine agnostic
- New `sx` prop

### Codemod
`npx @mui/codemod v5.0.0/preset-safe`
```

---

### 案例 2：remix-run/react-router (53k⭐)

React Router v5→v6 迁移指南：

```markdown
## Upgrading from v5 to v6

### Breaking: Switch → Routes
- Before: `<Switch><Route path="..." component={X}/></Switch>`
- After: `<Routes><Route path="..." element={<X/>}/></Routes>`

### Breaking: component → element
All route children now use `element` prop instead of `component` or `render`.

### New Features
- Relative routes and links
- `useNavigate` replaces `useHistory`
```

---

### 案例 3：emberjs/ember.js (22k⭐)

Ember 的升级指南强调渐进式迁移：

```markdown
## Ember 3.x → 4.x Migration

### Deprecation Guide
[逐个废弃 API + 替代方案]

### Codemods Available
`ember-cli-update` 自动升级

### Timeline
- Ember 3.x: LTS until Dec 2022
- Ember 4.x: actively maintained
```

---

## 普通版（简洁迁移指南）

### 案例 4：angular/components (25k⭐)

Angular Material 迁移：Breaking Changes → New → Deprecated → Upgrade Steps 分类列表。

### 案例 5：styled-components/styled-components (34k⭐)

API 变更 + 迁移步骤 + 回滚方案，简洁分类。

### 案例 6：reduxjs/redux-toolkit (11k⭐)

简洁迁移：Old API → New API → Migration Reason，每条变更附带迁移动机说明。

---

### 参考仓库链接

- https://github.com/mui/material-ui — Migration Guide v4→v5
- https://github.com/remix-run/react-router — Upgrade v5→v6
- https://github.com/emberjs/ember.js — 3.x→4.x Migration

> 收集日期：2026-06-12
