"""
Comprehensive tests for Minimum Window Substring problem.

Tests the sliding window algorithm for finding minimum window substring
that contains all characters from target string.
"""
import pytest
import sys
import os

# Add parent directory to path for imports
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Import using exec to handle the non-standard module name
solution_globals = {}
with open(os.path.join(os.path.dirname(__file__), '..', 'leetcode', 'Minimum_Window_Substring.py'), 'r') as f:
    exec(f.read(), solution_globals)

Solution = solution_globals['Solution']


class TestMinimumWindowSubstring:
    """Test class for minimum window substring implementation."""

    def setup_method(self):
        """Set up test fixtures before each test method."""
        self.solution = Solution()

    @pytest.fixture
    def leetcode_example_1(self):
        """First LeetCode example."""
        return "ADOBECODEBANC", "ABC"

    @pytest.fixture
    def leetcode_example_2(self):
        """Second LeetCode example."""
        return "a", "a"

    @pytest.fixture
    def leetcode_example_3(self):
        """Third LeetCode example."""
        return "a", "aa"

    def test_leetcode_example_1(self, leetcode_example_1):
        """Test first LeetCode example."""
        s, t = leetcode_example_1
        result = self.solution.minWindow(s, t)
        assert result == "BANC"

    def test_leetcode_example_2(self, leetcode_example_2):
        """Test second LeetCode example."""
        s, t = leetcode_example_2
        result = self.solution.minWindow(s, t)
        assert result == "a"

    def test_leetcode_example_3(self, leetcode_example_3):
        """Test third LeetCode example."""
        s, t = leetcode_example_3
        result = self.solution.minWindow(s, t)
        assert result == ""

    def test_empty_strings(self):
        """Test with empty strings."""
        assert self.solution.minWindow("", "") == ""
        assert self.solution.minWindow("abc", "") == ""
        assert self.solution.minWindow("", "a") == ""

    def test_single_character(self):
        """Test with single characters."""
        assert self.solution.minWindow("a", "a") == "a"
        assert self.solution.minWindow("a", "b") == ""
        assert self.solution.minWindow("b", "a") == ""

    def test_identical_strings(self):
        """Test when s and t are identical."""
        assert self.solution.minWindow("abc", "abc") == "abc"
        assert self.solution.minWindow("aab", "aab") == "aab"

    def test_t_longer_than_s(self):
        """Test when t is longer than s."""
        assert self.solution.minWindow("a", "aa") == ""
        assert self.solution.minWindow("ab", "abc") == ""

    def test_no_valid_window(self):
        """Test when no valid window exists."""
        assert self.solution.minWindow("abc", "d") == ""
        assert self.solution.minWindow("abc", "aab") == ""

    def test_entire_string_is_minimum(self):
        """Test when entire string is the minimum window."""
        assert self.solution.minWindow("abc", "abc") == "abc"
        assert self.solution.minWindow("abc", "cba") == "abc"

    def test_multiple_occurrences(self):
        """Test with multiple occurrences of characters."""
        result = self.solution.minWindow("ADOBECODEBANC", "AABC")
        # Should find minimum window containing 2 A's, 1 B, 1 C
        assert len(result) == 11
        assert "ADOBECODEBA" == result

    def test_repeated_characters_in_t(self):
        """Test with repeated characters in target."""
        assert self.solution.minWindow("aa", "aa") == "aa"
        assert self.solution.minWindow("aab", "aa") == "aa"
        assert self.solution.minWindow("baa", "aa") == "aa"

    def test_case_sensitivity(self):
        """Test case sensitivity."""
        assert self.solution.minWindow("Aa", "A") == "A"
        assert self.solution.minWindow("Aa", "a") == "a"
        assert self.solution.minWindow("Aa", "Aa") == "Aa"

    def test_minimum_at_beginning(self):
        """Test when minimum window is at the beginning."""
        assert self.solution.minWindow("abcdef", "abc") == "abc"
        assert self.solution.minWindow("abcxyz", "abc") == "abc"

    def test_minimum_at_end(self):
        """Test when minimum window is at the end."""
        assert self.solution.minWindow("xyzabc", "abc") == "abc"
        assert self.solution.minWindow("defabc", "abc") == "abc"

    def test_minimum_in_middle(self):
        """Test when minimum window is in the middle."""
        assert self.solution.minWindow("xabcy", "abc") == "abc"
        assert self.solution.minWindow("xabcyabc", "abc") == "abc"

    def test_overlapping_windows(self):
        """Test with overlapping potential windows."""
        result = self.solution.minWindow("acbbaca", "aba")
        # Should find minimum window containing a, b, a
        assert result == "baca"  # Minimum window of length 4

    def test_all_same_character(self):
        """Test with all same characters."""
        assert self.solution.minWindow("aaaa", "aa") == "aa"
        assert self.solution.minWindow("aaaa", "aaa") == "aaa"

    def test_complex_pattern(self):
        """Test with complex character patterns."""
        result = self.solution.minWindow("abcdefghijklmnop", "cfk")
        assert result == "cdefghijk"

    def test_duplicate_chars_different_positions(self):
        """Test duplicate characters at different positions."""
        result = self.solution.minWindow("acbbaca", "aa")
        assert result == "aca"

    def test_long_string_short_target(self):
        """Test long string with short target."""
        s = "a" * 1000 + "b" + "a" * 1000
        t = "ab"
        result = self.solution.minWindow(s, t)
        assert len(result) == 2  # Should be minimal "ab"
        assert result == "ab"

    def test_performance_repeated_pattern(self):
        """Test performance with repeated patterns."""
        s = "abcabc" * 100
        t = "abc"
        result = self.solution.minWindow(s, t)
        assert result == "abc"

    def test_edge_case_single_match(self):
        """Test edge case with single character match."""
        assert self.solution.minWindow("ab", "a") == "a"
        assert self.solution.minWindow("ab", "b") == "b"
        assert self.solution.minWindow("ba", "a") == "a"

    def test_multiple_solutions_same_length(self):
        """Test when multiple minimum windows have same length."""
        result = self.solution.minWindow("abab", "ab")
        assert result in ["ab", "ba"]  # Both are valid

    def test_unicode_characters(self):
        """Test with unicode characters."""
        assert self.solution.minWindow("αβγ", "αγ") == "αβγ"
        assert self.solution.minWindow("αβα", "α") == "α"

    def test_numbers_and_symbols(self):
        """Test with numbers and symbols."""
        assert self.solution.minWindow("123!@#", "1#") == "123!@#"
        assert self.solution.minWindow("a1b2c3", "1c") == "1b2c"

    def test_window_shrinking(self):
        """Test optimal window shrinking."""
        result = self.solution.minWindow("ADOBECODEBANC", "ABC")
        assert result == "BANC"
        # Verify it's actually minimal
        assert len(result) == 4

    def test_frequency_matching(self):
        """Test exact frequency matching requirement."""
        # Need exactly 2 A's, not just 1
        result = self.solution.minWindow("AABC", "AAB")
        assert result == "AAB"


if __name__ == '__main__':
    pytest.main([__file__])
