from app.simple_calculator import subtract
import pytest

def test_subtract_positive():
    assert subtract(5, 3) == 2

def test_subtract_negative():
    assert subtract(-5, -3) == -2
