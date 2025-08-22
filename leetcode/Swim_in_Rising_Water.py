"""
Swim in Rising Water
Source: https://leetcode.com/problems/swim-in-rising-water/description/
"""

from typing import List
import heapq

class Solution:
    """
    Solution class for the Swim in Rising Water problem.
    Uses Dijkstra's algorithm to find the minimum time to reach the destination.
    """

    def swimInWater(self, grid: List[List[int]]) -> int:
        """
        Find the minimum time required to swim from top-left to bottom-right.
        
        Args:
            grid: 2D grid where each cell represents the water level at time t
            
        Returns:
            Minimum time to reach the bottom-right corner
        """
        m, n = len(grid), len(grid[0])
        visited = [[False] * n for _ in range(m)]
        heap = [(grid[0][0], 0, 0)]
        visited[0][0] = True
        time = 0
        while heap:
            height, row, col = heapq.heappop(heap)
            time = max(time, height)
            if row == m - 1 and col == n - 1:
                return time
            for dr, dc in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                nr, nc = row + dr, col + dc
                if 0 <= nr < m and 0 <= nc < n and not visited[nr][nc]:
                    visited[nr][nc] = True
                    heapq.heappush(heap, (grid[nr][nc], nr, nc))

        # This should never be reached if the grid is valid
        return -1


if __name__ == "__main__":
    test_grid = [[0, 100], [1, 2]]
    print(Solution().swimInWater(test_grid))  # Example usage
