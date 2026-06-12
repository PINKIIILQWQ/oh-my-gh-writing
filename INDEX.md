# oh-my-gh-writing 索引

这个文件是仓库的全量导航。README 只负责解释项目是什么和如何开始；这里负责把场景标准、内部文档、测试材料和维护入口串起来。

Agent 执行写作任务时优先读取 [`SKILL.md`](./SKILL.md) 和对应 `reference/*.md`；`DOCS/` 与 `test/` 是维护材料，不是运行时规则本体。

## 阅读路径

| 层级 | 入口 | 适合谁 | 内容粒度 |
|------|------|--------|----------|
| 0 | [`README.md`](./README.md) | 第一次打开仓库的人 | 项目定位、安装、最短路径 |
| 1 | [`INDEX.md`](./INDEX.md) | 想找某个场景或文档的人 | 全量索引和目录 |
| 2 | [`SKILL.md`](./SKILL.md) | Agent / skill 使用者 | 入口规则、场景识别、摘要标准 |
| 3 | [`reference/`](./reference) | 要改写法标准的人 | 每场景完整版/普通版/checklist |
| 4 | [`DOCS/`](./DOCS) | 维护者 | 采集计划、outline、设计演进 |
| 5 | [`test/`](./test) | 维护者 / 验证者 | 18 场景测试和全量报告 |

## 18 场景索引

| # | 类别 | 场景 | 使用时机 | 标准文件 |
|---|------|------|----------|----------|
| 1 | Issue | Bug Report | 报告可复现缺陷 | [`reference/bug-report.md`](./reference/bug-report.md) |
| 2 | Issue | Feature Request | 提议新功能或新 API | [`reference/feature-request.md`](./reference/feature-request.md) |
| 3 | Issue | Enhancement | 改进现有能力 | [`reference/enhancement.md`](./reference/enhancement.md) |
| 4 | Issue | Discussion | 开放式社区讨论 | [`reference/discussion.md`](./reference/discussion.md) |
| 5 | PR | Feature PR | 新功能 Pull Request | [`reference/feature-pr.md`](./reference/feature-pr.md) |
| 6 | PR | Bug Fix PR | 修复缺陷 Pull Request | [`reference/bug-fix-pr.md`](./reference/bug-fix-pr.md) |
| 7 | PR | Refactor PR | 不改变行为的重构 | [`reference/refactor-pr.md`](./reference/refactor-pr.md) |
| 8 | PR | Documentation PR | 文档改动 Pull Request | [`reference/documentation-pr.md`](./reference/documentation-pr.md) |
| 9 | Review | Code Review | 审查代码变更 | [`reference/code-review.md`](./reference/code-review.md) |
| 10 | Commit | Standard Commit | 写提交信息 | [`reference/standard-commit.md`](./reference/standard-commit.md) |
| 11 | Docs | README | 项目首页文档 | [`reference/readme.md`](./reference/readme.md) |
| 12 | Docs | CONTRIBUTING | 贡献指南 | [`reference/contributing.md`](./reference/contributing.md) |
| 13 | Docs | CHANGELOG | 版本变更记录 | [`reference/changelog.md`](./reference/changelog.md) |
| 14 | Release | Release Notes | 发布说明 | [`reference/release-notes.md`](./reference/release-notes.md) |
| 15 | Release | Migration Guide | 迁移指南 | [`reference/migration-guide.md`](./reference/migration-guide.md) |
| 16 | Design | RFC | 设计提案 | [`reference/rfc.md`](./reference/rfc.md) |
| 17 | Templates | Issue Form YAML | GitHub Issue 表单 | [`reference/issue-form-yaml.md`](./reference/issue-form-yaml.md) |
| 18 | Templates | PR Template | Pull Request 模板 | [`reference/pr-template.md`](./reference/pr-template.md) |

测试统一入口见 [`test/README.md`](./test/README.md)。

## 目录索引

| 目录 | 作用 | 入口 |
|------|------|------|
| [`reference/`](./reference) | 场景标准、工具分析、格式武器库 | [`reference/readme.md`](./reference/readme.md) |
| [`DOCS/`](./DOCS) | 内部设计过程和采集计划 | [`DOCS/README.md`](./DOCS/README.md) |
| [`test/`](./test) | 验证材料、双版样例、全量报告 | [`test/README.md`](./test/README.md) |
| [`assets/`](./assets) | README 和项目展示素材 | [`assets/oh-my-gh-writing-logo.png`](./assets/oh-my-gh-writing-logo.png) |

## Reference 文件索引

| 类型 | 文件 |
|------|------|
| Issue | [`bug-report.md`](./reference/bug-report.md), [`feature-request.md`](./reference/feature-request.md), [`enhancement.md`](./reference/enhancement.md), [`discussion.md`](./reference/discussion.md) |
| PR | [`feature-pr.md`](./reference/feature-pr.md), [`bug-fix-pr.md`](./reference/bug-fix-pr.md), [`refactor-pr.md`](./reference/refactor-pr.md), [`documentation-pr.md`](./reference/documentation-pr.md) |
| Review / Commit | [`code-review.md`](./reference/code-review.md), [`standard-commit.md`](./reference/standard-commit.md) |
| Docs | [`readme.md`](./reference/readme.md), [`contributing.md`](./reference/contributing.md), [`changelog.md`](./reference/changelog.md) |
| Release / Design | [`release-notes.md`](./reference/release-notes.md), [`migration-guide.md`](./reference/migration-guide.md), [`rfc.md`](./reference/rfc.md) |
| Templates | [`issue-form-yaml.md`](./reference/issue-form-yaml.md), [`pr-template.md`](./reference/pr-template.md) |
| Appendix | [`tool-analysis.md`](./reference/tool-analysis.md), [`weapons.md`](./reference/weapons.md) |

## 内部文档索引

| 文件 | 内容 |
|------|------|
| [`DOCS/README.md`](./DOCS/README.md) | 文档目录和渐进式披露规则 |
| [`DOCS/collection-plan.md`](./DOCS/collection-plan.md) | 参考材料采集计划 |
| [`DOCS/skill-outline.md`](./DOCS/skill-outline.md) | v1 skill outline |
| [`DOCS/skill-outline-v2.md`](./DOCS/skill-outline-v2.md) | v2 outline 和扩展原则 |

## 验证材料索引

| 文件 | 内容 |
|------|------|
| [`test/README.md`](./test/README.md) | 18 场景测试提示词和预期产出 |
| [`test/compare-18-scenarios.md`](./test/compare-18-scenarios.md) | 18 场景完整版/精简版样例 |
| [`test/full-run-2026-06-11.md`](./test/full-run-2026-06-11.md) | 2026-06-11 全量检查报告 |

## 维护规则

- 新增场景时，同步更新 `SKILL.md`、`INDEX.md`、`README.md`、`test/README.md` 和对应 `reference/*.md`
- 新增文档时，优先挂到 `DOCS/README.md`，再按需要挂到这里
- README 只放最短路径和核心入口，避免再次变成大而全的文档
- 深层细节必须有上层入口可达，不能只散落在目录里
