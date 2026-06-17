# CONTRIBUTING — 写作标准

## 适用场景
规范外部贡献者如何参与项目，从 bug 报告到代码提交。

## 输出边界

CONTRIBUTING 面向真实贡献者，必须来自仓库事实。未知的本地命令、包管理器、CI 名称、coverage 目标、发布流程和权限要求要标为 `TODO`，不要用常见开源流程补齐。

## 标准结构

CONTRIBUTING 应按仓库证据裁剪，不要默认写成大型开源项目流程。

1. **Welcome**：欢迎贡献、项目定位、沟通语气。
2. **Ways to contribute**：报告问题、改文档、提建议、提交代码；按项目实际入口保留。
3. **Reporting issues**：如果仓库已有 issue template、security policy 或 discussion 入口，链接对应入口；未知时用通用说明。
4. **Proposing changes**：说明先开 issue/discussion 还是直接 PR；没有证据时保持轻量。
5. **Pull request process**：只写已知要求，例如 fork/branch/PR、review、截图、文档更新。
6. **Local development**：仅当仓库文件证明安装、构建、测试命令存在时写具体步骤。
7. **Code style / tests / CI**：仅当仓库已有配置、脚本或 CI 文件时写具体命令和工作流名。
8. **Code of Conduct / Security / License**：仅当对应文件或用户要求存在时链接；否则标 `TODO` 或省略。

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
- [ ] 贡献入口和 PR 流程说明按仓库实际情况裁剪
- [ ] 本地开发、代码规范、测试和 CI 命令只在有仓库证据时出现
- [ ] Node/npm/包管理器版本、coverage 目标、发布流程和 CI 要求来自仓库证据；未知时标为 `TODO` 或省略
- [ ] 不把未确认工具链（Storybook、Playwright、semantic-release 等）写成项目事实
