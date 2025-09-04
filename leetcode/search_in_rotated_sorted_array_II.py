"""
LeetCode #81: Search in Rotated Sorted Array II
https://leetcode.com/problems/search-in-rotated-sorted-array-ii/

Search for a target value in a rotated sorted array with duplicates.

Time: O(log n) average, O(n) worst case, Space: O(1)
"""

from typing import List


class Solution:
    """Search in Rotated Sorted Array II using binary search with duplicate handling."""

    def search(self, nums: List[int], target: int) -> bool:
        """Search for target in rotated sorted array with duplicates."""
        if not nums:
            return False

        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return True

            # Handle duplicates: when left, mid, right are all equal
            if nums[left] == nums[mid] == nums[right]:
                left += 1
                right -= 1
            elif nums[left] <= nums[mid]:
                # Left half is sorted
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                # Right half is sorted
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1

        return False


if __name__ == "__main__":
    solution = Solution()

    # Test case 1: Basic search with duplicates
    TEST_NUMS1 = [2, 5, 6, 0, 0, 1, 2]
    RESULT1 = solution.search(TEST_NUMS1, 0)
    print(f"Test 1 - Search for 0 in {TEST_NUMS1}: {RESULT1}")

    # Test case 2: Target not found
    TEST_NUMS2 = [2, 5, 6, 0, 0, 1, 2]
    RESULT2 = solution.search(TEST_NUMS2, 3)
    print(f"Test 2 - Search for 3 in {TEST_NUMS2}: {RESULT2}")

    # Test case 3: All duplicates
    TEST_NUMS3 = [1, 0, 1, 1, 1]
    RESULT3 = solution.search(TEST_NUMS3, 0)
    print(f"Test 3 - Search for 0 in {TEST_NUMS3}: {RESULT3}")
