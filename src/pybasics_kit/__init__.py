"""PyBasics Kit — A lightweight Python toolkit for everyday mathematical and financial calculations.

It can be used in budgeting apps, e-commerce platforms, school systems,
business applications, and ordinary Python programs.
"""

__version__ = "0.2.0"

from pybasics_kit.calculations import (
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

__all__ = [
    "__version__",
    # Mathematical & Statistical Calculations
    "calculate_percentage",
    "calculate_average",
    "calculate_sum",
    "calculate_median",
    "find_minimum",
    "find_maximum",
    "is_prime",
    "calculate_percentage_change",
    "clamp",
    "average",
    # Personal Finance & Budgeting Calculations
    "calculate_balance",
    "calculate_total_expenses",
    "calculate_savings",
    "calculate_savings_rate",
    "calculate_budget_remaining",
    "calculate_budget_usage",
    "calculate_daily_budget",
    # Commercial, Retail & Business Calculations
    "calculate_discounted_price",
    "calculate_tax",
    "calculate_total_with_tax",
    "split_amount",
    "calculate_unit_price",
    "calculate_profit",
    "calculate_profit_margin",
]
