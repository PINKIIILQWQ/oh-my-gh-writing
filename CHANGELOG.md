# Changelog

All notable changes to this project are documented here.

This project follows the spirit of [Keep a Changelog](https://keepachangelog.com/) and uses explicit evidence boundaries for release facts.

## [Unreleased]

### Changed

- Made the documented runtime install minimal: `SKILL.md`, `INDEX.md`, and `references/` only; moved Agent Skills CLI install to an explicitly full-repository convenience option after testing it.
- Added a concise static Shields.io badge formula and encoding guidance.

### Removed

- Removed optional Codex UI metadata from the repository and runtime installation path.

## [0.1.0] - 2026-06-20

### Added

- Added 18 GitHub artifact standards covering issues, pull requests, reviews, commits, repository docs, releases, migrations, RFCs, Issue Form YAML, and PR templates.
- Added 7 local workflow packs for version releases, project launches, contribution setup, bug-fix workflows, proposal-to-implementation flows, breaking-change packages, and docs overhauls.
- Added a thin `SKILL.md` runtime router with progressive loading from `references/*.md`.
- Added evidence-boundary and output-cleanliness rules for avoiding invented facts, chat prefaces, outer Markdown fences, copied residue, stale test titles, and checked checklist items without evidence.
- Added runtime-only install guidance for supported or folder-compatible skill hosts.
- Added Codex UI metadata in `agents/openai.yaml`.
- Added English and Simplified Chinese public README files.
- Added lightweight eval fixtures, synthetic public case drafts, and validation scripts for repository maintenance.
- Added GitHub Issue Forms, a pull request template, and a validation workflow for public collaboration.

### Changed

- Simplified Quick Start so the first install path is a one-line Agent Skills CLI command, with exact runtime-only installation kept as a manual fallback.
- Added guidance for verified Trendshift and Star History badges without inventing GitHub Trending status.
- Added common and special copy-paste badge recipes with evidence requirements for Shields.io, deployment, social, funding, and dynamic badges.
- Moved the public launch readiness case into the main example section and clarified public case excerpt rules.
- Refined Quick Start to install only runtime and display files: `SKILL.md`, `INDEX.md`, `references/`, `agents/`, and `assets/`.
- Clarified that `evals/`, `cases/`, and `scripts/` are repository maintenance files, not runtime skill dependencies.
- Clarified audit-only behavior for readiness checks so the skill recommends files without creating drafts or modifying repository files by default.
- Simplified public docs to keep only English and Simplified Chinese README pages.

### Removed

- Removed draft example README content from the public root to keep the first release focused on the canonical homepage and runtime files.
