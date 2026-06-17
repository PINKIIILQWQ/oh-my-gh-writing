<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/oh-my-gh-writing-logo.png">
  <img alt="oh-my-gh-writing" src="assets/oh-my-gh-writing-logo.png" width="160">
</picture>

# oh-my-gh-writing

[![License](https://img.shields.io/github/license/PINKIIILQWQ/oh-my-gh-writing?label=License&color=blue)](LICENSE)
[![Scenarios](https://img.shields.io/badge/Scenarios-18-6a0dad)](#-시나리오-인덱스)
[![Agent](https://img.shields.io/badge/Agent-Claude%20Code-8A2BE2)](https://claude.ai/code)
[![PRs](https://img.shields.io/badge/PRs-Welcome-brightgreen)](CONTRIBUTING.md)
[![GitHub last commit](https://img.shields.io/github/last-commit/PINKIIILQWQ/oh-my-gh-writing?label=Updated)](https://github.com/PINKIIILQWQ/oh-my-gh-writing/commits/main)

**oh-my-gh-writing**는 AI Agent를 위한 GitHub 라이팅 규범 시스템입니다. README 생성기나 독립 실행형 앱이 아니라, 포터블 스킬 패키지입니다. Agent가 로드하면 Issue, PR, Review, Commit, README, CHANGELOG, RFC 등 18가지 GitHub 문서를 시나리오에 따라 자동으로 라우팅하여 일관된 품질과 증거 기반 출력을 제공합니다.

---

## 시나리오 인덱스

| # | 카테고리 | 시나리오 | 표준 파일 |
|---|----------|----------|-----------|
| 1–4 | Issue | Bug Report / Feature Request / Enhancement / Discussion | `reference/bug-report.md` 등 |
| 5–8 | PR | Feature PR / Bug Fix PR / Refactor PR / Documentation PR | `reference/feature-pr.md` 등 |
| 9–10 | Review & Commit | Code Review / Standard Commit | `reference/code-review.md` 등 |
| 11–13 | Docs | README / CONTRIBUTING / CHANGELOG | `reference/readme.md` 등 |
| 14–15 | Release | Release Notes / Migration Guide | `reference/release-notes.md` 등 |
| 16 | Design | RFC | `reference/rfc.md` |
| 17–18 | Templates | Issue Form YAML / PR Template | `reference/issue-form-yaml.md` 등 |

전체 라우팅 규칙은 [`SKILL.md`](SKILL.md)를 참조하세요.

---

## 설치

### Claude Code (직접 로드)

```bash
gh repo clone PINKIIILQWQ/oh-my-gh-writing ~/.claude/skills/oh-my-gh-writing
```

그런 다음 Claude Code에서 `/oh-my-gh-writing`을 사용하세요.

### 다른 AI Agent

| Agent | 지원 수준 | 방법 |
|-------|-----------|------|
| Cline / Roo Code | 어댑티드 임포트 | `SKILL.md` 내용을 프로젝트 커스텀 명령어에 복사하고, 필요 시 해당 `reference/*.md` 로드 |

> 이 스킬은 Claude Code용으로 네이티브 설계되었습니다. 다른 Agent는 자체 규칙 시스템에 맞게 조정해야 합니다.

---

## 퀵 스타트

```text
/oh-my-gh-writing Bug Report 작성해줘
/oh-my-gh-writing 이 변경사항에 대한 PR 설명 작성해줘
/oh-my-gh-writing 이 PR 변경사항 리뷰해줘
/oh-my-gh-writing CHANGELOG 항목 작성해줘
```

Agent가 시나리오를 인식하고 해당 `reference/*.md`를 로드하여 GitHub에 바로 제출 가능한 아티팩트를 출력합니다.

---

## 핵심 원칙

- **증거 경계** — 버전 번호, PR 번호, 테스트 결과, 설치 명령어는 출처가 필요합니다. 알 수 없는 사실은 `TODO`로 표시
- **정확한 라우팅** — 사용자 의도에 따라 올바른 시나리오로 라우팅. Feature Request가 이미 구현된 PR로 작성되지 않음
- **출물 청결** — 아티팩트를 GitHub에 직접 붙여넣기 가능 — 대화형 서문, 외부 코드 블록, 테스트 메타데이터 없음
- **원아티팩트 원잡** — 여러 Issue나 Release Note를 하나의 출력에 혼합하지 않음
- **사용 가능 우선** — 정보가 부족하면 `TODO` 플레이스홀더로 초안을 작성하고 차단하지 않음

---

## 프로젝트 구조

```
oh-my-gh-writing/
├── SKILL.md                    # Agent 런타임 라우터 및 공유 규칙
├── INDEX.md                    # 저장소 내비게이션
├── reference/
│   ├── bug-report.md           # Bug Report 표준
│   ├── feature-request.md      # Feature Request 표준
│   ├── enhancement.md          # Enhancement 표준
│   ├── discussion.md           # Discussion 표준
│   ├── feature-pr.md           # Feature PR 표준
│   ├── bug-fix-pr.md           # Bug Fix PR 표준
│   ├── refactor-pr.md          # Refactor PR 표준
│   ├── documentation-pr.md     # Documentation PR 표준
│   ├── code-review.md          # Code Review 표준
│   ├── standard-commit.md      # 커밋 메시지 표준
│   ├── readme.md               # README 작성 표준
│   ├── contributing.md         # CONTRIBUTING 작성 표준
│   ├── changelog.md            # CHANGELOG 표준
│   ├── release-notes.md        # Release Notes 표준
│   ├── migration-guide.md      # Migration Guide 표준
│   ├── rfc.md                  # RFC 표준
│   ├── issue-form-yaml.md      # Issue Form YAML 표준
│   ├── pr-template.md          # PR Template 표준
│   ├── weapons.md              # GitHub Markdown 도구 모음
│   ├── emoji-guide.md          # 이모지 가이드
│   ├── output-validation.md    # 출력 검증 체크리스트
│   └── source-catalog.md       # 참조 소스 카탈로그
├── CONTRIBUTING.md             # 기여 가이드
├── assets/                     # 프로젝트 에셋
└── LICENSE                     # MIT
---

## 기여

시나리오 규칙, 참조 소스, 출력 검증 개선에 관한 PR을 환영합니다. 자세한 내용은 [`CONTRIBUTING.md`](CONTRIBUTING.md)를 참조하세요.

---

## 라이선스

[MIT](LICENSE)
