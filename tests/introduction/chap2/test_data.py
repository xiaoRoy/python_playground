
def test_list_is_mutable():
    list_a = [1, 2, 3]
    list_b = list_a
    list_b[0] = 99
    assert list_a[0] == 99
