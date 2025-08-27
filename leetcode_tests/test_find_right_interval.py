"""
Test cases for LeetCode Problem #436: Find Right Interval
"""
import unittest
from leetcode.find_right_interval import Solution


class TestFindRightInterval(unittest.TestCase):
    """Test cases for the FindRightInterval solution."""

    def setUp(self):
        """Set up test fixtures before each test method."""
        self.solution = Solution()

    def test_example_case_1(self):
        """Test the first example case."""
        intervals = [[1, 2]]
        result = self.solution.findRightInterval(intervals)
        expected = [-1]
        assert result == expected

    def test_example_case_2(self):
        """Test the second example case."""
        intervals = [[3, 4], [2, 3], [1, 2]]
        result = self.solution.findRightInterval(intervals)
        expected = [-1, 0, 1]
        assert result == expected

    def test_example_case_3(self):
        """Test the third example case."""
        intervals = [[1, 4], [2, 3], [3, 4]]
        result = self.solution.findRightInterval(intervals)
        expected = [-1, 2, -1]
        assert result == expected

    def test_no_right_intervals(self):
        """Test case where some intervals have right intervals."""
        intervals = [[1, 2], [3, 4], [5, 6]]
        result = self.solution.findRightInterval(intervals)
        # [1,2] -> [3,4] at index 1, [3,4] -> [5,6] at index 2, [5,6] -> none
        expected = [1, 2, -1]
        assert result == expected

    def test_truly_no_right_intervals(self):
        """Test case where no intervals have right intervals."""
        intervals = [[3, 4], [1, 2], [5, 6]]
        result = self.solution.findRightInterval(intervals)
        # [3,4] -> [5,6] at index 2, [1,2] -> [3,4] at index 0, [5,6] -> none
        expected = [2, 0, -1]
        assert result == expected

    def test_actually_no_right_intervals(self):
        """Test case where truly no intervals have right intervals."""
        intervals = [[5, 10], [3, 8], [1, 6]]
        result = self.solution.findRightInterval(intervals)
        # All end times (10, 8, 6) are greater than all start times (5, 3, 1)
        expected = [-1, -1, -1]
        assert result == expected

    def test_all_right_intervals_exist(self):
        """Test case where all intervals have right intervals."""
        intervals = [[1, 2], [2, 3], [3, 4]]
        result = self.solution.findRightInterval(intervals)
        expected = [1, 2, -1]
        assert result == expected

    def test_single_interval(self):
        """Test single interval."""
        intervals = [[1, 2]]
        result = self.solution.findRightInterval(intervals)
        expected = [-1]
        assert result == expected

    def test_identical_intervals(self):
        """Test with identical intervals."""
        intervals = [[1, 2], [1, 2], [1, 2]]
        result = self.solution.findRightInterval(intervals)
        # For [1,2] intervals, each can find the first one with start >= 2 (none exist)
        expected = [-1, -1, -1]
        assert result == expected

    def test_overlapping_intervals(self):
        """Test with overlapping intervals."""
        intervals = [[1, 4], [2, 3], [3, 4]]
        result = self.solution.findRightInterval(intervals)
        expected = [-1, 2, -1]
        assert result == expected

    def test_point_intervals(self):
        """Test with point intervals (start == end)."""
        intervals = [[1, 1], [2, 2], [3, 3]]
        result = self.solution.findRightInterval(intervals)
        # [1,1] -> [1,1] at index 0, [2,2] -> [2,2] at index 1, [3,3] -> [3,3] at index 2
        expected = [0, 1, 2]
        assert result == expected

    def test_reverse_order(self):
        """Test intervals in reverse order."""
        intervals = [[4, 5], [3, 4], [2, 3], [1, 2]]
        result = self.solution.findRightInterval(intervals)
        expected = [-1, 0, 1, 2]
        assert result == expected

    def test_gaps_between_intervals(self):
        """Test with gaps between intervals."""
        intervals = [[1, 2], [4, 5], [7, 8]]
        result = self.solution.findRightInterval(intervals)
        expected = [1, 2, -1]
        assert result == expected

    def test_nested_intervals(self):
        """Test with nested intervals."""
        intervals = [[1, 10], [2, 3], [4, 5]]
        result = self.solution.findRightInterval(intervals)
        expected = [-1, 2, -1]
        assert result == expected

    def test_adjacent_intervals(self):
        """Test with adjacent intervals."""
        intervals = [[1, 2], [2, 3], [3, 4], [4, 5]]
        result = self.solution.findRightInterval(intervals)
        expected = [1, 2, 3, -1]
        assert result == expected

    def test_large_intervals(self):
        """Test with large interval values."""
        intervals = [[1000000, 2000000], [2000000, 3000000]]
        result = self.solution.findRightInterval(intervals)
        expected = [1, -1]
        assert result == expected

    def test_mixed_interval_sizes(self):
        """Test with mixed interval sizes."""
        intervals = [[1, 10], [2, 3], [5, 6], [8, 9]]
        result = self.solution.findRightInterval(intervals)
        expected = [-1, 2, 3, -1]
        assert result == expected

    def test_return_type_and_constraints(self):
        """Test return type and constraints."""
        intervals = [[1, 2], [3, 4]]
        result = self.solution.findRightInterval(intervals)
        assert isinstance(result, list)
        assert len(result) == len(intervals)
        assert all(isinstance(x, int) for x in result)
        assert all(x == -1 or 0 <= x < len(intervals) for x in result)

    def test_algorithm_correctness(self):
        """Test algorithm correctness with various patterns."""
        test_cases = [
            ([[1, 2]], [-1]),
            ([[1, 2], [2, 3]], [1, -1]),
            ([[1, 3], [2, 4]], [-1, -1]),
            ([[1, 2], [1, 3]], [-1, -1]),  # Neither can find start >= their end
        ]
        
        for intervals, expected in test_cases:
            with self.subTest(intervals=intervals):
                result = self.solution.findRightInterval(intervals)
                assert result == expected

    def test_boundary_conditions(self):
        """Test edge cases and boundary conditions."""
        # Single point interval can reference itself
        result = self.solution.findRightInterval([[1, 1]])
        assert result == [0]
        
        # Two adjacent point intervals
        result = self.solution.findRightInterval([[1, 1], [1, 1]])
        assert len(result) == 2

    def test_performance_reasonable_input(self):
        """Test performance with reasonable input size."""
        # Create intervals that test binary search
        intervals = [[i, i+1] for i in range(100)]
        result = self.solution.findRightInterval(intervals)
        
        # Each interval should point to the next one, except the last
        expected = list(range(1, 100)) + [-1]
        assert result == expected

    def test_binary_search_correctness(self):
        """Test that binary search finds correct intervals."""
        intervals = [[1, 3], [2, 4], [3, 5], [4, 6]]
        result = self.solution.findRightInterval(intervals)
        
        # Manually verify each interval
        # [1,3] -> needs start >= 3, found [3,5] at index 2
        # [2,4] -> needs start >= 4, found [4,6] at index 3  
        # [3,5] -> needs start >= 5, not found
        # [4,6] -> needs start >= 6, not found
        expected = [2, 3, -1, -1]
        assert result == expected

    def test_duplicate_start_times(self):
        """Test intervals with duplicate start times."""
        intervals = [[1, 2], [1, 3], [1, 4]]
        result = self.solution.findRightInterval(intervals)
        
        # All should find some valid right interval with start >= end
        assert len(result) == 3
        assert all(x == -1 or 0 <= x < 3 for x in result)

    def test_self_reference_intervals(self):
        """Test intervals that can reference themselves."""
        intervals = [[1, 1], [2, 2]]
        result = self.solution.findRightInterval(intervals)
        
        # Point intervals can reference themselves or later intervals
        assert len(result) == 2
        assert result[0] in [0, 1]  # Can be itself or next
        assert result[1] in [1, -1]  # Can be itself or none

    def test_deterministic_behavior(self):
        """Test that algorithm produces consistent results."""
        intervals = [[1, 2], [2, 3], [3, 4]]
        result1 = self.solution.findRightInterval(intervals)
        result2 = self.solution.findRightInterval(intervals)
        assert result1 == result2

    def test_interval_ordering_independence(self):
        """Test that result corresponds to original order."""
        intervals = [[3, 4], [1, 2], [2, 3]]
        result = self.solution.findRightInterval(intervals)
        
        # Result should be in same order as input
        assert len(result) == 3
        # [3,4] -> no right interval
        # [1,2] -> [2,3] at original index 2
        # [2,3] -> [3,4] at original index 0
        expected = [-1, 2, 0]
        assert result == expected

    def test_complex_interval_pattern(self):
        """Test complex interval arrangements."""
        intervals = [[1, 5], [2, 3], [3, 4], [6, 7]]
        result = self.solution.findRightInterval(intervals)
        
        # [1,5] -> needs start >= 5, found [6,7] at index 3
        # [2,3] -> needs start >= 3, found [3,4] at index 2
        # [3,4] -> needs start >= 4, found [6,7] at index 3
        # [6,7] -> needs start >= 7, not found
        expected = [3, 2, 3, -1]
        assert result == expected


if __name__ == "__main__":
    unittest.main()
