"""
LeetCode Problem: https://leetcode.com/problems/permutations/
46. Permutations

Given an array nums of distinct integers, return all the possible permutations.
You can return the answer in any order.
"""

from typing import List


class Solution:
    """Solution for LeetCode Problem 46: Permutations."""

    def permute(self, nums: List[int]) -> List[List[int]]:
        """
        Generate all permutations of distinct integers using backtracking.

        Args:
            nums: List of distinct integers

        Returns:
            List of all permutations

        Time Complexity: O(n! * n)
        Space Complexity: O(n! * n)
        """
        permutations = []

        def backtrack(current_permutation: List[int], remaining: List[int]) -> None:
            # Base case: no more numbers to add
            if not remaining:
                permutations.append(current_permutation[:])
                return

            # Try each remaining number
            for idx, num in enumerate(remaining):
                # Choose
                current_permutation.append(num)
                # Recurse with remaining numbers (excluding current)
                new_remaining = remaining[:idx] + remaining[idx+1:]
                backtrack(current_permutation, new_remaining)
                # Backtrack
                current_permutation.pop()

        backtrack([], nums)
        return permutations


if __name__ == "__main__":
    solution = Solution()
    test_nums = [1, 2, 3]
    output = solution.permute(test_nums)
    print(f"Permutations of {test_nums}: {output}")
