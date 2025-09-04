"""Tests for LeetCode #81: Search in Rotated Sorted Array II."""

import pytest
from leetcode.search_in_rotated_sorted_array_II import Solution


class TestSearchInRotatedSortedArrayII:
    """Test class for Search in Rotated Sorted Array II problem."""

    def setup_method(self):
        """Set up test fixtures before each test method."""
        self.solution = Solution()

    @pytest.mark.parametrize(
        "nums,target,expected",
        [
            # Basic test cases with duplicates
            ([2, 5, 6, 0, 0, 1, 2], 0, True),
            ([2, 5, 6, 0, 0, 1, 2], 3, False),
            ([1, 0, 1, 1, 1], 0, True),
            ([1, 1, 1, 0, 1], 0, True),
            
            # Single element
            ([1], 1, True),
            ([1], 2, False),
            
            # All same elements
            ([1, 1, 1, 1], 1, True),
            ([1, 1, 1, 1], 2, False),
            
            # No rotation
            ([1, 2, 3, 4, 5], 3, True),
            ([1, 2, 3, 4, 5], 6, False),
            
            # Complete rotation (same as original)
            ([1, 2, 3, 4, 5], 1, True),
            ([1, 2, 3, 4, 5], 5, True),
            
            # Rotation with duplicates at boundaries
            ([1, 1, 3, 1], 3, True),
            ([1, 3, 1, 1], 3, True),
            ([3, 1, 1, 1], 3, True),
            ([1, 1, 1, 3], 3, True),
            
            # Target at pivot point
            ([4, 5, 6, 7, 0, 1, 2], 0, True),
            ([4, 5, 6, 7, 0, 1, 2], 7, True),
            
            # Multiple duplicates throughout
            ([2, 2, 2, 3, 4, 2], 3, True),
            ([2, 2, 2, 3, 4, 2], 4, True),
            ([2, 2, 2, 3, 4, 2], 5, False),
            
            # Edge cases with duplicates
            ([1, 1, 2, 1], 2, True),
            ([1, 2, 1, 1], 2, True),
            ([2, 1, 1, 1], 2, True),
            ([1, 1, 1, 2], 2, True),
        ]
    )
    def test_search_valid_inputs(self, nums, target, expected):
        """Test search with various valid inputs."""
        assert self.solution.search(nums, target) == expected

    def test_empty_array(self):
        """Test with empty array."""
        assert self.solution.search([], 1) is False

    def test_two_elements(self):
        """Test with two-element arrays."""
        assert self.solution.search([1, 3], 1) is True
        assert self.solution.search([1, 3], 3) is True
        assert self.solution.search([1, 3], 2) is False
        assert self.solution.search([3, 1], 1) is True
        assert self.solution.search([3, 1], 3) is True
        assert self.solution.search([1, 1], 1) is True
        assert self.solution.search([1, 1], 2) is False

    def test_three_elements(self):
        """Test with three-element arrays."""
        assert self.solution.search([2, 3, 1], 1) is True
        assert self.solution.search([2, 3, 1], 2) is True
        assert self.solution.search([2, 3, 1], 3) is True
        assert self.solution.search([2, 3, 1], 4) is False
        assert self.solution.search([1, 1, 2], 2) is True
        assert self.solution.search([2, 1, 1], 2) is True

    def test_negative_numbers(self):
        """Test with negative numbers."""
        assert self.solution.search([-1, 0, 1, 2, -1, -1], 0) is True
        assert self.solution.search([-1, 0, 1, 2, -1, -1], -1) is True
        assert self.solution.search([-1, 0, 1, 2, -1, -1], 3) is False

    def test_large_numbers(self):
        """Test with large numbers."""
        large_nums = [10**9, 10**9 + 1, 1, 2, 10**9]
        assert self.solution.search(large_nums, 10**9) is True
        assert self.solution.search(large_nums, 1) is True
        assert self.solution.search(large_nums, 3) is False

    def test_worst_case_duplicates(self):
        """Test worst-case scenario with many duplicates."""
        # This should degrade to O(n) time complexity
        nums = [1] * 100 + [2] + [1] * 100
        assert self.solution.search(nums, 2) is True
        assert self.solution.search(nums, 3) is False

    def test_rotation_points(self):
        """Test various rotation points."""
        original = [1, 2, 3, 4, 5]
        
        # Rotate at each position
        for i in range(len(original)):
            rotated = original[i:] + original[:i]
            for target in original:
                assert self.solution.search(rotated, target) is True
            assert self.solution.search(rotated, 0) is False
            assert self.solution.search(rotated, 6) is False

    def test_complex_duplicates(self):
        """Test complex cases with duplicates."""
        # Many duplicates with one different element
        nums1 = [1, 1, 1, 1, 2, 1, 1]
        assert self.solution.search(nums1, 2) is True
        assert self.solution.search(nums1, 1) is True
        assert self.solution.search(nums1, 3) is False

        # Alternating pattern
        nums2 = [1, 2, 1, 2, 1, 2]
        assert self.solution.search(nums2, 1) is True
        assert self.solution.search(nums2, 2) is True
        assert self.solution.search(nums2, 3) is False

    def test_boundary_values(self):
        """Test boundary values."""
        nums = [3, 4, 5, 1, 2]
        
        # Test first and last elements
        assert self.solution.search(nums, 3) is True
        assert self.solution.search(nums, 2) is True
        
        # Test pivot point
        assert self.solution.search(nums, 5) is True
        assert self.solution.search(nums, 1) is True

    def test_single_rotation_with_duplicates(self):
        """Test single rotation with duplicates."""
        nums = [2, 2, 2, 0, 1]
        assert self.solution.search(nums, 0) is True
        assert self.solution.search(nums, 1) is True
        assert self.solution.search(nums, 2) is True
        assert self.solution.search(nums, 3) is False


if __name__ == "__main__":
    pytest.main([__file__])
