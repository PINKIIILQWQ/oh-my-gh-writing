# 14 Release Notes 测试

# ripgrep 15.0.0

Published: 2025-10-16

ripgrep 15.0.0 is a major release focused on bug fixes, small performance improvements, and several user-facing search enhancements.

## Highlights

- Fixes several bugs around gitignore matching, including cases involving parent directories.
- Fixes a memory usage regression when handling very large gitignore files.
- Makes `rg -vf file` match everything when `file` is empty.
- Makes `-r/--replace` work with `--json`.
- Treats a subset of Jujutsu (`jj`) repositories as Git repositories so ripgrep respects their gitignores.
- Adds support for nested alternates in globs.

## Platform Support

- Adds release artifacts for Windows `aarch64`.
- Stops generating release artifacts for `powerpc64`.
- Builds release binaries with full LTO enabled, which may modestly reduce binary size and improve performance.

## Performance

- Avoids resolving helper binaries on Windows when `-z/--search-zip` is not used (#2111).
- Avoids path canonicalization on Windows when emitting hyperlinks (#2865).
- Improves performance of large values with `-A/--after-context` (#3184).

## Bug Fixes

- Fixes gitignore handling for parent directories (#829, #2731, #2747, #2770, #2778, #2836, #2933, #3067).
- Makes `rg -vf file` where `file` is empty match everything (#1332, #3001).
- Ignores UTF-8 BOM markers at the start of `.gitignore` and similar files (#2177).
- Fixes memory usage regression for very large gitignore files (#2750).
- Fixes incorrect "bytes searched" values in `--stats` output (#2944).
- Fixes glob handling when a glob ends with `.` (#2990).
- Fixes `-m/--max-count` with `-U/--multiline` showing too many matches (#2094, #3076).
- Preserves line terminators when using `-r/--replace` (#3100).
- Fixes `-q --files-without-match` exit code inversion (#3108).
- Fixes a rare panic for some large regexes on large haystacks (#3135).
- Fixes incorrect summary statistics with `--json` (#3178).
- Fixes a panic when using `-U/--multiline` and `-r/--replace` (#3180).

## Feature Enhancements

- Adds many enhancements to the default set of file types available for filtering.
- Adds `-r/--replace` support with `--json` (#1872).
- Improves shell completions for fish, bash, and zsh (#2708, #3096, #3102).
- Adds `italic` to available `--color` style attributes (#2841).
- Treats directories containing `.jj` as Git repositories (#2842).
- Schedules files in CLI order when using multithreading (#2849).
- Adds Windows `aarch64` release artifacts (#2943).
- Adds `highlight` color type for styling non-matching text in a matching line (#3024).
- Adds nested alternate support for globs (#3048).

## Breaking Changes

No explicit migration command or breaking-change section was provided in the release notes. The platform-support change for `powerpc64` release artifacts may affect users who depended on those binaries.

## Full Changelog

https://github.com/BurntSushi/ripgrep/releases/tag/15.0.0
