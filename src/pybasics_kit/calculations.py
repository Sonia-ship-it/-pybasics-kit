"""All mathematical and financial calculations for PyBasics Kit.

PyBasics Kit is a lightweight Python toolkit for everyday mathematical and financial
calculations. It provides reusable, beginner-friendly functions designed for budgeting apps,
e-commerce platforms, school systems, business applications, and everyday Python scripts.
"""

import math
import statistics
from typing import Any, Iterable, Sequence, Union

Number = Union[int, float]


# ============================================================================
# 1. Mathematical & Statistical Calculations
# ============================================================================


def calculate_percentage(value: float, total: float) -> float:
    """Calculate what percentage a given value represents of a total.

    Args:
        value: The portion or part value.
        total: The whole or total value. Must not be zero.

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
    return float((value / total) * 100.0)


def calculate_average(numbers: Sequence[Number]) -> float:
    """Calculate the arithmetic mean of a sequence of numbers.

    Args:
        numbers: A non-empty sequence of numbers.

    Returns:
        The average value as a float.

    Raises:
        ValueError: If the sequence is empty.

    Example:
        >>> calculate_average([70, 80, 90])
        80.0
        >>> calculate_average([10, 20, 30])
        20.0
    """
    if not numbers:
        raise ValueError("Cannot calculate average of an empty sequence.")
    return float(sum(numbers) / len(numbers))


# Backward compatibility alias
average = calculate_average


def calculate_sum(numbers: Iterable[Number]) -> Number:
    """Calculate the sum of a collection or iterable of numbers.

    Args:
        numbers: An iterable of numbers.

    Returns:
        The sum of the numbers, or 0 if empty.

    Example:
        >>> calculate_sum([10, 20, 30])
        60
        >>> calculate_sum((1.5, 2.5, 3.0))
        7.0
    """
    return sum(numbers)


def calculate_median(numbers: Sequence[Number]) -> float:
    """Calculate the median (middle value) of a sequence of numbers.

    Args:
        numbers: A non-empty sequence of numbers.

    Returns:
        The median as a float.

    Raises:
        ValueError: If the sequence is empty.

    Example:
        >>> calculate_median([1, 3, 2])
        2.0
        >>> calculate_median([1, 2, 3, 4])
        2.5
    """
    if not numbers:
        raise ValueError("Cannot calculate median of an empty sequence.")
    return float(statistics.median(numbers))


def find_minimum(numbers: Iterable[Number]) -> Number:
    """Find the smallest number in a collection.

    Args:
        numbers: A non-empty iterable of numbers.

    Returns:
        The minimum number.

    Raises:
        ValueError: If the collection is empty.

    Example:
        >>> find_minimum([12, 5, 89, 3])
        3
    """
    try:
        return min(numbers)
    except (ValueError, TypeError):
        raise ValueError("Cannot find minimum of an empty sequence.")


def find_maximum(numbers: Iterable[Number]) -> Number:
    """Find the largest number in a collection.

    Args:
        numbers: A non-empty iterable of numbers.

    Returns:
        The maximum number.

    Raises:
        ValueError: If the collection is empty.

    Example:
        >>> find_maximum([12, 5, 89, 3])
        89
    """
    try:
        return max(numbers)
    except (ValueError, TypeError):
        raise ValueError("Cannot find maximum of an empty sequence.")


def is_prime(number: int) -> bool:
    """Determine whether an integer is a prime number.

    A prime number is a natural number greater than 1 that has no positive
    divisors other than 1 and itself.

    Args:
        number: The integer to test.

    Returns:
        True if the number is prime, False otherwise.

    Raises:
        TypeError: If number is not an integer.

    Example:
        >>> is_prime(7)
        True
        >>> is_prime(10)
        False
        >>> is_prime(1)
        False
    """
    if not isinstance(number, int) or isinstance(number, bool):
        raise TypeError(f"Expected integer, got {type(number).__name__}.")

    if number <= 1:
        return False
    if number == 2:
        return True
    if number % 2 == 0:
        return False

    limit = math.isqrt(number)
    for i in range(3, limit + 1, 2):
        if number % i == 0:
            return False

    return True


def calculate_percentage_change(old: float, new: float) -> float:
    """Calculate the percentage increase or decrease from an old value to a new value.

    Args:
        old: The initial baseline value. Must not be zero.
        new: The new or final value.

    Returns:
        The percentage change (positive for increase, negative for decrease).

    Raises:
        ValueError: If old is zero.

    Example:
        >>> calculate_percentage_change(100, 150)
        50.0
        >>> calculate_percentage_change(100, 80)
        -20.0
    """
    if old == 0:
        raise ValueError("Old value cannot be zero when calculating percentage change.")
    return float(((new - old) / old) * 100.0)


def clamp(value: Number, minimum: Number, maximum: Number) -> Number:
    """Restrict a value to be within a specified range [minimum, maximum].

    Args:
        value: The number to clamp.
        minimum: The lower bound of the allowed range.
        maximum: The upper bound of the allowed range.

    Returns:
        minimum if value < minimum,
        maximum if value > maximum,
        otherwise value.

    Raises:
        ValueError: If minimum is greater than maximum.

    Example:
        >>> clamp(15, 0, 10)
        10
        >>> clamp(-5, 0, 10)
        0
        >>> clamp(7, 0, 10)
        7
    """
    if minimum > maximum:
        raise ValueError(
            f"minimum ({minimum}) cannot be greater than maximum ({maximum})."
        )
    return max(minimum, min(value, maximum))


# ============================================================================
# 2. Personal Finance & Budgeting Calculations
# ============================================================================


def calculate_total_expenses(
    expenses: Union[Number, Iterable[Number], dict]
) -> Number:
    """Calculate total expenses from a sequence, dictionary, or single expense value.

    Args:
        expenses: An iterable of expense numbers, a dictionary of {category: amount},
            or a single expense amount.

    Returns:
        The total expense sum.

    Example:
        >>> calculate_total_expenses([100, 250, 50])
        400
        >>> calculate_total_expenses({"rent": 1200, "utilities": 150})
        1350
        >>> calculate_total_expenses(350)
        350
    """
    if isinstance(expenses, dict):
        return sum(expenses.values())
    if isinstance(expenses, (int, float)):
        return expenses
    return sum(expenses)


def calculate_balance(
    income: Number,
    expenses: Union[Number, Iterable[Number], dict],
) -> Number:
    """Calculate remaining balance after deducting expenses from income.

    Args:
        income: Total incoming funds or revenue.
        expenses: Total expenses as a number, sequence of expense items, or dictionary.

    Returns:
        Remaining balance (income - expenses).

    Example:
        >>> calculate_balance(1000, 350)
        650
        >>> calculate_balance(2000, [500, 300, 200])
        1000
    """
    total_exp = calculate_total_expenses(expenses)
    return income - total_exp


def calculate_savings(
    income: Number,
    expenses: Union[Number, Iterable[Number], dict],
) -> Number:
    """Calculate the remaining savings amount (net surplus) after expenses.

    Args:
        income: Total income received.
        expenses: Total expenses as a number, sequence of expense items, or dictionary.

    Returns:
        The remaining savings amount.

    Example:
        >>> calculate_savings(3000, 2200)
        800
        >>> calculate_savings(1000, 350)
        650
    """
    return calculate_balance(income, expenses)


def calculate_savings_rate(income: float, savings: float) -> float:
    """Calculate the savings rate percentage relative to total income.

    Args:
        income: Total income. Must be greater than zero.
        savings: Total savings amount.

    Returns:
        The savings rate as a percentage.

    Raises:
        ValueError: If income is zero or negative.

    Example:
        >>> calculate_savings_rate(5000, 1000)
        20.0
        >>> calculate_savings_rate(2000, 500)
        25.0
    """
    if income <= 0:
        raise ValueError("Income must be greater than zero when calculating savings rate.")
    return float((savings / income) * 100.0)


def calculate_budget_remaining(
    budget: Number,
    spending: Union[Number, Iterable[Number], dict],
) -> Number:
    """Calculate the remaining budget after actual spending.

    Args:
        budget: Total allocated budget.
        spending: Total spent as a number, sequence of spending entries, or dictionary.

    Returns:
        Remaining budget allowance (can be negative if overbudget).

    Example:
        >>> calculate_budget_remaining(500, 320)
        180
        >>> calculate_budget_remaining(1000, [200, 300, 100])
        400
    """
    total_spent = calculate_total_expenses(spending)
    return budget - total_spent


def calculate_budget_usage(
    spending: Union[Number, Iterable[Number], dict],
    budget: float,
) -> float:
    """Calculate the percentage of the budget that has been used.

    Args:
        spending: Amount spent as a number, sequence, or dictionary.
        budget: Total allocated budget. Must be greater than zero.

    Returns:
        The percentage of budget utilized.

    Raises:
        ValueError: If budget is zero or negative.

    Example:
        >>> calculate_budget_usage(250, 1000)
        25.0
        >>> calculate_budget_usage(500, 500)
        100.0
    """
    if budget <= 0:
        raise ValueError("Budget must be greater than zero when calculating budget usage.")
    total_spent = calculate_total_expenses(spending)
    return float((total_spent / budget) * 100.0)


def calculate_daily_budget(remaining: float, days: int) -> float:
    """Calculate daily budget allowance for remaining days in a period.

    Args:
        remaining: Remaining funds available in budget.
        days: Number of days left in the period. Must be greater than zero.

    Returns:
        Daily budget allowance as a float.

    Raises:
        ValueError: If days is zero or negative.

    Example:
        >>> calculate_daily_budget(300, 10)
        30.0
        >>> calculate_daily_budget(140, 7)
        20.0
    """
    if days <= 0:
        raise ValueError("Days must be greater than zero.")
    return float(remaining / days)


# ============================================================================
# 3. Commercial, Retail & Business Calculations
# ============================================================================


def calculate_discounted_price(price: float, discount_percent: float) -> float:
    """Calculate the price of an item after applying a percentage discount.

    Args:
        price: The original item price. Must not be negative.
        discount_percent: The discount rate as a percentage (0 to 100).

    Returns:
        The discounted price as a float.

    Raises:
        ValueError: If price is negative or discount_percent is not in [0, 100].

    Example:
        >>> calculate_discounted_price(100, 20)
        80.0
        >>> calculate_discounted_price(50, 10)
        45.0
    """
    if price < 0:
        raise ValueError("Price cannot be negative.")
    if discount_percent < 0 or discount_percent > 100:
        raise ValueError("Discount percentage must be between 0 and 100.")
    return float(price * (1.0 - (discount_percent / 100.0)))


def calculate_tax(amount: float, tax_rate: float) -> float:
    """Calculate the tax amount based on an amount and tax rate percentage.

    Args:
        amount: The subtotal amount subject to tax. Must not be negative.
        tax_rate: The tax rate expressed as a percentage (e.g., 15 for 15%). Must not be negative.

    Returns:
        The calculated tax amount as a float.

    Raises:
        ValueError: If amount or tax_rate is negative.

    Example:
        >>> calculate_tax(100, 15)
        15.0
        >>> calculate_tax(200, 8)
        16.0
    """
    if amount < 0:
        raise ValueError("Amount cannot be negative.")
    if tax_rate < 0:
        raise ValueError("Tax rate cannot be negative.")
    return float(amount * (tax_rate / 100.0))


def calculate_total_with_tax(amount: float, tax_rate: float) -> float:
    """Calculate the total price including tax.

    Args:
        amount: The subtotal amount subject to tax.
        tax_rate: The tax rate expressed as a percentage (e.g., 15 for 15%).

    Returns:
        The total price including tax as a float.

    Example:
        >>> calculate_total_with_tax(100, 15)
        115.0
        >>> calculate_total_with_tax(50, 10)
        55.0
    """
    return float(amount + calculate_tax(amount, tax_rate))


def split_amount(amount: float, people: int) -> float:
    """Divide a total amount equally among a specified number of people.

    Args:
        amount: Total monetary amount or bill to split.
        people: Number of people to split the amount among. Must be greater than zero.

    Returns:
        The share for each person as a float.

    Raises:
        ValueError: If people is zero or negative.

    Example:
        >>> split_amount(100, 4)
        25.0
        >>> split_amount(90, 3)
        30.0
    """
    if people <= 0:
        raise ValueError("Number of people must be greater than zero.")
    return float(amount / people)


def calculate_unit_price(total_price: float, quantity: Union[int, float]) -> float:
    """Calculate price per unit given total price and quantity.

    Args:
        total_price: Total cost of the items. Must not be negative.
        quantity: Number of units purchased. Must be greater than zero.

    Returns:
        The unit price as a float.

    Raises:
        ValueError: If total_price is negative or quantity is zero or negative.

    Example:
        >>> calculate_unit_price(50, 5)
        10.0
        >>> calculate_unit_price(100, 4)
        25.0
    """
    if total_price < 0:
        raise ValueError("Total price cannot be negative.")
    if quantity <= 0:
        raise ValueError("Quantity must be greater than zero.")
    return float(total_price / quantity)


def calculate_profit(
    revenue: Number,
    costs: Union[Number, Iterable[Number], dict],
) -> Number:
    """Calculate profit by subtracting total costs from total revenue.

    Args:
        revenue: Total incoming revenue.
        costs: Total costs as a number, sequence of costs, or dictionary of expense items.

    Returns:
        The calculated profit (revenue - costs).

    Example:
        >>> calculate_profit(1000, 700)
        300
        >>> calculate_profit(5000, [1500, 1000, 500])
        2000
    """
    total_costs = calculate_total_expenses(costs)
    return revenue - total_costs


def calculate_profit_margin(revenue: float, profit: float) -> float:
    """Calculate profit margin as a percentage of total revenue.

    Args:
        revenue: Total revenue generated. Must not be zero.
        profit: Net profit earned.

    Returns:
        Profit margin percentage as a float.

    Raises:
        ValueError: If revenue is zero.

    Example:
        >>> calculate_profit_margin(1000, 200)
        20.0
        >>> calculate_profit_margin(500, 100)
        20.0
    """
    if revenue == 0:
        raise ValueError("Revenue cannot be zero when calculating profit margin.")
    return float((profit / revenue) * 100.0)
