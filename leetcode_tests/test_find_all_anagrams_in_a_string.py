"""
Test cases for LeetCode Problem #438: Find All Anagrams in a String
"""
import unittest
from leetcode.find_all_anagrams_in_a_string import Solution


class TestFindAllAnagrams(unittest.TestCase):
    """Test cases for the FindAllAnagrams solution."""

    def setUp(self):
        """Set up test fixtures before each test method."""
        self.solution = Solution()

    def test_example_case_1(self):
        """Test the first example case."""
        text = "cbaebabacd"
        pattern = "abc"
        result = self.solution.findAnagrams(text, pattern)
        expected = [0, 6]
        assert sorted(result) == sorted(expected)

    def test_example_case_2(self):
        """Test the second example case."""
        text = "abab"
        pattern = "ab"
        result = self.solution.findAnagrams(text, pattern)
        # All positions have anagrams: "ab" at 0, "ba" at 1, "ab" at 2
        expected = [0, 1, 2]
        assert sorted(result) == sorted(expected)

    def test_no_anagrams(self):
        """Test case with no anagrams."""
        text = "hello"
        pattern = "xyz"
        result = self.solution.findAnagrams(text, pattern)
        expected = []
        assert result == expected

    def test_pattern_longer_than_text(self):
        """Test when pattern is longer than text."""
        text = "ab"
        pattern = "abc"
        result = self.solution.findAnagrams(text, pattern)
        expected = []
        assert result == expected

    def test_empty_text(self):
        """Test with empty text."""
        text = ""
        pattern = "a"
        result = self.solution.findAnagrams(text, pattern)
        expected = []
        assert result == expected

    def test_single_character_pattern(self):
        """Test with single character pattern."""
        text = "aaaaaa"
        pattern = "a"
        result = self.solution.findAnagrams(text, pattern)
        expected = [0, 1, 2, 3, 4, 5]
        assert result == expected

    def test_single_character_text(self):
        """Test with single character text."""
        text = "a"
        pattern = "a"
        result = self.solution.findAnagrams(text, pattern)
        expected = [0]
        assert result == expected

    def test_all_same_characters(self):
        """Test with all same characters."""
        text = "aaaa"
        pattern = "aa"
        result = self.solution.findAnagrams(text, pattern)
        expected = [0, 1, 2]
        assert result == expected

    def test_exact_match(self):
        """Test when text exactly matches pattern."""
        text = "abc"
        pattern = "abc"
        result = self.solution.findAnagrams(text, pattern)
        expected = [0]
        assert result == expected

    def test_reverse_pattern(self):
        """Test with reverse of pattern."""
        text = "cba"
        pattern = "abc"
        result = self.solution.findAnagrams(text, pattern)
        expected = [0]
        assert result == expected

    def test_multiple_overlapping_anagrams(self):
        """Test multiple overlapping anagrams."""
        text = "abababa"
        pattern = "ab"
        result = self.solution.findAnagrams(text, pattern)
        # Every 2-char substring is an anagram
        expected = [0, 1, 2, 3, 4, 5]
        assert sorted(result) == sorted(expected)

    def test_complex_pattern(self):
        """Test with complex pattern."""
        text = "abacadaeaf"
        pattern = "aaa"
        result = self.solution.findAnagrams(text, pattern)
        expected = []  # No substring has 3 'a's
        assert result == expected

    def test_repeated_characters_in_pattern(self):
        """Test pattern with repeated characters."""
        text = "aabaaaba"
        pattern = "aab"
        result = self.solution.findAnagrams(text, pattern)
        # Check each position: aab(0), aba(1), baa(2), aaa(3), aab(4), aba(5)
        expected = [0, 1, 2, 4, 5]
        assert sorted(result) == sorted(expected)

    def test_case_sensitivity(self):
        """Test case sensitivity."""
        text = "AbA"
        pattern = "aB"
        result = self.solution.findAnagrams(text, pattern)
        expected = []  # Case sensitive
        assert result == expected

    def test_long_text_short_pattern(self):
        """Test long text with short pattern."""
        text = "a" * 1000 + "b" + "a" * 1000
        pattern = "ab"
        result = self.solution.findAnagrams(text, pattern)
        expected = [999, 1000]
        assert sorted(result) == sorted(expected)

    def test_consecutive_anagrams(self):
        """Test consecutive anagrams."""
        text = "abcabc"
        pattern = "abc"
        result = self.solution.findAnagrams(text, pattern)
        # All positions are anagrams: abc, bca, cab, abc
        expected = [0, 1, 2, 3]
        assert result == expected

    def test_alternating_pattern(self):
        """Test alternating character pattern."""
        text = "ababab"
        pattern = "ba"
        result = self.solution.findAnagrams(text, pattern)
        # Every 2-char substring is an anagram: ab, ba, ab, ba, ab
        expected = [0, 1, 2, 3, 4]
        assert result == expected

    def test_no_repeating_characters(self):
        """Test with no repeating characters."""
        text = "abcdefg"
        pattern = "fed"
        result = self.solution.findAnagrams(text, pattern)
        expected = [3]  # "def" at index 3
        assert result == expected

    def test_partial_anagrams(self):
        """Test detecting only complete anagrams."""
        text = "abcd"
        pattern = "abc"
        result = self.solution.findAnagrams(text, pattern)
        expected = [0]  # Only "abc" at index 0
        assert result == expected

    def test_return_type_and_order(self):
        """Test that return type is list and indices are in order."""
        text = "bac"
        pattern = "abc"
        result = self.solution.findAnagrams(text, pattern)
        assert isinstance(result, list)
        assert all(isinstance(idx, int) for idx in result)
        assert result == sorted(result)

    def test_algorithm_correctness(self):
        """Test algorithm correctness with various patterns."""
        test_cases = [
            ("a", "a", [0]),
            ("ab", "ba", [0]),
            ("abc", "bca", [0]),
            ("aab", "aba", [0]),
            ("abcd", "ab", [0]),
        ]
        
        for text, pattern, expected in test_cases:
            with self.subTest(text=text, pattern=pattern):
                result = self.solution.findAnagrams(text, pattern)
                assert sorted(result) == sorted(expected)

    def test_boundary_conditions(self):
        """Test edge cases and boundary conditions."""
        # Pattern same length as text
        result = self.solution.findAnagrams("abc", "cab")
        assert result == [0]
        
        # No matching characters
        result = self.solution.findAnagrams("abcd", "efgh")
        assert result == []

    def test_performance_reasonable_input(self):
        """Test performance with reasonable input size."""
        # Create a longer string with pattern occurrences
        text = "ab" * 500  # "ababab...ab" (1000 chars)
        pattern = "ba"
        
        result = self.solution.findAnagrams(text, pattern)
        # Every position except the last has an anagram
        expected = list(range(999))
        assert result == expected

    def test_duplicate_characters_edge_case(self):
        """Test edge case with many duplicate characters."""
        text = "aaabbbccc"
        pattern = "abc"
        result = self.solution.findAnagrams(text, pattern)
        # No valid anagrams (each substring has wrong character counts)
        expected = []
        assert result == expected

    def test_anagram_detection_accuracy(self):
        """Test accurate anagram detection."""
        text = "listen"
        pattern = "silent"
        result = self.solution.findAnagrams(text, pattern)
        expected = [0]
        assert result == expected

    def test_sliding_window_correctness(self):
        """Test sliding window implementation correctness."""
        text = "abcdefabc"
        pattern = "abc"
        result = self.solution.findAnagrams(text, pattern)
        expected = [0, 6]
        assert result == expected

    def test_deterministic_behavior(self):
        """Test that algorithm produces consistent results."""
        text = "abcabc"
        pattern = "abc"
        result1 = self.solution.findAnagrams(text, pattern)
        result2 = self.solution.findAnagrams(text, pattern)
        assert result1 == result2

    def test_character_frequency_matching(self):
        """Test accurate character frequency matching."""
        text = "aabbcc"
        pattern = "abc"
        result = self.solution.findAnagrams(text, pattern)
        expected = []  # No valid anagrams (different frequencies)
        assert result == expected

    def test_mixed_anagram_patterns(self):
        """Test various mixed anagram patterns."""
        text = "abcabcabc"
        pattern = "cab"
        result = self.solution.findAnagrams(text, pattern)
        # All 3-char substrings are anagrams
        expected = [0, 1, 2, 3, 4, 5, 6]
        assert result == expected


if __name__ == "__main__":
    unittest.main()
