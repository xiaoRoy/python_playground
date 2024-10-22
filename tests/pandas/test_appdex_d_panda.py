import math

import numpy as np
from pandas import RangeIndex
from pandas.testing import assert_frame_equal, assert_series_equal, assert_index_equal
import pandas as pd
from src.pandas.appdex_d_panda import create_car_data_frame, create_sub_data_frame_by_series, add_column, delete_column, \
    get_sub_data_frame_by_iloc, shuffle_data_frame, Operation, get_element_wise_operation


def test_create_car_data_frame():
    actual_cars_data_frame = create_car_data_frame()
    columns = actual_cars_data_frame.columns.array
    expected_columns = ['Make', 'Model', 'Year', 'Engine HP', 'Engine Cylinders',
                        'Transmission Type', 'Vehicle Style', 'MSRP']
    assert columns == expected_columns


def test_index():
    car_df = create_car_data_frame()
    expected_index = RangeIndex(start=0, stop=5, step=1)
    assert_index_equal(car_df.index, expected_index)


def test_get_a_series_from_data_frame():
    cars_df = create_car_data_frame()
    assert_series_equal(cars_df['Make'], pd.Series(['Nissan', 'Hyundai', 'Lotus', 'GMC', 'Nissan'], name='Make'))


def test_create_sub_data_frame_by_series():
    car_sub_dataframe = create_sub_data_frame_by_series('Make')
    expected_car_series = pd.Series(['Nissan', 'Hyundai', 'Lotus', 'GMC', 'Nissan'])
    expected_car_df = pd.DataFrame(expected_car_series, columns=['Make'])
    assert_frame_equal(car_sub_dataframe, expected_car_df)


def test_add_column():
    car_df = add_column('id', ['nis1', 'hyu1', 'lot2', 'gmc1', 'nis2'])
    actual_series = car_df['id']
    expected_series = pd.Series(['nis1', 'hyu1', 'lot2', 'gmc1', 'nis2'], name='id')
    assert_series_equal(actual_series, expected_series)


def test_delete_column():
    car_df = delete_column('Vehicle Style')
    assert 'Vehicle Style' not in car_df.columns.values


def test_accessing_row_by_iloc():
    car_df = create_car_data_frame()
    first_row = car_df.iloc[0]
    expected_car_series = pd.Series(['Nissan', 'Stanza', 1991, 138.0, 4, 'MANUAL', 'sedan', 2000], name=0,
                                    index=['Make', 'Model', 'Year', 'Engine HP', 'Engine Cylinders',
                                           'Transmission Type', 'Vehicle Style', 'MSRP'])
    assert_series_equal(first_row, expected_car_series)


def test_get_sub_data_frame_by_iloc():
    car_sub_df = get_sub_data_frame_by_iloc(2, 3, 0)
    print(car_sub_df.to_string())
    data = [
        ['Lotus', 'Elise', 2010, 218, 4, 'MANUAL', 'convertible', 54990],
        ['GMC', 'Acadia', 2017, 194, 4, 'AUTOMATIC', '4dr SUV', 34450],
        ['Nissan', 'Stanza', 1991, 138, 4, 'MANUAL', 'sedan', 2000],
    ]
    column_names = ['Make', 'Model', 'Year', 'Engine HP', 'Engine Cylinders',
                    'Transmission Type', 'Vehicle Style', 'MSRP']
    dtypes = {'Engine HP': 'float64'}

    expected_car_df = pd.DataFrame(data=data, index=[2, 3, 0], columns=column_names).astype(dtypes)
    assert_frame_equal(expected_car_df, car_sub_df)


def test_shuffle_data_frame():
    shuffled_car_df = shuffle_data_frame()
    index = shuffled_car_df.index
    expected_index = pd.Index([2, 4, 1, 3, 0])
    assert_index_equal(expected_index, index)


def test_accessing_rows_by_integer_location():
    shuffled_car_df = shuffle_data_frame()
    sub_car_df = shuffled_car_df.iloc[[0, 1, 2]]
    data = [['Lotus', 'Elise', 2010, 218, 4, 'MANUAL', 'convertible', 54990],
            ['Nissan', 'Frontier', 2017, 261, 6, 'MANUAL', 'Pickup', 32340],
            ['Hyundai', 'Sonata', 2017, None, 4, 'AUTOMATIC', 'Sedan', 27150], ]
    column_names = ['Make', 'Model', 'Year', 'Engine HP', 'Engine Cylinders',
                    'Transmission Type', 'Vehicle Style', 'MSRP']
    expected_car_df = pd.DataFrame(data, columns=column_names, index=pd.Index([2, 4, 1]))
    assert_frame_equal(expected_car_df, sub_car_df)


