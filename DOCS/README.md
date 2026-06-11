# 文档目录

`DOCS/` 放设计过程、采集计划和 outline，不放最终使用标准。最终标准在 [`SKILL.md`](../SKILL.md) 和 [`reference/`](../reference)。

## 渐进式披露

这个仓库按 5 层组织信息：

1. **入口层**：[`README.md`](../README.md)  
   只回答“这是什么、怎么安装、从哪里开始”。

2. **索引层**：[`INDEX.md`](../INDEX.md)  
   汇总 18 场景、目录、reference、测试和维护入口。

3. **执行层**：[`SKILL.md`](../SKILL.md)  
   给 agent 使用，包含场景识别、通用原则和摘要标准。

4. **标准层**：[`reference/`](../reference)  
   每个场景的完整版/普通版、参考仓库写法、checklist 和参考链接。

5. **验证层**：[`test/`](../test)  
   测试提示词、双版样例和全量检查报告。

## 当前文档

| 文件 | 状态 | 用途 |
|------|------|------|
| [`collection-plan.md`](./collection-plan.md) | 设计材料 | 说明参考仓库采集和分类计划 |
| [`skill-outline.md`](./skill-outline.md) | 历史草案 | v1 outline，保留演进记录 |
| [`skill-outline-v2.md`](./skill-outline-v2.md) | 设计草案 | v2 outline，包含更完整的原则和结构 |

## 写作规则

- `README.md` 不放完整标准，只放入口和少量示例
- `INDEX.md` 放全量导航，但不展开正文细节
- `DOCS/` 放设计过程，不和 `reference/` 争夺“最终标准”角色
- `reference/` 中每个场景必须能独立使用
- `test/` 中每个测试必须能追溯到一个 reference 文件

## 添加新文档

新增文档时按这个顺序处理：

1. 在 `DOCS/` 中创建文件
2. 在本文件的“当前文档”表格中登记
3. 如果它是用户入口或维护入口，再同步到 [`INDEX.md`](../INDEX.md)
4. 如果它改变了 skill 行为，再同步到 [`SKILL.md`](../SKILL.md) 或对应 `reference/*.md`
