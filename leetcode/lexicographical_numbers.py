"""
LeetCode Problem #386: Lexicographical Numbers
https://leetcode.com/problems/lexicographical-numbers/

Solution using DFS to generate numbers in lexicographical order.
Time Complexity: O(n) where n is the input number
Space Complexity: O(log n) for recursion stack depth
"""
# pylint: disable=invalid-name

from typing import List

# pylint: disable=too-few-public-methods


class Solution:
    """Solution for Lexicographical Numbers using DFS traversal."""

    def lexical_order(self, n: int) -> List[int]:
        """
        Generate numbers from 1 to n in lexicographical order.

        Args:
            n: Upper bound (inclusive) for number generation

        Returns:
            List of numbers from 1 to n in lexicographical order

        Examples:
            >>> solution = Solution()
            >>> solution.lexical_order(13)
            [1, 10, 11, 12, 13, 2, 3, 4, 5, 6, 7, 8, 9]
            >>> solution.lexical_order(2)
            [1, 2]
        """
        result = []

        def dfs(num: int) -> None:
            """DFS helper to generate numbers in lexicographical order."""
            if num > n:
                return
            result.append(num)
            for i in range(10):
                next_num = num * 10 + i
                if next_num > n:
                    break
                dfs(next_num)

        for i in range(1, 10):
            dfs(i)
        return result


if __name__ == "__main__":
    solution = Solution()
    test_result = solution.lexical_order(13)
    print(f"Lexicographical order for 13: {test_result}")
