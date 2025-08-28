"""
LeetCode Problem #532: K-diff Pairs in an Array
https://leetcode.com/problems/k-diff-pairs-in-an-array/

Given an array of integers and an integer k, find the number of unique k-diff pairs.
A k-diff pair is (nums[i], nums[j]) where |nums[i] - nums[j]| = k and i != j.
"""

from typing import List
from collections import Counter


class Solution:
    """Solution for K-diff Pairs in an Array problem."""

    def findPairs(self, nums: List[int], k: int) -> int:
        """
        Find unique k-diff pairs using hash set approach.
        Time: O(n), Space: O(n)
        """
        if k < 0:
            return 0

        counter = Counter(nums)
        count = 0

        for num in counter:
            if k == 0:
                # Special case: find duplicates
                if counter[num] >= 2:
                    count += 1
            else:
                # Check if num + k exists
                if num + k in counter:
                    count += 1

        return count


if __name__ == "__main__":
    test_nums = [3, 1, 4, 1, 5]
    test_k = 2
    print(Solution().findPairs(test_nums, test_k))
