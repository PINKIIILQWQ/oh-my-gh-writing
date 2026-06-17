# RFC — 写作标准

## 适用场景
提出重大功能或设计变更，需要社区讨论和决策。

## 输出边界

RFC 可以包含创造性的设计草案，但要把草案、备选方案和开放问题说清楚。不要把尚未验证的编译策略、运行时兼容性、性能影响或标准委员会状态写成既定事实。

## 标准结构

1. **摘要**（1-2 句提案核心）
2. **动机**：什么问题、为什么需要解决
3. **设计**：详细方案（含 API 签名 / 数据流 / 架构图）
4. **兼容性**：对现有系统的向后兼容分析
5. **备选方案**：考虑过但不选的方案及理由
6. **开放问题**：尚未决定的点、需要讨论的问题
7. **实施路径**：分阶段实施的计划

## 信息不足时

- 方案仍早期时，明确标 `Draft`。
- 性能、兼容性、实现成本未知时放入 `Open questions`。
- 没有治理流程时，不写“已接受”“已批准”。

## 禁止编造项

- 不编造 RFC 编号、状态、标准委员会立场、性能结果、兼容结论或实施时间线。
- 不把 open question 写成最终决策。

## 高质量参考来源

| 来源 | 可借鉴点 |
|------|----------|
| React RFCs | https://github.com/reactjs/rfcs |
| Rust RFCs | https://github.com/rust-lang/rfcs |
| Kubernetes Enhancement Proposals | https://github.com/kubernetes/enhancements/blob/master/keps/README.md |
| Python PEP 1 | https://peps.python.org/pep-0001/ |
| Swift Evolution | https://github.com/swiftlang/swift-evolution |
| TC39 proposals | https://github.com/tc39/proposals |

## 必含元素 Checklist
- [ ] 动机说明
- [ ] 设计方案
- [ ] 兼容性分析
- [ ] 备选方案
- [ ] 推测性设计已标明为 proposal / draft / open question
