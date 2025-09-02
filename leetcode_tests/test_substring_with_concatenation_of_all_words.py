"""
Comprehensive test suite for LeetCode Problem #30: 
Substring with Concatenation of All Words

Tests the findSubstring method which finds all starting indices of substrings
that are concatenations of all given words exactly once.
"""
import time
from collections import Counter

from leetcode.substring_with_concatenation_of_all_words import Solution


class TestSubstringWithConcatenationOfAllWords:
    """Test class for substring with concatenation of all words problem."""

    def setup_method(self):
        """Set up test fixtures before each test method."""
        self.solution = Solution()

    def test_example_case_1(self):
        """Test LeetCode example case 1."""
        s = "barfoothefoobarman"
        words = ["foo", "bar"]
        result = self.solution.findSubstring(s, words)
        expected = [0, 9]
        assert result == expected

    def test_example_case_2(self):
        """Test LeetCode example case 2."""
        s = "wordgoodgoodgoodbestword"
        words = ["word", "good", "best", "word"]
        result = self.solution.findSubstring(s, words)
        expected = []
        assert result == expected

    def test_example_case_3(self):
        """Test LeetCode example case 3."""
        s = "barfoobar"
        words = ["foo", "bar"]
        result = self.solution.findSubstring(s, words)
        expected = [0, 3]  # Both "barfoo" and "foobar" are valid
        assert result == expected

    def test_single_word_match(self):
        """Test with single word that matches."""
        s = "goodgood"
        words = ["good"]
        result = self.solution.findSubstring(s, words)
        expected = [0, 4]
        assert result == expected

    def test_single_word_no_match(self):
        """Test with single word that doesn't match."""
        s = "goodbest"
        words = ["word"]
        result = self.solution.findSubstring(s, words)
        expected = []
        assert result == expected

    def test_empty_string(self):
        """Test with empty input string."""
        s = ""
        words = ["foo", "bar"]
        result = self.solution.findSubstring(s, words)
        expected = []
        assert result == expected

    def test_empty_words_list(self):
        """Test with empty words list."""
        s = "barfoothefoobarman"
        words = []
        result = self.solution.findSubstring(s, words)
        expected = []
        assert result == expected

    def test_string_shorter_than_concatenation(self):
        """Test when string is shorter than total word length."""
        s = "bar"
        words = ["foo", "bar"]
        result = self.solution.findSubstring(s, words)
        expected = []
        assert result == expected

    def test_exact_match_whole_string(self):
        """Test when concatenation matches entire string."""
        s = "foobar"
        words = ["foo", "bar"]
        result = self.solution.findSubstring(s, words)
        expected = [0]
        assert result == expected

    def test_duplicate_words_in_list(self):
        """Test with duplicate words in the words list."""
        s = "barfoofoobarthefoobarman"
        words = ["bar", "foo", "the"]
        result = self.solution.findSubstring(s, words)
        expected = [6, 9, 12]
        assert result == expected

    def test_overlapping_matches(self):
        """Test case with overlapping potential matches."""
        s = "lingmindraboofooowingdingbarrwingmonkeypoundcake"
        words = ["fooo", "barr", "wing", "ding", "wing"]
        result = self.solution.findSubstring(s, words)
        expected = [13]  # "fooowingdingbarrwing" is a valid concatenation
        assert result == expected

    def test_repeated_characters(self):
        """Test with repeated characters in string and words."""
        s = "aaaaaaaaaa"
        words = ["aa", "aa"]
        result = self.solution.findSubstring(s, words)
        expected = [0, 1, 2, 3, 4, 5, 6]
        assert result == expected

    def test_case_sensitivity(self):
        """Test case sensitivity."""
        s = "BarFooBar"
        words = ["bar", "foo"]
        result = self.solution.findSubstring(s, words)
        expected = []
        assert result == expected

    def test_all_same_words(self):
        """Test with all identical words."""
        s = "abababab"
        words = ["ab", "ab", "ab"]
        result = self.solution.findSubstring(s, words)
        expected = [0, 2]
        assert result == expected

    def test_no_valid_concatenation(self):
        """Test when no valid concatenation exists."""
        s = "wordgoodgoodgoodbestword"
        words = ["word", "good", "best", "good"]
        result = self.solution.findSubstring(s, words)
        expected = [8]
        assert result == expected

    def test_single_character_words(self):
        """Test with single character words."""
        s = "abab"
        words = ["a", "b"]
        result = self.solution.findSubstring(s, words)
        expected = [0, 1, 2]
        assert result == expected

    def test_return_type_and_structure(self):
        """Test that return type is correct list of integers."""
        s = "barfoothefoobarman"
        words = ["foo", "bar"]
        result = self.solution.findSubstring(s, words)
        
        assert isinstance(result, list)
        for index in result:
            assert isinstance(index, int)
            assert 0 <= index < len(s)

    def test_result_order(self):
        """Test that results are returned in ascending order."""
        s = "barfoothefoobarman"
        words = ["foo", "bar"]
        result = self.solution.findSubstring(s, words)
        
        for i in range(1, len(result)):
            assert result[i] > result[i-1]

    def test_large_input_performance(self):
        """Test algorithm performance with larger input."""
        s = "a" * 1000 + "bcd" * 100
        words = ["bcd", "bcd"]
        
        start_time = time.time()
        result = self.solution.findSubstring(s, words)
        end_time = time.time()
        
        # Should complete within reasonable time
        assert end_time - start_time < 1.0
        assert isinstance(result, list)

    def test_word_boundary_verification(self):
        """Test that word boundaries are respected."""
        s = "wordgood"
        words = ["word", "good"]
        result = self.solution.findSubstring(s, words)
        expected = [0]
        assert result == expected

    def test_partial_word_rejection(self):
        """Test that partial words are not accepted."""
        s = "barfo"
        words = ["bar", "foo"]
        result = self.solution.findSubstring(s, words)
        expected = []
        assert result == expected

    def test_word_count_verification(self):
        """Test that exact word count is required."""
        s = "foobarfoo"
        words = ["foo", "bar"]
        result = self.solution.findSubstring(s, words)
        expected = [0, 3]  # Both "foobar" and "barfoo" are valid
        assert result == expected

    def test_algorithm_correctness_validation(self):
        """Validate algorithm correctness by checking each result."""
        s = "barfoothefoobarman"
        words = ["foo", "bar"]
        result = self.solution.findSubstring(s, words)
        word_len = len(words[0])
        total_len = len(words) * word_len
        
        for start_idx in result:
            # Extract substring at this position
            substring = s[start_idx:start_idx + total_len]
            
            # Break into words and verify
            found_words = []
            for i in range(0, len(substring), word_len):
                found_words.append(substring[i:i + word_len])
            
            # Check that found words match original words (order independent)
            assert Counter(found_words) == Counter(words)

    def test_edge_case_minimum_input(self):
        """Test minimum valid input case."""
        s = "a"
        words = ["a"]
        result = self.solution.findSubstring(s, words)
        expected = [0]
        assert result == expected

    def test_multiple_valid_positions(self):
        """Test string with multiple valid concatenation positions."""
        s = "abababab"
        words = ["ab", "ab"]
        result = self.solution.findSubstring(s, words)
        expected = [0, 2, 4]
        assert result == expected

    def test_complex_word_pattern(self):
        """Test with complex word patterns."""
        s = "goodgoodbestword"
        words = ["word", "good", "best", "good"]
        result = self.solution.findSubstring(s, words)
        # "good" + "good" + "best" + "word" = valid concatenation at position 0
        expected = [0]
        assert result == expected

    def test_concatenation_uniqueness(self):
        """Test that each result represents a unique valid concatenation."""
        s = "barfoobar"
        words = ["bar", "foo"]
        result = self.solution.findSubstring(s, words)
        
        # Verify no duplicates in results
        assert len(result) == len(set(result))

    def test_algorithm_efficiency_bounds(self):
        """Test algorithm stays within expected time bounds."""
        s = "test" * 50  # 200 character string
        words = ["test", "test"]
        
        start_time = time.time()
        result = self.solution.findSubstring(s, words)
        execution_time = time.time() - start_time
        
        # Should be efficient for moderate input sizes
        assert execution_time < 0.1
        assert isinstance(result, list)

    def test_mathematical_properties(self):
        """Test mathematical properties of the solution."""
        s = "abcabc"
        words = ["abc", "abc"]
        result = self.solution.findSubstring(s, words)
        
        # Total possible starting positions
        word_len = len(words[0])
        total_len = len(words) * word_len
        max_positions = len(s) - total_len + 1
        
        # Result should not exceed maximum possible positions
        assert len(result) <= max_positions
        
        # All indices should be valid
        for idx in result:
            assert 0 <= idx <= len(s) - total_len

    def test_comprehensive_edge_cases(self):
        """Test comprehensive edge cases."""
        test_cases = [
            ("", ["a"], []),  # Empty string
            ("a", [], []),    # Empty words
            ("abc", ["ab"], [0]),  # Simple match with single word
            ("abcabc", ["abc"], [0, 3]),  # Repeated pattern
            ("aaaa", ["aa", "aa"], [0]),  # All same characters
        ]
        
        for string, words, expected in test_cases:
            if words:  # Skip empty words case as it's handled separately
                result = self.solution.findSubstring(string, words)
                assert result == expected, f"Failed for s='{string}', words={words}"
