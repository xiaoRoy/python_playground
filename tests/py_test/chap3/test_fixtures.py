import pytest


@pytest.fixture
def some_data():
    return 14


def test_some_date(some_data):
    assert some_data == 14
