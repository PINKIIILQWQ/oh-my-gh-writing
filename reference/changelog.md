# CHANGELOG — 精细标准

## 适用场景
按版本记录变更日志，面向用户升级时查看。

## 精细标准（electron, npm/cli, pandas）

### 结构
```
## [版本号] - YYYY-MM-DD

### Breaking Changes
- 不兼容变更及迁移路径

### Features
- 新功能列表

### Bug Fixes
- 修复的问题列表

### Performance
- 性能改进

### Deprecation
- 废弃功能及时间线
```

### 参考仓库写法

**electron/electron**
- Keep a Changelog 最佳实践代表
- Breaking / Features / Fixes / Performance / Deprecation 严格分类
- 每条变更带 PR # 引用

**npm/cli**
- 混合风格：版本 + 日期 + 类型分类
- 合并次要变更减少噪声
- 每条带 Issue/PR 引用

**pandas-dev/pandas**
- 极致的版本覆盖（追溯到 0.x）
- Deprecation 体系最完整（FutureWarning → 废弃时间线 → 移除）
- 含贡献者致谢

## CHANGELOG — 中等标准（eslint, graphql-js, prisma）

### 结构
版本 + 日期 + 类型分类 + PR 引用

### 参考仓库写法

**eslint/eslint**
- 规则变更独立记录
- Breaking / Features / Fixes / Documentation 分类

**graphql/graphql-js**
- 干净简洁：版本 + 日期 + PR 列表
- Breaking 用 `⚠` 标记

**prisma/prisma**
- 产品级变更日志
- 含 CLI + Client + Migrate 分类
- 含 GitHub Release 镜像

## 必含元素 Checklist
- [ ] 版本号 + 发布日期
- [ ] 按类型分类（Breaking / Features / Fixes）
- [ ] PR/Issue 引用
