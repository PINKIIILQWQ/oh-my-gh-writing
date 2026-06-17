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

**oh-my-gh-writing** est un pack de compétences d'écriture GitHub pour les Agents IA. Il achemine les besoins courants d'écriture sur GitHub (Issues, PRs, READMEs, CHANGELOGs, etc.) vers le standard de qualité approprié, garantissant que chaque sortie respecte les conventions de la communauté — prête à être soumise et lisible sans relecture manuelle.

L'ensemble des règles est stocké sous forme de fichiers Markdown dans ce dépôt, sans dépendance externe. Tout Agent IA prenant en charge le chargement de compétences locales peut l'utiliser directement.

## Agents compatibles

oh-my-gh-writing est conçu pour les Agents IA. Tout outil de codage IA prenant en charge le chargement de règles personnalisées, de bases de connaissances ou d'instructions système peut utiliser cette compétence. Les niveaux de prise en charge varient selon la plateforme :

**Direct** — Peut charger `SKILL.md` et son répertoire `reference/` nativement, avec correspondance et routage automatiques des scénarios. Aucune sélection manuelle de scénario requise.

**Adapted** — Ne peut pas charger le format de compétence directement, mais peut référencer les normes d'écriture via des fichiers de règles du projet (par exemple, `.cursorrules`, `copilot-instructions.md`), des instructions personnalisées ou l'indexation de documentation. Le routage automatique est limité — les utilisateurs doivent spécifier le scénario manuellement.

