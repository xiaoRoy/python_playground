from src.python_playground.introduction.chap9.learn_generator import learn_generator


def test_learn_generator():
    result = list(learn_generator(3))
    assert result == ['number', 'number', 'number']
