"""
LeetCode Problem #53: Maximum Subarray
URL: https://leetcode.com/problems/maximum-subarray/
"""


class Solution:
    """Solution for maximum subarray problem using Kadane's algorithm."""

    def maxSubArray(self, nums):
        """Find the maximum sum of a contiguous subarray."""
        cur_max = global_max = float('-inf')
        for num in nums:
            cur_max = max(cur_max + num, num)
            global_max = max(global_max, cur_max)
        return global_max


if __name__ == '__main__':
    TEST_NUMS = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print(Solution().maxSubArray(TEST_NUMS))  # 6
