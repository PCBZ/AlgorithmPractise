"""Tests for Next Greater Element Problems I, II, and III."""

import pytest
from leetcode.next_greater import NextGreaterElementSolutions


class TestNextGreaterElementSolutions:
    """Test class for Next Greater Element problems."""

    def setup_method(self):
        """Set up test fixtures before each test method."""
        self.solution = NextGreaterElementSolutions()

    # Next Greater Element I Tests
    @pytest.mark.parametrize(
        "nums1,nums2,expected",
        [
            # Basic test cases
            ([4, 1, 2], [1, 3, 4, 2], [-1, 3, -1]),
            ([2, 4], [1, 2, 3, 4], [3, -1]),
            ([1, 3, 5, 2, 4], [6, 5, 4, 3, 2, 1, 7], [7, 7, 7, 7, 7]),
            
            # Single element cases
            ([1], [1], [-1]),
            ([1], [1, 2], [2]),
            ([2], [1, 2], [-1]),
            
            # All elements have next greater
            ([1, 2, 3], [1, 2, 3, 4], [2, 3, 4]),
            
            # No elements have next greater
            ([4, 3, 2], [1, 2, 3, 4], [-1, 4, 3]),
            
            # Mixed scenarios
            ([1, 3, 2], [1, 2, 3, 4], [2, 4, 3]),
        ]
    )
    def test_next_greater_element_i(self, nums1, nums2, expected):
        """Test next_greater_element_i with various inputs."""
        assert self.solution.next_greater_element_i(nums1, nums2) == expected

    # Next Greater Element II Tests
    @pytest.mark.parametrize(
        "nums,expected",
        [
            # Basic circular cases
            ([1, 2, 1], [2, -1, 2]),
            ([1, 2, 3, 4, 3], [2, 3, 4, -1, 4]),
            ([5, 4, 3, 2, 1], [-1, 5, 5, 5, 5]),
            
            # Single element
            ([1], [-1]),
            
            # All same elements
            ([3, 3, 3], [-1, -1, -1]),
            
            # Ascending order
            ([1, 2, 3, 4, 5], [2, 3, 4, 5, -1]),
            
            # Descending order
            ([5, 4, 3, 2, 1], [-1, 5, 5, 5, 5]),
            
            # Complex circular
            ([100, 1, 11, 1, 120, 111, 123, 1, -1, -100], [120, 11, 120, 120, 123, 123, -1, 100, 100, 100]),
        ]
    )
    def test_next_greater_element_ii(self, nums, expected):
        """Test next_greater_element_ii with various inputs."""
        assert self.solution.next_greater_element_ii(nums) == expected

    # Next Greater Element III Tests
    @pytest.mark.parametrize(
        "n,expected",
        [
            # Basic cases
            (12, 21),
            (21, -1),
            (12443322, 13222344),
            (1234, 1243),
            
            # Single digit
            (1, -1),
            (5, -1),
            
            # Already largest permutation
            (4321, -1),
            (987654321, -1),
            
            # Small numbers
            (12, 21),
            (123, 132),
            (321, -1),
            
            # Numbers with repeating digits
            (1122, 1212),
            (2143, 2314),
            
            # Edge case - results in overflow
            (2147483647, -1),  # Max 32-bit integer
        ]
    )
    def test_next_greater_element_iii(self, n, expected):
        """Test next_greater_element_iii with various inputs."""
        assert self.solution.next_greater_element_iii(n) == expected

    def test_next_greater_element_i_empty_cases(self):
        """Test edge cases for next_greater_element_i."""
        # Empty nums1
        assert self.solution.next_greater_element_i([], [1, 2, 3]) == []
        
        # nums1 elements not in nums2 (though this violates problem constraints)
        # In a real scenario, this wouldn't happen, but testing robustness
        result = self.solution.next_greater_element_i([5], [1, 2, 3, 4])
        assert result == [-1]

    def test_next_greater_element_ii_edge_cases(self):
        """Test edge cases for next_greater_element_ii."""
        # Two elements
        assert self.solution.next_greater_element_ii([1, 2]) == [2, -1]
        assert self.solution.next_greater_element_ii([2, 1]) == [-1, 2]
        
        # Large numbers
        large_nums = [1000000, 999999, 1000001]
        expected = [1000001, 1000001, -1]
        assert self.solution.next_greater_element_ii(large_nums) == expected

    def test_next_greater_element_iii_edge_cases(self):
        """Test edge cases for next_greater_element_iii."""
        # Numbers resulting in 32-bit integer overflow
        assert self.solution.next_greater_element_iii(1999999999) == -1
        
        # Very small valid cases
        assert self.solution.next_greater_element_iii(10) == -1
        assert self.solution.next_greater_element_iii(13) == 31
        
        # Numbers with all same digits
        assert self.solution.next_greater_element_iii(1111) == -1
        assert self.solution.next_greater_element_iii(2222) == -1

    def test_performance_cases(self):
        """Test performance with larger inputs."""
        # Large array for next_greater_element_ii
        large_array = list(range(1000)) + list(range(999, -1, -1))
        result = self.solution.next_greater_element_ii(large_array)
        assert len(result) == len(large_array)
        
        # For ascending part, each element should find next element
        for i in range(999):
            assert result[i] == i + 1
        
        # The peak element (999) is the maximum, so it has no next greater
        assert result[999] == -1
        # The duplicate 999 at index 1000 also has no next greater
        assert result[1000] == -1

    def test_algorithm_correctness(self):
        """Test specific algorithmic correctness scenarios."""
        # Test that circular property works correctly
        nums = [2, 1, 2, 4, 3, 1]
        expected = [4, 2, 4, -1, 4, 2]
        assert self.solution.next_greater_element_ii(nums) == expected
        
        # Test next permutation logic
        assert self.solution.next_greater_element_iii(12321) == 13122
        assert self.solution.next_greater_element_iii(54321) == -1


if __name__ == "__main__":
    pytest.main([__file__])
