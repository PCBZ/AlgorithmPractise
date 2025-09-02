"""
LeetCode Problem #695: Max Area of Island

URL: https://leetcode.com/problems/max-area-of-island/

Find the maximum area of an island in a 2D grid. An island is a group
of connected 1s (land), and the area is the number of 1s in the island.
Uses DFS to explore and calculate island areas.
"""
from typing import List


class Solution:
    """Solution class for max area of island problem using DFS."""

    def max_area_of_island(self, grid: List[List[int]]) -> int:
        """
        Find the maximum area of an island in the grid.

        Uses depth-first search (DFS) to explore each island and calculate
        its area. Marks visited cells to avoid double counting.

        Args:
            grid: 2D binary grid where 1 represents land and 0 represents water

        Returns:
            Maximum area of any island in the grid

        Time Complexity: O(m * n) where m, n are grid dimensions
        Space Complexity: O(m * n) for recursion stack in worst case
        """
        if not grid or not grid[0]:
            return 0

        rows, cols = len(grid), len(grid[0])
        max_area = 0

        def dfs(row: int, col: int) -> int:
            """
            Depth-first search to calculate area of current island.

            Args:
                row: Current row position
                col: Current column position

            Returns:
                Area of the island starting from this position
            """
            if (row < 0 or row >= rows or col < 0 or col >= cols or
                    grid[row][col] != 1):
                return 0

            # Mark as visited by changing 1 to 2
            grid[row][col] = 2
            area = 1

            # Explore all 4 directions
            directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            for delta_row, delta_col in directions:
                new_row, new_col = row + delta_row, col + delta_col
                area += dfs(new_row, new_col)

            return area

        # Search for islands in the entire grid
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    current_area = dfs(i, j)
                    max_area = max(max_area, current_area)

        return max_area

    def max_area_of_island_iterative(self, grid: List[List[int]]) -> int:
        """
        Iterative solution using stack instead of recursion.

        Args:
            grid: 2D binary grid where 1 represents land and 0 represents water

        Returns:
            Maximum area of any island in the grid

        Time Complexity: O(m * n)
        Space Complexity: O(min(m, n)) for stack
        """
        if not grid or not grid[0]:
            return 0

        rows, cols = len(grid), len(grid[0])
        max_area = 0
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    area = 0
                    stack = [(i, j)]

                    while stack:
                        row, col = stack.pop()
                        if (row < 0 or row >= rows or col < 0 or col >= cols or
                                grid[row][col] != 1):
                            continue

                        grid[row][col] = 2  # Mark as visited
                        area += 1

                        # Add adjacent cells to stack
                        for delta_row, delta_col in directions:
                            stack.append((row + delta_row, col + delta_col))

                    max_area = max(max_area, area)

        return max_area

    def max_area_of_island_non_destructive(self, grid: List[List[int]]) -> int:
        """
        Non-destructive solution that doesn't modify the original grid.

        Args:
            grid: 2D binary grid where 1 represents land and 0 represents water

        Returns:
            Maximum area of any island in the grid

        Time Complexity: O(m * n)
        Space Complexity: O(m * n) for visited set and recursion
        """
        if not grid or not grid[0]:
            return 0

        rows, cols = len(grid), len(grid[0])
        max_area = 0
        visited = set()

        def dfs_non_destructive(row: int, col: int) -> int:
            """DFS that uses a visited set instead of modifying the grid."""
            if (row, col) in visited:
                return 0
            if row < 0 or row >= rows or col < 0 or col >= cols:
                return 0
            if grid[row][col] != 1:
                return 0

            visited.add((row, col))
            area = 1

            directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            for delta_row, delta_col in directions:
                new_row, new_col = row + delta_row, col + delta_col
                area += dfs_non_destructive(new_row, new_col)

            return area

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1 and (i, j) not in visited:
                    current_area = dfs_non_destructive(i, j)
                    max_area = max(max_area, current_area)

        return max_area

    def count_islands(self, grid: List[List[int]]) -> int:
        """
        Bonus method: Count the total number of islands.

        Args:
            grid: 2D binary grid where 1 represents land and 0 represents water

        Returns:
            Total number of islands in the grid

        Time Complexity: O(m * n)
        Space Complexity: O(m * n) for recursion
        """
        if not grid or not grid[0]:
            return 0

        rows, cols = len(grid), len(grid[0])
        island_count = 0

        def dfs_count(row: int, col: int) -> None:
            """DFS to mark all cells of current island as visited."""
            if (row < 0 or row >= rows or col < 0 or col >= cols or
                    grid[row][col] != 1):
                return

            grid[row][col] = 2  # Mark as visited

            directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            for delta_row, delta_col in directions:
                new_row, new_col = row + delta_row, col + delta_col
                dfs_count(new_row, new_col)

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    dfs_count(i, j)
                    island_count += 1

        return island_count


if __name__ == "__main__":
    solution = Solution()

    # Test case 1: Example from LeetCode
    grid1 = [
        [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
        [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
        [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]
    ]

    # Need to copy for non-destructive test
    import copy
    grid1_copy = copy.deepcopy(grid1)

    print(f"Max area (DFS): {solution.max_area_of_island(grid1_copy)}")

    # Test case 2: No islands
    grid2 = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    print(f"Max area (no islands): {solution.max_area_of_island(grid2)}")

    # Test case 3: Single cell island
    grid3 = [[1]]
    print(f"Max area (single cell): {solution.max_area_of_island(grid3)}")

    # Test non-destructive version
    grid4 = [[1, 1, 0], [0, 1, 0], [0, 0, 1]]
    original_grid = copy.deepcopy(grid4)
    result = solution.max_area_of_island_non_destructive(grid4)
    print(f"Non-destructive result: {result}")
    print(f"Grid unchanged: {grid4 == original_grid}")
