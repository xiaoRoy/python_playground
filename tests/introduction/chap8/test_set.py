import pytest


def test_create_empty_set():
    empty_dict = {}
    assert isinstance(empty_dict, dict)
    empty_set = set()
    assert isinstance(empty_set, set)
    assert len(empty_set) == 0


def test_convert_string_to_set():
    assert set('letter') == {'l', 'e', 't', 'r'}


def test_covert_list_to_set():
    letter = ['l', 'e', 't', 't', 'e', 'r']
    assert set(letter) == {'l', 'e', 't', 'r'}


def test_covert_tuple_to_set():
    letter_tuple = ('l', 'e', 't', 't', 'e', 'r')
    assert set(letter_tuple) == {'l', 'e', 't', 'r'}


def test_covert_dictionary_to_set():
    color_dictionary = dict(apple='red', orange='orange', cheery='red')
    assert set(color_dictionary) == {'apple', 'orange', 'cheery'}


numbers_a = {1, 2}
numbers_b = {1, 3}


def test_intersection():
    assert numbers_a & numbers_b == {1}
    assert numbers_a.intersection(numbers_b) == {1}


def test_union():
    assert numbers_a | numbers_b == {1, 2, 3}
    assert numbers_a.union(numbers_b) == {1, 2, 3}


def test_difference():
    assert numbers_a - numbers_b == {2}
    assert numbers_a.difference(numbers_b) == {2}


def test_exclusive():
    assert numbers_a ^ numbers_b == {2, 3}
    assert numbers_a.symmetric_difference(numbers_b) == {2, 3}


def test_is_subset():
    assert not numbers_a.issubset(numbers_b)
    assert not numbers_a <= numbers_b


def test_is_proper_subset():
    letters_a = {'a', 'b', 'c', 'd'}
    letters_b = {'a', 'd'}
    letters_c = {'a', 'b', 'c', 'd'}
    assert letters_b < letters_a
    assert not letters_c < letters_a


def test_is_superset():
    letters_a = {'a', 'b', 'c', 'd'}
    letters_b = {'a', 'd'}
    assert letters_a >= letters_b
    assert letters_a.issuperset(letters_b)


def test_is_proper_superset():
    letters_a = {'a', 'b', 'c', 'd'}
    letters_b = {'a', 'd'}
    letters_d = {'a', 'b', 'c', 'd'}
    assert letters_a > letters_b
    assert not letters_a > letters_d


def test_set_comprehension():
    even_set = {number for number in range(0, 10) if number % 2 == 0}
    assert even_set == {0, 2, 4, 6, 8}


def test_frozen_set():
    numbers = frozenset([2, 1, 4, 5])
    with pytest.raises(AttributeError):
        numbers.add(2)


def test_things_to_do_8_10():
    squares = {number: number * number for number in range(10)}
    assert squares == {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}


def test_things_to_do_8_11():
    odd_numbers = {number for number in range(10) if number % 2 != 0}
    assert odd_numbers == {1, 3, 5, 7, 9}


def test_things_to_do_8_12():
    glasses_type = ('optimist', 'pessimist', 'troll')
    glasses_description = ('The glass is half full', 'The glass is half empty', 'How did you get a glass?')
    glasses = dict(zip(glasses_type, glasses_description))
    assert glasses.keys() == set(glasses_type)
    assert list(glasses.values()) == ['The glass is half full', 'The glass is half empty', 'How did you get a glass?']


def test_things_to_do_8_13():
    movie_titles = ['Creature of Habit', 'Crewel Fate', 'Sharks On a Plane']
    movie_plots = ['A nun turns into a monster', 'A haunted yarn shop', 'Check your exits']
    movies = dict(zip(movie_titles, movie_plots))
    assert movies['Creature of Habit'] == 'A nun turns into a monster'
    assert movies['Crewel Fate'] == 'A haunted yarn shop'
    assert movies['Sharks On a Plane'] == 'Check your exits'
