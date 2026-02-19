# tests/test_utils.py
# Tests for src/utils.py
# Expected to FAIL due to IndentationError in capitalize_words()

import pytest
from src.utils import greet, reverse_string, capitalize_words


def test_greet():
    assert greet("World") == "Hello, World!"


def test_reverse_string():
    assert reverse_string("hello") == "olleh"
    assert reverse_string("") == ""


def test_capitalize_words():
    # This will trigger the IndentationError in utils.py at import/call time
    result = capitalize_words("hello world")
    assert result == "Hello World"
