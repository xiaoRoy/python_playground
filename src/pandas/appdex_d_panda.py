import pandas as pd


def create_car_data_frame():
    data = [['Nissan', 'Stanza', 1991, 138, 4, 'MANUAL', 'sedan', 2000],
            ['Hyundai', 'Sonata', 2017, None, 4, 'AUTOMATIC', 'Sedan', 27150],
            ['Lotus', 'Elise', 2010, 218, 4, 'MANUAL', 'convertible', 54990],
            ['GMC', 'Acadia', 2017, 194, 4, 'AUTOMATIC', '4dr SUV', 34450],
            ['Nissan', 'Frontier', 2017, 261, 6, 'MANUAL', 'Pickup', 32340], ]

    column_names = ['Make', 'Model', 'Year', 'Engine HP', 'Engine Cylinders',
                    'Transmission Type', 'Vehicle_Style', 'MSRP']
    return pd.DataFrame(data, columns=column_names)


def show_car_data():
    car_df = create_car_data_frame()
    print(car_df.head(5).to_string())


if __name__ == '__main__':
    show_car_data()
