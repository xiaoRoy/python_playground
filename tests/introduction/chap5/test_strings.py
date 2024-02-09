# actual == expected
def test_raw_string():
    info = r'Type a \n to get a new line in a normal string'
    assert info == 'Type a \\n to get a new line in a normal string'


def test_string_combination():
    assert 'hello k' == 'hello ' 'k'
    result = ('j '
              'loves '
              'k')
    assert result == 'j loves k'


def test_string_duplication():
    love = 'love'
    result = love * 3000
    assert len(result) == 12_000


# The start offset is inclusive, and the end offset is exclusive
def test_string_slice():
    letters = 'abcdefghijklmnopqrstuvwxyz'
    assert letters[-3:] == 'xyz'
    assert letters[4:20:3] == 'ehknqt'
    assert letters[::-1] == 'zyxwvutsrqponmlkjihgfedcba'
    assert letters[100:] == ''
