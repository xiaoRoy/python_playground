import pytest

from python_playground.introduction.chap10.learn_class import Cat, CatThird, Yugo, Car, Person, MdPerson, JdPerson, \
    EmailPerson, Mule, Hinny, Donkey, Horse, Animal, PrettyMixin, Thing, Duck, DuckSecond, Circle, DuckThird, Point, \
    Counter, Quote, QuestionQuote, ExclamationQuote, WhoAmI, who_says


def test_cat():
    a_cat = Cat()
    assert isinstance(a_cat, Cat)


def test_cat_attributes():
    one_cat = Cat()
    one_cat.name = 'Tom'
    one_cat.age = 12
    another_cat = Cat()
    one_cat.nemesis = another_cat

    with pytest.raises(AttributeError):
        one_cat.nemesis.name.upper()


def test_cat_third_attributes():
    one_cat = CatThird('Tom')
    assert one_cat.name == 'Tom'


def test_class_inheritance():
    assert issubclass(Yugo, Car)


def test_car_exclaim():
    car = Car()
    yugo = Yugo()

    assert car.exclaim() == 'Car'
    assert yugo.exclaim() == 'Yugo'


def test_person_name():
    person = Person('Jack')
    doctor = MdPerson('Smith')
    lawyer = JdPerson('Saul')

    assert person.name == 'Jack'
    assert doctor.name == 'Doctor Smith'
    assert lawyer.name == 'Saul, Esquire'


def test_yugo_push():
    yugo = Yugo()
    assert yugo.push() == 'Yugo push'


def test_email_person():
    email_person = EmailPerson('Black', 'black@123.com')
    assert email_person.name == 'Black'
    assert email_person.email == 'black@123.com'


def test_multiple_inheritance():
    mule = Mule()
    hinny = Hinny()

    assert mule.says() == 'Hee-haw!'
    assert hinny.says() == 'Neigh!'


def test_multiple_inheritance_mro():
    assert Mule.mro() == [Mule, Donkey, Horse, Animal, object]
    assert Hinny.__mro__ == (Hinny, Horse, Donkey, Animal, object)


def test_class_instance_self():
    car = Car()
    assert Car.exclaim(car) == 'Car'


def test_duck():
    duck = Duck('Jack')
    assert duck.name == 'Jack'

    duck.name = 'Rose'
    assert duck.name == 'Rose'


def test_duck_decorator():
    second_duck = DuckSecond('Black')
    assert second_duck.name == 'Black'
    second_duck.name = 'White'
    assert second_duck.name == 'White'


def test_circle():
    circle = Circle(4)
    assert circle.diameter == 8


def test_private_attribute():
    duck = DuckThird('One')
    assert duck.name == 'One'


def test_class_attribute():
    point = Point('down')
    assert point.target == 'down'
    assert Point.target == 'up'
    assert point.__class__.target == 'up'


def test_counter():
    count_a = Counter()
    count_b = Counter()
    assert Counter.count == 2
    assert Counter.count_info() == 'Counter has 2 little objects.'
    assert Counter.show_counter() == 'Counter'


def test_quote():
    quote = Quote('Smith', "I'm a hunter")
    question_quote = QuestionQuote('Jack', 'Who are you')
    exclamation_quote = ExclamationQuote('Lucy', "You're awful pretty")

    assert quote.who_says() == "Smith says:I'm a hunter."
    assert question_quote.who_says() == "Jack says:Who are you?"
    assert exclamation_quote.who_says() == "Lucy says:You're awful pretty!"


def test_duck_typing():
    who_am_i = WhoAmI()
    assert who_says(who_am_i) == "no body says:nothing"
