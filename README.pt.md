<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/oh-my-gh-writing-logo.png">
  <img alt="oh-my-gh-writing" src="assets/oh-my-gh-writing-logo.png" width="160">
</picture>

# oh-my-gh-writing

[![License](https://img.shields.io/github/license/PINKIIILQWQ/oh-my-gh-writing?label=License&color=blue)](LICENSE)
[![Scenarios](https://img.shields.io/badge/Scenarios-18-6a0dad)](#-índice-de-cenários)
[![Agent](https://img.shields.io/badge/Agent-Claude%20Code-8A2BE2)](https://claude.ai/code)
[![PRs](https://img.shields.io/badge/PRs-Welcome-brightgreen)](CONTRIBUTING.md)
[![GitHub last commit](https://img.shields.io/github/last-commit/PINKIIILQWQ/oh-my-gh-writing?label=Updated)](https://github.com/PINKIIILQWQ/oh-my-gh-writing/commits/main)

**oh-my-gh-writing** é um sistema de normas de escrita para GitHub projetado para Agentes de IA. Não é um gerador de README nem um aplicativo independente, mas um pacote de habilidade portátil. Quando um Agente o carrega, ele roteia automaticamente a saída para o cenário correto (Issue, PR, Review, Commit, README, CHANGELOG, RFC, etc.) com qualidade consistente, limites de evidência e formato pronto para envio.

---

## Índice de cenários

| # | Categoria | Cenários | Arquivo padrão |
|---|-----------|----------|----------------|
| 1–4 | Issue | Bug Report / Feature Request / Enhancement / Discussion | `reference/bug-report.md` etc. |
| 5–8 | PR | Feature PR / Bug Fix PR / Refactor PR / Documentation PR | `reference/feature-pr.md` etc. |
| 9–10 | Review & Commit | Code Review / Standard Commit | `reference/code-review.md` etc. |
| 11–13 | Docs | README / CONTRIBUTING / CHANGELOG | `reference/readme.md` etc. |
| 14–15 | Release | Release Notes / Migration Guide | `reference/release-notes.md` etc. |
| 16 | Design | RFC | `reference/rfc.md` |
| 17–18 | Templates | Issue Form YAML / PR Template | `reference/issue-form-yaml.md` etc. |

Regras de roteamento completas em [`SKILL.md`](SKILL.md).

---

## Instalação

### Claude Code (carregamento direto)

```bash
gh repo clone PINKIIILQWQ/oh-my-gh-writing ~/.claude/skills/oh-my-gh-writing
```

Em seguida, use `/oh-my-gh-writing` no Claude Code.

### Outros Agentes de IA

| Agente | Nível de suporte | Ação |
|--------|------------------|------|
| Cline / Roo Code | Importação adaptada | Copie o conteúdo de `SKILL.md` nas instruções personalizadas do projeto; carregue o `reference/*.md` correspondente conforme necessário |

> Esta habilidade foi projetada nativamente para Claude Code. Outros agentes precisam de adaptação ao seu próprio sistema de regras.

---

## Início rápido

```text
/oh-my-gh-writing Escreva um Bug Report
/oh-my-gh-writing Escreva uma descrição de PR para estas alterações
/oh-my-gh-writing Revise as alterações deste PR
/oh-my-gh-writing Escreva uma entrada de CHANGELOG
```

O agente roteia para o cenário correto, carrega as regras `reference/*.md` correspondentes e produz um artefato pronto para envio ao GitHub.

---

## Princípios fundamentais

- **Limites de evidência** — Versões, números de PR, resultados de teste e comandos de instalação devem ter uma fonte; marque fatos desconhecidos como `TODO`
- **Roteamento preciso** — Roteie pela intenção do usuário; uma Feature Request nunca é escrita como um PR já implementado
- **Limpeza de saída** — Artefatos colam diretamente no GitHub — sem preâmbulos conversacionais, sem blocos de código externos, sem metadados de teste
- **Um artefato, um trabalho** — Nunca misture várias issues ou release notes em uma única saída
- **Usabilidade primeiro** — Esboce com marcadores `TODO` em vez de bloquear por falta de informações

---

## Estrutura do projeto

```
oh-my-gh-writing/
├── SKILL.md                    # Roteador de execução do Agente e regras compartilhadas
├── INDEX.md                    # Navegação do repositório
├── reference/
│   ├── bug-report.md           # Padrão Bug Report
│   ├── feature-request.md      # Padrão Feature Request
│   ├── enhancement.md          # Padrão Enhancement
│   ├── discussion.md           # Padrão Discussion
│   ├── feature-pr.md           # Padrão Feature PR
│   ├── bug-fix-pr.md           # Padrão Bug Fix PR
│   ├── refactor-pr.md          # Padrão Refactor PR
│   ├── documentation-pr.md     # Padrão Documentation PR
│   ├── code-review.md          # Padrão Code Review
│   ├── standard-commit.md      # Padrão de mensagem de commit
│   ├── readme.md               # Padrão de escrita README
│   ├── contributing.md         # Padrão de escrita CONTRIBUTING
│   ├── changelog.md            # Padrão CHANGELOG
│   ├── release-notes.md        # Padrão Release Notes
│   ├── migration-guide.md      # Padrão Migration Guide
│   ├── rfc.md                  # Padrão RFC
│   ├── issue-form-yaml.md      # Padrão Issue Form YAML
│   ├── pr-template.md          # Padrão PR Template
│   ├── weapons.md              # Ferramentas Markdown do GitHub
│   ├── emoji-guide.md          # Guia de emojis
│   ├── output-validation.md    # Lista de verificação de validação de saída
│   └── source-catalog.md       # Catálogo de fontes de referência
├── CONTRIBUTING.md             # Guia de contribuição
├── assets/                     # Assets do projeto
└── LICENSE                     # MIT
```

---

## Contribuição

PRs são bem-vindos para melhorar regras de cenários, fontes de referência ou validação de saída. Veja [`CONTRIBUTING.md`](CONTRIBUTING.md).

---

## Licença

[MIT](LICENSE)
