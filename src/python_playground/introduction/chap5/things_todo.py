def capitalize_the_word_start_m():
    song = """When an eel grabs your arm,
    and it causes great harm,
    that's - a moray!"""
    return song.replace(' m', ' M')


def questions_and_answers():
    questions = [
        "We don't serve the strings around here. Are you a string?",
        "What is said on the Father's Day in the forest?",
        "What makes the sound 'Sis! Boom! Bah!'?"
    ]
    answer = [
        "An exploding sheep.",
        "No, I'm a frayed knot.",
        "'Pop!' goes the weasel."
    ]
    result_dict = {0: 1, 1: 2, 2: 0}

    result_list = []
    for question_key, answer_value in result_dict.items():
        result_list.append(f"Q:{questions[question_key]}\nA:{answer[answer_value]}\n")

    return result_list


def old_style_formatting():
    input_info = """My kitty cat likes %s,
My kitty cat likes %s,
My kitty cat feels on his %s,
And now thinks he's a %s."""
    return input_info % ('roast beef', 'ham', 'head', 'clam')


letter = """Dear {salutation} {name},

Thank you for your letter. We are sorry that our {product}
{verbed} in your {room}. Please note that it should never
be used in a {room}, especially near any {animals}.

Send us your receipt and {amount} for shipping and handling.
We will send you another {product} that, in our tests,
is {percent}% less likely to have {verbed}.

Thank you for your support.
Sincerely,
{spokesman}
{job_title}
"""


def new_style_formatting():
    return letter.format(
        salutation='Ambassador',
        name='Nibbler',
        product='pudding',
        verbed='evaporated',
        room='gazebo',
        animals='octothorpes',
        amount='$1.99',
        percent=88,
        spokesman='Shirley Iugeste',
        job_title='I Hate This Job'
    )


names = ['duck', 'gourd', 'spitz']


def formatting_old():
    result = []
    for name in names:
        name_capitalized = name.capitalize()
        result.append("%sy Mc%sface" % (name_capitalized, name_capitalized))
    return result


def formatting_new():
    result = []
    for name in names:
        name_capitalized = name.capitalize()
        result.append("{name_capitalized}y Mc{name_capitalized}face".format(name_capitalized=name_capitalized))
    return result


def formatting_f_string():
    result = []
    for name in names:
        name_capitalized = name.capitalize()
        result.append(f"{name_capitalized}y Mc{name_capitalized}face")
    return result
