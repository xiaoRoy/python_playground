import numpy
from numpy.testing import assert_array_equal
import numpy as np
from src.learn_num_py.appendix_c_num_py import create_two_dimension_array


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
    two_d_array = create_two_dimension_array()
    expected = np.array([5, 6, 7, 8])
    assert_array_equal(expected, two_d_array[1])


def test_access_2_dimension_array():
    two_d_array = create_two_dimension_array()
    element = two_d_array[1, 3]
    assert 8 == element


def test_array_attribute_number_of_dimension():
    two_d_array = create_two_dimension_array()
    assert 2 == two_d_array.ndim


def test_array_attribute_shape():
    two_d_array = create_two_dimension_array()
    (num_dim, num_elements) = two_d_array.shape
    assert 3 == num_dim
    assert 4 == num_elements


def test_array_attribute_size():
    two_d_array = create_two_dimension_array()
    assert 12 == two_d_array.size


def test_array_attribute_data_type():
    two_d_array = create_two_dimension_array()
    assert numpy.int64 == two_d_array.dtype


def test_create_array_zeros():
    zero_array = np.zeros(3)
    expected = np.array([0, 0, 0])
    assert_array_equal(expected, zero_array)


def test_create_array_ones():
    one_array = np.ones(4)
    expected = np.array([1, 1, 1, 1])
    assert_array_equal(expected, one_array)


def test_create_array_empty():
    empty_array = np.empty(2)
    assert empty_array.size == 2


def test_create_array_range():
    array_one = np.array(np.arange(4))
    expected = np.array([0, 1, 2, 3])
    assert_array_equal(expected, array_one)


def test_create_array_range_start_stop_step():
    array_one = np.array(np.arange(0, 9, 2))
    expected = np.array([0, 2, 4, 6, 8])
    assert_array_equal(expected, array_one)


def test_create_array_linear_space():
    array_one = np.linspace(1.0, 10.0, num=5)

    # (10.0 - 1.0) / 4 = 2.25
    expected_one = np.array([1., 3.25, 5.5, 7.75, 10.])
    assert_array_equal(expected_one, array_one)

    array_two = np.linspace(1.0, 10.0, num=5, endpoint=False)
    # (10.0 - 1.0) / 5 = 1.8
    expected_two = np.array([1., 2.8, 4.6, 6.4, 8.2])
    assert_array_equal(expected_two, array_two)


def test_specify_data_type():
    array_one = np.ones(3, dtype=np.int64)
    assert numpy.int64 == array_one.dtype


def test_element_wise_operation_multiplication():
    array_one = np.arange(5)
    result = array_one * 2
    expected = np.arange(0, 10, 2)
    assert_array_equal(expected, result)


def test_element_wise_operation_array_and_array():
    noise = 0.01 * np.random.rand(5)
    numbers = np.arange(5)
    result = noise + numbers
    assert (5,) == result.shape


def test_element_wise_operation_array_and_array_power():
    numbers = np.arange(6)
    result = numbers ** 3
    expected = np.array([0, 1, 8, 27, 64, 125])
    assert_array_equal(expected, result)


def test_element_wise_operation_boolean_comparison():
    number_array = np.array([3, 2, 1, 14, 8])
    result = number_array > 0
    expected = np.repeat(True, 5)
    assert_array_equal(expected, result)


def test_element_wise_operation_boolean_comparison_array_and_array():
    array_one = np.array([1, 2, 3])
    array_two = np.array([4, 5, 6])
    result = array_one < array_two
    expected = np.repeat(True, 3)
    assert_array_equal(expected, result)


def test_element_wise_operation_logical_array_and_array():
    array_one = np.array([2, 4, 6])
    array_two = np.array([1, 3, 5])
    is_even_one = array_one % 2 == 0
    is_even_two = array_two % 2 == 0
    is_all_even = is_even_one & is_even_two
    result = np.all(is_all_even)
    assert not result


def test_summarizing_operations():
    array_one = np.arange(1, 11)
    sum_array = array_one.sum()
    assert 55 == sum_array
    assert 1 == array_one.min()
    assert 10 == array_one.max()
    assert 5.5 == array_one.mean()


def create_2d_array():
    return np.array([
        [0, 1, 2, 3],
        [4, 5, 6, 7],
        [8, 9, 19, 11],
    ])


def test_summarizing_operations_2d_array():
    array_one = create_2d_array()

    assert 19 == array_one.max()


def test_summarizing_operations_axis():
    array_one = create_2d_array()
    maximum_in_each_column = array_one.max(axis=0)
    maximum_in_each_row = array_one.max(axis=1)

    expected_in_column = np.array([8, 9, 19, 11])
    expected_in_row = np.array([3, 7, 19])
    assert_array_equal(expected_in_column, maximum_in_each_column)
    assert_array_equal(expected_in_row, maximum_in_each_row)


def test_summarizing_operations_axis_sum():
    array_one = create_2d_array()
    sum_in_each_column = array_one.sum(axis=0)
    sum_in_each_row = array_one.sum(axis=1)

    expected_sum_in_each_column = np.array([12, 15, 27, 21])
    expected_sum_in_each_row = np.array([6, 22, 47])

    assert_array_equal(expected_sum_in_each_row, sum_in_each_row)
    assert_array_equal(expected_sum_in_each_column, sum_in_each_column)


def create_array_to_sort():
    return np.array([2, 95, 21, 7, 22, 44, 14, 8])


def test_sorting():
    origin_array = create_array_to_sort()
    origin_array.sort()
    expected_sorted_array = np.array([2, 7, 8, 14, 21, 22, 44, 95])
    assert_array_equal(expected_sorted_array, origin_array)


def test_sorting_copy():
    origin_array = create_array_to_sort()
    assert (2 == origin_array[0]) & (8 == origin_array[7])

    sorted_array = np.sort(origin_array)
    expected_sorted_array = np.array([2, 7, 8, 14, 21, 22, 44, 95])

    assert_array_equal(expected_sorted_array, sorted_array)


def test_sorting_arg_sort():
    origin_array = create_array_to_sort()
    sorted_index = origin_array.argsort()

    expected_sorted_index = np.array([0, 3, 7, 6, 2, 4, 5, 1])
    assert_array_equal(expected_sorted_index, sorted_index)

    expected_sorted_array = np.array([2, 7, 8, 14, 21, 22, 44, 95])
    assert_array_equal(origin_array[expected_sorted_index], expected_sorted_array)


def test_advancing_indexing():
    array_one = np.arange(9, step=2)
    result = array_one[(2, 3, 4),]
    expected = np.array([4, 6, 8])
    assert_array_equal(expected, result)


