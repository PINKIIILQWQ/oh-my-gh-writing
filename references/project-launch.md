# Project Launch Workflow Pack

## Use When

Use when the user wants to make a repository ready for first public release, open-source launch, public GitHub presentation, or "ready to show" repository setup.

If the user asks only for a README, route to `readme.md`.

## Default Output Location

Write local drafts under `.github-writing/project-launch/<version-or-date>/`. If no version/date is known, use `.github-writing/project-launch/TBD/`.

Do not publish the repository, push files, create releases, or open PRs unless explicitly requested.

## Decision Rule

If the repository has no public contribution policy, default to Public launch pack. If license status is unknown, mark it `TBD` and do not add public-readiness claims.

## Required Package Question

Ask this before drafting unless the user already chose:

```text
Which project launch package should I prepare?

A. Public launch pack (Recommended): README + CONTRIBUTING + Issue Forms + PR Template + credits/source notes.
B. Minimal launch: README + contribution entry + basic issue/PR templates.
C. Maintainer-ready launch: public launch pack + stricter intake and review guidance.

Add any supplements in the same reply: official website, docs/demo URL, supported platforms, license status, screenshots/logo, acknowledgement sources, target languages, or contribution policy.
```

## Artifact Selection

| Option | Load |
|--------|------|
| Public launch pack | `readme.md`, `contributing.md`, `issue-form-yaml.md`, `pr-template.md`, `source-catalog.md` when credits are needed |
| Minimal launch | `readme.md`, `issue-form-yaml.md`, `pr-template.md` |
| Maintainer-ready launch | `readme.md`, `contributing.md`, `issue-form-yaml.md`, `pr-template.md`, `code-review.md` |

Read `weapons.md` or `emoji-guide.md` only when visuals, badges, icons, or emoji are needed.

## Evidence Rules

- Applicability scope, install commands, package names, platform support, contribution process, and credits require evidence.
- Use `TBD` for missing launch facts. Do not invent public-readiness claims.

## Suggested File Names

- `README.md`
- `CONTRIBUTING.md`
- `.github/ISSUE_TEMPLATE/bug_report.yml`
- `.github/ISSUE_TEMPLATE/feature_request.yml`
- `.github/pull_request_template.md`
- `package-manifest.md`

## Package Manifest

Every workflow package should include `package-manifest.md` with:

- Selected package option.
- Generated files and intended target paths.
- Assumptions and evidence sources.
- `TODO` / `TBD` fields.
- Files safe to write directly.
- Files requiring maintainer confirmation before use.

## Checklist

- [ ] Package option is selected.
- [ ] README includes project applicability scope.
- [ ] Credits or acknowledgements are relationship-specific.
- [ ] No public launch action is performed by default.
