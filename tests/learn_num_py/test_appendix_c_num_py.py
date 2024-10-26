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
