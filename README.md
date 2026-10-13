# 🧮 PyBasics Kit (`pybasics-kit`)

[![Python Versions](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Tests](https://img.shields.io/badge/tests-passing-brightgreen.svg)]()

> **A lightweight Python toolkit for everyday mathematical and financial calculations.**

`pybasics-kit` is a zero-dependency, beginner-friendly Python utility library built following modern packaging standards (PEP 517/518/621, `pyproject.toml`, and the standard `src/` layout). It brings together essential numerical, statistical, personal budgeting, retail, and commercial calculations into a single, cohesive module (`calculations.py`).

Whether you are building budgeting apps, e-commerce checkout platforms, school gradebooks, business reporting dashboards, or everyday Python scripts, `pybasics-kit` eliminates repetitive boilerplate code with reliable, thoroughly tested calculations.

---

## 📑 Table of Contents

- [Features](#-features)
- [Project Architecture](#-project-architecture)
- [Installation](#-installation)
- [Quick Start](#-quick-start)
- [Function Reference](#-function-reference)
  - [1. Mathematical & Statistical Calculations](#1-mathematical--statistical-calculations)
  - [2. Personal Finance & Budgeting](#2-personal-finance--budgeting)
  - [3. Commercial, Retail & Business](#3-commercial-retail--business)
- [Usage Examples](#-usage-examples)
- [Development & Testing](#-development--testing)
- [Building & Packaging](#-building--packaging)
- [License](#-license)

---

## ✨ Features

- **Single Intuitive Module**: Everything lives in `calculations.py`, importable directly from `pybasics_kit`.
- **Zero Third-Party Dependencies**: Pure Python standard library implementation (`math`, `statistics`).
- **Completely Independent**: Decoupled from any framework or database (no Django, Flask, or ORM dependencies).
- **Flexible Inputs**: Financial and aggregation functions seamlessly accept floats, integers, lists, tuples, or categorized dictionaries.
- **Robust Error Handling**: Explicit validation with descriptive `ValueError` and `TypeError` messages for zero denominators, invalid ranges, and negative dimensions.
- **100% Tested**: Comprehensive unit test suite covering nominal cases, boundary conditions, and edge cases.

---

## 🏛️ Project Architecture

```text
pybasics-kit/
│
├── src/
│   └── pybasics_kit/
│       ├── __init__.py          # Exports public calculation functions
│       └── calculations.py      # All mathematical and financial calculation logic
│
├── tests/
│   ├── __init__.py
│   └── test_calculations.py    # Comprehensive test suite (90+ assertions)
│
├── pyproject.toml               # PEP 621 build configuration
├── README.md                    # Documentation and reference
└── LICENSE                      # MIT License
```

---

## 📦 Installation

### Standard Installation (PyPI)

```bash
pip install pybasics-kit
```

### Lab / TestPyPI Installation

```bash
python -m pip install --index-url https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple/ pybasics-kit
```

---

## 🚀 Quick Start

Import functions directly from `pybasics_kit`:

```python
from pybasics_kit import (
    calculate_percentage,
    calculate_average,
    calculate_discounted_price,
    calculate_balance,
)

print(calculate_percentage(25, 100))        # 25.0
print(calculate_average([70, 80, 90]))       # 80.0
print(calculate_discounted_price(100, 20))  # 80.0
print(calculate_balance(1000, 350))         # 650
```

---

## 📚 Function Reference

### 1. Mathematical & Statistical Calculations

| Function | Signature | What it calculates |
| :--- | :--- | :--- |
| `calculate_percentage` | `(value, total)` | Percentage of a total |
| `calculate_average` | `(numbers)` | Arithmetic mean of numbers |
| `calculate_sum` | `(numbers)` | Total sum of numbers |
| `calculate_median` | `(numbers)` | Median (middle value) of numbers |
| `find_minimum` | `(numbers)` | Smallest number in a collection |
| `find_maximum` | `(numbers)` | Largest number in a collection |
| `is_prime` | `(number)` | Whether an integer is prime |
| `calculate_percentage_change` | `(old, new)` | Percentage increase or decrease |
| `clamp` | `(value, minimum, maximum)` | Restricts value within a given range |

### 2. Personal Finance & Budgeting

| Function | Signature | What it calculates |
| :--- | :--- | :--- |
| `calculate_balance` | `(income, expenses)` | Remaining balance after expenses |
| `calculate_total_expenses` | `(expenses)` | Total expenses (supports lists or categorized dicts) |
| `calculate_savings` | `(income, expenses)` | Remaining savings amount (net surplus) |
| `calculate_savings_rate` | `(income, savings)` | Savings percentage of total income |
| `calculate_budget_remaining` | `(budget, spending)` | Remaining budget allowance |
| `calculate_budget_usage` | `(spending, budget)` | Percentage of budget consumed |
| `calculate_daily_budget` | `(remaining, days)` | Daily spending allowance |

### 3. Commercial, Retail & Business

| Function | Signature | What it calculates |
| :--- | :--- | :--- |
| `calculate_discounted_price` | `(price, discount_percent)` | Price after a percentage discount |
| `calculate_tax` | `(amount, tax_rate)` | Tax amount for a given tax percentage |
| `calculate_total_with_tax` | `(amount, tax_rate)` | Total amount including tax |
| `split_amount` | `(amount, people)` | Equal division of an amount |
| `calculate_unit_price` | `(total_price, quantity)` | Price per unit |
| `calculate_profit` | `(revenue, costs)` | Net profit after costs |
| `calculate_profit_margin` | `(revenue, profit)` | Profit margin percentage |

---

## 💡 Usage Examples

### Everyday Math & Statistics

```python
from pybasics_kit import (
    calculate_percentage,
    calculate_average,
    calculate_median,
    find_minimum,
    find_maximum,
    is_prime,
    calculate_percentage_change,
    clamp,
)

# Exam grading & score analysis
scores = [75, 88, 92, 64, 85]
print(calculate_average(scores))             # 80.8
print(calculate_median(scores))              # 85.0
print(find_minimum(scores))                  # 64
print(find_maximum(scores))                  # 92

# Safe clamping within range [0, 100]
print(clamp(115, 0, 100))                    # 100
print(clamp(-10, 0, 100))                    # 0

# Growth analysis
print(calculate_percentage_change(100, 125)) # 25.0 (25% increase)
print(calculate_percentage_change(200, 150)) # -25.0 (25% decrease)

# Prime number testing
print(is_prime(17))                          # True
print(is_prime(4))                           # False
```

### Personal Budgeting & Financial Planning

```python
from pybasics_kit import (
    calculate_balance,
    calculate_savings_rate,
    calculate_budget_remaining,
    calculate_budget_usage,
    calculate_daily_budget,
)

monthly_income = 4000
monthly_expenses = {"rent": 1200, "groceries": 450, "utilities": 150}

# Balance and savings
balance = calculate_balance(monthly_income, monthly_expenses)
print(f"Remaining balance: ${balance}")       # $2200

savings_rate = calculate_savings_rate(monthly_income, balance)
print(f"Savings rate: {savings_rate}%")       # 55.0%

# Track monthly budget
budget = 2000
spending = [350, 420, 130]
print(calculate_budget_remaining(budget, spending)) # 1100
print(calculate_budget_usage(spending, budget))     # 45.0%

# Days remaining in period
print(calculate_daily_budget(1100, 22))             # 50.0 ($50/day)
```

### E-Commerce & Retail Checkout

```python
from pybasics_kit import (
    calculate_discounted_price,
    calculate_tax,
    calculate_total_with_tax,
    split_amount,
    calculate_unit_price,
    calculate_profit,
    calculate_profit_margin,
)

# Apply 20% discount on $150 item
subtotal = calculate_discounted_price(150, 20)
print(f"Discounted subtotal: ${subtotal}")    # $120.0

# 8.25% sales tax
tax = calculate_tax(subtotal, 8.25)
total = calculate_total_with_tax(subtotal, 8.25)
print(f"Tax: ${tax:.2f}, Total: ${total:.2f}")# Tax: $9.90, Total: $129.90

# Split restaurant bill among 4 friends
print(split_amount(129.90, 4))               # 32.475

# Unit economics & business reporting
unit_cost = calculate_unit_price(500, 100)   # 5.0 ($5 per unit)
profit = calculate_profit(10000, 7500)       # 2500
margin = calculate_profit_margin(10000, profit) # 25.0%
```

---

## 🧪 Development & Testing

Run all unit tests using `pytest`:

```bash
python -m pytest -v
```

All 23 functions are thoroughly tested with 90+ test cases covering standard operations, empty inputs, zero divisions, boundary limits, and parameter validation.

---

## 🛠️ Building & Packaging

Build distribution archives (wheel and source distribution) with PEP 517 `build`:

```bash
python -m build
```

Verify build output with `twine`:

```bash
python -m twine check dist/*
```

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).
