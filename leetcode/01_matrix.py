"""
01 Matrix - BFS Solution
Source: https://leetcode.com/problems/01-matrix/description/
"""

from typing import List
from collections import deque

class Solution:
    """
    Solution class for the 01 Matrix problem.
    Uses BFS to find the distance of the nearest 0 for each cell.
    """

    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        """
        Find the distance of the nearest 0 for each cell in the matrix.
        
        Args:
            mat: Binary matrix containing only 0s and 1s
            
        Returns:
            Matrix where each cell contains distance to nearest 0
        """
        m, n = len(mat), len(mat[0])
        distance = [[float('inf')] * n for i in range(m)]
        queue = deque([])
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    distance[i][j] = 0
                    queue.append((i, j))

        directions = [(-1, 0), (0, -1), (0, 1), (1, 0)]
        while queue:
            row, col = queue.popleft()
            for dr, dc in directions:
                nr, nc = row + dr, col + dc
                if 0 <= nr < m and 0 <= nc < n and distance[nr][nc] > distance[row][col] + 1:
                    distance[nr][nc] = distance[row][col] + 1
                    queue.append((nr, nc))
        return distance


if __name__ == "__main__":
    test_matrix = [[0, 0, 0], [0, 1, 0], [1, 1, 1]]
    print(Solution().updateMatrix(test_matrix))
