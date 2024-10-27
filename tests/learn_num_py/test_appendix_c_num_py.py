from array import array

import numpy
from numpy.testing import assert_array_equal
import numpy as np
from src.learn_num_py.appendix_c_num_py import create_two_dimension_array


def test_create_array_full():
    array_one = np.full(5, 0.1)
    expected = np.array([0.1, 0.1, 0.1, 0.1, 0.1])
    assert_array_equal(array_one, expected)


def test_create_array_repeat():
    array_one = np.repeat([0, 1], 3)
    expected = np.array([0, 0, 0, 1, 1, 1])
    assert_array_equal(expected, array_one)


def test_create_array_repeat_repetitions():
    array_one = np.repeat([0, 1], [2, 4])
    expected = np.array([0, 0, 1, 1, 1, 1])
    assert_array_equal(expected, array_one)


def test_access_array_multiple_index():
    array_one = np.arange(7)
    result = array_one[[0, 2, 4]]
    expected = np.array([0, 2, 4])
    assert_array_equal(expected, result)


def test_create_two_dimension_array():
    array_one = np.zeros((2, 3), dtype=np.float32)
    expected_data = [[0., 0., 0.],
                     [0., 0., 0.], ]
    expected = np.array(expected_data, dtype=np.float32)
    assert_array_equal(expected, array_one)


def test_access_two_dimension_array():
    array_one = create_two_dimension_array()
    second_element = array_one[1]
    expected = np.arange(5, 9)
    assert_array_equal(expected, second_element)


def test_selecting_all_rows_one_column():
    numbers = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
    ]

    array_one = np.array(numbers)
    second_column = array_one[:, 1]
    expected = np.array([2, 5, 8])
    assert_array_equal(expected, second_column)


def test_random_generate_array():
    np.random.seed(2)
    array_one = np.random.rand(5, 2)
    row = 5
    column = 2
    assert (row, column) == array_one.shape


def test_random_generate_array_between():
    np.random.seed(2)
    array_one = np.random.randint(low=0, high=100, size=(5, 2))
    assert np.all(array_one >= 0) & np.all(array_one < 100)
