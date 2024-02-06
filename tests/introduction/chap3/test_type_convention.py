def test_type_conversion_integer():
    assert 0 == int(False)
    assert 814 == int(814.2)
    assert 814 == int('814')


def test_type_conversion_float():
    assert 0 == 1.0 - float(True)
    assert 0 == 10000.0 - float('1.0e4')


