"""
Tests for the theme builder.
"""

import tempfile
import unittest
from pathlib import Path

from theme_builder.builder import ThemeBuilder
from theme_builder.config import ConfigManager
from theme_builder.models import BuildConfig, ThemeConfig
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


if __name__ == '__main__':
    unittest.main()
