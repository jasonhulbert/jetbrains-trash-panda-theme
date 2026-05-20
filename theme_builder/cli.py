import argparse
import logging
import sys
from pathlib import Path

from .builder import ThemeBuilder
from .config import ConfigManager
from .utils import setup_logging

logger = logging.getLogger(__name__)


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Build theme files for the Trash Panda Theme",
        prog="build-themes",
    )

    parser.add_argument(
        "--theme", help="Build specific theme only", metavar="THEME_NAME"
    )

    parser.add_argument(
        "--target",
        choices=["jetbrains", "vscode", "warp", "obsidian", "all"],
        default="all",
        help="Build for specific target only (default: all)",
    )

    parser.add_argument(
        "--output-dir", type=Path, help="Override output directory", metavar="PATH"
    )

    parser.add_argument(
        "--list-themes", action="store_true", help="List available themes and exit"
    )

    parser.add_argument(
        "--list-targets", action="store_true", help="List available targets and exit"
    )

    parser.add_argument(
        "--log-level",
        choices=["DEBUG", "INFO", "WARNING", "ERROR"],
        default="INFO",
        help="Set logging level (default: INFO)",
    )

    parser.add_argument("--version", action="version", version="%(prog)s 3.0.0")

    args = parser.parse_args()

    # Set up logging
    setup_logging(args.log_level)

    try:
        base_dir = Path(__file__).parent.parent
        logger.debug(f"Using base directory: {base_dir}")

        config_manager = ConfigManager(base_dir)
        build_config = config_manager.get_build_config(args.output_dir)

        builder = ThemeBuilder(build_config)

        if args.list_themes:
            themes = builder.list_available_themes()
            print("Available themes:")
            for theme in sorted(themes):
                print(f"  - {theme}")
            return 0

        if args.list_targets:
            targets = builder.list_available_targets()
            print("Available targets:")
            for target in sorted(targets):
                print(f"  - {target}")
            return 0

        if args.theme:
            logger.info(f"Building specific theme: {args.theme}")

        if args.target != "all":
            logger.info(f"Building for target: {args.target}")

        builder.build_all(
            theme_filter=args.theme,
            target_filter=args.target,
        )

        print("Theme building completed successfully!")
        return 0

    except FileNotFoundError as e:
        logger.error(f"File not found: {e}")
        return 1
    except ValueError as e:
        logger.error(f"Configuration error: {e}")
        return 1
    except Exception as e:
        logger.error(f"Unexpected error: {e}")
        logger.debug("Full traceback:", exc_info=True)
        return 1


if __name__ == "__main__":
    sys.exit(main())
