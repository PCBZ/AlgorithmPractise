"""
Beautiful Arrangement - Backtracking Solution.

This module contains a solution to count the number of beautiful arrangements
where a beautiful arrangement is a permutation of numbers 1 to n such that:
- The number at the ith position is divisible by i, OR
- i is divisible by the number at the ith position

LeetCode Problem: https://leetcode.com/problems/beautiful-arrangement/
Problem Number: 526
"""


class Solution:
    """Solution class for Beautiful Arrangement problem."""

    def countArrangement(self, num_count: int) -> int:
        """
        Count the number of beautiful arrangements.
        
        A beautiful arrangement is a permutation where for every position i,
        either the number at position i is divisible by i, or i is divisible
        by the number at position i.
        
        Args:
            num_count: The number of integers from 1 to n to arrange
            
        Returns:
            The count of beautiful arrangements
        """
        def backtrack(index: int) -> int:
            """
            Backtrack to find all valid arrangements.
            
            Args:
                index: Current position to fill (1-indexed)
                
            Returns:
                Number of valid arrangements from this position
            """
            if index > num_count:
                return 1
            count = 0
            for i in range(1, num_count + 1):
                if not used[i] and (index % i == 0 or i % index == 0):
                    used[i] = True
                    count += backtrack(index + 1)
                    used[i] = False
            return count

        used = [False] * (num_count + 1)
        return backtrack(1)


if __name__ == "__main__":
    test_n = 4
    print(Solution().countArrangement(test_n))
