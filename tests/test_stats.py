# tests/test_stats.py
# Tests for src/stats.py
# Expected to FAIL due to:
#   - ZERO_DIVISION: average([]) raises ZeroDivisionError
#   - ATTRIBUTE_ERROR: count_occurrences() calls non-existent str.count_chars()

import pytest
from src.stats import average, max_value, min_value, count_occurrences


def test_average_normal():
    assert average([10, 20, 30]) == 20.0


def test_average_empty_list():
    # BUG [ZERO_DIVISION]: average([]) raises ZeroDivisionError, should return 0 or raise ValueError
    result = average([])
    assert result == 0.0


def test_max_value():
    assert max_value([3, 1, 4, 1, 5, 9]) == 9


def test_min_value():
    assert min_value([3, 1, 4, 1, 5, 9]) == 1


def test_count_occurrences():
    # BUG [ATTRIBUTE_ERROR]: str has no method 'count_chars', raises AttributeError
    assert count_occurrences("hello world", "l") == 3
