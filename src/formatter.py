# src/formatter.py
# Formatting functions for the project

from src.nonexistent_module import helper  # BUG [IMPORT]: module does not exist


def format_currency(amount: float, symbol: str = "$") -> str:
    """Return a formatted currency string."""
    return f"{symbol}{amount:.2f}"


def format_percentage(value: float) -> str:
    """Return a formatted percentage string."""
    return f"{value * 100:.1f}%"


def pad_string(s: str, width: int) -> str:
    """Return the string padded to the given width."""
    return s.ljust(width)
