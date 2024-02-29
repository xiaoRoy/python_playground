from python_playground.introduction.chap9.functions import echo, menu, menu_with_default, my_range


def test_echo():
    result = echo('hello')
    assert result == 'hello hello'


def test_menu():
    result = menu('chardonnay', 'chicken', 'cake')
    assert result == {'wine': 'chardonnay', 'entree': 'chicken', 'dessert': 'cake'}


def test_menu_default():
    result = menu_with_default('chardonnay', 'chicken')
    assert result == {'wine': 'chardonnay', 'entree': 'chicken', 'dessert': 'pudding'}


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
