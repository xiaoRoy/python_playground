import pandas as pd
import numpy as np

pd.set_option('display.max_rows', None)  # Show all rows
pd.set_option('display.max_columns', None)  # Show all columns


def create_car_data_frame():
    data = [['Nissan', 'Stanza', 1991, 138, 4, 'MANUAL', 'sedan', 2000],
            ['Hyundai', 'Sonata', 2017, None, 4, 'AUTOMATIC', 'Sedan', 27150],
            ['Lotus', 'Elise', 2010, 218, 4, 'MANUAL', 'convertible', 54990],
            ['GMC', 'Acadia', 2017, 194, 4, 'AUTOMATIC', '4dr SUV', 34450],
            ['Nissan', 'Frontier', 2017, 261, 6, 'MANUAL', 'Pickup', 32340], ]

    column_names = ['Make', 'Model', 'Year', 'Engine HP', 'Engine Cylinders',
                    'Transmission Type', 'Vehicle Style', 'MSRP']
    return pd.DataFrame(data, columns=column_names)


def shuffle_data_frame():
    index = np.arange(5)
    np.random.seed(2)
    np.random.shuffle(index)
    car_df = create_car_data_frame()
    return car_df.iloc[index]


def create_sub_data_frame_by_series(*columns):
    car_df = create_car_data_frame()
    columns_list = list(columns)
    return car_df[columns_list]


def add_column(column_name, column):
    car_df = create_car_data_frame()
    series = pd.Series(column, name=column_name)
    car_df[column_name] = series
    return car_df


def delete_column(column_name):
    car_df = create_car_data_frame()
    del car_df[column_name]
    return car_df


def get_sub_data_frame_by_iloc(*index_locations):
    car_df = create_car_data_frame()
    print(list(index_locations))
    return car_df.iloc[list(index_locations)]


def show_car_data():
    car_df = create_car_data_frame()
    print(car_df.head(5).to_string())


if __name__ == '__main__':
    shuffle_data_frame()
