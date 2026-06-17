<p align="center">
  <img src="assets/oh-my-gh-writing-logo.png" alt="oh-my-gh-writing ロゴ" width="200">
</p>

<h1 align="center">oh-my-gh-writing</h1>

<p align="center">
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-MIT-0f766e?style=flat" alt="MIT License"></a>
  <a href="SKILL.md"><img src="https://img.shields.io/badge/Status-Release%20Candidate-2563eb?style=flat" alt="Release Candidate"></a>
  <a href="INDEX.md"><img src="https://img.shields.io/badge/Scenarios-18-6a0dad?style=flat" alt="18 scenarios"></a>
  <a href="SKILL.md"><img src="https://img.shields.io/badge/Format-SKILL.md-22AA66?style=flat" alt="SKILL.md"></a>
</p>

<p align="center">
  <a href="README.md">简体中文</a> · <a href="README.en.md">English</a> · <a href="README.es.md">Español</a> · <a href="README.hi.md">हिन्दी</a> · <a href="README.ar.md">العربية</a> · <a href="README.fr.md">Français</a> · <a href="README.pt.md">Português</a> · 日本語 · <a href="README.ko.md">한국어</a>
</p>

**oh-my-gh-writing** は、AI Agent 向けの GitHub ライティング skill pack です。Issues、PRs、Reviews、Commits、README、CHANGELOG、Release Notes、Migration Guides、RFCs、Issue Forms、PR Templates などの一般的な GitHub 文書作成タスクを、シナリオごとの標準にルーティングし、構造が明確で evidence boundary を持つ Markdown / YAML ドラフトを生成しやすくします。

これは README generator でも GitHub integration service でもありません。移植可能な Markdown rulebase です。Agent Skills をネイティブに扱えるツールではそのまま読み込めます。そうでないツールでは、`SKILL.md` と必要な `reference/*.md` を rules、custom instructions、knowledge base として適用できます。

## なぜ oh-my-gh-writing？

GitHub でよい文章を書くことは、Markdown を埋めるだけではありません。難しいのは、今どのシナリオなのか、どの事実を検証すべきか、何を推測してはいけないか、そして最終 artifact を Issue、PR、Review、README にそのまま貼れるかを判断することです。

- **18 の GitHub writing scenarios**: Issues、PRs、Code Review、Commit、README、CHANGELOG、Release Notes、Migration Guide、RFC、Issue Form、PR Template など。
- **書く前にルーティング**: Feature Request、Enhancement、Discussion、Feature PR、Bug Fix PR、Refactor PR を分離します。
- **Progressive reference loading**: `SKILL.md` は軽量に保ち、詳細な標準は必要なときだけ読み込みます。
- **Evidence boundaries**: version、command、CI、compatibility、release、issue/PR number を推測しません。
- **よりクリーンな artifact**: 会話的な前置き、外側の Markdown fence、テスト用タイトル、コピー残りを避けます。
- **実際の OSS 参照**: GitHub Docs、Conventional Commits、Keep a Changelog、React、Kubernetes、TypeScript、Node.js、Tailwind CSS などから学習したルールです。

## 利用方法

**skill として使う**: agent が `SKILL.md` を含むフォルダを読み込み、必要に応じて `reference/` を読める場所に置きます。

**rules として使う**: ツールがこの skill 形式を直接扱えない場合は、`SKILL.md` のルーティング表と該当する `reference/*.md` を project rules、custom instructions、knowledge base に変換してください。

