# Project Launch Workflow Pack

## Use When

Use when the user wants to make a repository ready for first public release, open-source launch, public GitHub presentation, or "ready to show" repository setup.

If the user asks only for a README, route to `readme.md`.

If the user asks "what is missing", "what files are needed", "check whether this is ready to publish", or similar readiness-review wording, produce an audit report only. Do not create `README.md`, `CONTRIBUTING.md`, `.github/` files, or `.github-writing/` drafts unless the user explicitly asks to draft, create, write, apply, or update the files.

## Default Output Location

Write local drafts under `.github-writing/project-launch/<version-or-date>/`. If no version/date is known, use `.github-writing/project-launch/TBD/`.

Do not publish the repository, push files, create releases, or open PRs unless explicitly requested.
Do not write root files or `.github/` files during audit-only requests.

## Decision Rule

If the repository has no public contribution policy, default to Public launch pack. If license status is unknown, mark it `TBD` and do not add public-readiness claims.

For audit-only requests, do not select a package or ask the package-selection question. Report existing files, missing recommended files, optional files, and why each recommendation matters.

## Required Package Question

Ask this when the Decision Rule cannot safely choose a package option:

```text
Which project launch package should I prepare?

A. Public launch pack (Recommended): README + CONTRIBUTING + Issue Forms + PR Template + credits/source notes.
B. Minimal launch: README + contribution entry + basic issue/PR templates.
C. Maintainer-ready launch: public launch pack + stricter intake and review guidance.

Add any supplements in the same reply: repository description, official website, docs/demo URL, relevant topics, supported platforms, license status, screenshots/logo, acknowledgement sources, target languages, or contribution policy.
```

## Artifact Selection

| Option | Load |
|--------|------|
| Public launch pack | `readme.md`, `contributing.md`, `issue-form-yaml.md`, `pr-template.md`, `source-catalog.md` when credits are needed |
| Minimal launch | `readme.md`, `issue-form-yaml.md`, `pr-template.md` |
| Maintainer-ready launch | `readme.md`, `contributing.md`, `issue-form-yaml.md`, `pr-template.md`, `code-review.md` |

Read `weapons.md` or `emoji-guide.md` only when visuals, badges, icons, or emoji are needed.

## Evidence Rules

- Applicability scope, install commands, package names, platform support, contribution process, credits, repository description, homepage URL, and topics require evidence.
- Use `TBD` for missing launch facts. Do not invent public-readiness claims.

## Repository About Metadata

For a public launch, include a local `repository-about.md` draft or an audit recommendation covering:

- A concise repository description.
- An official homepage URL only when one exists.
- Two to five relevant GitHub topics.

About metadata is repository configuration, not a README substitute. Do not update remote metadata unless the user explicitly asks. Do not infer a website, package registry, topic, or support claim from the project name alone.

## Suggested File Names

- `README.md`
- `CONTRIBUTING.md`
- `.github/ISSUE_TEMPLATE/bug_report.yml`
- `.github/ISSUE_TEMPLATE/feature_request.yml`
- `.github/pull_request_template.md`
- `repository-about.md`
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
- [ ] Repository About description, homepage, and topics are evidenced or marked `TBD`.
- [ ] Credits or acknowledgements are relationship-specific.
- [ ] No public launch action is performed by default.
- [ ] Audit-only requests do not create files or package drafts.
