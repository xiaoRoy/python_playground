def test_empty_tuple():
    assert len(()) == 0


def test_create_single_tuple():
    assert len(('Smith',)) == 1
    assert isinstance(('Smith'), str)
    assert isinstance(('Smith',), tuple)


def test_create_a_tuple_with_multiple_items():
    one = 3, 5, 6
    another = (3, 5, 6)
    assert one == another


def test_swap_with_tuple():
    one, another = 'one', 'another'
    one, another = another, one
    assert one == 'another'
    assert another == 'one'


def test_create_with_function_tuple():
    number_tuple = tuple([1, 2, 4])
    assert number_tuple == (1, 2, 4)


def test_combine_tuple_using_plus():
    one = (0, 8, 14)
    another = (0, 9, 11)
    assert one + another == (0, 8, 14, 0, 9, 11)


def test_tuple_multiplication():
    messages = 'love',
    assert messages * 3 == ('love', 'love', 'love')


def test_tuple_id():
    one = 'test', 'one'
    another = 'another',
    another_id = id(another)
    another += one
    another_new_id = id(another)
    assert another_id != another_new_id

