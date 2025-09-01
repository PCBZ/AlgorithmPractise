"""
Comprehensive test suite for LeetCode Problem #424: Longest Repeating Character Replacement.
Tests the sliding window solution for finding longest substring with at most k replacements.
"""

import pytest
import sys
import os
import importlib.util

# Add the parent directory to the path to allow imports
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

try:
    from leetcode.longest_repeating_character_replacement_01 import Solution
except ImportError:
    # Fallback for environments where package import fails
    module_path = os.path.join(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
        "leetcode",
        "longest_repeating_character_replacement.py"
    )
    spec = importlib.util.spec_from_file_location("longest_repeating_character_replacement", module_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    Solution = module.Solution


class TestLongestRepeatingCharacterReplacement:
    """Test cases for longest repeating character replacement."""

    def setup_method(self):
        """Set up test fixtures before each test method."""
        self.solution = Solution()

    def test_basic_example_1(self):
        """Test basic example from problem description."""
        result = self.solution.character_replacement("ABAB", 2)
        assert result == 4  # Replace both A's or both B's

    def test_basic_example_2(self):
        """Test basic example with different pattern."""
        result = self.solution.character_replacement("AABABBA", 1)
        assert result == 4  # "AABA" or "ABBB"

    def test_all_same_characters(self):
        """Test string with all same characters."""
        result = self.solution.character_replacement("AAAA", 2)
        assert result == 4

    def test_empty_string(self):
        """Test empty string."""
        result = self.solution.character_replacement("", 1)
        assert result == 0

    def test_single_character(self):
        """Test single character string."""
        result = self.solution.character_replacement("A", 1)
        assert result == 1

    def test_two_characters_no_replacement(self):
        """Test two different characters with no replacements allowed."""
        result = self.solution.character_replacement("AB", 0)
        assert result == 1

    def test_two_characters_one_replacement(self):
        """Test two different characters with one replacement."""
        result = self.solution.character_replacement("AB", 1)
        assert result == 2

    def test_alternating_pattern(self):
        """Test alternating pattern."""
        result = self.solution.character_replacement("ABAB", 1)
        assert result == 3  # "AAB" or "ABB"

    def test_no_replacements_needed(self):
        """Test when no replacements are needed."""
        result = self.solution.character_replacement("AAAA", 0)
        assert result == 4

    def test_k_equals_string_length(self):
        """Test when k equals string length."""
        result = self.solution.character_replacement("ABCD", 4)
        assert result == 4  # Can replace all to same character

    def test_k_greater_than_needed(self):
        """Test when k is greater than needed."""
        result = self.solution.character_replacement("AABA", 10)
        assert result == 4  # Only need 1 replacement

    def test_complex_pattern_1(self):
        """Test complex pattern case 1."""
        result = self.solution.character_replacement("AAABABB", 1)
        assert result == 5  # "AAABA"

    def test_complex_pattern_2(self):
        """Test complex pattern case 2."""
        result = self.solution.character_replacement("XYYX", 2)
        assert result == 4  # Can replace all

    def test_longer_string(self):
        """Test longer string with optimal sliding window."""
        result = self.solution.character_replacement("ABCABC", 2)
        assert result == 4  # "AAAA" by replacing B,C in "ABCA"

    def test_three_different_characters(self):
        """Test string with three different characters."""
        result = self.solution.character_replacement("ABCABC", 1)
        assert result == 2  # Can get "AA" or "BB" or "CC" with 1 replacement

    def test_edge_case_k_zero(self):
        """Test edge case where k is zero."""
        result = self.solution.character_replacement("ABCDEF", 0)
        assert result == 1  # Can only take one character

    def test_repeated_segments(self):
        """Test string with repeated segments."""
        result = self.solution.character_replacement("AABBAA", 2)
        assert result == 6  # Entire string by replacing 2 B's

    def test_get_replacement_details_basic(self):
        """Test getting detailed replacement information."""
        result = self.solution.get_replacement_details("ABAB", 2)
        assert result["length"] == 4
        assert result["start"] == 0
        assert result["end"] == 4
        assert result["most_frequent"] in ["A", "B"]

    def test_get_replacement_details_empty(self):
        """Test getting details for empty string."""
        result = self.solution.get_replacement_details("", 1)
        assert result == {"length": 0, "start": 0, "end": 0, "most_frequent": ""}

    def test_get_replacement_details_single(self):
        """Test getting details for single character."""
        result = self.solution.get_replacement_details("A", 1)
        assert result["length"] == 1
        assert result["start"] == 0
        assert result["end"] == 1
        assert result["most_frequent"] == "A"

    def test_sliding_window_efficiency(self):
        """Test sliding window maintains efficiency."""
        # Long string that tests window sliding
        long_string = "A" * 100 + "B" * 100 + "A" * 100
        result = self.solution.character_replacement(long_string, 50)
        assert result == 150  # Optimal window: 100 As + 50 Bs replaced = 150

    def test_algorithm_correctness_properties(self):
        """Test fundamental properties of the algorithm."""
        test_cases = [
            ("A", 0, 1),
            ("AA", 0, 2), 
            ("AB", 1, 2),
            ("ABC", 2, 3),
            ("ABAB", 1, 3),
            ("AAAA", 0, 4)
        ]
        
        for s, k, expected in test_cases:
            result = self.solution.character_replacement(s, k)
            assert result == expected, f"Failed for s='{s}', k={k}: got {result}, expected {expected}"

    def test_boundary_conditions(self):
        """Test boundary conditions."""
        # Minimum cases
        assert self.solution.character_replacement("", 0) == 0
        assert self.solution.character_replacement("A", 0) == 1
        
        # Maximum k value
        assert self.solution.character_replacement("ABCD", 100) == 4

    def test_character_frequency_tracking(self):
        """Test that character frequencies are tracked correctly."""
        # Test case where frequency tracking is critical
        result = self.solution.character_replacement("AABACADA", 2)
        assert result >= 5  # Should find optimal substring

    def test_window_shrinking_logic(self):
        """Test window shrinking logic."""
        # Pattern that requires careful window management
        result = self.solution.character_replacement("ABCABC", 1)
        assert result == 2

    def test_multiple_optimal_solutions(self):
        """Test cases with multiple optimal solutions."""
        # Both methods should return consistent length
        test_str = "ABAB"
        k = 1
        length = self.solution.character_replacement(test_str, k)
        details = self.solution.get_replacement_details(test_str, k)
        assert details["length"] == length

    def test_all_different_characters(self):
        """Test string where all characters are different."""
        result = self.solution.character_replacement("ABCDE", 2)
        assert result == 3  # Can make 3 characters same with 2 replacements

    def test_large_k_value(self):
        """Test with very large k value."""
        result = self.solution.character_replacement("ABCDEFGH", 1000)
        assert result == 8  # Entire string length

    def test_return_type_validation(self):
        """Test that return type is correct integer."""
        result = self.solution.character_replacement("ABC", 1)
        assert isinstance(result, int)
        assert result >= 0

    def test_input_preservation(self):
        """Test that input string is not modified."""
        original = "ABAB"
        test_str = original
        self.solution.character_replacement(test_str, 1)
        assert test_str == original

    def test_both_methods_consistency(self):
        """Test that both methods return consistent results."""
        test_cases = [
            ("", 0),
            ("A", 1),
            ("AB", 1),
            ("ABAB", 2),
            ("AAABABB", 1),
            ("XYYX", 2)
        ]
        
        for test_str, k in test_cases:
            length = self.solution.character_replacement(test_str, k)
            details = self.solution.get_replacement_details(test_str, k)
            assert details["length"] == length

    def test_performance_larger_strings(self):
        """Test performance with larger strings."""
        # Create a pattern that tests sliding window efficiency
        large_str = ("AB" * 500) + ("A" * 100)
        result = self.solution.character_replacement(large_str, 50)
        assert result > 0  # Should complete efficiently

    def test_optimal_window_identification(self):
        """Test that optimal window is correctly identified."""
        result = self.solution.character_replacement("ABACADAEAF", 2)
        assert result >= 4  # Should find good substring

    def test_edge_case_single_replacement(self):
        """Test edge case with single replacement."""
        result = self.solution.character_replacement("ABCABC", 1)
        assert result == 2

    def test_substring_validation(self):
        """Test that identified substrings are valid."""
        test_str = "AABACADA"
        k = 2
        details = self.solution.get_replacement_details(test_str, k)
        
        # Extract the identified substring
        substring = test_str[details["start"]:details["end"]]
        assert len(substring) == details["length"]

    def test_special_patterns(self):
        """Test special patterns that might cause edge cases."""
        # Pattern with single character dominating
        assert self.solution.character_replacement("AAABBBCCC", 3) == 6
        
        # Pattern with even distribution
        assert self.solution.character_replacement("ABCABC", 2) == 4

    def test_maximum_character_frequency(self):
        """Test scenarios with maximum character frequency tracking."""
        # Test that max frequency is tracked correctly during window sliding
        result = self.solution.character_replacement("ABBBACCCAAA", 2)
        assert result >= 5

    def test_window_expansion_and_contraction(self):
        """Test window expansion and contraction logic."""
        # Pattern that requires both expansion and contraction
        result = self.solution.character_replacement("AABABACABAA", 3)
        assert result >= 7

    def test_replacement_strategy_validation(self):
        """Test that replacement strategy is optimal."""
        # For each test case, verify the result makes sense
        test_cases = [
            ("ABAB", 0, 1),  # No replacements -> max single character run
            ("ABAB", 1, 3),  # One replacement -> 3 characters
            ("ABAB", 2, 4),  # Two replacements -> entire string
        ]
        
        for s, k, expected in test_cases:
            result = self.solution.character_replacement(s, k)
            assert result == expected

    def test_complex_sliding_scenarios(self):
        """Test complex sliding window scenarios."""
        # Multiple potential optimal windows
        result = self.solution.character_replacement("ABCABCABC", 2)
        assert result >= 4

    def test_frequency_map_accuracy(self):
        """Test that frequency maps are accurate."""
        # Use the details method to verify frequency tracking
        details = self.solution.get_replacement_details("AAABBB", 1)
        assert details["length"] == 4  # AAAB or ABBB


if __name__ == "__main__":
    pytest.main([__file__])
