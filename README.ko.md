<p align="center">
  <img src="assets/oh-my-gh-writing-logo.png" alt="oh-my-gh-writing 로고" width="200">
</p>

<h1 align="center">oh-my-gh-writing</h1>

<p align="center">
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-MIT-0f766e?style=flat" alt="MIT License"></a>
  <a href="SKILL.md"><img src="https://img.shields.io/badge/Status-Release%20Candidate-2563eb?style=flat" alt="Release Candidate"></a>
  <a href="INDEX.md"><img src="https://img.shields.io/badge/Artifacts-18-6a0dad?style=flat" alt="18 artifact standards"></a>
  <a href="INDEX.md"><img src="https://img.shields.io/badge/Workflows-7-0f766e?style=flat" alt="7 workflow packs"></a>
  <a href="SKILL.md"><img src="https://img.shields.io/badge/Format-SKILL.md-22AA66?style=flat" alt="SKILL.md"></a>
</p>

<p align="center">
  <a href="README.md">简体中文</a> · <a href="README.en.md">English</a> · <a href="README.es.md">Español</a> · <a href="README.hi.md">हिन्दी</a> · <a href="README.ar.md">العربية</a> · <a href="README.fr.md">Français</a> · <a href="README.pt.md">Português</a> · <a href="README.ja.md">日本語</a> · 한국어
</p>

**oh-my-gh-writing**은 AI Agent를 위한 GitHub writing skill pack입니다. Issues, PRs, Reviews, Commits, README, CHANGELOG, Release Notes, Migration Guides, RFCs, Issue Forms, PR Templates 같은 일반적인 GitHub 작성 작업을 시나리오별 표준으로 라우팅하여, 구조가 명확하고 evidence boundary가 있는 Markdown 또는 YAML 초안을 만들도록 돕습니다.

이 프로젝트는 README generator도, GitHub integration service도 아닙니다. 이식 가능한 Markdown rulebase입니다. Agent Skills를 네이티브로 지원하는 도구는 그대로 로드할 수 있고, 그렇지 않은 도구는 `SKILL.md`와 필요한 `reference/*.md` 파일을 rules, custom instructions, knowledge base로 변환해 사용할 수 있습니다.

## 왜 oh-my-gh-writing인가?

GitHub에서 좋은 글을 쓰는 일은 Markdown을 채우는 것만이 아닙니다. 어려운 부분은 지금 어떤 시나리오인지, 어떤 사실을 검증해야 하는지, 무엇을 지어내면 안 되는지, 최종 artifact를 Issue, PR, Review, README에 정리 없이 붙여넣을 수 있는지 판단하는 것입니다.

- **18개의 GitHub writing scenarios**: Issues, PRs, Code Review, Commit, README, CHANGELOG, Release Notes, Migration Guide, RFC, Issue Form, PR Template 등.
- **쓰기 전에 라우팅**: Feature Request, Enhancement, Discussion, Feature PR, Bug Fix PR, Refactor PR을 구분합니다.
- **Progressive reference loading**: `SKILL.md`는 가볍게 유지하고, 상세 표준은 필요할 때만 읽습니다.
- **Evidence boundaries**: versions, commands, CI, compatibility, releases, issue/PR numbers를 추측하지 않습니다.
- **더 깨끗한 artifacts**: 대화식 서문, 바깥 Markdown fence, 테스트 제목, 복사 잔여물을 피합니다.
- **실제 오픈소스 참고**: GitHub Docs, Conventional Commits, Keep a Changelog, React, Kubernetes, TypeScript, Node.js, Tailwind CSS 등의 패턴을 참고합니다.

## 사용 방식

**Skill로 사용**: agent가 `SKILL.md`가 있는 폴더를 로드하고 필요할 때 `reference/`를 읽을 수 있는 위치에 이 저장소를 둡니다.

**Rules로 사용**: 도구가 이 skill 형식을 직접 소비하지 못한다면 `SKILL.md`의 라우팅 표와 관련 `reference/*.md`를 project rules, custom instructions, knowledge base로 변환하세요.

