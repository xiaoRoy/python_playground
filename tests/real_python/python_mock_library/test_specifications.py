import unittest
from unittest.mock import Mock, create_autospec, patch
import src.real_python.python_mock_library.learning_mock as holidays


class TestSpecifications(unittest.TestCase):

    def test_specifications(self):
        mock_learning = Mock(spec=["is_weekday", "get_holidays"])
        with self.assertRaises(AttributeError):
            mock_learning.not_a_method()

    def test_specification_using_auto_spec(self):
        mock_learning = create_autospec(holidays)
        with self.assertRaises(AttributeError):
            mock_learning.not_a_method()

    def test_specification_using_patch(self):
        with patch("src.real_python.python_mock_library.learning_mock", autospec=True) as mock_holidays:
        # with patch("__main__.learning_mock", autospec=True) as mock_holidays:
            with self.assertRaises(AttributeError):
                mock_holidays.not_a_method()
