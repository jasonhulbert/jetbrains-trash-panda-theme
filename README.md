# JetBrains Trash Panda Theme

A theme for raccoons and other creatures of the night.

## Installation

[📦 Download/Install from Marketplace](https://plugins.jetbrains.com/plugin/12995-trash-panda-theme)

## Donations

[🙏 Donate to say thanks](https://www.venmo.com/u/Jason-Hulbert-1)

## Building the plugin:

First, compile the theme template files via python. Run the following python command from the project root:

```
python ./theme.py
```

This will generate the theme `*.json` and scheme `*.xml` files in `src/main/resources`. 

To build the plugin for distribution, run the following gradle wrapper script from the project root:

```
./gradlew assemble
```

This will produce an installable plugin distribution located at `build/distributions/jetbrains-trash-panda-theme-[version].zip`.
