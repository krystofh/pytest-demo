# Test functions from source/functions.py
import pytest
from source import functions


def test_add() -> None:
    # Positive numbers
    result = functions.add(10, 7)
    assert result == 17
    # Negative numbers
    result = functions.add(10, -2)
    assert result == 8
    # Zero
    result = functions.add(5, 0)
    assert result == 5
    # Floats
    result = functions.add(5, 2.5)
    assert result == 7.5  # will also work as Python does not treat types like c
    # assert type(result) == int  # one can catch the error like this


def test_subtract():
    assert functions.subtract(32, 4) == 28
    assert functions.subtract(32, -2) == 34
    assert functions.subtract(32, -2) == 34


def test_multiply():
    assert functions.multiply(4, 8) == 32
    assert functions.multiply(2.5, 2.5) == 6.25
    assert functions.multiply(4, 0) == 0


def test_divide():
    assert functions.divide(32, 8) == 4
    with pytest.raises(ZeroDivisionError):  # Test that error is raised correctly
        functions.divide(16, 0)
