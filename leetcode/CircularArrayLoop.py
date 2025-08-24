"""
Circular Array Loop - Array Traversal Solution.

This module contains a solution to determine if there exists a circular loop
in an array where you move according to the value at each position.

LeetCode Problem: https://leetcode.com/problems/circular-array-loop/
Problem Number: 457
"""

from typing import List


class Solution:
    """Solution class for Circular Array Loop problem."""

    def circularArrayLoop(self, array_nums: List[int]) -> bool:
        """
        Determine if there exists a circular loop in the array.
        
        A loop is valid if:
        1. It has more than one element
        2. All moves in the loop are in the same direction (all forward or all backward)
        3. The loop eventually returns to the starting position
        
        Args:
            array_nums: Array of integers representing move directions and distances
            
        Returns:
            True if a valid circular loop exists, False otherwise
        """
        def getNext(idx: int) -> int:
            return (idx + array_nums[idx]) % n

        n = len(array_nums)
        visited = [False] * n

        for i in range(n):
            if visited[i]:
                continue
            visited[i] = True
            cur_set = set()
            cur_idx = i

            while True:
                if cur_idx in cur_set:
                    if cur_idx == i and len(cur_set) > 1:
                        return True
                    break

                # Check if direction changes (invalid loop)
                if array_nums[cur_idx] * array_nums[i] <= 0:
                    break

                visited[cur_idx] = True
                cur_set.add(cur_idx)
                cur_idx = getNext(cur_idx)

        return False


if __name__ == "__main__":
    test_nums = [1, 1, 2]
    print(Solution().circularArrayLoop(test_nums))
