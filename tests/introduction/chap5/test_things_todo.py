from python_playground.introduction.chap5.things_todo import capitalize_the_word_start_m, questions_and_answers, \
    old_style_formatting, new_style_formatting, formatting_old, formatting_new, formatting_f_string


def test_capitalize_m():
    song = """When an eel grabs your arm,
    and it causes great harm,
    that's - a Moray!"""
    result = capitalize_the_word_start_m()
    assert result == song


def test_questions_and_answers():
    expected = """Q:We don't serve the strings around here. Are you a string?
A:No, I'm a frayed knot.
Q:What is said on the Father's Day in the forest?
A:'Pop!' goes the weasel.
Q:What makes the sound 'Sis! Boom! Bah!'?
A:An exploding sheep.
"""
    print()
    print(expected)
    result = ''.join(questions_and_answers())

    assert result == expected


def test_old_style_formatting():
    expected = ("My kitty cat likes roast beef,\n"
                "My kitty cat likes ham,\n"
                "My kitty cat feels on his head,\n"
                "And now thinks he's a clam.")
    assert old_style_formatting() == expected


def test_new_style_formatting():
    excepted = """Dear Ambassador Nibbler,

Thank you for your letter. We are sorry that our pudding
evaporated in your gazebo. Please note that it should never
be used in a gazebo, especially near any octothorpes.

Send us your receipt and $1.99 for shipping and handling.
We will send you another pudding that, in our tests,
is 88% less likely to have evaporated.

Thank you for your support.
Sincerely,
Shirley Iugeste
I Hate This Job
"""
    assert new_style_formatting() == excepted


formatting_result = ['Ducky McDuckface', 'Gourdy McGourdface', 'Spitzy McSpitzface']


def test_formatting_old():
    assert formatting_old() == formatting_result


def test_formatting_new():
    assert formatting_new() == formatting_result


def test_formatting_f_string():
    assert formatting_f_string() == formatting_result
