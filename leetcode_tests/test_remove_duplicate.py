
import pytest
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from leetcode.remove_duplicates_from_sorted_array import Solution


class TestRemoveDuplicates:
    
    def setup_method(self):
        self.solution = Solution()
    
    def test_example_1(self):
        nums = [1, 1, 2]
        result = self.solution.removeDuplicates(nums)
        assert result == 2
        assert nums[:result] == [1, 2]
    
    def test_example_2(self):
        nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
        result = self.solution.removeDuplicates(nums)
        assert result == 5
        assert nums[:result] == [0, 1, 2, 3, 4]
    
    def test_empty_array(self):
        nums = []
        result = self.solution.removeDuplicates(nums)
        assert result == 0
    
    def test_single_element(self):
        nums = [1]
        result = self.solution.removeDuplicates(nums)
        assert result == 1
        assert nums[:result] == [1]
    
    def test_no_duplicates(self):
        nums = [1, 2, 3, 4, 5]
        result = self.solution.removeDuplicates(nums)
        assert result == 5
        assert nums[:result] == [1, 2, 3, 4, 5]
    
    def test_all_duplicates(self):
        nums = [1, 1, 1, 1, 1]
        result = self.solution.removeDuplicates(nums)
        assert result == 1
        assert nums[:result] == [1]
    
    def test_two_elements_same(self):
        nums = [1, 1]
        result = self.solution.removeDuplicates(nums)
        assert result == 1
        assert nums[:result] == [1]
    
    def test_two_elements_different(self):
        nums = [1, 2]
        result = self.solution.removeDuplicates(nums)
        assert result == 2
        assert nums[:result] == [1, 2]
    
    def test_negative_numbers(self):
        nums = [-3, -1, -1, 0, 0, 0, 0, 1, 1, 2]
        result = self.solution.removeDuplicates(nums)
        assert result == 5
        assert nums[:result] == [-3, -1, 0, 1, 2]
    
    def test_large_gaps(self):
        nums = [1, 1, 1, 100, 100, 1000]
        result = self.solution.removeDuplicates(nums)
        assert result == 3
        assert nums[:result] == [1, 100, 1000]
    
    def test_consecutive_pairs(self):
        nums = [1, 1, 2, 2, 3, 3, 4, 4]
        result = self.solution.removeDuplicates(nums)
        assert result == 4
        assert nums[:result] == [1, 2, 3, 4]
    
    def test_multiple_consecutive_duplicates(self):
        nums = [1, 1, 1, 2, 2, 2, 2, 3, 3]
        result = self.solution.removeDuplicates(nums)
        assert result == 3
        assert nums[:result] == [1, 2, 3]
    
    def test_alternating_pattern(self):
        nums = [1, 1, 2, 3, 3, 4, 5, 5]
        result = self.solution.removeDuplicates(nums)
        assert result == 5
        assert nums[:result] == [1, 2, 3, 4, 5]
    
    def test_zero_values(self):
        nums = [0, 0, 0, 1, 1, 2]
        result = self.solution.removeDuplicates(nums)
        assert result == 3
        assert nums[:result] == [0, 1, 2]
    
    def test_large_array(self):
        nums = [1] * 50 + [2] * 30 + [3] * 20
        result = self.solution.removeDuplicates(nums)
        assert result == 3
        assert nums[:result] == [1, 2, 3]
    
    def test_boundary_values(self):
        nums = [-1000, -1000, 0, 1000, 1000]
        result = self.solution.removeDuplicates(nums)
        assert result == 3
        assert nums[:result] == [-1000, 0, 1000]
    
    # Property tests
    def test_result_length_property(self):
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
