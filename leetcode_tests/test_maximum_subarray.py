"""
Comprehensive tests for Maximum Subarray problem.

Tests the implementation of Kadane's algorithm.
"""
import pytest

from leetcode.maximum_subarray import Solution


class TestMaximumSubarray:
    """Test class for maximum subarray implementation."""

    def setup_method(self):
        """Set up test fixtures before each test method."""
        self.solution = Solution()

    @pytest.fixture
    def leetcode_example(self):
        """LeetCode example case."""
        return [-2, 1, -3, 4, -1, 2, 1, -5, 4]

    @pytest.fixture
    def all_negative(self):
        """Array with all negative numbers."""
        return [-3, -2, -1, -5]

    @pytest.fixture
    def all_positive(self):
        """Array with all positive numbers."""
        return [1, 2, 3, 4, 5]

    @pytest.fixture
    def mixed_array(self):
        """Mixed positive and negative array."""
        return [5, -3, 2, -1, 4]

    @pytest.fixture
    def single_element(self):
        """Single element arrays."""
        return ([5], [-3], [0])

    def test_leetcode_example(self, leetcode_example):
        """Test with LeetCode example."""
        result = self.solution.maxSubArray(leetcode_example)
        assert result == 6

    def test_all_negative(self, all_negative):
        """Test with all negative numbers."""
        result = self.solution.maxSubArray(all_negative)
        assert result == -1

    def test_all_positive_numbers(self, all_positive):
        """Test array with all positive numbers."""
        result = self.solution.maxSubArray(all_positive)
        expected = sum(all_positive)  # Sum of all elements
        assert result == expected

    def test_mixed_array(self, mixed_array):
        """Test mixed positive and negative array."""
        result = self.solution.maxSubArray(mixed_array)
        assert result == 7  # [5, -3, 2, -1, 4] = 7

    def test_single_element_arrays(self, single_element):
        """Test single element arrays."""
        for arr in single_element:
            result = self.solution.maxSubArray(arr)
            expected = arr[0]
            assert result == expected

    def test_two_elements_positive(self):
        """Test two positive elements."""
        arr = [1, 2]
        result = self.solution.maxSubArray(arr)
        assert result == 3  # Sum of both

    def test_two_elements_negative(self):
        """Test two negative elements."""
        arr = [-1, -2]
        result = self.solution.maxSubArray(arr)
        assert result == -1  # Less negative element

    def test_two_elements_mixed(self):
        """Test two mixed elements."""
        arr = [-1, 2]
        result = self.solution.maxSubArray(arr)
        assert result == 2  # Just the positive element

    def test_alternating_positive_negative(self):
        """Test alternating positive and negative."""
        arr = [1, -1, 1, -1, 1]
        result = self.solution.maxSubArray(arr)
        assert result == 1  # Any single positive element

    def test_large_positive_at_start(self):
        """Test large positive number at start."""
        arr = [10, -5, 2, -1]
        result = self.solution.maxSubArray(arr)
        assert result == 10  # Just the first element

    def test_large_positive_at_end(self):
        """Test large positive number at end."""
        arr = [-5, 2, -1, 10]
        result = self.solution.maxSubArray(arr)
        assert result == 11  # [2, -1, 10] = 11

    def test_zeros_in_array(self):
        """Test array containing zeros."""
        arr = [0, -1, 0, 2, 0]
        result = self.solution.maxSubArray(arr)
        assert result == 2  # Just the 2

    def test_subarray_in_middle(self):
        """Test optimal subarray in middle."""
        arr = [-2, 3, 4, -1, 2, -5]
        result = self.solution.maxSubArray(arr)
        assert result == 8  # [3, 4, -1, 2] = 8

    def test_negative_then_positive(self):
        """Test negative numbers followed by positive."""
        arr = [-5, -2, 1, 3, 2]
        result = self.solution.maxSubArray(arr)
        assert result == 6  # [1, 3, 2] = 6

    def test_positive_then_negative(self):
        """Test positive numbers followed by negative."""
        arr = [5, 3, -10, -2, -1]
        result = self.solution.maxSubArray(arr)
        assert result == 8  # [5, 3] = 8

    def test_single_positive_in_negative(self):
        """Test single positive number among negatives."""
        arr = [-3, -1, 5, -2, -4]
        result = self.solution.maxSubArray(arr)
        assert result == 5  # Just the 5

    def test_kadane_edge_case(self):
        """Test edge case for Kadane's algorithm."""
        arr = [1, -3, 2, -1, 3]
        result = self.solution.maxSubArray(arr)
        assert result == 4  # [2, -1, 3] = 4

    def test_large_array(self):
        """Test with larger array."""
        arr = [1, -2, 3, 4, -5, 6, -1, 2]
        result = self.solution.maxSubArray(arr)
        assert result == 9  # [3, 4, -5, 6, -1, 2] = 9

    def test_all_zeros(self):
        """Test array with all zeros."""
        arr = [0, 0, 0, 0]
        result = self.solution.maxSubArray(arr)
        assert result == 0

    def test_alternating_large_values(self):
        """Test alternating large positive and negative values."""
        arr = [100, -50, 80, -40, 60]
        result = self.solution.maxSubArray(arr)
        assert result == 150  # [100, -50, 80, -40, 60] = 150


if __name__ == '__main__':
    pytest.main([__file__])
