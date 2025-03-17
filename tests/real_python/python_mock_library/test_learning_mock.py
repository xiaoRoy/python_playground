import unittest
from unittest.mock import Mock, call, patch
from datetime import datetime
from requests.exceptions import Timeout

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
def get_holidays():
    response = requests.get("http://localhost/api/holidays")
    result = None
    if response.status_code == 200:
        result = response.json()
    return result

class TestHolidays(unittest.TestCase):

    def test_get_holidays_timeout(self):
        requests.get.side_effect = Timeout
        with self.assertRaises(Timeout):
            get_holidays()

    @staticmethod
    def log_request(url):
        print(f"Making a request to {url}")
        print("Request Received")

        response_mock = TestHolidays.mock_response()
        return response_mock

    @staticmethod
    def mock_response():
        response_mock = Mock()
        response_mock.status_code = 200
        response_mock.json.return_value = {
            "12/25": "Christmas",
            "7/4": "Independence Day",
        }
        return response_mock

    def test_get_holidays_logging(self):
        requests.get.side_effect = TestHolidays.log_request
        assert get_holidays()["12/25"] == "Christmas"

    def test_get_holidays_retry(self):
        requests.get.side_effect = [Timeout, TestHolidays.mock_response()]

        with self.assertRaises(Timeout):
            get_holidays()

        assert get_holidays()["12/25"] == "Christmas"

        assert requests.get.call_count == 2

