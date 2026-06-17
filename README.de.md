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
  <a href="INDEX.md"><img src="https://img.shields.io/badge/Scenarios-18-6a0dad?style=flat" alt="18 Szenarien"></a>
  <a href="SKILL.md"><img src="https://img.shields.io/badge/Format-Agent%20Skill-22AA66?style=flat" alt="Agent Skill"></a>
</p>

**oh-my-gh-writing** ist ein GitHub-Schreibkompetenzpaket für KI-Agenten. Es leitet häufige GitHub-Schreibanforderungen (Issues, PRs, READMEs, CHANGELOGs usw.) an den entsprechenden Qualitätsstandard weiter und stellt sicher, dass jede Ausgabe den Community-Konventionen folgt – einreichbar und lesbar ohne manuelle Nachbearbeitung.

Der gesamte Regelsatz ist als Markdown-Dateien in diesem Repository gespeichert, ohne externe Abhängigkeiten. Jeder KI-Agent, der das Laden lokaler Kompetenzen unterstützt, kann ihn direkt verwenden.

## Unterstützte Agenten

oh-my-gh-writing wurde für KI-Agenten entwickelt. Jedes KI-Coding-Tool, das das Laden benutzerdefinierter Regeln, Wissensdatenbanken oder Systemanweisungen unterstützt, kann diese Kompetenz nutzen. Die Unterstützungsstufen variieren je nach Plattform:

**Direct** — Kann `SKILL.md` und das `reference/`-Verzeichnis nativ laden, mit automatischer Szenarioerkennung und Weiterleitung. Keine manuelle Szenarioauswahl erforderlich.

**Adapted** — Kann das Kompetenzformat nicht direkt laden, kann aber über Projektregeldateien (z. B. `.cursorrules`, `copilot-instructions.md`), benutzerdefinierte Anweisungen oder Dokumentationsindizierung auf die Schreibstandards verweisen. Die automatische Weiterleitung ist eingeschränkt – Benutzer müssen das Szenario manuell angeben.

