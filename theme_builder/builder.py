import logging
from typing import Dict, List, Optional, Any
from jinja2 import Environment, FileSystemLoader, select_autoescape

from .models import ThemeConfig, BuildConfig
from .config import ConfigManager
from .utils import validate_theme_data

logger = logging.getLogger(__name__)


class ThemeBuilder:
    def __init__(self, config: BuildConfig):
        self.config = config
        self.config_manager = ConfigManager(config.data_dir.parent.parent)

        self.env = Environment(
            loader=FileSystemLoader(config.templates_dir),
            autoescape=select_autoescape(),
        )
        self.env.filters["bool"] = bool

        logger.info(f"ThemeBuilder initialized with output dir: {config.output_dir}")

    def build_theme(self, theme_name: str, theme_data_file: str) -> None:
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

    def build_all(self, theme_filter: Optional[str] = None) -> None:
        themes_config = self.config_manager.get_themes_config()

        if theme_filter:
            if theme_filter not in themes_config:
                raise ValueError(f"Theme '{theme_filter}' not found in configuration")
            themes_to_build = {theme_filter: themes_config[theme_filter]}
        else:
            themes_to_build = themes_config

        logger.info(f"Building {len(themes_to_build)} theme(s)...")

        for theme_name, data_file in themes_to_build.items():
            self.build_theme(theme_name, data_file)

        logger.info("All themes built successfully")

    def _render_theme_files(
        self, theme_config: ThemeConfig, theme_data: Dict[str, Any]
    ) -> None:
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
