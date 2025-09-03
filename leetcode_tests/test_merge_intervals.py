"""
Comprehensive tests for Merge Intervals problem.

Tests the solution for merging overlapping intervals with various edge cases.
"""
import pytest
import sys
import os

# Add parent directory to path for imports
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from leetcode.merge_intervals import Solution


class TestMergeIntervals:
    """Test class for merge intervals implementation."""

    def setup_method(self):
        """Set up test fixtures before each test method."""
        self.solution = Solution()

    @pytest.fixture
    def leetcode_example_1(self):
        """First LeetCode example."""
        return [[1, 3], [2, 6], [8, 10], [15, 18]]

    @pytest.fixture
    def leetcode_example_2(self):
        """Second LeetCode example."""
        return [[1, 4], [4, 5]]

    def test_leetcode_example_1(self, leetcode_example_1):
        """Test first LeetCode example."""
        expected = [[1, 6], [8, 10], [15, 18]]
        result = self.solution.merge(leetcode_example_1)
        assert result == expected

    def test_leetcode_example_2(self, leetcode_example_2):
        """Test second LeetCode example."""
        expected = [[1, 5]]
        result = self.solution.merge(leetcode_example_2)
        assert result == expected

    def test_empty_intervals(self):
        """Test empty input."""
        result = self.solution.merge([])
        assert result == []

    def test_single_interval(self):
        """Test single interval input."""
        intervals = [[1, 4]]
        result = self.solution.merge(intervals)
        assert result == [[1, 4]]

    def test_no_overlap(self):
        """Test intervals with no overlaps."""
        intervals = [[1, 2], [3, 4], [5, 6]]
        expected = [[1, 2], [3, 4], [5, 6]]
        result = self.solution.merge(intervals)
        assert result == expected

    def test_complete_overlap(self):
        """Test one interval completely contains another."""
        intervals = [[1, 5], [2, 3]]
        expected = [[1, 5]]
        result = self.solution.merge(intervals)
        assert result == expected

    def test_partial_overlap(self):
        """Test intervals with partial overlap."""
        intervals = [[1, 3], [2, 4]]
        expected = [[1, 4]]
        result = self.solution.merge(intervals)
        assert result == expected

    def test_touching_intervals(self):
        """Test intervals that touch at endpoints."""
        intervals = [[1, 4], [4, 5]]
        expected = [[1, 5]]
        result = self.solution.merge(intervals)
        assert result == expected

    def test_identical_intervals(self):
        """Test identical intervals."""
        intervals = [[1, 3], [1, 3]]
        expected = [[1, 3]]
        result = self.solution.merge(intervals)
        assert result == expected

    def test_multiple_merges(self):
        """Test multiple consecutive merges."""
        intervals = [[1, 3], [2, 4], [3, 5], [4, 6]]
        expected = [[1, 6]]
        result = self.solution.merge(intervals)
        assert result == expected

    def test_unsorted_input(self):
        """Test with unsorted intervals."""
        intervals = [[8, 10], [1, 3], [15, 18], [2, 6]]
        expected = [[1, 6], [8, 10], [15, 18]]
        result = self.solution.merge(intervals)
        assert result == expected

    def test_large_numbers(self):
        """Test with large numbers."""
        intervals = [[1000000, 2000000], [1500000, 3000000]]
        expected = [[1000000, 3000000]]
        result = self.solution.merge(intervals)
        assert result == expected

    def test_negative_numbers(self):
        """Test with negative numbers."""
        intervals = [[-3, -1], [-2, 1], [0, 3]]
        expected = [[-3, 3]]
        result = self.solution.merge(intervals)
        assert result == expected

    def test_zero_interval(self):
        """Test intervals containing zero."""
        intervals = [[-1, 0], [0, 1]]
        expected = [[-1, 1]]
        result = self.solution.merge(intervals)
        assert result == expected

    def test_point_intervals(self):
        """Test intervals that are single points."""
        intervals = [[1, 1], [2, 2], [3, 3]]
        expected = [[1, 1], [2, 2], [3, 3]]
        result = self.solution.merge(intervals)
        assert result == expected

    def test_overlapping_points(self):
        """Test overlapping point intervals."""
        intervals = [[1, 1], [1, 1], [1, 2]]
        expected = [[1, 2]]
        result = self.solution.merge(intervals)
        assert result == expected

    def test_complex_case_1(self):
        """Test complex overlapping scenario."""
        intervals = [[1, 4], [0, 4]]
        expected = [[0, 4]]
        result = self.solution.merge(intervals)
        assert result == expected

    def test_complex_case_2(self):
        """Test another complex scenario."""
        intervals = [[1, 4], [0, 2], [3, 5]]
        expected = [[0, 5]]
        result = self.solution.merge(intervals)
        assert result == expected

    def test_many_intervals(self):
        """Test with many intervals."""
        intervals = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6]]
        expected = [[1, 6]]
        result = self.solution.merge(intervals)
        assert result == expected

    def test_alternating_pattern(self):
        """Test alternating overlap pattern."""
        intervals = [[1, 3], [4, 6], [2, 5], [7, 9]]
        expected = [[1, 6], [7, 9]]
        result = self.solution.merge(intervals)
        assert result == expected

    def test_nested_intervals(self):
        """Test nested intervals."""
        intervals = [[1, 10], [2, 3], [4, 5], [6, 7], [8, 9]]
        expected = [[1, 10]]
        result = self.solution.merge(intervals)
        assert result == expected

    def test_gaps_between_intervals(self):
        """Test intervals with gaps."""
        intervals = [[1, 2], [4, 5], [7, 8]]
        expected = [[1, 2], [4, 5], [7, 8]]
        result = self.solution.merge(intervals)
        assert result == expected

    def test_reverse_order(self):
        """Test intervals in reverse order."""
        intervals = [[15, 18], [8, 10], [2, 6], [1, 3]]
        expected = [[1, 6], [8, 10], [15, 18]]
        result = self.solution.merge(intervals)
        assert result == expected

    def test_performance_large_input(self):
        """Test with larger input for performance."""
        # Create 100 intervals with some overlaps
        intervals = []
        for i in range(0, 100, 2):
            intervals.append([i, i + 3])
        
        result = self.solution.merge(intervals)
        
        # Should merge many intervals
        assert len(result) < len(intervals)
        
        # Check result is sorted and non-overlapping
        for i in range(len(result) - 1):
            assert result[i][1] < result[i + 1][0]


if __name__ == '__main__':
    pytest.main([__file__])
