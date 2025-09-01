"""
LeetCode Problem #845: Longest Mountain in Array
https://leetcode.com/problems/longest-mountain-in-array/

Solution using one-pass algorithm to find the longest mountain.
A mountain is a subarray that increases then decreases with length >= 3.
Time Complexity: O(n) where n is the length of array
Space Complexity: O(1) constant space
"""
from typing import List


class Solution:
    """Solution for Longest Mountain in Array using one-pass traversal."""

    def longest_mountain(self, arr: List[int]) -> int:
        """
        Find the length of the longest mountain in array.

        Args:
            arr: Array of integers

        Returns:
            Length of longest mountain (subarray that goes up then down)
        """
        if len(arr) < 3:
            return 0

        n = len(arr)
        max_length = 0
        i = 0

        while i < n - 1:
            # Skip if current element is not start of potential mountain
            if arr[i] >= arr[i + 1]:
                i += 1
                continue

            # Count ascending part
            up = 0
            while i < n - 1 and arr[i] < arr[i + 1]:
                up += 1
                i += 1

            # Count descending part
            down = 0
            while i < n - 1 and arr[i] > arr[i + 1]:
                down += 1
                i += 1

            # Valid mountain needs both up and down parts
            if up > 0 and down > 0:
                max_length = max(max_length, up + down + 1)

        return max_length


if __name__ == "__main__":
    solution = Solution()
    test_arr = [875, 884, 239, 731, 723, 685]
    print(f"Longest mountain: {solution.longest_mountain(test_arr)}")
