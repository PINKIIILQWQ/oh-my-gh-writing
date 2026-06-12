# ripgrep (rg)

> ripgrep is a line-oriented search tool that recursively searches the current
> directory for a regex pattern while respecting gitignore rules.

## Quick Start

```bash
# macOS
brew install ripgrep

# Linux (deb)
curl -LO https://github.com/BurntSushi/ripgrep/releases/download/15.1.0/ripgrep_15.1.0-1_amd64.deb
sudo dpkg -i ripgrep_15.1.0-1_amd64.deb

# Windows (scoop)
scoop install ripgrep

# From source (requires Rust)
cargo install ripgrep
```

**TODO**: Replace release URL with the latest version from [releases](https://github.com/BurntSushi/ripgrep/releases).

## Usage

```bash
rg pattern             # Search recursively in current dir
rg "foo.*bar"          # Regex search
rg -i "hello"          # Case-insensitive
rg -g "!*.min.js"      # Exclude glob
rg --type py "class"   # File-type filter
rg -l "FIXME"          # Only list file paths
```

See `rg --help` or the [full documentation](https://github.com/BurntSushi/ripgrep/blob/master/README.md).

## License

Unlicense OR MIT
