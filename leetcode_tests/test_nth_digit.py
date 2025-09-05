"""
Test cases for LeetCode 400: Nth Digit
"""

import pytest

from leetcode.nth_digit import Solution


class TestNthDigit:
    """Test class for Nth Digit problem."""

    def setup_method(self):
        """Set up test fixtures before each test method."""
        self.solution = Solution()

    def build_sequence(self, length: int) -> str:
        """
        Helper function to build the actual sequence for verification.
        
        Args:
            length: Number of digits to generate
            
        Returns:
            String representation of the sequence
        """
        sequence = ""
        num = 1
        while len(sequence) < length:
            sequence += str(num)
            num += 1
        return sequence

    @pytest.mark.parametrize(
        "n,expected",
        [
            # Basic test cases from examples
            (3, 3),     # Sequence: 123456... -> 3rd digit is 3
            (11, 0),    # Sequence: 123456789101112... -> 11th digit is 0 (from 10)
            (15, 2),    # Sequence: 123456789101112... -> 15th digit is 2 (from 12)
            
            # Edge cases
            (1, 1),     # First digit
            (9, 9),     # Last single digit
            (10, 1),    # First digit of first two-digit number (10)
            
            # Boundary cases between digit groups
            (189, 9),   # Last digit of 2-digit numbers (99)
            (190, 1),   # First digit of 3-digit numbers (100)
            
            # Larger numbers
            (1000, 3),  # Test with larger input
            (2889, 9),  # Last digit of 3-digit numbers (999)
            (2890, 1),  # First digit of 4-digit numbers (1000)
        ]
    )
    def test_nth_digit(self, n, expected):
        """Test findNthDigit with various inputs."""
        assert self.solution.findNthDigit(n) == expected

    def test_small_sequence_verification(self):
        """Verify correctness against manually built sequence for small inputs."""
        # Build sequence: "123456789101112131415161718192021222324252627282930..."
        sequence = self.build_sequence(100)
        
        for i in range(1, min(51, len(sequence) + 1)):
            expected = int(sequence[i - 1])  # Convert to 1-indexed
            result = self.solution.findNthDigit(i)
            assert result == expected, f"Position {i}: expected {expected}, got {result}"

    def test_single_digit_numbers(self):
        """Test positions within single digit numbers (1-9)."""
        # Positions 1-9 should return digits 1-9
        for i in range(1, 10):
            assert self.solution.findNthDigit(i) == i

    def test_two_digit_number_boundaries(self):
        """Test boundaries around two-digit numbers."""
        # Position 10 should be '1' from "10"
        assert self.solution.findNthDigit(10) == 1
        
        # Position 11 should be '0' from "10"
        assert self.solution.findNthDigit(11) == 0
        
        # Position 12 should be '1' from "11"
        assert self.solution.findNthDigit(12) == 1
        
        # Position 13 should be '1' from "11"
        assert self.solution.findNthDigit(13) == 1

    def test_three_digit_number_boundaries(self):
        """Test boundaries around three-digit numbers."""
        # Last two-digit number is 99 at positions 188-189
        # First three-digit number is 100 at positions 190-192
        
        # Position 189 should be '9' from "99"
        assert self.solution.findNthDigit(189) == 9
        
        # Position 190 should be '1' from "100"
        assert self.solution.findNthDigit(190) == 1
        
        # Position 191 should be '0' from "100"
        assert self.solution.findNthDigit(191) == 0
        
        # Position 192 should be '0' from "100"
        assert self.solution.findNthDigit(192) == 0

    def test_digit_group_calculations(self):
        """Test that digit group calculations are correct."""
        # Single digits: 1-9 (9 numbers × 1 digit = 9 total digits)
        # Two digits: 10-99 (90 numbers × 2 digits = 180 total digits)
        # Three digits: 100-999 (900 numbers × 3 digits = 2700 total digits)
        
        # After single digits (position 9), next should start two-digit numbers
        assert self.solution.findNthDigit(10) == 1  # "10" first digit
        
        # After single + two digits (position 9 + 180 = 189), next should start three-digit
        assert self.solution.findNthDigit(190) == 1  # "100" first digit

    def test_large_numbers(self):
        """Test with larger numbers to ensure algorithm efficiency."""
        # These should complete quickly without building the entire sequence
        test_cases = [
            (1000, 3),
            (10000, 7),
            (100000, 2),
        ]
        
        for n, expected in test_cases:
            result = self.solution.findNthDigit(n)
            assert result == expected

    def test_manual_verification_examples(self):
        """Manually verify specific examples step by step."""
        # For n = 11:
        # Sequence: 1 2 3 4 5 6 7 8 9 1 0 1 1 1 2 1 3 ...
        # Positions: 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17
        # The 11th digit is 0 (from number 10)
        assert self.solution.findNthDigit(11) == 0
        
        # For n = 15:
        # The 15th digit is 2 (from number 12)
        assert self.solution.findNthDigit(15) == 2

    def test_algorithm_correctness_verification(self):
        """Verify algorithm correctness with known patterns."""
        # Test the pattern: positions in two-digit numbers
        # Two-digit numbers start at position 10
        # Number 10: positions 10-11 (digits 1, 0)
        # Number 11: positions 12-13 (digits 1, 1)
        # Number 12: positions 14-15 (digits 1, 2)
        
        two_digit_tests = [
            (10, 1), (11, 0),  # Number 10
            (12, 1), (13, 1),  # Number 11
            (14, 1), (15, 2),  # Number 12
            (16, 1), (17, 3),  # Number 13
        ]
        
        for pos, expected in two_digit_tests:
            result = self.solution.findNthDigit(pos)
            assert result == expected, f"Position {pos}: expected {expected}, got {result}"

    def test_performance_large_input(self):
        """Test that the algorithm handles large inputs efficiently."""
        import time
        
        # Should handle large inputs without timeout
        large_inputs = [1000000, 2147483647]  # Including max int value
        
        for n in large_inputs:
            start_time = time.time()
            result = self.solution.findNthDigit(n)
            end_time = time.time()
            
            # Should complete quickly (less than 1 second)
            assert end_time - start_time < 1.0
            assert isinstance(result, int)
            assert 0 <= result <= 9

    def test_return_type(self):
        """Test that return type is correct integer."""
        result = self.solution.findNthDigit(100)
        assert isinstance(result, int)
        assert 0 <= result <= 9
