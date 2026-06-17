# Code Review — 写作标准

## 适用场景
对 Pull Request 或提交进行代码审查评论。

## 输入边界

必须先读取 diff、PR 文件、提交内容或用户贴出的代码后再给出文件/行号级结论。只有 PR URL 但无法访问内容时，不要编造 `src/foo.ts:42` 之类的位置；改为说明“需要 diff 才能逐行审查”，并提供基于已知变更主题的风险清单。

## 标准结构

1. **位置**（文件 + 行号）
2. **问题**（当前代码的问题）
3. **根因**（为什么这是错的）
4. **建议**（如何修改）
5. **Severity**：blocking / major / minor / nit

## 信息不足时

- 没有 diff 时，不输出行号级发现。
- 只能看到摘要时，输出风险清单和需要查看的文件。
- 不确定严重程度时，用 `minor` 或 `question`，不要夸大。

## 禁止编造项

- 不编造文件路径、行号、调用链、测试失败、性能影响或安全漏洞。
- 不把风格偏好写成 blocking，除非项目规范明确要求。

## 高质量参考来源

| 来源 | 可借鉴点 |
|------|----------|
| GitHub PR review docs | https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/reviewing-changes-in-pull-requests/about-pull-request-reviews |
| Google Engineering Review Guide | https://google.github.io/eng-practices/review/ |
| Go contribution review | https://go.dev/doc/contribute#review |
| Kubernetes Review Ownership | https://github.com/kubernetes/community/blob/main/contributors/guide/owners.md |
| Rust compiler contributing guide | https://github.com/rust-lang/rustc-dev-guide/blob/main/src/contributing.md |
| Chromium review respect guide | https://chromium.googlesource.com/chromium/src/+/main/docs/cr_respect.md |

## 必含元素 Checklist
- [ ] 标注位置（文件/行号；必须来自真实 diff 或代码）
- [ ] 问题说明
- [ ] 建议修复方案
- [ ] Severity 标注
- [ ] 无法读取代码时只输出审查计划或主题风险，不输出虚构发现
