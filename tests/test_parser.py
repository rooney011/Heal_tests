# tests/test_parser.py
# Tests for src/parser.py
# Expected to FAIL due to:
#   - NAME_ERROR: parse_csv_line() references undefined 'results'
#   - NAME_ERROR: repeat_string() references undefined 'time'

import pytest
from src.parser import parse_int, parse_csv_line, repeat_string, to_uppercase


def test_parse_int():
    assert parse_int("42") == 42
    assert parse_int("-7") == -7


def test_parse_csv_line():
    # BUG [NAME_ERROR]: raises NameError because 'results' is not defined
    result = parse_csv_line("  foo , bar , baz  ")
    assert result == ["foo", "bar", "baz"]


def test_repeat_string():
    # BUG [NAME_ERROR]: raises NameError because 'time' is not defined
    assert repeat_string("ha", 3) == "hahaha"


def test_to_uppercase():
    assert to_uppercase("hello") == "HELLO"
