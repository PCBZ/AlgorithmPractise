"""
LeetCode #209: Minimum Size Subarray Sum

Find the minimal length of a contiguous subarray whose sum is greater than or equal to target.

Time: O(n), Space: O(1)
"""
from typing import List


class Solution:
    """Find minimum size subarray sum using sliding window technique."""

    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        """Find minimal length of contiguous subarray with sum >= target."""
        if not nums or target <= 0:
            return 0

        n = len(nums)
        left = 0
        right = 0
        cur_sum = 0
        min_len = float('inf')

        while right < n:
            cur_sum += nums[right]
            while cur_sum >= target:
                cur_len = right - left + 1
                min_len = min(min_len, cur_len)
                cur_sum -= nums[left]
                left += 1
            right += 1

        return min_len if min_len < float('inf') else 0


if __name__ == "__main__":
    TEST_NUMS = [1, 1, 1, 1, 1, 1, 1]
    TEST_TARGET = 11
    solution = Solution()
    result = solution.minSubArrayLen(TEST_TARGET, TEST_NUMS)
    print(f"Input: target={TEST_TARGET}, nums={TEST_NUMS}")
    print(f"Output: {result}")
