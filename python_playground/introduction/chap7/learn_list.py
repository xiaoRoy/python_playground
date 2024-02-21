def learn_for_loop_break():
    cheeses = ['brie', 'gjetost', 'havarti', 'x']
    for cheese in cheeses:
        if cheese.startswith('x'):
            print(f'This {cheese} starts with x')
            break
        else:
            print(cheese)
    else:
        print('Not Found')


def learn_zip():
    days = ['Monday', 'Tuesday', 'Wednesday']
    fruits = ['banana', 'orange', 'peach']
    drinks = ['coffee', 'tea', 'beer']
    desserts = ['tiramisu', 'ice cream', 'pie', 'pudding']

    for day, fruit, drink, dessert in zip(days, fruits, drinks, desserts):
        # what is type to tuple
        what = day, ': drink', drink, '- eat', fruit, '- enjoy', dessert
        print(what)


def things_to_do_7_5():
    things = ['mozzarella', 'cinderella', 'salmonella']
    for thing in things:
        print(thing.capitalize())


def things_to_do_7_11():
    start1 = ['fee', 'fie', 'foe']
    rhymes = [
        ('flop', 'get a mop'),
        ('fope', 'turn the rope'),
        ('fa', 'get your ma'),
        ('fudge', 'call the judge'),
        ('fat', 'pet the cat'),
        ('fog', 'walk the dog'),
        ('fun', "say we're done"),
    ]
    start2 = 'Someone better'
    start1_upper = []
    for word in start1:
        start1_upper.append(word.capitalize() + '!')
    first_line = ' '.join(start1_upper)
    for first, second in rhymes:
        first_handled = first.capitalize() + '!'
        print(first_line + ' ' + first_handled)
        print(start2 + ' ' + second + '.')


def things_to_do_7_11_second_approach():
    start1 = ['fee', 'fie', 'foe']
    rhymes = [
        ('flop', 'get a mop'),
        ('fope', 'turn the rope'),
        ('fa', 'get your ma'),
        ('fudge', 'call the judge'),
        ('fat', 'pet the cat'),
        ('fog', 'walk the dog'),
        ('fun', "say we're done"),
    ]
    start2 = 'Someone better'
    start1_upper = [word.capitalize() + '!' for word in start1]
    first_line = ' '.join(start1_upper)
    for first, second in rhymes:
        print(f"{first_line} {first.capitalize()}!")
        print(f"{start2} {second}.")