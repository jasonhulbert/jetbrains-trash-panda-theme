"""
Tests for the theme builder.
"""

import json
import tempfile
import unittest
from pathlib import Path

from theme_builder.builder import ThemeBuilder
from theme_builder.config import ConfigManager
from theme_builder.models import BuildConfig, TargetConfig, TargetTemplate, ThemeConfig
from theme_builder.utils import validate_theme_data


class TestThemeBuilder(unittest.TestCase):
    """Test cases for the theme builder."""

    def setUp(self):
        """Set up test fixtures."""
        self.base_dir = Path(__file__).parent.parent
        self.config_manager = ConfigManager(self.base_dir)

    def test_config_manager(self):
        """Test configuration manager."""
        config = self.config_manager.get_build_config()
        self.assertIsInstance(config, BuildConfig)
        self.assertTrue(config.data_dir.exists())
        self.assertTrue(config.templates_dir.exists())

    def test_themes_config(self):
        """Test themes configuration loading."""
        themes = self.config_manager.get_themes_config()
        self.assertIsInstance(themes, dict)
        self.assertIn('default', themes)

    def test_theme_data_validation(self):
        """Test theme data validation."""
        valid_data = {
            'name': 'Test Theme',
            'author': 'Test Author',
            'dark': True,
            'theme_out_file': 'test.theme.json',
            'scheme_out_file': 'test.xml',
            'theme': {'base0': '000000'}
        }
        self.assertTrue(validate_theme_data(valid_data))

        # Test missing field
        invalid_data = valid_data.copy()
        del invalid_data['name']
        self.assertFalse(validate_theme_data(invalid_data))

    def test_theme_config_from_dict(self):
        """Test ThemeConfig creation from dictionary."""
        data = {
            'name': 'Test Theme',
            'author': 'Test Author',
            'dark': True,
            'high_contrast': False,
            'theme_out_file': 'test.theme.json',
            'scheme_out_file': 'test.xml',
            'parent_scheme': 'Darcula',
            'theme': {'base0': '000000'}
        }
        config = ThemeConfig.from_dict(data)
        self.assertEqual(config.name, 'Test Theme')
        self.assertEqual(config.author, 'Test Author')
        self.assertTrue(config.dark)

    def test_obsidian_output_uses_modern_theme_folder(self):
        """Obsidian themes need theme.css and manifest.json in a theme folder."""
        data = self.config_manager.load_theme_data(
            self.base_dir / 'src' / 'data' / 'default-2026.yaml'
        )
        theme_config = ThemeConfig.from_dict(data)
        build_config = self.config_manager.get_build_config()
        builder = ThemeBuilder(build_config)
        target = TargetConfig(
            name='obsidian',
            templates=[
                TargetTemplate(template='obsidian.tmpl', output_suffix='.css')
            ],
            output_dir='dist/obsidian',
        )

        with tempfile.TemporaryDirectory() as tmp_dir:
            output_dir = Path(tmp_dir)
            legacy_css = output_dir / f"{theme_config.slug}.css"
            legacy_manifest = output_dir / f"{theme_config.slug}.manifest.json"
            legacy_dir = output_dir / theme_config.slug
            legacy_css.write_text('legacy css')
            legacy_manifest.write_text('{}')
            legacy_dir.mkdir()

            builder._render_obsidian_themes(
                target,
                [('default-2026', theme_config, data)],
                output_dir,
            )

            theme_dir = output_dir / data['name']
            theme_css = theme_dir / 'theme.css'
            manifest = theme_dir / 'manifest.json'

            self.assertTrue(theme_css.exists())
            self.assertTrue(manifest.exists())
            self.assertFalse(legacy_css.exists())
            self.assertFalse(legacy_manifest.exists())
            self.assertFalse(legacy_dir.exists())
            self.assertEqual(theme_dir.name, json.loads(manifest.read_text())['name'])


if __name__ == '__main__':
    unittest.main()
