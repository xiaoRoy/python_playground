from datetime import datetime

import requests


def is_weekday():
    today = datetime.today()
    day_in_weekday = today.weekday()
    return 0 <= day_in_weekday < 5


wednesday = datetime(year=2025, month=1, day=1)


def get_holidays():
    response = requests.get("http://localhost/api/holidays")
    result = None
    if response.status_code == 200:
        result = response.json()
    return result
