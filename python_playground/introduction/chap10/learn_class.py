import pprint


class Cat:
    pass


class CatSecond:
    def __init__(self):
        pass


class CatThird:
    def __init__(self, name):
        self.name = name


class Car:
    def exclaim(self):
        return 'Car'


class Yugo(Car):
    def exclaim(self):
        return 'Yugo'

    def push(self):
        return self.exclaim() + ' push'


class Person:
    def __init__(self, name):
        self.name = name


class MdPerson(Person):
    def __init__(self, name):
        super().__init__(name)
        self.name = 'Doctor ' + name


class JdPerson(Person):
    def __init__(self, name):
        super().__init__(name)
        self.name = name + ', Esquire'


class EmailPerson(Person):
    def __init__(self, name, email):
        super().__init__(name)
        self.email = email


class Animal:
    def says(self):
        return 'I speak!'


class Horse(Animal):
    def says(self):
        return 'Neigh!'


class Donkey(Animal):
    def says(self):
        return 'Hee-haw!'


class Mule(Donkey, Horse):
    pass


class Hinny(Horse, Donkey):
    pass


class PrettyMixin:
    def dump(self):
        pprint.pprint(vars(self))


class Thing(PrettyMixin):
    pass


class Duck(object):
    def __init__(self, name):
        self.hidden_name = name

    def get_name(self):
        return self.hidden_name

    def set_name(self, name):
        self.hidden_name = name

    name = property(get_name, set_name)


class DuckSecond:
    def __init__(self, name):
        self.hidden_name = name

    @property
    def name(self):
        return self.hidden_name

    @name.setter
    def name(self, name):
        self.hidden_name = name


class DuckThird:
    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name


class Circle:
    def __init__(self, radius):
        self.radius = radius

    @property
    def diameter(self):
        return self.radius * 2


class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    area = property(area, doc='area of the rectangle')


class Point:
    target = 'up'

    def __init__(self, target):
        self.target = target
