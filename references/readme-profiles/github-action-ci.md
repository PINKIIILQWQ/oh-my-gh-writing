# README Profile: GitHub Action / CI Template

## Use When

Use for GitHub Actions, reusable workflows, CI templates, workflow generators, and repository automation intended to run in GitHub Actions.

## Required Shape

- Overview: what the workflow/action automates.
- Quick Start: minimal workflow YAML.
- Inputs/outputs: only documented fields.
- Permissions and secrets: required token scopes and secret names.
- Events/runners: supported triggers and environments.
- Examples: common workflow variants.

## Quick Start

Show a complete minimal `.github/workflows/*.yml` snippet. Keep commands inside the YAML only when required by the action.

## Applicability

State supported GitHub event types, runner OS, required permissions, secrets, repository types, language/tooling assumptions, and whether it is an action or reusable workflow.

## Badges/Visuals

Use workflow status badges only for workflows that exist. Do not add marketplace, downloads, or version badges unless the action is published.

## Avoid

- Broad DevOps claims unrelated to GitHub Actions.
- Missing `permissions:` guidance when tokens are used.
- Inventing secret names or runner support.

## Evidence Required

Use `action.yml`, workflow files, official GitHub Actions docs, examples, tests, and user-confirmed secrets/permissions.
