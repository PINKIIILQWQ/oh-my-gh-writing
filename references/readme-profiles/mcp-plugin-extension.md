# README Profile: MCP Server / Plugin / Extension

## Use When

Use for MCP servers, editor extensions, Codex/agent plugins, browser extensions, IDE integrations, or host-specific add-ons.

## Required Shape

- Overview: host capability added by the integration.
- Quick Start: host-specific install or registration path.
- Compatibility: supported host apps and protocol versions.
- Configuration: permissions, auth, environment variables, local/remote transport.
- Usage: example commands or host interactions.
- Security boundary: what data leaves the host.

## Quick Start

Choose the primary host setup path first. If multiple hosts differ only by target path or config key, show each path as its own copyable block and keep shared commands separate.

## Applicability

State supported host apps, plugin format, MCP transport, permissions, auth requirements, local/remote boundary, supported commands/tools, and unsupported hosts.

## Badges/Visuals

Use host, protocol, version, license, and validation badges only when evidenced. Prefer official host icons or omit icons.

## Avoid

- Claiming native support for hosts that require adapted rules.
- Hiding permission or network behavior.
- Mixing plugin installation with unrelated project setup.

## Evidence Required

Use manifest files, host docs, MCP config, extension metadata, plugin registry pages, security notes, and user-tested install paths.
