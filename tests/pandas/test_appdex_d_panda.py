from pandas.testing import assert_frame_equal, assert_series_equal
import pandas as pd
from src.pandas.appdex_d_panda import create_car_data_frame


def test_create_car_data_frame():
    actual_cars_data_frame = create_car_data_frame()
    columns = actual_cars_data_frame.columns.array
    expected_columns = ['Make', 'Model', 'Year', 'Engine HP', 'Engine Cylinders',
                        'Transmission Type', 'Vehicle_Style', 'MSRP']
    assert columns == expected_columns


def test_get_a_series_from_data_frame():
    cars_df = create_car_data_frame()
    assert_series_equal(cars_df['Make'], pd.Series(['Nissan', 'Hyundai', 'Lotus', 'GMC', 'Nissan'], name='Make'))
