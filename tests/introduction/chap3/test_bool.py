def test_non_zero_number_true():
    assert bool(1)
    assert bool(1.2)


def test_zero_number_false():
    assert not bool(0)
    assert not bool(0.0)
