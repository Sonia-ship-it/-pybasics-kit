"""Math utility functions for everyday calculations."""

import math
from typing import Sequence, Union


def calculate_percentage(value: float, total: float) -> float:
    """Calculate what percentage a given value represents of a total.

    Args:
        value: The portion value.
        total: The whole/total value. Must not be zero.

    Returns:
        The percentage representation (e.g., 25 out of 100 is 25.0).

    Raises:
        ValueError: If total is zero.

    Example:
        >>> calculate_percentage(25, 100)
        25.0
        >>> calculate_percentage(1, 4)
        25.0
    """
    if total == 0:
        raise ValueError("Total cannot be zero when calculating percentage.")
    return (value / total) * 100.0


def is_prime(number: int) -> bool:
    """Determine whether an integer is a prime number.

    A prime number is a natural number greater than 1 that has no positive
    divisors other than 1 and itself.

    Uses an efficient O(sqrt(n)) check by testing divisibility up to
    the integer square root.

    Args:
        number: The integer to test.

    Returns:
        True if the number is prime, False otherwise.

    Example:
        >>> is_prime(2)
        True
        >>> is_prime(7)
        True
        >>> is_prime(10)
        False
        >>> is_prime(1)
        False
    """
    if not isinstance(number, int):
        raise TypeError(f"Expected integer, got {type(number).__name__}.")

    if number <= 1:
        return False
    if number == 2:
        return True
    if number % 2 == 0:
        return False

    # Check odd divisors up to the square root of number
    limit = math.isqrt(number)
    for i in range(3, limit + 1, 2):
        if number % i == 0:
            return False

    return True


def clamp(value: float, min_value: float, max_value: float) -> float:
    """Restrict a value to be within a specified range [min_value, max_value].

    Args:
        value: The number to clamp.
        min_value: The lower bound of the range.
        max_value: The upper bound of the range.

    Returns:
        min_value if value < min_value,
        max_value if value > max_value,
        otherwise value.

    Raises:
        ValueError: If min_value is greater than max_value.

    Example:
        >>> clamp(15, 0, 10)
        10
        >>> clamp(-5, 0, 10)
        0
        >>> clamp(7, 0, 10)
        7
    """
    if min_value > max_value:
        raise ValueError(
            f"min_value ({min_value}) cannot be greater than max_value ({max_value})."
        )
    return max(min_value, min(value, max_value))


def average(numbers: Sequence[Union[int, float]]) -> float:
    """Calculate the arithmetic mean of a sequence of numbers.

    Args:
        numbers: A non-empty sequence of numbers.

    Returns:
        The average value as a float.

    Raises:
        ValueError: If the sequence is empty.

    Example:
        >>> average([10, 20, 30])
        20.0
    """
    if not numbers:
        raise ValueError("Cannot calculate average of an empty sequence.")
    return float(sum(numbers) / len(numbers))
