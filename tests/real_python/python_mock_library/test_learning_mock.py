import unittest
from unittest.mock import Mock, call, patch
from datetime import datetime
from requests.exceptions import Timeout

from src.real_python.python_mock_library.learning_mock import is_weekday, get_holidays


def mock_json():
    json = Mock()
    json.loads('{"name": "smith"}')
    return json


def test_json_loads():
    mocked_json = mock_json()
    assert 1 == mocked_json.loads.call_count
    assert mocked_json.loads.call_args == call('{"name": "smith"}')



class TestWeekDay(unittest.TestCase):
    learning_mock_module_datetime = "src.real_python.python_mock_library.learning_mock.datetime"

    @patch(learning_mock_module_datetime)
    def test_weekday(self, mock_datetime):
        wednesday = datetime(year=2025, month=1, day=1)
        mock_datetime.today.return_value = wednesday
        assert is_weekday()

    @patch(learning_mock_module_datetime)
    def test_not_weekday(self, mock_datetime):
        sunday = datetime(year=2025, month=1, day=5)
        mock_datetime.today.return_value = sunday
        assert not is_weekday()


class TestHolidays(unittest.TestCase):
    learning_mock_module_request = "src.real_python.python_mock_library.learning_mock.requests"

    def test_get_holidays_timeout(self):
        with patch(TestHolidays.learning_mock_module_request) as mock_requests:
            mock_requests.get.side_effect = Timeout
            with self.assertRaises(Timeout):
                get_holidays()
                mock_requests.get.assert_called_once()

    def test_get_holidays_timeout_using_patch_object(self):
        with patch(TestHolidays.learning_mock_module_request) as mock_requests:
            mock_requests.get.side_effect = Timeout
            with self.assertRaises(Timeout):
                get_holidays()
                mock_requests.get.assert_called_once()

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
        with patch(TestHolidays.learning_mock_module_request) as mock_request:
            mock_request.get.side_effect = TestHolidays.log_request
            assert get_holidays()["12/25"] == "Christmas"

    def test_get_holidays_retry(self):
        with patch(TestHolidays.learning_mock_module_request) as mock_request:
            mock_request.get.side_effect = [Timeout, TestHolidays.mock_response()]

            with self.assertRaises(Timeout):
                get_holidays()

            assert get_holidays()["12/25"] == "Christmas"

            assert mock_request.get.call_count == 2
