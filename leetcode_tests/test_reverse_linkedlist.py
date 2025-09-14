"""
Comprehensive test suite for LeetCode 206 & 92: Reverse Linked List problems.
"""

import pytest

from leetcode.reverse_linkedlist import Solution, ListNode


class TestReverseLinkedList:
    """Test cases for the Reverse Linked List problems."""
    
    def setup_method(self):
        """Set up test fixtures before each test method."""
        self.solution = Solution()

    def create_linked_list(self, values):
        """Helper method to create a linked list from a list of values."""
        if not values:
            return None
        
        head = ListNode(values[0])
        current = head
        for val in values[1:]:
            current.next = ListNode(val)
            current = current.next
        return head

    def linked_list_to_list(self, head):
        """Helper method to convert linked list to Python list for easy comparison."""
        result = []
        current = head
        while current:
            result.append(current.val)
            current = current.next
        return result

    # Tests for LeetCode 206: Reverse Linked List
    def test_reverse_list_basic(self):
        """Test basic reversal of a linked list."""
        head = self.create_linked_list([1, 2, 3, 4, 5])
        result = self.solution.reverseList(head)
        assert self.linked_list_to_list(result) == [5, 4, 3, 2, 1]

    def test_reverse_list_empty(self):
        """Test reversal of empty list."""
        result = self.solution.reverseList(None)
        assert result is None

    def test_reverse_list_single_node(self):
        """Test reversal of single node."""
        head = self.create_linked_list([42])
        result = self.solution.reverseList(head)
        assert self.linked_list_to_list(result) == [42]

    def test_reverse_list_two_nodes(self):
        """Test reversal of two nodes."""
        head = self.create_linked_list([1, 2])
        result = self.solution.reverseList(head)
        assert self.linked_list_to_list(result) == [2, 1]

    def test_reverse_list_duplicate_values(self):
        """Test reversal with duplicate values."""
        head = self.create_linked_list([1, 1, 2, 3, 3])
        result = self.solution.reverseList(head)
        assert self.linked_list_to_list(result) == [3, 3, 2, 1, 1]

    def test_reverse_list_negative_values(self):
        """Test reversal with negative values."""
        head = self.create_linked_list([-1, -2, 0, 1, 2])
        result = self.solution.reverseList(head)
        assert self.linked_list_to_list(result) == [2, 1, 0, -2, -1]

    def test_reverse_list_large_values(self):
        """Test reversal with large values."""
        head = self.create_linked_list([1000000, 999999, 1000001])
        result = self.solution.reverseList(head)
        assert self.linked_list_to_list(result) == [1000001, 999999, 1000000]

    def test_reverse_list_long_list(self):
        """Test reversal of longer list."""
        values = list(range(1, 11))  # [1, 2, 3, ..., 10]
        head = self.create_linked_list(values)
        result = self.solution.reverseList(head)
        assert self.linked_list_to_list(result) == list(reversed(values))

    # Tests for LeetCode 92: Reverse Linked List II
    def test_reverse_between_basic(self):
        """Test basic reversal between positions."""
        head = self.create_linked_list([1, 2, 3, 4, 5])
        result = self.solution.reverseBetween(head, 2, 4)
        assert self.linked_list_to_list(result) == [1, 4, 3, 2, 5]

    def test_reverse_between_entire_list(self):
        """Test reversal of entire list using reverseBetween."""
        head = self.create_linked_list([1, 2, 3, 4, 5])
        result = self.solution.reverseBetween(head, 1, 5)
        assert self.linked_list_to_list(result) == [5, 4, 3, 2, 1]

    def test_reverse_between_single_node_range(self):
        """Test reversal of single node range."""
        head = self.create_linked_list([1, 2, 3, 4, 5])
        result = self.solution.reverseBetween(head, 3, 3)
        assert self.linked_list_to_list(result) == [1, 2, 3, 4, 5]

    def test_reverse_between_first_two_nodes(self):
        """Test reversal of first two nodes."""
        head = self.create_linked_list([1, 2, 3, 4, 5])
        result = self.solution.reverseBetween(head, 1, 2)
        assert self.linked_list_to_list(result) == [2, 1, 3, 4, 5]

    def test_reverse_between_last_two_nodes(self):
        """Test reversal of last two nodes."""
        head = self.create_linked_list([1, 2, 3, 4, 5])
        result = self.solution.reverseBetween(head, 4, 5)
        assert self.linked_list_to_list(result) == [1, 2, 3, 5, 4]

    def test_reverse_between_middle_section(self):
        """Test reversal of middle section."""
        head = self.create_linked_list([1, 2, 3, 4, 5, 6, 7])
        result = self.solution.reverseBetween(head, 3, 5)
        assert self.linked_list_to_list(result) == [1, 2, 5, 4, 3, 6, 7]

    def test_reverse_between_single_node_list(self):
        """Test reverseBetween on single node list."""
        head = self.create_linked_list([42])
        result = self.solution.reverseBetween(head, 1, 1)
        assert self.linked_list_to_list(result) == [42]

    def test_reverse_between_two_node_list(self):
        """Test reverseBetween on two node list."""
        head = self.create_linked_list([1, 2])
        result = self.solution.reverseBetween(head, 1, 2)
        assert self.linked_list_to_list(result) == [2, 1]

    def test_reverse_between_with_duplicates(self):
        """Test reverseBetween with duplicate values."""
        head = self.create_linked_list([1, 2, 2, 3, 3, 4])
        result = self.solution.reverseBetween(head, 2, 5)
        assert self.linked_list_to_list(result) == [1, 3, 3, 2, 2, 4]

    def test_reverse_between_negative_values(self):
        """Test reverseBetween with negative values."""
        head = self.create_linked_list([-3, -2, -1, 0, 1, 2])
        result = self.solution.reverseBetween(head, 2, 4)
        assert self.linked_list_to_list(result) == [-3, 0, -1, -2, 1, 2]

    def test_reverse_between_large_range(self):
        """Test reverseBetween with large range."""
        values = list(range(1, 21))  # [1, 2, 3, ..., 20]
        head = self.create_linked_list(values)
        result = self.solution.reverseBetween(head, 5, 15)
        expected = values[:4] + list(reversed(values[4:15])) + values[15:]
        assert self.linked_list_to_list(result) == expected

    def test_reverse_between_at_boundaries(self):
        """Test reverseBetween at list boundaries."""
        # Test starting from first node
        head1 = self.create_linked_list([1, 2, 3, 4, 5])
        result1 = self.solution.reverseBetween(head1, 1, 3)
        assert self.linked_list_to_list(result1) == [3, 2, 1, 4, 5]
        
        # Test ending at last node
        head2 = self.create_linked_list([1, 2, 3, 4, 5])
        result2 = self.solution.reverseBetween(head2, 3, 5)
        assert self.linked_list_to_list(result2) == [1, 2, 5, 4, 3]

    def test_reverse_between_consecutive_pairs(self):
        """Test multiple consecutive pairs."""
        head = self.create_linked_list([1, 2, 3, 4, 5, 6])
        result = self.solution.reverseBetween(head, 2, 3)
        assert self.linked_list_to_list(result) == [1, 3, 2, 4, 5, 6]

    # Edge Cases and Error Conditions
    def test_reverse_between_empty_list(self):
        """Test reverseBetween on empty list."""
        # For empty list, the algorithm should handle gracefully
        # In practice, this would be an edge case that might cause errors
        # but we test that it doesn't crash catastrophically
        try:
            result = self.solution.reverseBetween(None, 1, 1)
            # If it doesn't crash, result should be None
            assert result is None
        except (AttributeError, IndexError):
            # It's acceptable for this edge case to raise an error
            # since LeetCode constraints typically guarantee valid input
            pass

    def test_large_list_performance(self):
        """Test performance with larger lists."""
        # Test with 1000 nodes
        values = list(range(1000))
        head = self.create_linked_list(values)
        
        # Test reverseList
        result1 = self.solution.reverseList(head)
        expected1 = list(reversed(values))
        assert self.linked_list_to_list(result1) == expected1
        
        # Test reverseBetween on fresh list
        head2 = self.create_linked_list(values)
        result2 = self.solution.reverseBetween(head2, 100, 900)
        expected2 = values[:99] + list(reversed(values[99:900])) + values[900:]
        assert self.linked_list_to_list(result2) == expected2

    # Comparison Tests
    def test_reverse_methods_equivalence(self):
        """Test that reverseBetween(head, 1, n) equals reverseList(head)."""
        values = [1, 2, 3, 4, 5, 6, 7]
        
        # Test reverseList
        head1 = self.create_linked_list(values)
        result1 = self.solution.reverseList(head1)
        
        # Test reverseBetween for entire list
        head2 = self.create_linked_list(values)
        result2 = self.solution.reverseBetween(head2, 1, len(values))
        
        assert self.linked_list_to_list(result1) == self.linked_list_to_list(result2)

    def test_reverse_twice_identity(self):
        """Test that reversing twice returns original list."""
        values = [1, 2, 3, 4, 5]
        head = self.create_linked_list(values)
        
        # Reverse twice
        reversed_once = self.solution.reverseList(head)
        reversed_twice = self.solution.reverseList(reversed_once)
        
        assert self.linked_list_to_list(reversed_twice) == values

    def test_reverse_between_twice_identity(self):
        """Test that reverseBetween twice on same range returns original."""
        values = [1, 2, 3, 4, 5, 6, 7]
        head = self.create_linked_list(values)
        
        # Reverse between twice
        result1 = self.solution.reverseBetween(head, 2, 5)
        result2 = self.solution.reverseBetween(result1, 2, 5)
        
        assert self.linked_list_to_list(result2) == values

    # Special Value Tests
    def test_reverse_with_zeros(self):
        """Test reversal with zero values."""
        head = self.create_linked_list([0, 0, 1, 0, 2])
        result = self.solution.reverseList(head)
        assert self.linked_list_to_list(result) == [2, 0, 1, 0, 0]

    def test_reverse_between_with_zeros(self):
        """Test reverseBetween with zero values."""
        head = self.create_linked_list([0, 1, 0, 2, 0])
        result = self.solution.reverseBetween(head, 2, 4)
        assert self.linked_list_to_list(result) == [0, 2, 0, 1, 0]

    def test_reverse_mixed_positive_negative(self):
        """Test reversal with mixed positive and negative values."""
        head = self.create_linked_list([-5, -1, 0, 3, 7])
        result = self.solution.reverseList(head)
        assert self.linked_list_to_list(result) == [7, 3, 0, -1, -5]


if __name__ == "__main__":
    # Run the tests
    pytest.main([__file__, "-v"])