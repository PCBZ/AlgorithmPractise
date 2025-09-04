"""Tests for LeetCode #491: Non-decreasing Subsequences."""

import pytest
from leetcode.non_descending_subarray import Solution


class TestNonDescendingSubsequences:
    """Test class for Non-decreasing Subsequences problem."""

    def setup_method(self):
        """Set up test fixtures before each test method."""
        self.solution = Solution()

    @pytest.mark.parametrize(
        "nums,expected",
        [
            # Basic test cases
            ([4, 6, 7, 7], [[4, 6], [4, 6, 7], [4, 6, 7, 7], [4, 7], [4, 7, 7], [6, 7], [6, 7, 7], [7, 7]]),
            ([4, 4, 3, 2, 1], [[4, 4]]),
            ([1, 2, 3, 4], [[1, 2], [1, 2, 3], [1, 2, 3, 4], [1, 2, 4], [1, 3], [1, 3, 4], [1, 4], [2, 3], [2, 3, 4], [2, 4], [3, 4]]),
            
            # Single element (no valid subsequences)
            ([1], []),
            ([5], []),
            
            # Two elements
            ([1, 2], [[1, 2]]),
            ([2, 1], []),
            ([3, 3], [[3, 3]]),
            
            # All same elements
            ([2, 2, 2], [[2, 2], [2, 2, 2]]),
            ([5, 5, 5, 5], [[5, 5], [5, 5, 5], [5, 5, 5, 5]]),
            
            # Strictly decreasing (only duplicates work)
            ([5, 4, 3, 2, 1], []),
            ([6, 5, 4, 4, 3], [[4, 4]]),
            
            # Mixed patterns
            ([1, 3, 2, 4], [[1, 3], [1, 3, 4], [1, 2], [1, 2, 4], [1, 4], [2, 4], [3, 4]]),
            ([10, 9, 2, 5, 3, 7, 101, 18], [[2, 3], [2, 3, 7], [2, 3, 7, 18], [2, 3, 7, 101], [2, 3, 18], [2, 3, 101], [2, 5], [2, 5, 7], [2, 5, 7, 18], [2, 5, 7, 101], [2, 5, 18], [2, 5, 101], [2, 7], [2, 7, 18], [2, 7, 101], [2, 18], [2, 101], [3, 7], [3, 7, 18], [3, 7, 101], [3, 18], [3, 101], [5, 7], [5, 7, 18], [5, 7, 101], [5, 18], [5, 101], [7, 18], [7, 101], [9, 18], [9, 101], [10, 18], [10, 101]]),
        ]
    )
    def test_find_non_decreasing_subsequences(self, nums, expected):
        """Test find_non_decreasing_subsequences with various inputs."""
        result = self.solution.find_non_decreasing_subsequences(nums)
        # Sort both result and expected for comparison since order may vary
        result_sorted = [sorted(seq) for seq in sorted(result)]
        expected_sorted = [sorted(seq) for seq in sorted(expected)]
        assert result_sorted == expected_sorted
        assert len(result) == len(expected)

    def test_empty_array(self):
        """Test with empty array."""
        assert self.solution.find_non_decreasing_subsequences([]) == []

    def test_negative_numbers(self):
        """Test with negative numbers."""
        result = self.solution.find_non_decreasing_subsequences([-1, 0, 1])
        expected = [[-1, 0], [-1, 0, 1], [-1, 1], [0, 1]]
        result_sorted = [sorted(seq) for seq in sorted(result)]
        expected_sorted = [sorted(seq) for seq in sorted(expected)]
        assert result_sorted == expected_sorted

    def test_duplicates_at_different_positions(self):
        """Test duplicates at different positions."""
        result = self.solution.find_non_decreasing_subsequences([1, 2, 1, 2])
        # Expected: all valid non-decreasing subsequences
        expected_count = len(result)
        # Check that we have valid subsequences
        assert expected_count > 0
        
        # Verify all subsequences are non-decreasing and length >= 2
        for seq in result:
            assert len(seq) >= 2
            for i in range(1, len(seq)):
                assert seq[i-1] <= seq[i]

    def test_large_duplicates(self):
        """Test with many duplicates."""
        nums = [1, 1, 1, 1, 1]
        result = self.solution.find_non_decreasing_subsequences(nums)
        
        # Should have subsequences of lengths 2, 3, 4, 5
        # For n identical elements, we get 1 subsequence each of length 2,3,...,n
        expected_lengths = [2, 3, 4, 5]
        assert len(result) == 4
        
        for i, seq in enumerate(result):
            assert len(seq) == expected_lengths[i]
            assert all(x == 1 for x in seq)

    def test_no_valid_subsequences(self):
        """Test cases with no valid subsequences."""
        # Single element
        assert self.solution.find_non_decreasing_subsequences([42]) == []
        
        # Strictly decreasing
        assert self.solution.find_non_decreasing_subsequences([5, 4, 3, 2, 1]) == []
        assert self.solution.find_non_decreasing_subsequences([10, 5, 1]) == []

    def test_boundary_values(self):
        """Test with boundary values."""
        # Minimum and maximum integers
        result = self.solution.find_non_decreasing_subsequences([-100, 0, 100])
        expected = [[-100, 0], [-100, 0, 100], [-100, 100], [0, 100]]
        result_sorted = [sorted(seq) for seq in sorted(result)]
        expected_sorted = [sorted(seq) for seq in sorted(expected)]
        assert result_sorted == expected_sorted

    def test_long_sequence(self):
        """Test with longer sequence."""
        nums = [1, 2, 3, 4, 5]
        result = self.solution.find_non_decreasing_subsequences(nums)
        
        # Should have many subsequences
        assert len(result) > 10
        
        # All should be non-decreasing and length >= 2
        for seq in result:
            assert len(seq) >= 2
            for i in range(1, len(seq)):
                assert seq[i-1] <= seq[i]

    def test_alternating_pattern(self):
        """Test with alternating up/down pattern."""
        nums = [1, 3, 2, 4, 3, 5]
        result = self.solution.find_non_decreasing_subsequences(nums)
        
        # Should find valid subsequences like [1,3], [1,2,4], [2,4,5], etc.
        assert len(result) > 0
        
        # Verify all are valid
        for seq in result:
            assert len(seq) >= 2
            for i in range(1, len(seq)):
                assert seq[i-1] <= seq[i]

    def test_duplicate_handling(self):
        """Test that duplicates are handled correctly."""
        nums = [4, 6, 7, 7]
        result = self.solution.find_non_decreasing_subsequences(nums)
        
        # Should not have duplicate subsequences
        result_set = set(tuple(seq) for seq in result)
        assert len(result) == len(result_set)

    def test_performance_case(self):
        """Test with larger input to check performance."""
        # Create a case that could generate many subsequences
        nums = list(range(10))  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        result = self.solution.find_non_decreasing_subsequences(nums)
        
        # Should generate 2^10 - 10 - 1 = 1013 subsequences
        # (all subsets minus single element subsets minus empty set)
        expected_count = 2**10 - 10 - 1
        assert len(result) == expected_count


if __name__ == "__main__":
    pytest.main([__file__])
