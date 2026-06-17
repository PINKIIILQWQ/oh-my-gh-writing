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
  <a href="INDEX.md"><img src="https://img.shields.io/badge/Scenarios-18-6a0dad?style=flat" alt="18 Cenários"></a>
  <a href="SKILL.md"><img src="https://img.shields.io/badge/Format-Agent%20Skill-22AA66?style=flat" alt="Agent Skill"></a>
</p>

**oh-my-gh-writing** é um pacote de habilidades de escrita para GitHub voltado para Agentes de IA. Ele direciona necessidades comuns de escrita no GitHub (Issues, PRs, READMEs, CHANGELOGs, etc.) para o padrão de qualidade apropriado, garantindo que cada saída siga as convenções da comunidade — pronta para envio e legível sem ajustes manuais.

O conjunto completo de regras é armazenado como arquivos Markdown neste repositório, sem dependências externas. Qualquer Agente de IA que suporte carregamento de habilidades locais pode usá-lo diretamente.

## Agentes compatíveis

oh-my-gh-writing foi projetado para Agentes de IA. Qualquer ferramenta de codificação com IA que suporte carregamento de regras personalizadas, bases de conhecimento ou instruções do sistema pode usar esta habilidade. Os níveis de suporte variam de acordo com a plataforma:

**Direct** — Pode carregar `SKILL.md` e seu diretório `reference/` nativamente, com correspondência e roteamento automáticos de cenários. Nenhuma seleção manual de cenário necessária.

**Adapted** — Não pode carregar o formato de habilidade diretamente, mas pode referenciar os padrões de escrita através de arquivos de regras do projeto (por exemplo, `.cursorrules`, `copilot-instructions.md`), instruções personalizadas ou indexação de documentação. O roteamento automático é limitado — os usuários precisam especificar o cenário manualmente.

