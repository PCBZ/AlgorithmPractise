"""
Comprehensive tests for Min Cost to Connect All Points problem.

Tests the Prim's algorithm implementation for finding minimum spanning tree
with Manhattan distance as edge weights.
"""
import pytest

from leetcode.min_cost_to_connect_all_points import Solution


class TestMinCostConnectAllPoints:
    """Test class for min cost to connect all points implementation."""

    def setup_method(self):
        """Set up test fixtures before each test method."""
        self.solution = Solution()

    @pytest.fixture
    def leetcode_example_1(self):
        """First LeetCode example."""
        return [[0, 0], [2, 2], [3, 10], [5, 2], [7, 0]]

    @pytest.fixture
    def leetcode_example_2(self):
        """Second LeetCode example."""
        return [[3, 12], [-2, 5], [-4, 1]]

    @pytest.fixture
    def leetcode_example_3(self):
        """Third LeetCode example."""
        return [[0, 0], [1, 1], [1, 0], [-1, 1]]

    def test_leetcode_example_1(self, leetcode_example_1):
        """Test first LeetCode example."""
        result = self.solution.minCostConnectPoints(leetcode_example_1)
        assert result == 20

    def test_leetcode_example_2(self, leetcode_example_2):
        """Test second LeetCode example."""
        result = self.solution.minCostConnectPoints(leetcode_example_2)
        assert result == 18

    def test_leetcode_example_3(self, leetcode_example_3):
        """Test third LeetCode example."""
        result = self.solution.minCostConnectPoints(leetcode_example_3)
        assert result == 4

    def test_empty_points(self):
        """Test empty input."""
        result = self.solution.minCostConnectPoints([])
        assert result == 0

    def test_single_point(self):
        """Test single point."""
        result = self.solution.minCostConnectPoints([[0, 0]])
        assert result == 0

    def test_two_points(self):
        """Test two points."""
        points = [[0, 0], [3, 4]]
        result = self.solution.minCostConnectPoints(points)
        # Manhattan distance: |0-3| + |0-4| = 3 + 4 = 7
        assert result == 7

    def test_three_points_line(self):
        """Test three points in a line."""
        points = [[0, 0], [1, 0], [2, 0]]
        result = self.solution.minCostConnectPoints(points)
        # Connect (0,0)-(1,0) and (1,0)-(2,0): 1 + 1 = 2
        assert result == 2

    def test_three_points_triangle(self):
        """Test three points forming a triangle."""
        points = [[0, 0], [1, 0], [0, 1]]
        result = self.solution.minCostConnectPoints(points)
        # Connect (0,0)-(1,0) and (0,0)-(0,1): 1 + 1 = 2
        assert result == 2

    def test_square_points(self):
        """Test four points forming a square."""
        points = [[0, 0], [1, 0], [1, 1], [0, 1]]
        result = self.solution.minCostConnectPoints(points)
        # MST should connect 3 edges with cost 1 each
        assert result == 3

    def test_negative_coordinates(self):
        """Test with negative coordinates."""
        points = [[-1, -1], [1, 1], [-1, 1], [1, -1]]
        result = self.solution.minCostConnectPoints(points)
        # Each edge has Manhattan distance 2 or 4
        # MST needs 3 edges, optimal should be 6
        assert result == 6

    def test_large_distances(self):
        """Test with large coordinate values."""
        points = [[0, 0], [1000, 1000], [2000, 0]]
        result = self.solution.minCostConnectPoints(points)
        # MST: (0,0)-(2000,0) cost 2000, (0,0)-(1000,1000) cost 2000
        # Total: 4000
        assert result == 4000

    def test_collinear_points(self):
        """Test with multiple collinear points."""
        points = [[0, 0], [1, 1], [2, 2], [3, 3], [4, 4]]
        result = self.solution.minCostConnectPoints(points)
        # Connect consecutive points: 2 + 2 + 2 + 2 = 8
        assert result == 8

    def test_star_pattern(self):
        """Test star pattern with center point."""
        points = [[0, 0], [1, 0], [-1, 0], [0, 1], [0, -1]]
        result = self.solution.minCostConnectPoints(points)
        # Center at (0,0) connected to all others: 1 + 1 + 1 + 1 = 4
        assert result == 4

    def test_duplicate_points(self):
        """Test with duplicate points."""
        points = [[1, 1], [1, 1], [2, 2]]
        result = self.solution.minCostConnectPoints(points)
        # Two points at (1,1) can be connected with 0 cost
        # Then connect to (2,2) with cost 2
        assert result == 2

    def test_grid_pattern(self):
        """Test 3x3 grid pattern."""
        points = []
        for i in range(3):
            for j in range(3):
                points.append([i, j])
        
        result = self.solution.minCostConnectPoints(points)
        # 9 points need 8 edges, each with cost 1
        assert result == 8

    def test_random_pattern(self):
        """Test with random-looking pattern."""
        points = [[1, 3], [3, 1], [1, 1], [3, 3], [2, 2]]
        result = self.solution.minCostConnectPoints(points)
        # Should find optimal MST
        assert result <= 8  # Upper bound check

    def test_performance_larger_input(self):
        """Test with larger input for performance."""
        # Create 20 points in a line
        points = [[i, 0] for i in range(20)]
        result = self.solution.minCostConnectPoints(points)
        # Should connect consecutive points: 19 edges of cost 1
        assert result == 19

    def test_l_shape_pattern(self):
        """Test L-shaped point arrangement."""
        points = [[0, 0], [1, 0], [2, 0], [0, 1], [0, 2]]
        result = self.solution.minCostConnectPoints(points)
        # Optimal: connect along the L shape
        assert result == 4

    def test_cross_pattern(self):
        """Test cross/plus pattern."""
        points = [[0, 1], [1, 0], [1, 1], [1, 2], [2, 1]]
        result = self.solution.minCostConnectPoints(points)
        # Center at (1,1) connected to all others
        assert result == 4

    def test_circle_approximation(self):
        """Test points roughly in a circle."""
        points = [[1, 0], [0, 1], [-1, 0], [0, -1], [0, 0]]
        result = self.solution.minCostConnectPoints(points)
        # Center point should be optimal
        assert result == 4

    def test_manhattan_distance_properties(self):
        """Test Manhattan distance calculations."""
        points = [[0, 0], [3, 4]]
        result = self.solution.minCostConnectPoints(points)
        # Manhattan distance: |0-3| + |0-4| = 7
        assert result == 7

    def test_optimal_vs_non_optimal(self):
        """Test to ensure MST vs non-optimal solutions."""
        points = [[0, 0], [1, 0], [2, 0], [1, 1]]
        result = self.solution.minCostConnectPoints(points)
        # MST should be 3, not 4 (if we connected non-optimally)
        assert result == 3

    def test_asymmetric_pattern(self):
        """Test asymmetric point arrangement."""
        points = [[0, 0], [10, 0], [0, 10], [1, 1]]
        result = self.solution.minCostConnectPoints(points)
        # Should find optimal path
        assert result <= 22  # Upper bound check

    def test_edge_case_very_close_points(self):
        """Test points very close to each other."""
        points = [[0, 0], [0, 1], [1, 0], [1, 1]]
        result = self.solution.minCostConnectPoints(points)
        # Unit square: 3 edges of cost 1
        assert result == 3


if __name__ == '__main__':
    pytest.main([__file__])
