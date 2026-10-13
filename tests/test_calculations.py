"""Unit tests for the calculations module in PyBasics Kit."""

import pytest
from pybasics_kit import (
    average,
    calculate_average,
    calculate_balance,
    calculate_budget_remaining,
    calculate_budget_usage,
    calculate_daily_budget,
    calculate_discounted_price,
    calculate_median,
    calculate_percentage,
    calculate_percentage_change,
    calculate_profit,
    calculate_profit_margin,
    calculate_savings,
    calculate_savings_rate,
    calculate_sum,
    calculate_tax,
    calculate_total_expenses,
    calculate_total_with_tax,
    calculate_unit_price,
    clamp,
    find_maximum,
    find_minimum,
    is_prime,
    split_amount,
)


class TestCalculatePercentage:
    def test_standard_percentage(self):
        assert calculate_percentage(25, 100) == 25.0
        assert calculate_percentage(1, 4) == 25.0
        assert calculate_percentage(50, 200) == 25.0

    def test_zero_value(self):
        assert calculate_percentage(0, 100) == 0.0

    def test_value_greater_than_total(self):
        assert calculate_percentage(150, 100) == 150.0

    def test_division_by_zero_raises_error(self):
        with pytest.raises(ValueError, match="Total cannot be zero"):
            calculate_percentage(25, 0)


class TestCalculateAverage:
    def test_standard_average(self):
        assert calculate_average([70, 80, 90]) == 80.0
        assert calculate_average([10, 20, 30]) == 20.0

    def test_single_element(self):
        assert calculate_average([42]) == 42.0

    def test_float_values(self):
        assert calculate_average([1.5, 2.5, 5.0]) == 3.0

    def test_empty_list_raises_error(self):
        with pytest.raises(ValueError, match="Cannot calculate average of an empty"):
            calculate_average([])

    def test_backward_compatible_average_alias(self):
        assert average([10, 20, 30]) == 20.0


class TestCalculateSum:
    def test_standard_sum(self):
        assert calculate_sum([10, 20, 30]) == 60

    def test_float_sum(self):
        assert calculate_sum([1.5, 2.5, 3.0]) == 7.0

    def test_empty_sequence(self):
        assert calculate_sum([]) == 0

    def test_tuple_input(self):
        assert calculate_sum((5, 10, 15)) == 30


class TestCalculateMedian:
    def test_odd_length(self):
        assert calculate_median([1, 3, 2]) == 2.0
        assert calculate_median([5, 1, 9, 3, 7]) == 5.0

    def test_even_length(self):
        assert calculate_median([1, 2, 3, 4]) == 2.5
        assert calculate_median([10, 20]) == 15.0

    def test_single_element(self):
        assert calculate_median([99]) == 99.0

    def test_empty_sequence_raises_error(self):
        with pytest.raises(ValueError, match="Cannot calculate median of an empty"):
            calculate_median([])


class TestFindMinimumAndMaximum:
    def test_find_minimum(self):
        assert find_minimum([12, 5, 89, 3]) == 3
        assert find_minimum([0, -10, 5, -3]) == -10
        assert find_minimum([7]) == 7

    def test_find_minimum_empty_raises_error(self):
        with pytest.raises(ValueError, match="Cannot find minimum"):
            find_minimum([])

    def test_find_maximum(self):
        assert find_maximum([12, 5, 89, 3]) == 89
        assert find_maximum([-10, -5, -20]) == -5
        assert find_maximum([42]) == 42

    def test_find_maximum_empty_raises_error(self):
        with pytest.raises(ValueError, match="Cannot find maximum"):
            find_maximum([])


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

    def test_boolean_type_error(self):
        with pytest.raises(TypeError):
            is_prime(True)  # type: ignore


class TestCalculatePercentageChange:
    def test_percentage_increase(self):
        assert calculate_percentage_change(100, 150) == 50.0
        assert calculate_percentage_change(50, 75) == 50.0

    def test_percentage_decrease(self):
        assert calculate_percentage_change(100, 80) == -20.0
        assert calculate_percentage_change(200, 100) == -50.0

    def test_no_change(self):
        assert calculate_percentage_change(50, 50) == 0.0

    def test_zero_old_raises_error(self):
        with pytest.raises(ValueError, match="Old value cannot be zero"):
            calculate_percentage_change(0, 100)


class TestClamp:
    def test_value_within_range(self):
        assert clamp(5, 0, 10) == 5
        assert clamp(7, 0, 10) == 7

    def test_value_below_min(self):
        assert clamp(-5, 0, 10) == 0

    def test_value_above_max(self):
        assert clamp(15, 0, 10) == 10

    def test_value_at_boundaries(self):
        assert clamp(0, 0, 10) == 0
        assert clamp(10, 0, 10) == 10

    def test_invalid_range_raises_error(self):
        with pytest.raises(ValueError, match="minimum.*cannot be greater"):
            clamp(5, 10, 0)


