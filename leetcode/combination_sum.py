"""
LeetCode Problem #39: Combination Sum
URL: https://leetcode.com/problems/combination-sum/

Given an array of distinct integers candidates and a target integer target,
return a list of all unique combinations of candidates where the chosen numbers sum to target.
The same number may be chosen from candidates an unlimited number of times.
"""

from typing import List


class Solution:
    """Solution class for finding combinations that sum to target with unlimited reuse."""

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        Find all unique combinations where chosen numbers sum to target.
        
        Each number can be used multiple times. Uses backtracking approach.
        
        Args:
            candidates: Array of distinct integers
            target: Target sum to achieve
            
        Returns:
            List of all unique combinations that sum to target
        """
        res = []

        def trace_back(start: int, combines: List[int], remain: int):
            """Recursive backtracking helper function."""
            if remain == 0:
                res.append(combines.copy())
                return
            if remain < 0:
                return
            for i in range(start, len(candidates)):
                combines.append(candidates[i])
                trace_back(i, combines, remain - candidates[i])
                combines.pop()

        trace_back(0, [], target)
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.combinationSum([2, 3, 6, 7], 7))
