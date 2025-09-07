"""
Test cases for LeetCode Problem 328: Odd Even Linked List.
"""

import pytest
from leetcode.odd_even_linkedlist import Solution, ListNode


class TestOddEvenLinkedList:
    """Test class for odd even linked list problem."""

    def setup_method(self):
        """Set up test fixtures."""
        self.solution = Solution()

    def create_linked_list(self, values):
        """Helper to create linked list from values."""
        if not values:
            return None
        
        head = ListNode(values[0])
        current = head
        for val in values[1:]:
            current.next = ListNode(val)
            current = current.next
        
        return head

    def linked_list_to_list(self, head):
        """Helper to convert linked list to list for testing."""
        result = []
        current = head
        while current:
            result.append(current.val)
            current = current.next
        return result

    @pytest.mark.parametrize("input_values,expected", [
        # Basic test cases from LeetCode examples
        ([1, 2, 3, 4, 5], [1, 3, 5, 2, 4]),
        ([2, 1, 3, 5, 6, 4, 7], [2, 3, 6, 7, 1, 5, 4]),
        
        # Edge cases
        ([], []),                    # Empty list
        ([1], [1]),                  # Single node
        ([1, 2], [1, 2]),            # Two nodes
        ([1, 2, 3], [1, 3, 2]),      # Three nodes
        ([1, 2, 3, 4], [1, 3, 2, 4]), # Four nodes
        
        # Larger cases
        ([1, 2, 3, 4, 5, 6], [1, 3, 5, 2, 4, 6]),
        ([1, 2, 3, 4, 5, 6, 7, 8], [1, 3, 5, 7, 2, 4, 6, 8]),
        
        # Different value patterns
        ([10, 20, 30, 40], [10, 30, 20, 40]),
        ([5, 4, 3, 2, 1], [5, 3, 1, 4, 2]),
        
        # Negative numbers
        ([-1, -2, -3, -4], [-1, -3, -2, -4]),
        ([1, -2, 3, -4, 5], [1, 3, 5, -2, -4]),
        
        # Large numbers
        ([100, 200, 300, 400, 500], [100, 300, 500, 200, 400]),
    ])
    def test_odd_even_list(self, input_values, expected):
        """Test oddEvenList with various inputs."""
        head = self.create_linked_list(input_values)
        result_head = self.solution.oddEvenList(head)
        result = self.linked_list_to_list(result_head)
        assert result == expected, f"Failed for {input_values}: expected {expected}, got {result}"

    def test_empty_list(self):
        """Test with empty list."""
        head = None
        result = self.solution.oddEvenList(head)
        assert result is None

    def test_single_node(self):
        """Test with single node."""
        head = ListNode(42)
        result = self.solution.oddEvenList(head)
        assert result.val == 42
        assert result.next is None

    def test_two_nodes(self):
        """Test with two nodes."""
        head = ListNode(1)
        head.next = ListNode(2)
        
        result = self.solution.oddEvenList(head)
        values = self.linked_list_to_list(result)
        assert values == [1, 2]

    def test_three_nodes(self):
        """Test with three nodes."""
        head = ListNode(1)
        head.next = ListNode(2)
        head.next.next = ListNode(3)
        
        result = self.solution.oddEvenList(head)
        values = self.linked_list_to_list(result)
        assert values == [1, 3, 2]

    def test_odd_length_list(self):
        """Test with odd length list."""
        values = [1, 2, 3, 4, 5, 6, 7]
        head = self.create_linked_list(values)
        result = self.solution.oddEvenList(head)
        result_values = self.linked_list_to_list(result)
        expected = [1, 3, 5, 7, 2, 4, 6]
        assert result_values == expected

    def test_even_length_list(self):
        """Test with even length list."""
        values = [1, 2, 3, 4, 5, 6, 7, 8]
        head = self.create_linked_list(values)
        result = self.solution.oddEvenList(head)
        result_values = self.linked_list_to_list(result)
        expected = [1, 3, 5, 7, 2, 4, 6, 8]
        assert result_values == expected

    def test_relative_order_preserved(self):
        """Test that relative order within odd/even groups is preserved."""
        values = [10, 20, 30, 40, 50, 60]
        head = self.create_linked_list(values)
        result = self.solution.oddEvenList(head)
        result_values = self.linked_list_to_list(result)
        
        # Odd positions (1st, 3rd, 5th): 10, 30, 50
        # Even positions (2nd, 4th, 6th): 20, 40, 60
        expected = [10, 30, 50, 20, 40, 60]
        assert result_values == expected

    def test_large_list_performance(self):
        """Test with larger list to check basic performance."""
        values = list(range(1, 101))  # 1 to 100
        head = self.create_linked_list(values)
        result = self.solution.oddEvenList(head)
        result_values = self.linked_list_to_list(result)
        
        # First 50 should be odd positions (1, 3, 5, ..., 99)
        # Last 50 should be even positions (2, 4, 6, ..., 100)
        odd_positions = [i for i in range(1, 101) if i % 2 == 1]
        even_positions = [i for i in range(1, 101) if i % 2 == 0]
        expected = odd_positions + even_positions
        
        assert result_values == expected

    def test_return_type(self):
        """Test that return type is correct."""
        head = ListNode(1)
        result = self.solution.oddEvenList(head)
        assert isinstance(result, ListNode) or result is None

    def test_original_nodes_reused(self):
        """Test that original nodes are reused (no new nodes created)."""
        # Create nodes with unique objects to track
        node1 = ListNode(1)
        node2 = ListNode(2)
        node3 = ListNode(3)
        node1.next = node2
        node2.next = node3
        
        original_nodes = {id(node1), id(node2), id(node3)}
        
        result = self.solution.oddEvenList(node1)
        
        # Collect all node IDs in result
        result_node_ids = set()
        current = result
        while current:
            result_node_ids.add(id(current))
            current = current.next
        
        # Should use exact same node objects
        assert result_node_ids == original_nodes

    def test_no_cycles_created(self):
        """Test that no cycles are created in the result."""
        values = [1, 2, 3, 4, 5]
        head = self.create_linked_list(values)
        result = self.solution.oddEvenList(head)
        
        # Traverse and ensure it terminates
        visited = set()
        current = result
        while current:
            node_id = id(current)
            assert node_id not in visited, "Cycle detected in linked list"
            visited.add(node_id)
            current = current.next

    def test_tail_properly_terminated(self):
        """Test that the tail of result list is properly terminated."""
        values = [1, 2, 3, 4]
        head = self.create_linked_list(values)
        result = self.solution.oddEvenList(head)
        
        # Find the last node
        current = result
        while current and current.next:
            current = current.next
        
        # Last node should point to None
        assert current.next is None

    def test_duplicate_values(self):
        """Test with duplicate values in the list."""
        values = [1, 1, 2, 2, 3, 3]
        head = self.create_linked_list(values)
        result = self.solution.oddEvenList(head)
        result_values = self.linked_list_to_list(result)
        
        # Odd positions: 1, 2, 3 (indices 0, 2, 4)
        # Even positions: 1, 2, 3 (indices 1, 3, 5)
        expected = [1, 2, 3, 1, 2, 3]
        assert result_values == expected

    def test_zero_values(self):
        """Test with zero values."""
        values = [0, 1, 0, 1, 0]
        head = self.create_linked_list(values)
        result = self.solution.oddEvenList(head)
        result_values = self.linked_list_to_list(result)
        expected = [0, 0, 0, 1, 1]
        assert result_values == expected

    def test_all_same_values(self):
        """Test with all same values."""
        values = [5, 5, 5, 5, 5, 5]
        head = self.create_linked_list(values)
        result = self.solution.oddEvenList(head)
        result_values = self.linked_list_to_list(result)
        expected = [5, 5, 5, 5, 5, 5]
        assert result_values == expected

    def test_alternating_pattern(self):
        """Test with alternating high-low pattern."""
        values = [1, 100, 2, 99, 3, 98]
        head = self.create_linked_list(values)
        result = self.solution.oddEvenList(head)
        result_values = self.linked_list_to_list(result)
        expected = [1, 2, 3, 100, 99, 98]
        assert result_values == expected

    def test_boundary_values(self):
        """Test with boundary integer values."""
        values = [-1000, 1000, -500, 500]
        head = self.create_linked_list(values)
        result = self.solution.oddEvenList(head)
        result_values = self.linked_list_to_list(result)
        expected = [-1000, -500, 1000, 500]
        assert result_values == expected
