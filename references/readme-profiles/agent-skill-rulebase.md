# README Profile: Agent Skill / Rulebase

## Use When

Use for repositories whose main deliverable is an Agent Skill, prompt pack, rulebase, custom instruction set, or knowledge-base-backed writing/runtime standard.

## Required Shape

- Short overview: what the skill helps agents do.
- Quick Start: shortest credible install or activation path, with runtime-only caveat if needed.
- Example prompts: 3-6 realistic invocations.
- Applicability: supported agent hosts or adaptation targets, target artifact types, required local files.
- Runtime files: state the minimal files an agent needs.
- Quality boundaries: evidence, local/remote state, and what the skill does not do.

## Quick Start

Start with the simplest tested installer. If it installs the full repository, say so immediately and provide a collapsible runtime-only path. Keep each standalone command copyable on its own line.

## Applicability

Name agent products, skill hosts, custom-instruction targets, rule hosts, and GitHub artifact types. Distinguish native skill loading from adapted rules or knowledge-base use.

## Badges/Visuals

Use version, license, validation, and supported-host badges only when evidenced. Avoid badges that imply package distribution or runtime support that does not exist.

## Avoid

- Calling the project a standalone app or GitHub integration unless it is one.
- Treating evals, cases, screenshots, or scripts as runtime requirements.
- Claiming broad host support without official docs or tested setup.

## Evidence Required

Use `SKILL.md`, runtime references, install docs, validation scripts, official host docs, and user-confirmed host tests.
