"""
Comprehensive test suite for LeetCode Problem #138: Copy List with Random Pointer

Tests the copyRandomList method which creates a deep copy of a linked list
where each node has an additional random pointer.
"""

from leetcode.copy_list_with_random_pointer import Solution, Node


class TestCopyListWithRandomPointer:
    """Test class for copy list with random pointer problem."""

    def setup_method(self):
        """Set up test fixtures before each test method."""
        self.solution = Solution()

    def _create_linked_list(self, values, random_indices=None):
        """
        Helper method to create a linked list with random pointers.
        
        Args:
            values: List of node values
            random_indices: List of indices for random pointers (None for no random)
        
        Returns:
            Head of the created linked list
        """
        if not values:
            return None
        
        # Create nodes
        nodes = [Node(val) for val in values]
        
        # Connect next pointers
        for i in range(len(nodes) - 1):
            nodes[i].next = nodes[i + 1]
        
        # Connect random pointers
        if random_indices:
            for i, random_idx in enumerate(random_indices):
                if random_idx is not None and 0 <= random_idx < len(nodes):
                    nodes[i].random = nodes[random_idx]
        
        return nodes[0]

    def _compare_lists(self, original, copied):
        """
        Compare original and copied lists to ensure deep copy correctness.
        
        Args:
            original: Head of original list
            copied: Head of copied list
        
        Returns:
            True if lists are equivalent but independent, False otherwise
        """
        if not original and not copied:
            return True
        if not original or not copied:
            return False
        
        # Track original nodes for verification
        original_nodes = set()
        current = original
        while current:
            original_nodes.add(current)
            current = current.next
        
        # Verify copied list
        orig_current = original
        copy_current = copied
        
        while orig_current and copy_current:
            # Values should match
            if orig_current.val != copy_current.val:
                return False
            
            # Copied nodes should be different objects
            if copy_current in original_nodes:
                return False
            
            # Random pointer structure should match
            if orig_current.random is None:
                if copy_current.random is not None:
                    return False
            else:
                if copy_current.random is None:
                    return False
                if orig_current.random.val != copy_current.random.val:
                    return False
                # Random pointer should not point to original nodes
                if copy_current.random in original_nodes:
                    return False
            
            orig_current = orig_current.next
            copy_current = copy_current.next
        
        # Both should end at the same time
        return orig_current is None and copy_current is None

    def test_empty_list(self):
        """Test with empty list."""
        result = self.solution.copyRandomList(None)
        assert result is None

    def test_single_node_no_random(self):
        """Test with single node and no random pointer."""
        head = Node(1)
        result = self.solution.copyRandomList(head)
        
        assert result is not None
        assert result.val == 1
        assert result.next is None
        assert result.random is None
        assert result is not head  # Different object

    def test_single_node_self_random(self):
        """Test with single node pointing to itself."""
        head = Node(1)
        head.random = head
        result = self.solution.copyRandomList(head)
        
        assert result is not None
        assert result.val == 1
        assert result.next is None
        assert result.random is result  # Points to itself
        assert result is not head  # Different object

    def test_two_nodes_no_random(self):
        """Test with two nodes and no random pointers."""
        head = self._create_linked_list([1, 2])
        result = self.solution.copyRandomList(head)
        
        assert self._compare_lists(head, result)

    def test_two_nodes_with_random(self):
        """Test with two nodes having random pointers."""
        head = self._create_linked_list([1, 2], [1, 0])  # 1->2, random: 1->2, 2->1
        result = self.solution.copyRandomList(head)
        
        assert self._compare_lists(head, result)

    def test_example_case(self):
        """Test the LeetCode example case."""
        # Create: 7->13->11->10->1
        # Random: null, 0, 4, 2, 0
        head = self._create_linked_list([7, 13, 11, 10, 1], [None, 0, 4, 2, 0])
        result = self.solution.copyRandomList(head)
        
        assert self._compare_lists(head, result)

    def test_all_nodes_random_to_first(self):
        """Test where all random pointers point to first node."""
        head = self._create_linked_list([1, 2, 3, 4], [0, 0, 0, 0])
        result = self.solution.copyRandomList(head)
        
        assert self._compare_lists(head, result)

    def test_circular_random_pointers(self):
        """Test with circular random pointer pattern."""
        head = self._create_linked_list([1, 2, 3], [1, 2, 0])  # 1->2, 2->3, 3->1
        result = self.solution.copyRandomList(head)
        
        assert self._compare_lists(head, result)

    def test_no_random_pointers(self):
        """Test list with no random pointers at all."""
        head = self._create_linked_list([1, 2, 3, 4, 5])
        result = self.solution.copyRandomList(head)
        
        assert self._compare_lists(head, result)

    def test_all_random_to_last(self):
        """Test where all random pointers point to last node."""
        head = self._create_linked_list([1, 2, 3, 4], [3, 3, 3, 3])
        result = self.solution.copyRandomList(head)
        
        assert self._compare_lists(head, result)

    def test_random_pattern_every_other(self):
        """Test pattern where every other node has random pointer."""
        head = self._create_linked_list([1, 2, 3, 4, 5], [2, None, 4, None, 0])
        result = self.solution.copyRandomList(head)
        
        assert self._compare_lists(head, result)

    def test_deep_copy_independence(self):
        """Test that modifications to original don't affect copy."""
        head = self._create_linked_list([1, 2, 3], [1, 2, 0])
        result = self.solution.copyRandomList(head)
        
        # Modify original
        head.val = 999
        head.next.val = 888
        
        # Copy should be unchanged
        assert result.val == 1
        assert result.next.val == 2

    def test_return_type_and_structure(self):
        """Test that return type and structure are correct."""
        head = self._create_linked_list([1, 2, 3])
        result = self.solution.copyRandomList(head)
        
        assert isinstance(result, Node)
        assert result.val == 1
        assert isinstance(result.next, Node)
        assert result.next.val == 2

    def test_complex_random_pattern(self):
        """Test complex random pointer pattern."""
        # Create more complex pattern
        values = [7, 13, 11, 10, 1]
        random_indices = [None, 0, 4, 2, 0]
        head = self._create_linked_list(values, random_indices)
        result = self.solution.copyRandomList(head)
        
        assert self._compare_lists(head, result)
        
        # Verify specific random connections
        current = result
        expected_random_vals = [None, 7, 1, 11, 7]
        for i, expected_val in enumerate(expected_random_vals):
            if expected_val is None:
                assert current.random is None
            else:
                assert current.random.val == expected_val
            current = current.next

    def test_large_list_performance(self):
        """Test performance with larger list."""
        values = list(range(100))
        random_indices = [(i + 50) % 100 for i in range(100)]  # Each points 50 ahead (mod 100)
        
        head = self._create_linked_list(values, random_indices)
        result = self.solution.copyRandomList(head)
        
        assert self._compare_lists(head, result)

    def test_node_identity_independence(self):
        """Test that copied nodes are completely independent objects."""
        head = self._create_linked_list([1, 2, 3], [1, 2, 0])
        result = self.solution.copyRandomList(head)
        
        # Collect all original nodes
        original_nodes = set()
        current = head
        while current:
            original_nodes.add(current)
            current = current.next
        
        # Verify no copied node is in original set
        current = result
        while current:
            assert current not in original_nodes
            if current.random:
                assert current.random not in original_nodes
            current = current.next

    def test_random_pointer_correctness(self):
        """Test that random pointers in copy point to correct copied nodes."""
        head = self._create_linked_list([1, 2, 3, 4], [2, 3, 0, 1])
        result = self.solution.copyRandomList(head)
        
        # Create mapping of original to copied for verification
        orig_to_copy = {}
        orig_current = head
        copy_current = result
        while orig_current:
            orig_to_copy[orig_current] = copy_current
            orig_current = orig_current.next
            copy_current = copy_current.next
        
        # Verify random pointers
        orig_current = head
        copy_current = result
        while orig_current:
            if orig_current.random:
                expected_copy = orig_to_copy[orig_current.random]
                assert copy_current.random is expected_copy
            else:
                assert copy_current.random is None
            orig_current = orig_current.next
            copy_current = copy_current.next

    def test_edge_case_all_same_values(self):
        """Test with all nodes having same value."""
        head = self._create_linked_list([5, 5, 5, 5], [1, 2, 3, 0])
        result = self.solution.copyRandomList(head)
        
        assert self._compare_lists(head, result)

    def test_algorithm_correctness_validation(self):
        """Comprehensive validation of algorithm correctness."""
        test_cases = [
            ([1], [None]),
            ([1, 2], [1, 0]),
            ([1, 2, 3], [2, 0, 1]),
            ([7, 13, 11, 10, 1], [None, 0, 4, 2, 0]),
        ]
        
        for values, random_indices in test_cases:
            head = self._create_linked_list(values, random_indices)
            result = self.solution.copyRandomList(head)
            assert self._compare_lists(head, result)

    def test_memory_efficiency(self):
        """Test that solution uses reasonable memory."""
        # This is more of a structural test - the algorithm should use O(n) space
        values = list(range(50))
        random_indices = [i for i in range(49, -1, -1)]  # Reverse order random pointers
        
        head = self._create_linked_list(values, random_indices)
        result = self.solution.copyRandomList(head)
        
        # Just verify it completes and produces correct result
        assert self._compare_lists(head, result)

    def test_list_integrity_after_copy(self):
        """Test that original list remains intact after copying."""
        original_values = [1, 2, 3, 4]
        random_indices = [3, 0, 1, 2]
        head = self._create_linked_list(original_values, random_indices)
        
        # Store original state
        orig_vals = []
        orig_random_vals = []
        current = head
        while current:
            orig_vals.append(current.val)
            orig_random_vals.append(current.random.val if current.random else None)
            current = current.next
        
        # Perform copy
        result = self.solution.copyRandomList(head)
        
        # Verify original is unchanged
        current = head
        for i, expected_val in enumerate(orig_vals):
            assert current.val == expected_val
            if orig_random_vals[i] is not None:
                assert current.random.val == orig_random_vals[i]
            else:
                assert current.random is None
            current = current.next

    def test_mathematical_properties(self):
        """Test mathematical properties of the solution."""
        values = [1, 2, 3, 4, 5]
        random_indices = [4, 0, 1, 2, 3]
        head = self._create_linked_list(values, random_indices)
        result = self.solution.copyRandomList(head)
        
        # Count nodes in both lists
        orig_count = 0
        current = head
        while current:
            orig_count += 1
            current = current.next
        
        copy_count = 0
        current = result
        while current:
            copy_count += 1
            current = current.next
        
        assert orig_count == copy_count == len(values)
