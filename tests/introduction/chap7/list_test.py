import copy


def test_create_empty_list():
    empty_list = []
    assert len(empty_list) == 0


def test_create_list_with_function_list():
    cat_letters = list('cat')
    assert cat_letters == ['c', 'a', 't']

    cat_list_by_tuple = list(('cat',))
    assert cat_list_by_tuple == ['cat']


def test_list_slice():
    names = ['Groucho', 'Chico', 'Harpo']
    assert names[::-2] == ['Harpo', 'Groucho']


def test_list_slice_negative_start_negative_stop():
    names = ['Groucho', 'Chico', 'Harpo']
    assert names[-6:] == ['Groucho', 'Chico', 'Harpo']
    assert names[-6:-2] == ['Groucho']
    assert names[-6:-4] == []


def test_list_slice_negative_start_negative_stop_vowel():
    vowel_letters = 'aeiou'
    assert vowel_letters[-6:] == 'aeiou'
    assert vowel_letters[-999:] == 'aeiou'

    assert vowel_letters[-100:-4] == 'a'
    assert vowel_letters[-100:-5] == ''


def test_add_item_with_offset():
    fruits = ['apple', 'pear', 'peach', 'orange']
    fruits.insert(2, 'cherry')
    assert fruits[2] == 'cherry'


def test_duplicate_list():
    letters = ['a', 'b', 'c'] * 3
    assert len(letters) == 9


def test_combine_list():
    countries = ['China', 'Canada', 'Mexico']
    others = ['Japan', 'France', 'Span']
    countries.extend(others)
    assert len(countries) == 6


def test_combine_list_using_add():
    countries = ['China', 'Canada', 'Mexico']
    others = ['Japan', 'France', 'Span']
    countries += others
    assert len(countries) == 6


def test_append_different_types_in_list():
    countries = ['China', 'Canada', 'Mexico']
    others = ['Japan', 'France', 'Span']
    countries.append(others)
    assert countries == ['China', 'Canada', 'Mexico', ['Japan', 'France', 'Span']]


def test_chang_items_with_slice():
    numbers = [1, 2, 3, 4]
    numbers[1:3] = [8, 9]
    assert numbers == [1, 8, 9, 4]


def test_chang_items_with_slice_tuple():
    numbers = [1, 2, 3, 5]
    numbers[2:] = (7, 9, 11)
    assert numbers == [1, 2, 7, 9, 11]


def test_chang_items_with_slice_string():
    letters = ['a', 'e', 'k', 'j']
    letters[0:2] = 'love'
    assert letters == ['l', 'o', 'v', 'e', 'k', 'j']


def test_delete_item_with_del():
    names = ['smith', 'jack', 'black']
    del names[1]
    assert names == ['smith', 'black']


def test_delete_itme_with_remove():
    names = ['smith', 'jack', 'black']
    names.remove('jack')
    assert names == ['smith', 'black']


def test_delete_item_with_pop():
    names = ['smith', 'jack', 'black']
    last = names.pop()
    assert last == 'black'
    assert names == ['smith', 'jack']


def test_delete_item_with_pop_offset():
    names = ['smith', 'jack', 'black']
    name_jack = names.pop(1)
    assert name_jack == 'jack'
    assert names == ['smith', 'black']


def test_delete_all_items():
    names = ['smith', 'jack', 'black']
    names.clear()
    assert len(names) == 0


def test_find_items():
    names = ['smith', 'jack', 'black']
    index_smith = names.index('jack')
    assert index_smith == 1


def test_check_item_existence():
    names = ['smith', 'jack', 'black']
    assert 'black' in names


def test_occurrence():
    numbers = [1, 3, 7, 0, 2, 6, 1, 6, 3, 1, 4]
    assert numbers.count(1) == 3


def test_join():
    friends = ['Harry', 'Hermione', 'Ron']
    seperator = ' * '
    assert seperator.join(friends) == 'Harry * Hermione * Ron'


def test_sort_using_sorted():
    numbers = [2, 12, 41, 22]
    numbers_sorted = sorted(numbers)
    assert numbers == [2, 12, 41, 22]
    assert numbers_sorted == [2, 12, 22, 41]


def test_sort_using_sort():
    numbers = [2, 12, 41, 22]
    numbers.sort()
    assert numbers == [2, 12, 22, 41]


def test_copy_using_list():
    numbers = [2, 12, 41, 22]
    numbers_copied = list(numbers)
    assert numbers == numbers_copied


def test_copy_using_copy():
    numbers = [2, 12, 41, 22]
    numbers_copied = numbers.copy()
    assert numbers == numbers_copied


def test_copy_using_slice():
    numbers = [2, 12, 41, 22]
    numbers_copied = numbers[:]
    assert numbers == numbers_copied


def test_shallow_copy():
    numbers = [1, 2, [24, 34]]
    numbers_copied = numbers.copy()
    numbers[2][1] = 44
    assert numbers == [1, 2, [24, 44]]
    assert numbers_copied == [1, 2, [24, 44]]


def test_deep_copy():
    numbers = [1, 2, [24, 34]]
    numbers_copied = copy.deepcopy(numbers)
    numbers[2][1] = 44
    assert numbers == [1, 2, [24, 44]]
    assert numbers_copied == [1, 2, [24, 34]]


def test_zip():
    days_in_english = ['Monday', 'Tuesday', 'Wednesday']
    days_in_french = ['Lundi', 'Mardi', 'Mercredi']
    zipped = zip(days_in_english, days_in_french)
    zipped_list = list(zipped)
    first = zipped_list[0]
    assert isinstance(first, tuple)
    assert zipped_list == [('Monday', 'Lundi'), ('Tuesday', 'Mardi'), ('Wednesday', 'Mercredi')]


def test_create_list_with_comprehension():
    numbers = [number for number in range(1, 6)]
    assert numbers == [1, 2, 3, 4, 5]

    numbers_second = [number * number for number in range(0, 4)]
    assert numbers_second == [0, 1, 4, 9]


def test_create_list_with_comprehension_with_if():
    numbers = [number for number in range(1, 6) if number % 2 == 1]
    assert numbers == [1, 3, 5]


def test_create_list_with_comprehension_with_nested_for():
    rows = range(1, 4)
    columns = range(1, 3)
    cells = [(row, column) for row in rows for column in columns]
    assert cells == [(1, 1), (1, 2), (2, 1), (2, 2), (3, 1), (3, 2)]


def test_things_to_do_7_1():
    initial = 1987
    assert list(range(initial, initial + 5)) == [1987, 1988, 1989, 1990, 1991]


def test_things_to_do_7_10():
    surprise = ['Groucho', 'Chico', 'Harpo']
    assert surprise[-1][::-1] == 'opraH'

