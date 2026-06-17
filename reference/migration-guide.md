# Migration Guide — 写作标准

## 适用场景
引导用户从旧 API、旧配置或旧发布迁移到目标发布。

## 输出边界

Migration Guide 只写真实升级路径。环境变量、codemod、GA 日期、下线日期、兼容周期和回滚方案必须有来源。

## 标准结构

必需：

1. **Who needs this**：谁需要迁移，哪些用户不受影响。
2. **Before / After**：旧用法和新用法；可用代码、配置、命令或行为描述。
3. **Step-by-step migration**：按可执行顺序写迁移步骤。
4. **Known breaking changes**：只列已知不兼容点。

条件项：

5. **Codemod / automation**：仅当已有工具或命令时写。
6. **Rollback**：仅当仓库或用户提供回滚方式时写；否则 `Rollback: To confirm`。
7. **Deprecation timeline**：仅当版本计划、日期或支持周期有证据时写。
8. **Compatibility matrix**：仅当平台、版本或依赖范围有证据时写。

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
- [ ] API/配置/行为变化说明
- [ ] 回滚、codemod、废弃时间线和兼容矩阵只在有证据时出现
- [ ] 不虚构环境变量、自动迁移命令、GA 日期、下线日期或兼容周期
