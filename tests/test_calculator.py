# tests/test_calculator.py
# Tests for src/calculator.py
# Expected to FAIL due to:
#   - LOGIC bug: add() returns subtraction instead of addition
#   - TYPE_ERROR bug: divide() returns str instead of float

import pytest
from src.calculator import add, subtract, multiply, divide


def test_add():
    # BUG [LOGIC]: add(2, 3) returns -1 instead of 5
    assert add(2, 3) == 5


def test_subtract():
    assert subtract(10, 4) == 6


def test_multiply():
    assert multiply(3, 4) == 12


def test_divide_returns_float():
    # BUG [TYPE_ERROR]: divide returns str, not float
    result = divide(10, 2)
    assert isinstance(result, float), f"Expected float, got {type(result).__name__}"
    assert result == 5.0


def test_divide_by_zero():
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        divide(5, 0)
