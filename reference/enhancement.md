# Enhancement — 写作标准

## 适用场景
对已有功能做增量改进，不是新增能力。

> 与 Feature Request 区别：Enhancement 是改进已有功能的行为/性能/API，Feature Request 是增加尚未存在的能力。

## 输出边界

Enhancement 改进已有能力，不等同于全新功能。必须说明当前行为和改进后的行为；性能、内存、延迟等数字必须有证据。

## 标准结构

1. **当前限制**：现有功能的不足
2. **改进效果**：改进后应该怎么样
3. **兼容性**：对现有 API/行为的破坏程度
4. **Before / After**：可使用代码、配置、命令输出、截图、行为描述或性能数据；没有证据时不要编造。
5. **验证方式**：如何确认改进有效；没有真实数据时不要写 benchmark 数字。

## 信息不足时

- 不清楚现有行为时，先要求或标记 `Current behavior: TODO`。
- 不确定是否 breaking 时，写 `Compatibility impact: To confirm`。
- 没有 benchmark 时，只写验证计划，不写数字。

## 禁止编造项

- 不编造性能提升、内存下降、兼容版本、迁移路径或用户规模。
- 不把 feature request 写成 enhancement；现有能力不存在时改走 Feature Request。

## 高质量参考来源

| 来源 | 可借鉴点 |
|------|----------|
| GitHub Issue templates | https://docs.github.com/en/communities/using-templates-to-encourage-useful-issues-and-pull-requests/configuring-issue-templates-for-your-repository |
| Angular Feature Request | https://github.com/angular/angular/blob/main/.github/ISSUE_TEMPLATE/2-feature-request.yaml |
| TypeScript Feature Request | https://github.com/microsoft/TypeScript/blob/main/.github/ISSUE_TEMPLATE/feature_request.yml |
| Kubernetes Enhancement Proposals | https://github.com/kubernetes/enhancements/blob/master/keps/README.md |
| React RFCs | https://github.com/reactjs/rfcs |
| Rust RFCs | https://github.com/rust-lang/rfcs |

## 必含元素 Checklist
- [ ] 当前行为说明
- [ ] 改进后的行为
- [ ] 兼容性分析或 `To confirm`
- [ ] 性能、内存、延迟等数字只在有证据时出现
