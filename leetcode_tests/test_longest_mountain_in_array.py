"""
Comprehensive test suite for LeetCode Problem #845: Longest Mountain in Array.
Tests the one-pass algorithm for finding the longest mountain subarray.
"""

import pytest
import sys
import os
import importlib.util

# Add the parent directory to the path to allow imports
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

try:
    from leetcode.longest_mountain_in_array import Solution
except ImportError:
    # Fallback for environments where package import fails
    module_path = os.path.join(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
        "leetcode",
        "longest_mountain_in_array.py"
    )
    spec = importlib.util.spec_from_file_location("longest_mountain_in_array", module_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    Solution = module.Solution


class TestLongestMountainInArray:
    """Test cases for longest mountain in array calculation."""

    def setup_method(self):
        """Set up test fixtures before each test method."""
        self.solution = Solution()

    def test_basic_example_1(self):
        """Test basic example from problem description."""
        result = self.solution.longest_mountain([2, 1, 4, 7, 3, 2, 5])
        assert result == 5  # [1, 4, 7, 3, 2]

    def test_basic_example_2(self):
        """Test example with no valid mountain."""
        result = self.solution.longest_mountain([2, 2, 2])
        assert result == 0

    def test_perfect_mountain(self):
        """Test perfect mountain shape."""
        result = self.solution.longest_mountain([0, 1, 2, 3, 4, 5, 4, 3, 2, 1, 0])
        assert result == 11  # Entire array

    def test_given_example(self):
        """Test the given example in main function."""
        result = self.solution.longest_mountain([875, 884, 239, 731, 723, 685])
        assert result == 4  # [884, 239, 731, 723] or similar

    def test_empty_array(self):
        """Test empty array."""
        result = self.solution.longest_mountain([])
        assert result == 0

    def test_single_element(self):
        """Test single element array."""
        result = self.solution.longest_mountain([1])
        assert result == 0

    def test_two_elements(self):
        """Test two element array."""
        result = self.solution.longest_mountain([1, 2])
        assert result == 0

    def test_three_elements_valid_mountain(self):
        """Test minimal valid mountain (3 elements)."""
        result = self.solution.longest_mountain([1, 3, 2])
        assert result == 3

    def test_three_elements_ascending(self):
        """Test three ascending elements (not a mountain)."""
        result = self.solution.longest_mountain([1, 2, 3])
        assert result == 0

    def test_three_elements_descending(self):
        """Test three descending elements (not a mountain)."""
        result = self.solution.longest_mountain([3, 2, 1])
        assert result == 0

    def test_multiple_mountains(self):
        """Test array with multiple mountains."""
        result = self.solution.longest_mountain([1, 3, 2, 4, 6, 5, 7, 9, 8])
        assert result == 4  # Corrected expectation

    def test_plateau_in_mountain(self):
        """Test mountain with plateau (should break mountain)."""
        result = self.solution.longest_mountain([1, 2, 3, 3, 2, 1])
        assert result == 0  # Plateau breaks the mountain

    def test_ascending_only(self):
        """Test strictly ascending array."""
        result = self.solution.longest_mountain([1, 2, 3, 4, 5])
        assert result == 0

    def test_descending_only(self):
        """Test strictly descending array."""
        result = self.solution.longest_mountain([5, 4, 3, 2, 1])
        assert result == 0

    def test_flat_array(self):
        """Test flat array (all elements equal)."""
        result = self.solution.longest_mountain([5, 5, 5, 5, 5])
        assert result == 0

    def test_single_peak_mountain(self):
        """Test mountain with single peak."""
        result = self.solution.longest_mountain([1, 5, 2])
        assert result == 3

    def test_long_mountain(self):
        """Test longer mountain."""
        result = self.solution.longest_mountain([1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 3, 2, 1])
        assert result == 13  # Entire array

    def test_mountain_at_start(self):
        """Test mountain at beginning of array."""
        result = self.solution.longest_mountain([3, 5, 2, 1, 1, 1])
        assert result == 4  # [3, 5, 2, 1]

    def test_mountain_at_end(self):
        """Test mountain at end of array."""
        result = self.solution.longest_mountain([1, 1, 1, 2, 4, 3])
        assert result == 4  # [1, 2, 4, 3]

    def test_mountain_in_middle(self):
        """Test mountain in middle of array."""
        result = self.solution.longest_mountain([1, 1, 2, 4, 3, 1, 1])
        assert result == 5  # [1, 2, 4, 3, 1]

    def test_overlapping_potential_mountains(self):
        """Test overlapping potential mountains."""
        result = self.solution.longest_mountain([1, 2, 1, 3, 2])
        assert result == 3  # Either [1, 2, 1] or [1, 3, 2]

    def test_complex_pattern(self):
        """Test complex mountain pattern."""
        result = self.solution.longest_mountain([1, 3, 5, 4, 6, 8, 7, 2, 1])
        assert result == 6  # Longer mountain found

    def test_multiple_equal_length_mountains(self):
        """Test multiple mountains of equal length."""
        result = self.solution.longest_mountain([1, 3, 2, 5, 7, 6])
        assert result == 4  # Longer mountain found

    def test_very_small_mountains(self):
        """Test array with only minimum size mountains."""
        result = self.solution.longest_mountain([1, 2, 1, 3, 2, 4, 3])
        assert result == 3  # Multiple mountains of length 3

    def test_large_numbers(self):
        """Test with large numbers."""
        result = self.solution.longest_mountain([1000, 2000, 1500, 3000, 2500])
        assert result == 3  # [1000, 2000, 1500] or [1500, 3000, 2500]

    def test_negative_numbers(self):
        """Test with negative numbers."""
        result = self.solution.longest_mountain([-3, -1, -2, 0, -1])
        assert result == 3  # [-2, 0, -1]

    def test_mixed_positive_negative(self):
        """Test with mixed positive and negative numbers."""
        result = self.solution.longest_mountain([-1, 0, 1, 0, -1])
        assert result == 5  # Entire array

    def test_duplicate_peaks(self):
        """Test pattern that could form multiple peaks."""
        result = self.solution.longest_mountain([1, 3, 2, 3, 1])
        assert result == 3  # [1, 3, 2] or [2, 3, 1]

    def test_algorithm_correctness_properties(self):
        """Test fundamental properties of the algorithm."""
        # Property 1: Result is always non-negative
        test_arrays = [
            [1, 2, 3],
            [3, 2, 1],
            [1, 3, 2, 4, 3],
            []
        ]
        for arr in test_arrays:
            result = self.solution.longest_mountain(arr)
            assert result >= 0

        # Property 2: Result is 0 for arrays with length < 3
        assert self.solution.longest_mountain([]) == 0
        assert self.solution.longest_mountain([1]) == 0
        assert self.solution.longest_mountain([1, 2]) == 0

    def test_boundary_conditions(self):
        """Test boundary conditions."""
        # Minimum valid mountain
        assert self.solution.longest_mountain([1, 2, 1]) == 3
        
        # Just one element short of mountain
        assert self.solution.longest_mountain([1, 2]) == 0
        assert self.solution.longest_mountain([2, 1]) == 0
        
        # Plateau breaks mountain
        assert self.solution.longest_mountain([1, 2, 2, 1]) == 0

    def test_performance_larger_input(self):
        """Test performance with larger input."""
        # Create a large array with known mountain (avoiding duplicate at peak)
        large_arr = list(range(1, 501)) + list(range(499, 0, -1))  # 999 elements, no duplicate
        result = self.solution.longest_mountain(large_arr)
        assert result == 999  # Entire array is one big mountain

    def test_edge_case_alternating_pattern(self):
        """Test alternating up-down pattern."""
        result = self.solution.longest_mountain([1, 3, 2, 4, 3, 5, 4])
        assert result == 3  # Multiple small mountains

    def test_steep_mountain(self):
        """Test mountain with steep slopes."""
        result = self.solution.longest_mountain([1, 100, 2])
        assert result == 3

    def test_gradual_mountain(self):
        """Test mountain with gradual slopes."""
        result = self.solution.longest_mountain([1, 2, 3, 4, 5, 4, 3, 2, 1])
        assert result == 9

    def test_return_type_validation(self):
        """Test that return type is correct integer."""
        result = self.solution.longest_mountain([1, 3, 2])
        assert isinstance(result, int)
        assert result >= 0

    def test_input_preservation(self):
        """Test that input array is not modified."""
        original = [1, 3, 2, 4, 3]
        test_arr = original.copy()
        self.solution.longest_mountain(test_arr)
        assert test_arr == original

    def test_specific_mountain_patterns(self):
        """Test specific mountain patterns and their expected lengths."""
        # Simple ascending then descending
        assert self.solution.longest_mountain([1, 2, 3, 2, 1]) == 5
        
        # Longer ascending, shorter descending
        assert self.solution.longest_mountain([1, 2, 3, 4, 3]) == 5
        
        # Shorter ascending, longer descending
        assert self.solution.longest_mountain([1, 3, 2, 1, 0]) == 5

    def test_mountain_with_repeated_elements(self):
        """Test arrays with repeated elements that break mountains."""
        # Note: Algorithm may find partial mountains before reaching repeated elements
        assert self.solution.longest_mountain([1, 2, 2, 3, 2]) == 3  # [2, 3, 2] after plateau
        
        # Repeated element in descending part - still finds mountain
        assert self.solution.longest_mountain([1, 3, 2, 2, 1]) == 3  # [1, 3, 2]
        
        # Repeated element at peak
        assert self.solution.longest_mountain([1, 2, 3, 3, 2]) == 0

    def test_comprehensive_edge_cases(self):
        """Test comprehensive edge cases."""
        # All increasing then all decreasing
        assert self.solution.longest_mountain([1, 2, 3, 4, 3, 2, 1]) == 7
        
        # Multiple valid mountains, return longest
        assert self.solution.longest_mountain([1, 3, 2, 4, 6, 5, 7, 9, 8, 6]) == 5


if __name__ == "__main__":
    pytest.main([__file__])
