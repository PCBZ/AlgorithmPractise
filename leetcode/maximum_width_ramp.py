
"""
LeetCode #962: Maximum Width Ramp
https://leetcode.com/problems/maximum-width-ramp/
"""

from typing import List

class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        """Return the maximum width ramp in nums."""
        n = len(nums)
        stack = []
        # Build decreasing stack of indices
        for i in range(n):
            if not stack or nums[i] < nums[stack[-1]]:
                stack.append(i)
        max_ramp = 0
        # Scan from right, pop stack when ramp found
        for j in reversed(range(n)):
            while stack and nums[j] >= nums[stack[-1]]:
                max_ramp = max(max_ramp, j - stack[-1])
                stack.pop()
        return max_ramp


if __name__ == "__main__":
    test_cases = [
        ([6,0,8,2,1,5], 4),
        ([9,8,1,0,1,9,4,0,4,1], 7),
        ([1,2,3,4,5], 4),
        ([5,4,3,2,1], 0),
        ([1,1,1,1,1], 4),
        ([0], 0),
    ]
    sol = Solution()
    for nums, expected in test_cases:
        result = sol.maxWidthRamp(nums)
        print(f"Input: {nums}\nMax Width Ramp: {result} (Expected: {expected})\n")