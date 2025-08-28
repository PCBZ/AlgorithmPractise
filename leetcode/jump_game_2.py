"""
LeetCode Problem #45: Jump Game II
https://leetcode.com/problems/jump-game-ii/

Given an array of non-negative integers where each element represents
the maximum jump length at that position, return the minimum number
of jumps to reach the last index.
"""

from typing import List


class Solution:
    """Solution for Jump Game II problem."""

    def jump(self, nums: List[int]) -> int:
        """
        Find minimum number of jumps to reach the last index using greedy approach.
        Time: O(n), Space: O(1)
        """
        if len(nums) <= 1:
            return 0

        jumps = 0
        current_end = 0     # End of current jump range
        farthest = 0        # Farthest position reachable

        # Process all positions except the last
        for i in range(len(nums) - 1):
            # Update farthest reachable position
            farthest = max(farthest, i + nums[i])

            # If we've reached the end of current jump range
            if i == current_end:
                jumps += 1
                current_end = farthest

                # Early exit if we can reach the end
                if current_end >= len(nums) - 1:
                    break

        return jumps


if __name__ == '__main__':
    test_nums = [2, 3, 1, 1, 4]
    print(Solution().jump(test_nums))  # Expected: 2
