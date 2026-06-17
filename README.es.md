<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/oh-my-gh-writing-logo.png">
  <img alt="oh-my-gh-writing" src="assets/oh-my-gh-writing-logo.png" width="160">
</picture>

# oh-my-gh-writing

[![License](https://img.shields.io/github/license/PINKIIILQWQ/oh-my-gh-writing?label=License&color=blue)](LICENSE)
[![Scenarios](https://img.shields.io/badge/Scenarios-18-6a0dad)](#-índice-de-escenarios)
[![Agent](https://img.shields.io/badge/Agent-Claude%20Code-8A2BE2)](https://claude.ai/code)
[![PRs](https://img.shields.io/badge/PRs-Welcome-brightgreen)](CONTRIBUTING.md)
[![GitHub last commit](https://img.shields.io/github/last-commit/PINKIIILQWQ/oh-my-gh-writing?label=Updated)](https://github.com/PINKIIILQWQ/oh-my-gh-writing/commits/main)

**oh-my-gh-writing** es un sistema de normas de escritura para GitHub diseñado para Agentes de IA. No es un generador de README ni una aplicación independiente, sino un paquete de habilidades portátil. Cuando un Agente lo carga, enruta automáticamente la salida al escenario correcto (Issue, PR, Review, Commit, README, CHANGELOG, RFC, etc.) con calidad consistente, límites de evidencia y formato listo para enviar.

---

## Índice de escenarios

| # | Categoría | Escenarios | Archivo estándar |
|---|-----------|------------|------------------|
| 1–4 | Issue | Bug Report / Feature Request / Enhancement / Discussion | `reference/bug-report.md` etc. |
| 5–8 | PR | Feature PR / Bug Fix PR / Refactor PR / Documentation PR | `reference/feature-pr.md` etc. |
| 9–10 | Review & Commit | Code Review / Standard Commit | `reference/code-review.md` etc. |
| 11–13 | Docs | README / CONTRIBUTING / CHANGELOG | `reference/readme.md` etc. |
| 14–15 | Release | Release Notes / Migration Guide | `reference/release-notes.md` etc. |
| 16 | Design | RFC | `reference/rfc.md` |
| 17–18 | Templates | Issue Form YAML / PR Template | `reference/issue-form-yaml.md` etc. |

Reglas de enrutamiento completas en [`SKILL.md`](SKILL.md).

---

## Instalación

### Claude Code (carga directa)

```bash
gh repo clone PINKIIILQWQ/oh-my-gh-writing ~/.claude/skills/oh-my-gh-writing
```

Luego usa `/oh-my-gh-writing` dentro de Claude Code.

### Otros Agentes de IA

| Agente | Nivel de soporte | Acción |
|--------|------------------|--------|
| Cline / Roo Code | Importación adaptada | Copia el contenido de `SKILL.md` en las instrucciones personalizadas del proyecto; carga el `reference/*.md` correspondiente según sea necesario |

> Esta habilidad está diseñada de forma nativa para Claude Code. Otros agentes requieren adaptación a su propio sistema de normas.

---

## Inicio rápido

```text
/oh-my-gh-writing Escribe un Bug Report
/oh-my-gh-writing Escribe una descripción de PR para estos cambios
/oh-my-gh-writing Revisa los cambios de este PR
/oh-my-gh-writing Escribe una entrada de CHANGELOG
```

El agente enruta al escenario correcto, carga las normas `reference/*.md` correspondientes y genera un artefacto listo para enviar a GitHub.

---

## Principios fundamentales

- **Límites de evidencia** — Versiones, números de PR, resultados de pruebas y comandos de instalación deben tener una fuente; marca los hechos desconocidos como `TODO`
- **Enrutamiento preciso** — Enruta según la intención del usuario; una Feature Request nunca se escribe como un PR ya implementado
- **Limpieza de salida** — Los artefactos se pegan directamente en GitHub — sin preámbulos conversacionales, sin bloques de código exteriores, sin metadatos de prueba
- **Un artefacto, un trabajo** — Nunca mezcles múltiples issues o release notes en una sola salida
- **Prioridad de uso** — Redacta con marcadores `TODO` en lugar de bloquear por falta de información

---

## Estructura del proyecto

```
oh-my-gh-writing/
├── SKILL.md                    # Enrutador de tiempo de ejecución del Agente y reglas compartidas
├── INDEX.md                    # Navegación del repositorio
├── reference/
│   ├── bug-report.md           # Estándar de Bug Report
│   ├── feature-request.md      # Estándar de Feature Request
│   ├── enhancement.md          # Estándar de Enhancement
│   ├── discussion.md           # Estándar de Discussion
│   ├── feature-pr.md           # Estándar de Feature PR
│   ├── bug-fix-pr.md           # Estándar de Bug Fix PR
│   ├── refactor-pr.md          # Estándar de Refactor PR
│   ├── documentation-pr.md     # Estándar de Documentation PR
│   ├── code-review.md          # Estándar de Code Review
│   ├── standard-commit.md      # Estándar de mensajes de commit
│   ├── readme.md               # Estándar de escritura de README
│   ├── contributing.md         # Estándar de escritura de CONTRIBUTING
│   ├── changelog.md            # Estándar de CHANGELOG
│   ├── release-notes.md        # Estándar de Release Notes
│   ├── migration-guide.md      # Estándar de Migration Guide
│   ├── rfc.md                  # Estándar de RFC
│   ├── issue-form-yaml.md      # Estándar de Issue Form YAML
│   ├── pr-template.md          # Estándar de PR Template
│   ├── weapons.md              # Herramientas de Markdown de GitHub
│   ├── emoji-guide.md          # Guía de emojis
│   ├── output-validation.md    # Lista de verificación de validación de salida
│   └── source-catalog.md       # Catálogo de fuentes de referencia
├── CONTRIBUTING.md             # Guía de contribución
├── assets/                     # Activos del proyecto
└── LICENSE                     # MIT
```

---

## Contribuciones

Se aceptan PRs para mejorar reglas de escenarios, fuentes de referencia o validación de salida. Consulta [`CONTRIBUTING.md`](CONTRIBUTING.md).

---

## Licencia

[MIT](LICENSE)
