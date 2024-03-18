import pytest
import copy


def test_create_dictionary_with_dict():
    customers = dict(first='wile', middle='E', last='Coyote')
    assert customers['middle'] == 'E'


def test_convert_with_dict_list_of_two_item_list():
    two_items_list = [['a', 'z'], ['b', 'y'], ['c', 'z']]
    result = dict(two_items_list)
    assert result == {'a': 'z', 'b': 'y', 'c': 'z'}


def test_convert_with_dict_list_of_two_item_tuple():
    two_items_tuple = [('a', 'z'), ('b', 'y'), ('c', 'z')]
    result = dict(two_items_tuple)
    assert result == {'a': 'z', 'b': 'y', 'c': 'z'}


def test_convert_with_dict_list_of_two_item_string():
    two_items_string = ['az', 'by', 'cz']
    result = dict(two_items_string)
    assert result == {'a': 'z', 'b': 'y', 'c': 'z'}


def test_convert_with_dict_tuple_of_two_item_list():
    two_item_list = (['a', 'z'], ['b', 'y'], ['c', 'z'])
    result = dict(two_item_list)
    assert result == {'a': 'z', 'b': 'y', 'c': 'z'}


def test_covert_with_dict_tuple_of_two_item_tuple():
    two_item_tuple = (('a', 'z'), ('b', 'y'), ('c', 'z'))
    result = dict(two_item_tuple)
    assert result == {'a': 'z', 'b': 'y', 'c': 'z'}


def test_convert_with_dict_tuple_of_two_item_string():
    two_item_string = ('az', 'by', 'cz')
    result = dict(two_item_string)
    assert result == {'a': 'z', 'b': 'y', 'c': 'z'}


def test_get_an_item_from_dict():
    letter_mapping = {'a': 'z', 'b': 'y', 'c': 'z'}
    assert letter_mapping.get('a') == 'z'
    assert letter_mapping.get('d') is None
    assert letter_mapping.get('d', 'Not Found') == 'Not Found'


def test_dict_combination():
    first = dict(a='agony', b='bliss')
    second = {'b': 'bagels', 'c': 'candy'}
    third = dict(d='donut')
    combined = {**first, **second, **third}
    assert combined == {'a': 'agony', 'b': 'bagels', 'c': 'candy', 'd': 'donut'}


def test_dict_combination_using_update():
    first = dict(a='agony', b='bliss')
    second = {'b': 'bagels', 'c': 'candy'}
    first.update(second)
    assert first == {'a': 'agony', 'b': 'bagels', 'c': 'candy', }


def test_delete_item_using_del():
    english_to_french = {'dog': 'chien', 'cat': 'chat', 'walrus': 'morse'}
    del english_to_french['dog']
    assert english_to_french == {'cat': 'chat', 'walrus': 'morse'}


def test_pop_without_key():
    with pytest.raises(KeyError):
        english_to_french = {'dog': 'chien', 'cat': 'chat', 'walrus': 'morse'}
        english_to_french.pop('not exist')


def test_pop_default():
    english_to_french = {'dog': 'chien', 'cat': 'chat', 'walrus': 'morse'}
    assert english_to_french.pop('not exist', 'default') == 'default'


def test_clear_dict():
    english_to_french = {'dog': 'chien', 'cat': 'chat', 'walrus': 'morse'}
    english_to_french.clear()
    assert len(english_to_french) == 0


def test_copy_dictionary():
    signals = {'red': 'smile for the camera', 'green': 'go', 'yellow': 'go faster'}
    signals_copied = signals.copy()
    signals_copied['red'] = 'lucky'
    assert signals['red'] == 'smile for the camera'
    assert signals_copied['red'] == 'lucky'


def test_deep_copy_dictionary():
    all_kinds = {
        'fruit': ['apple', 'pear', 'orange', ],
        'animal': ['cat', 'dog', 'tiger', 'horse'],
        'drink': ['coffee', 'juice', 'beer']
    }

    all_kinds_copy = all_kinds.copy()
    all_kinds_deep_copy = copy.deepcopy(all_kinds)
    all_kinds['animal'].append('monkey')
    assert all_kinds_copy['animal'] == ['cat', 'dog', 'tiger', 'horse', 'monkey']
    assert all_kinds_deep_copy['animal'] == ['cat', 'dog', 'tiger', 'horse']


def test_create_dictionary_with_comprehensions():
    word = 'letters'
    letter_count = {letter: word.count(letter) for letter in word}
    assert letter_count == {'l': 1, 'e': 2, 't': 2, 'r': 1, 's': 1}


def test_create_dictionary_with_comprehensions_second():
    word = 'letters'
    letter_count = {letter: word.count(letter) for letter in set(word)}
    assert letter_count == {'l': 1, 'e': 2, 't': 2, 'r': 1, 's': 1}


def test_create_dictionary_with_comprehensions_with_if_condition():
    vowels = 'aeiou'
    word = 'onmatopoeia'
    vowel_count = {letter: word.count(letter) for letter in set(word) if letter in vowels}
    assert vowel_count == {'a': 2, 'e': 1, 'i': 1, 'o': 3}


def test_create_dictionary():
    english_to_french = {'dog': 'chien', 'cat': 'chat', 'walrus': 'morse'}
    assert english_to_french['dog'] == 'chien'


def test_swap_key_value_dictionary():
    english_to_french = {'dog': 'chien', 'cat': 'chat', 'walrus': 'morse'}
    french_to_english = {}
    for english, french in english_to_french.items():
        french_to_english[french] = english
    assert french_to_english == {'chien': 'dog', 'chat': 'cat', 'morse': 'walrus'}
    assert french_to_english.keys() == {'chien', 'chat', 'morse'}
    assert list(french_to_english.values()) == ['dog', 'cat', 'walrus']
