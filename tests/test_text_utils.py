"""Unit tests for text_utils module."""

import pytest
from pybasics_kit.text_utils import count_words, slugify, truncate


class TestCountWords:
    def test_simple_string(self):
        assert count_words("Hello world") == 2

    def test_string_with_extra_whitespace(self):
        assert count_words("  Python   is   great  ") == 3

    def test_multiline_and_tabs(self):
        assert count_words("One\ttwo\nthree  four") == 4

    def test_empty_string(self):
        assert count_words("") == 0

    def test_whitespace_only(self):
        assert count_words("   \t\n  ") == 0

    def test_invalid_type_raises_error(self):
        with pytest.raises(TypeError):
            count_words(12345)  # type: ignore


class TestSlugify:
    def test_standard_slug(self):
        assert slugify("Hello World From Python!") == "hello-world-from-python"

    def test_special_characters_and_punctuation(self):
        assert slugify("Fast & Furious: Tokyo Drift") == "fast-furious-tokyo-drift"

    def test_accents_and_unicode(self):
        assert slugify("Crème Brûlée & Café") == "creme-brulee-cafe"

    def test_multiple_consecutive_separators_and_spaces(self):
        assert slugify("   Multiple   ---   Spaces   ") == "multiple-spaces"

    def test_custom_separator(self):
        assert slugify("Hello World", separator="_") == "hello_world"

    def test_invalid_type_raises_error(self):
        with pytest.raises(TypeError):
            slugify(None)  # type: ignore


class TestTruncate:
    def test_short_string_not_truncated(self):
        assert truncate("Short", 10) == "Short"

    def test_exact_length_string_not_truncated(self):
        assert truncate("Exact", 5) == "Exact"

    def test_long_string_truncated(self):
        assert truncate("Python Programming", 10) == "Python ..."
        assert len(truncate("Python Programming", 10)) == 10

    def test_custom_suffix(self):
        assert truncate("Long sentence goes here", 10, suffix="*") == "Long sent*"

    def test_max_length_less_than_suffix_raises_error(self):
        with pytest.raises(ValueError, match="max_length.*must be at least"):
            truncate("Hello", 2, suffix="...")
