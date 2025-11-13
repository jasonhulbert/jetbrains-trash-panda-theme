from dataclasses import dataclass
from pathlib import Path
from typing import Dict, Any, Optional


@dataclass
class ThemeConfig:
    name: str
    author: str
    dark: bool
    high_contrast: bool
    theme_out_file: str
    scheme_out_file: str
    parent_scheme: str
    theme: Dict[str, str]

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "ThemeConfig":
        return cls(
            name=data["name"],
            author=data["author"],
            dark=data["dark"],
            high_contrast=data["high_contrast"],
            theme_out_file=data["theme_out_file"],
            scheme_out_file=data["scheme_out_file"],
            parent_scheme=data["parent_scheme"],
            theme=data["theme"],
        )


@dataclass
class BuildConfig:
    data_dir: Path
    templates_dir: Path
    output_dir: Path
    themes_config_file: Optional[Path] = None

    def __post_init__(self):
        if not self.data_dir.exists():
            raise FileNotFoundError(f"Data directory not found: {self.data_dir}")
        if not self.templates_dir.exists():
            raise FileNotFoundError(
                f"Templates directory not found: {self.templates_dir}"
            )
        if not self.output_dir.exists():
            self.output_dir.mkdir(parents=True, exist_ok=True)
