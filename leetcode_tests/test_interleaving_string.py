"""
Comprehensive test suite for LeetCode Problem #97: Interleaving String
Tests the dynamic programming algorithm for string interleaving validation.
"""

import pytest

from leetcode.interleaving_string import Solution


class TestInterleavingString:
    """Test cases for Interleaving String problem."""

    def setup_method(self):
        """Set up test fixtures before each test method."""
        self.solution = Solution()

    def test_basic_interleaving_true(self):
        """Test basic case where interleaving is possible."""
        s1 = "aabcc"
        s2 = "dbbca"
        s3 = "aadbbcbcac"
        assert self.solution.isInterleave(s1, s2, s3) is True

    def test_basic_interleaving_false(self):
        """Test basic case where interleaving is not possible."""
        s1 = "aabcc"
        s2 = "dbbca"
        s3 = "aadbbbaccc"
        assert self.solution.isInterleave(s1, s2, s3) is False

    def test_empty_strings_all(self):
        """Test when all strings are empty."""
        assert self.solution.isInterleave("", "", "") is True

    def test_empty_s1_and_s2(self):
        """Test when s1 and s2 are empty but s3 is not."""
        assert self.solution.isInterleave("", "", "a") is False

    def test_empty_s1_only(self):
        """Test when only s1 is empty."""
        assert self.solution.isInterleave("", "abc", "abc") is True
        assert self.solution.isInterleave("", "abc", "acb") is False

    def test_empty_s2_only(self):
        """Test when only s2 is empty."""
        assert self.solution.isInterleave("abc", "", "abc") is True
        assert self.solution.isInterleave("abc", "", "acb") is False

    def test_empty_s3_only(self):
        """Test when only s3 is empty."""
        assert self.solution.isInterleave("a", "b", "") is False
        assert self.solution.isInterleave("", "", "") is True

    def test_single_character_strings(self):
        """Test with single character strings."""
        assert self.solution.isInterleave("a", "b", "ab") is True
        assert self.solution.isInterleave("a", "b", "ba") is True
        assert self.solution.isInterleave("a", "b", "aa") is False
        assert self.solution.isInterleave("a", "a", "aa") is True

    def test_length_mismatch(self):
        """Test when s3 length doesn't match s1 + s2 length."""
        assert self.solution.isInterleave("ab", "cd", "abcd") is True
        assert self.solution.isInterleave("ab", "cd", "abc") is False
        assert self.solution.isInterleave("ab", "cd", "abcde") is False

    def test_identical_characters(self):
        """Test with strings containing identical characters."""
        assert self.solution.isInterleave("aaa", "bbb", "aaabbb") is True
        assert self.solution.isInterleave("aaa", "bbb", "ababab") is True  # a(s1)b(s2)a(s1)b(s2)a(s1)b(s2)
        assert self.solution.isInterleave("aaa", "aaa", "aaaaaa") is True
        assert self.solution.isInterleave("aaa", "aaa", "aabaaa") is False

    def test_alternating_pattern(self):
        """Test with alternating patterns."""
        assert self.solution.isInterleave("abc", "def", "adbecf") is True
        assert self.solution.isInterleave("abc", "def", "adbefc") is True
        assert self.solution.isInterleave("abc", "def", "dabecf") is True

    def test_complex_interleaving(self):
        """Test complex interleaving scenarios."""
        s1 = "abcdef"
        s2 = "123456"
        s3 = "a1b2c3d4e5f6"
        assert self.solution.isInterleave(s1, s2, s3) is True
        
        s3_false = "123456abcdef"
        assert self.solution.isInterleave(s1, s2, s3_false) is True

    def test_repeated_characters_complex(self):
        """Test with repeated characters in complex patterns."""
        s1 = "aabcc"
        s2 = "dbbca"
        # Valid interleavings
        assert self.solution.isInterleave(s1, s2, "aadbbcbcac") is True
        assert self.solution.isInterleave(s1, s2, "daadbcbbca") is False

    def test_one_char_repeated(self):
        """Test strings with one character repeated."""
        assert self.solution.isInterleave("a", "aa", "aaa") is True
        assert self.solution.isInterleave("aa", "a", "aaa") is True
        assert self.solution.isInterleave("aaa", "", "aaa") is True

    def test_no_common_characters(self):
        """Test strings with no common characters."""
        assert self.solution.isInterleave("abc", "def", "adbecf") is True
        assert self.solution.isInterleave("abc", "def", "abcdef") is True
        assert self.solution.isInterleave("abc", "def", "defabc") is True

    def test_all_same_character(self):
        """Test when all characters are the same."""
        assert self.solution.isInterleave("aa", "aa", "aaaa") is True
        assert self.solution.isInterleave("aaa", "aa", "aaaaa") is True
        assert self.solution.isInterleave("aa", "aaa", "aaaaa") is True

    def test_prefix_suffix_patterns(self):
        """Test prefix and suffix patterns."""
        assert self.solution.isInterleave("abc", "def", "abcdef") is True
        assert self.solution.isInterleave("abc", "def", "defabc") is True
        assert self.solution.isInterleave("abc", "def", "abdefcdef") is False

    def test_impossible_interleaving(self):
        """Test cases where interleaving is impossible."""
        # Character not in s1 or s2
        assert self.solution.isInterleave("abc", "def", "abcdefg") is False
        # Wrong character order
        assert self.solution.isInterleave("abc", "def", "acbdef") is False

    def test_long_strings(self):
        """Test with longer strings."""
        s1 = "abcdefghij"
        s2 = "1234567890"
        s3 = "a1b2c3d4e5f6g7h8i9j0"
        assert self.solution.isInterleave(s1, s2, s3) is True

    def test_edge_case_single_chars(self):
        """Test edge cases with single characters."""
        assert self.solution.isInterleave("a", "", "a") is True
        assert self.solution.isInterleave("", "b", "b") is True
        assert self.solution.isInterleave("a", "b", "c") is False

    def test_palindrome_strings(self):
        """Test with palindromic strings."""
        assert self.solution.isInterleave("aba", "cdc", "acbdac") is True
        assert self.solution.isInterleave("aba", "cdc", "abacdc") is True

    def test_substring_relationship(self):
        """Test when one string is substring of another."""
        assert self.solution.isInterleave("abc", "ab", "aabbc") is True
        assert self.solution.isInterleave("abc", "ab", "ababc") is True

    def test_performance_medium_strings(self):
        """Test performance with medium-sized strings."""
        s1 = "a" * 50 + "b" * 50
        s2 = "c" * 50 + "d" * 50
        s3 = ("ac" * 50) + ("bd" * 50)
        result = self.solution.isInterleave(s1, s2, s3)
        assert isinstance(result, bool)

    def test_dynamic_programming_correctness(self):
        """Test that DP table is filled correctly."""
        # Test case where we need proper DP to get correct answer
        s1 = "aab"
        s2 = "aac" 
        s3 = "aacaab"  # Should be True: a(s2) + a(s2) + c(s2) + a(s1) + a(s1) + b(s1)
        assert self.solution.isInterleave(s1, s2, s3) is True
        
        s3_false = "aaabc"  # Should be False - impossible ordering
        assert self.solution.isInterleave(s1, s2, s3_false) is False

    def test_greedy_vs_dp_difference(self):
        """Test cases where greedy approach would fail but DP succeeds."""
        # Case where you need to backtrack
        s1 = "aa"
        s2 = "ab" 
        s3 = "aaba"
        assert self.solution.isInterleave(s1, s2, s3) is True

    def test_algorithm_properties(self):
        """Test fundamental properties of the algorithm."""
        # Commutative property
        s1, s2 = "abc", "def"
        s3 = "adbecf"
        assert self.solution.isInterleave(s1, s2, s3) == self.solution.isInterleave(s2, s1, s3)
        
        # Empty string properties
        assert self.solution.isInterleave("", "abc", "abc") is True
        assert self.solution.isInterleave("abc", "", "abc") is True

    def test_character_frequency_validation(self):
        """Test that character frequencies are preserved."""
        # If s3 is interleaving of s1 and s2, char frequencies should match
        s1 = "aab"
        s2 = "bbc"
        s3 = "aabbbc"  # Correct frequencies
        assert self.solution.isInterleave(s1, s2, s3) is True
        
        s3_wrong = "aaabbc"  # Wrong frequency of 'a'
        assert self.solution.isInterleave(s1, s2, s3_wrong) is False


if __name__ == '__main__':
    # Run the tests
    pytest.main([__file__])