def test_accessing_rows_by_location():
    shuffled_car_df = shuffle_data_frame()
    sub_car_df = shuffled_car_df.loc[[0, 1, 2]]
    data = [['Nissan', 'Stanza', 1991, 138, 4, 'MANUAL', 'sedan', 2000],
            ['Hyundai', 'Sonata', 2017, None, 4, 'AUTOMATIC', 'Sedan', 27150],
            ['Lotus', 'Elise', 2010, 218, 4, 'MANUAL', 'convertible', 54990], ]
    column_names = ['Make', 'Model', 'Year', 'Engine HP', 'Engine Cylinders',
                    'Transmission Type', 'Vehicle Style', 'MSRP']
    expected_car_df = pd.DataFrame(data, columns=column_names, index=pd.Index([0, 1, 2]))
    assert_frame_equal(expected_car_df, sub_car_df)


def test_rest_index():
    shuffled_car_df = shuffle_data_frame().reset_index(drop=True)
    expected_index = pd.Index(range(0, 5))
    assert_index_equal(expected_index, shuffled_car_df.index)


def test_spit_data_frame():
    n_train = 3
    n_validation = 1
    n_test = 1
    shuffled_car_df = shuffle_data_frame()
    train_car_df = shuffled_car_df[:n_train]
    training_data = [['Lotus', 'Elise', 2010, 218, 4, 'MANUAL', 'convertible', 54990],
                     ['Nissan', 'Frontier', 2017, 261, 6, 'MANUAL', 'Pickup', 32340],
                     ['Hyundai', 'Sonata', 2017, None, 4, 'AUTOMATIC', 'Sedan', 27150], ]
    column_names = ['Make', 'Model', 'Year', 'Engine HP', 'Engine Cylinders',
                    'Transmission Type', 'Vehicle Style', 'MSRP']
    expected_training_car_df = pd.DataFrame(training_data, columns=column_names, index=pd.Index([2, 4, 1]))
    assert_frame_equal(expected_training_car_df, train_car_df)

    validation_car_df = shuffled_car_df[n_train:n_train + n_validation]
    data_validation = [['GMC', 'Acadia', 2017, 194.0, 4, 'AUTOMATIC', '4dr SUV', 34450]]
    expected_car_validation_df = pd.DataFrame(data_validation, columns=column_names, index=pd.Index([3]))
    assert_frame_equal(expected_car_validation_df, validation_car_df)

    test_car_df = shuffled_car_df[n_train + n_validation:]
    data_test = [['Nissan', 'Stanza', 1991, 138.0, 4, 'MANUAL', 'sedan', 2000]]
    expected_car_test_df = pd.DataFrame(data_test, columns=column_names, index=pd.Index([0]))
    assert_frame_equal(expected_car_test_df, test_car_df)


def test_element_wise_operation_multiplication():
    car_data_frame = shuffle_data_frame()
    series_engine_hp = car_data_frame['Engine HP']
    double_engine_hp = get_element_wise_operation(Operation.MULTIPLE)(series_engine_hp, 2.0)
    expected_data = [436.0, 522.0, math.nan, 388.0, 276.0]
    expected_series = pd.Series(data=expected_data, name='Engine HP', index=[2, 4, 1, 3, 0])
    assert_series_equal(expected_series, double_engine_hp)


def test_element_wise_operation_multiplication_grater_than():
    car_data_frame = shuffle_data_frame()
    years_after_2000 = car_data_frame['Year'] > 2000
    expected_series = pd.Series([True, True, True, True, False], name='Year', index=[2, 4, 1, 3, 0])
    assert_series_equal(expected_series, years_after_2000)


def test_element_wise_operation_using_logical_operator():
    car_data_frame = shuffle_data_frame()
    result = (car_data_frame['Make'] == 'Nissan') & (car_data_frame['Year'] > 2000)

    expected = pd.Series([False, True, False, False, False], index=[2, 4, 1, 3, 0])
    assert_series_equal(expected, result)
