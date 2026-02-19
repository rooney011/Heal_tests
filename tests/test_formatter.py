# tests/test_formatter.py
# Tests for src/formatter.py
# Expected to FAIL due to ImportError: src.nonexistent_module does not exist

import pytest
from src.formatter import format_currency, format_percentage, pad_string


def test_format_currency():
    assert format_currency(9.99) == "$9.99"
    assert format_currency(1000.0, "€") == "€1000.00"


def test_format_percentage():
    assert format_percentage(0.75) == "75.0%"
    assert format_percentage(1.0) == "100.0%"


def test_pad_string():
    result = pad_string("hi", 10)
    assert len(result) == 10
    assert result.startswith("hi")
