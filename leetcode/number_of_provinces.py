"""
LeetCode Problem: https://leetcode.com/problems/number-of-provinces/
547. Number of Provinces

Given n x n adjacency matrix, find number of connected components (provinces).
Cities are connected if they share direct or indirect connections.
"""

from typing import List


class Solution:
    """Solution for LeetCode Problem 547: Number of Provinces."""

    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        """Count provinces via DFS. Time: O(n²), Space: O(n)"""
        n = len(isConnected)
        visited = [False] * n
        provinces = 0

        def dfs(city: int) -> None:
            """Mark cities visited."""
            visited[city] = True
            for neighbor in range(n):
                if not visited[neighbor] and isConnected[city][neighbor] == 1:
                    dfs(neighbor)

        # Count connected components
        for city in range(n):
            if not visited[city]:
                dfs(city)
                provinces += 1

        return provinces


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        [[1, 1, 0], [1, 1, 0], [0, 0, 1]],  # Expected: 2
        [[1, 0, 0], [0, 1, 0], [0, 0, 1]],  # Expected: 3
        [[1, 1, 1], [1, 1, 1], [1, 1, 1]],  # Expected: 1
    ]

    for i, matrix in enumerate(test_cases):
        output = solution.findCircleNum(matrix)
        print(f"Test case {i+1}: {matrix} -> {output}")
