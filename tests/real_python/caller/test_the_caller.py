from src.real_python.caller.the_caller import show_package_initialization
from src.real_python.modules_and_packages.module_example import Apple


def test_show_package_initialization():
    apple = show_package_initialization()
    assert isinstance(apple, Apple)
