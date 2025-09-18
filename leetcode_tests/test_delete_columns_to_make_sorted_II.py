"""
Test suite for LeetCode #955: Delete Columns to Make Sorted II
"""

import pytest
import time

from leetcode.delete_columns_to_make_sorted_II import Solution


class TestDeleteColumnsToMakeSortedII:
    """Comprehensive test suite for Delete Columns to Make Sorted II problem."""
    
    def setup_method(self):
        """Set up test fixtures before each test method."""
        self.solution = Solution()
    
    # LeetCode Examples
    def test_example_1_leetcode(self):
        """Test LeetCode Example 1: ["ca","bb","ac"] -> 1"""
        strs = ["ca", "bb", "ac"]
        expected = 1
        result = self.solution.minDeletionSize(strs)
        assert result == expected, f"Expected {expected}, got {result}"
    
    def test_example_2_leetcode(self):
        """Test LeetCode Example 2: ["xc","yb","za"] -> 0"""
        strs = ["xc", "yb", "za"]
        expected = 0
        result = self.solution.minDeletionSize(strs)
        assert result == expected, f"Expected {expected}, got {result}"
    
    def test_example_3_leetcode(self):
        """Test LeetCode Example 3: ["zyx","wvu","tsr"] -> 3"""
        strs = ["zyx", "wvu", "tsr"]
        expected = 3
        result = self.solution.minDeletionSize(strs)
        assert result == expected, f"Expected {expected}, got {result}"
    
    # Edge Cases
    def test_single_string(self):
        """Test with single string."""
        strs = ["abc"]
        expected = 0
        result = self.solution.minDeletionSize(strs)
        assert result == expected, f"Expected {expected}, got {result}"
    
    def test_single_character_strings(self):
        """Test with single character strings."""
        strs = ["a", "b", "c"]
        expected = 0
        result = self.solution.minDeletionSize(strs)
        assert result == expected, f"Expected {expected}, got {result}"
    
    def test_reverse_order_single_chars(self):
        """Test with reverse order single character strings."""
        strs = ["c", "b", "a"]
        expected = 1
        result = self.solution.minDeletionSize(strs)
        assert result == expected, f"Expected {expected}, got {result}"
    
    def test_two_strings_already_sorted(self):
        """Test with two strings already in order."""
        strs = ["abc", "def"]
        expected = 0
        result = self.solution.minDeletionSize(strs)
        assert result == expected, f"Expected {expected}, got {result}"
    
    def test_two_strings_need_all_deleted(self):
        """Test where all columns need deletion."""
        strs = ["zyx", "abc"]
        expected = 3
        result = self.solution.minDeletionSize(strs)
        assert result == expected, f"Expected {expected}, got {result}"
    
    def test_identical_strings(self):
        """Test with identical strings."""
        strs = ["abc", "abc", "abc"]
        expected = 0
        result = self.solution.minDeletionSize(strs)
        assert result == expected, f"Expected {expected}, got {result}"
    
    # Complex Cases
    def test_partial_sorting_achieved(self):
        """Test case where partial sorting is achieved."""
        strs = ["ab", "ba"]
        expected = 0  # Already lexicographically sorted: "ab" < "ba"
        result = self.solution.minDeletionSize(strs)
        assert result == expected, f"Expected {expected}, got {result}"
    
    def test_multiple_strings_complex(self):
        """Test with multiple strings requiring careful analysis."""
        strs = ["abc", "bcd", "cde"]
        expected = 0  # Already sorted lexicographically
        result = self.solution.minDeletionSize(strs)
        assert result == expected, f"Expected {expected}, got {result}"
    
    def test_need_multiple_deletions(self):
        """Test case requiring multiple column deletions."""
        strs = ["dcba", "cbad", "abcd"]
        expected = 3  # Need to delete all columns for this case
        result = self.solution.minDeletionSize(strs)
        assert result == expected, f"Expected {expected}, got {result}"
    
    def test_mixed_sorting_requirements(self):
        """Test with mixed sorting requirements."""
        strs = ["ac", "bb", "ca"]
        expected = 0  # Already lexicographically sorted: "ac" < "bb" < "ca"
        result = self.solution.minDeletionSize(strs)
        assert result == expected, f"Expected {expected}, got {result}"
    
    def test_early_termination_case(self):
        """Test case where sorting is achieved early."""
        strs = ["ab", "cd"]
        expected = 0  # First column already establishes order
        result = self.solution.minDeletionSize(strs)
        assert result == expected, f"Expected {expected}, got {result}"
    
    def test_longer_strings(self):
        """Test with longer strings."""
        strs = ["abcdef", "bcdefg", "cdefgh"]
        expected = 0  # Already sorted
        result = self.solution.minDeletionSize(strs)
        assert result == expected, f"Expected {expected}, got {result}"
    
    def test_reverse_sorted_longer(self):
        """Test with longer strings in reverse order."""
        strs = ["fedcba", "edcbaf", "dcbafg"]  # Equal length strings
        expected = 5  # Need to delete 5 columns
        result = self.solution.minDeletionSize(strs)
        assert result == expected, f"Expected {expected}, got {result}"
    
    # Boundary Cases
    def test_minimum_input_size(self):
        """Test with minimum valid input."""
        strs = ["a", "b"]
        expected = 0
        result = self.solution.minDeletionSize(strs)
        assert result == expected, f"Expected {expected}, got {result}"
    
    def test_all_same_characters(self):
        """Test with all same characters."""
        strs = ["aaa", "aaa", "aaa"]
        expected = 0
        result = self.solution.minDeletionSize(strs)
        assert result == expected, f"Expected {expected}, got {result}"
    
    def test_alternating_pattern(self):
        """Test with alternating pattern."""
        strs = ["abab", "baba"]
        expected = 0  # Already lexicographically sorted: "abab" < "baba"
        result = self.solution.minDeletionSize(strs)
        assert result == expected, f"Expected {expected}, got {result}"
    
    # Performance Tests
    def test_performance_large_input(self):
        """Test performance with larger input."""
        # Create test case with many strings
        n_strings = 100
        string_length = 10
        strs = []
        for i in range(n_strings):
            # Create strings that are already sorted
            s = ''.join(chr(ord('a') + (i + j) % 26) for j in range(string_length))
            strs.append(s)
        
        start_time = time.time()
        result = self.solution.minDeletionSize(strs)
        end_time = time.time()
        
        execution_time = end_time - start_time
        assert execution_time < 1.0, f"Performance test failed: {execution_time:.3f}s"
        assert isinstance(result, int), "Result should be integer"
        assert result >= 0, "Result should be non-negative"
    
    def test_performance_worst_case(self):
        """Test performance with worst-case scenario."""
        # All strings in reverse order
        strs = []
        for i in range(50):
            s = ''.join(chr(ord('z') - j) for j in range(i, i + 5))
            strs.append(s)
        
        start_time = time.time()
        result = self.solution.minDeletionSize(strs)
        end_time = time.time()
        
        execution_time = end_time - start_time
        assert execution_time < 1.0, f"Performance test failed: {execution_time:.3f}s"
        assert isinstance(result, int), "Result should be integer"
    
    # Validation Tests
    def test_return_type(self):
        """Test that function returns correct type."""
        strs = ["abc", "def"]
        result = self.solution.minDeletionSize(strs)
        assert isinstance(result, int), f"Expected int, got {type(result)}"
    
    def test_non_negative_result(self):
        """Test that result is always non-negative."""
        test_cases = [
            ["a"],
            ["ab", "cd"],
            ["abc", "def", "ghi"],
            ["zyx", "wvu", "tsr"]
        ]
        
        for strs in test_cases:
            result = self.solution.minDeletionSize(strs)
            assert result >= 0, f"Result should be non-negative, got {result} for {strs}"
    
    def test_max_deletions_bound(self):
        """Test that deletions don't exceed string length."""
        strs = ["zyx", "wvu", "tsr"]
        result = self.solution.minDeletionSize(strs)
        max_possible = len(strs[0])
        assert result <= max_possible, f"Result {result} exceeds max possible {max_possible}"
    
    # Algorithm Correctness Tests
    def test_greedy_optimality(self):
        """Test that greedy approach gives optimal result."""
        # Test case where greedy and optimal should match
        strs = ["ba", "ab"]
        result = self.solution.minDeletionSize(strs)
        # Only need to delete one column to make it sorted
        assert result == 1, f"Expected 1, got {result}"
    
    def test_sorted_flag_logic(self):
        """Test the sorted flag logic with specific case."""
        # Case where sorted flags help avoid unnecessary deletions
        strs = ["abc", "bcd"]
        result = self.solution.minDeletionSize(strs)
        assert result == 0, f"Expected 0, got {result}"
    
    def test_lexicographic_correctness(self):
        """Test lexicographic ordering correctness."""
        strs = ["apple", "banana", "cherry"]
        result = self.solution.minDeletionSize(strs)
        assert result == 0, f"Expected 0 for already sorted strings, got {result}"


if __name__ == "__main__":
    pytest.main([__file__])