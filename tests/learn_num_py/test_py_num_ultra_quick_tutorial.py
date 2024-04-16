import numpy


def test_populate_array_with_sequence_of_numbers():
    sequence_of_integers = numpy.arange(5, 12)
    print(sequence_of_integers)
    expected = numpy.array([5, 6, 7, 8, 9, 10, 11])
    assert numpy.array_equal(sequence_of_integers, expected)


def test_populate_arrays_with_random_numbers():
    random_integers_between_50_and_100 = numpy.random.randint(low=50, high=101, size=(6,))
    assert random_integers_between_50_and_100.size == 6
    assert not any(number < 50 or number > 101 for number in random_integers_between_50_and_100)


def test_populate_arrays_with_random_float_numbers():
    random_numbers_between_0_and_1 = numpy.random.random((4,))
    assert random_numbers_between_0_and_1.size == 4
    assert any(0.0 <= number < 1.0 for number in random_numbers_between_0_and_1)


def test_task_one():
    feature = numpy.arange(6, 21)
    label = (feature * 3) + 4
    expected = numpy.array(list((number * 3 + 4) for number in range(6, 21)))
    assert numpy.array_equal(label, expected)


def test_task_two():
    feature = numpy.arange(6, 21)
    label = (feature * 3) + 4
    noise = (numpy.random.random((15,)) * 4) - 2
    label = label + noise
    print(noise)
