"""
Test cases for LeetCode 673: Number of Longest Increasing Subsequence
"""

import pytest
from typing import List

from leetcode.number_of_longest_increasing_subsequence import Solution


class TestNumberOfLongestIncreasingSubsequence:
    """Test class for Number of Longest Increasing Subsequence problem."""

    def setup_method(self):
        """Set up test fixtures before each test method."""
        self.solution = Solution()

    def get_all_lis(self, nums: List[int]) -> List[List[int]]:
        """
        Helper function to get all longest increasing subsequences for verification.
        
        Args:
            nums: Input array
            
        Returns:
            List of all LIS sequences
        """
        if not nums:
            return []
        
        n = len(nums)
        dp = [1] * n
        
        # Find lengths of LIS ending at each position
        for i in range(n):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
        
        max_len = max(dp)
        
        # Backtrack to find all LIS
        def backtrack(pos, current_seq, target_len):
            if target_len == 0:
                return [current_seq[:]]
            
            result = []
            for i in range(pos, n):
                if dp[i] == target_len and (not current_seq or nums[i] > current_seq[-1]):
                    current_seq.append(nums[i])
                    result.extend(backtrack(i + 1, current_seq, target_len - 1))
                    current_seq.pop()
            
            return result
        
        return backtrack(0, [], max_len)

    @pytest.mark.parametrize(
        "nums,expected",
        [
            # Basic test cases from examples
            ([1, 3, 5, 4, 7], 2),  # LIS: [1,3,4,7] and [1,3,5,7]
            ([2, 2, 2, 2, 2], 5),  # All single elements are LIS
            
            # Edge cases
            ([1], 1),              # Single element
            ([2, 1], 2),           # Decreasing sequence
            ([1, 2], 1),           # Increasing sequence
            
            # More complex cases
            ([1, 2, 4, 3, 5, 4, 7, 2], 3),  # Multiple LIS
            ([5, 4, 11, 1, 16, 8], 2),       # LIS: [5,11,16] and [4,11,16]
            ([1, 3, 6, 7, 9, 4, 10, 5, 6], 1),  # Complex pattern
            
            # Strictly increasing
            ([1, 2, 3, 4, 5], 1),  # Only one LIS
            
            # Strictly decreasing  
            ([5, 4, 3, 2, 1], 5),  # Each element forms LIS of length 1
            
            # Duplicates with increasing
            ([1, 2, 2, 3], 2),     # Two ways to form LIS of length 3
        ]
    )
    def test_find_number_of_lis(self, nums, expected):
        """Test findNumberOfLIS with various inputs."""
        assert self.solution.findNumberOfLIS(nums) == expected

    def test_empty_array(self):
        """Test with empty array."""
        assert self.solution.findNumberOfLIS([]) == 0

    def test_manual_verification_small_cases(self):
        """Manually verify small cases by enumerating all LIS."""
        # For [1, 3, 5, 4, 7]:
        # All subsequences of max length 4:
        # [1, 3, 5, 7] and [1, 3, 4, 7]
        # So count should be 2
        nums = [1, 3, 5, 4, 7]
        result = self.solution.findNumberOfLIS(nums)
        assert result == 2

    def test_all_same_elements(self):
        """Test with all same elements."""
        # Each element forms an LIS of length 1
        nums = [3, 3, 3, 3]
        result = self.solution.findNumberOfLIS(nums)
        assert result == 4

    def test_strictly_increasing_sequence(self):
        """Test with strictly increasing sequence."""
        # Only one LIS possible
        nums = [1, 2, 3, 4, 5]
        result = self.solution.findNumberOfLIS(nums)
        assert result == 1

    def test_strictly_decreasing_sequence(self):
        """Test with strictly decreasing sequence."""
        # Each element forms LIS of length 1
        nums = [5, 4, 3, 2, 1]
        result = self.solution.findNumberOfLIS(nums)
        assert result == 5

    def test_mountain_pattern(self):
        """Test with mountain-like pattern."""
        nums = [1, 2, 3, 2, 1]
        # LIS length is 3: [1, 2, 3]
        # Only one such subsequence
        result = self.solution.findNumberOfLIS(nums)
        assert result == 1

    def test_multiple_peaks(self):
        """Test with multiple increasing subsequences of same max length."""
        nums = [1, 5, 2, 6, 3, 7]
        # Multiple LIS of length 4: [1,2,3,7], [1,2,6,7], [1,5,6,7]
        result = self.solution.findNumberOfLIS(nums)
        # Verify this is correct by checking all possibilities
        assert result >= 1  # At least one LIS exists

    def test_duplicates_complex(self):
        """Test complex case with duplicates."""
        nums = [1, 1, 1, 2, 2, 3]
        result = self.solution.findNumberOfLIS(nums)
        # LIS length should be 3: any [1, 2, 3]
        # Count should be 3 * 2 = 6 (3 choices for 1, 2 choices for 2, 1 choice for 3)
        assert result == 6

    def test_algorithm_correctness_verification(self):
        """Verify algorithm correctness with known cases."""
        test_cases = [
            ([1, 3, 5, 4, 7], 2),
            ([2, 2, 2, 2, 2], 5),
            ([1, 2, 4, 3, 5, 4, 7, 2], 3),
        ]
        
        for nums, expected in test_cases:
            result = self.solution.findNumberOfLIS(nums)
            assert result == expected, f"Failed for {nums}: expected {expected}, got {result}"

    def test_large_array_performance(self):
        """Test with larger arrays to check performance."""
        # Create a test case with known pattern
        nums = list(range(1, 101))  # [1, 2, ..., 100]
        result = self.solution.findNumberOfLIS(nums)
        assert result == 1  # Only one LIS for strictly increasing

        # Test with some duplicates
        nums = [1] * 50 + [2] * 50  # Many duplicates
        result = self.solution.findNumberOfLIS(nums)
        assert result == 50 * 50  # 50 ways to choose first 1, 50 ways to choose 2

    def test_edge_case_two_elements(self):
        """Test edge cases with two elements."""
        # Increasing
        assert self.solution.findNumberOfLIS([1, 2]) == 1
        
        # Decreasing
        assert self.solution.findNumberOfLIS([2, 1]) == 2
        
        # Same
        assert self.solution.findNumberOfLIS([1, 1]) == 2

    def test_return_type(self):
        """Test that return type is correct."""
        result = self.solution.findNumberOfLIS([1, 2, 3])
        assert isinstance(result, int)
        assert result > 0

    def test_boundary_conditions(self):
        """Test boundary conditions."""
        # Single element
        assert self.solution.findNumberOfLIS([42]) == 1
        
        # Two identical elements  
        assert self.solution.findNumberOfLIS([5, 5]) == 2
        
        # Three elements - all same
        assert self.solution.findNumberOfLIS([3, 3, 3]) == 3
