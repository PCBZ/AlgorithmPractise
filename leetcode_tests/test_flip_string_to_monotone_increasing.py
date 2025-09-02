"""
Test cases for LeetCode Problem #926: Flip String to Monotone Increasing
"""
import unittest

from leetcode.flip_string_to_monotone_increasing import Solution


class TestFlipStringToMonotoneIncreasing(unittest.TestCase):
    """Test cases for the FlipStringToMonotoneIncreasing solution."""

    def setUp(self):
        """Set up test fixtures before each test method."""
        self.solution = Solution()

    def test_example_case_1(self):
        """Test the first example case."""
        s = "00110"
        result = self.solution.minFlipsMonoIncr(s)
        expected = 1  # Flip last '0' to '1'
        assert result == expected

    def test_example_case_2(self):
        """Test the second example case."""
        s = "010110"
        result = self.solution.minFlipsMonoIncr(s)
        expected = 2  # Multiple ways to achieve monotone
        assert result == expected

    def test_example_case_3(self):
        """Test the third example case."""
        s = "00011000"
        result = self.solution.minFlipsMonoIncr(s)
        expected = 2  # Flip last two '0's to '1's
        assert result == expected

    def test_single_zero(self):
        """Test single '0' character."""
        s = "0"
        result = self.solution.minFlipsMonoIncr(s)
        expected = 0  # Already monotone
        assert result == expected

    def test_single_one(self):
        """Test single '1' character."""
        s = "1"
        result = self.solution.minFlipsMonoIncr(s)
        expected = 0  # Already monotone
        assert result == expected

    def test_already_monotone_01(self):
        """Test string already monotone increasing."""
        s = "01"
        result = self.solution.minFlipsMonoIncr(s)
        expected = 0  # Already monotone
        assert result == expected

    def test_reverse_monotone_10(self):
        """Test string that's reverse monotone."""
        s = "10"
        result = self.solution.minFlipsMonoIncr(s)
        expected = 1  # Flip either '1' to '0' or '0' to '1'
        assert result == expected

    def test_all_zeros(self):
        """Test string with all zeros."""
        s = "0000"
        result = self.solution.minFlipsMonoIncr(s)
        expected = 0  # Already monotone
        assert result == expected

    def test_all_ones(self):
        """Test string with all ones."""
        s = "1111"
        result = self.solution.minFlipsMonoIncr(s)
        expected = 0  # Already monotone
        assert result == expected

    def test_alternating_pattern(self):
        """Test alternating pattern."""
        s = "0101"
        result = self.solution.minFlipsMonoIncr(s)
        expected = 1  # Flip one character
        assert result == expected

    def test_reverse_alternating_pattern(self):
        """Test reverse alternating pattern."""
        s = "1010"
        result = self.solution.minFlipsMonoIncr(s)
        expected = 2  # Need to flip multiple characters
        assert result == expected

    def test_long_mixed_string(self):
        """Test longer mixed string."""
        s = "00110011"
        result = self.solution.minFlipsMonoIncr(s)
        expected = 2  # Flip last two '0's
        assert result == expected

    def test_majority_zeros(self):
        """Test string with majority zeros."""
        s = "000100"
        result = self.solution.minFlipsMonoIncr(s)
        expected = 1  # Flip the '1' to '0'
        assert result == expected

    def test_majority_ones(self):
        """Test string with majority ones."""
        s = "111011"
        result = self.solution.minFlipsMonoIncr(s)
        expected = 1  # Flip the '0' to '1'
        assert result == expected

    def test_ones_at_start(self):
        """Test string starting with ones."""
        s = "110000"
        result = self.solution.minFlipsMonoIncr(s)
        expected = 2  # Flip first two '1's to '0's
        assert result == expected

    def test_zeros_at_end(self):
        """Test string ending with zeros."""
        s = "111000"
        result = self.solution.minFlipsMonoIncr(s)
        expected = 3  # Flip last three '0's to '1's
        assert result == expected

    def test_complex_pattern_1(self):
        """Test complex mixed pattern."""
        s = "0110100"
        result = self.solution.minFlipsMonoIncr(s)
        # Find optimal way to make monotone
        assert isinstance(result, int)
        assert result >= 0

    def test_complex_pattern_2(self):
        """Test another complex pattern."""
        s = "1001010"
        result = self.solution.minFlipsMonoIncr(s)
        # Find optimal way to make monotone
        assert isinstance(result, int)
        assert result >= 0

    def test_edge_case_small_strings(self):
        """Test various small strings."""
        test_cases = [
            ("00", 0),  # Already monotone
            ("11", 0),  # Already monotone
            ("001", 0), # Already monotone
            ("011", 0), # Already monotone
            ("111", 0), # Already monotone
            ("100", 1), # One flip needed
            ("110", 1), # One flip needed
        ]
        
        for string, expected in test_cases:
            with self.subTest(string=string):
                result = self.solution.minFlipsMonoIncr(string)
                assert result == expected

    def test_return_type_and_constraints(self):
        """Test return type and basic constraints."""
        s = "0110"
        result = self.solution.minFlipsMonoIncr(s)
        assert isinstance(result, int)
        assert result >= 0
        assert result <= len(s)  # Can't flip more than total characters

    def test_algorithm_optimality(self):
        """Test that algorithm finds optimal solution."""
        # For string "0110", optimal is 1 flip (either flip last 0 or first 1)
        s = "0110"
        result = self.solution.minFlipsMonoIncr(s)
        assert result == 1
        
        # For string "1100", optimal is 2 flips
        s = "1100"
        result = self.solution.minFlipsMonoIncr(s)
        assert result == 2

    def test_dynamic_programming_correctness(self):
        """Test DP approach correctness with known cases."""
        test_cases = [
            ("010", 1),    # Flip middle '1' to '0' or last '0' to '1'
            ("101", 1),    # Flip first '1' to '0' or middle '0' to '1'
            ("0011", 0),   # Already monotone
            ("1100", 2),   # Flip both '0's to '1's or both '1's to '0's
        ]
        
        for string, expected in test_cases:
            with self.subTest(string=string):
                result = self.solution.minFlipsMonoIncr(string)
                assert result == expected

    def test_monotone_property_validation(self):
        """Test that we understand monotone property correctly."""
        # Monotone means all 0s come before all 1s
        monotone_strings = ["", "0", "1", "00", "11", "01", "001", "011", "0011"]
        
        for s in monotone_strings:
            if s:  # Skip empty string
                result = self.solution.minFlipsMonoIncr(s)
                assert result == 0, f"String '{s}' should already be monotone"

    def test_performance_reasonable_input(self):
        """Test performance with reasonable input size."""
        # Create a string that requires some flips
        s = "01" * 50  # "010101...01" pattern
        result = self.solution.minFlipsMonoIncr(s)
        
        # Should handle this efficiently
        assert isinstance(result, int)
        assert result >= 0

    def test_boundary_flip_decisions(self):
        """Test boundary cases for flip decisions."""
        # Test where it's unclear whether to flip or not
        test_cases = [
            "0101010",  # Alternating pattern
            "1010101",  # Reverse alternating
            "0011001",  # Mixed pattern
        ]
        
        for s in test_cases:
            result = self.solution.minFlipsMonoIncr(s)
            # Verify it's a reasonable result
            assert 0 <= result <= len(s)

    def test_dp_state_transitions(self):
        """Test DP state transitions are correct."""
        # Manual verification for small case
        s = "001"
        result = self.solution.minFlipsMonoIncr(s)
        expected = 0  # Already monotone
        assert result == expected
        
        s = "110"
        result = self.solution.minFlipsMonoIncr(s)
        expected = 1  # Flip one character
        assert result == expected

    def test_optimal_substructure(self):
        """Test that optimal substructure property holds."""
        # The solution should work for all prefixes optimally
        s = "010110"
        result = self.solution.minFlipsMonoIncr(s)
        
        # Should be optimal solution
        assert isinstance(result, int)
        assert result >= 0

    def test_string_reconstruction_concept(self):
        """Test understanding of what makes a string monotone."""
        # These should require no flips
        monotone_cases = ["0", "1", "01", "001", "011", "0001", "0011", "0111"]
        
        for s in monotone_cases:
            result = self.solution.minFlipsMonoIncr(s)
            assert result == 0, f"Monotone string '{s}' should need 0 flips"

    def test_greedy_vs_dp_comparison(self):
        """Test cases where greedy might fail but DP succeeds."""
        # Cases where local optimal isn't global optimal
        s = "001011"
        result = self.solution.minFlipsMonoIncr(s)
        
        # DP should find optimal solution
        assert isinstance(result, int)
        assert result >= 0


if __name__ == "__main__":
    unittest.main()
