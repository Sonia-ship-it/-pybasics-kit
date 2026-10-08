"""Unit tests for game_utils module."""

import pytest
from pybasics_kit.game_utils import flip_coin, roll_dice


class TestRollDice:
    def test_default_dice_range(self):
        for _ in range(50):
            result = roll_dice()
            assert isinstance(result, int)
            assert 1 <= result <= 6

    def test_twenty_sided_dice_range(self):
        for _ in range(50):
            result = roll_dice(faces=20)
            assert 1 <= result <= 20

    def test_minimum_two_faces(self):
        for _ in range(20):
            result = roll_dice(faces=2)
            assert result in (1, 2)

    def test_invalid_faces_raises_value_error(self):
        with pytest.raises(ValueError, match="at least 2 faces"):
            roll_dice(faces=1)
        with pytest.raises(ValueError, match="at least 2 faces"):
            roll_dice(faces=0)
        with pytest.raises(ValueError, match="at least 2 faces"):
            roll_dice(faces=-6)

    def test_deterministic_dice_roll_with_seed(self):
        roll1 = roll_dice(faces=100, seed=42)
        roll2 = roll_dice(faces=100, seed=42)
        assert roll1 == roll2


class TestFlipCoin:
    def test_flip_coin_valid_outcomes(self):
        valid_outcomes = {"Heads", "Tails"}
        for _ in range(50):
            result = flip_coin()
            assert result in valid_outcomes

    def test_deterministic_coin_flip_with_seed(self):
        # Testing with fixed seeds should always produce predictable, reproducible outcomes
        result_seed_42_a = flip_coin(seed=42)
        result_seed_42_b = flip_coin(seed=42)
        assert result_seed_42_a == result_seed_42_b
        assert result_seed_42_a in ("Heads", "Tails")

        result_seed_99_a = flip_coin(seed=99)
        result_seed_99_b = flip_coin(seed=99)
        assert result_seed_99_a == result_seed_99_b
