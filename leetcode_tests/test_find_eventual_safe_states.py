"""
Test cases for LeetCode Problem #802: Find Eventual Safe States
"""
import unittest
from leetcode.find_eventual_safe_states import Solution


class TestFindEventualSafeStates(unittest.TestCase):
    """Test cases for the FindEventualSafeStates solution."""

    def setUp(self):
        """Set up test fixtures before each test method."""
        self.solution = Solution()

    def test_example_case_1(self):
        """Test the first example case."""
        graph = [[], [0, 2, 3, 4], [3], [4], []]
        result = self.solution.eventualSafeNodes(graph)
        expected = [0, 1, 2, 3, 4]
        assert sorted(result) == sorted(expected)

    def test_example_case_2(self):
        """Test the second example case."""
        graph = [[1, 2, 3, 4], [1, 2], [3, 4], [0, 4], []]
        result = self.solution.eventualSafeNodes(graph)
        expected = [4]
        assert sorted(result) == sorted(expected)

    def test_single_node_no_edges(self):
        """Test single node with no outgoing edges."""
        graph = [[]]
        result = self.solution.eventualSafeNodes(graph)
        expected = [0]
        assert result == expected

    def test_single_node_self_cycle(self):
        """Test single node with self-loop."""
        graph = [[0]]
        result = self.solution.eventualSafeNodes(graph)
        expected = []
        assert result == expected

    def test_simple_cycle(self):
        """Test simple cycle between two nodes."""
        graph = [[1], [0]]
        result = self.solution.eventualSafeNodes(graph)
        expected = []
        assert result == expected

    def test_all_terminal_nodes(self):
        """Test graph where all nodes are terminal."""
        graph = [[], [], []]
        result = self.solution.eventualSafeNodes(graph)
        expected = [0, 1, 2]
        assert sorted(result) == sorted(expected)

    def test_linear_chain(self):
        """Test linear chain of nodes."""
        graph = [[1], [2], []]
        result = self.solution.eventualSafeNodes(graph)
        expected = [0, 1, 2]
        assert sorted(result) == sorted(expected)

    def test_tree_structure(self):
        """Test tree-like structure."""
        graph = [[1, 2], [3], [3], []]
        result = self.solution.eventualSafeNodes(graph)
        expected = [0, 1, 2, 3]
        assert sorted(result) == sorted(expected)

    def test_complex_graph_with_cycles(self):
        """Test complex graph with multiple cycles."""
        graph = [[1, 2], [2, 3], [5], [0], [5], []]
        result = self.solution.eventualSafeNodes(graph)
        expected = [2, 4, 5]
        assert sorted(result) == sorted(expected)

    def test_disconnected_components(self):
        """Test graph with disconnected components."""
        graph = [[1], [], [3], []]
        result = self.solution.eventualSafeNodes(graph)
        expected = [0, 1, 2, 3]
        assert sorted(result) == sorted(expected)

    def test_large_cycle(self):
        """Test larger cycle."""
        graph = [[1], [2], [3], [0]]
        result = self.solution.eventualSafeNodes(graph)
        expected = []
        assert result == expected

    def test_multiple_paths_to_safe_node(self):
        """Test multiple paths leading to safe node."""
        graph = [[1, 2], [3], [3], []]
        result = self.solution.eventualSafeNodes(graph)
        expected = [0, 1, 2, 3]
        assert sorted(result) == sorted(expected)

    def test_node_with_cycle_and_safe_path(self):
        """Test node that has both cyclic and safe paths."""
        graph = [[1, 3], [2], [1], []]
        result = self.solution.eventualSafeNodes(graph)
        # Node 0 has paths to both cycle (0->1->2->1) and safe node (0->3)
        # But since it has ANY path to cycle, it's not safe
        expected = [3]
        assert sorted(result) == sorted(expected)

    def test_star_pattern(self):
        """Test star pattern where center connects to terminals."""
        graph = [[1, 2, 3], [], [], []]
        result = self.solution.eventualSafeNodes(graph)
        expected = [0, 1, 2, 3]
        assert sorted(result) == sorted(expected)

    def test_reverse_star_pattern(self):
        """Test reverse star pattern where terminals connect to center."""
        graph = [[], [0], [0], [0]]
        result = self.solution.eventualSafeNodes(graph)
        expected = [0, 1, 2, 3]
        assert sorted(result) == sorted(expected)

    def test_complex_mixed_structure(self):
        """Test complex structure with safe and unsafe nodes."""
        graph = [[1], [2, 3], [4], [1], []]
        result = self.solution.eventualSafeNodes(graph)
        # Node 0->1, Node 1 can go to 2->4 (safe) or 3->1 (cycle)
        # Since Node 1 has path to cycle, Node 0 is also not safe
        expected = [2, 4]
        assert sorted(result) == sorted(expected)

    def test_self_loop_with_exit(self):
        """Test node with self-loop and safe exit."""
        graph = [[0, 1], []]
        result = self.solution.eventualSafeNodes(graph)
        expected = [1]
        assert sorted(result) == sorted(expected)

    def test_nested_cycles(self):
        """Test nested cycle structures."""
        graph = [[1], [2], [3, 4], [1], []]
        result = self.solution.eventualSafeNodes(graph)
        expected = [4]
        assert sorted(result) == sorted(expected)

    def test_return_type_and_order(self):
        """Test that return type is list and order is correct."""
        graph = [[1], []]
        result = self.solution.eventualSafeNodes(graph)
        assert isinstance(result, list)
        assert all(isinstance(node, int) for node in result)
        assert result == sorted(result)

    def test_algorithm_correctness(self):
        """Test algorithm correctness with various patterns."""
        test_cases = [
            ([[]], [0]),
            ([[0]], []),
            ([[1], [0]], []),
            ([[1], []], [0, 1]),
            ([[1, 2], [], []], [0, 1, 2])
        ]
        
        for graph, expected in test_cases:
            with self.subTest(graph=graph):
                result = self.solution.eventualSafeNodes(graph)
                assert sorted(result) == sorted(expected)

    def test_boundary_conditions(self):
        """Test edge cases and boundary conditions."""
        # Single terminal node
        result = self.solution.eventualSafeNodes([[]])
        assert result == [0]
        
        # Two nodes, one terminal
        result = self.solution.eventualSafeNodes([[1], []])
        assert sorted(result) == [0, 1]

    def test_performance_reasonable_input(self):
        """Test performance with reasonable input size."""
        # Create a larger graph (chain of 100 nodes)
        size = 100
        graph = [[i + 1] if i < size - 1 else [] for i in range(size)]
        
        result = self.solution.eventualSafeNodes(graph)
        expected = list(range(size))
        assert sorted(result) == sorted(expected)

    def test_cycle_detection_accuracy(self):
        """Test accurate cycle detection."""
        # Graph with cycle: 0->1->2->0, and safe node 3
        graph = [[1], [2], [0], []]
        result = self.solution.eventualSafeNodes(graph)
        expected = [3]
        assert result == expected

    def test_multiple_terminal_convergence(self):
        """Test nodes converging to multiple terminals."""
        graph = [[1, 2], [], []]
        result = self.solution.eventualSafeNodes(graph)
        expected = [0, 1, 2]
        assert sorted(result) == sorted(expected)

    def test_deterministic_behavior(self):
        """Test that algorithm produces consistent results."""
        graph = [[1, 2], [3], [3], []]
        result1 = self.solution.eventualSafeNodes(graph)
        result2 = self.solution.eventualSafeNodes(graph)
        assert sorted(result1) == sorted(result2)

    def test_graph_structure_validation(self):
        """Test various graph structures for correctness."""
        # Triangle with exit
        graph = [[1], [2], [0, 3], []]
        result = self.solution.eventualSafeNodes(graph)
        expected = [3]
        assert result == expected

    def test_long_path_to_cycle(self):
        """Test long path leading to cycle."""
        graph = [[1], [2], [3], [4], [5], [3]]
        result = self.solution.eventualSafeNodes(graph)
        expected = []
        assert result == expected

    def test_multiple_entry_points_to_safe_area(self):
        """Test multiple paths entering safe area."""
        graph = [[2], [2], [], [2]]
        result = self.solution.eventualSafeNodes(graph)
        expected = [0, 1, 2, 3]
        assert sorted(result) == sorted(expected)


if __name__ == "__main__":
    unittest.main()
