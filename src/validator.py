# src/validator.py
# Validation functions for the project


def is_non_empty_string(value) -> bool:
    """Return True if value is a non-empty string."""
    return isinstance(value, str) and len(value) > 0


def is_positive_number(value) -> bool
    """Return True if value is a positive number."""
    return isinstance(value, (int, float)) and value > 0


def is_valid_email(email: str) -> bool:
    """Return True if email contains '@' and '.'."""
    return "@" in email and "." in email
