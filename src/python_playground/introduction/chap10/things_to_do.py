import textwrap


class ThingSecond:
    pass


class ThingThird:
    letters = 'third'


class ThingFourth:

    def __init__(self, letters):
        self.letters = letters


class Element:

    def __init__(self, name, symbol, number):
        self.__name = name
        self.__symbol = symbol
        self.__number = number

    @property
    def name(self):
        return self.__name

    @property
    def symbol(self):
        return self.__symbol

    @property
    def number(self):
        return self.__number

    def dump(self):
        result = f"""
        name:{self.__name}
        symbol:{self.__symbol}
        number:{self.__number}"""
        return textwrap.dedent(result)

    def __str__(self):
        return self.dump()


class Bear:

    def eats(self):
        return 'berries'


class Rabbit:

    def eats(self):
        return 'clover'


class Octothore:

    def eats(self):
        return 'campers'


class Laser:
    def does(self):
        return 'disintegrate'


class Claw:
    def dose(self):
        return 'crush'


class SmartPhone:
    def dose(self):
        return 'ring'


class Robot:
    def __init__(self, laser, claw, smart_phone):
        self.laser = laser
        self.claw = claw
        self.smart_phone = smart_phone

    def does(self):
        return """
        I have many attachments:
        My laser, to %s.
        My claw, to %s.
        My smartphone, to %s.
        """ % (self.laser.does(), self.claw.dose(), self.smart_phone.dose())
