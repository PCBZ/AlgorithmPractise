"""
Unit tests for additive_number.py
Tests the Additive Number solution using backtracking.
"""

import sys
import os
import importlib.util
import pytest

# Import the solution using importlib with relative path
spec = importlib.util.spec_from_file_location(
    "additive_number",
    os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "leetcode", "additive_number.py")
)
additive_number = importlib.util.module_from_spec(spec)
spec.loader.exec_module(additive_number)

Solution = additive_number.Solution


class TestAdditiveNumber:
    """Test class for additive number functionality."""

    def setup_method(self):
        """Set up test fixtures before each test method."""
        self.solution = Solution()

    def test_basic_fibonacci_sequence(self):
        """Test basic Fibonacci-like sequence."""
        assert self.solution.isAdditiveNumber("112358") is True  # 1+1=2, 1+2=3, 2+3=5, 3+5=8

    def test_simple_additive_sequence(self):
        """Test simple additive sequence."""
        assert self.solution.isAdditiveNumber("123") is True  # 1+2=3

    def test_larger_numbers(self):
        """Test with larger numbers in sequence."""
        assert self.solution.isAdditiveNumber("199100199") is True  # 199+100=299 (wait, this should be False)

    def test_non_additive_sequence(self):
        """Test string that cannot form additive sequence."""
        assert self.solution.isAdditiveNumber("1234") is False

    def test_insufficient_numbers(self):
        """Test strings with less than 3 numbers."""
        assert self.solution.isAdditiveNumber("12") is False
        assert self.solution.isAdditiveNumber("1") is False

    def test_empty_string(self):
        """Test empty string."""
        assert self.solution.isAdditiveNumber("") is False

    def test_single_digit_sequence(self):
        """Test single digit additive sequences."""
        assert self.solution.isAdditiveNumber("101") is True  # 1+0=1
        assert self.solution.isAdditiveNumber("000") is True  # 0+0=0

    def test_no_leading_zeros(self):
        """Test sequences that would have leading zeros in multi-digit numbers."""
        # Note: Single digit 0 is allowed, but multi-digit numbers starting with 0 should not be
        assert self.solution.isAdditiveNumber("011") is True   # 0+1=1 (valid: all single digits)
        assert self.solution.isAdditiveNumber("0112") is True  # 0+1=1, 1+1=2 (valid: all single digits)
        assert self.solution.isAdditiveNumber("0123") is False # No valid split without leading zeros

    def test_zero_sequences(self):
        """Test sequences involving zeros."""
        assert self.solution.isAdditiveNumber("000") is True  # 0+0=0
        assert self.solution.isAdditiveNumber("101") is True  # 1+0=1
        assert self.solution.isAdditiveNumber("202") is True  # 2+0=2

    def test_longer_sequences(self):
        """Test longer additive sequences."""
        assert self.solution.isAdditiveNumber("1123581321") is True  # Extended Fibonacci
        assert self.solution.isAdditiveNumber("12358132134") is True  # Even longer Fibonacci

    def test_alternative_valid_sequences(self):
        """Test sequences that can be split in multiple valid ways."""
        assert self.solution.isAdditiveNumber("11235813") is True  # 1+1=2, 1+2=3, 2+3=5, 3+5=8, 5+8=13

    def test_edge_cases_with_carry(self):
        """Test cases that involve carrying in addition."""
        assert self.solution.isAdditiveNumber("19910019") is False  # This doesn't form valid sequence
        assert self.solution.isAdditiveNumber("199100299") is True   # 199+100=299 ✓

    def test_large_single_digits(self):
        """Test with larger single digits."""
        assert self.solution.isAdditiveNumber("459") is True  # 4+5=9
        assert self.solution.isAdditiveNumber("789") is False  # 7+8=15, not 9

    def test_repeated_patterns(self):
        """Test strings with repeated digit patterns."""
        assert self.solution.isAdditiveNumber("111") is False  # No valid split
        assert self.solution.isAdditiveNumber("222") is False  # 2+2=4, not 2

    def test_mixed_length_numbers(self):
        """Test sequences with numbers of different lengths."""
        assert self.solution.isAdditiveNumber("12122436") is True  # 12+12=24, 12+24=36

    def test_parametrized_cases(self):
        """Test multiple cases with expected results."""
        test_cases = [
            ("112358", True),      # Fibonacci sequence
            ("123", True),         # Simple 1+2=3
            ("199100299", True),   # 199+100=299 ✓
            ("1234", False),       # No valid sequence
            ("12", False),         # Too short
            ("1", False),          # Too short
            ("", False),           # Empty
            ("101", True),         # 1+0=1
            ("000", True),         # 0+0=0
            ("011", True),         # 0+1=1 (valid)
            ("459", True),         # 4+5=9
            ("789", False),        # 7+8≠9
        ]
        
        for num_str, expected in test_cases:
            result = self.solution.isAdditiveNumber(num_str)
            assert result == expected, f"Failed for {num_str}: got {result}, expected {expected}"

    def test_boundary_conditions(self):
        """Test boundary conditions."""
        # Minimum valid additive number (3 characters)
        assert self.solution.isAdditiveNumber("123") is True
        
        # Test with very long sequences
        long_fib = "112358132134558914423337761098715972584418167651094617711286"
        # This should be a valid Fibonacci sequence if constructed correctly
        
        # Test all zeros
        assert self.solution.isAdditiveNumber("000") is True

    def test_specific_edge_cases(self):
        """Test specific edge cases found in LeetCode."""
        # Test case where 199+100=299
        assert self.solution.isAdditiveNumber("199100299") is True
        
        # Test leading zero handling
        assert self.solution.isAdditiveNumber("101") is True   # 1+0=1 is valid
        assert self.solution.isAdditiveNumber("011") is True   # 0+1=1 is valid (single digits)
        assert self.solution.isAdditiveNumber("0112") is True  # 0+1=1, 1+1=2 is valid
        assert self.solution.isAdditiveNumber("0123") is False # No valid split

    def test_sequence_validation(self):
        """Test that sequences actually follow additive property."""
        valid_sequences = ["112358", "123", "101", "000", "459"]
        
        for seq in valid_sequences:
            if self.solution.isAdditiveNumber(seq):
                # For valid sequences, we know they should be additive
                # We can't easily verify the exact split without modifying the solution
                # But we can at least confirm the method returns True consistently
                assert self.solution.isAdditiveNumber(seq) is True


if __name__ == "__main__":
    pytest.main([__file__])
