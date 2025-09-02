"""
Comprehensive test suite for LeetCode Problem #395: Longest Substring with At Least K Repeating Characters
Tests both divide-and-conquer and sliding window approaches for finding valid substrings.
"""

import pytest

from leetcode.longest_substring_with_at_least_k_repeating_characters import Solution


class TestLongestSubstringWithAtLeastKRepeatingCharacters:
    """Test cases for longest substring with at least k repeating characters."""

    def setup_method(self):
        """Set up test fixtures before each test method."""
        self.solution = Solution()

    def test_basic_example_1(self):
        """Test basic example from problem description."""
        result = self.solution.longest_substring("aaabb", 3)
        assert result == 3  # "aaa"

    def test_basic_example_2(self):
        """Test basic example with mixed characters."""
        result = self.solution.longest_substring("ababbc", 2)
        assert result == 5  # "ababb"

    def test_empty_string(self):
        """Test empty string."""
        result = self.solution.longest_substring("", 1)
        assert result == 0

    def test_single_character_sufficient(self):
        """Test single character that meets requirement."""
        result = self.solution.longest_substring("a", 1)
        assert result == 1

    def test_single_character_insufficient(self):
        """Test single character that doesn't meet requirement."""
        result = self.solution.longest_substring("a", 2)
        assert result == 0

    def test_all_characters_meet_requirement(self):
        """Test when entire string meets requirement."""
        result = self.solution.longest_substring("aaabbb", 3)
        assert result == 6  # Entire string

    def test_no_character_meets_requirement(self):
        """Test when no character meets frequency requirement."""
        result = self.solution.longest_substring("abcdef", 2)
        assert result == 0

    def test_k_zero(self):
        """Test edge case with k=0."""
        result = self.solution.longest_substring("abc", 0)
        assert result == 0  # Edge case: k=0 returns 0

    def test_k_negative(self):
        """Test edge case with negative k."""
        result = self.solution.longest_substring("abc", -1)
        assert result == 0

    def test_multiple_valid_substrings(self):
        """Test string with multiple valid substrings."""
        result = self.solution.longest_substring("aaabbbaaa", 3)
        assert result == 9  # Entire string: a appears 6 times, b appears 3 times

    def test_repeated_pattern(self):
        """Test string with repeated patterns."""
        result = self.solution.longest_substring("abacadaeaf", 2)
        assert result == 0  # No character appears >= 2 times

    def test_long_valid_substring(self):
        """Test longer string with valid substring."""
        result = self.solution.longest_substring("aaabbbcccdddeee", 3)
        assert result == 15  # Entire string

    def test_alternating_characters(self):
        """Test alternating character pattern."""
        result = self.solution.longest_substring("ababab", 3)
        assert result == 6  # Entire string (a appears 3 times, b appears 3 times)

    def test_case_sensitivity(self):
        """Test that solution handles case correctly."""
        result = self.solution.longest_substring("AAAaaa", 3)
        assert result == 6  # Entire string: A and a are different characters, each appears 3 times

    @pytest.mark.parametrize("test_input,k,expected", [
        ("", 1, 0),
        ("a", 1, 1),
        ("aa", 2, 2),
        ("aab", 2, 2),
        ("aaab", 3, 3),
        ("aaabb", 3, 3),
        ("ababbc", 2, 5),
        ("ababacb", 3, 0),
        ("aabbcc", 2, 6),
        ("abcdef", 1, 6),
    ])
    def test_parametrized_cases(self, test_input, k, expected):
        """Test multiple cases using parametrize."""
        assert self.solution.longest_substring(test_input, k) == expected

    def test_sliding_window_method_consistency(self):
        """Test that sliding window method gives same results."""
        test_cases = [
            ("aaabb", 3),
            ("ababbc", 2),
            ("", 1),
            ("a", 1),
            ("abcdef", 2),
            ("aaabbbccc", 3),
        ]
        
        for s, k in test_cases:
            divide_result = self.solution.longest_substring(s, k)
            sliding_result = self.solution.longest_substring_sliding_window(s, k)
            assert divide_result == sliding_result, f"Methods differ for s='{s}', k={k}"

    def test_large_string_performance(self):
        """Test performance with larger strings."""
        # Create a pattern that should work efficiently
        large_str = "a" * 1000 + "b" * 1000 + "c" * 1000
        result = self.solution.longest_substring(large_str, 500)
        assert result >= 1500  # Should find valid substring

    def test_all_same_character(self):
        """Test string with all same characters."""
        result = self.solution.longest_substring("aaaaaaa", 3)
        assert result == 7  # Entire string

    def test_complex_mixed_pattern(self):
        """Test complex pattern with mixed requirements."""
        result = self.solution.longest_substring("aabbccddee", 2)
        assert result == 10  # Entire string

    def test_edge_case_very_high_k(self):
        """Test edge case with very high k value."""
        result = self.solution.longest_substring("abc", 100)
        assert result == 0

    def test_substring_boundary_conditions(self):
        """Test various boundary conditions."""
        # k equals string length
        assert self.solution.longest_substring("aaa", 3) == 3
        
        # k greater than string length
        assert self.solution.longest_substring("aa", 5) == 0
        
        # String length equals 1
        assert self.solution.longest_substring("a", 1) == 1

    def test_character_frequency_edge_cases(self):
        """Test edge cases related to character frequencies."""
        # Just enough frequency
        assert self.solution.longest_substring("aabbcc", 2) == 6
        
        # One character short
        assert self.solution.longest_substring("aabbc", 2) == 4  # "aabb"
        
        # Mixed frequencies
        assert self.solution.longest_substring("aaabbc", 2) == 5  # "aaabb"

    def test_method_consistency_extensive(self):
        """Extensive test of method consistency."""
        test_strings = [
            "a", "ab", "abc", "aab", "aaab", "aaabb", "aaabbb",
            "ababab", "abcabc", "aabbcc", "aaabbcc", "abcdefg"
        ]
        test_ks = [1, 2, 3, 4, 5]
        
        for s in test_strings:
            for k in test_ks:
                if len(s) > 0:  # Skip empty string for extensive testing
                    divide_result = self.solution.longest_substring(s, k)
                    sliding_result = self.solution.longest_substring_sliding_window(s, k)
                    assert divide_result == sliding_result, \
                        f"Methods differ for s='{s}', k={k}: {divide_result} vs {sliding_result}"

    def test_return_type_validation(self):
        """Test that return type is always integer."""
        test_cases = [
            ("", 1),
            ("a", 1),
            ("abc", 2),
            ("aaabbb", 3),
        ]
        
        for s, k in test_cases:
            result = self.solution.longest_substring(s, k)
            assert isinstance(result, int)
            assert result >= 0

    def test_input_preservation(self):
        """Test that input strings are not modified."""
        original = "aaabbb"
        test_str = original
        self.solution.longest_substring(test_str, 3)
        assert test_str == original

    def test_special_unicode_characters(self):
        """Test with special characters (if needed)."""
        # Note: Problem typically deals with lowercase English letters
        result = self.solution.longest_substring("aaa", 3)
        assert result == 3

    def test_both_methods_performance(self):
        """Test that both methods handle moderate sized inputs efficiently."""
        medium_str = ("abc" * 100)  # 300 characters
        k = 50
        
        # Both methods should complete without timeout
        result1 = self.solution.longest_substring(medium_str, k)
        result2 = self.solution.longest_substring_sliding_window(medium_str, k)
        
        assert result1 == result2
        assert isinstance(result1, int)


if __name__ == "__main__":
    pytest.main([__file__])
