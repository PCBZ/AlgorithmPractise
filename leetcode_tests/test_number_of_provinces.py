"""
Test cases for LeetCode Problem 547: Number of Provinces.
"""

import pytest
from leetcode.number_of_provinces import Solution


class TestNumberOfProvinces:
    """Test class for number of provinces problem."""

    def setup_method(self):
        """Set up test fixtures."""
        self.solution = Solution()

    @pytest.mark.parametrize("is_connected,expected", [
        # Basic test cases from LeetCode examples
        ([[1, 1, 0], [1, 1, 0], [0, 0, 1]], 2),
        ([[1, 0, 0], [0, 1, 0], [0, 0, 1]], 3),
        
        # Single city
        ([[1]], 1),
        
        # All cities connected
        ([[1, 1, 1], [1, 1, 1], [1, 1, 1]], 1),
        
        # Two cities connected
        ([[1, 1], [1, 1]], 1),
        
        # Two cities disconnected
        ([[1, 0], [0, 1]], 2),
        
        # Chain connection
        ([[1, 1, 0, 0], [1, 1, 1, 0], [0, 1, 1, 0], [0, 0, 0, 1]], 2),
        
        # Star pattern (one center connected to all)
        ([[1, 1, 1, 1], [1, 1, 0, 0], [1, 0, 1, 0], [1, 0, 0, 1]], 1),
        
        # Complex pattern
        ([[1, 0, 0, 1], [0, 1, 1, 0], [0, 1, 1, 1], [1, 0, 1, 1]], 1),
        
        # Multiple small groups
        ([[1, 1, 0, 0, 0], [1, 1, 0, 0, 0], [0, 0, 1, 1, 0], [0, 0, 1, 1, 0], [0, 0, 0, 0, 1]], 3),
    ])
    def test_find_circle_num(self, is_connected, expected):
        """Test findCircleNum with various inputs."""
        result = self.solution.findCircleNum(is_connected)
        assert result == expected, f"Failed for {is_connected}: expected {expected}, got {result}"

    def test_single_city(self):
        """Test with single city."""
        is_connected = [[1]]
        result = self.solution.findCircleNum(is_connected)
        assert result == 1

    def test_two_cities_connected(self):
        """Test with two connected cities."""
        is_connected = [[1, 1], [1, 1]]
        result = self.solution.findCircleNum(is_connected)
        assert result == 1

    def test_two_cities_disconnected(self):
        """Test with two disconnected cities."""
        is_connected = [[1, 0], [0, 1]]
        result = self.solution.findCircleNum(is_connected)
        assert result == 2

    def test_all_cities_connected(self):
        """Test when all cities form one province."""
        # Complete graph of size 4
        is_connected = [
            [1, 1, 1, 1],
            [1, 1, 1, 1],
            [1, 1, 1, 1],
            [1, 1, 1, 1]
        ]
        result = self.solution.findCircleNum(is_connected)
        assert result == 1

    def test_all_cities_isolated(self):
        """Test when no cities are connected."""
        # Identity matrix (only diagonal is 1)
        is_connected = [
            [1, 0, 0, 0],
            [0, 1, 0, 0],
            [0, 0, 1, 0],
            [0, 0, 0, 1]
        ]
        result = self.solution.findCircleNum(is_connected)
        assert result == 4

    def test_linear_connection(self):
        """Test linear chain of connections."""
        # Cities connected in a chain: 0-1-2-3
        is_connected = [
            [1, 1, 0, 0],
            [1, 1, 1, 0],
            [0, 1, 1, 1],
            [0, 0, 1, 1]
        ]
        result = self.solution.findCircleNum(is_connected)
        assert result == 1

    def test_multiple_components(self):
        """Test multiple separate components."""
        # Two separate pairs: (0,1) and (2,3)
        is_connected = [
            [1, 1, 0, 0],
            [1, 1, 0, 0],
            [0, 0, 1, 1],
            [0, 0, 1, 1]
        ]
        result = self.solution.findCircleNum(is_connected)
        assert result == 2

    def test_symmetric_matrix_property(self):
        """Test that function works correctly with symmetric matrix."""
        # The adjacency matrix should be symmetric
        is_connected = [
            [1, 1, 0, 1],
            [1, 1, 1, 0],
            [0, 1, 1, 0],
            [1, 0, 0, 1]
        ]
        result = self.solution.findCircleNum(is_connected)
        # All cities are connected through various paths
        assert result == 1

    def test_large_input_performance(self):
        """Test with larger input to check basic performance."""
        n = 20
        # Create identity matrix (all isolated)
        is_connected = [[1 if i == j else 0 for j in range(n)] for i in range(n)]
        result = self.solution.findCircleNum(is_connected)
        assert result == n  # Each city is its own province

    def test_large_connected_component(self):
        """Test with one large connected component."""
        n = 15
        # Create complete graph (all connected to all)
        is_connected = [[1 for _ in range(n)] for _ in range(n)]
        result = self.solution.findCircleNum(is_connected)
        assert result == 1  # All cities in one province

    def test_return_type(self):
        """Test that return type is correct integer."""
        is_connected = [[1, 0], [0, 1]]
        result = self.solution.findCircleNum(is_connected)
        assert isinstance(result, int)
        assert result >= 1

    def test_input_unchanged(self):
        """Test that input matrix is not modified."""
        is_connected = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
        original = [row[:] for row in is_connected]  # Deep copy
        
        self.solution.findCircleNum(is_connected)
        
        assert is_connected == original, "Input matrix was modified"

    def test_diagonal_always_one(self):
        """Test assumes diagonal elements are always 1 (city connected to itself)."""
        is_connected = [[1, 0, 1], [0, 1, 1], [1, 1, 1]]
        result = self.solution.findCircleNum(is_connected)
        # Cities 0 and 2 connected, city 1 connected to 2, so all form one province
        assert result == 1

    def test_triangle_pattern(self):
        """Test triangle connection pattern."""
        # Triangle: 0-1, 1-2, 2-0
        is_connected = [
            [1, 1, 1],
            [1, 1, 1],
            [1, 1, 1]
        ]
        result = self.solution.findCircleNum(is_connected)
        assert result == 1

    def test_disconnected_pairs(self):
        """Test multiple disconnected pairs."""
        # Pairs: (0,1), (2,3), (4,5)
        is_connected = [
            [1, 1, 0, 0, 0, 0],
            [1, 1, 0, 0, 0, 0],
            [0, 0, 1, 1, 0, 0],
            [0, 0, 1, 1, 0, 0],
            [0, 0, 0, 0, 1, 1],
            [0, 0, 0, 0, 1, 1]
        ]
        result = self.solution.findCircleNum(is_connected)
        assert result == 3

    def test_mixed_connectivity(self):
        """Test mixed connectivity with isolated and connected cities."""
        # One large component (0,1,2,3) and two isolated cities (4,5)
        is_connected = [
            [1, 1, 0, 1, 0, 0],  # 0 connected to 1,3
            [1, 1, 1, 0, 0, 0],  # 1 connected to 0,2
            [0, 1, 1, 1, 0, 0],  # 2 connected to 1,3
            [1, 0, 1, 1, 0, 0],  # 3 connected to 0,2
            [0, 0, 0, 0, 1, 0],  # 4 isolated
            [0, 0, 0, 0, 0, 1]   # 5 isolated
        ]
        result = self.solution.findCircleNum(is_connected)
        assert result == 3  # One component of size 4, two components of size 1

    def test_boundary_conditions(self):
        """Test boundary conditions and edge cases."""
        # Minimum case: 2x2 with different patterns
        test_cases = [
            ([[1, 0], [0, 1]], 2),  # No connection
            ([[1, 1], [1, 1]], 1),  # Full connection
        ]
        
        for matrix, expected in test_cases:
            result = self.solution.findCircleNum(matrix)
            assert result == expected, f"Failed for {matrix}"
