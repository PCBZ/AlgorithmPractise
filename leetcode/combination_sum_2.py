"""
LeetCode Problem #40: Combination Sum II
URL: https://leetcode.com/problems/combination-sum-ii/

Given a collection of candidate numbers (candidates) and a target number (target),
find all unique combinations in candidates where the candidate numbers sum to target.
Each number in candidates may only be used once in the combination.
"""

from typing import List


class Solution:
    """Solution class for finding unique combinations that sum to target using backtracking."""

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        Find all unique combinations in candidates where numbers sum to target.
        
        Each number may only be used once. Uses backtracking with duplicate handling.
        
        Args:
            candidates: List of candidate numbers (may contain duplicates)
            target: Target sum to achieve
            
        Returns:
            List of all unique combinations that sum to target
        """
        res = []
        candidates.sort()

        def traceBack(start: int, candidates: List[int], total: int, values: List[int]):
            """Recursive backtracking helper with duplicate handling."""
            if total == target:
                res.append(list(values))
                return
            if total > target:
                return
            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i-1]:
                    continue
                values.append(candidates[i])
                traceBack(i+1, candidates, total + candidates[i], values)
                values.pop()

        traceBack(0, candidates, 0, [])
        return res

if __name__ == '__main__':
    s = Solution()
    print(s.combinationSum2([10, 1, 2, 7, 6, 1, 5], 8))
