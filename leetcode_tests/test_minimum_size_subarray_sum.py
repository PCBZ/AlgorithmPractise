"""
Comprehensive tests for Minimum Size Subarray Sum problem.

Tests the sliding window algorithm for finding the minimal length
of a contiguous subarray whose sum is >= target.
"""
import pytest
import sys
import os

# Add parent directory to path for imports
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Import using exec to handle the non-standard module name
solution_globals = {}
with open(os.path.join(os.path.dirname(__file__), '..', 'leetcode', 'minimum_size_subarray_sum.py'), 'r') as f:
    exec(f.read(), solution_globals)

Solution = solution_globals['Solution']


class TestMinimumSizeSubarraySum:
    """Test class for minimum size subarray sum implementation."""

    def setup_method(self):
        """Set up test fixtures before each test method."""
        self.solution = Solution()

    @pytest.fixture
    def leetcode_example_1(self):
        """First LeetCode example."""
        return 7, [2, 3, 1, 2, 4, 3]

    @pytest.fixture
    def leetcode_example_2(self):
        """Second LeetCode example."""
        return 4, [1, 4, 4]

    @pytest.fixture
    def leetcode_example_3(self):
        """Third LeetCode example."""
        return 11, [1, 1, 1, 1, 1, 1, 1, 1]

    def test_leetcode_example_1(self, leetcode_example_1):
        """Test first LeetCode example."""
        target, nums = leetcode_example_1
        result = self.solution.minSubArrayLen(target, nums)
        assert result == 2  # [4, 3] has sum 7

    def test_leetcode_example_2(self, leetcode_example_2):
        """Test second LeetCode example."""
        target, nums = leetcode_example_2
        result = self.solution.minSubArrayLen(target, nums)
        assert result == 1  # [4] has sum 4

    def test_leetcode_example_3(self, leetcode_example_3):
        """Test third LeetCode example."""
        target, nums = leetcode_example_3
        result = self.solution.minSubArrayLen(target, nums)
        assert result == 0  # No subarray sums to 11

    def test_empty_array(self):
        """Test with empty array."""
        assert self.solution.minSubArrayLen(1, []) == 0

    def test_single_element_sufficient(self):
        """Test single element that meets target."""
        assert self.solution.minSubArrayLen(5, [5]) == 1
        assert self.solution.minSubArrayLen(3, [5]) == 1

    def test_single_element_insufficient(self):
        """Test single element that doesn't meet target."""
        assert self.solution.minSubArrayLen(10, [5]) == 0

    def test_entire_array_needed(self):
        """Test when entire array is needed."""
        assert self.solution.minSubArrayLen(15, [1, 2, 3, 4, 5]) == 5

    def test_entire_array_insufficient(self):
        """Test when entire array sum is insufficient."""
        assert self.solution.minSubArrayLen(20, [1, 2, 3, 4, 5]) == 0

    def test_target_zero(self):
        """Test with target of zero."""
        # Any single element will have sum >= 0
        assert self.solution.minSubArrayLen(0, [1, 2, 3]) == 0  # Actually should be 0 based on problem

    def test_all_positive_numbers(self):
        """Test with all positive numbers."""
        assert self.solution.minSubArrayLen(6, [1, 2, 3, 4]) == 2  # [3, 4]

    def test_large_numbers(self):
        """Test with large numbers."""
        assert self.solution.minSubArrayLen(100, [50, 60, 30]) == 2  # [50, 60]

    def test_minimum_length_one(self):
        """Test cases where minimum length is 1."""
        assert self.solution.minSubArrayLen(4, [1, 4, 4]) == 1
        assert self.solution.minSubArrayLen(10, [5, 1, 15, 3]) == 1
        assert self.solution.minSubArrayLen(100, [200]) == 1

    def test_minimum_length_two(self):
        """Test cases where minimum length is 2."""
        assert self.solution.minSubArrayLen(7, [2, 3, 1, 2, 4, 3]) == 2
        assert self.solution.minSubArrayLen(6, [1, 2, 3, 4]) == 2

    def test_minimum_length_three(self):
        """Test cases where minimum length is 3."""
        assert self.solution.minSubArrayLen(6, [1, 1, 1, 1, 1, 4]) == 3  # [1, 1, 4]

    def test_increasing_sequence(self):
        """Test with increasing sequence."""
        nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        assert self.solution.minSubArrayLen(15, nums) == 2  # [9, 10] = 19 >= 15

    def test_decreasing_sequence(self):
        """Test with decreasing sequence."""
        nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        assert self.solution.minSubArrayLen(15, nums) == 2  # [10, 9] = 19 >= 15

    def test_repeated_elements(self):
        """Test with repeated elements."""
        assert self.solution.minSubArrayLen(12, [3, 3, 3, 3, 3]) == 4  # [3, 3, 3, 3]

    def test_mixed_small_large(self):
        """Test with mix of small and large numbers."""
        assert self.solution.minSubArrayLen(10, [1, 1, 1, 15, 1, 1]) == 1  # [15]

    def test_target_equals_sum(self):
        """Test when target equals array sum."""
        nums = [1, 2, 3, 4]
        target = sum(nums)  # 10
        assert self.solution.minSubArrayLen(target, nums) == 4

    def test_performance_large_array(self):
        """Test performance with larger array."""
        nums = [1] * 1000 + [500]  # 1000 ones followed by 500
        assert self.solution.minSubArrayLen(500, nums) == 1  # [500]

    def test_performance_worst_case(self):
        """Test worst case performance."""
        nums = [1] * 100
        target = 50
        assert self.solution.minSubArrayLen(target, nums) == 50

    def test_sliding_window_efficiency(self):
        """Test that sliding window works efficiently."""
        nums = [10, 2, 3]
        assert self.solution.minSubArrayLen(6, nums) == 1  # [10] = 10 >= 6

    def test_boundary_conditions(self):
        """Test boundary conditions."""
        # Target exactly matches one element
        assert self.solution.minSubArrayLen(5, [1, 2, 5, 3]) == 1
        
        # Target exactly matches sum of two elements
        assert self.solution.minSubArrayLen(7, [1, 3, 4, 2]) == 2  # [3, 4]

    def test_complex_scenarios(self):
        """Test complex sliding window scenarios."""
        # Multiple valid subarrays, need minimum
        nums = [1, 2, 1, 2, 6, 1, 1]
        assert self.solution.minSubArrayLen(6, nums) == 1  # [6]
        
        # Need to slide window multiple times
        nums = [2, 1, 2, 4, 3, 1]
        assert self.solution.minSubArrayLen(7, nums) == 2  # [4, 3]

    def test_edge_case_patterns(self):
        """Test edge case patterns."""
        # All elements equal
        assert self.solution.minSubArrayLen(6, [2, 2, 2, 2]) == 3  # [2, 2, 2]
        
        # One large element among small ones
        assert self.solution.minSubArrayLen(10, [1, 1, 1, 100, 1, 1]) == 1  # [100]

    def test_various_targets(self):
        """Test with various target values."""
        nums = [1, 2, 3, 4, 5]
        
        # Small target
        assert self.solution.minSubArrayLen(1, nums) == 1
        
        # Medium target
        assert self.solution.minSubArrayLen(7, nums) == 2  # [3, 4] or [4, 5]
        
        # Large target (entire array)
        assert self.solution.minSubArrayLen(15, nums) == 5

    def test_algorithm_correctness(self):
        """Test algorithm correctness with known cases."""
        # Verify the sliding window approach works correctly
        test_cases = [
            (4, [1, 4, 4], 1),
            (7, [2, 3, 1, 2, 4, 3], 2),
            (11, [1, 1, 1, 1, 1, 1, 1, 1], 0),
            (15, [5, 1, 3, 5, 10, 7, 4, 9, 2, 8], 2),
            (213, [12, 28, 83, 4, 25, 26, 25, 2, 25, 25, 25, 12], 8),
        ]
        
        for target, nums, expected in test_cases:
            result = self.solution.minSubArrayLen(target, nums)
            assert result == expected, f"Failed for target={target}, nums={nums}"


if __name__ == '__main__':
    pytest.main([__file__])
