# Package Manifest

- Package option: Standard release pack
- Output path: `.github-writing/version-release/v1.2.0/`

## Generated Files

| File | Intended target | Status |
|------|-----------------|--------|
| `package-manifest.md` | Local workflow package manifest | Safe local draft |
| `.github-writing/version-release/v1.2.0/CHANGELOG.patch.md` | Changelog draft | Safe local draft |
| `.github-writing/version-release/v1.2.0/RELEASE_NOTES.md` | Release notes draft | Safe local draft |

## Assumptions

- Version: `v1.2.0`
- Release date: TBD
- Compare URL: TBD

## Evidence Sources

- Changelog source: merged PR summaries provided in prompt.
- Release scope: fix login redirect, add CSV export, update docs.

## Safe To Write

- Local draft files under `.github-writing/version-release/v1.2.0/`

## Requires Confirmation

- Applying the changelog draft to root `CHANGELOG.md`
- Publishing the GitHub Release
- Creating or pushing a tag
- Updating remote release notes
