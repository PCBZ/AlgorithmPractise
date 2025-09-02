"""
LeetCode Problem #329: Longest Increasing Path in a Matrix.
URL: https://leetcode.com/problems/longest-increasing-path-in-a-matrix/
DFS with memoization solution.
"""

from typing import List


class Solution:
    """Solution for finding the longest increasing path in a matrix using DFS + memoization."""

    def longest_increasing_path(self, matrix: List[List[int]]) -> int:
        """
        Find the longest increasing path in a 2D matrix.
        
        Time: O(m*n), Space: O(m*n)
        """
        if not matrix or not matrix[0]:
            return 0

        rows, cols = len(matrix), len(matrix[0])
        memo = [[0] * cols for _ in range(rows)]

        def dfs(row: int, col: int) -> int:
            """DFS to find longest path from current position."""
            if memo[row][col] != 0:
                return memo[row][col]

            directions = [(-1, 0), (0, -1), (0, 1), (1, 0)]
            max_length = 1

            for delta_row, delta_col in directions:
                new_row, new_col = row + delta_row, col + delta_col
                if (0 <= new_row < rows and 0 <= new_col < cols and
                        matrix[new_row][new_col] > matrix[row][col]):
                    max_length = max(max_length, 1 + dfs(new_row, new_col))

            memo[row][col] = max_length
            return max_length

        max_path_length = 0
        for i in range(rows):
            for j in range(cols):
                max_path_length = max(max_path_length, dfs(i, j))
        return max_path_length

    def get_longest_path_details(self, matrix: List[List[int]]) -> dict:
        """Get detailed path information including starting positions and values."""
        if not matrix or not matrix[0]:
            return {
                'length': 0,
                'starting_positions': [],
                'path_values': []
            }

        rows, cols = len(matrix), len(matrix[0])
        memo = [[0] * cols for _ in range(rows)]
        path_memo = {}

        def dfs_with_path(row: int, col: int) -> tuple:
            """DFS that also tracks the actual path taken."""
            if (row, col) in path_memo:
                return path_memo[(row, col)]

            if memo[row][col] != 0:
                return memo[row][col], [(row, col)]

            directions = [(-1, 0), (0, -1), (0, 1), (1, 0)]
            max_length = 1
            best_path = [(row, col)]

            for delta_row, delta_col in directions:
                new_row, new_col = row + delta_row, col + delta_col
                if (0 <= new_row < rows and 0 <= new_col < cols and
                        matrix[new_row][new_col] > matrix[row][col]):
                    length, path = dfs_with_path(new_row, new_col)
                    if 1 + length > max_length:
                        max_length = 1 + length
                        best_path = [(row, col)] + path

            memo[row][col] = max_length
            path_memo[(row, col)] = (max_length, best_path)
            return max_length, best_path

        max_length = 0
        best_starting_positions = []
        best_paths = []

        for i in range(rows):
            for j in range(cols):
                length, path = dfs_with_path(i, j)
                if length > max_length:
                    max_length = length
                    best_starting_positions = [(i, j)]
                    best_paths = [path]
                elif length == max_length:
                    best_starting_positions.append((i, j))
                    best_paths.append(path)

        path_values = []
        for path in best_paths[:1]:  # Return one example path
            path_values = [matrix[r][c] for r, c in path]

        return {
            'length': max_length,
            'starting_positions': best_starting_positions,
            'path_values': path_values
        }


def main():
    """Demo function."""
    test_matrix = [[3, 4, 5], [3, 2, 6], [2, 2, 1]]
    solution = Solution()
    result = solution.longest_increasing_path(test_matrix)
    print(f"Longest increasing path length: {result}")


if __name__ == "__main__":
    main()
