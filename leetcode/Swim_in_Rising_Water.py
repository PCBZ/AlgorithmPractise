from typing import List
import heapq

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
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


if __name__ == "__main__":
    grid = [[0, 100], [1, 2]]
    print(Solution().swimInWater(grid))  # Example usage
