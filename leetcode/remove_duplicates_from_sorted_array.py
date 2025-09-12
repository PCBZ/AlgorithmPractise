"""
LeetCode 26: Remove Duplicates from Sorted Array

Given an integer array nums sorted in non-decreasing order, remove the duplicates
in-place such that each unique element appears only once. The relative order of
the elements should be kept the same. Then return the number of unique elements in nums.

URL: https://leetcode.com/problems/remove-duplicates-from-sorted-array/
"""

from typing import List


class Solution:  # pylint: disable=too-few-public-methods
    """Solution for Remove Duplicates from Sorted Array problem."""

    def removeDuplicates(self, nums: List[int]) -> int:  # pylint: disable=invalid-name
        """
        Remove duplicates from sorted array in-place.
        Time: O(n), Space: O(1)
        """
        if not nums:
            return 0

        write_pos = 0

        for read_pos in range(1, len(nums)):
            if nums[read_pos] != nums[write_pos]:
                write_pos += 1
                nums[write_pos] = nums[read_pos]

        return write_pos + 1


if __name__ == "__main__":
    sol = Solution()

    NUMS1 = [1, 1, 2]
    RESULT1 = sol.removeDuplicates(NUMS1)
    print(f"Test 1: {RESULT1}, array: {NUMS1[:RESULT1]}")

    NUMS2 = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    RESULT2 = sol.removeDuplicates(NUMS2)
    print(f"Test 2: {RESULT2}, array: {NUMS2[:RESULT2]}")

    NUMS3 = [1]
    RESULT3 = sol.removeDuplicates(NUMS3)
    print(f"Test 3: {RESULT3}, array: {NUMS3[:RESULT3]}")
