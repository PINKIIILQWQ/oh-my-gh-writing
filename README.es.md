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

**oh-my-gh-writing** es un paquete de habilidades de escritura para GitHub orientado a Agentes de IA. Enruta las necesidades comunes de escritura en GitHub (Issues, PRs, READMEs, CHANGELOGs, etc.) al estándar de calidad correspondiente, asegurando que cada salida siga las convenciones de la comunidad — lista para enviar y legible sin pulido manual.

El conjunto completo de reglas se almacena como archivos Markdown en este repositorio, sin dependencias externas. Cualquier Agente de IA que admita la carga de habilidades locales puede usarlo directamente.

## Escenarios

| # | Categoría | Escenario | Cuándo usarlo |
|---|-----------|-----------|---------------|
| 1 | Issue | Bug Report | Reportar un defecto reproducible |
| 2 | Issue | Feature Request | Proponer una nueva función o API |
| 3 | Issue | Enhancement | Mejorar una capacidad existente |
| 4 | Issue | Discussion | Discusión comunitaria abierta |
| 5 | PR | Feature PR | Pull Request de nueva función |
| 6 | PR | Bug Fix PR | Pull Request de corrección de error |
| 7 | PR | Refactor PR | Refactorización sin cambio de comportamiento |
| 8 | PR | Documentation PR | Cambios solo de documentación |
| 9 | Review | Code Review | Revisar cambios de código |
| 10 | Commit | Standard Commit | Escribir mensajes de commit |
| 11 | Docs | README | Documentación de inicio del proyecto |
| 12 | Docs | CONTRIBUTING | Guía de contribución |
| 13 | Docs | CHANGELOG | Registro de cambios de versión |
| 14 | Release | Release Notes | Anuncio de lanzamiento |
| 15 | Release | Migration Guide | Guía de actualización |
| 16 | Design | RFC | Propuesta de diseño |
| 17 | Templates | Issue Form YAML | Formularios de Issue en GitHub |
| 18 | Templates | PR Template | Plantilla de Pull Request |

Cada escenario tiene un archivo de estándar de escritura correspondiente en `reference/`, con estructura estándar, campos obligatorios, reglas de límite de evidencia, fuentes de referencia de alta calidad y una lista de verificación de elementos requeridos.

## Inicio rápido

Cargue este repositorio como una habilidad en su Agente de IA:

```bash
# Claude Code — configure en .claude/settings.json o la configuración de Claude
# O referencie SKILL.md directamente como parte de las instrucciones del sistema del Agente
```

Para todas las reglas de escenarios y enrutamiento, vea [`SKILL.md`](SKILL.md). Índice completo en [`INDEX.md`](INDEX.md).

## Estructura del proyecto

```
oh-my-gh-writing/
├── SKILL.md                  # Punto de entrada del Agente y enrutamiento
├── INDEX.md                  # Índice de navegación completo
├── CONTRIBUTING.md           # Reglas de contribución
├── LICENSE                   # Licencia MIT
├── .gitignore
├── assets/                   # Recursos del proyecto
│   └── oh-my-gh-writing-logo.png
└── reference/                # Archivos de estándares de escenarios
    ├── shared-principles.md  # 19 reglas de calidad compartidas
    ├── readme.md             # Reglas de escritura de README
    ├── output-validation.md  # Lista de verificación de validación de salida
    └── source-catalog.md     # Catálogo de fuentes de referencia
```

## Contribuir

Las contribuciones son bienvenidas — ya sea corregir reglas de escenarios, mejorar la calidad de las fuentes de referencia, añadir referencias de herramientas Markdown, o enviar casos de uso.

- Abra un Issue o Discussion para discutir sus ideas primero
- Haga un Fork del repositorio y envíe un PR
- Ponga las reglas de escenarios en el `reference/*.md` correspondiente, no en la capa de enrutamiento
- Mantenga `SKILL.md` ligero y centrado en el enrutamiento

Vea [`CONTRIBUTING.md`](CONTRIBUTING.md) para las reglas detalladas.

## Agradecimientos

- [GitHub Docs](https://docs.github.com/en) — Plantillas de Issue/PR, sintaxis Markdown y prácticas comunitarias
- [Conventional Commits](https://www.conventionalcommits.org/) — Especificación de formato de mensajes de commit
- [Keep a Changelog](https://keepachangelog.com/) — Estándar de formato CHANGELOG
- [shields.io](https://shields.io) — Servicio de generación de badges
- [Google Engineering Practices](https://google.github.io/eng-practices/review/) — Guía de Code Review
- Plantillas y guías de contribución de proyectos de código abierto como Angular, Kubernetes, React, TypeScript, VS Code, Node.js, Tailwind CSS — Referencias estructurales para estándares de escenarios
- [ikatyang/emoji-cheat-sheet](https://github.com/ikatyang/emoji-cheat-sheet) — Referencia rápida de emojis
- [carloscuesta/gitmoji](https://github.com/carloscuesta/gitmoji) — Guía de emojis para intención de commits

## Licencia

[MIT](LICENSE) © 2026 oh-my-gh-writing contributors
