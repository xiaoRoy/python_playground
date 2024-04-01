import types

from python_playground.introduction.chap11.choices.advice import answers
from python_playground.introduction.chap11.choices.fast_food_picker import restaurants
from python_playground.introduction.chap11.questions import give_advice
from python_playground.introduction.chap11.time_to_lunch import pick_lunch, show_module, pick_lunch_second, \
    pick_lunch_third


def test_time_to_lunch():
    target = pick_lunch()
    assert target in restaurants


def test_time_to_lunch_second():
    target = pick_lunch_second()
    assert target in restaurants


def test_time_to_lunch_third():
    target = pick_lunch_third()
    assert target in restaurants


def test_show_module():
    target_module = show_module()
    assert isinstance(target_module, types.ModuleType)


def test_give_advice():
    advice = give_advice()
    assert advice in answers
