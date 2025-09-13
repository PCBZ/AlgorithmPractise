"""
LeetCode 26: Remove Duplicates from Sorted Array
LeetCode 80: Remove Duplicates from Sorted Array II

URL: https://leetcode.com/problems/remove-duplicates-from-sorted-array/
URL: https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/
"""

from typing import List


class Solution:
    """Solution for Remove Duplicates from Sorted Array problems."""

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

    def removeDuplicatesII(self, nums: List[int]) -> int:  # pylint: disable=invalid-name
        """
        Remove duplicates from sorted array allowing at most 2 duplicates.
        Time: O(n), Space: O(1)
        """
        if not nums:
            return 0

        write_pos = 0
        count = 0

        for i, num in enumerate(nums):
            if i == 0:
                count = 1
                write_pos = 1
            else:
                if num == nums[i-1]:
                    count += 1
                else:
                    count = 1
                if count <= 2:
                    nums[write_pos] = num
                    write_pos += 1

        return write_pos


if __name__ == "__main__":
    sol = Solution()

    # Test LeetCode 26: Remove Duplicates
    print("=== LeetCode 26: Remove Duplicates ===")
    NUMS1 = [1, 1, 2]
    RESULT1 = sol.removeDuplicates(NUMS1)
    print(f"Test 1: {RESULT1}, array: {NUMS1[:RESULT1]}")

    NUMS2 = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    RESULT2 = sol.removeDuplicates(NUMS2)
    print(f"Test 2: {RESULT2}, array: {NUMS2[:RESULT2]}")

    NUMS3 = [1]
    RESULT3 = sol.removeDuplicates(NUMS3)
    print(f"Test 3: {RESULT3}, array: {NUMS3[:RESULT3]}")

    # Test LeetCode 80: Remove Duplicates II
    print("\n=== LeetCode 80: Remove Duplicates II ===")
    NUMS4 = [0, 0, 1, 1, 1, 1, 2, 3, 3]
    RESULT4 = sol.removeDuplicatesII(NUMS4)
    print(f"Test 4: {RESULT4}, array: {NUMS4[:RESULT4]}")

    NUMS5 = [1, 1, 1, 2, 2, 3]
    RESULT5 = sol.removeDuplicatesII(NUMS5)
    print(f"Test 5: {RESULT5}, array: {NUMS5[:RESULT5]}")
