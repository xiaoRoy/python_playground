def things_to_do_9_2():
    evens = (number for number in range(10) if number % 2 == 0)
    return evens


def things_to_do_9_2_using_yield():
    for number in range(10):
        if number % 2 == 0:
            yield number


# things to do 9_3
def start_and_end(function):
    def echo_start_and_end(*args, **kwargs):
        print('star')
        function(*args, **kwargs)
        print('end')

    return echo_start_and_end


@start_and_end
def show_information(information):
    print(information)
