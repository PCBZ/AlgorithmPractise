"""Test cases for LeetCode 316: Remove Duplicate Letters"""

import pytest
from leetcode.remove_duplicate_letters import Solution


class TestRemoveDuplicateLetters:
    
    def setup_method(self):
        self.solution = Solution()
    
    def test_example_1(self):
        assert self.solution.removeDuplicateLetters("bcabc") == "abc"
    
    def test_example_2(self):
        assert self.solution.removeDuplicateLetters("cbacdcbc") == "acdb"
    
    def test_single_character(self):
        assert self.solution.removeDuplicateLetters("a") == "a"
    
    def test_no_duplicates(self):
        assert self.solution.removeDuplicateLetters("abcdef") == "abcdef"
    
    def test_all_same_character(self):
        assert self.solution.removeDuplicateLetters("aaaa") == "a"
    
    def test_reverse_order(self):
        assert self.solution.removeDuplicateLetters("dcba") == "dcba"
    
    def test_alternating_pattern(self):
        assert self.solution.removeDuplicateLetters("abab") == "ab"
    
    def test_complex_pattern(self):
        assert self.solution.removeDuplicateLetters("bddbccd") == "bcd"
    
    def test_nested_duplicates(self):
        assert self.solution.removeDuplicateLetters("ecbacba") == "eacb"
    
    def test_long_string(self):
        assert self.solution.removeDuplicateLetters("abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz") == "abcdefghijklmnopqrstuvwxyz"
    
    def test_descending_with_duplicates(self):
        # When chars repeat, we can get lexicographically smallest
        assert self.solution.removeDuplicateLetters("dcbadcba") == "adcb"
    
    def test_mixed_case_pattern(self):
        assert self.solution.removeDuplicateLetters("cabacabac") == "abc"
    
    def test_early_large_char(self):
        assert self.solution.removeDuplicateLetters("zabcza") == "abcz"
    
    def test_late_small_char(self):
        assert self.solution.removeDuplicateLetters("bcabca") == "abc"
    
    def test_repeated_subsequence(self):
        assert self.solution.removeDuplicateLetters("abcabcabc") == "abc"
    
    def test_interwoven_pattern(self):
        assert self.solution.removeDuplicateLetters("dacefedbcf") == "acedbf"
    
    def test_two_characters(self):
        assert self.solution.removeDuplicateLetters("ab") == "ab"
        assert self.solution.removeDuplicateLetters("ba") == "ba"
    
    def test_three_characters_all_unique(self):
        assert self.solution.removeDuplicateLetters("abc") == "abc"
        assert self.solution.removeDuplicateLetters("acb") == "acb"
        assert self.solution.removeDuplicateLetters("bac") == "bac"
        assert self.solution.removeDuplicateLetters("bca") == "bca"
        assert self.solution.removeDuplicateLetters("cab") == "cab"
        assert self.solution.removeDuplicateLetters("cba") == "cba"
    
    def test_edge_case_pattern(self):
        assert self.solution.removeDuplicateLetters("babc") == "abc"
    
    def test_property_unique_characters(self):
        test_cases = [
            "bcabc", "cbacdcbc", "abcdef", "aaaa", "dcba"
        ]
        for s in test_cases:
            result = self.solution.removeDuplicateLetters(s)
            assert len(result) == len(set(result))
    
    def test_property_contains_all_unique_chars(self):
        test_cases = [
            "bcabc", "cbacdcbc", "abcdef", "aaaa", "dcba"
        ]
        for s in test_cases:
            result = self.solution.removeDuplicateLetters(s)
            unique_chars = set(s)
            assert set(result) == unique_chars
    
    def test_property_lexicographically_smallest(self):
        s = "bcabc"
        result = self.solution.removeDuplicateLetters(s)
        assert result == "abc"
        
        s = "cbacdcbc"
        result = self.solution.removeDuplicateLetters(s)
        assert result == "acdb"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])