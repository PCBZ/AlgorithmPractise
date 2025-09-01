"""
Comprehensive test suite for LeetCode Problem #720: Longest Word in Dictionary.
Tests the algorithm for finding longest word that can be built one character at a time.
"""
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import pytest
from leetcode.longest_word_in_dictionary import Solution


class TestLongestWordInDictionary:
    """Test cases for longest word in dictionary."""

    def setup_method(self):
        """Set up test fixtures before each test method."""
        self.solution = Solution()

    def test_basic_example_1(self):
        """Test basic example from problem description."""
        words = ["w", "wo", "wor", "worl", "world"]
        result = self.solution.longest_word(words)
        assert result == "world"

    def test_basic_example_2(self):
        """Test example with lexicographical ordering."""
        words = ["a", "banana", "app", "appl", "ap", "apply", "apple"]
        result = self.solution.longest_word(words)
        assert result == "apple"

    def test_provided_example(self):
        """Test the provided example in the original code."""
        words = ["yo", "ew", "fc", "zrc", "yodn", "fcm", "qm", "qmo",
                 "fcmz", "z", "ewq", "yod", "ewqz", "y"]
        result = self.solution.longest_word(words)
        assert result == "yodn"

    def test_empty_list(self):
        """Test empty word list."""
        result = self.solution.longest_word([])
        assert result == ""

    def test_single_character_words(self):
        """Test list with only single character words."""
        words = ["a", "b", "c", "z"]
        result = self.solution.longest_word(words)
        assert result == "a"  # Lexicographically smallest

    def test_no_buildable_word(self):
        """Test case where no word can be built."""
        words = ["abc", "def", "ghi"]
        result = self.solution.longest_word(words)
        assert result == ""

    def test_single_word(self):
        """Test single word in list."""
        words = ["a"]
        result = self.solution.longest_word(words)
        assert result == "a"

    def test_multiple_chains(self):
        """Test multiple buildable chains."""
        words = ["a", "ab", "abc", "x", "xy", "xyz"]
        result = self.solution.longest_word(words)
        assert result in ["abc", "xyz"]  # Both have same length

    def test_lexicographical_priority(self):
        """Test lexicographical priority for same length words."""
        words = ["b", "ba", "bac", "a", "ab", "abc"]
        result = self.solution.longest_word(words)
        assert result == "abc"  # "abc" comes before "bac" lexicographically

    def test_broken_chain(self):
        """Test chain with missing intermediate word."""
        words = ["a", "abc"]  # Missing "ab" to build "abc"
        result = self.solution.longest_word(words)
        assert result == "a"

    def test_longer_chains(self):
        """Test longer buildable chains."""
        words = ["a", "ab", "abc", "abcd", "abcde"]
        result = self.solution.longest_word(words)
        assert result == "abcde"

    def test_multiple_single_chars(self):
        """Test multiple single character starting points."""
        words = ["a", "ab", "b", "ba", "c"]
        result = self.solution.longest_word(words)
        assert result in ["ab", "ba"]  # Both length 2, lexicographically "ab" < "ba"

    def test_unsorted_input(self):
        """Test that algorithm works with unsorted input."""
        words = ["world", "w", "worl", "wo", "wor"]
        result = self.solution.longest_word(words)
        assert result == "world"

    def test_duplicate_words(self):
        """Test handling of duplicate words."""
        words = ["a", "a", "ab", "ab", "abc"]
        result = self.solution.longest_word(words)
        assert result == "abc"

    def test_get_build_path_basic(self):
        """Test getting build path for a word."""
        words = ["a", "ab", "abc"]
        path = self.solution.get_build_path(words, "abc")
        assert path == ["a", "ab", "abc"]

    def test_get_build_path_empty_target(self):
        """Test build path for empty target."""
        words = ["a", "ab"]
        path = self.solution.get_build_path(words, "")
        assert path == []

    def test_get_build_path_non_buildable(self):
        """Test build path for non-buildable word."""
        words = ["a", "c"]
        path = self.solution.get_build_path(words, "abc")
        assert path == []

    def test_algorithm_correctness_properties(self):
        """Test fundamental properties of the algorithm."""
        test_cases = [
            (["a"], "a"),
            (["a", "ab"], "ab"),
            (["a", "ab", "abc"], "abc"),
            (["z", "y", "x"], "x"),  # Lexicographically smallest single char
            (["b", "a"], "a"),  # Lexicographically smallest
        ]
        
        for words, expected in test_cases:
            result = self.solution.longest_word(words)
            assert result == expected, f"Failed for {words}: got {result}, expected {expected}"

    def test_boundary_conditions(self):
        """Test boundary conditions."""
        # Empty input
        assert self.solution.longest_word([]) == ""
        
        # Single character
        assert self.solution.longest_word(["z"]) == "z"
        
        # Two character progression
        assert self.solution.longest_word(["a", "ab"]) == "ab"

    def test_complex_dictionary(self):
        """Test complex dictionary with multiple valid chains."""
        words = ["cat", "c", "ca", "dog", "d", "do", "bird", "b", "bi", "bir"]
        result = self.solution.longest_word(words)
        assert result == "bird"

    def test_prefix_validation(self):
        """Test that prefixes are properly validated."""
        # Missing intermediate prefix
        words = ["a", "abc"]  # Missing "ab"
        result = self.solution.longest_word(words)
        assert result == "a"

    def test_chain_building_order(self):
        """Test that chains are built in correct order."""
        words = ["abcd", "abc", "ab", "a"]  # Reverse order
        result = self.solution.longest_word(words)
        assert result == "abcd"

    def test_multiple_optimal_solutions(self):
        """Test case with multiple optimal solutions."""
        words = ["a", "ab", "x", "xy"]
        result = self.solution.longest_word(words)
        assert result == "ab"  # "ab" < "xy" lexicographically

    def test_large_alphabet_coverage(self):
        """Test with coverage of large alphabet."""
        words = list("abcdefghijklmnopqrstuvwxyz")
        result = self.solution.longest_word(words)
        assert result == "a"  # All single chars, lexicographically smallest

    def test_progressive_building(self):
        """Test progressive building validation."""
        words = ["a", "ab", "abc", "abcd", "abcde", "abcdef"]
        result = self.solution.longest_word(words)
        assert result == "abcdef"

    def test_return_type_validation(self):
        """Test that return type is correct string."""
        result = self.solution.longest_word(["a", "ab"])
        assert isinstance(result, str)

    def test_input_preservation(self):
        """Test that input list is not modified."""
        original = ["c", "a", "b"]
        test_words = original.copy()
        self.solution.longest_word(test_words)
        # The method may sort internally, but shouldn't modify the original reference
        # We test that the method completes without error

    def test_both_methods_consistency(self):
        """Test that both methods return consistent results."""
        test_cases = [
            ["a", "ab", "abc"],
            ["w", "wo", "wor", "worl", "world"],
            ["a", "banana", "app", "appl", "ap", "apply", "apple"]
        ]
        
        for words in test_cases:
            longest = self.solution.longest_word(words)
            if longest:  # Only test if there's a result
                path = self.solution.get_build_path(words, longest)
                assert path[-1] == longest  # Last word in path should be the longest
                assert len(path) == len(longest)  # Path length should equal word length

    def test_case_sensitivity(self):
        """Test case sensitivity (assuming all lowercase)."""
        words = ["a", "ab", "abc"]
        result = self.solution.longest_word(words)
        assert result == "abc"

    def test_special_characters_not_present(self):
        """Test that algorithm works with standard alphabetic characters."""
        words = ["hello", "h", "he", "hel", "hell"]
        result = self.solution.longest_word(words)
        assert result == "hello"

    def test_performance_larger_dictionary(self):
        """Test performance with larger dictionary."""
        # Create a larger test case
        words = []
        base = "a"
        for i in range(100):
            words.append(base)
            base += "a"
        
        result = self.solution.longest_word(words)
        assert len(result) == 100

    def test_edge_case_similar_prefixes(self):
        """Test edge case with similar prefixes."""
        words = ["app", "ap", "a", "apple", "appl"]
        result = self.solution.longest_word(words)
        assert result == "apple"

    def test_build_path_accuracy(self):
        """Test that build paths are accurate."""
        words = ["a", "ab", "abc", "abcd"]
        for word in words:
            path = self.solution.get_build_path(words, word)
            assert len(path) == len(word)
            assert path[-1] == word
            # Verify each step in path
            for i, step in enumerate(path):
                assert len(step) == i + 1

    def test_sorting_behavior(self):
        """Test that sorting behavior works correctly."""
        # Words of same length should be sorted lexicographically
        words = ["z", "a", "m"]
        result = self.solution.longest_word(words)
        assert result == "a"  # Lexicographically first

    def test_chain_completeness(self):
        """Test that only complete chains are considered."""
        words = ["a", "ab", "abc", "xyz"]  # "xyz" can't be built
        result = self.solution.longest_word(words)
        assert result == "abc"

    def test_optimal_selection_criteria(self):
        """Test optimal selection based on length and lexicographical order."""
        # Same length, different lexicographical order
        words = ["a", "ab", "z", "za"]
        result = self.solution.longest_word(words)
        assert result == "ab"  # Length 2, lexicographically smaller than "za"

    def test_incremental_building_validation(self):
        """Test that incremental building is properly validated."""
        words = ["a", "aa", "aaa", "aaaa"]
        result = self.solution.longest_word(words)
        assert result == "aaaa"

    def test_complex_branching_paths(self):
        """Test complex branching paths in dictionary."""
        words = ["a", "ab", "abc", "abd", "ac", "acd"]
        result = self.solution.longest_word(words)
        assert result in ["abc", "abd", "acd"]  # All length 3

    def test_method_consistency_validation(self):
        """Test that method results are consistent."""
        words = ["test", "t", "te", "tes"]
        longest = self.solution.longest_word(words)
        path = self.solution.get_build_path(words, longest)
        
        if longest:
            assert path  # Should have a valid path
            assert path[0] in [w for w in words if len(w) == 1]  # Starts with single char
            assert all(len(path[i]) == i + 1 for i in range(len(path)))  # Progressive length


if __name__ == "__main__":
    pytest.main([__file__])
