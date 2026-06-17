# Migration Guide — 写作标准

## 适用场景
引导用户从旧 API、旧配置或旧发布迁移到目标发布。

## 输出边界

Migration Guide 只写真实升级路径。环境变量、codemod、GA 日期、下线日期、兼容周期和回滚方案必须有来源。

## 标准结构

1. **概览**：迁移范围 + 目标版本
2. **迁移步骤**（分步操作，每步含旧代码→新代码 diff）
3. **API 变更表**（旧 API → 新 API 映射）
4. **自动迁移工具**（codemod 脚本等，已存在时）
5. **回滚方案**（如何恢复；未知时写待确认）
6. **废弃时间线**（各版本支持周期；只在已知时写）

## 信息不足时

- 缺少旧/新 API 映射时，先列 `To confirm` 表格。
- 没有自动迁移工具时，不写 codemod。
- 没有回滚路径时，写 `Rollback: To confirm`。

## 禁止编造项

- 不编造环境变量、命令、兼容周期、下线日期、迁移工具、数据迁移步骤或支持平台。
- 不把 release notes 当成完整 migration guide，除非它确实包含迁移步骤。

## 高质量参考来源

| 来源 | 可借鉴点 |
|------|----------|
| GitHub migrations docs | https://docs.github.com/en/migrations |
| GitLab update docs | https://docs.gitlab.com/update/ |
| pandas whatsnew / migration notes | https://pandas.pydata.org/docs/whatsnew/index.html |
| React 19 Upgrade Guide | https://react.dev/blog/2024/04/25/react-19-upgrade-guide |
| Django upgrade guide | https://docs.djangoproject.com/en/stable/howto/upgrade-version/ |

## 必含元素 Checklist
- [ ] 迁移步骤（旧→新）
- [ ] API/配置变更表
- [ ] 回滚方案或待确认项
- [ ] 不虚构环境变量、自动迁移命令、GA 日期、下线日期或兼容周期
