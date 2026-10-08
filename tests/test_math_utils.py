"""Unit tests for math_utils module."""

import pytest
from pybasics_kit.math_utils import average, calculate_percentage, clamp, is_prime


class TestCalculatePercentage:
    def test_standard_percentage(self):
        assert calculate_percentage(25, 100) == 25.0
        assert calculate_percentage(1, 4) == 25.0
        assert calculate_percentage(50, 200) == 25.0

    def test_zero_value(self):
        assert calculate_percentage(0, 100) == 0.0

    def test_value_greater_than_total(self):
        assert calculate_percentage(150, 100) == 150.0

    def test_division_by_zero_raises_value_error(self):
        with pytest.raises(ValueError, match="Total cannot be zero"):
            calculate_percentage(25, 0)


class TestIsPrime:
    @pytest.mark.parametrize(
        "num",
        [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 97],
    )
    def test_prime_numbers(self, num: int):
        assert is_prime(num) is True

    @pytest.mark.parametrize(
        "num",
        [-10, -1, 0, 1, 4, 6, 8, 9, 10, 12, 15, 21, 25, 27, 33, 49, 100],
    )
    def test_non_prime_numbers(self, num: int):
        assert is_prime(num) is False

    def test_non_integer_type_error(self):
        with pytest.raises(TypeError):
            is_prime(3.14)  # type: ignore


class TestClamp:
    def test_value_within_range(self):
        assert clamp(5, 0, 10) == 5

    def test_value_below_min(self):
        assert clamp(-5, 0, 10) == 0

    def test_value_above_max(self):
        assert clamp(15, 0, 10) == 10

    def test_value_at_boundaries(self):
        assert clamp(0, 0, 10) == 0
        assert clamp(10, 0, 10) == 10

    def test_invalid_range_raises_error(self):
        with pytest.raises(ValueError, match="min_value.*cannot be greater"):
            clamp(5, 10, 0)


class TestAverage:
    def test_standard_average(self):
        assert average([10, 20, 30]) == 20.0
        assert average([1, 2, 3, 4, 5]) == 3.0

    def test_single_element(self):
        assert average([42]) == 42.0

    def test_empty_list_raises_error(self):
        with pytest.raises(ValueError, match="Cannot calculate average of an empty"):
            average([])
