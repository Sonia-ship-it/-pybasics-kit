"""Unit tests for conv_utils module."""

import pytest
from pybasics_kit.conv_utils import (
    celsius_to_fahrenheit,
    fahrenheit_to_celsius,
    kg_to_pounds,
    pounds_to_kg,
)


class TestTemperatureConversions:
    def test_celsius_to_fahrenheit_freezing(self):
        assert celsius_to_fahrenheit(0) == 32.0

    def test_celsius_to_fahrenheit_boiling(self):
        assert celsius_to_fahrenheit(100) == 212.0

    def test_celsius_to_fahrenheit_subzero(self):
        assert celsius_to_fahrenheit(-40) == -40.0

    def test_fahrenheit_to_celsius_freezing(self):
        assert fahrenheit_to_celsius(32) == 0.0

    def test_fahrenheit_to_celsius_boiling(self):
        assert fahrenheit_to_celsius(212) == 100.0

    def test_fahrenheit_to_celsius_subzero(self):
        assert fahrenheit_to_celsius(-40) == -40.0

    def test_temperature_roundtrip(self):
        original = 23.5
        converted = celsius_to_fahrenheit(original)
        reverted = fahrenheit_to_celsius(converted)
        assert pytest.approx(reverted, rel=1e-5) == original


class TestWeightConversions:
    def test_kg_to_pounds_standard(self):
        assert kg_to_pounds(1) == pytest.approx(2.20462, rel=1e-5)
        assert kg_to_pounds(10) == pytest.approx(22.0462, rel=1e-5)

    def test_kg_to_pounds_zero(self):
        assert kg_to_pounds(0) == 0.0

    def test_kg_to_pounds_negative_raises_error(self):
        with pytest.raises(ValueError, match="Weight cannot be negative"):
            kg_to_pounds(-5)

    def test_pounds_to_kg_standard(self):
        assert pounds_to_kg(2.20462) == pytest.approx(1.0, rel=1e-5)

    def test_pounds_to_kg_zero(self):
        assert pounds_to_kg(0) == 0.0

    def test_pounds_to_kg_negative_raises_error(self):
        with pytest.raises(ValueError, match="Weight cannot be negative"):
            pounds_to_kg(-10)

    def test_weight_roundtrip(self):
        original_kg = 75.0
        lbs = kg_to_pounds(original_kg)
        restored_kg = pounds_to_kg(lbs)
        assert pytest.approx(restored_kg, rel=1e-5) == original_kg
