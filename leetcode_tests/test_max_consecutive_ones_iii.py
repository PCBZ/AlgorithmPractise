"""
Comprehensive tests for Max Consecutive Ones III problem.

Tests all implementations: sliding window, optimized, and brute force approaches.
"""
import copy
import pytest
import sys
import os

# Add parent directory to path for imports
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Import using importlib to handle module name with numbers
import importlib.util
spec = importlib.util.spec_from_file_location(
    "max_consecutive_ones_iii", 
    "/Users/wenshuangzhou/Developer/AlgorithmPractise/leetcode/Max_Consecutive_Ones_III.py"
)
max_consecutive_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(max_consecutive_module)
Solution = max_consecutive_module.Solution


class TestMaxConsecutiveOnesIII:
    """Test class for max consecutive ones III implementations."""

    def setup_method(self):
        """Set up test fixtures before each test method."""
        self.solution = Solution()

    @pytest.fixture
    def leetcode_example_1(self):
        """First LeetCode example."""
        return [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], 2

    @pytest.fixture
    def leetcode_example_2(self):
        """Second LeetCode example."""
        return [0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1], 3

    @pytest.fixture
    def all_zeros(self):
        """Array with all zeros."""
        return [0, 0, 0, 0, 0], 3

    @pytest.fixture
    def all_ones(self):
        """Array with all ones."""
        return [1, 1, 1, 1, 1], 0

    @pytest.fixture
    def single_element(self):
        """Single element arrays."""
        return [([0], 1), ([1], 0), ([0], 0), ([1], 1)]

    def test_leetcode_example_1(self, leetcode_example_1):
        """Test first LeetCode example."""
        nums, k = leetcode_example_1
        result = self.solution.longest_ones(nums, k)
        assert result == 6  # Flip zeros at indices 3,4 to get 6 consecutive ones

    def test_leetcode_example_2(self, leetcode_example_2):
        """Test second LeetCode example."""
        nums, k = leetcode_example_2
        result = self.solution.longest_ones(nums, k)
        assert result == 10  # Expected result from LeetCode

    def test_all_zeros_array(self, all_zeros):
        """Test array with all zeros."""
        nums, k = all_zeros
        result = self.solution.longest_ones(nums, k)
        assert result == 3  # Can flip at most k=3 zeros

    def test_all_ones_array(self, all_ones):
        """Test array with all ones."""
        nums, k = all_ones
        result = self.solution.longest_ones(nums, k)
        assert result == 5  # All elements are already ones

    def test_single_element_arrays(self, single_element):
        """Test single element arrays."""
        test_cases = single_element
        for nums, k in test_cases:
            result = self.solution.longest_ones(nums, k)
            if nums[0] == 1 or k >= 1:
                assert result == 1
            else:
                assert result == 0

    def test_empty_array(self):
        """Test empty array."""
        result = self.solution.longest_ones([], 2)
        assert result == 0

    def test_k_zero(self):
        """Test when k=0 (no flips allowed)."""
        nums = [1, 0, 1, 1, 0, 1]
        result = self.solution.longest_ones(nums, 0)
        assert result == 2  # Maximum consecutive ones without flipping

    def test_k_greater_than_zeros(self):
        """Test when k is greater than number of zeros."""
        nums = [1, 0, 1, 0, 1]
        k = 5  # More than the 2 zeros in array
        result = self.solution.longest_ones(nums, k)
        assert result == 5  # Can flip all zeros

    def test_alternating_pattern(self):
        """Test alternating 0s and 1s."""
        nums = [0, 1, 0, 1, 0, 1, 0]
        k = 2
        result = self.solution.longest_ones(nums, k)
        assert result == 5  # Flip 2 zeros to get 5 consecutive ones

    def test_consecutive_zeros_at_start(self):
        """Test array starting with consecutive zeros."""
        nums = [0, 0, 0, 1, 1, 1]
        k = 2
        result = self.solution.longest_ones(nums, k)
        assert result == 5  # Flip first 2 zeros

    def test_consecutive_zeros_at_end(self):
        """Test array ending with consecutive zeros."""
        nums = [1, 1, 1, 0, 0, 0]
        k = 2
        result = self.solution.longest_ones(nums, k)
        assert result == 5  # Flip last 2 zeros

    def test_zeros_in_middle(self):
        """Test zeros in the middle of array."""
        nums = [1, 1, 0, 0, 0, 1, 1]
        k = 1
        result = self.solution.longest_ones(nums, k)
        assert result == 3  # Can flip one zero to get 3 consecutive ones

    def test_large_array(self):
        """Test with larger array."""
        nums = [1] * 100 + [0] * 5 + [1] * 100
        k = 3
        result = self.solution.longest_ones(nums, k)
        assert result == 103  # 100 ones + 3 flipped zeros (best we can do with k=3)

    def test_optimized_method_consistency(self, leetcode_example_1):
        """Test optimized method gives same result."""
        nums, k = leetcode_example_1
        standard_result = self.solution.longest_ones(nums, k)
        optimized_result = self.solution.longest_ones_optimized(nums, k)
        assert standard_result == optimized_result

    def test_brute_force_consistency(self):
        """Test brute force method for smaller arrays."""
        test_cases = [
            ([1, 0, 1, 1, 0], 1),
            ([0, 0, 1, 1], 1),
            ([1, 1, 1], 0),
            ([0, 0, 0], 2),
        ]
        
        for nums, k in test_cases:
            standard = self.solution.longest_ones(nums, k)
            brute_force = self.solution.longest_ones_brute_force(nums, k)
            optimized = self.solution.longest_ones_optimized(nums, k)
            
            assert standard == brute_force == optimized

    def test_all_methods_consistency(self, leetcode_example_2):
        """Test all three methods give same results."""
        nums, k = leetcode_example_2
        
        result1 = self.solution.longest_ones(nums, k)
        result2 = self.solution.longest_ones_optimized(nums, k)
        result3 = self.solution.longest_ones_brute_force(nums, k)
        
        assert result1 == result2 == result3

    def test_with_positions_method(self):
        """Test the method that returns positions."""
        nums = [1, 0, 1, 1, 0, 1]
        k = 1
        
        length, start, end = self.solution.longest_ones_with_positions(nums, k)
        
        # Verify the result makes sense
        assert length > 0
        assert 0 <= start <= end < len(nums)
        assert end - start + 1 == length
        
        # Verify it matches the standard method
        standard_result = self.solution.longest_ones(nums, k)
        assert length == standard_result

    def test_count_max_consecutive_ones(self):
        """Test bonus method for counting consecutive ones without flips."""
        nums = [1, 1, 0, 1, 1, 1, 0, 1]
        result = self.solution.count_max_consecutive_ones(nums)
        assert result == 3  # Three consecutive ones

    def test_edge_case_positions_empty(self):
        """Test positions method with empty array."""
        length, start, end = self.solution.longest_ones_with_positions([], 1)
        assert length == 0
        assert start == -1
        assert end == -1

    def test_performance_pattern(self):
        """Test specific pattern for performance validation."""
        # Pattern that could cause issues with naive sliding window
        nums = [1, 0] * 1000  # Alternating pattern
        k = 500
        
        result = self.solution.longest_ones(nums, k)
        # Should be able to handle this efficiently
        assert result > 0
        assert isinstance(result, int)

    def test_boundary_conditions(self):
        """Test various boundary conditions."""
        # k equals number of zeros
        nums = [1, 0, 1, 0, 1]
        k = 2
        result = self.solution.longest_ones(nums, k)
        assert result == 5  # Can flip all zeros
        
        # k is 1 less than number of zeros
        k = 1
        result = self.solution.longest_ones(nums, k)
        assert result == 3  # Best we can do with 1 flip

    def test_complex_mixed_pattern(self):
        """Test complex pattern with mixed lengths."""
        nums = [1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1]
        k = 2
        
        result1 = self.solution.longest_ones(nums, k)
        result2 = self.solution.longest_ones_optimized(nums, k)
        result3 = self.solution.longest_ones_brute_force(nums, k)
        
        # All methods should agree
        assert result1 == result2 == result3
        # Result should be reasonable
        assert result1 >= k  # At minimum, we can flip k zeros

    def test_stress_consistency(self):
        """Stress test with multiple random-like patterns."""
        patterns = [
            [1, 0, 1, 0, 1, 0, 1, 0],
            [0, 1, 0, 1, 0, 1, 0, 1],
            [1, 1, 0, 0, 1, 1, 0, 0],
            [0, 0, 1, 1, 0, 0, 1, 1],
        ]
        
        for nums in patterns:
            for k in range(5):
                standard = self.solution.longest_ones(nums, k)
                optimized = self.solution.longest_ones_optimized(nums, k)
                
                assert standard == optimized
                assert standard >= 0
                assert standard <= len(nums)


if __name__ == "__main__":
    pytest.main([__file__])
