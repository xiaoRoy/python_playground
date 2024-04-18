import numpy
import pandas


def create_dataframe():
    data = numpy.array([[0, 3], [10, 7], [20, 9], [30, 14], [40, 15]])
    column_names = ['temperature', 'activity']

    dataframe = pandas.DataFrame(data=data, columns=column_names)
    return dataframe


def add_column():
    dataframe = create_dataframe()
    dataframe["adjusted"] = dataframe['activity'] + 2
    return dataframe


def task_one():
    data = numpy.random.randint(low=0, high=101, size=(3, 4))
    dataframe = pandas.DataFrame(data=data, columns=['Eleanor', 'Chidi', 'Tahani', 'Jason'])
    return dataframe


def task_one_extra():
    dataframe = task_one()
    dataframe['Janet'] = dataframe['Tahani'] + dataframe['Jason']
    return dataframe


if __name__ == '__main__':
    task_one()
