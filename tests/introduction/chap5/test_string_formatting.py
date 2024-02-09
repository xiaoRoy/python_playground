def test_string_formatting_old():
    actor = 'alan smith'
    result = "My wife's favorite actor is %s" % actor
    assert result == "My wife's favorite actor is alan smith"

    cat = 'Chester'
    weight = 28
    result_a = "Our cat %s weights %d pounds" % (cat, weight)
    assert result_a == "Our cat Chester weights 28 pounds"


def test_string_formatting_new():
    thing = 'woodchuck'
    place = 'lake'
    result = 'The {} is in the {}.'.format(thing, place)
    assert result == 'The woodchuck is in the lake.'


def test_string_formatting_new_using_map():
    mapping = {'thing': 'woodchuck', 'place': 'bathtub'}
    result = 'The {0[thing]} is in the {0[place]}.'.format(mapping)
    assert result == 'The woodchuck is in the bathtub.'


#f-string
def test_string_formatting_newest():
    thing = 'woodchuck'
    place = 'werepond'
    result = f'The {thing} is in the {place.upper()}.'
    assert result == 'The woodchuck is in the WEREPOND.'


def test_string_f_strings():
    thing = 'woodchuck'
    place = 'lake'
    assert f'{thing =}, {place =}' == "thing ='woodchuck', place ='lake'"

