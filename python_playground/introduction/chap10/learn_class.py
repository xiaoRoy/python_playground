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

