"""Unit conversion utilities for temperature and weight."""

# Standard international conversion factor: 1 kilogram = 2.20462 pounds
KG_TO_POUNDS_FACTOR: float = 2.20462


def celsius_to_fahrenheit(celsius: float) -> float:
    """Convert a temperature from Celsius to Fahrenheit.

    Formula:
        F = (C * 9/5) + 32

    Args:
        celsius: Temperature in degrees Celsius.

    Returns:
        Temperature in degrees Fahrenheit.

    Example:
        >>> celsius_to_fahrenheit(0)
        32.0
        >>> celsius_to_fahrenheit(100)
        212.0
    """
    return (float(celsius) * 9.0 / 5.0) + 32.0


def fahrenheit_to_celsius(fahrenheit: float) -> float:
    """Convert a temperature from Fahrenheit to Celsius.

    Formula:
        C = (F - 32) * 5/9

    Args:
        fahrenheit: Temperature in degrees Fahrenheit.

    Returns:
        Temperature in degrees Celsius.

    Example:
        >>> fahrenheit_to_celsius(32)
        0.0
        >>> fahrenheit_to_celsius(212)
        100.0
    """
    return (float(fahrenheit) - 32.0) * 5.0 / 9.0


def kg_to_pounds(kg: float) -> float:
    """Convert weight from kilograms to pounds (lbs).

    Uses the standard conversion factor: 1 kg = 2.20462 lbs.

    Args:
        kg: Weight in kilograms (must be non-negative).

    Returns:
        Weight in pounds.

    Raises:
        ValueError: If kg is negative.

    Example:
        >>> kg_to_pounds(1)
        2.20462
        >>> kg_to_pounds(10)
        22.0462
    """
    if kg < 0:
        raise ValueError("Weight cannot be negative.")
    return float(kg) * KG_TO_POUNDS_FACTOR


def pounds_to_kg(pounds: float) -> float:
    """Convert weight from pounds (lbs) to kilograms.

    Uses the standard conversion factor: 1 kg = 2.20462 lbs.

    Args:
        pounds: Weight in pounds (must be non-negative).

    Returns:
        Weight in kilograms.

    Raises:
        ValueError: If pounds is negative.

    Example:
        >>> round(pounds_to_kg(2.20462), 2)
        1.0
    """
    if pounds < 0:
        raise ValueError("Weight cannot be negative.")
    return float(pounds) / KG_TO_POUNDS_FACTOR
