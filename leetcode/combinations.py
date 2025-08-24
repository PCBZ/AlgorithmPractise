"""
LeetCode Problem #77: Combinations
URL: https://leetcode.com/problems/combinations/

Given two integers n and k, return all possible combinations of k numbers
chosen from the range [1, n].
"""

from typing import List


class Solution:
    """Solution class for generating combinations using backtracking."""

    def combine(self, num_range: int, k_size: int) -> List[List[int]]:
        """
        Generate all possible combinations of k numbers from range [1, n].
        
        Uses backtracking to explore all possible combinations.
        
        Args:
            num_range: Upper bound of the range [1, n]
            k_size: Size of each combination
            
        Returns:
            List of all possible combinations
        """
        res = []

        def traceBack(start: int, combs: List[int]):
            """Recursive backtracking helper function."""
            if len(combs) == k_size:
                res.append(combs[:])
                return
            for i in range(start, num_range):
                combs.append(i + 1)
                traceBack(i + 1, combs)
                combs.pop()

        traceBack(0, [])
        return res




if __name__ == "__main__":
    n_value, k_value = 4, 4
    print(Solution().combine(n_value, k_value))
