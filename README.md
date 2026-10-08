# 🧰 pybasics_kit

[![Python Versions](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

> **The Swiss Army Knife utility library for everyday Python workflows.**

`pybasics_kit` is a lightweight, zero-dependency Python utility package designed to eliminate repetitive boilerplate code. Built following modern packaging standards (PEP 621, `pyproject.toml`, and the standard `src/` layout), it offers clean, beginner-friendly tools for everyday calculations, string transformations, unit conversions, and mini-games.

---

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Quick Start](#quick-start)
- [Usage Examples](#usage-examples)
  - [Math Utilities](#1-math-utilities)
  - [Text Utilities](#2-text-utilities)
  - [Unit Conversions](#3-unit-conversions)
  - [Game Utilities](#4-game-utilities)
- [API Reference](#api-reference)
- [Development Setup](#development-setup)
- [Running Tests](#running-tests)
- [Building the Package](#building-the-package)
- [Publishing to TestPyPI](#publishing-to-testpypi)
- [License](#license)

---

## Features

- 🧮 **Math Utilities**: Percentage calculation with zero-division validation, prime number checking, numerical clamping, and sequence averages.
- 📝 **Text Utilities**: Intelligent whitespace-aware word counting, URL-friendly slug generation with unicode normalization, and safe string truncation.
- 🌡️ **Unit Conversions**: Bidirectional Celsius ↔ Fahrenheit temperature conversions and Kilograms ↔ Pounds weight conversions.
- 🎲 **Game Utilities**: Configurable virtual dice rolling and coin flipping with optional deterministic seed support for reproducible testing.
- 📦 **Modern Standards**: Compliant with PEP 517/518/621, structured with the secure `src/` layout, fully type-hinted, and thoroughly tested with `pytest`.

---

## Installation

### Standard Installation (PyPI)

Once published to PyPI, install via standard `pip`:

```bash
pip install pybasics-kit
```

### Lab / TestPyPI Installation

During testing, install the distribution package from **TestPyPI**:

```bash
python -m pip install --index-url https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple/ pybasics-kit
```

> **Why `--extra-index-url`?**  
> TestPyPI is an isolated testing index and does not mirror all standard PyPI packages. Including `--extra-index-url https://pypi.org/simple/` ensures pip can locate any third-party dependencies from the primary PyPI index if required.

---

## Quick Start

You can import utilities either directly from the root package or from individual modules:

```python
import pybasics_kit

# Convenient top-level access
from pybasics_kit import is_prime, slugify, celsius_to_fahrenheit, roll_dice

print(is_prime(17))                   # True
print(slugify("Hello World!"))        # "hello-world"
print(celsius_to_fahrenheit(25))      # 77.0
print(roll_dice())                    # 1 to 6
```

---

## Usage Examples

### 1. Math Utilities

```python
from pybasics_kit.math_utils import calculate_percentage, is_prime, clamp, average

# Calculate percentages safely
print(calculate_percentage(25, 100))  # 25.0
print(calculate_percentage(1, 4))     # 25.0

# Efficient prime checking
print(is_prime(17))  # True
print(is_prime(10))  # False
print(is_prime(1))   # False

# Restrict values within a range
print(clamp(15, 0, 10))  # 10
print(clamp(-5, 0, 10))  # 0

# Arithmetic mean
print(average([10, 20, 30]))  # 20.0
```

### 2. Text Utilities

```python
from pybasics_kit.text_utils import count_words, slugify, truncate

# Whitespace-resilient word counting
print(count_words("Python is awesome"))             # 3
print(count_words("  Tabs\tand   newlines\ncount! "))  # 4

# Web-safe slug generator
print(slugify("Hello World From Python!"))         # "hello-world-from-python"
print(slugify("Café & Crème Brûlée!"))             # "cafe-creme-brulee"

# Text truncator
print(truncate("Long article headline here", 15))  # "Long article..."
```

### 3. Unit Conversions

```python
from pybasics_kit.conv_utils import (
    celsius_to_fahrenheit,
    fahrenheit_to_celsius,
    kg_to_pounds,
    pounds_to_kg,
)

# Temperature
print(celsius_to_fahrenheit(0))     # 32.0 (freezing)
print(celsius_to_fahrenheit(100))   # 212.0 (boiling)
print(fahrenheit_to_celsius(212))   # 100.0

# Weight
print(kg_to_pounds(1))              # 2.20462
print(pounds_to_kg(2.20462))        # 1.0
```

### 4. Game Utilities

```python
from pybasics_kit.game_utils import roll_dice, flip_coin

# Virtual dice
print(roll_dice())         # Random integer 1 to 6
print(roll_dice(20))       # Random integer 1 to 20 (D20)

# Coin flip
print(flip_coin())         # "Heads" or "Tails"

# Deterministic coin flip (reproducible testing without altering global state)
print(flip_coin(seed=42))  # Always "Heads"
```

---

## API Reference

### `pybasics_kit.math_utils`
- `calculate_percentage(value: float, total: float) -> float`: Calculates `(value / total) * 100.0`. Raises `ValueError` if `total == 0`.
- `is_prime(number: int) -> bool`: Efficient $O(\sqrt{n})$ prime test. Returns `False` for integers $\le 1$.
- `clamp(value: float, min_value: float, max_value: float) -> float`: Constrains `value` to `[min_value, max_value]`.
- `average(numbers: Sequence[float]) -> float`: Computes arithmetic mean. Raises `ValueError` if sequence is empty.

### `pybasics_kit.text_utils`
- `count_words(text: str) -> int`: Counts words using whitespace splitting (`split()`), handling arbitrary spacing.
- `slugify(text: str, separator: str = "-") -> str`: Normalizes unicode, lowercases, removes non-alphanumeric punctuation, and joins with `separator`.
- `truncate(text: str, max_length: int, suffix: str = "...") -> str`: Shortens string if longer than `max_length`.

### `pybasics_kit.conv_utils`
- `celsius_to_fahrenheit(celsius: float) -> float`: Converts °C to °F via `(C * 9/5) + 32`.
- `fahrenheit_to_celsius(fahrenheit: float) -> float`: Converts °F to °C via `(F - 32) * 5/9`.
- `kg_to_pounds(kg: float) -> float`: Converts kilograms to pounds (factor `2.20462`). Raises `ValueError` for negative values.
- `pounds_to_kg(pounds: float) -> float`: Converts pounds to kilograms. Raises `ValueError` for negative values.

### `pybasics_kit.game_utils`
- `roll_dice(faces: int = 6, seed: Optional[int] = None) -> int`: Returns random integer in `[1, faces]`. Validates `faces >= 2`.
- `flip_coin(seed: Optional[int] = None) -> str`: Returns `"Heads"` or `"Tails"`. Accepts optional `seed` for isolated deterministic runs.

---

## Development Setup

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Sonia-ship-it/pybasics-kit.git
   cd pybasics-kit
   ```

2. **Create and activate a virtual environment**:
   - **Windows PowerShell**:
     ```powershell
     python -m venv .venv
     .\.venv\Scripts\Activate.ps1
     ```
   - **Windows Command Prompt (CMD)**:
     ```cmd
     python -m venv .venv
     .venv\Scripts\activate.bat
     ```
   - **Linux / macOS**:
     ```bash
     python3 -m venv .venv
     source .venv/bin/activate
     ```

3. **Install development tools and package in editable mode**:
   ```bash
   python -m pip install --upgrade pip
   python -m pip install build twine pytest
   python -m pip install -e .
   ```

---

## Running Tests

Run the full pytest suite:

```bash
python -m pytest
```

With verbose output:

```bash
python -m pytest -v
```

---

## Building the Package

Build the source distribution (`.tar.gz`) and wheel (`.whl`):

```bash
python -m build
```

The output artifacts will be created in the `dist/` directory:
- `dist/pybasics_kit-0.1.0-py3-none-any.whl` (Wheel distribution)
- `dist/pybasics_kit-0.1.0.tar.gz` (Source distribution)

---

## Publishing to TestPyPI

Upload the built distributions to TestPyPI using **Twine**:

```bash
python -m twine upload --repository testpypi dist/*
```

When prompted:
- **Username**: `__token__`
- **Password**: *Paste your TestPyPI API token (begins with `pypi-...`)*

> 🔒 **Security Notice:**  
> Never commit your API token, passwords, or credentials into source control (`git`), `pyproject.toml`, or any project documentation. Keep your tokens safe and private.

---

## License

This project is licensed under the [MIT License](LICENSE) - see the [LICENSE](LICENSE) file for details.
