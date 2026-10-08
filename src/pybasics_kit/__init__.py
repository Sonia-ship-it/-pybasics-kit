"""🧰 pybasics_kit — The Swiss Army Knife utility library for everyday Python workflows.

A lightweight, beginner-friendly collection of everyday utilities for math,
text processing, unit conversions, and mini-games.
"""

__version__ = "0.1.0"

# Convenient top-level imports for the most commonly used utilities
from pybasics_kit.conv_utils import (
    celsius_to_fahrenheit,
    fahrenheit_to_celsius,
    kg_to_pounds,
    pounds_to_kg,
)
from pybasics_kit.game_utils import (
    flip_coin,
    roll_dice,
)
from pybasics_kit.math_utils import (
    average,
    calculate_percentage,
    clamp,
    is_prime,
)
from pybasics_kit.text_utils import (
    count_words,
    slugify,
    truncate,
)

__all__ = [
    "__version__",
    # Math
    "calculate_percentage",
    "is_prime",
    "clamp",
    "average",
    # Text
    "count_words",
    "slugify",
    "truncate",
    # Conversions
    "celsius_to_fahrenheit",
    "fahrenheit_to_celsius",
    "kg_to_pounds",
    "pounds_to_kg",
    # Games
    "roll_dice",
    "flip_coin",
]
