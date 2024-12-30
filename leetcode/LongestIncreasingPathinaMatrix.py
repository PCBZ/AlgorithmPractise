from typing import List

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        memo = [[0] * n for _ in range(m)] 
        def dfs(row: int, col: int) -> int:
            if memo[row][col] != 0:
                return memo[row][col]
            directions = [(-1, 0), (0, -1), (0, 1), (1, 0)]
            max_len = 1
            for dx, dy in directions:
                n_row, n_col = row + dx, col + dy
                if 0 <= n_row < m and 0 <= n_col < n and matrix[n_row][n_col] > matrix[row][col]:
                    max_len = max(max_len, 1 + dfs(n_row, n_col))
            memo[row][col] = max_len
            return max_len
        
        max_len = 0
        for i in range(m):
            for j in range(n):
                max_len = max(max_len, dfs(i, j))
        return max_len


if __name__ == "__main__":
    matrix = [[3,4,5],[3,2,6],[2,2,1]]
    print(Solution().longestIncreasingPath(matrix))