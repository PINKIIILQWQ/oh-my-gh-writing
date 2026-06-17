# Discussion — 写作标准

## 适用场景
公开讨论功能方向、方案选择，需要社区输入。

## 输出边界

Discussion 用来征求意见，不替社区做决定。它可以比较方案，但不能把未确认方案写成最终路线图、已批准 RFC 或维护者共识。

## 标准结构

1. **背景**：讨论的来由
2. **动机**：为什么需要讨论
3. **方案对比**：各方案优缺点（表格形式）
4. **征求意见**：明确需要社区回答的问题

## 信息不足时

- 方案不成熟时，保留 `Open questions`，不要强行给推荐方案。
- 缺少影响面时，列出需要确认的用户群、API、兼容性或维护成本。
- 如果用户要的是未来能力请求而非征求意见，路由到 Feature Request。

## 禁止编造项

- 不编造投票结果、维护者态度、路线图状态、RFC 编号或时间表。
- 不把讨论写成 PR 描述或 release announcement。

## 高质量参考来源

| 来源 | 可借鉴点 |
|------|----------|
| GitHub Discussions docs | https://docs.github.com/en/discussions |
| React RFCs | https://github.com/reactjs/rfcs |
| Rust RFCs | https://github.com/rust-lang/rfcs |
| Python PEP 1 | https://peps.python.org/pep-0001/ |
| Kubernetes Enhancement Proposals | https://github.com/kubernetes/enhancements/blob/master/keps/README.md |

## 必含元素 Checklist
- [ ] 讨论背景
- [ ] 方案选项
- [ ] 征求意见点
