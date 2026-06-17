# CONTRIBUTING — 写作标准

## 适用场景
规范外部贡献者如何参与项目，从 bug 报告到代码提交。

## 输出边界

CONTRIBUTING 面向真实贡献者，必须来自仓库事实。未知的本地命令、包管理器、CI 名称、coverage 目标、发布流程和权限要求要标为 `TODO`，不要用常见开源流程补齐。

## 标准结构

1. **欢迎语**（项目理念 + 行为准则链接）
2. **工作流概述**（Fork + Branch + PR 流程 5 步）
3. **分支策略**（main / dev / release 的关系）
4. **Commit 规范**（Conventional Commits 要求 + 示例）
5. **代码风格**（linter 配置 + 代码审查标准）
6. **PR 流程**（checklist：测试→文档→screenshot→CI）
7. **本地开发环境**（依赖安装 → 构建 → 测试 → 调试）
8. **Issue 分类**（bug / feature / 讨论各自处理方式）

## 信息不足时

- 仓库没有 package/config 文件时，不写具体安装命令。
- 仓库没有 CI 配置时，不写 workflow 名称。
- 没有行为准则或安全政策时，写 `TODO: add Code of Conduct` 或删除对应段落。

## 禁止编造项

- 不编造 Node/npm/pnpm 版本、测试命令、devcontainer、Storybook、Playwright、semantic-release、coverage 门槛或发布权限。
- 不把参考项目的 CLA、DCO、bot、label、reviewer 规则写进目标项目，除非目标仓库已有证据。

## 高质量参考来源

| 来源 | 可借鉴点 |
|------|----------|
| GitHub contributing guide | https://docs.github.com/en/get-started/exploring-projects-on-github/contributing-to-a-project |
| Node.js CONTRIBUTING | https://github.com/nodejs/node/blob/main/CONTRIBUTING.md |
| Angular CONTRIBUTING | https://github.com/angular/angular/blob/main/CONTRIBUTING.md |
| Electron CONTRIBUTING | https://github.com/electron/electron/blob/main/CONTRIBUTING.md |
| Django CONTRIBUTING | https://github.com/django/django/blob/main/CONTRIBUTING.rst |
| Home Assistant CONTRIBUTING | https://github.com/home-assistant/core/blob/dev/CONTRIBUTING.md |

## 必含元素 Checklist
- [ ] PR 工作流说明
- [ ] 代码规范
- [ ] 本地开发环境搭建
- [ ] Node/npm/包管理器版本、coverage 目标、发布流程和 CI 要求来自仓库证据；未知时标为 `TODO`
- [ ] 不把未确认工具链（Storybook、Playwright、semantic-release 等）写成项目事实
