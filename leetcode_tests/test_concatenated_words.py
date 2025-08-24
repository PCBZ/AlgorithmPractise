"""
Comprehensive test suite for LeetCode Problem #472: Concatenated Words

Tests the findAllConcatenatedWordsInADict method which finds all words
that can be formed by concatenating at least two shorter words from the input.
"""
import os
import sys
import time

# Add the parent directory to sys.path to import the solution
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from leetcode.concatenated_words import Solution


class TestConcatenatedWords:
    """Test class for concatenated words problem."""

    def setup_method(self):
        """Set up test fixtures before each test method."""
        self.solution = Solution()

    def test_example_case_1(self):
        """Test LeetCode example case."""
        words = ["cat", "cats", "catsdogcats", "dog", "dogcatsdog",
                 "hippopotamuses", "rat", "ratcatdogcat"]
        result = self.solution.findAllConcatenatedWordsInADict(words)
        expected = ["catsdogcats", "dogcatsdog", "ratcatdogcat"]
        
        # Sort both lists for comparison since order may vary
        assert sorted(result) == sorted(expected)

    def test_simple_concatenation(self):
        """Test simple two-word concatenation."""
        words = ["cat", "dog", "catdog"]
        result = self.solution.findAllConcatenatedWordsInADict(words)
        expected = ["catdog"]
        assert result == expected

    def test_no_concatenated_words(self):
        """Test when no concatenated words exist."""
        words = ["apple", "banana", "cherry"]
        result = self.solution.findAllConcatenatedWordsInADict(words)
        expected = []
        assert result == expected

    def test_empty_input(self):
        """Test with empty input list."""
        words = []
        result = self.solution.findAllConcatenatedWordsInADict(words)
        expected = []
        assert result == expected

    def test_single_word(self):
        """Test with single word input."""
        words = ["hello"]
        result = self.solution.findAllConcatenatedWordsInADict(words)
        expected = []
        assert result == expected

    def test_two_words_no_concatenation(self):
        """Test with two words that don't form concatenation."""
        words = ["hello", "world"]
        result = self.solution.findAllConcatenatedWordsInADict(words)
        expected = []
        assert result == expected

    def test_multiple_ways_to_concatenate(self):
        """Test word that can be formed in multiple ways."""
        words = ["a", "aa", "aaa", "aaaa"]
        result = self.solution.findAllConcatenatedWordsInADict(words)
        # "aa" = "a" + "a", "aaa" = "a" + "aa" or "aa" + "a", "aaaa" = "aa" + "aa" etc.
        expected = ["aa", "aaa", "aaaa"]
        assert sorted(result) == sorted(expected)

    def test_overlapping_words(self):
        """Test with overlapping word patterns."""
        words = ["cats", "dog", "sand", "and", "cat"]
        result = self.solution.findAllConcatenatedWordsInADict(words)
        # "sand" = "s" + "and" (but "s" not in words), "cats" can't be formed
        expected = []
        assert result == expected

    def test_longer_concatenations(self):
        """Test concatenations of more than two words."""
        words = ["cat", "cats", "dog", "catsdog"]
        result = self.solution.findAllConcatenatedWordsInADict(words)
        expected = ["catsdog"]  # "cats" + "dog"
        assert result == expected

    def test_self_reference_prevention(self):
        """Test that words don't use themselves in concatenation."""
        words = ["word", "wordword"]
        result = self.solution.findAllConcatenatedWordsInADict(words)
        expected = ["wordword"]  # "word" + "word"
        assert result == expected

    def test_prefix_and_suffix_combinations(self):
        """Test combinations with prefixes and suffixes."""
        words = ["tech", "lead", "techlead", "google", "leetcode"]
        result = self.solution.findAllConcatenatedWordsInADict(words)
        expected = ["techlead"]  # "tech" + "lead"
        assert result == expected

    def test_case_sensitivity(self):
        """Test case sensitivity in concatenations."""
        words = ["Cat", "dog", "catdog", "Catdog"]
        result = self.solution.findAllConcatenatedWordsInADict(words)
        expected = ["Catdog"]  # "Cat" + "dog" forms "Catdog"
        assert result == expected

    def test_duplicate_handling(self):
        """Test that duplicates in input are processed correctly."""
        words = ["a", "b", "ab", "ab"]  # Has duplicate "ab"
        result = self.solution.findAllConcatenatedWordsInADict(words)
        # Each "ab" in input gets processed independently
        assert "ab" in result
        assert result.count("ab") == 2  # Both instances are concatenated

    def test_single_character_words(self):
        """Test with single character words."""
        words = ["a", "b", "ab", "ba", "aba"]
        result = self.solution.findAllConcatenatedWordsInADict(words)
        expected = ["ab", "ba", "aba"]  # "aba" = "a" + "b" + "a" or "ab" + "a"
        assert sorted(result) == sorted(expected)

    def test_nested_concatenations(self):
        """Test concatenations where parts are also concatenated."""
        words = ["a", "b", "ab", "abc", "c"]
        result = self.solution.findAllConcatenatedWordsInADict(words)
        # "ab" = "a" + "b", "abc" = "ab" + "c" or "a" + "b" + "c"
        expected = ["ab", "abc"]
        assert sorted(result) == sorted(expected)

    def test_return_type_and_structure(self):
        """Test that return type is correct list of strings."""
        words = ["cat", "dog", "catdog"]
        result = self.solution.findAllConcatenatedWordsInADict(words)
        
        assert isinstance(result, list)
        for word in result:
            assert isinstance(word, str)
            assert word in words  # All results should be from original input

    def test_algorithm_correctness_validation(self):
        """Validate algorithm correctness by checking each result."""
        words = ["cat", "cats", "dog", "catsdog", "dogcat"]
        result = self.solution.findAllConcatenatedWordsInADict(words)
        word_set = set(words)
        
        for concatenated_word in result:
            # Verify each result can indeed be formed by concatenation
            assert self._can_be_concatenated(concatenated_word, word_set)

    def _can_be_concatenated(self, word: str, word_set: set) -> bool:
        """Helper method to verify if a word can be concatenated."""
        available_words = word_set - {word}  # Exclude the word itself
        
        def can_form(remaining: str, used_count: int) -> bool:
            if not remaining:
                return used_count >= 2  # Must use at least 2 words
            
            for i in range(1, len(remaining) + 1):
                prefix = remaining[:i]
                if prefix in available_words:
                    if can_form(remaining[i:], used_count + 1):
                        return True
            return False
        
        return can_form(word, 0)

    def test_edge_case_very_short_words(self):
        """Test edge cases with very short words."""
        words = ["", "a", "aa"]  # Include empty string
        # Filter out empty strings as they're typically not valid
        words = [w for w in words if w]
        result = self.solution.findAllConcatenatedWordsInADict(words)
        expected = ["aa"]  # "a" + "a"
        assert result == expected

    def test_large_input_performance(self):
        """Test algorithm performance with larger input."""
        # Create a larger test case
        words = [f"word{i}" for i in range(50)] + ["word0word1", "word2word3"]
        
        start_time = time.time()
        result = self.solution.findAllConcatenatedWordsInADict(words)
        end_time = time.time()
        
        # Should complete within reasonable time
        assert end_time - start_time < 2.0
        assert "word0word1" in result
        assert "word2word3" in result

    def test_minimum_two_words_requirement(self):
        """Test that concatenation requires at least two words."""
        words = ["a", "b", "c", "ab"]
        result = self.solution.findAllConcatenatedWordsInADict(words)
        # "ab" is formed by "a" + "b" (exactly 2 words)
        assert "ab" in result

    def test_word_order_independence(self):
        """Test that input order doesn't affect results."""
        words1 = ["cat", "dog", "catdog"]
        words2 = ["dog", "catdog", "cat"]
        
        result1 = self.solution.findAllConcatenatedWordsInADict(words1)
        result2 = self.solution.findAllConcatenatedWordsInADict(words2)
        
        assert sorted(result1) == sorted(result2)

    def test_complex_overlapping_patterns(self):
        """Test complex patterns with overlapping substrings."""
        words = ["leet", "code", "leetcode", "lee", "tc", "od", "e"]
        result = self.solution.findAllConcatenatedWordsInADict(words)
        # "leetcode" = "leet" + "code"
        assert "leetcode" in result

    def test_all_results_are_from_input(self):
        """Test that all results are words from the original input."""
        words = ["sun", "flower", "sunflower", "pot"]
        result = self.solution.findAllConcatenatedWordsInADict(words)
        
        for word in result:
            assert word in words

    def test_no_false_positives(self):
        """Test that non-concatenated words are not included."""
        words = ["hello", "world", "python", "code"]
        result = self.solution.findAllConcatenatedWordsInADict(words)
        # None of these can be formed by concatenating others
        assert result == []

    def test_concatenation_uniqueness(self):
        """Test output reflects input structure (including duplicates)."""
        words = ["a", "b", "ab", "ba"]  # No duplicates in input
        result = self.solution.findAllConcatenatedWordsInADict(words)
        
        # Should have no duplicates since input has no duplicates
        assert len(result) == len(set(result))

    def test_mathematical_properties(self):
        """Test mathematical properties of the solution."""
        words = ["cat", "dog", "rat", "catdog", "dograt"]
        result = self.solution.findAllConcatenatedWordsInADict(words)
        
        # Number of concatenated words should not exceed total input words
        assert len(result) <= len(words)
        
        # All results should be longer than shortest component word
        if result:
            min_component_len = min(len(w) for w in words if w not in result)
            for concat_word in result:
                assert len(concat_word) > min_component_len

    def test_algorithm_efficiency_bounds(self):
        """Test algorithm stays within expected time bounds."""
        words = ["test"] * 20 + ["testtest"]  # 20 identical words + 1 concatenation
        
        start_time = time.time()
        result = self.solution.findAllConcatenatedWordsInADict(words)
        execution_time = time.time() - start_time
        
        # Should be efficient for moderate input sizes
        assert execution_time < 1.0
        assert "testtest" in result

    def test_comprehensive_edge_cases(self):
        """Test comprehensive edge cases."""
        test_cases = [
            ([], []),  # Empty input
            (["a"], []),  # Single word
            (["a", "b"], []),  # Two words, no concatenation
            (["a", "b", "ab"], ["ab"]),  # Simple concatenation with both parts
            (["cat", "cats", "dog", "catsdog"], ["catsdog"]),  # Multiple words
        ]
        
        for words, expected in test_cases:
            result = self.solution.findAllConcatenatedWordsInADict(words)
            assert sorted(result) == sorted(expected), f"Failed for words={words}"

    def test_recursive_concatenation_validation(self):
        """Test that the algorithm handles recursive concatenation correctly."""
        words = ["a", "aa", "aaa", "aaaa", "aaaaa"]
        result = self.solution.findAllConcatenatedWordsInADict(words)
        
        # All except "a" should be concatenated
        expected = ["aa", "aaa", "aaaa", "aaaaa"]
        assert sorted(result) == sorted(expected)
        
        # Verify each can be formed by concatenation
        for word in result:
            assert self._can_be_concatenated(word, set(words))
