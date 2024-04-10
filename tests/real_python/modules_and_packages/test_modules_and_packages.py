import pytest

from unittest.mock import MagicMock
from src.real_python.modules_and_packages import *


def test_import_error():
    with pytest.raises(ImportError):
        learn_module.learn_import_error()


def test_main():
    learn_module.show_added_namespace = MagicMock()
    learn_module.show_added_namespace.assert_not_called()


# The code in __init__.py is not invoked.
def test_init_package():
    import src.real_python.modules_and_packages as modules_and_packages
    print(modules_and_packages.color)
    assert True


def test_all_in_module():
    imported = dir(learn_module)
    assert 'Pear' not in imported
    assert 'Cat' in imported


def test_all_in_package():
    import src.real_python.modules_and_packages as modules_and_packages
    imported = dir(modules_and_packages)
    assert 'learn_module' in imported
    assert 'module_example' in imported
