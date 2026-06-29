# Target Repository Conventions

## Use When

Read this reference when the user identifies a target repository and the requested GitHub artifact may be governed by that repository's template, contribution policy, release process, or established document structure.

Do not read it for a general draft with no target repository, or for a standard commit or code review unless the user asks to follow repository-specific rules.

## Required Discovery

Before drafting a target-specific artifact:

1. Identify the target repository and active working tree, URL, or both.
2. Inspect only the scenario-relevant files in the local working tree first.
3. If local evidence is absent or clearly stale and a remote repository is known, inspect only the matching remote paths. Do not clone or scan the whole repository merely to find a template.
4. If a user explicitly provides or approves a template cache, apply `template-cache.md` before treating cached files as evidence.
5. If no relevant convention exists, use the matching oh-my-gh-writing standard.

Precedence is: current local working tree, fresh local cache when explicitly available, matching remote repository file, then this skill's scenario standard.

The local working tree is authoritative for an in-progress branch. A remote file is evidence of upstream policy, not permission to overwrite local work.

## Scenario Path Map

| Artifact group | Inspect when relevant |
| --- | --- |
| Issue, Bug Report, Feature Request, Enhancement, Discussion | `.github/ISSUE_TEMPLATE/`, issue config, issue-form YAML, `.github/DISCUSSION_TEMPLATE/`, `CONTRIBUTING.md` |
| Feature PR, Bug Fix PR, Refactor PR, Documentation PR | `.github/pull_request_template.md`, `.github/PULL_REQUEST_TEMPLATE.md`, `PULL_REQUEST_TEMPLATE.md`, `CONTRIBUTING.md` |
| Maintainer Response | Relevant issue/PR/discussion context provided by the user, `.github/ISSUE_TEMPLATE/`, `.github/DISCUSSION_TEMPLATE/`, PR template, `CONTRIBUTING.md`, `SECURITY.md`, support policy, CODEOWNERS only when the reply cites policy or maintainer authority |
| README, CONTRIBUTING, Docs Overhaul | Existing `README.md`, `CONTRIBUTING.md`, adjacent docs, project-specific docs style rules |
| CHANGELOG, Release Notes, Migration Guide, Version Release | `CHANGELOG.md`, `.github/release.yml`, release configuration, prior release notes, migration docs, generated changelog configuration |
| RFC, Proposal to Implementation, Breaking Change Package | RFC or design directories, contribution rules, existing migration and changelog conventions |
| Issue / Discussion Form YAML, PR Template, Project Launch, Contribution Setup | Existing `.github/` forms and templates, `config.yml`, `.github/DISCUSSION_TEMPLATE/`, `CONTRIBUTING.md`, `CODEOWNERS`, support or security guidance when present |

Read the smallest useful set. A PR description does not need all issue forms; a README update does not need release templates.

## Apply Conventions Safely

Treat a repository template as a submission shell, not as a source of target facts.

- Preserve field names, order, required validation, established section names, and demonstrated wording conventions.
- Ask the user for required fields that cannot be inferred safely.
- Omit or leave optional fields empty instead of filling them with invented data or optional `TODO`s.
- Do not carry labels, teams, SIGs, release-note markers, cherry-pick procedures, version lists, test commands, or support policies to another repository.
- Do not turn a local template into a remote modification, publication, issue, PR, tag, or release without an explicit request.

If local and remote templates conflict, use the local file for the current artifact and mention the conflict only when it changes a required field or submission outcome.

## Remote and Cache Boundaries

- Prefer direct repository evidence over model memory.
- Do not make a network request when a matching local file already answers the question.
- Remote inspection must be path-targeted: check only the paths listed in the scenario map or the smallest equivalent path set.
- Do not clone full repositories, traverse broad directory trees, or collect unrelated files just to find a template.
- Do not claim a remote template was read when remote access is unavailable.
- Persistent template caching is opt-in only. Do not create `.github-template-cache/` or any persistent cache automatically.
- When the user explicitly allows persistent template caching, follow `template-cache.md`.
- If a user provides a local template cache, treat it as secondary evidence and state when it is stale, lacks a source revision, or conflicts with local/remote files.

## Submission Notes

Keep template provenance outside the target artifact. Add it only when the artifact is complex, a required field is unresolved, the template source is stale or conflicting, or the user asks for traceability.

```markdown
## Submission Notes

- Template basis: `.github/pull_request_template.md` from the current working tree.
- Blocking: confirm the required release-note field before submitting.
```

## Checklist

- [ ] The target repository and scenario-relevant files were identified.
- [ ] The local working tree was checked before remote files.
- [ ] Only relevant template paths were inspected.
- [ ] Required fields have evidence or a user question.
- [ ] Repository-specific policy was not copied into an unrelated project.
- [ ] Provenance stays outside the target artifact unless requested.
