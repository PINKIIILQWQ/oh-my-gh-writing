# Migration Guide — 经典案例

---

## 精细版（完整迁移指南）

### 案例 1：prisma/prisma (43k⭐)

**来源：** Prisma 官方文档（prisma.io/docs/guides/upgrade-guides）

Prisma 的升级指南是业界标杆级迁移文档，结构：

```
## Upgrade to Prisma 5 from Prisma 4

### Overview
- Prisma 5 drops support for Node.js 14
- Minimum TypeScript version 5.0

### Breaking Changes
#### 1. Node.js 14 no longer supported
- Migration: Upgrade to Node.js 16 or later

#### 2. `@prisma/client` Middleware API changed
- Before: `prisma.$use(async (params, next) => { ... })`
- After: `prisma.$use(async (params, next) => { ... return next(params) })`

#### 3. Deprecated APIs removed
- `findOne()` → use `findUnique()` or `findFirst()`
- `update()` no longer returns the old record

### How to Upgrade
1. `npm install prisma@5 @prisma/client@5`
2. Run `prisma generate`
3. Update deprecated API calls

### Rollback
`npm install prisma@4 @prisma/client@4`

### Timeline
- Prisma 4: maintenance until Dec 2025
```

**特点：** 逐个 Breaking Change 配 before/after 代码对比 + 升级步骤 + 回滚方案 + 废弃时间线。

---

### 案例 2：Prisma — Node.js → Edge 迁移指南

**来源：** Prisma 官方文档

```
# Migrating from Node.js to Edge Runtime

## Why migrate?
- Lower cold starts (5ms vs 200ms)
- Global deployment

## Changes needed

### 1. Data source configuration
Before: `provider = "postgresql"`
After: `provider = "postgresql"` + `relationMode = "prisma"`

### 2. Remove unsupported features
- Raw queries with `$queryRaw`
- Interactive transactions

### 3. Package updates
- `@prisma/client` → `@prisma/adapter-neon` or `@prisma/adapter-planetscale`

### Testing your migration
```

**特点：** 问题 → 方案 → 步骤 → 验证，完整的迁移叙事。

---

### 案例 3：tc39/proposals (ECMAScript 迁移)

**来源：** https://github.com/tc39/proposals

ECMAScript 提案的迁移说明通常包含在 Stage 4 提案中：

```
## Migration from legacy API

### Old API
```js
// Callback-based
fs.readFile('/path', (err, data) => { ... })
```

### New API
```js
// Promise-based
const data = await fs.readFile('/path')
```

### Compatibility
The old API continues to work but is deprecated.
```

**特点：** 语言标准级的迁移说明，强调向后兼容。

---

## 普通版（简洁迁移指南）

### 案例 4：apache/echarts (62k⭐)

ECharts 的版本迁移说明通常：

```
## Upgrading from v4 to v5

### Breaking Changes
- `series.type: 'graph'` properties renamed
- `tooltip.formatter` callback signature changed

### New Features
- Dataset support
- Improved SVG renderer

### Deprecated
- `legend.selectedMode` removed
```

**特点：** 简洁的分类列表 + 重要变更的代码示例（可选）。

---

### 案例 5：jestjs/jest (45k⭐)

Jest 在 CHANGELOG 和博客中发布迁移指南：

```markdown
## Migrating from Jest 29 to 30

### Major changes
- `jest.useFakeTimers()` default changed
- `jest.mock()` auto-mocking behavior updated

### How to update
1. `npm install jest@30`
2. Run `jest --clearCache`
3. Check for deprecated matcher warnings
```

---

### 案例 6：hashicorp/vagrant (27k⭐)

Vagrant 的 CHANGELOG 直接包含迁移说明：

```markdown
## 2.4.0

### Upgrade notes
- Provider API v2 is now the default
- Vagrantfile `config.vm.provider` syntax updated
- VirtualBox 7.0+ required

### Rollback
`vagrant version` to check current, then reinstall 2.3.x
```

---

> 收集日期：2026-06-12
