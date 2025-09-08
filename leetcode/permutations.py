"""
LeetCode Problems:
46. Permutations - https://leetcode.com/problems/permutations/
47. Permutations II - https://leetcode.com/problems/permutations-ii/

46: Given an array nums of distinct integers, return all the possible permutations.
47: Given a collection of numbers that might contain duplicates, return all possible unique permutations.
You can return the answer in any order.
"""

from typing import List


class Solution:
    """Solution for LeetCode Problems 46 & 47: Permutations and Permutations II."""

    def permute(self, nums: List[int]) -> List[List[int]]:
        """
        Generate all permutations of distinct integers using backtracking.
        LeetCode 46: Permutations

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

    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        """
        Generate all unique permutations of integers (may contain duplicates).
        LeetCode 47: Permutations II

        Args:
            nums: List of integers that may contain duplicates

        Returns:
            List of all unique permutations

        Time Complexity: O(n! * n)
        Space Complexity: O(n! * n)
        """
        n = len(nums)
        res = []

        def traceBack(path, used):
            if len(path) == n:
                res.append(path[:])
                return
            for i in range(n):
                if used[i]:
                    continue
                # Skip duplicates: if current number is same as previous and previous not used
                if i > 0 and nums[i] == nums[i-1] and not used[i-1]:
                    continue
                path.append(nums[i])
                used[i] = True
                traceBack(path, used)
                path.pop()
                used[i] = False

        nums.sort()  # Sort to group duplicates together
        traceBack([], [False] * n)
        return res


if __name__ == "__main__":
    solution = Solution()

    # Test Permutations (LeetCode 46) - distinct integers
    print("=== LeetCode 46: Permutations ===")
    test_nums1 = [1, 2, 3]
    output1 = solution.permute(test_nums1)
    print(f"Permutations of {test_nums1}: {output1}")

    test_nums2 = [0, 1]
    output2 = solution.permute(test_nums2)
    print(f"Permutations of {test_nums2}: {output2}")

    # Test Permutations II (LeetCode 47) - may contain duplicates
    print("\n=== LeetCode 47: Permutations II ===")
    test_nums3 = [1, 1, 2]
    output3 = solution.permuteUnique(test_nums3)
    print(f"Unique permutations of {test_nums3}: {output3}")

    test_nums4 = [1, 2, 1, 1]
    output4 = solution.permuteUnique(test_nums4)
    print(f"Unique permutations of {test_nums4}: {output4}")
