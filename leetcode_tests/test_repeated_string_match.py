"""Test cases for LeetCode 686: Repeated String Match"""

import pytest

from leetcode.repeated_string_match import Solution


class TestRepeatedStringMatch:
    
    def setup_method(self):
        self.solution = Solution()
    
    def test_example_1(self):
        assert self.solution.repeatedStringMatch("abcd", "cdabcdab") == 3
    
    def test_example_2(self):
        assert self.solution.repeatedStringMatch("a", "aa") == 2
    
    def test_single_char_match(self):
        assert self.solution.repeatedStringMatch("a", "a") == 1
    
    def test_impossible_match(self):
        assert self.solution.repeatedStringMatch("abc", "wxyz") == -1
    
    def test_longer_string_a(self):
        assert self.solution.repeatedStringMatch("abcdef", "abc") == 1
    
    def test_exact_repetition(self):
        assert self.solution.repeatedStringMatch("abc", "abcabc") == 2
    
    def test_partial_at_start(self):
        assert self.solution.repeatedStringMatch("abc", "ab") == 1
    
    def test_partial_at_end(self):
        assert self.solution.repeatedStringMatch("abc", "bc") == 1
    
    def test_cross_boundary(self):
        assert self.solution.repeatedStringMatch("abc", "bca") == 2
    
    def test_cross_multiple_boundaries(self):
        assert self.solution.repeatedStringMatch("abc", "cabcab") == 3
    
    def test_single_char_multiple(self):
        assert self.solution.repeatedStringMatch("a", "aaaa") == 4
    
    def test_no_common_chars(self):
        assert self.solution.repeatedStringMatch("abc", "xyz") == -1
    
    def test_b_longer_than_a(self):
        assert self.solution.repeatedStringMatch("ab", "abab") == 2
    
    def test_b_much_longer_than_a(self):
        assert self.solution.repeatedStringMatch("a", "aaaaaaaaaa") == 10
    
    def test_complex_pattern(self):
        assert self.solution.repeatedStringMatch("abab", "ababab") == 2
    
    def test_edge_case_wrap_around(self):
        assert self.solution.repeatedStringMatch("abc", "cabca") == 3
    
    def test_impossible_different_chars(self):
        assert self.solution.repeatedStringMatch("ab", "cd") == -1
    
    def test_impossible_missing_char(self):
        assert self.solution.repeatedStringMatch("ab", "abc") == -1
    
    def test_b_is_empty(self):
        # Edge case: empty string b should return 1 (need at least one repetition)
        assert self.solution.repeatedStringMatch("abc", "") == 1
    
    def test_same_string(self):
        assert self.solution.repeatedStringMatch("hello", "hello") == 1
    
    def test_overlapping_pattern(self):
        assert self.solution.repeatedStringMatch("aaac", "aac") == 1
    
    def test_long_repetition_needed(self):
        assert self.solution.repeatedStringMatch("aa", "aaaaaaaaaaaa") == 6
    
    def test_minimal_repetition(self):
        assert self.solution.repeatedStringMatch("abcdef", "defabc") == 2
    
    def test_char_frequency_mismatch(self):
        # b has more of a character than a can provide
        assert self.solution.repeatedStringMatch("ab", "aaa") == -1
    
    def test_cyclic_pattern(self):
        assert self.solution.repeatedStringMatch("abc", "bcab") == 2
    
    def test_large_input(self):
        a = "abcdef" * 100
        b = "defabc"
        assert self.solution.repeatedStringMatch(a, b) == 1
    
    def test_property_impossible_cases(self):
        # Property test: if b contains chars not in a, result should be -1
        test_cases = [
            ("abc", "xyz"),
            ("ab", "cd"),
            ("hello", "world"),
            ("12", "34")
        ]
        
        for a, b in test_cases:
            result = self.solution.repeatedStringMatch(a, b)
            if not set(b).issubset(set(a)):
                assert result == -1
    
    def test_property_minimum_repetitions(self):
        # Property test: result should never be less than ceil(len(b)/len(a))
        from math import ceil
        
        test_cases = [
            ("abc", "abcabc"),
            ("ab", "abab"),
            ("a", "aaaa"),
            ("xyz", "xyzxyz")
        ]
        
        for a, b in test_cases:
            result = self.solution.repeatedStringMatch(a, b)
            if result != -1:
                min_reps = ceil(len(b) / len(a))
                assert result >= min_reps
    
    def test_property_maximum_repetitions(self):
        # Property test: result should never exceed ceil(len(b)/len(a)) + 1
        from math import ceil
        
        test_cases = [
            ("abc", "cabcab"),
            ("ab", "baba"),
            ("xyz", "yzxyz")
        ]
        
        for a, b in test_cases:
            result = self.solution.repeatedStringMatch(a, b)
            if result != -1:
                max_reps = ceil(len(b) / len(a)) + 1
                assert result <= max_reps


if __name__ == "__main__":
    pytest.main([__file__, "-v"])