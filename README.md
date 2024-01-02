# JetBrains Trash Panda Theme

A theme for raccoons and other creatures of the night.

[📦 Download/Install](https://plugins.jetbrains.com/plugin/12995-trash-panda-theme)

[🙏 Donate to say thanks](https://www.venmo.com/u/Jason-Hulbert-1)

---

Building the plugin:

Before building the plugin, compile the template files via python. Run the following python command from the project root.

```
python ./theme.py
```

This will generate the theme json and scheme xml files in `src/main/resources`. 

To build the plugin, run the following gradle wrapper script from the project root:

```
./gradlew assemble
```
