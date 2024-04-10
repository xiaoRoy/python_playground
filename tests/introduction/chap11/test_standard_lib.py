from collections import defaultdict
import itertools

import pytest

from src.python_playground.introduction.chap11.standard_lib import count_food, EnhancedCounter, get_keys_as_list, \
    check_palindrome, check_palindrome_second


def get_init_periodic_table():
    return {"Hydrogen": 1, "Helium": 2}


def test_set_default():
    periodic_table = get_init_periodic_table()
    carbon = periodic_table.setdefault('Carbon', 12)
    assert periodic_table == {"Hydrogen": 1, "Helium": 2, "Carbon": 12}
    assert carbon == 12


def test_default_dict():
    periodic_table = defaultdict(lambda: -1)
    hydrogen = periodic_table['Hydrogen']
    assert hydrogen == -1
    assert 'Hydrogen' in periodic_table


def test_food_counter():
    result = count_food(['spam', 'spam', 'egg', 'apple', 'spam'])
    assert result['spam'] == 3
    assert result['apple'] == 1
    assert result['egg'] == 1


def test_enhanced_counter():
    counter = EnhancedCounter(['spam', 'spam', 'egg', 'apple', 'spam'])
    assert counter.first() == ('spam', 3)


def test_enhanced_counter_index_error():
    counter = EnhancedCounter([])
    with pytest.raises(IndexError):
        counter.first()


def test_dict_order():
    result = get_keys_as_list(get_init_periodic_table())
    assert result == ['Hydrogen', 'Helium']


def test_check_palindrome():
    assert check_palindrome('radar')
    assert not check_palindrome('word')


def test_check_palindrome_second():
    assert check_palindrome_second('radar')
    assert not check_palindrome_second('word')


def test_chain():
    result = list(itertools.chain(['a', 'b', 'c'], 'abc'))
    assert result == ['a', 'b', 'c', 'a', 'b', 'c']


def test_accumulate():
    numbers = [1, 2, 3, 4]
    result = list(itertools.accumulate(numbers))[-1]
    assert result == 10
