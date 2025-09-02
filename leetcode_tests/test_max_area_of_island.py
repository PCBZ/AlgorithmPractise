"""
Comprehensive tests for Max Area of Island problem.

Tests all three implementations: DFS recursive, iterative, and non-destructive.
"""
import copy
import pytest

from leetcode.max_area_of_islend import Solution


class TestMaxAreaOfIsland:
    """Test class for max area of island implementations."""

    def setup_method(self):
        """Set up test fixtures before each test method."""
        self.solution = Solution()

    @pytest.fixture
    def example_grid(self):
        """LeetCode example grid with maximum area of 6."""
        return [
            [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
            [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
            [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]
        ]

    @pytest.fixture
    def small_grid(self):
        """Small test grid."""
        return [
            [1, 1, 0],
            [0, 1, 0],
            [0, 0, 1]
        ]

    @pytest.fixture
    def empty_grid(self):
        """Grid with no islands."""
        return [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]
        ]

    @pytest.fixture
    def single_cell_grid(self):
        """Single cell grid."""
        return [[1]]

    @pytest.fixture
    def all_land_grid(self):
        """Grid that is all land."""
        return [
            [1, 1, 1],
            [1, 1, 1],
            [1, 1, 1]
        ]

    def test_max_area_example_grid(self, example_grid):
        """Test with LeetCode example grid."""
        grid_copy = copy.deepcopy(example_grid)
        result = self.solution.max_area_of_island(grid_copy)
        assert result == 6

    def test_max_area_small_grid(self, small_grid):
        """Test with small grid containing two islands."""
        grid_copy = copy.deepcopy(small_grid)
        result = self.solution.max_area_of_island(grid_copy)
        assert result == 3  # Largest island has area 3

    def test_max_area_empty_grid(self, empty_grid):
        """Test with grid containing no islands."""
        grid_copy = copy.deepcopy(empty_grid)
        result = self.solution.max_area_of_island(grid_copy)
        assert result == 0

    def test_max_area_single_cell(self, single_cell_grid):
        """Test with single cell island."""
        grid_copy = copy.deepcopy(single_cell_grid)
        result = self.solution.max_area_of_island(grid_copy)
        assert result == 1

    def test_max_area_all_land(self, all_land_grid):
        """Test with grid that is all land."""
        grid_copy = copy.deepcopy(all_land_grid)
        result = self.solution.max_area_of_island(grid_copy)
        assert result == 9

    def test_max_area_single_row(self):
        """Test with single row grid."""
        grid = [[1, 0, 1, 1, 0, 1]]
        result = self.solution.max_area_of_island(grid)
        assert result == 2  # Two consecutive 1s

    def test_max_area_single_column(self):
        """Test with single column grid."""
        grid = [[1], [0], [1], [1], [0]]
        result = self.solution.max_area_of_island(grid)
        assert result == 2  # Two consecutive 1s

    def test_max_area_l_shaped_island(self):
        """Test with L-shaped island."""
        grid = [
            [1, 1, 0],
            [1, 0, 0],
            [1, 0, 0]
        ]
        result = self.solution.max_area_of_island(grid)
        assert result == 4

    def test_max_area_diagonal_islands(self):
        """Test islands connected only diagonally (should be separate)."""
        grid = [
            [1, 0, 1],
            [0, 1, 0],
            [1, 0, 1]
        ]
        result = self.solution.max_area_of_island(grid)
        assert result == 1  # All islands have area 1

    def test_max_area_iterative_example_grid(self, example_grid):
        """Test iterative implementation with example grid."""
        grid_copy = copy.deepcopy(example_grid)
        result = self.solution.max_area_of_island_iterative(grid_copy)
        assert result == 6

    def test_max_area_iterative_small_grid(self, small_grid):
        """Test iterative implementation with small grid."""
        grid_copy = copy.deepcopy(small_grid)
        result = self.solution.max_area_of_island_iterative(grid_copy)
        assert result == 3

    def test_max_area_iterative_empty_grid(self, empty_grid):
        """Test iterative implementation with empty grid."""
        grid_copy = copy.deepcopy(empty_grid)
        result = self.solution.max_area_of_island_iterative(grid_copy)
        assert result == 0

    def test_max_area_iterative_all_land(self, all_land_grid):
        """Test iterative implementation with all land."""
        grid_copy = copy.deepcopy(all_land_grid)
        result = self.solution.max_area_of_island_iterative(grid_copy)
        assert result == 9

    def test_max_area_non_destructive_example_grid(self, example_grid):
        """Test non-destructive implementation with example grid."""
        grid_copy = copy.deepcopy(example_grid)
        original = copy.deepcopy(example_grid)
        result = self.solution.max_area_of_island_non_destructive(grid_copy)
        assert result == 6
        assert grid_copy == original  # Grid should be unchanged

    def test_max_area_non_destructive_small_grid(self, small_grid):
        """Test non-destructive implementation with small grid."""
        grid_copy = copy.deepcopy(small_grid)
        original = copy.deepcopy(small_grid)
        result = self.solution.max_area_of_island_non_destructive(grid_copy)
        assert result == 3
        assert grid_copy == original

    def test_max_area_non_destructive_preserves_grid(self):
        """Test that non-destructive version preserves original grid."""
        grid = [[1, 1, 0], [1, 0, 1]]
        original = copy.deepcopy(grid)
        self.solution.max_area_of_island_non_destructive(grid)
        assert grid == original

    def test_all_implementations_consistency(self, example_grid):
        """Test that all three implementations give same results."""
        grid1 = copy.deepcopy(example_grid)
        grid2 = copy.deepcopy(example_grid)
        grid3 = copy.deepcopy(example_grid)

        result1 = self.solution.max_area_of_island(grid1)
        result2 = self.solution.max_area_of_island_iterative(grid2)
        result3 = self.solution.max_area_of_island_non_destructive(grid3)

        assert result1 == result2 == result3 == 6

    def test_edge_cases_empty_input(self):
        """Test edge cases with empty input."""
        assert self.solution.max_area_of_island([]) == 0
        assert self.solution.max_area_of_island([[]]) == 0
        assert self.solution.max_area_of_island_iterative([]) == 0
        assert self.solution.max_area_of_island_iterative([[]]) == 0
        assert self.solution.max_area_of_island_non_destructive([]) == 0
        assert self.solution.max_area_of_island_non_destructive([[]]) == 0

    def test_large_single_island(self):
        """Test with a large single island."""
        grid = [[1] * 5 for _ in range(4)]  # 4x5 grid of all 1s
        expected_area = 20

        grid1 = copy.deepcopy(grid)
        grid2 = copy.deepcopy(grid)
        grid3 = copy.deepcopy(grid)

        assert self.solution.max_area_of_island(grid1) == expected_area
        assert self.solution.max_area_of_island_iterative(grid2) == expected_area
        assert self.solution.max_area_of_island_non_destructive(grid3) == expected_area

    def test_multiple_equal_islands(self):
        """Test with multiple islands of equal maximum area."""
        grid = [
            [1, 1, 0, 1, 1],
            [1, 1, 0, 1, 1],
            [0, 0, 0, 0, 0],
            [1, 1, 0, 0, 0],
            [1, 1, 0, 0, 0]
        ]
        # Two islands of area 4 each, one of area 4
        expected_area = 4

        grid1 = copy.deepcopy(grid)
        grid2 = copy.deepcopy(grid)
        grid3 = copy.deepcopy(grid)

        assert self.solution.max_area_of_island(grid1) == expected_area
        assert self.solution.max_area_of_island_iterative(grid2) == expected_area
        assert self.solution.max_area_of_island_non_destructive(grid3) == expected_area

    def test_count_islands_functionality(self):
        """Test the bonus count_islands method."""
        grid = [
            [1, 1, 0, 0, 0],
            [1, 1, 0, 0, 0],
            [0, 0, 1, 0, 0],
            [0, 0, 0, 1, 1]
        ]
        # Should have 3 islands
        grid_copy = copy.deepcopy(grid)
        result = self.solution.count_islands(grid_copy)
        assert result == 3

    def test_complex_shape_island(self):
        """Test with complex shaped island."""
        grid = [
            [1, 0, 1, 1, 0],
            [1, 0, 0, 1, 0],
            [1, 1, 1, 1, 0],
            [0, 0, 0, 0, 0],
            [1, 1, 0, 1, 1]
        ]
        # The large connected island has area 9 (connected via row 2)
        expected_area = 9

        grid1 = copy.deepcopy(grid)
        grid2 = copy.deepcopy(grid)
        grid3 = copy.deepcopy(grid)

        assert self.solution.max_area_of_island(grid1) == expected_area
        assert self.solution.max_area_of_island_iterative(grid2) == expected_area
        assert self.solution.max_area_of_island_non_destructive(grid3) == expected_area

    def test_boundary_conditions(self):
        """Test islands at grid boundaries."""
        grid = [
            [1, 0, 0, 0, 1],
            [0, 0, 1, 0, 0],
            [0, 0, 1, 0, 0],
            [0, 0, 1, 0, 0],
            [1, 0, 0, 0, 1]
        ]
        # Largest island (vertical line) has area 3
        expected_area = 3

        grid1 = copy.deepcopy(grid)
        grid2 = copy.deepcopy(grid)
        grid3 = copy.deepcopy(grid)

        assert self.solution.max_area_of_island(grid1) == expected_area
        assert self.solution.max_area_of_island_iterative(grid2) == expected_area
        assert self.solution.max_area_of_island_non_destructive(grid3) == expected_area


if __name__ == "__main__":
    pytest.main([__file__])
