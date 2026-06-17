<p align="center">
  <img src="assets/oh-my-gh-writing-logo.png" alt="logotipo de oh-my-gh-writing" width="200">
</p>

<h1 align="center">oh-my-gh-writing</h1>

<p align="center">
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-MIT-0f766e?style=flat" alt="Licencia MIT"></a>
  <a href="SKILL.md"><img src="https://img.shields.io/badge/Status-Release%20Candidate-2563eb?style=flat" alt="Release Candidate"></a>
  <a href="INDEX.md"><img src="https://img.shields.io/badge/Scenarios-18-6a0dad?style=flat" alt="18 escenarios"></a>
  <a href="SKILL.md"><img src="https://img.shields.io/badge/Format-SKILL.md-22AA66?style=flat" alt="SKILL.md"></a>
</p>

<p align="center">
  <a href="README.md">简体中文</a> · <a href="README.en.md">English</a> · Español · <a href="README.hi.md">हिन्दी</a> · <a href="README.ar.md">العربية</a> · <a href="README.fr.md">Français</a> · <a href="README.pt.md">Português</a> · <a href="README.ja.md">日本語</a> · <a href="README.ko.md">한국어</a>
</p>

**oh-my-gh-writing** es un paquete de escritura para GitHub orientado a AI Agents. Enruta tareas comunes como Issues, PRs, Reviews, Commits, README, CHANGELOG, Release Notes, Migration Guides, RFCs, Issue Forms y PR Templates hacia estándares específicos por escenario, para producir borradores Markdown o YAML claros, con límites de evidencia explícitos y más cercanos a ser publicables.

No es un generador de README ni un servicio de integración con GitHub. Es una base portable de reglas Markdown: las herramientas con soporte nativo para Agent Skills pueden cargarla directamente; las demás pueden adaptar `SKILL.md` y los archivos `reference/*.md` necesarios como reglas, instrucciones o base de conocimiento.

## ¿Por qué usar oh-my-gh-writing?

Escribir bien para GitHub no consiste solo en llenar Markdown. Lo difícil es reconocer el escenario, saber qué hechos deben verificarse, qué no debe inventarse y si el resultado puede pegarse en un Issue, PR, Review o README sin limpieza adicional.

- **18 escenarios de escritura GitHub**: Issues, PRs, Code Review, Commit, README, CHANGELOG, Release Notes, Migration Guide, RFC, Issue Form, PR Template y más.
- **Primero enruta, luego escribe**: separa Feature Request, Enhancement, Discussion, Feature PR, Bug Fix PR y Refactor PR.
- **Carga progresiva de referencias**: `SKILL.md` queda ligero y las reglas detalladas se cargan solo cuando hacen falta.
- **Límites de evidencia**: versiones, comandos, CI, compatibilidad, releases e IDs de issues/PRs no se inventan.
- **Artifacts más limpios**: evita introducciones conversacionales, fences externos, títulos de prueba y restos de copia.
- **Referencias reales**: se inspira en GitHub Docs, Conventional Commits, Keep a Changelog y proyectos como React, Kubernetes, TypeScript, Node.js y Tailwind CSS.

## Formas de uso

**Como skill**: coloca este repositorio donde el agente pueda cargar una carpeta con `SKILL.md` y leer `reference/` bajo demanda.

**Como reglas**: si tu herramienta no consume este formato, adapta la tabla de rutas de `SKILL.md` y los `reference/*.md` relevantes a reglas de proyecto, instrucciones personalizadas o una base de conocimiento.

