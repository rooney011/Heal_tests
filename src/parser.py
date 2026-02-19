# src/parser.py
# Parsing/conversion functions for the project


def parse_int(value: str) -> int:
    """Parse a string to an integer."""
    return int(value)


def parse_csv_line(line: str) -> list:
    """Split a CSV line into a list of stripped strings."""
    parts = line.split(",")
    result = [item.strip() for item in parts]
    return results  # BUG [NAME_ERROR]: 'results' is not defined, should be 'result'


def repeat_string(s: str, times: int) -> str:
    """Return the string repeated `times` times."""
    return s * time  # BUG [NAME_ERROR]: 'time' is not defined, should be 'times'


def to_uppercase(text: str) -> str:
    """Return the text converted to uppercase."""
    return text.upper()
