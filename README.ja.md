<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/oh-my-gh-writing-logo.png">
  <img alt="oh-my-gh-writing" src="assets/oh-my-gh-writing-logo.png" width="160">
</picture>

# oh-my-gh-writing

[![License](https://img.shields.io/github/license/PINKIIILQWQ/oh-my-gh-writing?label=License&color=blue)](LICENSE)
[![Scenarios](https://img.shields.io/badge/Scenarios-18-6a0dad)](#-シナリオ一覧)
[![Agent](https://img.shields.io/badge/Agent-Claude%20Code-8A2BE2)](https://claude.ai/code)
[![PRs](https://img.shields.io/badge/PRs-Welcome-brightgreen)](CONTRIBUTING.md)
[![GitHub last commit](https://img.shields.io/github/last-commit/PINKIIILQWQ/oh-my-gh-writing?label=Updated)](https://github.com/PINKIIILQWQ/oh-my-gh-writing/commits/main)

**oh-my-gh-writing** は、AI Agent のための GitHub ライティング規範システムです。これは README ジェネレーターやスタンドアロンアプリではなく、移植可能なスキルパッケージです。Agent が読み込むと、Issue、PR、Review、Commit、README、CHANGELOG、RFC など 18 種類の GitHub 文書をシナリオに応じて自動的にルーティングし、一貫した品質と証拠に基づいた出力を実現します。

---

## シナリオ一覧

| # | カテゴリ | シナリオ | 標準ファイル |
|---|----------|----------|--------------|
| 1–4 | Issue | Bug Report / Feature Request / Enhancement / Discussion | `reference/bug-report.md` 等 |
| 5–8 | PR | Feature PR / Bug Fix PR / Refactor PR / Documentation PR | `reference/feature-pr.md` 等 |
| 9–10 | Review & Commit | Code Review / Standard Commit | `reference/code-review.md` 等 |
| 11–13 | Docs | README / CONTRIBUTING / CHANGELOG | `reference/readme.md` 等 |
| 14–15 | Release | Release Notes / Migration Guide | `reference/release-notes.md` 等 |
| 16 | Design | RFC | `reference/rfc.md` |
| 17–18 | Templates | Issue Form YAML / PR Template | `reference/issue-form-yaml.md` 等 |

ルーティングルールの詳細は [`SKILL.md`](SKILL.md) を参照してください。

---

## インストール

### Claude Code（直接読み込み）

```bash
gh repo clone PINKIIILQWQ/oh-my-gh-writing ~/.claude/skills/oh-my-gh-writing
```

その後、Claude Code 内で `/oh-my-gh-writing` を実行します。

### 他の AI Agent

| Agent | サポートレベル | 操作 |
|-------|---------------|------|
| Cline / Roo Code | アダプテッドインポート | `SKILL.md` の内容をプロジェクトのカスタム指示にコピーし、必要に応じて対応する `reference/*.md` を読み込む |

> このスキルは Claude Code 向けにネイティブ設計されています。他の Agent は各自のルールシステムに適応させる必要があります。

---

## クイックスタート

```text
/oh-my-gh-writing Bug Report を書いて
/oh-my-gh-writing 変更内容の PR 説明を書いて
/oh-my-gh-writing この PR の変更をレビューして
/oh-my-gh-writing CHANGELOG エントリを書いて
```

Agent がシナリオを認識し、対応する `reference/*.md` を読み込み、GitHub にそのまま提出できる成果物を出力します。

---

## コア原則

- **証拠の境界** — バージョン番号、PR 番号、テスト結果、インストールコマンドは出典が必要。不明な場合は `TODO` とマーク
- **正確なルーティング** — ユーザーの意図に応じて正しいシナリオにルーティング。Feature Request が実装済み PR として書かれることはありません
- **出力のクリーンさ** — 成果物は GitHub にそのまま貼り付け可能 — 会話的な前置き、外側のコードブロック、テストメタデータは一切なし
- **1成果物1ジョブ** — 複数の Issue や Release Note を1つの出力に混ぜません
- **使えることを優先** — 情報が不足している場合は、`TODO` プレースホルダーを付けてドラフトを作成し、ブロックしません

---

## プロジェクト構造

```
oh-my-gh-writing/
├── SKILL.md                    # Agent ランタイムルーターと共有ルール
├── INDEX.md                    # リポジトリナビゲーション
├── reference/
│   ├── bug-report.md           # Bug Report 標準
│   ├── feature-request.md      # Feature Request 標準
│   ├── enhancement.md          # Enhancement 標準
│   ├── discussion.md           # Discussion 標準
│   ├── feature-pr.md           # Feature PR 標準
│   ├── bug-fix-pr.md           # Bug Fix PR 標準
│   ├── refactor-pr.md          # Refactor PR 標準
│   ├── documentation-pr.md     # Documentation PR 標準
│   ├── code-review.md          # Code Review 標準
│   ├── standard-commit.md      # コミットメッセージ標準
│   ├── readme.md               # README ライティング標準
│   ├── contributing.md         # CONTRIBUTING ライティング標準
│   ├── changelog.md            # CHANGELOG 標準
│   ├── release-notes.md        # Release Notes 標準
│   ├── migration-guide.md      # Migration Guide 標準
│   ├── rfc.md                  # RFC 標準
│   ├── issue-form-yaml.md      # Issue Form YAML 標準
│   ├── pr-template.md          # PR Template 標準
│   ├── weapons.md              # GitHub Markdown ツール集
│   ├── emoji-guide.md          # Emoji ガイド
│   ├── output-validation.md    # 出力検収チェックリスト
│   └── source-catalog.md       # 参考ソースカタログ
├── CONTRIBUTING.md             # コントリビューションガイド
├── assets/                     # プロジェクトアセット
└── LICENSE                     # MIT
```

---

## コントリビューション

シナリオルール、参考ソース、出力検収の改善に関する PR を歓迎します。詳細は [`CONTRIBUTING.md`](CONTRIBUTING.md) を参照してください。

---

## ライセンス

[MIT](LICENSE)
