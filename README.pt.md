<p align="center">
  <img src="assets/oh-my-gh-writing-logo.png" alt="logo do oh-my-gh-writing" width="200">
</p>

<h1 align="center">oh-my-gh-writing</h1>

<p align="center">
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-MIT-0f766e?style=flat" alt="Licença MIT"></a>
  <a href="SKILL.md"><img src="https://img.shields.io/badge/Status-Release%20Candidate-2563eb?style=flat" alt="Release Candidate"></a>
  <a href="INDEX.md"><img src="https://img.shields.io/badge/Artifacts-18-6a0dad?style=flat" alt="18 padrões de artefatos"></a>
  <a href="INDEX.md"><img src="https://img.shields.io/badge/Workflows-7-0f766e?style=flat" alt="7 pacotes de workflow"></a>
  <a href="SKILL.md"><img src="https://img.shields.io/badge/Format-SKILL.md-22AA66?style=flat" alt="SKILL.md"></a>
</p>

<p align="center">
  <a href="README.md">简体中文</a> · <a href="README.en.md">English</a> · <a href="README.es.md">Español</a> · <a href="README.hi.md">हिन्दी</a> · <a href="README.ar.md">العربية</a> · <a href="README.fr.md">Français</a> · Português · <a href="README.ja.md">日本語</a> · <a href="README.ko.md">한국어</a>
</p>

**oh-my-gh-writing** é um pacote de escrita para GitHub voltado a AI Agents. Ele roteia tarefas comuns como Issues, PRs, Reviews, Commits, README, CHANGELOG, Release Notes, Migration Guides, RFCs, Issue Forms e PR Templates para padrões específicos por cenário, ajudando o agente a produzir rascunhos Markdown ou YAML claros, estruturados e com limites de evidência explícitos.

Ele não é um gerador de README nem um serviço de integração com GitHub. É uma base portátil de regras Markdown: ferramentas com suporte nativo a Agent Skills podem carregá-lo diretamente; outras ferramentas podem adaptar `SKILL.md` e os arquivos `reference/*.md` relevantes como regras, instruções ou base de conhecimento.

## Por que usar oh-my-gh-writing?

Escrever bem para GitHub não é apenas preencher Markdown. O difícil é reconhecer o cenário, saber quais fatos precisam ser verificados, o que não deve ser inventado e se o artifact final pode ser colado em uma Issue, PR, Review ou README sem limpeza adicional.

- **18 padrões de artefatos GitHub + 7 pacotes de workflow**: Issues, PRs, Code Review, Commit, README, CHANGELOG, Release Notes, Migration Guide, RFC, Issue Form, PR Template e pacotes compostos.
- **Roteie antes de escrever**: separa Feature Request, Enhancement, Discussion, Feature PR, Bug Fix PR e Refactor PR.
- **Carregamento progressivo de referências**: `SKILL.md` permanece leve; regras detalhadas são carregadas apenas quando necessário.
- **Limites de evidência**: versões, comandos, CI, compatibilidade, releases e números de issues/PRs não são inventados.
- **Artifacts mais limpos**: evita prefácios conversacionais, fences Markdown externos, títulos de teste e resíduos de cópia.
- **Referências open source reais**: GitHub Docs, Conventional Commits, Keep a Changelog e projetos como React, Kubernetes, TypeScript, Node.js e Tailwind CSS.

## Modos de uso

**Como skill**: coloque este repositório em um local onde o agente consiga carregar uma pasta com `SKILL.md` e ler `reference/` sob demanda.

**Como regras**: se sua ferramenta não consumir este formato, adapte a tabela de roteamento em `SKILL.md` e os `reference/*.md` relevantes para regras de projeto, instruções personalizadas ou base de conhecimento.

