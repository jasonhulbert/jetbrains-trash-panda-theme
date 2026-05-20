from dataclasses import dataclass
from pathlib import Path
from typing import Dict, Any, List, Optional


@dataclass
class TargetTemplate:
    template: str
    output_key: Optional[str] = None
    output_suffix: Optional[str] = None


@dataclass
class TargetConfig:
    name: str
    templates: List[TargetTemplate]
    output_dir: str
    enabled: bool = True

    @classmethod
    def from_dict(cls, name: str, data: Dict[str, Any]) -> "TargetConfig":
        templates = []
        for t in data.get("templates", []):
            templates.append(
                TargetTemplate(
                    template=t["template"],
                    output_key=t.get("output_key"),
                    output_suffix=t.get("output_suffix"),
                )
            )
        return cls(
            name=name,
            templates=templates,
            output_dir=data["output_dir"],
            enabled=data.get("enabled", True),
        )


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

    @property
    def slug(self) -> str:
        """Derive slug from theme_out_file by stripping .theme.json suffix."""
        return self.theme_out_file.replace(".theme.json", "")

    @property
    def slug_underscored(self) -> str:
        """Slug with underscores instead of hyphens (for Warp filenames)."""
        return self.slug.replace("-", "_")


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
