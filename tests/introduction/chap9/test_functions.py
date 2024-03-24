import pytest

from python_playground.introduction.chap9.functions import echo, menu, menu_with_default, my_range, fibonacci_recursion, \
    get_item_by
from python_playground.introduction.chap9.things_to_do import things_to_do_9_2, things_to_do_9_2_using_yield


def test_echo():
    result = echo('hello')
    assert result == 'hello hello'


def test_menu():
    result = menu('chardonnay', 'chicken', 'cake')
    assert result == {'wine': 'chardonnay', 'entree': 'chicken', 'dessert': 'cake'}


def test_menu_default():
    result = menu_with_default('chardonnay', 'chicken')
    assert result == {'wine': 'chardonnay', 'entree': 'chicken', 'dessert': 'pudding'}


def return_what(*args):
    return args


def test_arbitrary_arguments_gather():
    target = return_what(1, 3, 5, 5, 4)
    assert target == (1, 3, 5, 5, 4)


def test_arbitrary_arguments_gather_nested():
    numbers = (1, 3, 5, 5, 4)
    target = return_what(numbers)
    assert target == ((1, 3, 5, 5, 4),)


def test_arbitrary_arguments_explode():
    numbers = (1, 3, 5, 5, 4)
    target = return_what(*numbers)
    assert target == (1, 3, 5, 5, 4)


def test_my_range():
    range_first = my_range()
    assert list(range_first) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


def test_iterate_range_twice():
    number_range = my_range()
    number_list_first = []
    for number in number_range:
        number_list_first.append(number)
    assert number_list_first == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    number_list_second = []
    for number in number_range:
        number_list_second.append(number)
    assert len(number_list_second) == 0


def test_generator_comprehension():
    generator = (combination for combination in zip(('a', 'b'), (1, 2)))
    assert tuple(generator) == (('a', 1), ('b', 2))


animal = 'cat'


def test_local_name_space():
    global animal
    id_global_animal = id(animal)
    animal = 'dog'
    id_local_animal = id(animal)
    assert id_global_animal != id_local_animal


fruit = 'apple'


def test_global_name_space():
    global fruit
    fruit = 'orange'
    assert fruit == 'orange'


color = 'blue'


def test_globals_and_locals():
    key_color = 'color'
    color = 'yellow'
    globals_animal = globals()[key_color]
    locals_animal = locals()[key_color]
    assert globals_animal == 'blue'
    assert locals_animal == 'yellow'


def test_fibonacci_recursion():
    result_0 = fibonacci_recursion(0)
    assert result_0 == 0

    result_1 = fibonacci_recursion(1)
    assert result_1 == 1

    result_2 = fibonacci_recursion(2)
    assert result_2 == 1

    result_3 = fibonacci_recursion(3)
    assert result_3 == 2


def test_fibonacci_recursion_exception():
    with pytest.raises(IndexError):
        fibonacci_recursion(-2)


def test_get_item_by():
    result = get_item_by(12)
    assert result == 0


def test_things_to_do_9_2():
    evens = things_to_do_9_2()
    assert list(evens) == [0, 2, 4, 6, 8]


def test_things_to_do_9_2_using_yield():
    evens = things_to_do_9_2_using_yield()
    assert list(evens) == [0, 2, 4, 6, 8]



