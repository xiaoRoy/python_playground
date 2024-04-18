from pandas.testing import assert_frame_equal, assert_series_equal
import pandas

from src.pandas.panda_data_frame_ultra_quick_tutorial import create_dataframe, add_column, task_one, task_one_extra


def test_create_dataframe():
    dataframe = create_dataframe()
    expected_dataframe = pandas.DataFrame({
        'temperature': [0, 10, 20, 30, 40],
        'activity': [3, 7, 9, 14, 15]
    })

    assert_frame_equal(dataframe, expected_dataframe)


def test_add_column():
    dataframe = add_column()
    expected_dataframe = pandas.DataFrame({
        'temperature': [0, 10, 20, 30, 40],
        'activity': [3, 7, 9, 14, 15],
        'adjusted': [5, 9, 11, 16, 17]
    })
    assert_frame_equal(dataframe, expected_dataframe)


def test_specify_subsets_by_head():
    dataframe = add_column()
    subset_by_head = dataframe.head(3)
    expected_dataframe = pandas.DataFrame(
        [[0, 3, 5], [10, 7, 9], [20, 9, 11]],
        index=[0, 1, 2],
        columns=['temperature', 'activity', 'adjusted'])
    assert_frame_equal(subset_by_head, expected_dataframe)


def test_specify_subset_by_index_location():
    dataframe = add_column()
    subset_by_index_location = dataframe.iloc[[2]]
    expected_dataframe = pandas.DataFrame(
        [[20, 9, 11]],
        index=[2],
        columns=['temperature', 'activity', 'adjusted']
    )
    assert_frame_equal(subset_by_index_location, expected_dataframe)


def test_specify_subset_by_slice():
    dataframe = add_column()
    subset_by_slice = dataframe[1:3]
    expected_dataframe = pandas.DataFrame(
        {'temperature': [10, 20, ],
         'activity': [7, 9, ],
         'adjusted': [9, 11, ]},
        index=[1, 2])
    assert subset_by_slice.equals(expected_dataframe)


def test_specify_subset_by_series():
    dataframe = add_column()
    subset_by_name = dataframe['temperature']
    expected_series = pandas.Series([0, 10, 20, 30, 40], name='temperature')
    assert_series_equal(subset_by_name, expected_series)


def test_task_one():
    dataframe = task_one()
    assert dataframe.size == 12
    assert list(dataframe.columns) == ['Eleanor', 'Chidi', 'Tahani', 'Jason']
    assert dataframe['Eleanor'][0]


def test_task_one_extra():
    dataframe = task_one_extra()
    expected = dataframe['Tahani'] + dataframe['Jason']
    assert dataframe['Janet'].equals(expected)


def test_copy_frame():
    dataframe = add_column()
    dataframe_copied = dataframe.copy()
    dataframe['temperature'][0] = 12
    assert not dataframe.equals(dataframe_copied)
