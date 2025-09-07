"""
LeetCode 417. Pacific Atlantic Water Flow

Find cells where water can flow to both Pacific (top/left) and Atlantic (bottom/right) oceans.
Water flows from higher to lower or equal heights in 4 directions.

URL: https://leetcode.com/problems/pacific-atlantic-water-flow/
"""

from typing import List


class Solution:
    """Solution for Pacific Atlantic Water Flow problem using DFS from ocean borders."""

    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        """Find cells that can reach both oceans using DFS from borders."""
        if not heights or not heights[0]:
            return []

        rows, cols = len(heights), len(heights[0])

        pacific_reachable = [[False] * cols for _ in range(rows)]
        atlantic_reachable = [[False] * cols for _ in range(rows)]

        def dfs(row: int, col: int, reachable: List[List[bool]], prev_height: int) -> None:
            """DFS to mark reachable cells from current position."""
            if (row < 0 or row >= rows or col < 0 or col >= cols):
                return
            if reachable[row][col] or heights[row][col] < prev_height:
                return

            reachable[row][col] = True
            current_height = heights[row][col]
            directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

            for delta_row, delta_col in directions:
                new_row = row + delta_row
                new_col = col + delta_col
                dfs(new_row, new_col, reachable, current_height)

        # DFS from Pacific borders
        for row in range(rows):
            dfs(row, 0, pacific_reachable, 0)
        for col in range(cols):
            dfs(0, col, pacific_reachable, 0)

        # DFS from Atlantic borders
        for row in range(rows):
            dfs(row, cols - 1, atlantic_reachable, 0)
        for col in range(cols):
            dfs(rows - 1, col, atlantic_reachable, 0)

        # Find intersection
        result = []
        for row in range(rows):
            for col in range(cols):
                if pacific_reachable[row][col] and atlantic_reachable[row][col]:
                    result.append([row, col])

        return result


if __name__ == "__main__":
    solution = Solution()

    heights1 = [
        [1, 2, 2, 3, 5],
        [3, 2, 3, 4, 4],
        [2, 4, 5, 3, 1],
        [6, 7, 1, 4, 5],
        [5, 1, 1, 2, 4]
    ]
    result1 = solution.pacificAtlantic(heights1)
    print("Test 1 - Expected: [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]")
    print("Test 1 - Got:", sorted(result1))

    heights2 = [[1, 1], [1, 1]]
    result2 = solution.pacificAtlantic(heights2)
    print("Test 2 - Expected: [[0,0],[0,1],[1,0],[1,1]]")
    print("Test 2 - Got:", sorted(result2))

    heights3 = [[1]]
    result3 = solution.pacificAtlantic(heights3)
    print("Test 3 - Expected: [[0,0]]")
    print("Test 3 - Got:", result3)
