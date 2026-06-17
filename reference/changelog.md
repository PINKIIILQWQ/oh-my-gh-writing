# CHANGELOG — 写作标准

## 适用场景
按版本记录变更日志，面向用户升级时查看。

## 输出边界

CHANGELOG 是版本历史，不是发布宣传稿。必须基于真实版本、日期、PR/Issue、提交或 release notes。没有证据时，不写编号、发布日期、移除时间线或迁移链接。

## 标准结构

```
## [Unreleased]

## [版本号] - YYYY-MM-DD

### Added
- 新增能力

### Changed
- 行为、API、文档或内部实现变化

### Fixed
- 修复的问题列表

### Removed
- 移除内容及迁移路径

### Deprecated
- 废弃功能及时间线

### Security
- 安全修复或公告链接
```

只保留有内容的分类。不要输出空的 `Performance`、`Deprecation`、`Security` 或 breaking-change 段落。

## 信息不足时

- 缺少日期时写 `YYYY-MM-DD` 或 `TBD`，不要猜发布日期。
- 缺少 PR/Issue 编号时省略编号，不写 `#123` 占位。
- 变更类型不确定时，用 `Changed`，不要强行归到 Breaking 或 Security。

## 禁止编造项

- 不编造 bug 编号、贡献者名单、迁移链接、废弃时间线、移除版本或安全公告。
- 不把 release notes 的营销语气搬进 changelog。
- 不把参考仓库的分类名强套到目标项目。

## 高质量参考来源

| 来源 | 可借鉴点 |
|------|----------|
| Keep a Changelog | https://keepachangelog.com/en/1.1.0/ |
| npm CLI CHANGELOG | https://github.com/npm/cli/blob/latest/CHANGELOG.md |
| ESLint CHANGELOG | https://github.com/eslint/eslint/blob/main/CHANGELOG.md |
| Node.js v24 CHANGELOG | https://github.com/nodejs/node/blob/main/doc/changelogs/CHANGELOG_V24.md |
| React CHANGELOG | https://github.com/react/react/blob/main/CHANGELOG.md |
| Conventional Commits | https://www.conventionalcommits.org/en/v1.0.0/ |

## 必含元素 Checklist
- [ ] `[Unreleased]` 或明确版本号 + 发布日期
- [ ] 按类型分类（Added / Changed / Fixed / Removed / Deprecated / Security）
- [ ] PR/Issue 引用（已知时）
- [ ] 不虚构 bug 编号、文档链接、迁移链接、废弃时间线或移除版本
