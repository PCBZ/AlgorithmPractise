"""
Comprehensive tests for Minimum Height Trees problem.

Tests the topological sorting algorithm for finding all possible roots
that result in minimum height trees.
"""
import pytest

from leetcode.minimum_height_trees import Solution


class TestMinimumHeightTrees:
    """Test class for minimum height trees implementation."""

    def setup_method(self):
        """Set up test fixtures before each test method."""
        self.solution = Solution()

    @pytest.fixture
    def leetcode_example_1(self):
        """First LeetCode example."""
        return 4, [[1, 0], [1, 2], [1, 3]]

    @pytest.fixture
    def leetcode_example_2(self):
        """Second LeetCode example."""
        return 6, [[3, 0], [3, 1], [3, 2], [3, 4], [5, 4]]

    def test_leetcode_example_1(self, leetcode_example_1):
        """Test first LeetCode example."""
        n, edges = leetcode_example_1
        result = self.solution.findMinHeightTrees(n, edges)
        assert result == [1]

    def test_leetcode_example_2(self, leetcode_example_2):
        """Test second LeetCode example."""
        n, edges = leetcode_example_2
        result = sorted(self.solution.findMinHeightTrees(n, edges))
        assert result == [3, 4]

    def test_single_node(self):
        """Test single node case."""
        result = self.solution.findMinHeightTrees(1, [])
        assert result == [0]

    def test_two_nodes(self):
        """Test two nodes case."""
        result = sorted(self.solution.findMinHeightTrees(2, [[0, 1]]))
        assert result == [0, 1]

    def test_three_nodes_linear(self):
        """Test linear tree with 3 nodes."""
        result = self.solution.findMinHeightTrees(3, [[0, 1], [1, 2]])
        assert result == [1]

    def test_four_nodes_linear(self):
        """Test linear tree with 4 nodes."""
        result = sorted(self.solution.findMinHeightTrees(4, [[0, 1], [1, 2], [2, 3]]))
        assert result == [1, 2]

    def test_five_nodes_linear(self):
        """Test linear tree with 5 nodes."""
        result = self.solution.findMinHeightTrees(5, [[0, 1], [1, 2], [2, 3], [3, 4]])
        assert result == [2]

    def test_six_nodes_linear(self):
        """Test linear tree with 6 nodes."""
        result = sorted(self.solution.findMinHeightTrees(6, [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5]]))
        assert result == [2, 3]

    def test_star_tree_4_nodes(self):
        """Test star tree with 4 nodes."""
        result = self.solution.findMinHeightTrees(4, [[0, 1], [0, 2], [0, 3]])
        assert result == [0]

    def test_star_tree_5_nodes(self):
        """Test star tree with 5 nodes."""
        result = self.solution.findMinHeightTrees(5, [[0, 1], [0, 2], [0, 3], [0, 4]])
        assert result == [0]

    def test_balanced_tree(self):
        """Test balanced tree structure."""
        edges = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6]]
        result = self.solution.findMinHeightTrees(7, edges)
        assert result == [0]

    def test_y_shaped_tree(self):
        """Test Y-shaped tree."""
        edges = [[0, 1], [1, 2], [2, 3], [2, 4], [4, 5]]
        result = self.solution.findMinHeightTrees(6, edges)
        assert result == [2]

    def test_fork_tree(self):
        """Test fork-like tree structure."""
        edges = [[0, 1], [1, 2], [1, 3], [1, 4]]
        result = self.solution.findMinHeightTrees(5, edges)
        assert result == [1]

    def test_tree_with_long_branch(self):
        """Test tree with one long branch."""
        edges = [[0, 1], [0, 2], [0, 3], [1, 4], [4, 5], [5, 6]]
        result = sorted(self.solution.findMinHeightTrees(7, edges))
        assert result == [1, 4]

    def test_unbalanced_tree(self):
        """Test unbalanced tree structure."""
        edges = [[0, 1], [1, 2], [2, 3], [1, 4], [4, 5]]
        result = self.solution.findMinHeightTrees(6, edges)
        assert result == [1]

    def test_binary_tree_like(self):
        """Test binary tree-like structure."""
        edges = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6]]
        result = self.solution.findMinHeightTrees(7, edges)
        assert result == [0]

    def test_complex_tree_structure(self):
        """Test more complex tree structure."""
        edges = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [3, 7]]
        result = sorted(self.solution.findMinHeightTrees(8, edges))
        assert result == [0, 1]

    def test_diamond_like_structure(self):
        """Test diamond-like tree structure."""
        edges = [[0, 1], [1, 2], [2, 3], [1, 4]]
        result = sorted(self.solution.findMinHeightTrees(5, edges))
        assert result == [1, 2]

    def test_larger_linear_tree(self):
        """Test larger linear tree."""
        n = 10
        edges = [[i, i+1] for i in range(n-1)]
        result = sorted(self.solution.findMinHeightTrees(n, edges))
        assert result == [4, 5]

    def test_larger_star_tree(self):
        """Test larger star tree."""
        n = 8
        center = 0
        edges = [[center, i] for i in range(1, n)]
        result = self.solution.findMinHeightTrees(n, edges)
        assert result == [center]

    def test_result_count_property(self):
        """Test that result always has at most 2 nodes."""
        test_cases = [
            (1, []),
            (2, [[0, 1]]),
            (3, [[0, 1], [1, 2]]),
            (4, [[0, 1], [1, 2], [2, 3]]),
            (5, [[0, 1], [1, 2], [2, 3], [3, 4]]),
            (6, [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5]]),
        ]
        
        for n, edges in test_cases:
            result = self.solution.findMinHeightTrees(n, edges)
            assert 1 <= len(result) <= 2, f"Failed for n={n}, got {len(result)} roots"

    def test_tree_with_multiple_branches(self):
        """Test tree with multiple equal branches."""
        edges = [[3, 0], [3, 1], [3, 2], [3, 4]]
        result = self.solution.findMinHeightTrees(5, edges)
        assert result == [3]

    def test_performance_larger_tree(self):
        """Test performance with larger tree."""
        n = 50
        # Create a linear tree for predictable behavior
        edges = [[i, i+1] for i in range(n-1)]
        result = sorted(self.solution.findMinHeightTrees(n, edges))
        # For even n, should be [n//2-1, n//2], for odd n, should be [n//2]
        if n % 2 == 0:
            expected = [n//2 - 1, n//2]
        else:
            expected = [n//2]
        assert result == expected

    def test_edge_cases_consistency(self):
        """Test that edge cases are handled consistently."""
        # Single node
        assert len(self.solution.findMinHeightTrees(1, [])) == 1
        
        # Two nodes
        assert len(self.solution.findMinHeightTrees(2, [[0, 1]])) == 2
        
        # Linear trees should have at most 2 roots
        for n in range(3, 10):
            edges = [[i, i+1] for i in range(n-1)]
            result = self.solution.findMinHeightTrees(n, edges)
            assert 1 <= len(result) <= 2

    def test_branching_factor_3(self):
        """Test tree with branching factor of 3."""
        n = 13
        edges = []
        # Create a tree where each node has at most 3 children
        for i in range(1, n):
            parent = (i - 1) // 3
            edges.append([parent, i])
        
        result = self.solution.findMinHeightTrees(n, edges)
        # Should return 1-2 nodes
        assert 1 <= len(result) <= 2

    def test_different_tree_patterns(self):
        """Test various tree patterns."""
        # Path of length 7
        edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6]]
        result = self.solution.findMinHeightTrees(7, edges)
        assert result == [3]
        
        # Path of length 8
        edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7]]
        result = sorted(self.solution.findMinHeightTrees(8, edges))
        assert result == [3, 4]

    def test_algorithm_correctness(self):
        """Test algorithm correctness with known cases."""
        # For a path graph, the center(s) should be the middle node(s)
        for n in range(1, 11):
            edges = [[i, i+1] for i in range(n-1)]
            result = sorted(self.solution.findMinHeightTrees(n, edges))
            
            if n == 1:
                expected = [0]
            elif n % 2 == 1:
                # Odd number of nodes: single center
                expected = [n // 2]
            else:
                # Even number of nodes: two centers
                expected = [n // 2 - 1, n // 2]
            
            assert result == expected, f"Failed for path of length {n}"


if __name__ == '__main__':
    pytest.main([__file__])
