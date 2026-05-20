import logging
import shutil
from pathlib import Path
from typing import Dict, List, Optional, Any
from jinja2 import Environment, FileSystemLoader, select_autoescape

from .models import ThemeConfig, BuildConfig, TargetConfig
from .config import ConfigManager
from .utils import validate_theme_data

logger = logging.getLogger(__name__)


class ThemeBuilder:
    def __init__(self, config: BuildConfig):
        self.config = config
        self.base_dir = config.data_dir.parent.parent
        self.config_manager = ConfigManager(self.base_dir)

        self.env = Environment(
            loader=FileSystemLoader(config.templates_dir),
            autoescape=select_autoescape(),
        )
        self.env.filters["bool"] = bool

        logger.info(f"ThemeBuilder initialized with output dir: {config.output_dir}")

    def build_theme(self, theme_name: str, theme_data_file: str) -> None:
        """Build a single theme for the JetBrains target (legacy compat)."""
        logger.info(f"Building theme: {theme_name}")

        try:
            data_file_path = self.config.data_dir / theme_data_file
            theme_data = self.config_manager.load_theme_data(data_file_path)

            if not validate_theme_data(theme_data):
                raise ValueError(f"Invalid theme data in {theme_data_file}")

            theme_config = ThemeConfig.from_dict(theme_data)

            self._render_theme_files(theme_config, theme_data)

            logger.info(f"Successfully built theme: {theme_name}")

        except FileNotFoundError as e:
            logger.error(f"Theme data file not found for {theme_name}: {e}")
            raise
        except Exception as e:
            logger.error(f"Failed to build theme {theme_name}: {e}")
            raise

    def build_all(
        self,
        theme_filter: Optional[str] = None,
        target_filter: Optional[str] = None,
    ) -> None:
        themes_config = self.config_manager.get_themes_config()
        targets = self.config_manager.get_targets_config()

        if theme_filter:
            if theme_filter not in themes_config:
                raise ValueError(f"Theme '{theme_filter}' not found in configuration")
            themes_to_build = {theme_filter: themes_config[theme_filter]}
        else:
            themes_to_build = themes_config

        if target_filter and target_filter != "all":
            targets = [t for t in targets if t.name == target_filter]
            if not targets:
                raise ValueError(f"Target '{target_filter}' not found in configuration")

        logger.info(
            f"Building {len(themes_to_build)} theme(s) for "
            f"{len(targets)} target(s)..."
        )

        # Load all theme data up front
        loaded_themes: List[tuple] = []
        for theme_name, data_file in themes_to_build.items():
            data_file_path = self.config.data_dir / data_file
            theme_data = self.config_manager.load_theme_data(data_file_path)
            if not validate_theme_data(theme_data):
                raise ValueError(f"Invalid theme data in {data_file}")
            theme_config = ThemeConfig.from_dict(theme_data)
            loaded_themes.append((theme_name, theme_config, theme_data))

        for target in targets:
            logger.info(f"Building target: {target.name}")
            output_dir = self.base_dir / target.output_dir
            output_dir.mkdir(parents=True, exist_ok=True)

            if target.name == "obsidian":
                self._render_obsidian_themes(target, loaded_themes, output_dir)
                continue

            for theme_name, theme_config, theme_data in loaded_themes:
                self._render_target_files(target, theme_config, theme_data, output_dir)

            # Generate VS Code package.json after all VS Code themes
            if target.name == "vscode":
                self._render_vscode_package_json(loaded_themes, output_dir)

        logger.info("All themes built successfully")

    def _render_target_files(
        self,
        target: TargetConfig,
        theme_config: ThemeConfig,
        theme_data: Dict[str, Any],
        output_dir: Path,
    ) -> None:
        for target_tmpl in target.templates:
            template = self.env.get_template(target_tmpl.template)

            if target_tmpl.output_key:
                # JetBrains style: filename from data YAML field
                filename = theme_data[target_tmpl.output_key]
            elif target_tmpl.output_suffix:
                # VS Code / Warp style: slug + suffix
                if target.name == "warp":
                    filename = theme_config.slug_underscored + target_tmpl.output_suffix
                else:
                    filename = theme_config.slug + target_tmpl.output_suffix
            else:
                raise ValueError(
                    f"Target template {target_tmpl.template} has no "
                    f"output_key or output_suffix"
                )

            output_path = output_dir / filename
            with open(output_path, "w") as f:
                f.write(template.render(theme_data))
            logger.debug(f"Wrote {target.name} file: {output_path}")

    def _render_vscode_package_json(
        self,
        loaded_themes: List[tuple],
        themes_output_dir: Path,
    ) -> None:
        """Generate dist/vscode/package.json from the vscode-package template."""
        try:
            template = self.env.get_template("vscode-package.tmpl")
        except Exception:
            logger.warning("vscode-package.tmpl not found, skipping package.json")
            return

        # Build list of theme entries for the manifest
        theme_entries = []
        for theme_name, theme_config, theme_data in loaded_themes:
            label = theme_config.name
            ui_theme = "vs-dark" if theme_config.dark else "vs"
            filename = f"themes/{theme_config.slug}-color-theme.json"
            theme_entries.append({
                "label": label,
                "uiTheme": ui_theme,
                "path": filename,
            })

        package_dir = themes_output_dir.parent  # dist/vscode/
        package_dir.mkdir(parents=True, exist_ok=True)
        output_path = package_dir / "package.json"

        with open(output_path, "w") as f:
            f.write(template.render(themes=theme_entries))
        logger.debug(f"Wrote VS Code package.json: {output_path}")

    def _render_obsidian_themes(
        self,
        target: TargetConfig,
        loaded_themes: List[tuple],
        output_dir: Path,
    ) -> None:
        """Generate each Obsidian theme as a modern theme folder."""
        try:
            manifest_template = self.env.get_template("obsidian-manifest.tmpl")
        except Exception:
            logger.warning("obsidian-manifest.tmpl not found, skipping Obsidian manifests")
            return

        for theme_name, theme_config, theme_data in loaded_themes:
            self._remove_legacy_obsidian_files(output_dir, theme_config)

            theme_dir = output_dir / theme_config.name
            theme_dir.mkdir(parents=True, exist_ok=True)

            for target_tmpl in target.templates:
                template = self.env.get_template(target_tmpl.template)
                theme_path = theme_dir / "theme.css"
                with open(theme_path, "w") as f:
                    f.write(template.render(theme_data))
                logger.debug(f"Wrote Obsidian theme CSS: {theme_path}")

            manifest_path = theme_dir / "manifest.json"
            with open(manifest_path, "w") as f:
                f.write(manifest_template.render(theme_data))
            logger.debug(f"Wrote Obsidian manifest: {manifest_path}")

    def _remove_legacy_obsidian_files(
        self,
        output_dir: Path,
        theme_config: ThemeConfig,
    ) -> None:
        """Remove old Obsidian output paths for rebuilt themes."""
        for legacy_path in (
            output_dir / f"{theme_config.slug}.css",
            output_dir / f"{theme_config.slug}.manifest.json",
            output_dir / theme_config.slug,
        ):
            if legacy_path.exists():
                if legacy_path.is_dir():
                    shutil.rmtree(legacy_path)
                else:
                    legacy_path.unlink()
                logger.debug(f"Removed legacy Obsidian output: {legacy_path}")

    def _render_theme_files(
        self, theme_config: ThemeConfig, theme_data: Dict[str, Any]
    ) -> None:
        """Legacy method for single-theme JetBrains build."""
        theme_template = self.env.get_template("theme.tmpl")
        scheme_template = self.env.get_template("scheme.tmpl")

        theme_output_path = self.config.output_dir / theme_config.theme_out_file
        with open(theme_output_path, "w") as f:
            f.write(theme_template.render(theme_data))
        logger.debug(f"Wrote theme file: {theme_output_path}")

        scheme_output_path = self.config.output_dir / theme_config.scheme_out_file
        with open(scheme_output_path, "w") as f:
            f.write(scheme_template.render(theme_data))
        logger.debug(f"Wrote scheme file: {scheme_output_path}")

    def list_available_themes(self) -> List[str]:
        themes_config = self.config_manager.get_themes_config()
        return list(themes_config.keys())

    def list_available_targets(self) -> List[str]:
        targets = self.config_manager.get_targets_config()
        return [t.name for t in targets]
