# JetBrains Trash Panda Theme

A theme for raccoons and other creatures of the night.

## Installation

[📦 Download/Install from Marketplace](https://plugins.jetbrains.com/plugin/12995-trash-panda-theme)

## Donations

[🙏 Donate to say thanks](https://www.venmo.com/u/Jason-Hulbert-1)

## Building the plugin:

### Theme Builder (Modern Approach)

The project includes a modern Python theme builder for generating theme files from YAML configuration and Jinja2 templates.

**Quick Start with UV (Recommended):**
```bash
# Install dependencies
uv sync

# Build all themes  
uv run python -m theme_builder
```

**Alternative methods:**
```bash
# Direct Python execution
python -m theme_builder

# Build specific theme
uv run python -m theme_builder --theme starlight

# List available themes
uv run python -m theme_builder --list-themes

# Enable debug logging
uv run python -m theme_builder --log-level DEBUG
```

> See [CLAUDE.md](CLAUDE.md) for additional details.

### Plugin Distribution

This will generate the theme `*.json` and scheme `*.xml` files in `src/main/resources`. 

To build the plugin for distribution, run the following gradle wrapper script from the project root:

```
./gradlew assemble
```

This will produce an installable plugin distribution located at `build/distributions/jetbrains-trash-panda-theme-[version].zip`.
