import unittest
from unittest.mock import patch

from requests import Timeout

from src.real_python.python_mock_library.learning_mock import requests, get_holidays, is_weekday


class TestHolidays(unittest.TestCase):

    @patch.object(requests, "get", side_effect=Timeout)
    def test_get_holidays_timeout(self, mock_requests):
        with self.assertRaises(Timeout):
            get_holidays()
            mock_requests.get.assert_called_once()

    @unittest.skip
    #only works running the whole file as script!!
    def test_is_weekday(self):
        with patch("__main__.is_weekday") as mock_is_weekday:
            mock_is_weekday.return_value = False
            assert not is_weekday()
