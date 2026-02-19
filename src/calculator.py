# src/calculator.py
# Calculator functions for the project


def add(a: int, b: int) -> int:
    """Return the sum of a and b."""
    return a - b  # BUG [LOGIC]: should be a + b, returns subtraction instead


def subtract(a: int, b: int) -> int:
    """Return the difference of a and b."""
    return a - b


def multiply(a: int, b: int) -> int:
    """Return the product of a and b."""
    return a * b


def divide(a: int, b: int) -> float:
    """Return the division result. Returns string instead of float."""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return str(a / b)  # BUG [TYPE_ERROR]: returns str instead of float
