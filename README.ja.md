<p align="center">
  <img src="assets/oh-my-gh-writing-logo.png" alt="oh-my-gh-writing logo" width="200">
</p>

<h1 align="center">oh-my-gh-writing</h1>

<p align="center">
  🌐 <a href="README.md">中文</a> · <a href="README.en.md">English</a> · <a href="README.ja.md">日本語</a> · <a href="README.ko.md">한국어</a> · <a href="README.es.md">Español</a> · <a href="README.fr.md">Français</a> · <a href="README.de.md">Deutsch</a> · <a href="README.pt.md">Português</a>
</p>

<p align="center">
  <a href="https://github.com/PINKIIILQWQ/oh-my-gh-writing/blob/main/LICENSE"><img src="https://img.shields.io/github/license/PINKIIILQWQ/oh-my-gh-writing?style=flat&label=License" alt="MIT"></a>
  <a href="https://github.com/PINKIIILQWQ/oh-my-gh-writing/commits/main"><img src="https://img.shields.io/github/last-commit/PINKIIILQWQ/oh-my-gh-writing?style=flat&label=Updated" alt="Last Commit"></a>
  <a href="INDEX.md"><img src="https://img.shields.io/badge/Scenarios-18-6a0dad?style=flat" alt="18 Scenarios"></a>
  <a href="SKILL.md"><img src="https://img.shields.io/badge/Format-Agent%20Skill-22AA66?style=flat" alt="Agent Skill"></a>
</p>

<p>
  <strong>oh-my-gh-writing</strong> は、AI Agent のための GitHub ライティングスキルパックです。Issue、PR、README、CHANGELOG などの一般的な GitHub ライティング要件を適切な品質基準にルーティングし、すべての出力がコミュニティの慣習に従い、手作業による修正なしで提出可能で読みやすい状態になることを保証します。
</p>
<p>
  ルールセット全体は Markdown ファイルとしてこのリポジトリに保存されており、外部サービスに依存しません。ローカルスキルの読み込みをサポートする AI Agent であれば、直接使用できます。
</p>

## シナリオ

| # | カテゴリ | シナリオ | 使用タイミング |
|---|----------|----------|----------------|
| 1 | Issue | Bug Report | 再現可能なバグの報告 |
| 2 | Issue | Feature Request | 新機能・新 API の提案 |
| 3 | Issue | Enhancement | 既存機能の改善 |
| 4 | Issue | Discussion | コミュニティでの自由討議 |
| 5 | PR | Feature PR | 新機能の Pull Request |
| 6 | PR | Bug Fix PR | バグ修正の Pull Request |
| 7 | PR | Refactor PR | 動作を変えないリファクタリング |
| 8 | PR | Documentation PR | ドキュメントのみの変更 |
| 9 | Review | Code Review | コード変更のレビュー |
| 10 | Commit | Standard Commit | コミットメッセージの作成 |
| 11 | Docs | README | プロジェクトホームページ |
| 12 | Docs | CONTRIBUTING | コントリビューションガイド |
| 13 | Docs | CHANGELOG | バージョン変更履歴 |
| 14 | Release | Release Notes | リリース告知 |
| 15 | Release | Migration Guide | アップグレードガイド |
| 16 | Design | RFC | 設計提案 |
| 17 | Templates | Issue Form YAML | GitHub Issue フォーム |
| 18 | Templates | PR Template | Pull Request テンプレート |

各シナリオには、`reference/` ディレクトリに対応するライティング標準ファイルがあり、標準構成、必須フィールド、ファクトバウンダリルール、高品質な参考ソース、必須要素のチェックリストが含まれています。

## クイックスタート

このリポジトリを AI Agent にスキルとして読み込ませます：

```bash
# Claude Code — .claude/settings.json または Claude 設定で本スキルを関連付け
# または SKILL.md を Agent のシステム指示の一部として直接参照
```

すべてのシナリオルールとルーティングについては [`SKILL.md`](SKILL.md)、完全な索引は [`INDEX.md`](INDEX.md) を参照してください。

## プロジェクト構造

```
oh-my-gh-writing/
├── SKILL.md                  # Agent エントリとシナリオルーティング
├── INDEX.md                  # ナビゲーション索引
├── CONTRIBUTING.md           # コントリビューションルール
├── LICENSE                   # MIT ライセンス
├── .gitignore
├── assets/                   # プロジェクト素材
│   └── oh-my-gh-writing-logo.png
└── reference/                # シナリオ標準ファイル
    ├── shared-principles.md  # 19 の共有品質ルール
    ├── readme.md             # README ライティングルール
    ├── output-validation.md  # 出力検証チェックリスト
    └── source-catalog.md     # 参考ソースカタログ
```

## コントリビューション

コントリビューションを歓迎します。シナリオルールの修正、参考ソースの品質向上、Markdown ツールの追加、使用事例の提出など、あらゆる貢献が役立ちます。

- まず Issue または Discussion でアイデアを議論してください
- リポジトリを Fork して PR を提出してください
- シナリオルールは対応する `reference/*.md` に記述し、ルーティング層に詰め込まないでください
- `SKILL.md` は軽量に保ち、ルーティングに専念させてください

詳細なルールは [`CONTRIBUTING.md`](CONTRIBUTING.md) を参照してください。

## 謝辞

- [GitHub Docs](https://docs.github.com/en) — Issue/PR テンプレート、Markdown 構文、コミュニティ慣習
- [Conventional Commits](https://www.conventionalcommits.org/) — コミットメッセージ形式仕様
- [Keep a Changelog](https://keepachangelog.com/) — CHANGELOG 形式標準
- [shields.io](https://shields.io) — バッジ生成サービス
- [Google Engineering Practices](https://google.github.io/eng-practices/review/) — コードレビューガイド
- Angular、Kubernetes、React、TypeScript、VS Code、Node.js、Tailwind CSS などのオープンソースプロジェクトのテンプレートとコントリビューションガイド — シナリオ標準の構造的参考
- [ikatyang/emoji-cheat-sheet](https://github.com/ikatyang/emoji-cheat-sheet) — 絵文字クイックリファレンス
- [carloscuesta/gitmoji](https://github.com/carloscuesta/gitmoji) — コミット意図絵文字ガイド

## ライセンス

[MIT](LICENSE) © 2026 oh-my-gh-writing contributors
