# zzz v2.0.0 — Config overhaul + plugin system

## 🔥 Breaking Changes

### Config format: JSON → YAML
The configuration file format has changed from `.zzzrc.json` to
`.zzzrc.yaml` for better readability and composability.

**Before** (`.zzzrc.json`):
```json
{ "defaultDuration": 30, "sound": true }
```

**After** (`.zzzrc.yaml`):
```yaml
default_duration: 30
sound: true
profiles:
  dev: { duration: 15 }
  prod: { duration: 60 }
```

Migration: Run `zzz migrate-config` to auto-convert existing config.

### Profile directory structure
`--profile` flag now loads from `$HOME/.config/zzz/profiles/`:
```bash
zzz --profile dev 30 -- deploy.sh
```

## 🚀 New Features

### Multi-environment profiles
Define different presets for different environments:
```yaml
# ~/.config/zzz/profiles/dev.yaml
duration: 15
command: npm run dev
```

### Plugin system
Extend zzz with custom behaviors:
```bash
zzz --plugin notify -- 10 -- echo "Done!"
```

Built-in plugins: `notify` (desktop notification), `sound` (audio alert),
`webhook` (HTTP callback).

## Full Changelog
https://github.com/example/zzz/releases/tag/v2.0.0
