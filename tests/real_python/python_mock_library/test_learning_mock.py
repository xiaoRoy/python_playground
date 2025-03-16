import unittest
from unittest.mock import Mock, call, patch
from datetime import datetime
from requests.exceptions import Timeout

import pytest

from src.real_python.python_mock_library.learning_mock import get_holidays


def mock_json():
    json = Mock()
    json.loads('{"name": "smith"}')
    return json


def test_json_loads():
    mocked_json = mock_json()
    assert 1 == mocked_json.loads.call_count
    assert mocked_json.loads.call_args == call('{"name": "smith"}')


# def test_mock_weekday():
#     with patch('src.real_python.python_mock_library.learning_mock.datetime') as mock_datetime:
#         mock_datetime.today.return_value = wednesday
#         assert is_weekday()


# Save a couple of test days
wednesday = datetime(year=2025, month=1, day=1)
sunday = datetime(year=2025, month=1, day=5)

# Mock datetime to control today's date
datetime = Mock()


def is_weekday():
    today = datetime.today()
    # Python's datetime library treats Monday as 0 and Sunday as 6
    return 0 <= today.weekday() < 5


# Mock .today() to return Wednesday
datetime.today.return_value = wednesday
# Test Wednesday is a weekday
assert is_weekday()

# Mock .today() to return Sunday
datetime.today.return_value = sunday
# Test Sunday is not a weekday
assert not is_weekday()


# def test_get_holidays_time_out():
#     requests = Mock()
#     requests.get.side_effect = Timeout
#     with unittest.TestCase.assertRaises(Timeout):
requests = Mock()
class TestHolidays(unittest.TestCase):
    def test_get_holidays_timeout(self):

        requests.get.side_effect = Timeout
        with self.assertRaises(Timeout):
            get_holidays()
