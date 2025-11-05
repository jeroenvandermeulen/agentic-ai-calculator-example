"""
Test module for calculator logic.
Following TDD approach: Red-Green-Refactor.
"""
import pytest
from src.calculator import Calculator


class TestCalculator:
    """Test suite for Calculator class."""

    def test_add_two_positive_numbers(self):
        """Test addition of two positive numbers."""
        calc = Calculator()
        result = calc.add(5, 3)
        assert result == 8

    def test_add_negative_numbers(self):
        """Test addition with negative numbers."""
        calc = Calculator()
        result = calc.add(-5, -3)
        assert result == -8

    def test_add_with_zero(self):
        """Test addition with zero."""
        calc = Calculator()
        result = calc.add(5, 0)
        assert result == 5

    def test_subtract_two_numbers(self):
        """Test subtraction of two numbers."""
        calc = Calculator()
        result = calc.subtract(10, 3)
        assert result == 7

    def test_multiply_two_numbers(self):
        """Test multiplication of two numbers."""
        calc = Calculator()
        result = calc.multiply(4, 5)
        assert result == 20

    def test_divide_two_numbers(self):
        """Test division of two numbers."""
        calc = Calculator()
        result = calc.divide(20, 4)
        assert result == 5

    def test_divide_by_zero_raises_error(self):
        """Test that division by zero raises a ValueError."""
        calc = Calculator()
        with pytest.raises(ValueError, match="Cannot divide by zero"):
            calc.divide(10, 0)
