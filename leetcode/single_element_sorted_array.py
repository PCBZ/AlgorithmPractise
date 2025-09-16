"""
LeetCode 540: Single Element in a Sorted Array

You are given a sorted array consisting of only integers where every element 
appears exactly twice, except for one element which appears exactly once.

Return the single element that appears only once.
Your solution must run in O(log n) time and O(1) space.

URL: https://leetcode.com/problems/single-element-in-a-sorted-array/
"""

from typing import List


class Solution:  # pylint: disable=too-few-public-methods
    """Solution using binary search to find the single element."""
    def singleNonDuplicate(self, nums: List[int]) -> int:  # pylint: disable=invalid-name
        """
        Find the single element using binary search (corrected implementation).
        Time: O(log n), Space: O(1)
        """
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            # Ensure mid is even for pair comparison
            if mid % 2 == 1:
                mid -= 1
            if nums[mid] == nums[mid + 1]:
                left = mid + 2
            else:
                right = mid
        return nums[left]

if __name__ == "__main__":
    solution = Solution()

    # Test cases
    test_cases = [
        [1, 1, 2, 3, 3, 4, 4, 8, 8],
        [3, 3, 7, 7, 10, 11, 11],
        [1],
        [1, 1, 2],
        [0, 1, 1],
        [1, 2, 2, 3, 3, 4, 4]
    ]

    for i, test_nums in enumerate(test_cases):
        result = solution.singleNonDuplicate(test_nums)
        print(f"Test {i+1}: {test_nums} -> {result}")
