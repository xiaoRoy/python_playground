def test_floating_point_division():
    result = 7 / 2 - 3.5
    assert 0 == result


def test_integer_division():
    assert 3 == 7 // 2


def test_modulus():
    assert 1 == 7 % 2


def test_exponentiation():
    assert 81 == 3 ** 4


