# 02 Feature Request 测试

## Feature Description

Add a native `hermes profile link` CLI command that maps portable files from `~/.hermes/profiles/<name>` to an external Git working tree through symbolic links.

The goal is to let a profile behave as a live, version-controlled configuration source instead of a static snapshot created by `profile install`.

## Motivation

`hermes profile install` is useful for distributing profile files, but the prompt states that it removes the cloned `.git/` directory. That makes installed profiles difficult to keep in sync with an upstream configuration repository.

This creates three common problems:

- Users cannot update profile files with a normal `git pull`.
- Local edits made while using Hermes cannot be tracked and pushed back to the profile repository.
- Users cannot manage Hermes profile files in the same dotfiles workflow they use for tools such as `nvim`, `zsh`, or `tmux`.

The prompt also mentions `agentlink` as a third-party shell-script workaround, which suggests there is user demand for a first-party workflow.

## Use Cases

### Keep a profile synced from a dotfiles repository

```bash
hermes profile link work ~/dotfiles/hermes/work
cd ~/dotfiles/hermes/work
git pull
```

Expected result: portable profile files update in place without reinstalling the profile.

### Track local profile edits

```bash
hermes profile link personal ~/src/hermes-profile
# Hermes updates portable profile files during normal use.
cd ~/src/hermes-profile
git status
```

Expected result: portable file changes appear in the external Git repository and can be reviewed before commit.

## Proposed CLI

```bash
hermes profile link <name> <path>
```

Proposed behavior:

1. Validate that `<name>` resolves to a Hermes profile.
2. Validate that `<path>` exists, or create it when an explicit creation flag is provided.
3. Link portable profile files from the profile directory to the external path.
4. Leave local-only runtime state in `~/.hermes/profiles/<name>/`.
5. Refuse to overwrite conflicting files unless the user passes an explicit force option.

## Portable Files

The following files and directories are proposed as linkable profile content:

```text
SOUL.md
config.yaml
mcp.json
skills/
cron/
plugins/
```

## Local-Only Files

These should remain in the Hermes profile directory and should not be linked into the external Git repository:

```text
.env
auth.json
memories/
sessions/
state.db
logs/
```

## Optional Follow-Up Commands

```bash
hermes profile link --check <name> <path>
hermes profile link --unlink <name>
```

`--check` would verify that expected links still point to the external repository. `--unlink` would restore the profile to regular files without deleting the external repository.

## Alternatives Considered

| Option | Limitation |
|--------|------------|
| Continue using `profile install` | Good for distribution, but the prompt says it creates a static copy rather than a live Git working tree. |
| Manually create symlinks | Works for advanced users, but is undocumented, easy to break, and hard to validate. |
| Use `agentlink` | Confirms the workflow is useful, but adds a separate tool and cannot reliably track future Hermes profile layout changes. |

## Compatibility Notes

- Existing `profile install` behavior should remain unchanged.
- `profile link` should fail safely when a target file already exists and differs from the profile file.
- Atomic writes should preserve symlinks; if that behavior is not guaranteed in all profile writers, this should be verified before release.
- The exact portable/local file boundary should be confirmed against the current Hermes profile schema.

## Open Questions

- Should `<path>` be required to be a Git repository, or can it be any directory?
- Should the command link files individually, or link a whole profile subtree with an ignore list?
- Should `--unlink` copy current external file contents back into the profile directory?
- Which profile writers might replace symlinks instead of writing through them?
