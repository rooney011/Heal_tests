# tests/test_validator.py
# Tests for src/validator.py
# Expected to FAIL due to SyntaxError (missing colon in is_positive_number)

import pytest
from src.validator import is_non_empty_string, is_positive_number, is_valid_email


def test_is_non_empty_string():
    assert is_non_empty_string("hello") is True
    assert is_non_empty_string("") is False
    assert is_non_empty_string(123) is False


def test_is_positive_number():
    assert is_positive_number(5) is True
    assert is_positive_number(-1) is False
    assert is_positive_number(0) is False


def test_is_valid_email():
    assert is_valid_email("user@example.com") is True
    assert is_valid_email("notanemail") is False