| Ícone | Agent / Tool | Configuração recomendada | Notas / Docs |
|------|--------------|--------------------------|--------------|
| <a href="https://developers.openai.com/codex/skills"><img src="https://www.google.com/s2/favicons?domain=openai.com&sz=64" width="24" height="24" alt="OpenAI"></a> | [Codex](https://developers.openai.com/codex/skills) | Clone em `$HOME/.agents/skills/oh-my-gh-writing` ou `.agents/skills/oh-my-gh-writing` | [Codex Agent Skills](https://developers.openai.com/codex/skills) |
| <a href="https://code.claude.com/docs/en/skills"><img src="https://www.google.com/s2/favicons?domain=claude.ai&sz=64" width="24" height="24" alt="Claude"></a> | [Claude Code](https://code.claude.com/docs/en/skills) | Clone ou symlink em `~/.claude/skills/oh-my-gh-writing` ou `.claude/skills/oh-my-gh-writing` | [Claude Code Skills](https://code.claude.com/docs/en/skills) |
| <a href="https://geminicli.com/docs/cli/skills/"><img src="https://www.google.com/s2/favicons?domain=geminicli.com&sz=64" width="24" height="24" alt="Gemini CLI"></a> | [Gemini CLI](https://geminicli.com/docs/cli/skills/) | A documentação lista `~/.gemini/skills/`, `~/.agents/skills/` e `gemini skills install` | Confirme a [documentação oficial](https://geminicli.com/docs/cli/skills/) atual |
| <a href="https://antigravity.google/"><img src="https://www.google.com/s2/favicons?domain=antigravity.google&sz=64" width="24" height="24" alt="Antigravity"></a> | [Antigravity CLI](https://antigravity.google/) | Confirme na documentação atual o caminho de integração de skills / rules | [Google Antigravity](https://antigravity.google/) |
| <a href="https://hermes-agent.nousresearch.com/docs/guides/work-with-skills"><img src="assets/hermeslogo.png" width="24" height="24" alt="Hermes"></a> | [Hermes](https://hermes-agent.nousresearch.com/docs/guides/work-with-skills) | Coloque em `~/.hermes/skills/<category>/oh-my-gh-writing` | Instalação HTTP de arquivo único serve apenas para `SKILL.md`; mantenha `reference/`. Veja [Hermes Skills](https://hermes-agent.nousresearch.com/docs/guides/work-with-skills) |
| <a href="https://cursor.com/docs"><img src="https://www.google.com/s2/favicons?domain=cursor.com&sz=64" width="24" height="24" alt="Cursor"></a> | [Cursor](https://cursor.com/docs) | Adapte o router e as regras necessárias para regras de projeto ou base de conhecimento | Confira [Cursor Docs](https://cursor.com/docs) |
| <a href="https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/add-custom-instructions/add-repository-instructions"><img src="https://www.google.com/s2/favicons?domain=github.com&sz=64" width="24" height="24" alt="GitHub"></a> | [GitHub Copilot](https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/add-custom-instructions/add-repository-instructions) | Adapte para `.github/copilot-instructions.md`, `.github/instructions/*.instructions.md` ou estrutura de skill | [Copilot Custom Instructions](https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/add-custom-instructions/add-repository-instructions) |
| <a href="https://docs.continue.dev/customize/rules"><img src="https://www.google.com/s2/favicons?domain=continue.dev&sz=64" width="24" height="24" alt="Continue"></a> | [Continue](https://docs.continue.dev/customize/rules) | Adapte para `.continue/rules/*.md`; arquivos por cenário são mais estáveis | [Continue Rules](https://docs.continue.dev/customize/rules) |
| <a href="https://docs.windsurf.com"><img src="https://www.google.com/s2/favicons?domain=windsurf.com&sz=64" width="24" height="24" alt="Windsurf"></a> | [Windsurf / Devin Desktop](https://docs.windsurf.com) | A documentação atual menciona memories e rules para personalização | Confirme o método em [Windsurf / Devin Docs](https://docs.windsurf.com) |

## Início rápido

```bash
# Codex
git clone https://github.com/PINKIIILQWQ/oh-my-gh-writing.git "$HOME/.agents/skills/oh-my-gh-writing"

# Claude Code
git clone https://github.com/PINKIIILQWQ/oh-my-gh-writing.git "$HOME/.claude/skills/oh-my-gh-writing"
```

Symlinks para desenvolvimento local:

```bash
# Codex / Gemini CLI
ln -sfn "$PWD" "$HOME/.agents/skills/oh-my-gh-writing"

# Claude Code
ln -sfn "$PWD" "$HOME/.claude/skills/oh-my-gh-writing"
```

Exemplos:

```text
Escreva um README para este repositório.
Transforme este bug report em uma GitHub Issue.
Escreva uma descrição de PR a partir do diff atual.
Revise este PR e classifique os achados como blocking / major / minor / nit.
```

## Cenários

| # | Categoria | Cenário | Quando usar |
|---|-----------|---------|-------------|
| 1 | Issue | Bug Report | Reportar um defeito reproduzível |
| 2 | Issue | Feature Request | Propor uma nova funcionalidade ou API |
| 3 | Issue | Enhancement | Melhorar um comportamento existente |
| 4 | Issue | Discussion | Abrir uma discussão comunitária |
| 5 | PR | Feature PR | Descrever um PR de nova funcionalidade |
| 6 | PR | Bug Fix PR | Descrever um PR de correção |
| 7 | PR | Refactor PR | Descrever uma refatoração sem mudança de comportamento |
| 8 | PR | Documentation PR | Descrever alterações apenas de documentação |
| 9 | Review | Code Review | Revisar mudanças de código |
| 10 | Commit | Standard Commit | Escrever mensagens de commit |
| 11 | Docs | README | Criar ou revisar a página inicial do projeto |
| 12 | Docs | CONTRIBUTING | Criar diretrizes de contribuição |
| 13 | Docs | CHANGELOG | Escrever histórico de versões |
| 14 | Release | Release Notes | Escrever notas de lançamento |
| 15 | Release | Migration Guide | Explicar passos de migração |
| 16 | Design | RFC | Propor um design |
| 17 | Templates | Issue Form YAML | Criar GitHub Issue Forms |
| 18 | Templates | PR Template | Criar templates de Pull Request |

Cada cenário tem um arquivo padrão em `reference/`. A navegação completa está em [`INDEX.md`](INDEX.md).

## Estrutura

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

## Contribuindo

Contribuições para regras de cenário, fontes de referência, validação de saída e pequenos helpers Markdown são bem-vindas. Para exemplos ou casos de teste, descreva primeiro a fonte, o cenário, o objetivo do teste e os limites de licença ou privacidade em uma Issue ou Discussion.

Mantenha `SKILL.md` leve e coloque detalhes no `reference/*.md` correspondente. Consulte [`CONTRIBUTING.md`](CONTRIBUTING.md).

## Fontes

As regras usam como referência [GitHub Docs](https://docs.github.com/en), [Conventional Commits](https://www.conventionalcommits.org/), [Keep a Changelog](https://keepachangelog.com/), [Google Engineering Practices](https://google.github.io/eng-practices/review/) e projetos maduros como Angular, Kubernetes, React, TypeScript, VS Code, Node.js e Tailwind CSS. Veja [`reference/source-catalog.md`](reference/source-catalog.md).

## Licença

[MIT](LICENSE) © 2026 oh-my-gh-writing contributors
