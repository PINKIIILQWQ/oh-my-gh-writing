# Migration Guide — 精细标准

## 适用场景
引导用户从旧 API/版本迁移到新版本。

## 精细标准（fluentui, pandas, gitlabhq）

### 结构
1. **概览**：迁移范围 + 目标版本
2. **迁移步骤**（分步操作，每步含旧代码→新代码 diff）
3. **API 变更表**（旧 API → 新 API 映射）
4. **自动迁移工具**（codemod 脚本等）
5. **回滚方案**（如何恢复）
6. **废弃时间线**（各版本支持周期）

### 参考仓库写法

**microsoft/fluentui**
- 按组件分类的迁移指南
- 代码 diff 对比 + Reasons 解释为何改
- 含 codemod 自动迁移

**pandas-dev/pandas**
- 最系统的迁移文档：公函 + 版本 + 废弃时间线
- Deprecation → FutureWarning → 移除，三级警告体系

**gitlabhq/gitlabhq**
- 产品级迁移：从版本 A → B 的完整操作手册
- 数据库迁移 + API 变更 + 配置变更

## Migration Guide — 中等标准（reactjs/rfcs, react-spectrum, hugo）

### 结构
旧 vs 新对比 → 迁移步骤

### 参考仓库写法

**reactjs/rfcs**
- RFC 级迁移说明：设计动机 + 旧新对比 + CoD 模式

**adobe/react-spectrum**
- 版本迁移 + 组件迁移
- 示例代码对比

**gohugoio/hugo**
- 配置迁移说明
- 含 shortcode 兼容说明

## 必含元素 Checklist
- [ ] 迁移步骤（旧→新）
- [ ] API/配置变更表
- [ ] 回滚方案

## 参考链接

| 仓库 | 链接 |
|------|------|
| fluentui 迁移指南 | https://github.com/microsoft/fluentui/wiki/Migration-Guides |
| pandas 迁移指南 | https://pandas.pydata.org/docs/whatsnew/index.html |
| GitLab 升级文档 | https://docs.gitlab.com/ee/update/ |
| reactjs/rfcs 迁移 RFC | https://github.com/reactjs/rfcs |
| react-spectrum 迁移 | https://react-spectrum.adobe.com/releases.html |
| Hugo 升级指南 | https://gohugo.io/getting-started/upgrading/ |
