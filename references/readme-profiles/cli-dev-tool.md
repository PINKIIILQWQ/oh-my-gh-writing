# README Profile: CLI / Developer Tool

## Use When

Use for command-line tools, local developer utilities, code generators, linters, formatters, release helpers, or workflow automation commands.

## Required Shape

- Overview: the task the tool automates.
- Quick Start: install command, first successful command, expected output.
- Usage: common commands with flags and examples.
- Configuration: config files, environment variables, defaults.
- Compatibility: OS, shell, runtime, package manager, required tools.
- Development: build/test commands only when evidenced.

## Quick Start

Start with one install path and one minimal command. Put each standalone command on its own line. Do not combine setup steps with `&&` when users may copy lines independently.

## Applicability

State supported operating systems, shells, runtimes, package managers, local/CI use, auth requirements, and project types the tool can operate on.

## Badges/Visuals

Use package version, CI, license, and downloads badges only when registry or workflow evidence exists. Include terminal GIFs or screenshots only when assets are present.

## Avoid

- Long architecture before first runnable command.
- Claiming CI support without workflow examples.
- Inventing package names, install commands, or config files.

## Evidence Required

Use package manifests, executable entry points, help output, config files, CI files, official package registry pages, and user-provided commands.
