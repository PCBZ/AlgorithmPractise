"""
Comprehensive test suite for LeetCode Problem #57: Insert Interval
Tests the interval insertion and merging algorithm with various scenarios.
"""

import pytest

from leetcode.insert_interval import Solution


class TestInsertInterval:
    """Test cases for Insert Interval problem."""

    def setup_method(self):
        """Set up test fixtures before each test method."""
        self.solution = Solution()

    def test_basic_merge_case(self):
        """Test basic merging of overlapping intervals."""
        intervals = [[1, 3], [6, 9]]
        new_interval = [2, 5]
        expected = [[1, 5], [6, 9]]
        assert self.solution.insert(intervals, new_interval) == expected

    def test_multiple_merges(self):
        """Test merging with multiple overlapping intervals."""
        intervals = [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]]
        new_interval = [4, 8]
        expected = [[1, 2], [3, 10], [12, 16]]
        assert self.solution.insert(intervals, new_interval) == expected

    def test_empty_intervals(self):
        """Test insertion into empty interval list."""
        intervals = []
        new_interval = [5, 7]
        expected = [[5, 7]]
        assert self.solution.insert(intervals, new_interval) == expected

    def test_single_interval_no_overlap(self):
        """Test insertion with single interval, no overlap."""
        intervals = [[1, 5]]
        new_interval = [6, 8]
        expected = [[1, 5], [6, 8]]
        assert self.solution.insert(intervals, new_interval) == expected

    def test_single_interval_complete_overlap(self):
        """Test new interval completely overlaps existing."""
        intervals = [[1, 5]]
        new_interval = [2, 3]
        expected = [[1, 5]]
        assert self.solution.insert(intervals, new_interval) == expected

    def test_new_interval_encompasses_all(self):
        """Test new interval encompasses all existing intervals."""
        intervals = [[1, 2], [3, 5], [6, 7]]
        new_interval = [0, 10]
        expected = [[0, 10]]
        assert self.solution.insert(intervals, new_interval) == expected

    def test_insert_at_beginning(self):
        """Test insertion at the beginning with no overlap."""
        intervals = [[3, 5], [6, 9]]
        new_interval = [1, 2]
        expected = [[1, 2], [3, 5], [6, 9]]
        assert self.solution.insert(intervals, new_interval) == expected

    def test_insert_at_end(self):
        """Test insertion at the end with no overlap."""
        intervals = [[1, 3], [6, 9]]
        new_interval = [10, 12]
        expected = [[1, 3], [6, 9], [10, 12]]
        assert self.solution.insert(intervals, new_interval) == expected

    def test_insert_at_beginning_with_merge(self):
        """Test insertion at beginning that merges with first interval."""
        intervals = [[3, 5], [6, 9]]
        new_interval = [1, 4]
        expected = [[1, 5], [6, 9]]
        assert self.solution.insert(intervals, new_interval) == expected

    def test_insert_at_end_with_merge(self):
        """Test insertion at end that merges with last interval."""
        intervals = [[1, 3], [6, 9]]
        new_interval = [8, 12]
        expected = [[1, 3], [6, 12]]
        assert self.solution.insert(intervals, new_interval) == expected

    def test_touching_intervals(self):
        """Test intervals that touch but don't overlap."""
        intervals = [[1, 2], [3, 5], [6, 7], [8, 10]]
        new_interval = [2, 3]
        expected = [[1, 5], [6, 7], [8, 10]]
        assert self.solution.insert(intervals, new_interval) == expected

    def test_exact_same_interval(self):
        """Test inserting an interval that exactly matches existing one."""
        intervals = [[1, 3], [6, 9]]
        new_interval = [1, 3]
        expected = [[1, 3], [6, 9]]
        assert self.solution.insert(intervals, new_interval) == expected

    def test_new_interval_inside_existing(self):
        """Test new interval completely inside existing interval."""
        intervals = [[1, 10]]
        new_interval = [3, 7]
        expected = [[1, 10]]
        assert self.solution.insert(intervals, new_interval) == expected

    def test_partial_overlap_left(self):
        """Test new interval partially overlaps on the left."""
        intervals = [[3, 8], [10, 15]]
        new_interval = [1, 5]
        expected = [[1, 8], [10, 15]]
        assert self.solution.insert(intervals, new_interval) == expected

    def test_partial_overlap_right(self):
        """Test new interval partially overlaps on the right."""
        intervals = [[1, 5], [10, 15]]
        new_interval = [3, 12]
        expected = [[1, 15]]
        assert self.solution.insert(intervals, new_interval) == expected

    def test_merge_all_intervals(self):
        """Test new interval merges all existing intervals."""
        intervals = [[1, 2], [3, 4], [5, 6], [7, 8]]
        new_interval = [2, 7]
        expected = [[1, 8]]
        assert self.solution.insert(intervals, new_interval) == expected

    def test_single_point_intervals(self):
        """Test with single point intervals."""
        intervals = [[1, 1], [3, 3], [5, 5]]
        new_interval = [2, 4]
        expected = [[1, 1], [2, 4], [5, 5]]
        assert self.solution.insert(intervals, new_interval) == expected

    def test_adjacent_intervals(self):
        """Test with adjacent intervals that should merge."""
        intervals = [[1, 2], [4, 5]]
        new_interval = [2, 4]
        expected = [[1, 5]]
        assert self.solution.insert(intervals, new_interval) == expected

    def test_large_intervals(self):
        """Test with larger number ranges."""
        intervals = [[1, 100], [200, 300], [400, 500]]
        new_interval = [150, 250]
        expected = [[1, 100], [150, 300], [400, 500]]
        assert self.solution.insert(intervals, new_interval) == expected

    def test_zero_start_interval(self):
        """Test intervals starting from zero."""
        intervals = [[0, 2], [5, 10]]
        new_interval = [1, 6]
        expected = [[0, 10]]
        assert self.solution.insert(intervals, new_interval) == expected

    def test_negative_intervals(self):
        """Test with negative interval values."""
        intervals = [[-5, -2], [1, 3]]
        new_interval = [-1, 2]
        expected = [[-5, -2], [-1, 3]]
        assert self.solution.insert(intervals, new_interval) == expected

    def test_complex_merge_scenario(self):
        """Test complex scenario with multiple merges."""
        intervals = [[1, 2], [3, 4], [6, 7], [8, 9], [10, 11]]
        new_interval = [3, 8]
        expected = [[1, 2], [3, 9], [10, 11]]
        assert self.solution.insert(intervals, new_interval) == expected

    def test_insert_between_gaps(self):
        """Test insertion in gaps between intervals."""
        intervals = [[1, 2], [5, 6], [9, 10]]
        new_interval = [3, 4]
        expected = [[1, 2], [3, 4], [5, 6], [9, 10]]
        assert self.solution.insert(intervals, new_interval) == expected

    def test_merge_with_gap_filling(self):
        """Test merging that fills gaps between intervals."""
        intervals = [[1, 2], [5, 6]]
        new_interval = [2, 5]
        expected = [[1, 6]]
        assert self.solution.insert(intervals, new_interval) == expected

    def test_edge_case_maximum_values(self):
        """Test with maximum possible interval values."""
        intervals = [[1, 1000], [2000, 3000]]
        new_interval = [500, 1500]
        expected = [[1, 1500], [2000, 3000]]
        assert self.solution.insert(intervals, new_interval) == expected

    def test_algorithm_properties(self):
        """Test algorithm maintains sorted order and non-overlapping property."""
        intervals = [[1, 3], [6, 9], [10, 15], [20, 25]]
        new_interval = [4, 8]
        result = self.solution.insert(intervals, new_interval)
        
        # Check sorted order
        for i in range(len(result) - 1):
            assert result[i][1] < result[i + 1][0], "Intervals should be non-overlapping and sorted"
        
        # Check no gaps within merged intervals
        for interval in result:
            assert interval[0] <= interval[1], "Each interval should be valid"

    def test_performance_with_many_intervals(self):
        """Test performance with larger input."""
        # Create 100 non-overlapping intervals
        intervals = [[i * 10, i * 10 + 5] for i in range(100)]
        new_interval = [250, 350]  # Should merge multiple intervals
        
        result = self.solution.insert(intervals, new_interval)
        
        # Verify result is correct
        assert len(result) < len(intervals), "Should have merged some intervals"
        
        # Check all intervals are properly ordered
        for i in range(len(result) - 1):
            assert result[i][1] < result[i + 1][0], "Result should maintain order"


if __name__ == '__main__':
    # Run the tests
    pytest.main([__file__])
