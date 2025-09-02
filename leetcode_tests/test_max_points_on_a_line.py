"""
Comprehensive tests for Max Points on a Line problem.

Tests the slope-based solution for finding maximum collinear points.
"""
import pytest
import sys
import os

# Add parent directory to path for imports
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from leetcode.max_points_on_a_line import Solution


class TestMaxPointsOnALine:
    """Test class for max points on a line implementation."""

    def setup_method(self):
        """Set up test fixtures before each test method."""
        self.solution = Solution()

    @pytest.fixture
    def leetcode_example_1(self):
        """First LeetCode example."""
        return [[1, 1], [2, 2], [3, 3]]

    @pytest.fixture
    def leetcode_example_2(self):
        """Second LeetCode example."""
        return [[1, 1], [3, 2], [5, 3], [4, 1], [2, 3], [1, 4]]

    @pytest.fixture
    def simple_cases(self):
        """Simple test cases."""
        return [
            ([], 0),
            ([[1, 1]], 1),
            ([[1, 1], [2, 2]], 2),
        ]

    @pytest.fixture
    def vertical_line(self):
        """Points on a vertical line."""
        return [[1, 1], [1, 2], [1, 3], [1, 4]]

    @pytest.fixture
    def horizontal_line(self):
        """Points on a horizontal line."""
        return [[1, 1], [2, 1], [3, 1], [4, 1]]

    def test_leetcode_example_1(self, leetcode_example_1):
        """Test first LeetCode example."""
        result = self.solution.maxPoints(leetcode_example_1)
        assert result == 3  # All points on same line

    def test_leetcode_example_2(self, leetcode_example_2):
        """Test second LeetCode example."""
        result = self.solution.maxPoints(leetcode_example_2)
        assert result == 4  # Maximum points on same line

    def test_simple_cases(self, simple_cases):
        """Test simple edge cases."""
        for points, expected in simple_cases:
            result = self.solution.maxPoints(points)
            assert result == expected

    def test_vertical_line(self, vertical_line):
        """Test vertical line (infinite slope)."""
        result = self.solution.maxPoints(vertical_line)
        assert result == 4  # All points on vertical line

    def test_horizontal_line(self, horizontal_line):
        """Test horizontal line (zero slope)."""
        result = self.solution.maxPoints(horizontal_line)
        assert result == 4  # All points on horizontal line

    def test_duplicate_points(self):
        """Test with duplicate points."""
        points = [[1, 1], [1, 1], [2, 2], [2, 2]]
        result = self.solution.maxPoints(points)
        assert result == 4  # All points are effectively on same line

    def test_no_collinear_points(self):
        """Test with no three points collinear."""
        points = [[0, 0], [1, 0], [0, 1]]
        result = self.solution.maxPoints(points)
        assert result == 2  # Maximum is any pair

    def test_mixed_slopes(self):
        """Test with different slopes."""
        points = [[0, 0], [1, 1], [2, 2], [0, 1], [0, 2]]
        result = self.solution.maxPoints(points)
        assert result == 3  # Either diagonal line or vertical line

    def test_negative_coordinates(self):
        """Test with negative coordinates."""
        points = [[-1, -1], [0, 0], [1, 1], [2, 2]]
        result = self.solution.maxPoints(points)
        assert result == 4  # All on same line y = x

    def test_large_coordinates(self):
        """Test with large coordinates."""
        points = [[1000, 1000], [2000, 2000], [3000, 3000]]
        result = self.solution.maxPoints(points)
        assert result == 3  # All on same line

    def test_fractional_slope(self):
        """Test points with fractional slope."""
        points = [[0, 0], [1, 2], [2, 4], [3, 6]]
        result = self.solution.maxPoints(points)
        assert result == 4  # All on line y = 2x

    def test_complex_pattern(self):
        """Test complex pattern with multiple lines."""
        points = [
            [0, 0], [1, 1], [2, 2],  # Line 1: y = x (3 points)
            [0, 1], [1, 2], [2, 3],  # Line 2: y = x + 1 (3 points)
            [0, 2]                    # Additional point
        ]
        result = self.solution.maxPoints(points)
        assert result == 3  # Maximum is 3 points on same line

    def test_star_pattern(self):
        """Test star-like pattern."""
        points = [
            [0, 0],                   # Center
            [1, 0], [-1, 0],         # Horizontal line through center
            [0, 1], [0, -1],         # Vertical line through center
            [1, 1], [-1, -1]         # Diagonal line
        ]
        result = self.solution.maxPoints(points)
        assert result == 3  # Any line through center

    def test_collinear_subset(self):
        """Test where subset of points are collinear."""
        points = [
            [1, 1], [2, 2], [3, 3], [4, 4],  # 4 points on y = x
            [1, 2], [2, 3]                    # 2 points on y = x + 1
        ]
        result = self.solution.maxPoints(points)
        assert result == 4  # Maximum is the first line

    def test_zero_slope_variations(self):
        """Test variations of horizontal lines."""
        points = [[1, 5], [2, 5], [3, 5], [1, 3], [2, 3]]
        result = self.solution.maxPoints(points)
        assert result == 3  # Either horizontal line

    def test_steep_slope(self):
        """Test very steep slope."""
        points = [[0, 0], [1, 100], [2, 200], [3, 300]]
        result = self.solution.maxPoints(points)
        assert result == 4  # All on line y = 100x

    def test_gentle_slope(self):
        """Test very gentle slope."""
        points = [[0, 0], [100, 1], [200, 2], [300, 3]]
        result = self.solution.maxPoints(points)
        assert result == 4  # All on line y = x/100

    def test_precision_edge_case(self):
        """Test case that might cause precision issues."""
        points = [[0, 0], [94911151, 94911150], [94911152, 94911151]]
        result = self.solution.maxPoints(points)
        assert result == 2  # Should handle large numbers correctly

    def test_square_pattern(self):
        """Test square pattern."""
        points = [[0, 0], [0, 1], [1, 0], [1, 1]]
        result = self.solution.maxPoints(points)
        assert result == 2  # No three points collinear

    def test_cross_pattern(self):
        """Test cross pattern."""
        points = [
            [0, 1], [1, 0], [2, 1], [1, 2],  # Cross shape
            [1, 1]                            # Center
        ]
        result = self.solution.maxPoints(points)
        assert result == 3  # Any line through center and two opposite points

    def test_multiple_duplicates(self):
        """Test with multiple duplicate points."""
        points = [[0, 0], [0, 0], [1, 1], [1, 1], [2, 2]]
        result = self.solution.maxPoints(points)
        assert result == 5  # All points on same line considering duplicates

    def test_triangle_pattern(self):
        """Test triangle pattern."""
        points = [[0, 0], [1, 0], [0, 1]]
        result = self.solution.maxPoints(points)
        assert result == 2  # No three points collinear

    def test_performance_case(self):
        """Test performance with more points."""
        # Create a line with many points
        points = [[i, 2*i] for i in range(50)]
        # Add some noise points
        points.extend([[i, 3*i] for i in range(5)])
        
        result = self.solution.maxPoints(points)
        assert result >= 50  # At least the main line


if __name__ == '__main__':
    pytest.main([__file__])