| Icône | Agent | Niveau | Comment utiliser | Documentation |
|-------|-------|--------|-----------------|---------------|
| <img src="https://docs.anthropic.com/favicon.ico" width="14" height="14"> | **Claude Code** | Direct | Ajouter ce dépôt à la liste des compétences ; routage automatique | [Docs Claude Code](https://docs.anthropic.com/en/docs/claude-code) |
| <img src="https://docs.anthropic.com/favicon.ico" width="14" height="14"> | **Claude** (Web/API) | Adapted | Injecter `SKILL.md` et `reference/*.md` dans les instructions système | [Docs Claude API](https://docs.anthropic.com/en/docs) |
| <img src="https://cursor.sh/favicon.ico" width="14" height="14"> | **Cursor** | Adapted | Référencer les règles via `.cursorrules` ou indexer `reference/` avec Docs | [Docs Cursor](https://docs.cursor.com) |
| <img src="https://github.com/favicon.ico" width="14" height="14"> | **GitHub Copilot** | Adapted | Référencer les règles principales dans `.github/copilot-instructions.md` | [Docs Copilot](https://docs.github.com/en/copilot) |
| <img src="https://docs.continue.dev/favicon.ico" width="14" height="14"> | **Continue** | Adapted | Pointer la source docs vers `reference/` ; interroger via `@docs` | [Docs Continue](https://docs.continue.dev) |
| <img src="https://codeium.com/favicon.ico" width="14" height="14"> | **Windsurf** | Adapted | Référencer les règles via `.windsurfrules` ou la configuration AI Rules | [Docs Windsurf](https://docs.codeium.com) |

Les outils d'IA non listés ici peuvent également utiliser cette compétence en mode Adapted s'ils prennent en charge les instructions personnalisées ou le chargement de fichiers de règles. Les normes d'écriture principales (`reference/*.md`) sont en Markdown simple — tout outil capable de lire le Markdown peut les référencer.

## Scénarios

| # | Catégorie | Scénario | Quand l'utiliser |
|---|-----------|----------|------------------|
| 1 | Issue | Bug Report | Signaler un défaut reproductible |
| 2 | Issue | Feature Request | Proposer une nouvelle fonctionnalité ou API |
| 3 | Issue | Enhancement | Améliorer une capacité existante |
| 4 | Issue | Discussion | Discussion communautaire ouverte |
| 5 | PR | Feature PR | Pull Request pour nouvelle fonctionnalité |
| 6 | PR | Bug Fix PR | Pull Request pour correction de bug |
| 7 | PR | Refactor PR | Refactorisation sans changement de comportement |
| 8 | PR | Documentation PR | Changements de documentation uniquement |
| 9 | Review | Code Review | Examiner des modifications de code |
| 10 | Commit | Standard Commit | Rédiger des messages de commit |
| 11 | Docs | README | Page d'accueil du projet |
| 12 | Docs | CONTRIBUTING | Guide de contribution |
| 13 | Docs | CHANGELOG | Historique des versions |
| 14 | Release | Release Notes | Annonce de version |
| 15 | Release | Migration Guide | Guide de mise à niveau |
| 16 | Design | RFC | Proposition de conception |
| 17 | Templates | Issue Form YAML | Formulaires d'Issue GitHub |
| 18 | Templates | PR Template | Modèle de Pull Request |

Chaque scénario dispose d'un fichier de standard d'écriture correspondant dans `reference/`, avec structure standard, champs obligatoires, règles de limites factuelles, sources de référence de haute qualité et liste de contrôle des éléments requis.

## Démarrage rapide

Chargez ce dépôt en tant que compétence dans votre Agent IA :

```bash
# Claude Code — configurez dans .claude/settings.json ou la configuration Claude
# Ou référencez SKILL.md directement comme partie des instructions système de l'Agent
```

Pour toutes les règles de scénarios et le routage, voir [`SKILL.md`](SKILL.md). Index complet dans [`INDEX.md`](INDEX.md).

## Structure du projet

```
oh-my-gh-writing/
├── SKILL.md                  # Point d'entrée de l'Agent et routage
├── INDEX.md                  # Index de navigation complet
├── CONTRIBUTING.md           # Règles de contribution
├── LICENSE                   # Licence MIT
├── .gitignore
├── assets/                   # Ressources du projet
│   └── oh-my-gh-writing-logo.png
└── reference/                # Fichiers de standards de scénarios
    ├── shared-principles.md  # 19 règles de qualité partagées
    ├── readme.md             # Règles d'écriture README
    ├── output-validation.md  # Liste de validation des sorties
    └── source-catalog.md     # Catalogue des sources de référence
```

## Contribuer

Les contributions sont les bienvenues — que ce soit pour corriger des règles de scénarios, améliorer la qualité des sources de référence, ajouter des références d'outils Markdown, ou soumettre des cas d'utilisation.

- Ouvrez d'abord une Issue ou une Discussion pour discuter de vos idées
- Forkez le dépôt et soumettez un PR
- Placez les règles de scénarios dans le `reference/*.md` correspondant, pas dans la couche de routage
- Gardez `SKILL.md` léger et concentré sur le routage

Voir [`CONTRIBUTING.md`](CONTRIBUTING.md) pour les règles détaillées.

## Remerciements

- [GitHub Docs](https://docs.github.com/en) — Modèles d'Issue/PR, syntaxe Markdown et pratiques communautaires
- [Conventional Commits](https://www.conventionalcommits.org/) — Spécification de format de messages de commit
- [Keep a Changelog](https://keepachangelog.com/) — Standard de format CHANGELOG
- [shields.io](https://shields.io) — Service de génération de badges
- [Google Engineering Practices](https://google.github.io/eng-practices/review/) — Guide de Code Review
- Modèles et guides de contribution de projets open source comme Angular, Kubernetes, React, TypeScript, VS Code, Node.js, Tailwind CSS — Références structurelles pour les standards de scénarios
- [ikatyang/emoji-cheat-sheet](https://github.com/ikatyang/emoji-cheat-sheet) — Référence rapide d'émojis
- [carloscuesta/gitmoji](https://github.com/carloscuesta/gitmoji) — Guide d'émojis pour l'intention de commit

## Licence

[MIT](LICENSE) © 2026 oh-my-gh-writing contributors
