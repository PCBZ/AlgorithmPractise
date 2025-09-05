"""
LeetCode 673: Number of Longest Increasing Subsequence
https://leetcode.com/problems/number-of-longest-increasing-subsequence/

Find the number of longest increasing subsequences.
"""

from typing import List


class Solution:
    """Solution for Number of Longest Increasing Subsequence problem."""

    def findNumberOfLIS(self, nums: List[int]) -> int:  # pylint: disable=invalid-name
        """Find number of longest increasing subsequences using DP."""
        if not nums:
            return 0

        n = len(nums)
        lengths = [1] * n  # Length of LIS ending at each position
        counts = [1] * n   # Count of LIS ending at each position

        for i in range(n):
            for j in range(i):
                if nums[i] > nums[j]:
                    if lengths[j] + 1 > lengths[i]:
                        lengths[i] = lengths[j] + 1
                        counts[i] = counts[j]
                    elif lengths[j] + 1 == lengths[i]:
                        counts[i] += counts[j]

        max_length = max(lengths)
        return sum(counts[i] for i in range(n) if lengths[i] == max_length)


if __name__ == "__main__":
    solution = Solution()
    test_nums = [1, 3, 5, 4, 7]
    print(solution.findNumberOfLIS(test_nums))
