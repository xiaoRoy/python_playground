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


def test_globals_and_locals():
    key_animal = 'animal'
    animal = 'fish'
    globals_animal = globals()[key_animal]
    locals_animal = locals()[key_animal]
    assert globals_animal == 'cat'
    assert locals_animal == 'fish'

