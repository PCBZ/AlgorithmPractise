"""
Test cases for 3Sum problem
Source: https://leetcode.com/problems/3sum/description/
"""

import sys
import os
import importlib.util

# Add the parent directory to sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import pytest

# Import the module with numeric name
spec = importlib.util.spec_from_file_location(
    "three_sum", 
    os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "leetcode", "3_sum.py")
)
three_sum_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(three_sum_module)
Solution = three_sum_module.Solution


class TestThreeSum:
    def setup_method(self):
        """Set up test fixtures before each test method."""
        self.solution = Solution()

    def test_basic_case(self):
        """Test basic case with multiple triplets."""
        nums = [-1, 0, 1, 2, -1, -4]
        result = self.solution.threeSum(nums)
        expected = [[-1, -1, 2], [-1, 0, 1]]
        # Sort both lists for comparison since order doesn't matter
        result_sorted = sorted([sorted(triplet) for triplet in result])
        expected_sorted = sorted([sorted(triplet) for triplet in expected])
        assert result_sorted == expected_sorted

    def test_all_zeros(self):
        """Test case with all zeros."""
        nums = [0, 0, 0]
        result = self.solution.threeSum(nums)
        expected = [[0, 0, 0]]
        assert result == expected

    def test_no_solution(self):
        """Test case with no valid triplets."""
        nums = [1, 2, 3]
        result = self.solution.threeSum(nums)
        assert result == []

    def test_empty_array(self):
        """Test with empty array."""
        nums = []
        result = self.solution.threeSum(nums)
        assert result == []

    def test_single_element(self):
        """Test with single element."""
        nums = [1]
        result = self.solution.threeSum(nums)
        assert result == []

    def test_two_elements(self):
        """Test with two elements."""
        nums = [1, 2]
        result = self.solution.threeSum(nums)
        assert result == []

    def test_duplicates(self):
        """Test with many duplicates."""
        nums = [-1, 0, 1, 0]
        result = self.solution.threeSum(nums)
        expected = [[-1, 0, 1]]
        assert result == expected

    def test_all_negative(self):
        """Test with all negative numbers."""
        nums = [-1, -2, -3, -4]
        result = self.solution.threeSum(nums)
        assert result == []

    def test_all_positive(self):
        """Test with all positive numbers."""
        nums = [1, 2, 3, 4]
        result = self.solution.threeSum(nums)
        assert result == []

    def test_mixed_with_zero(self):
        """Test mixed positive/negative with zero."""
        nums = [-2, 0, 1, 1, 2]
        result = self.solution.threeSum(nums)
        expected = [[-2, 0, 2], [-2, 1, 1]]
        result_sorted = sorted([sorted(triplet) for triplet in result])
        expected_sorted = sorted([sorted(triplet) for triplet in expected])
        assert result_sorted == expected_sorted

    def test_larger_array(self):
        """Test with larger array."""
        nums = [-1, 0, 1, 2, -1, -4, -2, -3, 3, 0, 4]
        result = self.solution.threeSum(nums)
        # Check that result contains valid triplets
        for triplet in result:
            assert len(triplet) == 3
            assert sum(triplet) == 0
        # Check uniqueness
        unique_triplets = set()
        for triplet in result:
            sorted_triplet = tuple(sorted(triplet))
            assert sorted_triplet not in unique_triplets
            unique_triplets.add(sorted_triplet)

    def test_edge_case_sum_zero(self):
        """Test edge cases that sum to zero."""
        nums = [-3, 0, 1, 2]
        result = self.solution.threeSum(nums)
        expected = [[-3, 1, 2]]
        assert result == expected

    def test_multiple_zeros(self):
        """Test with multiple zeros."""
        nums = [0, 0, 0, 0]
        result = self.solution.threeSum(nums)
        expected = [[0, 0, 0]]
        assert result == expected

    def test_large_numbers(self):
        """Test with large numbers."""
        nums = [-100000, 0, 100000]
        result = self.solution.threeSum(nums)
        expected = [[-100000, 0, 100000]]
        assert result == expected

    def test_small_negative_numbers(self):
        """Test with small negative numbers."""
        nums = [-1, -1, 2]
        result = self.solution.threeSum(nums)
        expected = [[-1, -1, 2]]
        assert result == expected

    def test_consecutive_numbers(self):
        """Test with consecutive numbers."""
        nums = [-3, -2, -1, 0, 1, 2, 3]
        result = self.solution.threeSum(nums)
        # Verify all triplets sum to zero
        for triplet in result:
            assert sum(triplet) == 0
        # Should contain multiple valid triplets
        assert len(result) > 0

    @pytest.mark.parametrize("nums,expected_count", [
        ([0, 0, 0], 1),  # Only one unique triplet
        ([1, 2, 3], 0),  # No valid triplets
        ([-1, 0, 1], 1),  # One triplet
        ([0], 0),  # Not enough elements
        ([1, -1, 0], 1),  # One triplet in different order
    ])
    def test_parametrized_cases(self, nums, expected_count):
        """Test multiple cases using parametrization."""
        result = self.solution.threeSum(nums)
        assert len(result) == expected_count
        # Verify all results sum to zero
        for triplet in result:
            assert sum(triplet) == 0

    def test_uniqueness(self):
        """Test that all returned triplets are unique."""
        nums = [-1, 0, 1, 2, -1, -4]
        result = self.solution.threeSum(nums)
        # Convert to set of tuples to check uniqueness
        unique_triplets = set()
        for triplet in result:
            sorted_triplet = tuple(sorted(triplet))
            assert sorted_triplet not in unique_triplets, f"Duplicate triplet found: {triplet}"
            unique_triplets.add(sorted_triplet)

    def test_sum_correctness(self):
        """Test that all triplets sum to zero."""
        nums = [-4, -1, -1, 0, 1, 2]
        result = self.solution.threeSum(nums)
        for triplet in result:
            assert sum(triplet) == 0, f"Triplet {triplet} does not sum to zero"
            assert len(triplet) == 3, f"Triplet {triplet} does not have 3 elements"


if __name__ == "__main__":
    pytest.main([__file__])
