"""
Test suite for LeetCode 148: Sort List

This module contains comprehensive test cases for the sort list problem,
covering various edge cases and list patterns.
"""

import unittest
from leetcode.sort_list import Solution, list_to_array, array_to_list


class TestSortList(unittest.TestCase):
    """Test cases for Sort List solution."""

    def setUp(self):
        """Set up test fixtures before each test method."""
        self.solution = Solution()

    def test_example_1(self):
        """Test example 1 from LeetCode."""
        head = array_to_list([4, 2, 1, 3])
        result = self.solution.sortList(head)
        self.assertEqual(list_to_array(result), [1, 2, 3, 4])

    def test_example_2(self):
        """Test example 2 from LeetCode."""
        head = array_to_list([-1, 5, 3, 4, 0])
        result = self.solution.sortList(head)
        self.assertEqual(list_to_array(result), [-1, 0, 3, 4, 5])

    def test_empty_list(self):
        """Test empty list."""
        head = array_to_list([])
        result = self.solution.sortList(head)
        self.assertEqual(list_to_array(result), [])

    def test_single_element(self):
        """Test single element list."""
        head = array_to_list([1])
        result = self.solution.sortList(head)
        self.assertEqual(list_to_array(result), [1])

    def test_two_elements_sorted(self):
        """Test two elements already sorted."""
        head = array_to_list([1, 2])
        result = self.solution.sortList(head)
        self.assertEqual(list_to_array(result), [1, 2])

    def test_two_elements_reverse(self):
        """Test two elements in reverse order."""
        head = array_to_list([2, 1])
        result = self.solution.sortList(head)
        self.assertEqual(list_to_array(result), [1, 2])

    def test_already_sorted(self):
        """Test already sorted list."""
        head = array_to_list([1, 2, 3, 4, 5])
        result = self.solution.sortList(head)
        self.assertEqual(list_to_array(result), [1, 2, 3, 4, 5])

    def test_reverse_sorted(self):
        """Test reverse sorted list."""
        head = array_to_list([5, 4, 3, 2, 1])
        result = self.solution.sortList(head)
        self.assertEqual(list_to_array(result), [1, 2, 3, 4, 5])

    def test_duplicates(self):
        """Test list with duplicate values."""
        head = array_to_list([3, 1, 4, 1, 5, 9, 2, 6, 5])
        result = self.solution.sortList(head)
        self.assertEqual(list_to_array(result), [1, 1, 2, 3, 4, 5, 5, 6, 9])

    def test_all_same(self):
        """Test list with all same values."""
        head = array_to_list([2, 2, 2, 2, 2])
        result = self.solution.sortList(head)
        self.assertEqual(list_to_array(result), [2, 2, 2, 2, 2])

    def test_negative_numbers(self):
        """Test list with negative numbers."""
        head = array_to_list([-3, -1, -4, -2, -5])
        result = self.solution.sortList(head)
        self.assertEqual(list_to_array(result), [-5, -4, -3, -2, -1])

    def test_mixed_positive_negative(self):
        """Test list with mixed positive and negative numbers."""
        head = array_to_list([-1, 3, -2, 0, 1, -5, 4])
        result = self.solution.sortList(head)
        self.assertEqual(list_to_array(result), [-5, -2, -1, 0, 1, 3, 4])

    def test_zeros(self):
        """Test list with zeros."""
        head = array_to_list([0, -1, 0, 1, 0])
        result = self.solution.sortList(head)
        self.assertEqual(list_to_array(result), [-1, 0, 0, 0, 1])

    def test_large_numbers(self):
        """Test list with large numbers."""
        head = array_to_list([100000, -100000, 50000, 0, -50000])
        result = self.solution.sortList(head)
        self.assertEqual(list_to_array(result), [-100000, -50000, 0, 50000, 100000])

    def test_odd_length(self):
        """Test odd length list."""
        head = array_to_list([7, 3, 9, 1, 5])
        result = self.solution.sortList(head)
        self.assertEqual(list_to_array(result), [1, 3, 5, 7, 9])

    def test_even_length(self):
        """Test even length list."""
        head = array_to_list([8, 4, 2, 6])
        result = self.solution.sortList(head)
        self.assertEqual(list_to_array(result), [2, 4, 6, 8])

    def test_random_order(self):
        """Test randomly ordered list."""
        head = array_to_list([9, 1, 8, 2, 7, 3, 6, 4, 5])
        result = self.solution.sortList(head)
        self.assertEqual(list_to_array(result), [1, 2, 3, 4, 5, 6, 7, 8, 9])

    def test_three_elements(self):
        """Test three element variations."""
        # Test case 1
        head = array_to_list([3, 1, 2])
        result = self.solution.sortList(head)
        self.assertEqual(list_to_array(result), [1, 2, 3])
        
        # Test case 2
        head = array_to_list([1, 3, 2])
        result = self.solution.sortList(head)
        self.assertEqual(list_to_array(result), [1, 2, 3])

    def test_large_list(self):
        """Test larger list to verify performance."""
        arr = list(range(20, 0, -1))  # [20, 19, 18, ..., 1]
        head = array_to_list(arr)
        result = self.solution.sortList(head)
        expected = list(range(1, 21))  # [1, 2, 3, ..., 20]
        self.assertEqual(list_to_array(result), expected)

    def test_merge_lists_method(self):
        """Test the merge_lists helper method directly."""
        list1 = array_to_list([1, 3, 5])
        list2 = array_to_list([2, 4, 6])
        result = self.solution.merge_lists(list1, list2)
        self.assertEqual(list_to_array(result), [1, 2, 3, 4, 5, 6])


if __name__ == "__main__":
    unittest.main()