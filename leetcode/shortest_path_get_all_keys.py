"""
LeetCode 864: Shortest Path to Get All Keys

Find the shortest path to collect all keys in a grid using BFS.

URL: https://leetcode.com/problems/shortest-path-to-get-all-keys/
"""

from collections import deque
from typing import List


class Solution:  # pylint: disable=too-few-public-methods
    """Solution using BFS with string-based key tracking."""
    
    def shortestPathAllKeys(self, grid: List[str]) -> int:  # pylint: disable=invalid-name
        """
        Find shortest path to collect all keys using BFS.
        
        Time: O(m * n * 2^k), Space: O(m * n * 2^k)
        """
        # Handle edge cases
        if not grid or not grid[0]:
            return -1
            
        m, n = len(grid), len(grid[0])
        keys = set()
        start = None
        
        # Find starting position and collect all keys
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "@":
                    start = (i, j)
                elif "a" <= grid[i][j] <= "z":
                    keys.add(grid[i][j])
        
        # If no start position found, return -1
        if start is None:
            return -1
            
        # Target state: all keys collected in sorted order        
        all_keys = "".join(sorted(keys))
        
        # BFS: (row, col, collected_keys, steps)
        visited = set([(start[0], start[1], "")])
        queue = deque([(start[0], start[1], "", 0)])
        
        # Four directions: up, down, left, right
        directions = [(-1, 0), (0, -1), (0, 1), (1, 0)]

        while queue:
            i, j, cur_keys, step = queue.popleft()
            
            # Check if all keys collected
            if cur_keys == all_keys:
                return step
                
            # Try all four directions
            for di, dj in directions:
                ni, nj = i + di, j + dj
                
                # Check bounds
                if 0 <= ni < m and 0 <= nj < n:
                    # Skip walls
                    if grid[ni][nj] == "#":
                        continue
                        
                    new_keys = cur_keys
                    
                    # If we find a key, add it to our collection
                    if "a" <= grid[ni][nj] <= "z":
                        key_set = set(cur_keys)
                        key_set.add(grid[ni][nj])
                        new_keys = "".join(sorted(key_set))
                    
                    # If we encounter a lock, check if we have the key
                    elif "A" <= grid[ni][nj] <= "Z" and grid[ni][nj].lower() not in cur_keys:
                        continue
                    
                    # Add new state if not visited
                    if (ni, nj, new_keys) not in visited:
                        queue.append((ni, nj, new_keys, step + 1))
                        visited.add((ni, nj, new_keys))
                
        return -1

if __name__ == "__main__":
    sol = Solution()

    # Test case 1: Basic example with keys and locks
    grid1 = ["@.a.#", "###.#", "b.A.B"]
    result1 = sol.shortestPathAllKeys(grid1)
    print(f"Test 1: {grid1}")
    print(f"Result: {result1}")  # Expected: 8
    print()

    # Test case 2: Multiple paths available
    grid2 = ["@..aA", "..B#.", "....b"]
    result2 = sol.shortestPathAllKeys(grid2)
    print(f"Test 2: {grid2}")
    print(f"Result: {result2}")  # Expected: 6
    print()

    # Test case 3: Impossible case
    grid3 = ["@Aa"]
    result3 = sol.shortestPathAllKeys(grid3)
    print(f"Test 3: {grid3}")
    print(f"Result: {result3}")  # Expected: -1
    print()

    # Test case 4: No keys needed
    grid4 = ["@..."]
    result4 = sol.shortestPathAllKeys(grid4)
    print(f"Test 4: {grid4}")
    print(f"Result: {result4}")  # Expected: 0
