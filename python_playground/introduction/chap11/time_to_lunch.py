# from python_playground.introduction.chap11 import fast_food_picker
from python_playground.introduction.chap11.choices import fast_food_picker
import sys


# from . import fast_food_picker


def pick_lunch():
    return fast_food_picker.pick()


def show_module():
    return sys.modules['python_playground.introduction.chap11.choices.fast_food_picker']


def pick_lunch_second():
    from choices import fast_food_picker as picker
    return picker.pick()


def pick_lunch_third():
    from choices.fast_food_picker import pick
    return pick()
