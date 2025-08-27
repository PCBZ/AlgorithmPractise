"""
Test cases for LeetCode Problem #592: Fraction Addition and Subtraction
"""
import unittest
import sys
import os

# Add the parent directory to the Python path
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parent_dir)

# Import using importlib
import importlib.util
spec = importlib.util.spec_from_file_location(
    "solution",
    os.path.join(parent_dir, "leetcode", "fraction_addition_and_subtraction.py")
)
solution_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(solution_module)
Solution = solution_module.Solution


class TestFractionAdditionAndSubtraction(unittest.TestCase):
    """Test cases for the FractionAdditionAndSubtraction solution."""

    def setUp(self):
        """Set up test fixtures before each test method."""
        self.solution = Solution()

    def test_example_case_1(self):
        """Test first example case - basic subtraction."""
        expression = "1/3-1/2"
        result = self.solution.fractionAddition(expression)
        expected = "-1/6"
        assert result == expected

    def test_example_case_2(self):
        """Test second example case - adding to zero."""
        expression = "-1/2+1/2"
        result = self.solution.fractionAddition(expression)
        expected = "0/1"
        assert result == expected

    def test_example_case_3(self):
        """Test third example case - multiple operations."""
        expression = "-1/2+1/2+1/3"
        result = self.solution.fractionAddition(expression)
        expected = "1/3"
        assert result == expected

    def test_single_fraction_positive(self):
        """Test single positive fraction."""
        expression = "1/2"
        result = self.solution.fractionAddition(expression)
        expected = "1/2"
        assert result == expected

    def test_single_fraction_negative(self):
        """Test single negative fraction."""
        expression = "-1/2"
        result = self.solution.fractionAddition(expression)
        expected = "-1/2"
        assert result == expected

    def test_two_fractions_addition(self):
        """Test simple addition of two fractions."""
        expression = "1/3+1/4"
        result = self.solution.fractionAddition(expression)
        expected = "7/12"
        assert result == expected

    def test_two_fractions_subtraction(self):
        """Test simple subtraction of two fractions."""
        expression = "3/4-1/4"
        result = self.solution.fractionAddition(expression)
        expected = "1/2"
        assert result == expected

    def test_same_denominator_addition(self):
        """Test addition with same denominators."""
        expression = "1/6+2/6"
        result = self.solution.fractionAddition(expression)
        expected = "1/2"
        assert result == expected

    def test_same_denominator_subtraction(self):
        """Test subtraction with same denominators."""
        expression = "5/3-2/3"
        result = self.solution.fractionAddition(expression)
        expected = "1/1"
        assert result == expected

    def test_multiple_additions(self):
        """Test multiple addition operations."""
        expression = "1/3+1/4+1/5"
        result = self.solution.fractionAddition(expression)
        expected = "47/60"
        assert result == expected

    def test_multiple_subtractions(self):
        """Test multiple subtraction operations."""
        expression = "1/2-1/3-1/6"
        result = self.solution.fractionAddition(expression)
        expected = "0/1"
        assert result == expected

    def test_mixed_operations(self):
        """Test mixed addition and subtraction."""
        expression = "1/2-1/3+1/4"
        result = self.solution.fractionAddition(expression)
        expected = "5/12"
        assert result == expected

    def test_complex_expression(self):
        """Test complex expression with multiple operations."""
        expression = "-1/4-1/2+3/4"
        result = self.solution.fractionAddition(expression)
        expected = "0/1"
        assert result == expected

    def test_improper_fractions(self):
        """Test with improper fractions."""
        expression = "5/3+1/3"
        result = self.solution.fractionAddition(expression)
        expected = "2/1"
        assert result == expected

    def test_negative_result(self):
        """Test expressions that result in negative fractions."""
        expression = "1/4-3/4"
        result = self.solution.fractionAddition(expression)
        expected = "-1/2"
        assert result == expected

    def test_zero_result_different_ways(self):
        """Test different expressions that result in zero."""
        test_cases = [
            ("-1/2+1/2", "0/1"),
            ("1/3-1/3", "0/1"),
            ("1/4+1/4-1/2", "0/1"),
            ("-1/6+1/6", "0/1"),
        ]
        
        for expr, expected in test_cases:
            with self.subTest(expression=expr):
                result = self.solution.fractionAddition(expr)
                assert result == expected

    def test_fraction_reduction(self):
        """Test that fractions are properly reduced."""
        expression = "2/4+2/4"
        result = self.solution.fractionAddition(expression)
        expected = "1/1"
        assert result == expected

    def test_large_numerators_denominators(self):
        """Test with larger numbers."""
        expression = "7/10+2/5"
        result = self.solution.fractionAddition(expression)
        expected = "11/10"
        assert result == expected

    def test_consecutive_negative_signs(self):
        """Test parsing with negative fractions."""
        expression = "-1/2-1/3"
        result = self.solution.fractionAddition(expression)
        expected = "-5/6"
        assert result == expected

    def test_leading_positive_sign(self):
        """Test with explicit leading positive sign."""
        expression = "+1/2+1/3"
        result = self.solution.fractionAddition(expression)
        expected = "5/6"
        assert result == expected

    def test_return_type_and_format(self):
        """Test return type and format."""
        result = self.solution.fractionAddition("1/2+1/3")
        assert isinstance(result, str)
        assert "/" in result
        parts = result.split("/")
        assert len(parts) == 2
        # Check that numerator and denominator are integers
        assert parts[0].lstrip("-").isdigit()
        assert parts[1].isdigit()

    def test_lowest_terms_property(self):
        """Test that results are always in lowest terms."""
        test_cases = [
            ("2/4+2/8", "3/4"),   # Should reduce intermediate calculations
            ("3/9+2/6", "2/3"),   # Should reduce final result
            ("4/12+6/18", "2/3"), # Multiple reductions needed
        ]
        
        for expr, expected in test_cases:
            with self.subTest(expression=expr):
                result = self.solution.fractionAddition(expr)
                assert result == expected

    def test_parsing_correctness(self):
        """Test that expression parsing is correct."""
        # Test edge cases in parsing
        expression = "1/10-1/2"
        result = self.solution.fractionAddition(expression)
        expected = "-2/5"
        assert result == expected

    def test_lcm_calculation(self):
        """Test LCM calculation with various denominators."""
        expression = "1/6+1/8+1/12"
        result = self.solution.fractionAddition(expression)
        # LCM of 6, 8, 12 is 24
        # 1/6 = 4/24, 1/8 = 3/24, 1/12 = 2/24
        # Sum = 9/24 = 3/8
        expected = "3/8"
        assert result == expected

    def test_gcd_reduction(self):
        """Test GCD reduction in final result."""
        expression = "6/8+9/12"
        result = self.solution.fractionAddition(expression)
        # 6/8 + 9/12 = 3/4 + 3/4 = 6/4 = 3/2
        expected = "3/2"
        assert result == expected

    def test_expression_with_ones(self):
        """Test expressions involving 1 as denominator."""
        expression = "1/1+1/2"
        result = self.solution.fractionAddition(expression)
        expected = "3/2"
        assert result == expected

    def test_alternating_signs(self):
        """Test expression with alternating signs."""
        expression = "1/2-1/3+1/4-1/5"
        result = self.solution.fractionAddition(expression)
        # Calculate manually: 30/60 - 20/60 + 15/60 - 12/60 = 13/60
        expected = "13/60"
        assert result == expected

    def test_performance_many_fractions(self):
        """Test performance with many fractions."""
        # Create expression with multiple fractions
        fractions = [f"1/{i}" for i in range(2, 12)]
        expression = "+".join(fractions)
        result = self.solution.fractionAddition(expression)
        
        # Should handle this efficiently and return valid fraction
        assert isinstance(result, str)
        assert "/" in result

    def test_edge_case_single_digit_numbers(self):
        """Test with single digit numbers."""
        expression = "1/2+1/3+1/4+1/5+1/6"
        result = self.solution.fractionAddition(expression)
        
        # Should compute correctly
        assert isinstance(result, str)
        assert "/" in result

    def test_mathematical_correctness(self):
        """Test mathematical correctness with known results."""
        test_cases = [
            ("1/2+1/2", "1/1"),      # 0.5 + 0.5 = 1
            ("3/4-1/4", "1/2"),      # 0.75 - 0.25 = 0.5  
            ("1/3+2/3", "1/1"),      # 1/3 + 2/3 = 1
            ("5/6-1/6", "2/3"),      # 5/6 - 1/6 = 4/6 = 2/3
        ]
        
        for expr, expected in test_cases:
            with self.subTest(expression=expr):
                result = self.solution.fractionAddition(expr)
                assert result == expected

    def test_sign_preservation(self):
        """Test that signs are correctly preserved."""
        test_cases = [
            ("-1/2+1/4", "-1/4"),    # Negative result
            ("-1/4+1/2", "1/4"),     # Positive result
            ("-1/2-1/4", "-3/4"),    # Double negative
        ]
        
        for expr, expected in test_cases:
            with self.subTest(expression=expr):
                result = self.solution.fractionAddition(expr)
                assert result == expected

    def test_boundary_conditions(self):
        """Test boundary conditions."""
        # Test minimal expressions
        assert self.solution.fractionAddition("0/1") == "0/1"
        assert self.solution.fractionAddition("1/1") == "1/1"
        assert self.solution.fractionAddition("-1/1") == "-1/1"

    def test_complex_denominators(self):
        """Test with various complex denominators."""
        expression = "1/7+1/11+1/13"
        result = self.solution.fractionAddition(expression)
        
        # Should handle prime denominators correctly
        assert isinstance(result, str)
        assert "/" in result
        
        # Result should be in lowest terms
        parts = result.split("/")
        from math import gcd
        assert gcd(int(parts[0].lstrip("-")), int(parts[1])) == 1


if __name__ == "__main__":
    unittest.main()
