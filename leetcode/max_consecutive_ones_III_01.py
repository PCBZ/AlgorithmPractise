"""
LeetCode Problem #1004: Max Consecutive Ones III
URL: https://leetcode.com/problems/max-consecutive-ones-iii/
"""
from typing import List


class Solution:
    """Solution for max consecutive ones III problem."""

    def longest_ones(self, nums: List[int], k: int) -> int:
        """Find maximum consecutive 1s after flipping at most k zeros."""
        n = len(nums)
        left = 0
        zero_count = 0
        max_len = 0
        for right in range(n):
            if nums[right] == 0:
                zero_count += 1
            while zero_count > k:
                if nums[left] == 0:
                    zero_count -= 1
                left += 1
            max_len = max(max_len, right - left + 1)
        return max_len


if __name__ == "__main__":
    TEST_NUMS = [0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1]
    TEST_K = 3
    print(Solution().longest_ones(TEST_NUMS, TEST_K))
