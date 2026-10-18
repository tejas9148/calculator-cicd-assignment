
def validate_numbers(a, b):
    """Validate that both inputs are positive integers."""
    if (
        isinstance(a, bool)
        or isinstance(b, bool)
        or not isinstance(a, int)
        or not isinstance(b, int)
    ):
        raise TypeError("Both inputs must be integers")

    if a <= 0 or b <= 0:
        raise ValueError("Both inputs must be positive integers")


def add(a, b):
    validate_numbers(a, b)
    return a + b


def subtract(a, b):
    validate_numbers(a, b)
    return a - b


def multiply(a, b):
    validate_numbers(a, b)
    return a * b
