# Feature PR — 写作标准

## 适用场景
提交新功能/特性的 Pull Request，需覆盖设计、实现、测试和升级。

## 输出边界

Feature PR 只描述当前分支或 diff 已经实现的能力。没有实现证据时，应转为 Feature Request；没有测试证据时，写 `Verification to run`。

## 标准结构

1. **动机**：为什么需要这个功能；关联 Issue # 只在已知时写
2. **设计**：变更的设计思路；架构图只在已有素材或复杂设计时写
3. **实现**：改了什么文件、如何改；必须来自 diff 或用户输入
4. **测试**：新增测试覆盖/手动验证步骤；未知时写“Verification to run”
5. **风险 / 兼容性**：仅在确有影响时写 Breaking、迁移或回滚
6. **用户影响**：用户如何使用或观察到新能力

## 信息不足时

- 缺少 diff 时，只能写 PR 草稿或待补信息，不写具体文件和测试结论。
- 缺少 Issue 编号时，写 `Related issue: TBD` 或删除该字段。
- 视觉变更没有截图时，写 `Screenshot: TODO`，不要编造图片。

## 禁止编造项

- 不编造 Issue、测试通过状态、CI、截图、benchmark、文件路径或 release note。
- 不把参考 PR 模板里的 SIG、cherry-pick、label 复制到无关项目。
- 不把未来计划写成已经完成的功能。

## 高质量参考来源

| 来源 | 可借鉴点 |
|------|----------|
| GitHub PR template docs | https://docs.github.com/en/communities/using-templates-to-encourage-useful-issues-and-pull-requests/creating-a-pull-request-template-for-your-repository |
| Kubernetes PR Template | https://github.com/kubernetes/kubernetes/blob/master/.github/PULL_REQUEST_TEMPLATE.md |
| React PR Template | https://github.com/react/react/blob/main/.github/PULL_REQUEST_TEMPLATE.md |
| Moby PR Template | https://github.com/moby/moby/blob/master/.github/PULL_REQUEST_TEMPLATE.md |
| ESLint PR Template | https://github.com/eslint/eslint/blob/main/.github/PULL_REQUEST_TEMPLATE.md |
| Tailwind CSS PR Template | https://github.com/tailwindlabs/tailwindcss/blob/main/.github/PULL_REQUEST_TEMPLATE.md |

## 必含元素 Checklist
- [ ] 变更描述
- [ ] 关联 Issue #（已知时）
- [ ] 测试结果或待运行验证项
- [ ] 不把未证实的测试、CI、文件路径或 Issue 编号写成事实

## 可选项
- 截图/录屏：视觉变更且素材可得时使用
