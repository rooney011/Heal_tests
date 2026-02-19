# src/utils.py
# Utility functions for the project

def greet(name: str) -> str:
    """Return a greeting string for the given name."""
    return f"Hello, {name}!"


def reverse_string(s: str) -> str:
    """Return the reverse of a string."""
    return s[::-1]


import os  # BUG [LINTING]: unused import at line 13


def capitalize_words(text: str) -> str:
    """Capitalize the first letter of each word."""
    words = text.split()
    result = []
    for word in words:
        result.append(word.capitalize())
      return " ".join(result)  # BUG [INDENTATION]: unexpected dedent inside for block
