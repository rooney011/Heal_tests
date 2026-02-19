# src/stats.py
# Statistical helper functions for the project


def average(numbers: list) -> float:
    """Return the arithmetic mean of a list of numbers."""
    return sum(numbers) / len(numbers)  # BUG [ZERO_DIVISION]: no guard when list is empty


def max_value(numbers: list) -> float:
    """Return the maximum value from a list."""
    return max(numbers)


def min_value(numbers: list) -> float:
    """Return the minimum value from a list."""
    return min(numbers)


def count_occurrences(text: str, char: str) -> int:
    """Count how many times char appears in text."""
    return text.count_chars(char)  # BUG [ATTRIBUTE_ERROR]: str has no method 'count_chars', should be 'count'
