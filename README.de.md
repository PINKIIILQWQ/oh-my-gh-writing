<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/oh-my-gh-writing-logo.png">
  <img alt="oh-my-gh-writing" src="assets/oh-my-gh-writing-logo.png" width="160">
</picture>

# oh-my-gh-writing

[![License](https://img.shields.io/github/license/PINKIIILQWQ/oh-my-gh-writing?label=License&color=blue)](LICENSE)
[![Scenarios](https://img.shields.io/badge/Scenarios-18-6a0dad)](#-szenarienübersicht)
[![Agent](https://img.shields.io/badge/Agent-Claude%20Code-8A2BE2)](https://claude.ai/code)
[![PRs](https://img.shields.io/badge/PRs-Welcome-brightgreen)](CONTRIBUTING.md)
[![GitHub last commit](https://img.shields.io/github/last-commit/PINKIIILQWQ/oh-my-gh-writing?label=Updated)](https://github.com/PINKIIILQWQ/oh-my-gh-writing/commits/main)

**oh-my-gh-writing** ist ein GitHub-Schreibregelsystem für KI-Agenten. Es ist kein README-Generator oder eine eigenständige App, sondern ein portables Skill-Paket. Sobald ein Agent es lädt, leitet er die Ausgabe automatisch zum richtigen Szenario (Issue, PR, Review, Commit, README, CHANGELOG, RFC usw.) mit konsistenter Qualität, evidenzbasierten Grenzen und einreichefertigem Format.

---

## Szenarienübersicht

| # | Kategorie | Szenarien | Standard-Datei |
|---|-----------|-----------|----------------|
| 1–4 | Issue | Bug Report / Feature Request / Enhancement / Discussion | `reference/bug-report.md` usw. |
| 5–8 | PR | Feature PR / Bug Fix PR / Refactor PR / Documentation PR | `reference/feature-pr.md` usw. |
| 9–10 | Review & Commit | Code Review / Standard Commit | `reference/code-review.md` usw. |
| 11–13 | Docs | README / CONTRIBUTING / CHANGELOG | `reference/readme.md` usw. |
| 14–15 | Release | Release Notes / Migration Guide | `reference/release-notes.md` usw. |
| 16 | Design | RFC | `reference/rfc.md` |
| 17–18 | Templates | Issue Form YAML / PR Template | `reference/issue-form-yaml.md` usw. |

Vollständige Routing-Regeln in [`SKILL.md`](SKILL.md).

---

## Installation

### Claude Code (direktes Laden)

```bash
gh repo clone PINKIIILQWQ/oh-my-gh-writing ~/.claude/skills/oh-my-gh-writing
```

Dann verwenden Sie `/oh-my-gh-writing` in Claude Code.

### Andere KI-Agenten

| Agent | Support-Level | Aktion |
|-------|---------------|--------|
| Cline / Roo Code | Adaptierter Import | Kopieren Sie den Inhalt von `SKILL.md` in die benutzerdefinierten Anweisungen des Projekts; laden Sie die entsprechende `reference/*.md` bei Bedarf |

> Dieser Skill ist nativ für Claude Code entwickelt. Andere Agenten müssen an ihr eigenes Regelsystem angepasst werden.

---

## Schnellstart

```text
/oh-my-gh-writing Schreibe einen Bug Report
/oh-my-gh-writing Schreibe eine PR-Beschreibung für diese Änderungen
/oh-my-gh-writing Review die Änderungen in diesem PR
/oh-my-gh-writing Schreibe einen CHANGELOG-Eintrag
```

Der Agent leitet zum richtigen Szenario weiter, lädt die entsprechenden `reference/*.md`-Regeln und erstellt ein einreichefertiges GitHub-Artefakt.

---

## Kernprinzipien

- **Evidenzgrenzen** — Versionsnummern, PR-Nummern, Testergebnisse und Installationsbefehle müssen eine Quelle haben; markieren Sie unbekannte Fakten als `TODO`
- **Präzises Routing** — Leiten Sie basierend auf der Benutzerabsicht weiter; eine Feature Request wird niemals als bereits ausgelieferter PR geschrieben
- **Saubere Ausgabe** — Artefakte können direkt in GitHub eingefügt werden — ohne einleitende Konversation, ohne äußere Codeblöcke, ohne Testmetadaten
- **Ein Artefakt, eine Aufgabe** — Vermischen Sie niemals mehrere Issues oder Release Notes in einer Ausgabe
- **Nutzbarkeit zuerst** — Erstellen Sie Entwürfe mit `TODO`-Platzhaltern, anstatt bei fehlenden Informationen zu blockieren

---

## Projektstruktur

```
oh-my-gh-writing/
├── SKILL.md                    # Agent-Laufzeitrouter und gemeinsame Regeln
├── INDEX.md                    # Repository-Navigation
├── reference/
│   ├── bug-report.md           # Bug Report Standard
│   ├── feature-request.md      # Feature Request Standard
│   ├── enhancement.md          # Enhancement Standard
│   ├── discussion.md           # Discussion Standard
│   ├── feature-pr.md           # Feature PR Standard
│   ├── bug-fix-pr.md           # Bug Fix PR Standard
│   ├── refactor-pr.md          # Refactor PR Standard
│   ├── documentation-pr.md     # Documentation PR Standard
│   ├── code-review.md          # Code Review Standard
│   ├── standard-commit.md      # Commit-Nachrichten Standard
│   ├── readme.md               # README-Schreibstandard
│   ├── contributing.md         # CONTRIBUTING-Schreibstandard
│   ├── changelog.md            # CHANGELOG Standard
│   ├── release-notes.md        # Release Notes Standard
│   ├── migration-guide.md      # Migration Guide Standard
│   ├── rfc.md                  # RFC Standard
│   ├── issue-form-yaml.md      # Issue Form YAML Standard
│   ├── pr-template.md          # PR Template Standard
│   ├── weapons.md              # GitHub Markdown-Werkzeuge
│   ├── emoji-guide.md          # Emoji-Leitfaden
│   ├── output-validation.md    # Ausgabevalidierungs-Checkliste
│   └── source-catalog.md       # Referenzquellen-Katalog
├── CONTRIBUTING.md             # Beitragsanleitung
├── assets/                     # Projekt-Assets
└── LICENSE                     # MIT
```

---

## Beitragen

PRs zur Verbesserung von Szenarioregeln, Referenzquellen oder Ausgabevalidierung sind willkommen. Siehe [`CONTRIBUTING.md`](CONTRIBUTING.md).

---

## Lizenz

[MIT](LICENSE)