| Icon | Agent / Tool | 권장 설정 | Notes / Docs |
|------|--------------|-----------|--------------|
| <a href="https://developers.openai.com/codex/skills"><img src="https://www.google.com/s2/favicons?domain=openai.com&sz=64" width="24" height="24" alt="OpenAI"></a> | [Codex](https://developers.openai.com/codex/skills) | `$HOME/.agents/skills/oh-my-gh-writing` 또는 `.agents/skills/oh-my-gh-writing`에 clone | [Codex Agent Skills](https://developers.openai.com/codex/skills) |
| <a href="https://code.claude.com/docs/en/skills"><img src="https://www.google.com/s2/favicons?domain=claude.ai&sz=64" width="24" height="24" alt="Claude"></a> | [Claude Code](https://code.claude.com/docs/en/skills) | `~/.claude/skills/oh-my-gh-writing` 또는 `.claude/skills/oh-my-gh-writing`에 clone/symlink | [Claude Code Skills](https://code.claude.com/docs/en/skills) |
| <a href="https://geminicli.com/docs/cli/skills/"><img src="https://www.google.com/s2/favicons?domain=geminicli.com&sz=64" width="24" height="24" alt="Gemini CLI"></a> | [Gemini CLI](https://geminicli.com/docs/cli/skills/) | docs에는 `~/.gemini/skills/`, `~/.agents/skills/`, `gemini skills install`이 나와 있습니다 | 현재 [official docs](https://geminicli.com/docs/cli/skills/)를 확인하세요 |
| <a href="https://antigravity.google/"><img src="https://www.google.com/s2/favicons?domain=antigravity.google&sz=64" width="24" height="24" alt="Antigravity"></a> | [Antigravity CLI](https://antigravity.google/) | skill / rules 연동 방식은 최신 문서에서 확인하세요 | [Google Antigravity](https://antigravity.google/) |
| <a href="https://hermes-agent.nousresearch.com/docs/guides/work-with-skills"><img src="https://www.google.com/s2/favicons?domain=hermes-agent.nousresearch.com&sz=64" width="24" height="24" alt="Hermes"></a> | [Hermes](https://hermes-agent.nousresearch.com/docs/guides/work-with-skills) | `~/.hermes/skills/<category>/oh-my-gh-writing`에 배치 | single-file HTTP install은 `SKILL.md`에만 적합합니다. `reference/`를 유지하세요. [Hermes Skills](https://hermes-agent.nousresearch.com/docs/guides/work-with-skills) |
| <a href="https://cursor.com/docs"><img src="https://www.google.com/s2/favicons?domain=cursor.com&sz=64" width="24" height="24" alt="Cursor"></a> | [Cursor](https://cursor.com/docs) | router와 필요한 scenario rules를 project rules 또는 knowledge base로 변환 | [Cursor Docs](https://cursor.com/docs) 확인 |
| <a href="https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/add-custom-instructions/add-repository-instructions"><img src="https://www.google.com/s2/favicons?domain=github.com&sz=64" width="24" height="24" alt="GitHub"></a> | [GitHub Copilot](https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/add-custom-instructions/add-repository-instructions) | `.github/copilot-instructions.md`, `.github/instructions/*.instructions.md`, 또는 Copilot agent skill structure로 변환 | [Copilot Custom Instructions](https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/add-custom-instructions/add-repository-instructions) |
| <a href="https://docs.continue.dev/customize/rules"><img src="https://www.google.com/s2/favicons?domain=continue.dev&sz=64" width="24" height="24" alt="Continue"></a> | [Continue](https://docs.continue.dev/customize/rules) | `.continue/rules/*.md`로 변환합니다. 시나리오별 파일이 더 안정적입니다 | [Continue Rules](https://docs.continue.dev/customize/rules) |
| <a href="https://docs.windsurf.com"><img src="https://www.google.com/s2/favicons?domain=windsurf.com&sz=64" width="24" height="24" alt="Windsurf"></a> | [Windsurf / Devin Desktop](https://docs.windsurf.com) | 현재 docs는 customization용 memories와 rules를 언급합니다 | [Windsurf / Devin Docs](https://docs.windsurf.com)에서 최신 방식을 확인하세요 |

## Quick Start

```bash
# Codex
git clone https://github.com/PINKIIILQWQ/oh-my-gh-writing.git "$HOME/.agents/skills/oh-my-gh-writing"

# Claude Code
git clone https://github.com/PINKIIILQWQ/oh-my-gh-writing.git "$HOME/.claude/skills/oh-my-gh-writing"
```

로컬 개발용 symlink:

```bash
# Codex / Gemini CLI
ln -sfn "$PWD" "$HOME/.agents/skills/oh-my-gh-writing"

# Claude Code
ln -sfn "$PWD" "$HOME/.claude/skills/oh-my-gh-writing"
```

예시:

```text
이 저장소의 README를 작성해 줘.
이 bug report를 GitHub Issue로 정리해 줘.
현재 diff를 바탕으로 PR description을 작성해 줘.
이 PR을 review하고 blocking / major / minor / nit로 분류해 줘.
```

## Artifact Standards

| # | Category | Scenario | Use when |
|---|----------|----------|----------|
| 1 | Issue | Bug Report | 재현 가능한 defect를 보고할 때 |
| 2 | Issue | Feature Request | 새 feature 또는 API를 제안할 때 |
| 3 | Issue | Enhancement | 기존 동작을 개선할 때 |
| 4 | Issue | Discussion | 열린 community discussion을 시작할 때 |
| 5 | PR | Feature PR | 새 feature PR을 설명할 때 |
| 6 | PR | Bug Fix PR | bug fix PR을 설명할 때 |
| 7 | PR | Refactor PR | 동작 변화 없는 refactor를 설명할 때 |
| 8 | PR | Documentation PR | documentation-only changes를 설명할 때 |
| 9 | Review | Code Review | code changes를 review할 때 |
| 10 | Commit | Standard Commit | commit message를 작성할 때 |
| 11 | Docs | README | project homepage를 만들거나 수정할 때 |
| 12 | Docs | CONTRIBUTING | contribution guidelines를 만들 때 |
| 13 | Docs | CHANGELOG | version history를 작성할 때 |
| 14 | Release | Release Notes | release announcement를 작성할 때 |
| 15 | Release | Migration Guide | upgrade steps를 설명할 때 |
| 16 | Design | RFC | design proposal을 작성할 때 |
| 17 | Templates | Issue Form YAML | GitHub Issue Forms를 만들 때 |
| 18 | Templates | PR Template | Pull Request templates를 만들 때 |

각 scenario의 standard file은 `reference/`에 있습니다. 전체 탐색은 [`INDEX.md`](INDEX.md)를 참고하세요.

## Repository Structure

```text
oh-my-gh-writing/
├── README.md
├── README.*.md
├── README_Example.md
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

scenario rules, reference sources, output validation, 작은 Markdown helpers에 대한 기여를 환영합니다. examples나 test cases를 추가하려면 먼저 Issue 또는 Discussion에서 source, scenario, test goal, license/privacy boundary를 설명해 주세요.

`SKILL.md`는 가볍게 유지하고 scenario details는 해당 `reference/*.md`에 넣어 주세요. [`CONTRIBUTING.md`](CONTRIBUTING.md)를 참고하세요.

## Sources

규칙은 [GitHub Docs](https://docs.github.com/en), [Conventional Commits](https://www.conventionalcommits.org/), [Keep a Changelog](https://keepachangelog.com/), [Google Engineering Practices](https://google.github.io/eng-practices/review/) 및 Angular, Kubernetes, React, TypeScript, VS Code, Node.js, Tailwind CSS 같은 성숙한 오픈소스 프로젝트를 참고합니다. [`reference/source-catalog.md`](reference/source-catalog.md)를 참고하세요.

## License

[MIT](LICENSE) © 2026 oh-my-gh-writing contributors