class TestPersonalFinanceCalculations:
    def test_calculate_balance_simple(self):
        assert calculate_balance(1000, 350) == 650

    def test_calculate_balance_with_list(self):
        assert calculate_balance(2000, [500, 300, 200]) == 1000

    def test_calculate_balance_with_dict(self):
        assert calculate_balance(2000, {"rent": 1200, "food": 300}) == 500

    def test_calculate_balance_negative(self):
        assert calculate_balance(500, 700) == -200

    def test_calculate_total_expenses(self):
        assert calculate_total_expenses([100, 250, 50]) == 400
        assert calculate_total_expenses({"rent": 1200, "utilities": 150}) == 1350
        assert calculate_total_expenses(350) == 350
        assert calculate_total_expenses([]) == 0

    def test_calculate_savings(self):
        assert calculate_savings(3000, 2200) == 800
        assert calculate_savings(1000, 350) == 650
        assert calculate_savings(3000, [1000, 1200]) == 800

    def test_calculate_savings_rate(self):
        assert calculate_savings_rate(5000, 1000) == 20.0
        assert calculate_savings_rate(2000, 500) == 25.0
        assert calculate_savings_rate(3000, 0) == 0.0

    def test_calculate_savings_rate_invalid_income(self):
        with pytest.raises(ValueError, match="Income must be greater than zero"):
            calculate_savings_rate(0, 100)
        with pytest.raises(ValueError, match="Income must be greater than zero"):
            calculate_savings_rate(-1000, 100)

    def test_calculate_budget_remaining(self):
        assert calculate_budget_remaining(500, 320) == 180
        assert calculate_budget_remaining(1000, [200, 300, 100]) == 400
        assert calculate_budget_remaining(500, 600) == -100

    def test_calculate_budget_usage(self):
        assert calculate_budget_usage(250, 1000) == 25.0
        assert calculate_budget_usage(500, 500) == 100.0
        assert calculate_budget_usage(600, 500) == 120.0
        assert calculate_budget_usage([100, 150], 1000) == 25.0

    def test_calculate_budget_usage_invalid_budget(self):
        with pytest.raises(ValueError, match="Budget must be greater than zero"):
            calculate_budget_usage(100, 0)
        with pytest.raises(ValueError, match="Budget must be greater than zero"):
            calculate_budget_usage(100, -500)

    def test_calculate_daily_budget(self):
        assert calculate_daily_budget(300, 10) == 30.0
        assert calculate_daily_budget(140, 7) == 20.0

    def test_calculate_daily_budget_invalid_days(self):
        with pytest.raises(ValueError, match="Days must be greater than zero"):
            calculate_daily_budget(300, 0)
        with pytest.raises(ValueError, match="Days must be greater than zero"):
            calculate_daily_budget(300, -5)


class TestCommercialBusinessCalculations:
    def test_calculate_discounted_price(self):
        assert calculate_discounted_price(100, 20) == 80.0
        assert calculate_discounted_price(50, 10) == 45.0
        assert calculate_discounted_price(100, 0) == 100.0
        assert calculate_discounted_price(100, 100) == 0.0

    def test_calculate_discounted_price_validation(self):
        with pytest.raises(ValueError, match="Price cannot be negative"):
            calculate_discounted_price(-10, 20)
        with pytest.raises(ValueError, match="Discount percentage must be between 0 and 100"):
            calculate_discounted_price(100, -5)
        with pytest.raises(ValueError, match="Discount percentage must be between 0 and 100"):
            calculate_discounted_price(100, 105)

    def test_calculate_tax(self):
        assert calculate_tax(100, 15) == 15.0
        assert calculate_tax(200, 8) == 16.0
        assert calculate_tax(100, 0) == 0.0

    def test_calculate_tax_validation(self):
        with pytest.raises(ValueError, match="Amount cannot be negative"):
            calculate_tax(-100, 15)
        with pytest.raises(ValueError, match="Tax rate cannot be negative"):
            calculate_tax(100, -5)

    def test_calculate_total_with_tax(self):
        assert calculate_total_with_tax(100, 15) == 115.0
        assert calculate_total_with_tax(50, 10) == 55.0
        assert calculate_total_with_tax(100, 0) == 100.0

    def test_split_amount(self):
        assert split_amount(100, 4) == 25.0
        assert split_amount(90, 3) == 30.0
        assert split_amount(50, 1) == 50.0

    def test_split_amount_validation(self):
        with pytest.raises(ValueError, match="Number of people must be greater than zero"):
            split_amount(100, 0)
        with pytest.raises(ValueError, match="Number of people must be greater than zero"):
            split_amount(100, -2)

    def test_calculate_unit_price(self):
        assert calculate_unit_price(50, 5) == 10.0
        assert calculate_unit_price(100, 4) == 25.0

    def test_calculate_unit_price_validation(self):
        with pytest.raises(ValueError, match="Total price cannot be negative"):
            calculate_unit_price(-50, 5)
        with pytest.raises(ValueError, match="Quantity must be greater than zero"):
            calculate_unit_price(50, 0)
        with pytest.raises(ValueError, match="Quantity must be greater than zero"):
            calculate_unit_price(50, -2)

    def test_calculate_profit(self):
        assert calculate_profit(1000, 700) == 300
        assert calculate_profit(5000, [1500, 1000, 500]) == 2000
        assert calculate_profit(500, 700) == -200

    def test_calculate_profit_margin(self):
        assert calculate_profit_margin(1000, 200) == 20.0
        assert calculate_profit_margin(500, 100) == 20.0
        assert calculate_profit_margin(1000, 0) == 0.0
        assert calculate_profit_margin(1000, -100) == -10.0

    def test_calculate_profit_margin_zero_revenue(self):
        with pytest.raises(ValueError, match="Revenue cannot be zero"):
            calculate_profit_margin(0, 100)
