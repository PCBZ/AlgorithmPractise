"""
Test suite for LeetCode 540: Single Element in a Sorted Array

This module contains comprehensive test cases for the single element problem,
covering various edge cases and array patterns.
"""

import unittest

from leetcode.single_element_sorted_array import Solution


class TestSingleElementSortedArray(unittest.TestCase):
    """Test cases for Single Element in Sorted Array solution."""

    def setUp(self):
        """Set up test fixtures before each test method."""
        self.solution = Solution()

    def test_example_1(self):
        """Test example 1 from LeetCode."""
        nums = [1, 1, 2, 3, 3, 4, 4, 8, 8]
        result = self.solution.singleNonDuplicate(nums)
        self.assertEqual(result, 2)

    def test_example_2(self):
        """Test example 2 from LeetCode."""
        nums = [3, 3, 7, 7, 10, 11, 11]
        result = self.solution.singleNonDuplicate(nums)
        self.assertEqual(result, 10)

    def test_single_element(self):
        """Test array with only one element."""
        nums = [1]
        result = self.solution.singleNonDuplicate(nums)
        self.assertEqual(result, 1)

    def test_single_at_beginning(self):
        """Test single element at the beginning."""
        nums = [1, 2, 2, 3, 3, 4, 4]
        result = self.solution.singleNonDuplicate(nums)
        self.assertEqual(result, 1)

    def test_single_at_end(self):
        """Test single element at the end."""
        nums = [1, 1, 2, 2, 3, 3, 4]
        result = self.solution.singleNonDuplicate(nums)
        self.assertEqual(result, 4)

    def test_three_elements_single_first(self):
        """Test three elements with single element first."""
        nums = [0, 1, 1]
        result = self.solution.singleNonDuplicate(nums)
        self.assertEqual(result, 0)

    def test_three_elements_single_middle(self):
        """Test three elements with single element in middle."""
        nums = [1, 2, 2]
        result = self.solution.singleNonDuplicate(nums)
        self.assertEqual(result, 1)

    def test_three_elements_single_last(self):
        """Test three elements with single element last."""
        nums = [1, 1, 2]
        result = self.solution.singleNonDuplicate(nums)
        self.assertEqual(result, 2)

    def test_five_elements_single_middle(self):
        """Test five elements with single in middle."""
        nums = [1, 1, 3, 4, 4]
        result = self.solution.singleNonDuplicate(nums)
        self.assertEqual(result, 3)

    def test_negative_numbers(self):
        """Test array with negative numbers."""
        nums = [-3, -3, -1, 0, 0, 1, 1]
        result = self.solution.singleNonDuplicate(nums)
        self.assertEqual(result, -1)

    def test_large_numbers(self):
        """Test array with large numbers."""
        nums = [100, 100, 200, 300, 300, 400, 400]
        result = self.solution.singleNonDuplicate(nums)
        self.assertEqual(result, 200)

    def test_duplicates_at_even_indices(self):
        """Test when all pairs start at even indices except for single element."""
        nums = [2, 2, 4, 4, 5, 6, 6, 8, 8]
        result = self.solution.singleNonDuplicate(nums)
        self.assertEqual(result, 5)

    def test_alternating_pattern_broken_early(self):
        """Test when the pattern breaks early in the array."""
        nums = [1, 2, 2, 3, 3, 4, 4, 5, 5]
        result = self.solution.singleNonDuplicate(nums)
        self.assertEqual(result, 1)

    def test_alternating_pattern_broken_late(self):
        """Test when the pattern breaks late in the array."""
        nums = [1, 1, 2, 2, 3, 3, 4, 4, 9]
        result = self.solution.singleNonDuplicate(nums)
        self.assertEqual(result, 9)

    def test_zeros_and_ones(self):
        """Test array with zeros and ones."""
        nums = [0, 0, 1, 1, 2]
        result = self.solution.singleNonDuplicate(nums)
        self.assertEqual(result, 2)

    def test_same_numbers_different_positions(self):
        """Test with same numbers in different arrangements."""
        nums = [5, 5, 7, 9, 9, 11, 11]
        result = self.solution.singleNonDuplicate(nums)
        self.assertEqual(result, 7)

    def test_single_element_middle_of_long_array(self):
        """Test single element in middle of longer array."""
        nums = [1, 1, 2, 2, 3, 3, 4, 5, 5, 6, 6, 7, 7]
        result = self.solution.singleNonDuplicate(nums)
        self.assertEqual(result, 4)

    def test_edge_case_small_array(self):
        """Test smallest possible array with pairs."""
        nums = [2, 3, 3]
        result = self.solution.singleNonDuplicate(nums)
        self.assertEqual(result, 2)

    def test_sequential_numbers(self):
        """Test with sequential numbers."""
        nums = [1, 1, 2, 2, 3, 4, 4, 5, 5]
        result = self.solution.singleNonDuplicate(nums)
        self.assertEqual(result, 3)

    def test_non_sequential_numbers(self):
        """Test with non-sequential numbers."""
        nums = [10, 10, 20, 30, 30, 40, 40]
        result = self.solution.singleNonDuplicate(nums)
        self.assertEqual(result, 20)


if __name__ == "__main__":
    unittest.main()