| Icono | Agent / Tool | Configuración recomendada | Notas / Docs |
|-------|--------------|---------------------------|--------------|
| <img src="https://openai.com/favicon.ico" width="14" height="14" alt="OpenAI"> | Codex | Clonar en `$HOME/.agents/skills/oh-my-gh-writing` o `.agents/skills/oh-my-gh-writing` | [Codex Agent Skills](https://developers.openai.com/codex/skills) |
| <img src="https://claude.ai/favicon.ico" width="14" height="14" alt="Claude"> | Claude Code | Clonar o enlazar en `~/.claude/skills/oh-my-gh-writing` o `.claude/skills/oh-my-gh-writing` | [Claude Code Skills](https://code.claude.com/docs/en/skills) |
| <img src="https://geminicli.com/favicon.ico" width="14" height="14" alt="Gemini CLI"> | Gemini CLI / Antigravity CLI | La documentación menciona `~/.gemini/skills/`, `~/.agents/skills/` y `gemini skills install` | Confirma la [documentación oficial](https://geminicli.com/docs/cli/skills/) actual |
| <img src="https://hermes-agent.nousresearch.com/favicon.ico" width="14" height="14" alt="Hermes"> | Hermes | Colocar en `~/.hermes/skills/<category>/oh-my-gh-writing` | La instalación HTTP de un solo archivo solo sirve para `SKILL.md`; conserva `reference/`. Ver [Hermes Skills](https://hermes-agent.nousresearch.com/docs/guides/work-with-skills) |
| <img src="https://cursor.com/favicon.ico" width="14" height="14" alt="Cursor"> | Cursor | Adaptar el router y las reglas necesarias a reglas de proyecto o conocimiento | Verifica [Cursor Docs](https://cursor.com/docs) |
| <img src="https://github.com/favicon.ico" width="14" height="14" alt="GitHub"> | GitHub Copilot | Adaptar a `.github/copilot-instructions.md`, `.github/instructions/*.instructions.md` o estructura de skill | [Copilot Custom Instructions](https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/add-custom-instructions/add-repository-instructions) |
| <img src="https://docs.continue.dev/favicon.ico" width="14" height="14" alt="Continue"> | Continue | Adaptar a `.continue/rules/*.md`; separar por escenario es más estable | [Continue Rules](https://docs.continue.dev/customize/rules) |
| <img src="https://docs.windsurf.com/favicon.ico" width="14" height="14" alt="Windsurf"> | Windsurf / Devin Desktop | La documentación actual menciona memories y rules | Confirma ruta y método en [Windsurf / Devin Docs](https://docs.windsurf.com) |

## Inicio rápido

```bash
# Codex
git clone https://github.com/PINKIIILQWQ/oh-my-gh-writing.git "$HOME/.agents/skills/oh-my-gh-writing"

# Claude Code
git clone https://github.com/PINKIIILQWQ/oh-my-gh-writing.git "$HOME/.claude/skills/oh-my-gh-writing"
```

Enlaces simbólicos para desarrollo local:

```bash
# Codex / Gemini CLI
ln -sfn "$PWD" "$HOME/.agents/skills/oh-my-gh-writing"

# Claude Code
ln -sfn "$PWD" "$HOME/.claude/skills/oh-my-gh-writing"
```

Ejemplos:

```text
Escribe un README para este repositorio.
Convierte este bug en un GitHub Issue.
Escribe una descripción de PR a partir del diff actual.
Revisa este PR y clasifica los hallazgos como blocking / major / minor / nit.
```

## Escenarios

| # | Categoría | Escenario | Cuándo usarlo |
|---|-----------|-----------|---------------|
| 1 | Issue | Bug Report | Reportar un defecto reproducible |
| 2 | Issue | Feature Request | Proponer una nueva función o API |
| 3 | Issue | Enhancement | Mejorar un comportamiento existente |
| 4 | Issue | Discussion | Abrir una discusión comunitaria |
| 5 | PR | Feature PR | Describir un PR de nueva funcionalidad |
| 6 | PR | Bug Fix PR | Describir un PR de corrección |
| 7 | PR | Refactor PR | Describir una refactorización sin cambio funcional |
| 8 | PR | Documentation PR | Describir cambios solo de documentación |
| 9 | Review | Code Review | Revisar cambios de código |
| 10 | Commit | Standard Commit | Escribir mensajes de commit |
| 11 | Docs | README | Crear o revisar la página principal |
| 12 | Docs | CONTRIBUTING | Crear una guía de contribución |
| 13 | Docs | CHANGELOG | Escribir historial de versiones |
| 14 | Release | Release Notes | Escribir notas de lanzamiento |
| 15 | Release | Migration Guide | Explicar pasos de migración |
| 16 | Design | RFC | Proponer un diseño |
| 17 | Templates | Issue Form YAML | Crear formularios de Issue |
| 18 | Templates | PR Template | Crear plantillas de Pull Request |

Cada escenario tiene un archivo estándar en `reference/`. La navegación completa está en [`INDEX.md`](INDEX.md).

## Estructura

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

## Contribuir

Se aceptan contribuciones a reglas de escenario, fuentes de referencia, validación de salida y pequeñas herramientas Markdown. Para ejemplos o casos de prueba, describe primero la fuente, el escenario, el objetivo y los límites de licencia o privacidad en un Issue o Discussion.

Mantén `SKILL.md` ligero y coloca los detalles en el `reference/*.md` correspondiente. Consulta [`CONTRIBUTING.md`](CONTRIBUTING.md).

## Fuentes

Las reglas toman referencia de [GitHub Docs](https://docs.github.com/en), [Conventional Commits](https://www.conventionalcommits.org/), [Keep a Changelog](https://keepachangelog.com/), [Google Engineering Practices](https://google.github.io/eng-practices/review/) y proyectos maduros como Angular, Kubernetes, React, TypeScript, VS Code, Node.js y Tailwind CSS. Consulta [`reference/source-catalog.md`](reference/source-catalog.md).

## Licencia

[MIT](LICENSE) © 2026 oh-my-gh-writing contributors
