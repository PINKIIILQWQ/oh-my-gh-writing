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

**oh-my-gh-writing**는 AI Agent를 위한 GitHub 라이팅 스킬 팩입니다. 일반적인 GitHub 라이팅 요구사항(Issue, PR, README, CHANGELOG 등)을 적절한 품질 표준으로 라우팅하여, 모든 출력물이 커뮤니티 관례를 따르고 추가 수정 없이 제출 가능하고 가독성이 높도록 보장합니다.

전체 규칙 세트는 Markdown 파일로 이 리포지토리에 저장되어 있으며, 외부 서비스에 의존하지 않습니다. 로컬 스킬 로딩을 지원하는 모든 AI Agent가 직접 사용할 수 있습니다.

## 시나리오

| # | 카테고리 | 시나리오 | 사용时机 |
|---|----------|----------|----------|
| 1 | Issue | Bug Report | 재현 가능한 버그 보고 |
| 2 | Issue | Feature Request | 새 기능 또는 API 제안 |
| 3 | Issue | Enhancement | 기존 기능 개선 |
| 4 | Issue | Discussion | 커뮤니티 자유 토론 |
| 5 | PR | Feature PR | 새 기능 Pull Request |
| 6 | PR | Bug Fix PR | 버그 수정 Pull Request |
| 7 | PR | Refactor PR | 동작을 변경하지 않는 리팩터링 |
| 8 | PR | Documentation PR | 문서 전용 변경 |
| 9 | Review | Code Review | 코드 변경 검토 |
| 10 | Commit | Standard Commit | 커밋 메시지 작성 |
| 11 | Docs | README | 프로젝트 홈페이지 문서 |
| 12 | Docs | CONTRIBUTING | 기여 가이드 |
| 13 | Docs | CHANGELOG | 버전 변경 이력 |
| 14 | Release | Release Notes | 릴리스 공지 |
| 15 | Release | Migration Guide | 업그레이드 가이드 |
| 16 | Design | RFC | 설계 제안 |
| 17 | Templates | Issue Form YAML | GitHub Issue 폼 |
| 18 | Templates | PR Template | Pull Request 템플릿 |

각 시나리오에는 `reference/` 디렉토리에 해당 라이팅 표준 파일이 있으며, 표준 구조, 필수 필드, 사실 경계 규칙, 고품질 참고 자료, 필수 요소 체크리스트가 포함되어 있습니다.

## 빠른 시작

이 리포지토리를 AI Agent에 스킬로 로드합니다:

```bash
# Claude Code — .claude/settings.json 또는 Claude 설정에서 이 스킬 연결
# 또는 SKILL.md를 Agent 시스템 지시의 일부로 직접 참조
```

모든 시나리오 규칙과 라우팅은 [`SKILL.md`](SKILL.md), 전체 색인은 [`INDEX.md`](INDEX.md)를 참조하세요.

## 프로젝트 구조

```
oh-my-gh-writing/
├── SKILL.md                  # Agent 진입점 및 시나리오 라우팅
├── INDEX.md                  # 탐색 색인
├── CONTRIBUTING.md           # 기여 규칙
├── LICENSE                   # MIT 라이선스
├── .gitignore
├── assets/                   # 프로젝트 에셋
│   └── oh-my-gh-writing-logo.png
└── reference/                # 시나리오 표준 파일
    ├── shared-principles.md  # 19가지 공유 품질 규칙
    ├── readme.md             # README 라이팅 규칙
    ├── output-validation.md  # 출력 검증 체크리스트
    └── source-catalog.md     # 참고 자료 카탈로그
```

## 기여

기여를 환영합니다. 시나리오 규칙 수정, 참고 자료 품질 개선, Markdown 도구 참조 추가, 사용 사례 제출 등 어떤 기여든 도움이 됩니다.

- 먼저 Issue나 Discussion에서 아이디어를 논의해 주세요
- 리포지토리를 Fork하고 PR을 제출해 주세요
- 시나리오 규칙은 해당 `reference/*.md`에 작성하고 라우팅 계층에 넣지 마세요
- `SKITH.md`는 가볍게 유지하고 라우팅에 집중하세요

자세한 규칙은 [`CONTRIBUTING.md`](CONTRIBUTING.md)를 참조하세요.

## 감사의 말

- [GitHub Docs](https://docs.github.com/en) — Issue/PR 템플릿, Markdown 문법, 커뮤니티 관행
- [Conventional Commits](https://www.conventionalcommits.org/) — 커밋 메시지 형식 규격
- [Keep a Changelog](https://keepachangelog.com/) — CHANGELOG 형식 표준
- [shields.io](https://shields.io) — 배지 생성 서비스
- [Google Engineering Practices](https://google.github.io/eng-practices/review/) — 코드 리뷰 가이드
- Angular, Kubernetes, React, TypeScript, VS Code, Node.js, Tailwind CSS 등 오픈소스 프로젝트의 템플릿 및 기여 가이드 — 시나리오 표준 구조 참고
- [ikatyang/emoji-cheat-sheet](https://github.com/ikatyang/emoji-cheat-sheet) — 이모지 참조
- [carloscuesta/gitmoji](https://github.com/carloscuesta/gitmoji) — 커밋 의도 이모지 가이드

## 라이선스

[MIT](LICENSE) © 2026 oh-my-gh-writing contributors
