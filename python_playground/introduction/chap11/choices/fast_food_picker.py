from random import choice


def __getattr__(name):
    print(name)
    print('=====================')
    if name == 'pick':
        print('Pick() is loaded')


restaurants = ['McDonalds', 'KFC', 'Burger King', 'Taco Bell',
               'Wendys', 'Arbys', 'Pizza Hut']


def pick():
    return choice(restaurants)


def pick_second():
    import random
    return random.choice(restaurants)
