import logging
from pathlib import Path
from typing import Dict, Any, Optional
from ruamel.yaml import YAML

from .models import BuildConfig

logger = logging.getLogger(__name__)


class ConfigManager:
    def __init__(self, base_dir: Path):
        self.base_dir = base_dir
        self.yaml = YAML(typ="safe")

    def get_build_config(self, output_dir: Path = None) -> BuildConfig:
        data_dir = self.base_dir / "src" / "data"
        templates_dir = self.base_dir / "src" / "templates"

        if output_dir is None:
            output_dir = self.base_dir / "src" / "main" / "resources" / "META-INF"

        return BuildConfig(
            data_dir=data_dir, templates_dir=templates_dir, output_dir=output_dir
        )

    def get_themes_config(self) -> Dict[str, str]:
        themes_config_file = self.base_dir / "theme_builder" / "themes.yaml"

        if themes_config_file.exists():
            with open(themes_config_file, "r") as f:
                config = self.yaml.load(f)
                return {theme["name"]: theme["data_file"] for theme in config["themes"]}
        else:
            # Theme file does not exist, return empty config
            logger.error("No themes.yaml found.")

            return {}

    def load_theme_data(self, data_file: Path) -> Dict[str, Any]:
        if not data_file.exists():
            raise FileNotFoundError(f"Theme data file not found: {data_file}")

        try:
            with open(data_file, "r") as f:
                data = self.yaml.load(f)
                logger.debug(f"Loaded theme data from {data_file}")
                return data
        except Exception as e:
            logger.error(f"Failed to load theme data from {data_file}: {e}")
            raise
