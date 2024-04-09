import sys

from src.real_python.modules_and_packages.learn_module_all import *
# sys.path.append('..')


def get_sys_paths():
    return sys.path


def learn_import_error():
    try:
        import not_exist
    except ImportError as import_error:
        raise import_error


def show_added_namespace(dir_list):
    for target_dir in dir_list:
        print(target_dir)


def get_imported():
    return dir()


if '__main__' == __name__:
    show_added_namespace(dir())
