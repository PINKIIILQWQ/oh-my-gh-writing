<p align="center">
  <img src="assets/oh-my-gh-writing-logo.png" alt="logo oh-my-gh-writing" width="200">
</p>

<h1 align="center">oh-my-gh-writing</h1>

<p align="center">
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-MIT-0f766e?style=flat" alt="Licence MIT"></a>
  <a href="SKILL.md"><img src="https://img.shields.io/badge/Status-Release%20Candidate-2563eb?style=flat" alt="Release Candidate"></a>
  <a href="INDEX.md"><img src="https://img.shields.io/badge/Artifacts-18-6a0dad?style=flat" alt="18 standards d'artefacts"></a>
  <a href="INDEX.md"><img src="https://img.shields.io/badge/Workflows-7-0f766e?style=flat" alt="7 packs de workflow"></a>
  <a href="SKILL.md"><img src="https://img.shields.io/badge/Format-SKILL.md-22AA66?style=flat" alt="SKILL.md"></a>
</p>

<p align="center">
  <a href="README.md">简体中文</a> · <a href="README.en.md">English</a> · <a href="README.es.md">Español</a> · <a href="README.hi.md">हिन्दी</a> · <a href="README.ar.md">العربية</a> · Français · <a href="README.pt.md">Português</a> · <a href="README.ja.md">日本語</a> · <a href="README.ko.md">한국어</a>
</p>

**oh-my-gh-writing** est un pack de compétence d’écriture GitHub pour AI Agents. Il route les tâches courantes, Issues, PRs, Reviews, Commits, README, CHANGELOG, Release Notes, Migration Guides, RFCs, Issue Forms et PR Templates, vers des standards adaptés à chaque scénario afin de produire des brouillons Markdown ou YAML clairs, structurés et encadrés par des limites de preuve.

Ce n’est ni un générateur de README ni un service d’intégration GitHub. C’est une base de règles Markdown portable : les outils compatibles Agent Skills peuvent la charger directement ; les autres peuvent adapter `SKILL.md` et les fichiers `reference/*.md` nécessaires en règles, instructions ou base de connaissance.

## Pourquoi oh-my-gh-writing ?

Bien écrire pour GitHub ne consiste pas seulement à remplir du Markdown. Le plus difficile est d’identifier le bon scénario, de savoir quels faits doivent être vérifiés, ce qui ne doit pas être inventé, et si l’artifact final peut être collé dans une Issue, une PR, une Review ou un README sans nettoyage.

- **18 standards d’artefacts GitHub + 7 packs de workflow** : Issues, PRs, Code Review, Commit, README, CHANGELOG, Release Notes, Migration Guide, RFC, Issue Form, PR Template et packs composés.
- **Router avant d’écrire** : distingue Feature Request, Enhancement, Discussion, Feature PR, Bug Fix PR et Refactor PR.
- **Chargement progressif des références** : `SKILL.md` reste léger ; les règles détaillées sont chargées uniquement si nécessaire.
- **Limites de preuve** : versions, commandes, CI, compatibilité, releases et numéros d’issues/PRs ne sont pas inventés.
- **Artifacts plus propres** : évite les préfaces conversationnelles, les fences Markdown externes, les titres de test et les résidus de copie.
- **Références open source réelles** : GitHub Docs, Conventional Commits, Keep a Changelog, React, Kubernetes, TypeScript, Node.js, Tailwind CSS, etc.

## Modes d’utilisation

**Comme skill** : placez ce dépôt dans un emplacement où l’agent peut charger un dossier contenant `SKILL.md` et lire `reference/` à la demande.

**Comme règles** : si votre outil ne consomme pas ce format, adaptez la table de routage de `SKILL.md` et les fichiers `reference/*.md` pertinents en règles de projet, instructions personnalisées ou base de connaissance.

