"""
LeetCode Problem #216: Combination Sum III
URL: https://leetcode.com/problems/combination-sum-iii/

Find all valid combinations of k numbers that sum up to n such that the following
conditions are true:
- Only numbers 1 through 9 are used.
- Each number is used at most once.
"""

from typing import List


class Solution:
    """Solution class for finding combinations that sum to target using backtracking."""

    def combinationSum3(self, k_count: int, target_sum: int) -> List[List[int]]:
        """
        Find all valid combinations of k numbers that sum up to n.
        
        Uses backtracking to explore all possible combinations of numbers 1-9.
        Each number can be used at most once.
        
        Args:
            k_count: Number of integers in each combination
            target_sum: Target sum for each combination
            
        Returns:
            List of all valid combinations
        """
        def traceBack(start: int, path: List[int]):
            """Recursive backtracking helper function."""
            if len(path) == k_count:
                if sum(path) == target_sum:
                    res.append(path[:])
                return
            for i in range(start + 1, 10):
                path.append(i)
                traceBack(i, path)
                path.pop()
        res = []
        traceBack(0, [])
        return res


if __name__ == "__main__":
    k_value, n_value = 3, 9
    print(Solution().combinationSum3(k_value, n_value))
