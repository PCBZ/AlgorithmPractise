"""
Comprehensive test suite for LeetCode Problem #516: Longest Palindromic Subsequence.
Tests the dynamic programming solution for finding longest palindromic subsequence.
"""
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import pytest
from leetcode.longest_palindromic_subsequence import Solution


class TestLongestPalindromicSubsequence:
    """Test cases for longest palindromic subsequence calculation."""

    def setup_method(self):
        """Set up test fixtures before each test method."""
        self.solution = Solution()

    def test_basic_example_1(self):
        """Test basic example from problem description."""
        result = self.solution.longest_palindrome_subseq("bbbab")
        assert result == 4  # "bbbb"

    def test_basic_example_2(self):
        """Test basic example with different pattern."""
        result = self.solution.longest_palindrome_subseq("cbbd")
        assert result == 2  # "bb"

    def test_single_character(self):
        """Test single character string."""
        result = self.solution.longest_palindrome_subseq("a")
        assert result == 1

    def test_empty_string(self):
        """Test empty string."""
        result = self.solution.longest_palindrome_subseq("")
        assert result == 0

    def test_two_characters_same(self):
        """Test two identical characters."""
        result = self.solution.longest_palindrome_subseq("aa")
        assert result == 2

    def test_two_characters_different(self):
        """Test two different characters."""
        result = self.solution.longest_palindrome_subseq("ab")
        assert result == 1

    def test_already_palindrome(self):
        """Test string that is already a palindrome."""
        result = self.solution.longest_palindrome_subseq("racecar")
        assert result == 7

    def test_reverse_string(self):
        """Test string and its reverse."""
        result = self.solution.longest_palindrome_subseq("abcdef")
        assert result == 1  # Any single character

    def test_all_same_characters(self):
        """Test string with all same characters."""
        result = self.solution.longest_palindrome_subseq("aaaa")
        assert result == 4

    def test_alternating_pattern(self):
        """Test alternating pattern."""
        result = self.solution.longest_palindrome_subseq("abab")
        assert result == 3  # "aba" or "bab"

    def test_complex_palindrome(self):
        """Test complex palindromic pattern."""
        result = self.solution.longest_palindrome_subseq("aabaa")
        assert result == 5  # "aabaa" itself

    def test_no_repeated_characters(self):
        """Test string with no repeated characters."""
        result = self.solution.longest_palindrome_subseq("abcde")
        assert result == 1

    def test_longer_example(self):
        """Test longer string example."""
        result = self.solution.longest_palindrome_subseq("babad")
        assert result == 3  # "bab" or "aba"

    def test_symmetric_pattern(self):
        """Test symmetric pattern."""
        result = self.solution.longest_palindrome_subseq("abcba")
        assert result == 5  # Entire string

    def test_partial_palindrome(self):
        """Test string with partial palindromic subsequence."""
        result = self.solution.longest_palindrome_subseq("aab")
        assert result == 2  # "aa"

    def test_mixed_case_letters(self):
        """Test mixed case letters (treated as different)."""
        result = self.solution.longest_palindrome_subseq("AaA")
        assert result == 3  # "AaA" entire string is palindromic

    def test_long_palindrome_embedded(self):
        """Test long palindrome embedded in other characters."""
        result = self.solution.longest_palindrome_subseq("xabacabay")
        assert result == 7  # "abacaba"

    def test_repeated_pattern(self):
        """Test repeated pattern."""
        result = self.solution.longest_palindrome_subseq("abcabc")
        assert result == 3  # "aca" or "bcb"

    def test_get_longest_palindrome_subseq_basic(self):
        """Test getting the actual palindromic subsequence string."""
        result = self.solution.get_longest_palindrome_subseq("bbbab")
        assert len(result) == 4
        assert self._is_palindrome(result)
        assert self._is_subsequence(result, "bbbab")

    def test_get_longest_palindrome_subseq_simple(self):
        """Test getting palindromic subsequence for simple case."""
        result = self.solution.get_longest_palindrome_subseq("aba")
        assert result == "aba"

    def test_get_longest_palindrome_subseq_empty(self):
        """Test getting palindromic subsequence for empty string."""
        result = self.solution.get_longest_palindrome_subseq("")
        assert result == ""

    def test_algorithm_correctness_properties(self):
        """Test fundamental properties of the algorithm."""
        test_cases = [
            "a",
            "aa", 
            "ab",
            "aba",
            "abcba",
            "racecar",
            "bbbab"
        ]
        
        for test_str in test_cases:
            length = self.solution.longest_palindrome_subseq(test_str)
            actual_subseq = self.solution.get_longest_palindrome_subseq(test_str)
            
            # Property 1: Length should match actual subsequence length
            assert len(actual_subseq) == length
            
            # Property 2: Result should be a palindrome
            assert self._is_palindrome(actual_subseq)
            
            # Property 3: Result should be a subsequence of original
            assert self._is_subsequence(actual_subseq, test_str)

    def test_boundary_conditions(self):
        """Test boundary conditions."""
        # Minimum length
        assert self.solution.longest_palindrome_subseq("") == 0
        assert self.solution.longest_palindrome_subseq("a") == 1
        
        # Maximum possible for given patterns
        assert self.solution.longest_palindrome_subseq("aa") == 2
        assert self.solution.longest_palindrome_subseq("aaa") == 3

    def test_edge_cases_dp_table(self):
        """Test edge cases for DP table construction."""
        # Single character
        result = self.solution.longest_palindrome_subseq("x")
        assert result == 1
        
        # Two identical
        result = self.solution.longest_palindrome_subseq("xx")
        assert result == 2
        
        # Three characters
        result = self.solution.longest_palindrome_subseq("abc")
        assert result == 1

    def test_performance_longer_strings(self):
        """Test performance with longer strings."""
        # Create a longer string with known palindromic pattern
        long_str = "a" + "b" * 50 + "a"
        result = self.solution.longest_palindrome_subseq(long_str)
        assert result == 52  # "a" + 50 "b"s + "a"

    def test_palindrome_in_middle(self):
        """Test palindromic subsequence in middle of string."""
        result = self.solution.longest_palindrome_subseq("xabacabax")
        assert result >= 7  # "abacaba" or similar

    def test_overlapping_characters(self):
        """Test overlapping character patterns."""
        result = self.solution.longest_palindrome_subseq("aabbaa")
        assert result == 6  # Entire string

    def test_complex_mixed_pattern(self):
        """Test complex mixed character pattern."""
        result = self.solution.longest_palindrome_subseq("abcdefghijklmnopqrstuvwxyz")
        assert result == 1  # Only single characters

    def test_numeric_characters(self):
        """Test with numeric characters."""
        result = self.solution.longest_palindrome_subseq("12321")
        assert result == 5  # Entire string

    def test_special_characters(self):
        """Test with special characters."""
        result = self.solution.longest_palindrome_subseq("!@#@!")
        assert result == 5  # Entire string

    def test_return_type_validation(self):
        """Test that return type is correct integer."""
        result = self.solution.longest_palindrome_subseq("test")
        assert isinstance(result, int)
        assert result >= 0

    def test_input_preservation(self):
        """Test that input string is not modified."""
        original = "test"
        test_str = original
        self.solution.longest_palindrome_subseq(test_str)
        assert test_str == original

    def test_both_methods_consistency(self):
        """Test that both methods return consistent results."""
        test_cases = ["", "a", "ab", "aba", "abcba", "bbbab", "racecar"]
        
        for test_str in test_cases:
            length = self.solution.longest_palindrome_subseq(test_str)
            actual = self.solution.get_longest_palindrome_subseq(test_str)
            assert len(actual) == length

    def test_large_alphabet_coverage(self):
        """Test coverage of large alphabet."""
        # String with all letters appearing twice
        test_str = "abcdefghijklmnopqrstuvwxyzzyxwvutsrqponmlkjihgfedcba"
        result = self.solution.longest_palindrome_subseq(test_str)
        assert result == 52  # All characters can form palindrome

    def test_specific_palindrome_patterns(self):
        """Test specific palindrome patterns."""
        # Pattern: abccba
        assert self.solution.longest_palindrome_subseq("abccba") == 6
        
        # Pattern: raceacar  
        assert self.solution.longest_palindrome_subseq("raceacar") == 7  # racecar
        
        # Pattern: abacabad
        assert self.solution.longest_palindrome_subseq("abacabad") >= 5  # abacaba

    def test_worst_case_scenarios(self):
        """Test worst case scenarios for the algorithm."""
        # All different characters
        worst_case = "abcdefghij"
        result = self.solution.longest_palindrome_subseq(worst_case)
        assert result == 1
        
        # Reverse strings
        reverse_case = "abcdefedcba"
        result = self.solution.longest_palindrome_subseq(reverse_case)
        assert result >= 6  # Should find good palindromic subsequence

    def _is_palindrome(self, s: str) -> bool:
        """Helper method to check if string is palindrome."""
        return s == s[::-1]

    def _is_subsequence(self, subseq: str, original: str) -> bool:
        """Helper method to check if subseq is subsequence of original."""
        i = j = 0
        while i < len(subseq) and j < len(original):
            if subseq[i] == original[j]:
                i += 1
            j += 1
        return i == len(subseq)


if __name__ == "__main__":
    pytest.main([__file__])
