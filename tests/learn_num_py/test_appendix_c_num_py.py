from numpy.testing import assert_array_equal
import numpy as np


def test_initialize_array():
    array_one = np.array([1, 2, 3, 4, 5, 6])
    first_element = array_one[0]
    assert array_one.tolist() == [1, 2, 3, 4, 5, 6]
    assert first_element == 1


def test_list_equality():
    list_one = list(range(4))
    assert [0, 1, 2, 3] == list_one


def test_array_slice():
    array_one = np.array(range(7))
    result = array_one[:3]
    expected = np.array([0, 1, 2])
    assert_array_equal(expected, result)


def test_array_slice_start():
    array_one = np.array(range(7))
    result = array_one[3:]
    expected = np.array([3, 4, 5, 6])
    assert_array_equal(expected, result)


def test_array_slice_start_end():
    array_one = np.array(range(7))
    result = array_one[2:5]
    expected = np.array([2, 3, 4])
    assert_array_equal(expected, result)


def test_array_slice_start_end_step():
    array_one = np.array(range(7))
    result = array_one[2:5:2]
    expected = np.array([2, 4])
    assert_array_equal(expected, result)


def test_array_slice_mutated():
    array_one = np.array(range(7))
    sliced_array = array_one[:6:2]
    # [0, 2, 4]
    sliced_array[2] = 44
    expected = np.array([0, 1, 2, 3, 44, 5, 6])
    assert_array_equal(expected, array_one)


def test_create_2_dimension_array():
    two_d_array = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
    expected = np.array([5, 6, 7, 8])
    assert_array_equal(expected, two_d_array[1])


def test_access_2_dimension_array():
    two_d_array = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
    element = two_d_array[1, 3]
    assert 8 == element
