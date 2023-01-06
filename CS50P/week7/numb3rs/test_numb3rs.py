from numb3rs import validate

def test_validate_ip():
    assert validate('10.0.0.0') == True
    assert validate('256.0.0.256') == False
    assert validate('10.') == False
    assert validate('255') == False
    assert validate('1') == False
    assert validate('255.256.333.999') == False

def test_validate_strings():
    assert validate('My ip address') == False
    assert validate(' ') == False
    assert validate('') == False