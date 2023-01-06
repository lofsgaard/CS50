from plates import is_valid

def test_is_valid_plates1():
    assert is_valid('CS50') == True

def test_is_valid_plates2():
    assert is_valid('CS05') == False

def test_is_valid_plates7():
    assert is_valid('SC05') == False

def test_is_valid_plates3():
    assert is_valid('CS50P') == False

def test_is_valid_plates4():
    assert is_valid('PI3.14') == False

def test_is_valid_plates5():
    assert is_valid('H') == False

def test_is_valid_plates6():
    assert is_valid('OUTATIME') == False
