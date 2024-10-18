from pandas.testing import assert_frame_equal, assert_series_equal
import pandas as pd
from src.pandas.appdex_d_panda import create_car_data_frame, create_sub_data_frame_by_series, add_column, delete_column


def test_create_car_data_frame():
    actual_cars_data_frame = create_car_data_frame()
    columns = actual_cars_data_frame.columns.array
    expected_columns = ['Make', 'Model', 'Year', 'Engine HP', 'Engine Cylinders',
                        'Transmission Type', 'Vehicle Style', 'MSRP']
    assert columns == expected_columns


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