| Ícone | Agent | Nível | Como usar | Documentação |
|-------|-------|-------|-----------|--------------|
| <img src="https://docs.anthropic.com/favicon.ico" width="14" height="14"> | **Claude Code** | Direct | Adicionar este repositório à lista de habilidades; roteamento automático | [Docs Claude Code](https://docs.anthropic.com/en/docs/claude-code) |
| <img src="https://docs.anthropic.com/favicon.ico" width="14" height="14"> | **Claude** (Web/API) | Adapted | Injetar `SKILL.md` e `reference/*.md` nas instruções do sistema | [Docs Claude API](https://docs.anthropic.com/en/docs) |
| <img src="https://cursor.sh/favicon.ico" width="14" height="14"> | **Cursor** | Adapted | Referenciar regras via `.cursorrules` ou indexar `reference/` com Docs | [Docs Cursor](https://docs.cursor.com) |
| <img src="https://github.com/favicon.ico" width="14" height="14"> | **GitHub Copilot** | Adapted | Referenciar regras principais em `.github/copilot-instructions.md` | [Docs Copilot](https://docs.github.com/en/copilot) |
| <img src="https://docs.continue.dev/favicon.ico" width="14" height="14"> | **Continue** | Adapted | Apontar fonte de docs para `reference/`; recuperar via `@docs` | [Docs Continue](https://docs.continue.dev) |
| <img src="https://codeium.com/favicon.ico" width="14" height="14"> | **Windsurf** | Adapted | Referenciar regras via `.windsurfrules` ou configuração AI Rules | [Docs Windsurf](https://docs.codeium.com) |

Ferramentas de IA não listadas aqui também podem usar esta habilidade no modo Adapted, desde que suportem instruções personalizadas ou carregamento de arquivos de regras. Os padrões de escrita principais (`reference/*.md`) são Markdown simples — qualquer ferramenta que possa ler Markdown pode referenciá-los.

## Cenários

| # | Categoria | Cenário | Quando usar |
|---|-----------|---------|-------------|
| 1 | Issue | Bug Report | Reportar um defeito reproduzível |
| 2 | Issue | Feature Request | Propor um novo recurso ou API |
| 3 | Issue | Enhancement | Melhorar uma capacidade existente |
| 4 | Issue | Discussion | Discussão comunitária aberta |
| 5 | PR | Feature PR | Pull Request de novo recurso |
| 6 | PR | Bug Fix PR | Pull Request de correção de bug |
| 7 | PR | Refactor PR | Refatoração sem alteração de comportamento |
| 8 | PR | Documentation PR | Alterações apenas na documentação |
| 9 | Review | Code Review | Revisar alterações de código |
| 10 | Commit | Standard Commit | Escrever mensagens de commit |
| 11 | Docs | README | Documentação inicial do projeto |
| 12 | Docs | CONTRIBUTING | Guia de contribuição |
| 13 | Docs | CHANGELOG | Registro de alterações de versão |
| 14 | Release | Release Notes | Anúncio de lançamento |
| 15 | Release | Migration Guide | Guia de atualização |
| 16 | Design | RFC | Proposta de design |
| 17 | Templates | Issue Form YAML | Formulários de Issue do GitHub |
| 18 | Templates | PR Template | Modelo de Pull Request |

Cada cenário possui um arquivo de padrão de escrita correspondente em `reference/`, com estrutura padrão, campos obrigatórios, regras de limites factuais, fontes de referência de alta qualidade e uma lista de verificação de elementos obrigatórios.

## Início rápido

Carregue este repositório como uma habilidade em seu Agente de IA:

```bash
# Claude Code — configure em .claude/settings.json ou na configuração do Claude
# Ou referencie SKILL.md diretamente como parte das instruções do sistema do Agente
```

Para todas as regras de cenários e roteamento, consulte [`SKILL.md`](SKILL.md). Índice completo em [`INDEX.md`](INDEX.md).

## Estrutura do projeto

```
oh-my-gh-writing/
├── SKILL.md                  # Ponto de entrada do Agente e roteamento
├── INDEX.md                  # Índice de navegação completo
├── CONTRIBUTING.md           # Regras de contribuição
├── LICENSE                   # Licença MIT
├── .gitignore
├── assets/                   # Recursos do projeto
│   └── oh-my-gh-writing-logo.png
└── reference/                # Arquivos de padrões de cenários
    ├── shared-principles.md  # 19 regras de qualidade compartilhadas
    ├── readme.md             # Regras de escrita do README
    ├── output-validation.md  # Lista de verificação de validação de saída
    └── source-catalog.md     # Catálogo de fontes de referência
```

## Contribuir

Contribuições são bem-vindas — seja corrigindo regras de cenários, melhorando a qualidade das fontes de referência, adicionando referências de ferramentas Markdown ou enviando casos de uso.

- Abra primeiro uma Issue ou Discussão para discutir suas ideias
- Faça um Fork do repositório e envie um PR
- Coloque as regras de cenários no `reference/*.md` correspondente, não na camada de roteamento
- Mantenha o `SKILL.md` leve e focado no roteamento

Consulte [`CONTRIBUTING.md`](CONTRIBUTING.md) para regras detalhadas.

## Agradecimentos

- [GitHub Docs](https://docs.github.com/en) — Modelos de Issue/PR, sintaxe Markdown e práticas comunitárias
- [Conventional Commits](https://www.conventionalcommits.org/) — Especificação de formato de mensagens de commit
- [Keep a Changelog](https://keepachangelog.com/) — Padrão de formato CHANGELOG
- [shields.io](https://shields.io) — Serviço de geração de badges
- [Google Engineering Practices](https://google.github.io/eng-practices/review/) — Guia de Code Review
- Modelos e guias de contribuição de projetos de código aberto como Angular, Kubernetes, React, TypeScript, VS Code, Node.js, Tailwind CSS — Referências estruturais para padrões de cenários
- [ikatyang/emoji-cheat-sheet](https://github.com/ikatyang/emoji-cheat-sheet) — Referência rápida de emojis
- [carloscuesta/gitmoji](https://github.com/carloscuesta/gitmoji) — Guia de emojis para intenção de commit

## Licença

[MIT](LICENSE) © 2026 oh-my-gh-writing contributors
