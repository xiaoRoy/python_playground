import numpy


def create_different_dimensions_array():
    one_dimension_array = numpy.array([1.2, 2.4, 3.5, 4.7, 6.1, 7.2, 8.3, 9.5])
    print(one_dimension_array)
    two_dimensions_array = numpy.array([[6, 5], [11, 7], [4, 8]])
    print(two_dimensions_array)


def task_two():
    feature = numpy.arange(6, 21)
    label = (feature * 3) + 4
    noise = (numpy.random.random((15,)) * 4) - 2
    label = label + noise
    print(label)


if __name__ == '__main__':
    task_two()
