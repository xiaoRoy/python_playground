drinks = {
    'martini': {'vodka', 'vermouth'},
    'black russian': {'vodka', 'kahlua'},
    'white russian': {'cream', 'kahlua', 'vodka'},
    'manhattan': {'rye', 'vermouth', 'bitters'},
    'screwdriver': {'orange juice', 'vodka'}
}


def learn_set_intersection_operator():
    for name, contents in drinks.items():
        if contents & {'vermouth', 'orange juice'}:
            print(name)


life = {
    'animals': {'cats': ['Henri', 'Grumpy', 'Lucy'],
                'octopi': [],
                'emus': []},
    'plants': {},
    'other': {}
}


def things_to_do_8_7():
    for life_key in life:
        print(life_key)


def things_to_do_8_8():
    animals = life['animals']
    for animals_key in animals:
        print(animals_key)


def things_to_do_8_9():
    cats = life['animals']['cats']
    for cat in cats:
        print(cat)


def things_to_do_8_12():
    for thing in ('Got %s' % number for number in range(10)):
        print(thing)




