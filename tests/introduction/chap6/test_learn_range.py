from python_playground.introduction.chap6.learn_range import create_number_list


def test_create_range():
    num_list = create_number_list(stop=10)
    assert num_list == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


def test_create_range_step():
    numbers = create_number_list(stop=10, start=2, step=2)
    assert numbers == [2, 4, 6, 8]


def test_create_range_negative_step():
    numbers = create_number_list(stop=-2, start=0, step=-1)
    assert numbers == [0, -1]


def test_create_range_negative_step_empty():
    numbers = create_number_list(stop=10, start=2, step=-1)
    assert len(numbers) == 0
