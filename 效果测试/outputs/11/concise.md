---
scenario: README
mode: concise
case-sources: https://github.com/ohmyzsh/ohmyzsh, https://github.com/nektos/act
input-prompt: ../../prompts/11-readme.md
---

# zzz — Terminal countdown + command runner

> "Set a timer, run your command."

```bash
# Countdown 30 seconds, then run deploy
zzz 30 -- ./deploy.sh

# Quick 5-second reminder
zzz 5 -- notify-send "Pasta is ready!"
```

## Install
```bash
curl -fsSL https://zzz.example/install.sh | sh
```

## Usage
```
zzz <seconds> -- <command>
zzz 1m30s -- ./test.sh   (90s with human-friendly duration)
zzz --help
```

## License
MIT
