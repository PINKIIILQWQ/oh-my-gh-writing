# Feature Request — 写作标准

## 适用场景
请求新功能或能力增强，需要阐明使用场景和期望行为。

## 输出边界

Feature Request 描述未来希望支持的能力。没有实现 diff 时，不写成 PR；没有 API 证据时，不把接口、版本、兼容范围写成已确认事实。

## 标准结构

1. **动机**：当前缺失的能力或痛点
2. **Use Case**（列出 2-3 个典型场景，含具体输入→输出）
3. **期望行为**：用户可观察到的行为；只有 API/CLI/配置类请求才写接口草案
4. **替代方案**：当前 workaround，为什么不够
5. **兼容性**：对现有 API 的影响；未知版本或支持范围用 `TBD`

## 信息不足时

- 缺少 API 细节时，用行为描述代替接口签名。
- 缺少目标版本时，用 `Target version: TBD`。
- 需求仍在征求意见时，路由到 Discussion，而不是替用户决定方案。

## 禁止编造项

- 不编造 API 签名、兼容版本、迁移成本、性能数字或维护者态度。
- 不把搜索页、讨论页里的单个观点写成项目共识。
- 不把“希望支持”写成“已经实现”。

## 高质量参考来源

| 来源 | 可借鉴点 |
|------|----------|
| GitHub Issue templates | https://docs.github.com/en/communities/using-templates-to-encourage-useful-issues-and-pull-requests/configuring-issue-templates-for-your-repository |
| Angular Feature Request | https://github.com/angular/angular/blob/main/.github/ISSUE_TEMPLATE/2-feature-request.yaml |
| TypeScript Feature Request | https://github.com/microsoft/TypeScript/blob/main/.github/ISSUE_TEMPLATE/feature_request.yml |
| VS Code Feature Request | https://github.com/microsoft/vscode/blob/main/.github/ISSUE_TEMPLATE/feature_request.md |
| React RFCs | https://github.com/reactjs/rfcs |
| Rust RFCs | https://github.com/rust-lang/rfcs |

## 必含元素 Checklist
- [ ] 使用场景描述
- [ ] 期望行为；仅在需要时写 API/CLI/配置草案
- [ ] 替代方案
- [ ] API、版本和兼容性没有被写成已确认事实，除非用户或资料已提供证据
