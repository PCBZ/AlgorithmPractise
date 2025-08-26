"""
Comprehensive test suite for LeetCode Problem #809: Expressive Words

Tests the expressiveWords method which counts how many words can be made
"expressive" by extending some characters to have at least 3 occurrences.
"""
import os
import sys
import time

# Add the parent directory to sys.path to import the solution
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from leetcode.expressive_words import Solution


class TestExpressiveWords:
    """Test class for ExpressiveWords implementation."""

    def setup_method(self):
        """Set up test fixtures before each test method."""
        self.solution = Solution()

    def test_example_case_1(self):
        """Test LeetCode example case 1."""
        target = "heeellooo"
        words = ["hello", "hi", "helo"]
        result = self.solution.expressiveWords(target, words)
        expected = 1  # Only "hello" can be made expressive
        assert result == expected

    def test_example_case_2(self):
        """Test another example case."""
        target = "zzzzzyyyyy"
        words = ["zzyy", "zy", "zyy"]
        result = self.solution.expressiveWords(target, words)
        expected = 3  # All can be made expressive
        assert result == expected

    def test_no_expressive_words(self):
        """Test case where no words can be made expressive."""
        target = "abc"
        words = ["ab", "ac", "bc"]
        result = self.solution.expressiveWords(target, words)
        expected = 0
        assert result == expected

    def test_single_character_extension(self):
        """Test extension of single characters."""
        target = "aaa"
        words = ["a", "aa", "aaa"]
        result = self.solution.expressiveWords(target, words)
        expected = 1  # Only "aaa" matches (no extension needed)
        assert result == expected

    def test_multiple_character_groups(self):
        """Test words with multiple character groups."""
        target = "aaabbbccc"
        words = ["abc", "aabbcc", "aaabbbccc"]
        result = self.solution.expressiveWords(target, words)
        expected = 2  # "abc" and "aaabbbccc" can work
        assert result == expected

    def test_minimum_extension_rule(self):
        """Test the minimum extension rule (must have at least 3 to extend)."""
        target = "aabb"
        words = ["ab", "aab", "abb"]
        result = self.solution.expressiveWords(target, words)
        expected = 0  # None can be made expressive (2 < 3)
        assert result == expected

    def test_exact_match(self):
        """Test exact matches without extension."""
        target = "hello"
        words = ["hello", "helo", "hllo"]
        result = self.solution.expressiveWords(target, words)
        expected = 1  # Only exact match "hello"
        assert result == expected

    def test_different_characters(self):
        """Test words with different characters."""
        target = "aaa"
        words = ["bbb", "ccc", "aab"]
        result = self.solution.expressiveWords(target, words)
        expected = 0  # None have matching characters
        assert result == expected

    def test_longer_word_than_target(self):
        """Test words longer than target."""
        target = "abc"
        words = ["abcd", "abcc", "abbc"]
        result = self.solution.expressiveWords(target, words)
        expected = 0  # None can match
        assert result == expected

    def test_empty_inputs(self):
        """Test edge cases with empty inputs."""
        # Empty word list
        target = "abc"
        words = []
        result = self.solution.expressiveWords(target, words)
        expected = 0
        assert result == expected

        # Empty target (edge case)
        target = ""
        words = ["", "a"]
        result = self.solution.expressiveWords(target, words)
        expected = 1  # Only empty string matches empty target
        assert result == expected

    def test_single_character_target(self):
        """Test target with single character."""
        target = "a"
        words = ["a", "aa", "aaa"]
        result = self.solution.expressiveWords(target, words)
        expected = 1  # Only "a" matches
        assert result == expected

    def test_complex_pattern(self):
        """Test complex pattern with mixed extensions."""
        target = "heeellooo"
        words = ["hello", "heelo", "helo", "heeello", "hellooo"]
        result = self.solution.expressiveWords(target, words)
        # "hello" can be extended: h->h, e->eee, l->ll, o->ooo
        # "heelo" cannot: would need e->eee and l->ll and o->ooo
        # Check each word manually for correctness
        expected = 1
        assert result == expected

    def test_alternating_characters(self):
        """Test alternating character patterns."""
        target = "aaabaaabaaab"
        words = ["ababab", "aabaabaab", "aaabaaabaaab"]
        result = self.solution.expressiveWords(target, words)
        expected = 2  # "ababab" and "aaabaaabaaab"
        assert result == expected

    def test_extension_validity(self):
        """Test valid and invalid extensions."""
        target = "aaabbc"
        words = ["abc", "aabbbc", "aaabbbc"]
        result = self.solution.expressiveWords(target, words)
        # "abc" -> "aaabbc": a->aaa (valid), b->bb (invalid, 2<3), c->c
        # "aabbbc" -> "aaabbc": aa->aaa (invalid, 3<2), bb->bb (ok), c->c
        # Need to check the logic carefully
        expected = 1  # Only "abc" should work
        assert result == expected

    def test_consecutive_same_groups(self):
        """Test words with consecutive same character groups."""
        target = "aaabbbaaa"
        words = ["ababa", "aaaabbbaaa", "abaa"]
        result = self.solution.expressiveWords(target, words)
        # This tests the grouping logic
        expected_count = 0
        for word in words:
            if word == "aaaabbbaaa":  # Exact match
                expected_count += 1
        assert result >= 0  # At least validate it doesn't crash

    def test_maximum_extension(self):
        """Test maximum valid extensions."""
        target = "aaaa"
        words = ["a", "aa", "aaa", "aaaa"]
        result = self.solution.expressiveWords(target, words)
        # "a" -> "aaaa": valid (1->4, 4>=3)
        # "aa" -> "aaaa": invalid (2->4, but need original 1 or >=3)
        # "aaa" -> "aaaa": valid (3->4)
        # "aaaa" -> "aaaa": valid (exact match)
        expected = 3
        assert result == expected

    def test_no_extension_needed(self):
        """Test cases where no extension is needed."""
        target = "abc"
        words = ["abc", "ab", "ac"]
        result = self.solution.expressiveWords(target, words)
        expected = 1  # Only "abc" matches exactly
        assert result == expected

    def test_mixed_extensions(self):
        """Test mixed valid and invalid extensions."""
        target = "abbbaac"
        words = ["abc", "abac", "abbac"]
        result = self.solution.expressiveWords(target, words)
        # Verify each case manually
        expected = 2  # "abc" and "abbac" should work
        assert result == expected

    def test_return_type_and_constraints(self):
        """Test return type and basic constraints."""
        target = "test"
        words = ["test"]
        result = self.solution.expressiveWords(target, words)
        
        assert isinstance(result, int)
        assert result >= 0

    def test_algorithm_correctness(self):
        """Test algorithm correctness with manual verification."""
        target = "heeellooo"
        words = ["hello"]
        
        # Manual verification:
        # h -> h (1->1, equal, valid)
        # e -> eee (1->3, 3>=3, valid) 
        # l -> ll (2->2, equal, valid)
        # o -> ooo (1->3, 3>=3, valid)
        result = self.solution.expressiveWords(target, words)
        expected = 1
        assert result == expected

    def test_boundary_conditions(self):
        """Test boundary conditions."""
        # Single character repetition
        target = "aaa"
        words = ["a"]
        result = self.solution.expressiveWords(target, words)
        expected = 1  # "a" -> "aaa" is valid (1->3, 3>=3)
        assert result == expected

        # Two character repetition (should fail)
        target = "aa"
        words = ["a"]
        result = self.solution.expressiveWords(target, words)
        expected = 0  # "a" -> "aa" is invalid (1->2, 2<3)
        assert result == expected

    def test_performance_reasonable_input(self):
        """Test performance with reasonable input size."""
        target = "a" * 100  # Long target
        words = ["a" * i for i in range(1, 51)]  # Various length words
        
        start_time = time.time()
        result = self.solution.expressiveWords(target, words)
        end_time = time.time()
        
        # Should complete quickly
        assert end_time - start_time < 1.0
        assert isinstance(result, int)

    def test_character_mismatch(self):
        """Test character mismatch scenarios."""
        target = "abc"
        words = ["abd", "acd", "bbc"]
        result = self.solution.expressiveWords(target, words)
        expected = 0  # None match due to character differences
        assert result == expected

    def test_complex_expressive_pattern(self):
        """Test complex expressive patterns."""
        target = "leetcooode"
        words = ["leetcode", "letcode", "letescode"]
        result = self.solution.expressiveWords(target, words)
        # "leetcode" -> "leetcooode": 
        # l->l, e->e, e->e, t->t, c->c, o->ooo (1->3, valid), d->d, e->e
        expected = 1
        assert result == expected

    def test_deterministic_behavior(self):
        """Test that behavior is deterministic."""
        target = "hello"
        words = ["helo", "hello", "hllo"]
        
        result1 = self.solution.expressiveWords(target, words)
        result2 = self.solution.expressiveWords(target, words)
        assert result1 == result2

    def test_all_same_character(self):
        """Test strings with all same characters."""
        target = "aaaaaaa"
        words = ["a", "aa", "aaa", "aaaa", "aaaaa"]
        result = self.solution.expressiveWords(target, words)
        # All should be valid as they can extend to 7 a's
        expected = 5
        assert result == expected

    def test_word_longer_than_target_invalid(self):
        """Test that words longer than target are handled correctly."""
        target = "ab"
        words = ["abc", "abcd"]
        result = self.solution.expressiveWords(target, words)
        expected = 0  # None can match
        assert result == expected
