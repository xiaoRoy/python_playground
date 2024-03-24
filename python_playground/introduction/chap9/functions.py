def echo(anything):
    return anything + ' ' + anything


def menu(wine, entree, dessert):
    return {'wine': wine, 'entree': entree, 'dessert': dessert}


def menu_with_default(wine, entree, dessert='pudding'):
    return menu(wine, entree, dessert)


def learn_arbitrary_parameter(*args):
    print('Positional tuple:', args)


def learn_required_parameters_arbitrary_parameter(required_1, required_2, *args):
    tuple_1 = "Required#1:", required_1
    tuple_2 = ("Required#2:", required_2)
    print(tuple_1)
    print(tuple_2)
    print('All the rest:', args)


def learn_arbitrary_keyword_parameter(**keyword_parameter):
    print(keyword_parameter)


def learn_keyword_only_parameter(data, *, end, start=0, ):
    data_to_display = data[start: end]
    print(data_to_display)


def echo_with_doc_string(anything):
    """echo return its input parameter"""
    return anything


def print_if_true(thing, check):
    """
    Prints the first param thing if param check is true.
    The operation is:
    1. Check whether the param *check* is true.
    2. If it is, print the param *thing*.
    """
    if check:
        print(thing)


def print_42():
    print(42)


def run_something(func):
    func()


def display(message):
    print(message)


def run_something_with_parameter(function, message):
    function(message)


def knights(saying):
    def inner(quote):
        return "We are the knights who say '%s'" % quote

    return inner(saying)


def knights2(saying):
    def inner2():
        return "We are the knights who say '%s'" % saying

    return inner2


def edit_story(story, edit_operation):
    for word in story:
        print(edit_operation(word))


def enliven(word):
    return word.capitalize() + '!'


def my_range(first=0, last=10, step=1):
    index = first
    length = last - first
    while index < length:
        yield index
        index += step


def document_it(func):
    def new_function(*args, **kwargs):
        print("Running function:", func.__name__)
        print('Positional arguments:', args)
        print('Keyword arguments:', kwargs)
        result = func(*args, **kwargs)
        print('Result:', result)
        return result

    return new_function


def square_it(func):
    def new_function(*args, **kwargs):
        result = func(*args, **kwargs)
        return result * result

    return new_function


@document_it
@square_it
def add_ints(one, another):
    return one + another


def fibonacci_recursion(n):
    if n < 0:
        raise IndexError
    if n < 2:
        result = n
    else:
        result = fibonacci_recursion(n - 1) + fibonacci_recursion(n - 2)
    return result


def get_item_by(index):
    numbers = [1, 2, 3, 4, 7]
    try:
        result = numbers[index]
    except IndexError:
        result = 0
    except Exception:
        result = -1
    return result
