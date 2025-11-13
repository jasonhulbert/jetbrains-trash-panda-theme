import logging
from pathlib import Path
from typing import List


def setup_logging(level: str = "INFO") -> None:
    logging.basicConfig(
        level=getattr(logging, level.upper()),
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    )


def find_theme_files(data_dir: Path) -> List[Path]:
    return list(data_dir.glob("*.yaml"))


def validate_theme_data(theme_data: dict) -> bool:
    required_fields = [
        "name",
        "author",
        "dark",
        "theme_out_file",
        "scheme_out_file",
        "theme",
    ]

    for field in required_fields:
        if field not in theme_data:
            logging.error(f"Missing required field in theme data: {field}")
            return False

    if not isinstance(theme_data["theme"], dict):
        logging.error("Theme data 'theme' field must be a dictionary")
        return False

    return True
