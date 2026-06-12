# zzz — Terminal countdown with command execution

> A lightweight CLI that counts down and runs your command when time's up.
> No dependencies. One binary. Works on Linux, macOS, and WSL.

## Quick Start
```bash
# 10 second countdown, then run tests
zzz 10 -- npm test

# Countdown with human-readable duration
zzz 2m30s -- ./deploy.sh
```

## Features
- **Human-friendly durations**: `zzz 1h30m`, `zzz 45s`, `zzz 5m`
- **Command execution**: Runs any command after countdown completes
- **Visual countdown**: Progress bar with remaining time
- **Cancel**: Ctrl+C stops countdown without running command
- **Sound alert**: Bell on completion (optional, `--bell`)

## Install
### macOS (Homebrew)
```bash
brew install zzz
```

### Linux (deb/rpm)
```bash
curl -LO https://github.com/example/zzz/releases/latest/zzz_amd64.deb
sudo dpkg -i zzz_amd64.deb
```

### From source
```bash
go install github.com/example/zzz@latest
```

## Usage
```
zzz [duration] -- [command] [args...]
```

### Examples
| Command | Effect |
|---------|--------|
| `zzz 30 -- deploy.sh` | 30s countdown, then deploy |
| `zzz 5m -- notify-send "Done"` | 5min, then notify |
| `zzz --help` | Show all options |

## License
MIT — see [LICENSE](./LICENSE)
