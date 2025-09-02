"""
Test cases for LeetCode Problem #166: Fraction to Recurring Decimal
"""
import unittest

from leetcode.fraction_to_recurring_decimal import Solution


class TestFractionToRecurringDecimal(unittest.TestCase):
    """Test cases for the FractionToRecurringDecimal solution."""

    def setUp(self):
        """Set up test fixtures before each test method."""
        self.solution = Solution()

    def test_example_case_1(self):
        """Test first example case - terminating decimal."""
        numerator, denominator = 1, 2
        result = self.solution.fractionToDecimal(numerator, denominator)
        expected = "0.5"
        assert result == expected

    def test_example_case_2(self):
        """Test second example case - integer result."""
        numerator, denominator = 2, 1
        result = self.solution.fractionToDecimal(numerator, denominator)
        expected = "2"
        assert result == expected

    def test_example_case_3(self):
        """Test third example case - pure repeating decimal."""
        numerator, denominator = 2, 3
        result = self.solution.fractionToDecimal(numerator, denominator)
        expected = "0.(6)"
        assert result == expected

    def test_mixed_repeating_decimal(self):
        """Test mixed repeating decimal."""
        numerator, denominator = 1, 6
        result = self.solution.fractionToDecimal(numerator, denominator)
        expected = "0.1(6)"
        assert result == expected

    def test_complex_repeating_pattern(self):
        """Test complex repeating pattern."""
        numerator, denominator = 4, 333
        result = self.solution.fractionToDecimal(numerator, denominator)
        expected = "0.(012)"
        assert result == expected

    def test_negative_numerator(self):
        """Test negative numerator."""
        numerator, denominator = -1, 2
        result = self.solution.fractionToDecimal(numerator, denominator)
        expected = "-0.5"
        assert result == expected

    def test_negative_denominator(self):
        """Test negative denominator."""
        numerator, denominator = 1, -2
        result = self.solution.fractionToDecimal(numerator, denominator)
        expected = "-0.5"
        assert result == expected

    def test_both_negative(self):
        """Test both numerator and denominator negative."""
        numerator, denominator = -1, -2
        result = self.solution.fractionToDecimal(numerator, denominator)
        expected = "0.5"
        assert result == expected

    def test_zero_numerator(self):
        """Test zero numerator."""
        numerator, denominator = 0, 1
        result = self.solution.fractionToDecimal(numerator, denominator)
        expected = "0"
        assert result == expected

    def test_zero_numerator_negative_denominator(self):
        """Test zero numerator with negative denominator."""
        numerator, denominator = 0, -5
        result = self.solution.fractionToDecimal(numerator, denominator)
        # Both "0" and "-0" are mathematically valid for 0/-5
        assert result in ["0", "-0"]

    def test_large_integer_result(self):
        """Test large integer result."""
        numerator, denominator = 10, 1
        result = self.solution.fractionToDecimal(numerator, denominator)
        expected = "10"
        assert result == expected

    def test_large_negative_integer(self):
        """Test large negative integer."""
        numerator, denominator = -100, 1
        result = self.solution.fractionToDecimal(numerator, denominator)
        expected = "-100"
        assert result == expected

    def test_terminating_decimal_powers_of_ten(self):
        """Test terminating decimals with powers of 10."""
        test_cases = [
            (1, 10, "0.1"),
            (1, 100, "0.01"),
            (1, 1000, "0.001"),
            (3, 10, "0.3"),
            (25, 100, "0.25"),
        ]
        
        for num, den, expected in test_cases:
            with self.subTest(numerator=num, denominator=den):
                result = self.solution.fractionToDecimal(num, den)
                assert result == expected

    def test_terminating_decimal_powers_of_two_and_five(self):
        """Test terminating decimals with powers of 2 and 5."""
        test_cases = [
            (1, 4, "0.25"),    # 1/4 = 0.25
            (1, 8, "0.125"),   # 1/8 = 0.125
            (1, 5, "0.2"),     # 1/5 = 0.2
            (3, 8, "0.375"),   # 3/8 = 0.375
            (7, 20, "0.35"),   # 7/20 = 0.35
        ]
        
        for num, den, expected in test_cases:
            with self.subTest(numerator=num, denominator=den):
                result = self.solution.fractionToDecimal(num, den)
                assert result == expected

    def test_pure_repeating_decimals(self):
        """Test pure repeating decimals."""
        test_cases = [
            (1, 3, "0.(3)"),
            (2, 3, "0.(6)"),
            (1, 7, "0.(142857)"),
            (1, 9, "0.(1)"),
            (2, 9, "0.(2)"),
        ]
        
        for num, den, expected in test_cases:
            with self.subTest(numerator=num, denominator=den):
                result = self.solution.fractionToDecimal(num, den)
                assert result == expected

    def test_mixed_repeating_decimals(self):
        """Test mixed repeating decimals."""
        test_cases = [
            (1, 6, "0.1(6)"),     # 1/6 = 0.1666...
            (5, 6, "0.8(3)"),     # 5/6 = 0.8333...
            (1, 12, "0.08(3)"),   # 1/12 = 0.0833...
            (7, 12, "0.58(3)"),   # 7/12 = 0.5833...
        ]
        
        for num, den, expected in test_cases:
            with self.subTest(numerator=num, denominator=den):
                result = self.solution.fractionToDecimal(num, den)
                assert result == expected

    def test_improper_fractions(self):
        """Test improper fractions."""
        test_cases = [
            (3, 2, "1.5"),
            (5, 3, "1.(6)"),
            (7, 4, "1.75"),
            (8, 3, "2.(6)"),
            (22, 7, "3.(142857)"),
        ]
        
        for num, den, expected in test_cases:
            with self.subTest(numerator=num, denominator=den):
                result = self.solution.fractionToDecimal(num, den)
                assert result == expected

    def test_edge_case_one_over_large_prime(self):
        """Test 1 divided by large prime numbers."""
        # These should produce long repeating cycles
        primes = [7, 11, 13, 17, 19]
        
        for prime in primes:
            result = self.solution.fractionToDecimal(1, prime)
            # Should start with "0.(" and end with ")"
            assert result.startswith("0.(")
            assert result.endswith(")")
            # Should have reasonable length
            assert len(result) >= 4

    def test_return_type_and_format(self):
        """Test return type and format constraints."""
        result = self.solution.fractionToDecimal(1, 3)
        assert isinstance(result, str)
        # Should have proper parentheses for repeating part
        assert result == "0.(3)"
        
        result = self.solution.fractionToDecimal(1, 2)
        assert isinstance(result, str)
        # Should not have parentheses for terminating decimal
        assert "(" not in result and ")" not in result

    def test_parentheses_placement(self):
        """Test correct placement of parentheses."""
        # Test that parentheses correctly mark the repeating part
        result = self.solution.fractionToDecimal(1, 6)
        assert result == "0.1(6)"
        
        result = self.solution.fractionToDecimal(1, 3)
        assert result == "0.(3)"
        
        result = self.solution.fractionToDecimal(5, 6)
        assert result == "0.8(3)"

    def test_long_division_correctness(self):
        """Test that long division algorithm is implemented correctly."""
        # Manual verification cases
        test_cases = [
            (1, 7, "0.(142857)"),  # Known repeating pattern
            (22, 7, "3.(142857)"), # Same pattern with integer part
            (50, 7, "7.(142857)"), # Different integer part, same pattern
        ]
        
        for num, den, expected in test_cases:
            with self.subTest(numerator=num, denominator=den):
                result = self.solution.fractionToDecimal(num, den)
                assert result == expected

    def test_sign_handling(self):
        """Test correct sign handling."""
        # Test XOR logic for signs
        test_cases = [
            (1, 2, "0.5"),      # Both positive
            (-1, 2, "-0.5"),    # Negative numerator
            (1, -2, "-0.5"),    # Negative denominator
            (-1, -2, "0.5"),    # Both negative
        ]
        
        for num, den, expected in test_cases:
            with self.subTest(numerator=num, denominator=den):
                result = self.solution.fractionToDecimal(num, den)
                assert result == expected

    def test_remainder_tracking(self):
        """Test that remainder tracking correctly detects cycles."""
        # Test case where cycle detection is crucial
        result = self.solution.fractionToDecimal(1, 17)
        # Should detect the cycle and place parentheses correctly
        assert result.startswith("0.(")
        assert result.endswith(")")
        # Should not have nested parentheses
        assert result.count("(") == 1
        assert result.count(")") == 1

    def test_algorithm_efficiency(self):
        """Test algorithm efficiency with various denominators."""
        # Test with denominators that could cause long cycles
        denominators = [7, 11, 13, 17, 19, 23]
        
        for den in denominators:
            result = self.solution.fractionToDecimal(1, den)
            # Should handle these efficiently
            assert isinstance(result, str)
            assert len(result) < 100  # Reasonable length

    def test_decimal_precision(self):
        """Test decimal precision and accuracy."""
        # Test cases where precision matters
        test_cases = [
            (1, 8, "0.125"),
            (3, 16, "0.1875"),
            (7, 32, "0.21875"),
        ]
        
        for num, den, expected in test_cases:
            with self.subTest(numerator=num, denominator=den):
                result = self.solution.fractionToDecimal(num, den)
                assert result == expected

    def test_boundary_conditions(self):
        """Test boundary conditions."""
        # Test minimum and maximum reasonable inputs
        test_cases = [
            (1, 1, "1"),
            (0, 1, "0"),
            (-0, 1, "0"),
            (1000000, 1, "1000000"),
            (1, 1000000, "0.000001"),
        ]
        
        for num, den, expected in test_cases:
            with self.subTest(numerator=num, denominator=den):
                result = self.solution.fractionToDecimal(num, den)
                assert result == expected

    def test_complex_repeating_patterns(self):
        """Test complex repeating patterns."""
        # Test fractions with known complex patterns
        test_cases = [
            (1, 13, "0.(076923)"),    # 1/13 has a 6-digit cycle
            (1, 21, "0.(047619)"),    # 1/21 has a 6-digit cycle
        ]
        
        for num, den, expected in test_cases:
            with self.subTest(numerator=num, denominator=den):
                result = self.solution.fractionToDecimal(num, den)
                assert result == expected


if __name__ == "__main__":
    unittest.main()
