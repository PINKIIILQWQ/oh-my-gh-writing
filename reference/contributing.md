# CONTRIBUTING — 完整写法

## 适用场景
规范外部贡献者如何参与项目，从 bug 报告到代码提交。

## 完整写法（home-assistant, nodejs, angular）

### 结构
1. **欢迎语**（项目理念 + 行为准则链接）
2. **工作流概述**（Fork + Branch + PR 流程 5 步）
3. **分支策略**（main / dev / release 的关系）
4. **Commit 规范**（Conventional Commits 要求 + 示例）
5. **代码风格**（linter 配置 + 代码审查标准）
6. **PR 流程**（checklist：测试→文档→screenshot→CI）
7. **本地开发环境**（依赖安装 → 构建 → 测试 → 调试）
8. **Issue 分类**（bug / feature / 讨论各自处理方式）

### 参考仓库写法

**home-assistant/core**
- 公认最详尽：从环境搭建到代码审查全流程
- 含开发容器 devcontainer 配置
- 包含 Add-on 开发指南

**nodejs/node**
- 协作流程详细：从 Issue 到 PR 到 CI 到合并
- 代码风格 + Commit 规范 + 测试要求
- 含 Collaborator 指南

**angular/angular**
- Commit 规范优先（Conventional Commits）
- PR 类型（fix/feat/docs/refactor）表达清楚
- 含 Dev Guide + 调试指南

## CONTRIBUTING — 简洁写法（electron, django, github/docs）

### 结构
PR 流程→代码风格→开发环境

### 参考仓库写法

**electron/electron**
- 核心流程：Bug Report → PR → Review → Merge
- 代码风格 + 测试要求
- 含调试指南

**django/django**
- Ticket 工作流（Triage → Accept → Patch）
- 代码规范 + 测试指南
- Django 社区成熟的贡献文化

**github/docs**
- GitHub 官方文档的贡献指南
- 简洁聚焦：安装→本地预览→提交
- 含 SEO/内容规范

## 必含元素 Checklist
- [ ] PR 工作流说明
- [ ] 代码规范
- [ ] 本地开发环境搭建

## 参考链接

| 仓库 | 链接 |
|------|------|
| home-assistant CONTRIBUTING | https://github.com/home-assistant/core/blob/main/CONTRIBUTING.md |
| nodejs CONTRIBUTING | https://github.com/nodejs/node/blob/main/CONTRIBUTING.md |
| angular CONTRIBUTING | https://github.com/angular/angular/blob/main/CONTRIBUTING.md |
| electron CONTRIBUTING | https://github.com/electron/electron/blob/main/CONTRIBUTING.md |
| django CONTRIBUTING | https://github.com/django/django/blob/main/CONTRIBUTING.rst |
| github/docs CONTRIBUTING | https://github.com/github/docs/blob/main/CONTRIBUTING.md |
