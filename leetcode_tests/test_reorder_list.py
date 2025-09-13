"""Test cases for LeetCode 143: Reorder List"""

import pytest

from leetcode.reorder_list import Solution, ListNode, list_to_array


class TestReorderList:
    
    def setup_method(self):
        self.solution = Solution()
    
    def create_list(self, values):
        """Helper to create linked list from values."""
        if not values:
            return None
        head = ListNode(values[0])
        current = head
        for val in values[1:]:
            current.next = ListNode(val)
            current = current.next
        return head
    
    def test_example_1(self):
        head = self.create_list([1, 2, 3, 4])
        self.solution.reorderList(head)
        assert list_to_array(head) == [1, 4, 2, 3]
    
    def test_example_2(self):
        head = self.create_list([1, 2, 3, 4, 5])
        self.solution.reorderList(head)
        assert list_to_array(head) == [1, 5, 2, 4, 3]
    
    def test_single_node(self):
        head = self.create_list([1])
        self.solution.reorderList(head)
        assert list_to_array(head) == [1]
    
    def test_two_nodes(self):
        head = self.create_list([1, 2])
        self.solution.reorderList(head)
        assert list_to_array(head) == [1, 2]
    
    def test_three_nodes(self):
        head = self.create_list([1, 2, 3])
        self.solution.reorderList(head)
        assert list_to_array(head) == [1, 3, 2]
    
    def test_six_nodes(self):
        head = self.create_list([1, 2, 3, 4, 5, 6])
        self.solution.reorderList(head)
        assert list_to_array(head) == [1, 6, 2, 5, 3, 4]
    
    def test_seven_nodes(self):
        head = self.create_list([1, 2, 3, 4, 5, 6, 7])
        self.solution.reorderList(head)
        assert list_to_array(head) == [1, 7, 2, 6, 3, 5, 4]
    
    def test_empty_list(self):
        head = None
        self.solution.reorderList(head)
        assert list_to_array(head) == []
    
    def test_duplicate_values(self):
        head = self.create_list([1, 1, 2, 2])
        self.solution.reorderList(head)
        assert list_to_array(head) == [1, 2, 1, 2]
    
    def test_negative_values(self):
        head = self.create_list([-1, -2, -3, -4])
        self.solution.reorderList(head)
        assert list_to_array(head) == [-1, -4, -2, -3]
    
    def test_mixed_values(self):
        head = self.create_list([-1, 0, 1, 2, -2])
        self.solution.reorderList(head)
        assert list_to_array(head) == [-1, -2, 0, 2, 1]
    
    def test_large_list(self):
        values = list(range(1, 11))  # [1, 2, 3, ..., 10]
        head = self.create_list(values)
        self.solution.reorderList(head)
        expected = [1, 10, 2, 9, 3, 8, 4, 7, 5, 6]
        assert list_to_array(head) == expected
    
    def test_even_length_patterns(self):
        # Test various even-length lists
        test_cases = [
            ([1, 2, 3, 4, 5, 6, 7, 8], [1, 8, 2, 7, 3, 6, 4, 5]),
            ([10, 20, 30, 40], [10, 40, 20, 30]),
            ([0, 1], [0, 1])
        ]
        
        for input_vals, expected in test_cases:
            head = self.create_list(input_vals)
            self.solution.reorderList(head)
            assert list_to_array(head) == expected
    
    def test_odd_length_patterns(self):
        # Test various odd-length lists
        test_cases = [
            ([1, 2, 3, 4, 5, 6, 7], [1, 7, 2, 6, 3, 5, 4]),
            ([5, 10, 15], [5, 15, 10]),
            ([42], [42])
        ]
        
        for input_vals, expected in test_cases:
            head = self.create_list(input_vals)
            self.solution.reorderList(head)
            assert list_to_array(head) == expected
    
    def test_sequential_operations(self):
        # Test that we can perform operation multiple times
        head = self.create_list([1, 2, 3, 4])
        
        # First reorder: [1,2,3,4] -> [1,4,2,3]
        self.solution.reorderList(head)
        result1 = list_to_array(head)
        assert result1 == [1, 4, 2, 3]
        
        # Create fresh list for second test
        head2 = self.create_list([1, 2, 3, 4, 5, 6])
        self.solution.reorderList(head2)
        result2 = list_to_array(head2)
        assert result2 == [1, 6, 2, 5, 3, 4]
    
    def test_property_length_preserved(self):
        # Property test: length should be preserved
        test_cases = [
            [1, 2, 3],
            [1, 2, 3, 4, 5],
            [10, 20, 30, 40, 50, 60, 70, 80]
        ]
        
        for values in test_cases:
            head = self.create_list(values)
            original_length = len(values)
            self.solution.reorderList(head)
            result = list_to_array(head)
            assert len(result) == original_length
    
    def test_property_elements_preserved(self):
        # Property test: all elements should be preserved
        test_cases = [
            [1, 2, 3, 4],
            [5, 1, 3, 2, 4],
            [10, 20, 30, 40, 50]
        ]
        
        for values in test_cases:
            head = self.create_list(values)
            original_set = set(values)
            self.solution.reorderList(head)
            result = list_to_array(head)
            result_set = set(result)
            assert result_set == original_set


if __name__ == "__main__":
    pytest.main([__file__, "-v"])