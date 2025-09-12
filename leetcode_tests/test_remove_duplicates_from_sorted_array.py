"""
Test cases for LeetCode 26: Remove Duplicates from Sorted Array
Testing two-pointer technique for in-place duplicate removal.
"""

import pytest
from leetcode.remove_duplicates_from_sorted_array import Solution


class TestRemoveDuplicates:
    """Test cases for Remove Duplicates from Sorted Array problem."""
    
    def setup_method(self):
        """Set up test fixtures before each test method."""
        self.solution = Solution()
    
    # Example test cases from LeetCode
    def test_example_1(self):
        """Test [1,1,2] -> 2."""
        nums = [1, 1, 2]
        result = self.solution.removeDuplicates(nums)
        assert result == 2
        assert nums[:result] == [1, 2]
    
    def test_example_2(self):
        """Test [0,0,1,1,1,2,2,3,3,4] -> 5."""
        nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
        result = self.solution.removeDuplicates(nums)
        assert result == 5
        assert nums[:result] == [0, 1, 2, 3, 4]
    
    # Edge cases
    def test_empty_array(self):
        """Test empty array."""
        nums = []
        result = self.solution.removeDuplicates(nums)
        assert result == 0
    
    def test_single_element(self):
        """Test single element array."""
        nums = [1]
        result = self.solution.removeDuplicates(nums)
        assert result == 1
        assert nums[:result] == [1]
    
    def test_no_duplicates(self):
        """Test array with no duplicates."""
        nums = [1, 2, 3, 4, 5]
        result = self.solution.removeDuplicates(nums)
        assert result == 5
        assert nums[:result] == [1, 2, 3, 4, 5]
    
    def test_all_duplicates(self):
        """Test array with all same elements."""
        nums = [1, 1, 1, 1, 1]
        result = self.solution.removeDuplicates(nums)
        assert result == 1
        assert nums[:result] == [1]
    
    def test_two_elements_same(self):
        """Test two identical elements."""
        nums = [1, 1]
        result = self.solution.removeDuplicates(nums)
        assert result == 1
        assert nums[:result] == [1]
    
    def test_two_elements_different(self):
        """Test two different elements."""
        nums = [1, 2]
        result = self.solution.removeDuplicates(nums)
        assert result == 2
        assert nums[:result] == [1, 2]
    
    def test_negative_numbers(self):
        """Test with negative numbers."""
        nums = [-3, -1, -1, 0, 0, 0, 0, 1, 1, 2]
        result = self.solution.removeDuplicates(nums)
        assert result == 5
        assert nums[:result] == [-3, -1, 0, 1, 2]
    
    def test_large_gaps(self):
        """Test with large gaps between unique elements."""
        nums = [1, 1, 1, 100, 100, 1000]
        result = self.solution.removeDuplicates(nums)
        assert result == 3
        assert nums[:result] == [1, 100, 1000]
    
    def test_consecutive_pairs(self):
        """Test consecutive duplicate pairs."""
        nums = [1, 1, 2, 2, 3, 3, 4, 4]
        result = self.solution.removeDuplicates(nums)
        assert result == 4
        assert nums[:result] == [1, 2, 3, 4]
    
    def test_multiple_consecutive_duplicates(self):
        """Test multiple consecutive duplicates."""
        nums = [1, 1, 1, 2, 2, 2, 2, 3, 3]
        result = self.solution.removeDuplicates(nums)
        assert result == 3
        assert nums[:result] == [1, 2, 3]
    
    def test_alternating_pattern(self):
        """Test alternating pattern of duplicates."""
        nums = [1, 1, 2, 3, 3, 4, 5, 5]
        result = self.solution.removeDuplicates(nums)
        assert result == 5
        assert nums[:result] == [1, 2, 3, 4, 5]
    
    def test_zero_values(self):
        """Test with zero values."""
        nums = [0, 0, 0, 1, 1, 2]
        result = self.solution.removeDuplicates(nums)
        assert result == 3
        assert nums[:result] == [0, 1, 2]
    
    def test_large_array(self):
        """Test with larger array."""
        nums = [1] * 50 + [2] * 30 + [3] * 20
        result = self.solution.removeDuplicates(nums)
        assert result == 3
        assert nums[:result] == [1, 2, 3]
    
    def test_boundary_values(self):
        """Test with boundary values."""
        nums = [-1000, -1000, 0, 1000, 1000]
        result = self.solution.removeDuplicates(nums)
        assert result == 3
        assert nums[:result] == [-1000, 0, 1000]
    
    # Property tests
    def test_result_length_property(self):
        """Test that result length is always <= original length."""
        test_cases = [
            [1, 2, 3],
            [1, 1, 1],
            [1, 2, 2, 3],
            [5, 5, 6, 6, 7, 7, 8, 8]
        ]
        
        for nums in test_cases:
            original_length = len(nums)
            result = self.solution.removeDuplicates(nums.copy())
            assert result <= original_length
    
    def test_sorted_property(self):
        """Test that result maintains sorted order."""
        test_cases = [
            [1, 1, 2, 3, 3, 4],
            [0, 0, 1, 1, 1, 2, 2, 3, 3, 4],
            [-5, -3, -3, -1, 0, 0, 2]
        ]
        
        for nums in test_cases:
            nums_copy = nums.copy()
            result = self.solution.removeDuplicates(nums_copy)
            result_array = nums_copy[:result]
            
            # Check if result is sorted
            for i in range(len(result_array) - 1):
                assert result_array[i] < result_array[i + 1]
    
    def test_unique_elements_property(self):
        """Test that result contains only unique elements."""
        test_cases = [
            [1, 1, 2, 2, 3, 3],
            [0, 0, 0, 1, 1, 2],
            [5, 5, 5, 5, 5]
        ]
        
        for nums in test_cases:
            nums_copy = nums.copy()
            result = self.solution.removeDuplicates(nums_copy)
            result_array = nums_copy[:result]
            
            # Check if all elements are unique
            assert len(result_array) == len(set(result_array))


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
