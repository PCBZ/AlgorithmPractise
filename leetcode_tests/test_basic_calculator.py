"""
Unit tests for basic_calculator.py
Tests the Basic Calculator solution with different operators and expressions.
"""

import pytest

from leetcode.basic_calculator import Solution



class TestBasicCalculator:
    """Test class for basic calculator functionality."""

    def setup_method(self):
        """Set up test fixtures before each test method."""
        self.solution = Solution()

    def test_simple_addition(self):
        """Test simple addition."""
        assert self.solution.calculate("1 + 1") == 2
        assert self.solution.calculate("2 + 3") == 5

    def test_simple_subtraction(self):
        """Test simple subtraction."""
        assert self.solution.calculate("2 - 1") == 1
        assert self.solution.calculate("5 - 3") == 2

    def test_mixed_addition_subtraction(self):
        """Test mixed addition and subtraction."""
        assert self.solution.calculate("2-1 + 2") == 3
        assert self.solution.calculate(" 2-1 + 2 ") == 3  # With spaces

    def test_single_number(self):
        """Test single number expressions."""
        assert self.solution.calculate("42") == 42
        assert self.solution.calculate(" 42 ") == 42

    def test_negative_numbers(self):
        """Test expressions starting with negative numbers."""
        assert self.solution.calculate("-1") == -1
        assert self.solution.calculate("-1 + 2") == 1
        assert self.solution.calculate("-2 - 3") == -5

    def test_parentheses_simple(self):
        """Test simple parentheses."""
        assert self.solution.calculate("(1)") == 1
        assert self.solution.calculate("(1 + 2)") == 3
        # Note: calculate method only supports +, -, (, ) - no multiplication

    def test_parentheses_basic(self):
        """Test basic parentheses (only + and -)."""
        assert self.solution.calculate("(1)") == 1
        assert self.solution.calculate("(1 + 2)") == 3
        assert self.solution.calculate("2 - (1 + 2)") == -1

    def test_nested_parentheses(self):
        """Test nested parentheses."""
        assert self.solution.calculate("((1))") == 1
        assert self.solution.calculate("(1 + (2))") == 3
        assert self.solution.calculate("(1 + (2 + 3))") == 6
        assert self.solution.calculate("((1 + 2) + 3)") == 6

    def test_complex_expressions(self):
        """Test complex expressions with parentheses."""
        assert self.solution.calculate("(1+(4+5+2)-3)+(6+8)") == 23
        assert self.solution.calculate("1 + (2 - (3 + 4))") == -4

    def test_whitespace_handling(self):
        """Test expressions with various whitespace."""
        assert self.solution.calculate("1+2") == 3
        assert self.solution.calculate(" 1 + 2 ") == 3
        assert self.solution.calculate("1  +   2") == 3

    def test_zero_handling(self):
        """Test expressions with zeros."""
        assert self.solution.calculate("0") == 0
        assert self.solution.calculate("0 + 0") == 0
        assert self.solution.calculate("1 - 1") == 0
        assert self.solution.calculate("(0)") == 0

    # Tests for calculate2 (with *, /)
    def test_calculate2_multiplication(self):
        """Test multiplication in calculate2."""
        assert self.solution.calculate2("2 * 3") == 6
        assert self.solution.calculate2("3*2*2") == 12

    def test_calculate2_division(self):
        """Test division in calculate2."""
        assert self.solution.calculate2("6 / 2") == 3
        assert self.solution.calculate2("8/2") == 4

    def test_calculate2_operator_precedence(self):
        """Test operator precedence in calculate2."""
        assert self.solution.calculate2("3+2*2") == 7  # 3 + (2*2) = 7
        assert self.solution.calculate2("2*3+1") == 7  # (2*3) + 1 = 7
        assert self.solution.calculate2("6/2+1") == 4  # (6/2) + 1 = 4

    def test_calculate2_complex_precedence(self):
        """Test complex expressions with precedence."""
        assert self.solution.calculate2("14-3*2") == 8   # 14 - (3*2) = 8
        assert self.solution.calculate2("1*2-3/3") == 1  # (1*2) - (3/3) = 1

    def test_calculate2_negative_division(self):
        """Test division with negative results."""
        assert self.solution.calculate2("10/5") == 2
        assert self.solution.calculate2("0-10/5") == -2  # Equivalent to -(10/5)
        # Note: algorithm doesn't handle negative numbers after operators like "10/-5"

    def test_parametrized_calculate_cases(self):
        """Test multiple cases for calculate method."""
        test_cases = [
            ("1", 1),
            ("1 + 1", 2),
            ("2 - 1", 1),
            ("(1)", 1),
            ("2-(1+2)", -1),
            ("(1+(4+5+2)-3)+(6+8)", 23),
        ]
        
        for expression, expected in test_cases:
            result = self.solution.calculate(expression)
            assert result == expected, f"Failed for '{expression}': got {result}, expected {expected}"

    def test_parametrized_calculate2_cases(self):
        """Test multiple cases for calculate2 method."""
        test_cases = [
            ("3+2*2", 7),
            ("3*2", 6),
            ("6/3", 2),
            ("14-3*2", 8),
            ("1+2*3", 7),
            ("2*3*2", 12),
        ]
        
        for expression, expected in test_cases:
            result = self.solution.calculate2(expression)
            assert result == expected, f"Failed for '{expression}': got {result}, expected {expected}"

    def test_large_numbers(self):
        """Test with larger numbers."""
        assert self.solution.calculate("100 + 200") == 300
        assert self.solution.calculate("1000 - 999") == 1
        assert self.solution.calculate2("100 * 2") == 200

    def test_edge_cases(self):
        """Test edge cases."""
        # Single digit
        assert self.solution.calculate("5") == 5
        
        # Multiple operations
        assert self.solution.calculate("1 + 2 + 3 + 4") == 10
        assert self.solution.calculate("10 - 1 - 2 - 3") == 4

    def test_consistency(self):
        """Test that methods are consistent for repeated calls."""
        expression1 = "1 + 2 - 3"
        expression2 = "2 * 3 + 1"
        
        # Multiple calls should return same result
        assert self.solution.calculate(expression1) == self.solution.calculate(expression1)
        assert self.solution.calculate2(expression2) == self.solution.calculate2(expression2)

    def test_expression_validation(self):
        """Test that expressions are properly evaluated."""
        # Test that we get the correct mathematical results
        test_expressions = [
            ("1 + 2 * 3", 7, 2),  # (expression, calculate2_result, calculate_would_fail)
            ("(1 + 2) - 3", 0, 1),  # calculate result
        ]
        
        # Only test calculate2 for expressions with * or /
        assert self.solution.calculate2("1 + 2 * 3") == 7
        assert self.solution.calculate("(1 + 2) - 3") == 0


if __name__ == "__main__":
    pytest.main([__file__])