| Icône | Agent / Tool | Configuration recommandée | Notes / Docs |
|------|--------------|---------------------------|--------------|
| <a href="https://developers.openai.com/codex/skills"><img src="https://www.google.com/s2/favicons?domain=openai.com&sz=64" width="24" height="24" alt="OpenAI"></a> | [Codex](https://developers.openai.com/codex/skills) | Cloner dans `$HOME/.agents/skills/oh-my-gh-writing` ou `.agents/skills/oh-my-gh-writing` | [Codex Agent Skills](https://developers.openai.com/codex/skills) |
| <a href="https://code.claude.com/docs/en/skills"><img src="https://www.google.com/s2/favicons?domain=claude.ai&sz=64" width="24" height="24" alt="Claude"></a> | [Claude Code](https://code.claude.com/docs/en/skills) | Cloner ou créer un symlink vers `~/.claude/skills/oh-my-gh-writing` ou `.claude/skills/oh-my-gh-writing` | [Claude Code Skills](https://code.claude.com/docs/en/skills) |
| <a href="https://geminicli.com/docs/cli/skills/"><img src="https://www.google.com/s2/favicons?domain=geminicli.com&sz=64" width="24" height="24" alt="Gemini CLI"></a> | [Gemini CLI](https://geminicli.com/docs/cli/skills/) | La documentation liste `~/.gemini/skills/`, `~/.agents/skills/` et `gemini skills install` | Vérifiez la [documentation officielle](https://geminicli.com/docs/cli/skills/) actuelle |
| <a href="https://antigravity.google/"><img src="https://www.google.com/s2/favicons?domain=antigravity.google&sz=64" width="24" height="24" alt="Antigravity"></a> | [Antigravity CLI](https://antigravity.google/) | Vérifiez dans la documentation actuelle le chemin d’intégration skill / rules | [Google Antigravity](https://antigravity.google/) |
| <a href="https://hermes-agent.nousresearch.com/docs/guides/work-with-skills"><img src="https://www.google.com/s2/favicons?domain=hermes-agent.nousresearch.com&sz=64" width="24" height="24" alt="Hermes"></a> | [Hermes](https://hermes-agent.nousresearch.com/docs/guides/work-with-skills) | Placer sous `~/.hermes/skills/<category>/oh-my-gh-writing` | L’installation HTTP monofichier convient seulement à `SKILL.md`; conservez `reference/`. Voir [Hermes Skills](https://hermes-agent.nousresearch.com/docs/guides/work-with-skills) |
| <a href="https://cursor.com/docs"><img src="https://www.google.com/s2/favicons?domain=cursor.com&sz=64" width="24" height="24" alt="Cursor"></a> | [Cursor](https://cursor.com/docs) | Adapter le routeur et les règles nécessaires en règles de projet ou base de connaissance | Vérifiez [Cursor Docs](https://cursor.com/docs) |
| <a href="https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/add-custom-instructions/add-repository-instructions"><img src="https://www.google.com/s2/favicons?domain=github.com&sz=64" width="24" height="24" alt="GitHub"></a> | [GitHub Copilot](https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/add-custom-instructions/add-repository-instructions) | Adapter vers `.github/copilot-instructions.md`, `.github/instructions/*.instructions.md` ou une structure de skill Copilot | [Copilot Custom Instructions](https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/add-custom-instructions/add-repository-instructions) |
| <a href="https://docs.continue.dev/customize/rules"><img src="https://www.google.com/s2/favicons?domain=continue.dev&sz=64" width="24" height="24" alt="Continue"></a> | [Continue](https://docs.continue.dev/customize/rules) | Adapter vers `.continue/rules/*.md` ; une règle par scénario est plus stable | [Continue Rules](https://docs.continue.dev/customize/rules) |
| <a href="https://docs.windsurf.com"><img src="https://www.google.com/s2/favicons?domain=windsurf.com&sz=64" width="24" height="24" alt="Windsurf"></a> | [Windsurf / Devin Desktop](https://docs.windsurf.com) | Les docs actuelles mentionnent memories et rules pour la personnalisation | Confirmez le chemin actuel dans [Windsurf / Devin Docs](https://docs.windsurf.com) |

## Démarrage rapide

```bash
# Codex
git clone https://github.com/PINKIIILQWQ/oh-my-gh-writing.git "$HOME/.agents/skills/oh-my-gh-writing"

# Claude Code
git clone https://github.com/PINKIIILQWQ/oh-my-gh-writing.git "$HOME/.claude/skills/oh-my-gh-writing"
```

Symlinks pour le développement local :

```bash
# Codex / Gemini CLI
ln -sfn "$PWD" "$HOME/.agents/skills/oh-my-gh-writing"

# Claude Code
ln -sfn "$PWD" "$HOME/.claude/skills/oh-my-gh-writing"
```

Exemples :

```text
Rédige un README pour ce dépôt.
Transforme ce bug report en GitHub Issue.
Rédige une description de PR à partir du diff actuel.
Relis cette PR et classe les remarques en blocking / major / minor / nit.
```

## Scénarios

| # | Catégorie | Scénario | Quand l’utiliser |
|---|-----------|----------|------------------|
| 1 | Issue | Bug Report | Signaler un défaut reproductible |
| 2 | Issue | Feature Request | Proposer une nouvelle fonctionnalité ou API |
| 3 | Issue | Enhancement | Améliorer un comportement existant |
| 4 | Issue | Discussion | Lancer une discussion communautaire |
| 5 | PR | Feature PR | Décrire une PR de nouvelle fonctionnalité |
| 6 | PR | Bug Fix PR | Décrire une PR de correction |
| 7 | PR | Refactor PR | Décrire un refactoring sans changement de comportement |
| 8 | PR | Documentation PR | Décrire des changements de documentation |
| 9 | Review | Code Review | Relire des changements de code |
| 10 | Commit | Standard Commit | Rédiger des messages de commit |
| 11 | Docs | README | Créer ou réviser la page d’accueil du projet |
| 12 | Docs | CONTRIBUTING | Créer un guide de contribution |
| 13 | Docs | CHANGELOG | Rédiger l’historique des versions |
| 14 | Release | Release Notes | Rédiger une annonce de release |
| 15 | Release | Migration Guide | Expliquer les étapes de migration |
| 16 | Design | RFC | Proposer un design |
| 17 | Templates | Issue Form YAML | Créer des GitHub Issue Forms |
| 18 | Templates | PR Template | Créer des Pull Request templates |

Chaque scénario possède un fichier standard dans `reference/`. La navigation complète se trouve dans [`INDEX.md`](INDEX.md).

## Structure

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

## Contribuer

Les contributions aux règles de scénario, sources de référence, règles de validation et petits outils Markdown sont bienvenues. Pour les exemples ou cas de test, décrivez d’abord la source, le scénario, l’objectif de test et les limites de licence ou de confidentialité dans une Issue ou une Discussion.

Gardez `SKILL.md` léger et placez les détails dans le fichier `reference/*.md` correspondant. Consultez [`CONTRIBUTING.md`](CONTRIBUTING.md).

## Sources

Les règles s’appuient sur [GitHub Docs](https://docs.github.com/en), [Conventional Commits](https://www.conventionalcommits.org/), [Keep a Changelog](https://keepachangelog.com/), [Google Engineering Practices](https://google.github.io/eng-practices/review/) et des projets matures comme Angular, Kubernetes, React, TypeScript, VS Code, Node.js et Tailwind CSS. Voir [`reference/source-catalog.md`](reference/source-catalog.md).

## Licence

[MIT](LICENSE) © 2026 oh-my-gh-writing contributors
