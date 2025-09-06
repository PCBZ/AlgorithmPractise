"""
Test cases for LeetCode Problem 947: Most Stones Removed with Same Row or Column.
"""

import pytest
from leetcode.most_stones_removed_with_same_row_or_column import Solution


class TestMostStonesRemoved:
    """Test class for most stones removed problem."""

    def setup_method(self):
        """Set up test fixtures."""
        self.solution = Solution()

    @pytest.mark.parametrize("stones,expected", [
        # Basic test cases from LeetCode examples
        ([[0, 0], [0, 1], [1, 0], [1, 2], [2, 1], [2, 2]], 5),
        ([[0, 0], [0, 2], [1, 1], [2, 0], [2, 2]], 3),
        ([[0, 0]], 0),
        
        # Edge cases
        ([], 0),  # No stones
        ([[1, 1]], 0),  # Single stone
        
        # Two stones cases
        ([[0, 0], [0, 1]], 1),  # Same row
        ([[0, 0], [1, 0]], 1),  # Same column
        ([[0, 0], [1, 1]], 0),  # Different row and column
        
        # Linear arrangements
        ([[0, 0], [0, 1], [0, 2]], 2),  # Horizontal line
        ([[0, 0], [1, 0], [2, 0]], 2),  # Vertical line
        
        # Complex connected components
        ([[0, 0], [0, 1], [1, 0], [1, 1]], 3),  # 2x2 square
        ([[0, 0], [1, 1], [2, 2]], 0),  # Diagonal (no connections)
        
        # Multiple disconnected components
        ([[0, 0], [0, 1], [2, 2], [2, 3]], 2),  # Two separate pairs
        
        # Large coordinates
        ([[1000, 1000], [1000, 1001], [1001, 1000]], 2),
        
        # Mixed positive coordinates
        ([[5, 9], [9, 0], [0, 0], [7, 0], [4, 3], [8, 5], [5, 8], [1, 1]], 3),
    ])
    def test_remove_stones(self, stones, expected):
        """Test removeStones with various inputs."""
        result = self.solution.removeStones(stones)
        assert result == expected, f"Failed for {stones}: expected {expected}, got {result}"

    def test_single_row_multiple_stones(self):
        """Test with multiple stones in same row."""
        stones = [[0, 0], [0, 1], [0, 2], [0, 3], [0, 4]]
        result = self.solution.removeStones(stones)
        # Can remove 4 out of 5 stones (leave one)
        assert result == 4

    def test_single_column_multiple_stones(self):
        """Test with multiple stones in same column."""
        stones = [[0, 5], [1, 5], [2, 5], [3, 5]]
        result = self.solution.removeStones(stones)
        # Can remove 3 out of 4 stones (leave one)
        assert result == 3

    def test_cross_pattern(self):
        """Test cross pattern where stones share center."""
        stones = [[1, 0], [1, 1], [1, 2], [0, 1], [2, 1]]
        result = self.solution.removeStones(stones)
        # All stones are connected through center stone
        assert result == 4

    def test_l_shape_pattern(self):
        """Test L-shaped pattern."""
        stones = [[0, 0], [0, 1], [0, 2], [1, 0], [2, 0]]
        result = self.solution.removeStones(stones)
        # All connected through (0,0)
        assert result == 4

    def test_disconnected_groups(self):
        """Test multiple disconnected groups."""
        stones = [
            # Group 1: connected via row 0
            [0, 0], [0, 1], [1, 0],
            # Group 2: connected via column 5
            [2, 5], [3, 5],
            # Group 3: isolated
            [10, 10]
        ]
        result = self.solution.removeStones(stones)
        # Group 1: remove 2, Group 2: remove 1, Group 3: remove 0
        assert result == 3

    def test_grid_pattern(self):
        """Test grid pattern where all stones are connected."""
        stones = [[0, 0], [0, 1], [1, 0], [1, 1], [2, 0], [2, 1]]
        result = self.solution.removeStones(stones)
        # All stones connected through shared rows/columns
        assert result == 5

    def test_large_input_performance(self):
        """Test with larger input to check performance."""
        # Create a 10x10 grid pattern
        stones = [[i, j] for i in range(10) for j in range(10)]
        result = self.solution.removeStones(stones)
        # All 100 stones are connected, can remove 99
        assert result == 99

    def test_sparse_large_coordinates(self):
        """Test with sparse stones at large coordinates."""
        stones = [[0, 0], [1000000, 0], [0, 1000000]]
        result = self.solution.removeStones(stones)
        # All connected through shared row/column 0
        assert result == 2

    def test_return_type(self):
        """Test that return type is correct integer."""
        stones = [[0, 0], [0, 1]]
        result = self.solution.removeStones(stones)
        assert isinstance(result, int)
        assert result >= 0

    def test_input_unchanged(self):
        """Test that input stones array is not modified."""
        stones = [[0, 0], [0, 1], [1, 0]]
        original_stones = [stone[:] for stone in stones]  # Deep copy
        
        self.solution.removeStones(stones)
        
        assert stones == original_stones, "Input was modified"

    def test_edge_case_max_removable(self):
        """Test that we never remove more than n-1 stones."""
        test_cases = [
            [[0, 0], [0, 1]],                    # 2 stones
            [[0, 0], [0, 1], [0, 2]],            # 3 stones
            [[0, 0], [0, 1], [1, 0], [1, 1]],    # 4 stones
        ]
        
        for stones in test_cases:
            result = self.solution.removeStones(stones)
            # Can never remove more than n-1 stones
            assert result <= len(stones) - 1, f"Removed too many stones for {stones}"

    def test_isolated_stones(self):
        """Test with completely isolated stones."""
        stones = [[0, 0], [2, 3], [5, 7], [10, 15]]
        result = self.solution.removeStones(stones)
        # No stones share row or column, can't remove any
        assert result == 0

    def test_boundary_coordinates(self):
        """Test with boundary coordinate values."""
        stones = [[0, 0], [0, 10000], [10000, 0]]
        result = self.solution.removeStones(stones)
        # All connected through row/column 0
        assert result == 2

    def test_duplicate_check_not_needed(self):
        """Test assumes no duplicate stones per problem constraints."""
        # Problem states each coordinate has at most one stone
        stones = [[1, 1], [1, 2], [2, 1]]
        result = self.solution.removeStones(stones)
        assert result == 2

    def test_complex_connectivity(self):
        """Test complex connectivity patterns."""
        stones = [
            [0, 1], [0, 2],      # Row 0 group
            [1, 0], [2, 0],      # Column 0 group  
            [1, 3], [3, 1],      # Connected through (1,0) and (0,1)
            [5, 5]               # Isolated
        ]
        result = self.solution.removeStones(stones)
        # Forms 3 components: {(0,1),(0,2),(3,1)}, {(1,0),(2,0),(1,3)}, {(5,5)}
        assert result == 4
