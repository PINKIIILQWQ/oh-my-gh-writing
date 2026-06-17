<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/oh-my-gh-writing-logo.png">
  <img alt="oh-my-gh-writing" src="assets/oh-my-gh-writing-logo.png" width="160">
</picture>

# oh-my-gh-writing

[![License](https://img.shields.io/github/license/PINKIIILQWQ/oh-my-gh-writing?label=License&color=blue)](LICENSE)
[![Scenarios](https://img.shields.io/badge/Scenarios-18-6a0dad)](#-index-des-scénarios)
[![Agent](https://img.shields.io/badge/Agent-Claude%20Code-8A2BE2)](https://claude.ai/code)
[![PRs](https://img.shields.io/badge/PRs-Welcome-brightgreen)](CONTRIBUTING.md)
[![GitHub last commit](https://img.shields.io/github/last-commit/PINKIIILQWQ/oh-my-gh-writing?label=Updated)](https://github.com/PINKIIILQWQ/oh-my-gh-writing/commits/main)

**oh-my-gh-writing** est un système de normes rédactionnelles GitHub conçu pour les Agents IA. Ce n'est pas un générateur de README ni une application autonome, mais un pack de compétences portable. Lorsqu'un Agent le charge, il achemine automatiquement la sortie vers le scénario approprié (Issue, PR, Review, Commit, README, CHANGELOG, RFC, etc.) avec une qualité constante, des preuves vérifiables et un format prêt à soumettre.

---

## Index des scénarios

| # | Catégorie | Scénarios | Fichier standard |
|---|-----------|-----------|------------------|
| 1–4 | Issue | Bug Report / Feature Request / Enhancement / Discussion | `reference/bug-report.md` etc. |
| 5–8 | PR | Feature PR / Bug Fix PR / Refactor PR / Documentation PR | `reference/feature-pr.md` etc. |
| 9–10 | Review & Commit | Code Review / Standard Commit | `reference/code-review.md` etc. |
| 11–13 | Docs | README / CONTRIBUTING / CHANGELOG | `reference/readme.md` etc. |
| 14–15 | Release | Release Notes / Migration Guide | `reference/release-notes.md` etc. |
| 16 | Design | RFC | `reference/rfc.md` |
| 17–18 | Templates | Issue Form YAML / PR Template | `reference/issue-form-yaml.md` etc. |

Les règles d'acheminement complètes se trouvent dans [`SKILL.md`](SKILL.md).

---

## Installation

### Claude Code (chargement direct)

```bash
gh repo clone PINKIIILQWQ/oh-my-gh-writing ~/.claude/skills/oh-my-gh-writing
```

Utilisez ensuite `/oh-my-gh-writing` dans Claude Code.

### Autres Agents IA

| Agent | Niveau de support | Action |
|-------|-------------------|--------|
| Cline / Roo Code | Import adapté | Copiez le contenu de `SKILL.md` dans les instructions personnalisées du projet ; chargez le fichier `reference/*.md` correspondant si nécessaire |

> Cette compétence est conçue nativement pour Claude Code. Les autres agents nécessitent une adaptation à leur propre système de règles.

---

## Démarrage rapide

```text
/oh-my-gh-writing Écris un Bug Report
/oh-my-gh-writing Écris une description de PR pour ces changements
/oh-my-gh-writing Review les changements de cette PR
/oh-my-gh-writing Écris une entrée de CHANGELOG
```

L'agent achemine vers le bon scénario, charge les règles `reference/*.md` correspondantes et produit un artefact prêt à être soumis sur GitHub.

---

## Principes fondamentaux

- **Limites des preuves** — Les numéros de version, numéros de PR, résultats de tests et commandes d'installation doivent avoir une source ; marquez les faits inconnus comme `TODO`
- **Acheminement précis** — Acheminez selon l'intention de l'utilisateur ; une Feature Request n'est jamais rédigée comme une PR déjà livrée
- **Propreté de sortie** — Les artefacts se collent directement dans GitHub — pas de préambule conversationnel, pas de bloc de code externe, pas de métadonnées de test
- **Un artefact, un travail** — Ne mélangez jamais plusieurs issues ou release notes dans une seule sortie
- **Utilisable d'abord** — Rédigez avec des espaces réservés `TODO` plutôt que de bloquer sur des informations manquantes

---

## Structure du projet

```
oh-my-gh-writing/
├── SKILL.md                    # Routeur d'exécution de l'Agent et règles partagées
├── INDEX.md                    # Navigation du dépôt
├── reference/
│   ├── bug-report.md           # Standard Bug Report
│   ├── feature-request.md      # Standard Feature Request
│   ├── enhancement.md          # Standard Enhancement
│   ├── discussion.md           # Standard Discussion
│   ├── feature-pr.md           # Standard Feature PR
│   ├── bug-fix-pr.md           # Standard Bug Fix PR
│   ├── refactor-pr.md          # Standard Refactor PR
│   ├── documentation-pr.md     # Standard Documentation PR
│   ├── code-review.md          # Standard Code Review
│   ├── standard-commit.md      # Standard de message de commit
│   ├── readme.md               # Standard de rédaction README
│   ├── contributing.md         # Standard de rédaction CONTRIBUTING
│   ├── changelog.md            # Standard CHANGELOG
│   ├── release-notes.md        # Standard Release Notes
│   ├── migration-guide.md      # Standard Migration Guide
│   ├── rfc.md                  # Standard RFC
│   ├── issue-form-yaml.md      # Standard Issue Form YAML
│   ├── pr-template.md          # Standard PR Template
│   ├── weapons.md              # Outils Markdown GitHub
│   ├── emoji-guide.md          # Guide des émojis
│   ├── output-validation.md    # Checklist de validation de sortie
│   └── source-catalog.md       # Catalogue des sources de référence
├── CONTRIBUTING.md             # Guide de contribution
├── assets/                     # Ressources du projet
└── LICENSE                     # MIT
```

---

## Contribution

Les PRs sont les bienvenues pour améliorer les règles de scénarios, les sources de référence ou la validation de sortie. Voir [`CONTRIBUTING.md`](CONTRIBUTING.md).

---

## Licence

[MIT](LICENSE)
