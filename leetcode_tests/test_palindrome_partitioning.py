"""
Test cases for LeetCode 131. Palindrome Partitioning

Tests the backtracking solution for finding all palindrome partitions.
Covers various string patterns, edge cases, and performance scenarios.
"""

import pytest
from typing import List
import sys
import os

# Add the parent directory to sys.path to import from leetcode module
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from leetcode.palindrome_partitioning import Solution


class TestPalindromePartitioning:
    """Test cases for Palindrome Partitioning solution."""
    
    def setup_method(self):
        """Set up test fixtures before each test method."""
        self.solution = Solution()
    
    def normalize_result(self, result: List[List[str]]) -> List[List[str]]:
        """Normalize result by sorting for consistent comparison."""
        return sorted([sorted(partition) for partition in result])
    
    def test_example_case_1(self):
        """Test the first example from problem description."""
        s = "aab"
        expected = [["a", "a", "b"], ["aa", "b"]]
        result = self.solution.partition(s)
        # Check all expected partitions are present
        for partition in expected:
            assert partition in result
        assert len(result) == len(expected)
    
    def test_example_case_2(self):
        """Test case with limited palindromes."""
        s = "raceacar"
        result = self.solution.partition(s)
        # Only valid partitions based on actual palindromes: r,a,c,e,a,aca,r
        expected = [
            ["r", "a", "c", "e", "a", "c", "a", "r"],
            ["r", "a", "c", "e", "aca", "r"]
        ]
        assert len(result) == 2
        for partition in expected:
            assert partition in result
    
    def test_single_character(self):
        """Test single character string."""
        s = "a"
        expected = [["a"]]
        result = self.solution.partition(s)
        assert result == expected
    
    def test_empty_string(self):
        """Test empty string."""
        s = ""
        expected = [[]]
        result = self.solution.partition(s)
        assert result == expected
    
    def test_all_same_characters(self):
        """Test string with all same characters."""
        s = "aaa"
        result = self.solution.partition(s)
        expected_partitions = [
            ["a", "a", "a"],
            ["a", "aa"],
            ["aa", "a"],
            ["aaa"]
        ]
        assert len(result) == 4
        for partition in expected_partitions:
            assert partition in result
    
    def test_no_palindromes_except_single(self):
        """Test string where only single characters are palindromes."""
        s = "abcd"
        result = self.solution.partition(s)
        expected = [["a", "b", "c", "d"]]
        assert result == expected
    
    def test_entire_string_palindrome(self):
        """Test where entire string is a palindrome."""
        s = "abcba"
        result = self.solution.partition(s)
        # Should include the whole string as one partition
        assert ["abcba"] in result
        # Should also include character-by-character partition
        assert ["a", "b", "c", "b", "a"] in result
        # Should have multiple valid partitions
        assert len(result) > 2
    
    def test_multiple_palindromes(self):
        """Test string with multiple palindromes of different lengths."""
        s = "aba"
        result = self.solution.partition(s)
        expected = [
            ["a", "b", "a"],
            ["aba"]
        ]
        assert len(result) == 2
        for partition in expected:
            assert partition in result
    
    def test_overlapping_palindromes(self):
        """Test string with overlapping palindromes."""
        s = "abccba"
        result = self.solution.partition(s)
        # Should include whole string palindrome
        assert ["abccba"] in result
        # Should include other valid partitions
        assert ["a", "b", "cc", "b", "a"] in result
        assert len(result) >= 2
    
    def test_alternating_pattern(self):
        """Test alternating character pattern."""
        s = "abab"
        result = self.solution.partition(s)
        # Valid partitions include: single chars, "aba" + "b", "a" + "bab"
        expected = [
            ["a", "b", "a", "b"],
            ["a", "bab"],
            ["aba", "b"]
        ]
        assert len(result) == 3
        for partition in expected:
            assert partition in result
    
    def test_mirror_pattern(self):
        """Test mirror pattern string."""
        s = "abcba"
        result = self.solution.partition(s)
        # Check that full palindrome is included
        assert ["abcba"] in result
        # Check character-by-character partition
        assert ["a", "b", "c", "b", "a"] in result
        # Should have additional valid partitions
        assert len(result) >= 2
    
    def test_double_characters(self):
        """Test string with double characters."""
        s = "aabb"
        result = self.solution.partition(s)
        expected_partitions = [
            ["a", "a", "b", "b"],
            ["a", "a", "bb"],
            ["aa", "b", "b"],
            ["aa", "bb"]
        ]
        assert len(result) == 4
        for partition in expected_partitions:
            assert partition in result
    
    def test_complex_palindromes(self):
        """Test complex case with nested palindromes."""
        s = "abcbab"
        result = self.solution.partition(s)
        # Should find various valid partitions
        assert len(result) >= 1
        # Should include character-by-character
        assert ["a", "b", "c", "b", "a", "b"] in result
        # Should find palindromic substrings
        partitions_with_bcb = [p for p in result if "bcb" in p]
        assert len(partitions_with_bcb) >= 1
    
    def test_performance_medium_string(self):
        """Test performance with medium-length string."""
        s = "abcdefghijklmno"
        result = self.solution.partition(s)
        # Should only have single character partition since no palindromes
        expected = [list(s)]
        assert result == expected
    
    def test_palindromic_sequence(self):
        """Test sequence of palindromes."""
        s = "aabaa"
        result = self.solution.partition(s)
        # Should include various combinations
        assert ["aa", "b", "aa"] in result
        assert ["a", "aba", "a"] in result
        assert ["aabaa"] in result
        assert len(result) >= 3
    
    def test_edge_case_two_chars_same(self):
        """Test two identical characters."""
        s = "bb"
        result = self.solution.partition(s)
        expected = [
            ["b", "b"],
            ["bb"]
        ]
        assert len(result) == 2
        for partition in expected:
            assert partition in result
    
    def test_edge_case_two_chars_different(self):
        """Test two different characters."""
        s = "ab"
        result = self.solution.partition(s)
        expected = [["a", "b"]]
        assert result == expected
    
    @pytest.mark.parametrize("s,min_partitions", [
        ("a", 1),
        ("aa", 2), 
        ("aba", 2),
        ("aaa", 4),
        ("abcd", 1),
        ("abcba", 3)
    ])
    def test_partition_count(self, s: str, min_partitions: int):
        """Test that minimum expected number of partitions are found."""
        result = self.solution.partition(s)
        assert len(result) >= min_partitions
    
    def test_all_partitions_valid(self):
        """Test that all returned partitions are valid."""
        test_strings = ["aab", "aba", "abccba", "aaa", "abcd"]
        
        for s in test_strings:
            result = self.solution.partition(s)
            
            for partition in result:
                # Check partition reconstructs original string
                assert "".join(partition) == s
                
                # Check each substring in partition is palindrome
                for substring in partition:
                    assert substring == substring[::-1], f"'{substring}' is not palindrome"
    
    def test_no_duplicate_partitions(self):
        """Test that no duplicate partitions are returned."""
        test_strings = ["aab", "aba", "aaa", "abccba"]
        
        for s in test_strings:
            result = self.solution.partition(s)
            
            # Convert to tuples for hashability and check uniqueness
            result_tuples = [tuple(partition) for partition in result]
            assert len(result_tuples) == len(set(result_tuples))
    
    def test_comprehensive_palindrome_validation(self):
        """Comprehensive test for palindrome validation in results."""
        s = "raceacar"
        result = self.solution.partition(s)
        
        # Validate each partition
        for partition in result:
            reconstructed = "".join(partition)
            assert reconstructed == s, f"Partition {partition} doesn't reconstruct '{s}'"
            
            # Validate each substring is palindrome
            for substring in partition:
                assert substring == substring[::-1], f"'{substring}' is not palindrome"
        
        # Should have exactly 2 valid partitions for this string
        assert len(result) == 2
    
    def test_stress_palindrome_heavy(self):
        """Stress test with palindrome-heavy string."""
        s = "aabaacaabaa"
        result = self.solution.partition(s)
        
        # Should have many valid partitions due to palindromes
        assert len(result) >= 10
        
        # Verify all are valid
        for partition in result:
            assert "".join(partition) == s
            for substring in partition:
                assert substring == substring[::-1]


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
