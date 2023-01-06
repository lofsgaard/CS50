from working import convert
import pytest

def test_convert():
    assert convert('9 AM to 5 PM') == '09:00 to 17:00'
    assert convert('6 AM to 3 PM') == '06:00 to 15:00'
    assert convert('7 PM to 12 AM') == '19:00 to 00:00'
    assert convert('7 PM to 5 AM') == '19:00 to 05:00'

def test_convert_valuerror_empty():
    with pytest.raises(ValueError):
        assert convert(" to ") is True
    with pytest.raises(ValueError):
        assert convert("9AM - 10PM ") is True

def test_convert_valuerror_wrong():
    with pytest.raises(ValueError):
        assert convert("13 AM to 15 PM") is True


