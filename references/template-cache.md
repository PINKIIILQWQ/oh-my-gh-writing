# Template Cache Protocol

## Use When

Use this protocol only when the user explicitly provides, asks for, or approves persistent caching of target-repository GitHub templates.

Do not use it for ordinary writing requests. Do not create a cache automatically.

## Default Boundary

Persistent template caching is disabled by default.

- Prefer current local repository files.
- Use targeted remote reads only when local evidence is missing or stale.
- Cache nothing for private repositories unless the user explicitly confirms persistent storage for that repository.
- Never store credentials, cookies, API tokens, session files, issue contents, PR contents, or arbitrary repository files.

## Cache Location

Use the platform cache directory:

```text
$XDG_CACHE_HOME/oh-my-gh-writing/templates/<host>/<owner>/<repo>/
```

If `XDG_CACHE_HOME` is unavailable, use:

```text
~/.cache/oh-my-gh-writing/templates/<host>/<owner>/<repo>/
```

Do not write caches inside the target repository, the skill runtime directory, `.github-writing/`, or tracked public repository files.

## Allowed Cached Files

Cache only scenario-relevant template and policy files, such as:

- `.github/ISSUE_TEMPLATE/*`
- `.github/DISCUSSION_TEMPLATE/*`
- `.github/pull_request_template.md`
- `.github/PULL_REQUEST_TEMPLATE.md`
- `PULL_REQUEST_TEMPLATE.md`
- `.github/release.yml`
- `README.md`
- `CONTRIBUTING.md`
- `CHANGELOG.md`
- `CODEOWNERS`
- `SECURITY.md`
- `SUPPORT.md`

Read or cache the smallest useful set for the current artifact.

## Manifest

Every cache directory must include `manifest.json` with these fields:

```json
{
  "repo": "owner/name",
  "host": "github.com",
  "source_url": "https://github.com/owner/name",
  "branch": "main",
  "commit_sha": "TBD",
  "fetched_at": "YYYY-MM-DDTHH:MM:SSZ",
  "expires_at": "YYYY-MM-DDTHH:MM:SSZ",
  "paths": [".github/pull_request_template.md"],
  "private_repo": false,
  "user_allowed_cache": true,
  "usage_count": 0,
  "last_used_at": null
}
```

`commit_sha` is required for a cache to be considered fresh evidence. If the source cannot provide a commit SHA, mark the cache as secondary evidence and prefer a fresh targeted remote read when possible.

## Freshness

Default TTL is 14 days.

- If `expires_at` is in the past, treat the cache as stale.
- If `commit_sha`, `fetched_at`, or `paths` is missing, treat the cache as incomplete.
- Do not silently use stale cache as fresh evidence; ask to refresh or use a targeted remote read.
- Local working-tree files still outrank a fresh cache.

## Provenance Output

Keep cache provenance outside the target artifact unless the user requests a provenance report.

Allowed locations:

- Composite `package-manifest.md`
- `Submission Notes`
- A separate provenance report requested by the user

Do not put cache paths, timestamps, usage counts, or generator versions inside a single GitHub issue, PR body, README, changelog, release note, or template file.

## Checklist

- [ ] User explicitly allowed persistent cache use or provided the cache.
- [ ] Cache location is outside the repository and skill runtime.
- [ ] Private repository cache was separately confirmed.
- [ ] Cached files are scenario-relevant only.
- [ ] `manifest.json` has source URL, branch, commit SHA, timestamps, paths, and consent.
- [ ] Stale or incomplete cache was not treated as fresh evidence.
