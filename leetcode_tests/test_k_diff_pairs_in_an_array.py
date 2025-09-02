"""
Comprehensive test suite for LeetCode Problem #532: K-diff Pairs in an Array
Tests the hash-based algorithm for finding unique k-diff pairs.
"""

import pytest

from leetcode.k_diff_pairs_in_an_array import Solution


class TestKDiffPairs:
    """Test cases for K-diff Pairs in an Array problem."""

    def setup_method(self):
        """Set up test fixtures before each test method."""
        self.solution = Solution()

    def test_basic_example_1(self):
        """Test first basic example from LeetCode."""
        nums = [3, 1, 4, 1, 5]
        k = 2
        expected = 2  # Pairs: (1,3) and (3,5)
        assert self.solution.findPairs(nums, k) == expected

    def test_basic_example_2(self):
        """Test second basic example from LeetCode."""
        nums = [1, 2, 3, 4, 5]
        k = 1
        expected = 4  # Pairs: (1,2), (2,3), (3,4), (4,5)
        assert self.solution.findPairs(nums, k) == expected

    def test_k_equals_zero(self):
        """Test case where k=0 (finding duplicates)."""
        nums = [1, 3, 1, 5, 4]
        k = 0
        expected = 1  # Only pair: (1,1)
        assert self.solution.findPairs(nums, k) == expected

    def test_multiple_duplicates_k_zero(self):
        """Test k=0 with multiple duplicate numbers."""
        nums = [1, 1, 1, 1, 1]
        k = 0
        expected = 1  # Only one unique pair: (1,1)
        assert self.solution.findPairs(nums, k) == expected

    def test_no_duplicates_k_zero(self):
        """Test k=0 with no duplicate numbers."""
        nums = [1, 2, 3, 4, 5]
        k = 0
        expected = 0  # No pairs with difference 0
        assert self.solution.findPairs(nums, k) == expected

    def test_negative_k(self):
        """Test case with negative k value."""
        nums = [1, 2, 3, 4, 5]
        k = -1
        expected = 0  # Negative k should return 0
        assert self.solution.findPairs(nums, k) == expected

    def test_empty_array(self):
        """Test with empty array."""
        nums = []
        k = 1
        expected = 0
        assert self.solution.findPairs(nums, k) == expected

    def test_single_element(self):
        """Test with single element array."""
        nums = [1]
        k = 1
        expected = 0  # Cannot form pairs with single element
        assert self.solution.findPairs(nums, k) == expected

    def test_two_elements_valid_pair(self):
        """Test with two elements forming valid pair."""
        nums = [1, 3]
        k = 2
        expected = 1  # Pair: (1,3)
        assert self.solution.findPairs(nums, k) == expected

    def test_two_elements_no_pair(self):
        """Test with two elements not forming valid pair."""
        nums = [1, 3]
        k = 1
        expected = 0  # No pair with difference 1
        assert self.solution.findPairs(nums, k) == expected

    def test_complex_example(self):
        """Test complex example with multiple duplicates."""
        nums = [1, 2, 4, 4, 3, 3, 0, 9, 2, 3]
        k = 3
        expected = 2  # Pairs: (0,3) and (6,9)
        assert self.solution.findPairs(nums, k) == expected

    def test_large_k_value(self):
        """Test with large k value."""
        nums = [1, 2, 3, 4, 5]
        k = 10
        expected = 0  # No pairs with difference 10
        assert self.solution.findPairs(nums, k) == expected

    def test_all_same_elements(self):
        """Test array with all same elements."""
        nums = [5, 5, 5, 5]
        k = 0
        expected = 1  # One unique pair: (5,5)
        assert self.solution.findPairs(nums, k) == expected

    def test_all_same_elements_k_positive(self):
        """Test array with all same elements and positive k."""
        nums = [5, 5, 5, 5]
        k = 1
        expected = 0  # No pairs with difference 1
        assert self.solution.findPairs(nums, k) == expected

    def test_negative_numbers(self):
        """Test with negative numbers."""
        nums = [-1, -2, -3, 1, 2, 3]
        k = 1
        expected = 4  # Pairs: (-3,-2), (-2,-1), (1,2), (2,3)
        assert self.solution.findPairs(nums, k) == expected

    def test_mixed_positive_negative(self):
        """Test with mix of positive and negative numbers."""
        nums = [-1, 0, 1, 2]
        k = 1
        expected = 3  # Pairs: (-1,0), (0,1), (1,2)
        assert self.solution.findPairs(nums, k) == expected

    def test_duplicate_elements_different_k(self):
        """Test duplicate elements with various k values."""
        nums = [1, 1, 2, 2, 3, 3]
        k = 1
        expected = 2  # Pairs: (1,2), (2,3)
        assert self.solution.findPairs(nums, k) == expected

    def test_consecutive_numbers(self):
        """Test with consecutive numbers."""
        nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        k = 1
        expected = 9  # Nine consecutive pairs
        assert self.solution.findPairs(nums, k) == expected

    def test_non_consecutive_gaps(self):
        """Test with non-consecutive numbers."""
        nums = [1, 3, 5, 7, 9]
        k = 2
        expected = 4  # Pairs: (1,3), (3,5), (5,7), (7,9)
        assert self.solution.findPairs(nums, k) == expected

    def test_unsorted_input(self):
        """Test that algorithm works with unsorted input."""
        nums = [5, 1, 3, 4, 2]
        k = 1
        expected = 4  # Same as sorted [1,2,3,4,5]
        assert self.solution.findPairs(nums, k) == expected

    def test_large_numbers(self):
        """Test with large numbers."""
        nums = [1000000, 1000001, 1000002]
        k = 1
        expected = 2  # Pairs: (1000000,1000001), (1000001,1000002)
        assert self.solution.findPairs(nums, k) == expected

    def test_zero_in_array(self):
        """Test array containing zero."""
        nums = [0, 1, 2, 3]
        k = 1
        expected = 3  # Pairs: (0,1), (1,2), (2,3)
        assert self.solution.findPairs(nums, k) == expected

    def test_only_zeros(self):
        """Test array with only zeros."""
        nums = [0, 0, 0]
        k = 0
        expected = 1  # One unique pair: (0,0)
        assert self.solution.findPairs(nums, k) == expected

    def test_k_larger_than_max_diff(self):
        """Test k larger than maximum possible difference."""
        nums = [1, 2, 3]
        k = 5
        expected = 0  # No pairs with difference 5
        assert self.solution.findPairs(nums, k) == expected

    def test_performance_large_array(self):
        """Test performance with larger array."""
        nums = list(range(100))  # [0, 1, 2, ..., 99]
        k = 1
        expected = 99  # 99 consecutive pairs
        assert self.solution.findPairs(nums, k) == expected

    def test_duplicate_handling(self):
        """Test proper handling of duplicates."""
        nums = [1, 1, 1, 2, 2, 2, 3, 3, 3]
        k = 1
        expected = 2  # Unique pairs: (1,2), (2,3)
        assert self.solution.findPairs(nums, k) == expected

    def test_algorithm_correctness_properties(self):
        """Test fundamental properties of the algorithm."""
        # Test that pairs are unique
        nums = [1, 1, 2, 2, 3, 3]
        result_k0 = self.solution.findPairs(nums, 0)
        result_k1 = self.solution.findPairs(nums, 1)
        
        # For k=0, should find duplicates
        assert result_k0 == 3  # (1,1), (2,2), (3,3)
        
        # For k=1, should find consecutive unique pairs
        assert result_k1 == 2  # (1,2), (2,3)

    def test_edge_case_all_negative(self):
        """Test with all negative numbers."""
        nums = [-5, -4, -3, -2, -1]
        k = 1
        expected = 4  # Pairs: (-5,-4), (-4,-3), (-3,-2), (-2,-1)
        assert self.solution.findPairs(nums, k) == expected

    def test_symmetric_pairs(self):
        """Test that algorithm doesn't double count symmetric pairs."""
        nums = [1, 3, 1, 3]
        k = 2
        expected = 1  # Only one unique pair: (1,3)
        assert self.solution.findPairs(nums, k) == expected

    def test_boundary_values(self):
        """Test with boundary k values."""
        nums = [1, 2, 3, 4, 5]
        
        # k = 0 should find no pairs (no duplicates)
        assert self.solution.findPairs(nums, 0) == 0
        
        # k = max_diff should find one pair
        assert self.solution.findPairs(nums, 4) == 1  # (1,5)


if __name__ == '__main__':
    # Run the tests
    pytest.main([__file__])
