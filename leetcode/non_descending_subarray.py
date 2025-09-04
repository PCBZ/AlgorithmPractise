"""
LeetCode #491: Non-decreasing Subsequences
https://leetcode.com/problems/non-decreasing-subsequences/

Find all possible non-decreasing subsequences with at least 2 elements.

Time: O(n * 2^n), Space: O(n * 2^n)
"""

from typing import List


class Solution:
    """Non-decreasing Subsequences using backtracking with duplicate handling."""

    def find_non_decreasing_subsequences(self, nums: List[int]) -> List[List[int]]:
        """Find all non-decreasing subsequences of length >= 2."""
        result = []

        def backtrack(path: List[int], start_idx: int) -> None:
            """Backtrack to find all valid subsequences."""
            # Add current path if it has at least 2 elements
            if len(path) >= 2:
                result.append(path[:])

            # Use set to avoid duplicates at current level
            used_at_level = set()

            for i in range(start_idx, len(nums)):
                current_num = nums[i]

                # Skip if we've used this value at current level (avoid duplicates)
                if current_num in used_at_level:
                    continue

                # Check if current number maintains non-decreasing order
                if not path or path[-1] <= current_num:
                    used_at_level.add(current_num)
                    path.append(current_num)
                    backtrack(path, i + 1)
                    path.pop()

        backtrack([], 0)
        return result


if __name__ == "__main__":
    solution = Solution()

    # Test case 1: Basic case with duplicates
    TEST_NUMS1 = [4, 6, 7, 7]
    RESULT1 = solution.find_non_decreasing_subsequences(TEST_NUMS1)
    print(f"Test 1 - nums: {TEST_NUMS1}")
    print(f"Result: {RESULT1}")

    # Test case 2: All same elements
    TEST_NUMS2 = [4, 4, 3, 2, 1]
    RESULT2 = solution.find_non_decreasing_subsequences(TEST_NUMS2)
    print(f"\nTest 2 - nums: {TEST_NUMS2}")
    print(f"Result: {RESULT2}")

    # Test case 3: Single element (no valid subsequences)
    TEST_NUMS3 = [1]
    RESULT3 = solution.find_non_decreasing_subsequences(TEST_NUMS3)
    print(f"\nTest 3 - nums: {TEST_NUMS3}")
    print(f"Result: {RESULT3}")
