# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Trash Panda Theme is a JetBrains IntelliJ plugin that provides multiple theme variations (dark and light) for IntelliJ-based IDEs. The plugin uses a template-based build system that generates theme files from YAML configuration files.

**Plugin ID**: `com.villains.intelij.plugin.trashpandatheme`
**Current Version**: 3.0.0
**Compatibility**: IntelliJ builds 203 through 252.*

## Build System Architecture

This project uses a **two-stage build process**:

1. **Python Theme Generation** (Stage 1): Generates theme JSON and scheme XML files from YAML templates
2. **Gradle Build** (Stage 2): Packages the generated files into a distributable plugin

### Theme Generation System

The theme generation system is template-based and uses a modern Python package:

- **Data files** (`src/data/*.yaml`): Color palettes and configuration for each theme variant
- **Templates** (`src/templates/*.tmpl`): Jinja2 templates that generate theme.json and scheme.xml files
- **Builder** (`theme_builder/`): Modern Python package with modular architecture for processing templates
- **Configuration** (`theme_builder/themes.yaml`): External theme configuration file
- **Output** (`src/main/resources/META-INF/`): Generated theme.json and scheme.xml files

The builder uses a modular architecture with separate modules for models, configuration, CLI, and core building logic. It iterates through 7 theme variants (default, default-2026, starlight, moonlight, dawnlight, daylight, blacklight) and generates corresponding theme and scheme files for each.

## Common Commands

### Building Theme Files

**IMPORTANT**: Always run theme generation before building the plugin:

```bash
# Using uv (recommended)
uv run python -m theme_builder

# OR using python directly
python -m theme_builder

# Build specific theme only
uv run python -m theme_builder --theme starlight

# List available themes
uv run python -m theme_builder --list-themes

# Enable debug logging
uv run python -m theme_builder --log-level DEBUG
```

This generates all `*.theme.json` and `*.xml` files in `src/main/resources/META-INF/`.

### Building the Plugin

```bash
# Build the plugin distribution
./gradlew assemble

# Output location: build/distributions/jetbrains-trash-panda-theme-[version].zip
```

### Testing the Plugin

```bash
# Run the plugin in a sandboxed IntelliJ instance
./gradlew runIde
```

### Other Gradle Tasks

```bash
# Clean build artifacts
./gradlew clean

# Verify plugin structure
./gradlew verifyPlugin

# Build and verify
./gradlew build
```

## Development Workflow

When modifying theme colors or adding new theme variants:

1. Edit the YAML file in `src/data/` (e.g., `default.yaml`, `starlight.yaml`)
2. Run the Python theme builder: `uv run python -m theme_builder` or `python -m theme_builder`
3. Build the plugin: `./gradlew assemble`
4. Test in sandbox IDE: `./gradlew runIde`

When modifying theme templates:

1. Edit Jinja2 templates in `src/templates/` (`theme.tmpl` or `scheme.tmpl`)
2. Run the Python theme builder to regenerate all themes
3. Build and test as above

## Adding New Theme Variants

To add a new theme variant:

1. Create a new YAML file in `src/data/` (e.g., `newtheme.yaml`)
2. Add the theme to `theme_builder/themes.yaml` configuration file
3. Register the new theme in `src/main/resources/META-INF/plugin.xml` with a new `<themeProvider>` entry
4. Update the plugin description if needed
5. Run the theme builder (`uv run python -m theme_builder` or `python -m theme_builder`) and rebuild the plugin

## File Structure

- `build.gradle` - Gradle build configuration with IntelliJ plugin settings
- `src/data/*.yaml` - Theme color palettes and metadata
- `src/templates/*.tmpl` - Jinja2 templates for theme.json and scheme.xml generation
- `theme_builder/` - Modern Python package for theme generation with modular architecture:
  - `__init__.py` - Package initialization
  - `cli.py` - Command-line interface
  - `builder.py` - Core theme building logic
  - `config.py` - Configuration management
  - `models.py` - Data models and types
  - `utils.py` - Helper functions
  - `themes.yaml` - Theme configuration file
- `src/main/resources/META-INF/plugin.xml` - Plugin descriptor with theme provider registrations
- `src/main/resources/META-INF/*.theme.json` - Generated theme files (UI colors)
- `src/main/resources/META-INF/*.xml` - Generated scheme files (editor syntax colors)

## Important Notes

- **Never commit generated files without regenerating them first** - Always run `uv run python -m theme_builder` or `python -m theme_builder` before committing changes to theme data/templates
- **Version synchronization** - Keep version numbers synchronized across `build.gradle`, `plugin.xml`, and `pyproject.toml`
- **Compatibility updates** - When updating IntelliJ compatibility ranges, update `patchPluginXml.sinceBuild` and `untilBuild` in `build.gradle`
- **Color modifiers** - Theme YAML files use a `_mod1`, `_mod2`, `_mod3` suffix pattern for color variations (progressively darker/lighter shades)
- **Parent scheme** - All themes inherit from either "Darcula" (dark) or "IntelliJ" (light) as specified in the YAML `parent_scheme` field

## Python Environment

The project uses `uv` for Python dependency management:

- `pyproject.toml` - Python project configuration with dependencies (Jinja2, ruamel.yaml)
- Required Python version: 3.8+
- Install dependencies: `uv sync` or `pip install jinja2 ruamel.yaml`

The theme builder is a modern Python package with modular architecture including CLI, configuration management, type safety, and comprehensive error handling.