| Icon | Agent / Tool | 推奨セットアップ | Notes / Docs |
|------|--------------|------------------|--------------|
| <img src="https://openai.com/favicon.ico" width="14" height="14" alt="OpenAI"> | Codex | `$HOME/.agents/skills/oh-my-gh-writing` または `.agents/skills/oh-my-gh-writing` に clone | [Codex Agent Skills](https://developers.openai.com/codex/skills) |
| <img src="https://claude.ai/favicon.ico" width="14" height="14" alt="Claude"> | Claude Code | `~/.claude/skills/oh-my-gh-writing` または `.claude/skills/oh-my-gh-writing` に clone / symlink | [Claude Code Skills](https://code.claude.com/docs/en/skills) |
| <img src="https://geminicli.com/favicon.ico" width="14" height="14" alt="Gemini CLI"> | Gemini CLI / Antigravity CLI | docs には `~/.gemini/skills/`、`~/.agents/skills/`、`gemini skills install` が記載されています | 最新の [official docs](https://geminicli.com/docs/cli/skills/) を確認してください |
| <img src="https://hermes-agent.nousresearch.com/favicon.ico" width="14" height="14" alt="Hermes"> | Hermes | `~/.hermes/skills/<category>/oh-my-gh-writing` に配置 | HTTP の single-file install は `SKILL.md` のみに適します。`reference/` を保持してください。[Hermes Skills](https://hermes-agent.nousresearch.com/docs/guides/work-with-skills) |
| <img src="https://cursor.com/favicon.ico" width="14" height="14" alt="Cursor"> | Cursor | router と必要な scenario rules を project rules や knowledge base に変換 | [Cursor Docs](https://cursor.com/docs) を確認 |
| <img src="https://github.com/favicon.ico" width="14" height="14" alt="GitHub"> | GitHub Copilot | `.github/copilot-instructions.md`、`.github/instructions/*.instructions.md`、または Copilot agent skill structure に変換 | [Copilot Custom Instructions](https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/add-custom-instructions/add-repository-instructions) |
| <img src="https://docs.continue.dev/favicon.ico" width="14" height="14" alt="Continue"> | Continue | `.continue/rules/*.md` に変換。scenario ごとに分ける方が安定します | [Continue Rules](https://docs.continue.dev/customize/rules) |
| <img src="https://docs.windsurf.com/favicon.ico" width="14" height="14" alt="Windsurf"> | Windsurf / Devin Desktop | 現在の docs は customization 用の memories と rules に言及しています | [Windsurf / Devin Docs](https://docs.windsurf.com) で最新手順を確認してください |

## Quick Start

```bash
# Codex
git clone https://github.com/PINKIIILQWQ/oh-my-gh-writing.git "$HOME/.agents/skills/oh-my-gh-writing"

# Claude Code
git clone https://github.com/PINKIIILQWQ/oh-my-gh-writing.git "$HOME/.claude/skills/oh-my-gh-writing"
```

ローカル開発用 symlink:

```bash
# Codex / Gemini CLI
ln -sfn "$PWD" "$HOME/.agents/skills/oh-my-gh-writing"

# Claude Code
ln -sfn "$PWD" "$HOME/.claude/skills/oh-my-gh-writing"
```

例:

```text
このリポジトリの README を書いて。
この bug report を GitHub Issue に整えて。
現在の diff から PR description を書いて。
この PR を review して blocking / major / minor / nit に分類して。
```

## Scenarios

| # | Category | Scenario | Use when |
|---|----------|----------|----------|
| 1 | Issue | Bug Report | 再現可能な defect を報告する |
| 2 | Issue | Feature Request | 新機能や API を提案する |
| 3 | Issue | Enhancement | 既存動作を改善する |
| 4 | Issue | Discussion | オープンな community discussion を始める |
| 5 | PR | Feature PR | 新機能 PR を説明する |
| 6 | PR | Bug Fix PR | bug fix PR を説明する |
| 7 | PR | Refactor PR | 動作変更のない refactor を説明する |
| 8 | PR | Documentation PR | documentation-only changes を説明する |
| 9 | Review | Code Review | code changes を review する |
| 10 | Commit | Standard Commit | commit message を書く |
| 11 | Docs | README | project homepage を作成・改訂する |
| 12 | Docs | CONTRIBUTING | contribution guidelines を作成する |
| 13 | Docs | CHANGELOG | version history を書く |
| 14 | Release | Release Notes | release announcement を書く |
| 15 | Release | Migration Guide | upgrade steps を説明する |
| 16 | Design | RFC | design proposal を作成する |
| 17 | Templates | Issue Form YAML | GitHub Issue Forms を作成する |
| 18 | Templates | PR Template | Pull Request templates を作成する |

各シナリオの標準ファイルは `reference/` にあります。全体のナビゲーションは [`INDEX.md`](INDEX.md) を参照してください。

## Repository Structure

```text
oh-my-gh-writing/
├── README.md
├── README.*.md
├── SKILL.md
├── INDEX.md
├── CONTRIBUTING.md
├── LICENSE
├── assets/
│   └── oh-my-gh-writing-logo.png
└── reference/
    ├── *.md
    ├── readme.md
    ├── shared-principles.md
    ├── output-validation.md
    ├── source-catalog.md
    ├── weapons.md
    ├── emoji-guide.md
    └── badge-catalog.md
```

## Contributing

scenario rules、reference sources、output validation、小さな Markdown helpers への貢献を歓迎します。examples や test cases を追加する場合は、まず Issue または Discussion で source、scenario、test goal、license/privacy boundary を説明してください。

`SKILL.md` は軽量に保ち、scenario details は対応する `reference/*.md` に置いてください。[`CONTRIBUTING.md`](CONTRIBUTING.md) を参照してください。

## Sources

ルールは [GitHub Docs](https://docs.github.com/en)、[Conventional Commits](https://www.conventionalcommits.org/)、[Keep a Changelog](https://keepachangelog.com/)、[Google Engineering Practices](https://google.github.io/eng-practices/review/)、および Angular、Kubernetes、React、TypeScript、VS Code、Node.js、Tailwind CSS などの成熟した OSS プロジェクトを参考にしています。[`reference/source-catalog.md`](reference/source-catalog.md) を参照してください。

## License

[MIT](LICENSE) © 2026 oh-my-gh-writing contributors
