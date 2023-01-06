from bank import value

def test_value_hello():
    assert value('hello') == 0

def test_value_hey():
    assert value('hey') == 20

def test_value_anything():
    assert value('random') == 100

def test_value_CAPSLOCK():
    assert value('HELLO') == 0