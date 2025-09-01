"""
Comprehensive test suite for LeetCode Problem #84: Largest Rectangle in Histogram
Tests the monotonic stack algorithm for finding maximum rectangle area.
"""

import pytest

from leetcode.largest_rectangle_in_histgram import Solution


class TestLargestRectangleInHistogram:
    """Test cases for Largest Rectangle in Histogram problem."""

    def setup_method(self):
        """Set up test fixtures before each test method."""
        self.solution = Solution()

    def test_basic_example_1(self):
        """Test first basic example from LeetCode."""
        heights = [2, 1, 5, 6, 2, 3]
        expected = 10  # Rectangle with height 5 and width 2
        assert self.solution.largestRectangleArea(heights) == expected

    def test_basic_example_2(self):
        """Test second basic example from LeetCode."""
        heights = [2, 4]
        expected = 4  # Rectangle with height 4 and width 1
        assert self.solution.largestRectangleArea(heights) == expected

    def test_single_bar(self):
        """Test histogram with single bar."""
        heights = [5]
        expected = 5
        assert self.solution.largestRectangleArea(heights) == expected

    def test_single_zero_bar(self):
        """Test histogram with single zero height bar."""
        heights = [0]
        expected = 0
        assert self.solution.largestRectangleArea(heights) == expected

    def test_all_same_height(self):
        """Test histogram where all bars have same height."""
        heights = [3, 3, 3, 3]
        expected = 12  # Height 3, width 4
        assert self.solution.largestRectangleArea(heights) == expected

    def test_ascending_heights(self):
        """Test histogram with ascending heights."""
        heights = [1, 2, 3, 4, 5]
        expected = 9  # Height 3, width 3 (middle 3 bars)
        assert self.solution.largestRectangleArea(heights) == expected

    def test_descending_heights(self):
        """Test histogram with descending heights."""
        heights = [5, 4, 3, 2, 1]
        expected = 9  # Height 3, width 3 (first 3 bars)
        assert self.solution.largestRectangleArea(heights) == expected

    def test_mountain_shape(self):
        """Test mountain-shaped histogram."""
        heights = [1, 3, 6, 7, 4, 3, 1]
        expected = 15  # Height 3, width 5 from indices 1-5
        assert self.solution.largestRectangleArea(heights) == expected

    def test_valley_shape(self):
        """Test valley-shaped histogram."""
        heights = [6, 4, 2, 0, 2, 4, 6]
        expected = 8  # Height 2, width 4 or height 4, width 2
        assert self.solution.largestRectangleArea(heights) == expected

    def test_zero_in_middle(self):
        """Test histogram with zero height in middle."""
        heights = [2, 1, 5, 6, 2, 3, 0, 1, 2]
        expected = 10  # Before the zero
        assert self.solution.largestRectangleArea(heights) == expected

    def test_multiple_zeros(self):
        """Test histogram with multiple zeros."""
        heights = [1, 0, 2, 0, 3]
        expected = 3  # Single bars
        assert self.solution.largestRectangleArea(heights) == expected

    def test_all_zeros(self):
        """Test histogram with all zero heights."""
        heights = [0, 0, 0, 0]
        expected = 0
        assert self.solution.largestRectangleArea(heights) == expected

    def test_large_rectangle_at_start(self):
        """Test when largest rectangle is at the beginning."""
        heights = [6, 6, 6, 2, 1]
        expected = 18  # Height 6, width 3
        assert self.solution.largestRectangleArea(heights) == expected

    def test_large_rectangle_at_end(self):
        """Test when largest rectangle is at the end."""
        heights = [1, 2, 6, 6, 6]
        expected = 18  # Height 6, width 3
        assert self.solution.largestRectangleArea(heights) == expected

    def test_large_rectangle_in_middle(self):
        """Test when largest rectangle is in the middle."""
        heights = [1, 5, 5, 5, 1]
        expected = 15  # Height 5, width 3
        assert self.solution.largestRectangleArea(heights) == expected

    def test_alternating_heights(self):
        """Test histogram with alternating heights."""
        heights = [1, 3, 1, 3, 1]
        expected = 5  # Height 1, width 5
        assert self.solution.largestRectangleArea(heights) == expected

    def test_two_bars_equal(self):
        """Test two bars with equal height."""
        heights = [4, 4]
        expected = 8  # Height 4, width 2
        assert self.solution.largestRectangleArea(heights) == expected

    def test_two_bars_different(self):
        """Test two bars with different heights."""
        heights = [2, 3]
        expected = 4  # Height 2, width 2 (both bars at height 2)
        assert self.solution.largestRectangleArea(heights) == expected

    def test_large_heights(self):
        """Test histogram with large height values."""
        heights = [100, 200, 300, 200, 100]
        expected = 600  # Height 200, width 3
        assert self.solution.largestRectangleArea(heights) == expected

    def test_complex_pattern(self):
        """Test complex histogram pattern."""
        heights = [6, 2, 5, 4, 5, 1, 6]
        expected = 12  # Height 4, width 3 (indices 1-3) or other combinations
        assert self.solution.largestRectangleArea(heights) == expected

    def test_stack_efficiency_ascending(self):
        """Test monotonic stack efficiency with ascending pattern."""
        heights = [1, 2, 3, 4, 5, 6]
        expected = 12  # Height 3, width 4 or height 4, width 3
        assert self.solution.largestRectangleArea(heights) == expected

    def test_stack_efficiency_descending(self):
        """Test monotonic stack efficiency with descending pattern."""
        heights = [6, 5, 4, 3, 2, 1]
        expected = 12  # Height 4, width 3 (first 3 bars)
        assert self.solution.largestRectangleArea(heights) == expected

    def test_wide_low_rectangle(self):
        """Test case where wide, low rectangle is optimal."""
        heights = [2, 1, 1, 1, 1, 1, 2]
        expected = 7  # Height 1, width 7 (entire histogram)
        assert self.solution.largestRectangleArea(heights) == expected

    def test_tall_narrow_rectangle(self):
        """Test case where tall, narrow rectangle is optimal."""
        heights = [1, 1, 10, 1, 1]
        expected = 10  # Height 10, width 1
        assert self.solution.largestRectangleArea(heights) == expected

    def test_empty_input_edge_case(self):
        """Test edge case with empty input."""
        heights = []
        expected = 0
        assert self.solution.largestRectangleArea(heights) == expected

    def test_performance_large_uniform(self):
        """Test performance with large uniform histogram."""
        heights = [5] * 100  # 100 bars of height 5
        expected = 500  # Height 5, width 100
        assert self.solution.largestRectangleArea(heights) == expected

    def test_performance_large_ascending(self):
        """Test performance with large ascending histogram."""
        heights = list(range(1, 101))  # 1 to 100
        result = self.solution.largestRectangleArea(heights)
        # Should handle efficiently without timeout
        assert isinstance(result, int) and result > 0

    def test_algorithm_correctness_properties(self):
        """Test fundamental properties of the algorithm."""
        heights = [3, 1, 3, 2, 2]
        result = self.solution.largestRectangleArea(heights)
        
        # Result should be non-negative
        assert result >= 0
        
        # Result should be at most max_height * len(heights)
        max_height = max(heights) if heights else 0
        assert result <= max_height * len(heights)

    def test_monotonic_stack_boundary_conditions(self):
        """Test boundary conditions for monotonic stack."""
        test_cases = [
            ([1], 1),
            ([1, 2], 2),
            ([2, 1], 2),
            ([1, 1], 2),
            ([5, 0, 5], 5)
        ]
        
        for heights, expected in test_cases:
            assert self.solution.largestRectangleArea(heights) == expected

    def test_input_not_modified(self):
        """Test that input array is not modified."""
        heights = [2, 1, 5, 6, 2, 3]
        original = heights.copy()
        
        self.solution.largestRectangleArea(heights)
        
        # Input should remain unchanged
        assert heights == original

    def test_multiple_optimal_rectangles(self):
        """Test case with multiple rectangles of same optimal area."""
        heights = [2, 2, 2]
        expected = 6  # Height 2, width 3
        assert self.solution.largestRectangleArea(heights) == expected

    def test_step_pattern(self):
        """Test step-like pattern."""
        heights = [1, 2, 2, 3, 3, 3]
        expected = 10  # Height 2, width 5 (all bars at height 2 or above)
        assert self.solution.largestRectangleArea(heights) == expected

    def test_reverse_step_pattern(self):
        """Test reverse step-like pattern."""
        heights = [3, 3, 3, 2, 2, 1]
        expected = 10  # Height 2, width 5 (first 5 bars at height 2 or above)
        assert self.solution.largestRectangleArea(heights) == expected

    def test_plateau_pattern(self):
        """Test plateau pattern."""
        heights = [1, 4, 4, 4, 1]
        expected = 12  # Height 4, width 3
        assert self.solution.largestRectangleArea(heights) == expected

    def test_random_pattern(self):
        """Test random-like pattern."""
        heights = [3, 6, 5, 7, 4, 8, 1, 0]
        result = self.solution.largestRectangleArea(heights)
        # Should handle any valid pattern
        assert isinstance(result, int) and result >= 0

    def test_edge_case_very_tall_single_bar(self):
        """Test edge case with very tall single bar."""
        heights = [1000]
        expected = 1000
        assert self.solution.largestRectangleArea(heights) == expected

    def test_edge_case_many_small_bars(self):
        """Test edge case with many small bars."""
        heights = [1] * 50
        expected = 50  # Height 1, width 50
        assert self.solution.largestRectangleArea(heights) == expected

    def test_zigzag_pattern(self):
        """Test zigzag pattern."""
        heights = [1, 5, 1, 5, 1, 5]
        expected = 6  # Height 1, width 6
        assert self.solution.largestRectangleArea(heights) == expected

    def test_symmetric_pattern(self):
        """Test symmetric histogram pattern."""
        heights = [1, 2, 3, 4, 3, 2, 1]
        expected = 10  # Height 2, width 5 (middle 5 bars at height 2 or above)
        assert self.solution.largestRectangleArea(heights) == expected


if __name__ == '__main__':
    # Run the tests
    pytest.main([__file__])