| Symbol | Agent | Stufe | Verwendung | Dokumentation |
|--------|-------|-------|------------|---------------|
| <img src="https://docs.anthropic.com/favicon.ico" width="14" height="14"> | **Claude Code** | Direct | Dieses Repository zur Skill-Liste hinzufügen; automatische Weiterleitung | [Claude Code Docs](https://docs.anthropic.com/en/docs/claude-code) |
| <img src="https://docs.anthropic.com/favicon.ico" width="14" height="14"> | **Claude** (Web/API) | Adapted | `SKILL.md` und `reference/*.md` in Systemanweisungen einfügen | [Claude API Docs](https://docs.anthropic.com/en/docs) |
| <img src="https://cursor.sh/favicon.ico" width="14" height="14"> | **Cursor** | Adapted | Regeln via `.cursorrules` referenzieren oder `reference/` mit Docs indizieren | [Cursor Docs](https://docs.cursor.com) |
| <img src="https://github.com/favicon.ico" width="14" height="14"> | **GitHub Copilot** | Adapted | Kernregeln in `.github/copilot-instructions.md` referenzieren | [Copilot Docs](https://docs.github.com/en/copilot) |
| <img src="https://docs.continue.dev/favicon.ico" width="14" height="14"> | **Continue** | Adapted | Docs-Quelle auf `reference/` verweisen; via `@docs` abrufen | [Continue Docs](https://docs.continue.dev) |
| <img src="https://codeium.com/favicon.ico" width="14" height="14"> | **Windsurf** | Adapted | Regeln via `.windsurfrules` oder AI Rules-Konfiguration referenzieren | [Windsurf Docs](https://docs.codeium.com) |

Nicht aufgeführte KI-Tools können diese Kompetenz ebenfalls im Adapted-Modus nutzen, sofern sie benutzerdefinierte Anweisungen oder das Laden von Regeldateien unterstützen. Die Kern-Schreibstandards (`reference/*.md`) sind reines Markdown – jedes Tool, das Markdown lesen kann, kann sie referenzieren.

## Szenarien

| # | Kategorie | Szenario | Verwendungszweck |
|---|-----------|----------|------------------|
| 1 | Issue | Bug Report | Ein reproduzierbares Problem melden |
| 2 | Issue | Feature Request | Neue Funktion oder API vorschlagen |
| 3 | Issue | Enhancement | Bestehende Fähigkeit verbessern |
| 4 | Issue | Discussion | Offene Community-Diskussion |
| 5 | PR | Feature PR | Pull Request für neue Funktion |
| 6 | PR | Bug Fix PR | Pull Request zur Fehlerbehebung |
| 7 | PR | Refactor PR | Verhaltenserhaltende Refaktorisierung |
| 8 | PR | Documentation PR | Nur Dokumentationsänderungen |
| 9 | Review | Code Review | Codeänderungen überprüfen |
| 10 | Commit | Standard Commit | Commit-Nachrichten schreiben |
| 11 | Docs | README | Projekteinstiegsseite |
| 12 | Docs | CONTRIBUTING | Mitwirkungsrichtlinien |
| 13 | Docs | CHANGELOG | Versionsänderungsprotokoll |
| 14 | Release | Release Notes | Veröffentlichungsankündigung |
| 15 | Release | Migration Guide | Upgrade-Anleitung |
| 16 | Design | RFC | Designvorschlag |
| 17 | Templates | Issue Form YAML | GitHub Issue-Formulare |
| 18 | Templates | PR Template | Pull-Request-Vorlage |

Jedes Szenario hat eine entsprechende Schreibstandarddatei in `reference/`, mit Standardstruktur, Pflichtfeldern, Faktenbegrenzungsregeln, hochwertigen Referenzquellen und einer Checkliste der erforderlichen Elemente.

## Kurzanleitung

Laden Sie dieses Repository als Kompetenz in Ihren KI-Agenten:

```bash
# Claude Code — konfigurieren Sie es in .claude/settings.json oder der Claude-Konfiguration
# Oder referenzieren Sie SKILL.md direkt als Teil der Systemanweisungen des Agenten
```

Alle Szenarioregeln und das Routing finden Sie in [`SKILL.md`](SKILL.md). Vollständiger Index unter [`INDEX.md`](INDEX.md).

## Projektstruktur

```
oh-my-gh-writing/
├── SKILL.md                  # Agenteneinstiegspunkt und Szenario-Routing
├── INDEX.md                  # Vollständiger Navigationsindex
├── CONTRIBUTING.md           # Mitwirkungsregeln
├── LICENSE                   # MIT-Lizenz
├── .gitignore
├── assets/                   # Projektmaterialien
│   └── oh-my-gh-writing-logo.png
└── reference/                # Szenario-Standarddateien
    ├── shared-principles.md  # 19 gemeinsame Qualitätsregeln
    ├── readme.md             # README-Schreibregeln
    ├── output-validation.md  # Ausgabevalidierungs-Checkliste
    └── source-catalog.md     # Referenzquellenkatalog
```

## Mitwirken

Beiträge sind willkommen – sei es zur Korrektur von Szenarioregeln, zur Verbesserung der Referenzquellenqualität, zum Hinzufügen von Markdown-Tool-Referenzen oder zum Einreichen von Anwendungsfällen.

- Eröffnen Sie zuerst ein Issue oder eine Discussion, um Ihre Ideen zu besprechen
- Forken Sie das Repository und reichen Sie einen PR ein
- Platzieren Sie Szenarioregeln in der entsprechenden `reference/*.md`, nicht in der Routing-Ebene
- Halten Sie `SKILL.md` schlank und auf das Routing fokussiert

Ausführliche Regeln finden Sie in [`CONTRIBUTING.md`](CONTRIBUTING.md).

## Danksagungen

- [GitHub Docs](https://docs.github.com/en) — Issue/PR-Vorlagen, Markdown-Syntax und Community-Praktiken
- [Conventional Commits](https://www.conventionalcommits.org/) — Commit-Nachrichten-Formatspezifikation
- [Keep a Changelog](https://keepachangelog.com/) — CHANGELOG-Formatstandard
- [shields.io](https://shields.io) — Badge-Generierungsdienst
- [Google Engineering Practices](https://google.github.io/eng-practices/review/) — Code-Review-Leitfaden
- Vorlagen und Mitwirkungsrichtlinien von Open-Source-Projekten wie Angular, Kubernetes, React, TypeScript, VS Code, Node.js, Tailwind CSS — Strukturelle Referenzen für Szenariostandards
- [ikatyang/emoji-cheat-sheet](https://github.com/ikatyang/emoji-cheat-sheet) — Emoji-Nachschlagereferenz
- [carloscuesta/gitmoji](https://github.com/carloscuesta/gitmoji) — Leitfaden für Commit-Absichts-Emojis

## Lizenz

[MIT](LICENSE) © 2026 oh-my-gh-writing contributors
