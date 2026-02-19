# Heal Test — CI/CD Healing Agent Target Repository

A minimal Python project designed as a target for an autonomous CI/CD healing agent.

The agent's goal is to detect failing tests, classify the root cause of each failure,
apply fixes, and re-run CI until all tests pass.

## Project Structure

```
/
├── src/
│   ├── utils.py         # String utility functions
│   ├── validator.py     # Input validation functions
│   ├── calculator.py    # Arithmetic functions
│   └── formatter.py     # Output formatting functions
├── tests/
│   ├── test_utils.py
│   ├── test_validator.py
│   ├── test_calculator.py
│   └── test_formatter.py
├── requirements.txt
└── .github/
    └── workflows/
        └── ci.yml
```

## Requirements

- Python 3.10+
- pytest

## Running Tests Locally

```bash
pip install -r requirements.txt
pytest -q
```

## CI

This project uses GitHub Actions. The CI pipeline runs automatically on every push and pull request.
