"""Game utility functions for dice rolling and coin flipping."""

import random
from typing import Optional


def roll_dice(faces: int = 6, seed: Optional[int] = None) -> int:
    """Roll a virtual die and return a result between 1 and faces.

    Args:
        faces: The number of faces on the die (must be at least 2, defaults to 6).
        seed: Optional integer seed for deterministic testing. If provided,
              an isolated random generator is used to avoid mutating global state.

    Returns:
        An integer between 1 and faces (inclusive).

    Raises:
        ValueError: If faces is less than 2.

    Example:
        >>> roll_dice()  # Random 1-6
        4
        >>> roll_dice(faces=20)  # Random 1-20
        17
        >>> roll_dice(faces=6, seed=42)  # Deterministic test
        6
    """
    if faces < 2:
        raise ValueError(f"A dice must have at least 2 faces, got {faces}.")

    rng = random.Random(seed) if seed is not None else random
    return rng.randint(1, faces)


def flip_coin(seed: Optional[int] = None) -> str:
    """Flip a virtual coin and return either 'Heads' or 'Tails'.

    By default, this produces a random result. You can optionally supply
    a seed parameter for deterministic output, which is especially useful
    in automated unit tests to ensure reproducible test scenarios without
    altering Python's global random state.

    Args:
        seed: Optional integer seed for deterministic testing.

    Returns:
        Either 'Heads' or 'Tails'.

    Example:
        >>> flip_coin()  # Random
        'Heads'
        >>> flip_coin(seed=42)  # Deterministic: always 'Heads' for seed 42
        'Heads'
    """
    rng = random.Random(seed) if seed is not None else random
    return rng.choice(["Heads", "Tails"])
