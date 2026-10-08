"""Text utility functions for string cleaning, formatting, and analysis."""

import re
import unicodedata


def count_words(text: str) -> int:
    """Count words in a string intelligently based on whitespace.

    Unlike naive space-counting, this handles leading, trailing, and
    consecutive whitespace (spaces, tabs, newlines) correctly.

    Args:
        text: The input string.

    Returns:
        The total number of words found.

    Example:
        >>> count_words("Hello world")
        2
        >>> count_words("  Python   is   great  ")
        3
        >>> count_words("")
        0
    """
    if not isinstance(text, str):
        raise TypeError(f"Expected string, got {type(text).__name__}.")
    return len(text.split())


def slugify(text: str, separator: str = "-") -> str:
    """Convert a string into a clean, URL-safe slug.

    Converts characters to lowercase, replaces spaces and punctuation
    with a separator, and removes redundant or trailing separators.

    Args:
        text: The input string to convert.
        separator: The character separating words (defaults to '-').

    Returns:
        A lowercase, normalized, web-safe string.

    Example:
        >>> slugify("Hello World From Python!")
        'hello-world-from-python'
        >>> slugify("  Fast & Furious: Tokyo Drift  ")
        'fast-furious-tokyo-drift'
    """
    if not isinstance(text, str):
        raise TypeError(f"Expected string, got {type(text).__name__}.")

    # Normalize unicode characters (e.g. accents -> ASCII equivalents)
    normalized = unicodedata.normalize("NFKD", text)
    ascii_text = normalized.encode("ascii", "ignore").decode("ascii")

    # Lowercase
    cleaned = ascii_text.lower()

    # Replace characters that are not letters, digits, or hyphens with a space
    cleaned = re.sub(r"[^\w\s-]", "", cleaned)

    # Replace consecutive spaces and hyphens with the designated separator
    escaped_sep = re.escape(separator)
    cleaned = re.sub(r"[-\s]+", separator, cleaned)

    # Strip leading and trailing separators
    return cleaned.strip(separator)


def truncate(text: str, max_length: int, suffix: str = "...") -> str:
    """Shorten a string to a maximum length, appending a suffix if truncated.

    Args:
        text: The string to truncate.
        max_length: Maximum allowed length of the resulting string.
        suffix: Suffix string to append when truncated (defaults to '...').

    Returns:
        The truncated string, or the original string if it is within limit.

    Raises:
        ValueError: If max_length is less than the length of suffix.

    Example:
        >>> truncate("Python Programming", 10)
        'Python ...'
        >>> truncate("Short", 10)
        'Short'
    """
    if not isinstance(text, str):
        raise TypeError(f"Expected string, got {type(text).__name__}.")
    if max_length < len(suffix):
        raise ValueError(
            f"max_length ({max_length}) must be at least the length of suffix ({len(suffix)})."
        )

    if len(text) <= max_length:
        return text

    cutoff = max_length - len(suffix)
    return text[:cutoff] + suffix
