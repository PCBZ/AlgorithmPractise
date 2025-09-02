

import pytest
from leetcode.swim_in_rising_water import Solution


class TestSwimInRisingWater:
    def setup_method(self):
        """Set up test fixtures before each test method."""
        self.solution = Solution()

    def test_basic_case(self):
        """Test the basic example case."""
        grid = [[0, 2], [1, 3]]
        expected = 3
        assert self.solution.swimInWater(grid) == expected

    def test_single_cell(self):
        """Test with a single cell grid."""
        grid = [[0]]
        expected = 0
        assert self.solution.swimInWater(grid) == expected

    def test_already_at_destination(self):
        """Test when start and end are the same (1x1 grid)."""
        grid = [[5]]
        expected = 5
        assert self.solution.swimInWater(grid) == expected

    def test_larger_grid(self):
        """Test with a larger 3x3 grid."""
        grid = [
            [0, 1, 2, 3, 4],
            [24, 23, 22, 21, 5],
            [12, 13, 14, 15, 16],
            [11, 17, 18, 19, 20],
            [10, 9, 8, 7, 6]
        ]
        expected = 16
        assert self.solution.swimInWater(grid) == expected

    def test_straight_path(self):
        """Test when the optimal path is straight."""
        grid = [
            [0, 1, 2],
            [9, 8, 3],
            [7, 6, 4]
        ]
        expected = 4
        assert self.solution.swimInWater(grid) == expected

    def test_high_start_value(self):
        """Test when the starting position has a high value."""
        grid = [
            [10, 1],
            [2, 0]
        ]
        expected = 10
        assert self.solution.swimInWater(grid) == expected

    def test_monotonic_increasing(self):
        """Test with monotonically increasing values."""
        grid = [
            [0, 1],
            [2, 3]
        ]
        expected = 3
        assert self.solution.swimInWater(grid) == expected

    def test_need_to_wait(self):
        """Test case where we need to wait for water level to rise."""
        grid = [
            [0, 2],
            [1, 100]
        ]
        expected = 100
        assert self.solution.swimInWater(grid) == expected

    def test_complex_path(self):
        """Test with a more complex grid requiring careful pathfinding."""
        grid = [
            [3, 2, 1],
            [6, 5, 4],
            [9, 8, 7]
        ]
        expected = 7
        assert self.solution.swimInWater(grid) == expected

    @pytest.mark.parametrize("grid,expected", [
        ([[0, 2], [1, 3]], 3),
        ([[0]], 0),
        ([[5, 4], [3, 2]], 5),
        ([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 9)
    ])
    def test_parametrized_cases(self, grid, expected):
        """Test multiple cases using parametrization."""
        assert self.solution.swimInWater(grid) == expected


if __name__ == "__main__":
    pytest.main([__file__])
