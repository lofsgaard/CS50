from fuel import convert, gauge
import pytest


def test_convert():
    assert convert('3/4') == 75
    with pytest.raises(ZeroDivisionError):
        assert convert("10/0") is True
    with pytest.raises(ValueError):
        assert convert("a/b") is True


def test_gauge():
    assert gauge(99) == 'F'
    assert gauge(1) == 'E'
    assert gauge(50) == '50%'