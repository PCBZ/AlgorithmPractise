"""
Comprehensive test suite for LeetCode 847: Shortest Path Visiting All Nodes
"""

import unittest
from leetcode.shortest_path_visiting_all_nodes import Solution


class TestShortestPathVisitingAllNodes(unittest.TestCase):
    """Test cases for Shortest Path Visiting All Nodes problem."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.solution = Solution()
    
    def test_example_1(self):
        """Test star graph - central node connected to all others."""
        graph = [[1, 2, 3], [0], [0], [0]]
        result = self.solution.shortestPathLength(graph)
        self.assertEqual(result, 4)
    
    def test_example_2(self):
        """Test linear path graph."""
        graph = [[1], [0, 2], [1]]
        result = self.solution.shortestPathLength(graph)
        self.assertEqual(result, 2)
    
    def test_single_node(self):
        """Test single node graph."""
        graph = [[]]
        result = self.solution.shortestPathLength(graph)
        self.assertEqual(result, 0)
    
    def test_two_nodes_connected(self):
        """Test simple two-node graph."""
        graph = [[1], [0]]
        result = self.solution.shortestPathLength(graph)
        self.assertEqual(result, 1)
    
    def test_triangle_complete_graph(self):
        """Test complete graph with 3 nodes (triangle)."""
        graph = [[1, 2], [0, 2], [0, 1]]
        result = self.solution.shortestPathLength(graph)
        self.assertEqual(result, 2)
    
    def test_four_node_cycle(self):
        """Test cycle graph with 4 nodes."""
        graph = [[1, 3], [0, 2], [1, 3], [0, 2]]
        result = self.solution.shortestPathLength(graph)
        self.assertEqual(result, 3)
    
    def test_four_node_star(self):
        """Test star graph with 4 nodes."""
        graph = [[1, 2, 3], [0], [0], [0]]
        result = self.solution.shortestPathLength(graph)
        self.assertEqual(result, 4)
    
    def test_linear_chain_4_nodes(self):
        """Test linear chain with 4 nodes."""
        graph = [[1], [0, 2], [1, 3], [2]]
        result = self.solution.shortestPathLength(graph)
        self.assertEqual(result, 3)
    
    def test_complete_graph_4_nodes(self):
        """Test complete graph with 4 nodes."""
        graph = [[1, 2, 3], [0, 2, 3], [0, 1, 3], [0, 1, 2]]
        result = self.solution.shortestPathLength(graph)
        self.assertEqual(result, 3)
    
    def test_tree_structure(self):
        """Test tree structure."""
        graph = [[1, 2], [0, 3, 4], [0], [1], [1]]
        result = self.solution.shortestPathLength(graph)
        self.assertEqual(result, 5)
    
    def test_disconnected_components_within_connected_graph(self):
        """Test graph with bridge structure."""
        graph = [[1], [0, 2], [1, 3], [2]]
        result = self.solution.shortestPathLength(graph)
        self.assertEqual(result, 3)
    
    def test_five_node_star(self):
        """Test star graph with 5 nodes."""
        graph = [[1, 2, 3, 4], [0], [0], [0], [0]]
        result = self.solution.shortestPathLength(graph)
        self.assertEqual(result, 6)
    
    def test_pentagon_cycle(self):
        """Test pentagon (5-node cycle)."""
        graph = [[1, 4], [0, 2], [1, 3], [2, 4], [0, 3]]
        result = self.solution.shortestPathLength(graph)
        self.assertEqual(result, 4)
    
    def test_binary_tree_like(self):
        """Test binary tree-like structure."""
        graph = [[1, 2], [0, 3], [0, 4], [1], [2]]
        result = self.solution.shortestPathLength(graph)
        self.assertEqual(result, 4)
    
    def test_complex_graph_6_nodes(self):
        """Test more complex 6-node graph."""
        graph = [[1, 2], [0, 2, 3], [0, 1, 4], [1, 5], [2, 5], [3, 4]]
        result = self.solution.shortestPathLength(graph)
        self.assertEqual(result, 5)
    
    def test_hub_and_spoke_variation(self):
        """Test hub and spoke with some interconnections."""
        graph = [[1, 2, 3], [0, 4], [0, 4], [0, 4], [1, 2, 3]]
        result = self.solution.shortestPathLength(graph)
        self.assertEqual(result, 4)
    
    def test_path_with_branch(self):
        """Test path graph with a branch."""
        graph = [[1], [0, 2, 3], [1], [1]]
        result = self.solution.shortestPathLength(graph)
        self.assertEqual(result, 4)
    
    def test_diamond_structure(self):
        """Test diamond-shaped graph."""
        graph = [[1, 2], [0, 3], [0, 3], [1, 2]]
        result = self.solution.shortestPathLength(graph)
        self.assertEqual(result, 3)
    
    def test_maximum_constraint_12_nodes(self):
        """Test with larger graph (12 nodes in star formation)."""
        # Create a star graph with 12 nodes (node 0 connected to all others)
        graph = [list(range(1, 12))] + [[0] for _ in range(11)]
        result = self.solution.shortestPathLength(graph)
        self.assertEqual(result, 20)  # 2 * (n-1) for star graph
    
    def test_highly_connected_small_graph(self):
        """Test small but highly connected graph."""
        graph = [[1, 2, 3, 4], [0, 2, 3], [0, 1, 4], [0, 1], [0, 2]]
        result = self.solution.shortestPathLength(graph)
        self.assertEqual(result, 4)


if __name__ == "__main__":
    unittest.main()