from collections import deque
from typing import List

class Solution:
    def shortestPathAllKeys(self, grid: List[str]) -> int:
        m, n = len(grid), len(grid[0])
        keys = set()
        start = None
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "@":
                    start = (i, j)
                elif "a" <= grid[i][j] <= "z":
                    keys.add(grid[i][j])
        all_keys = "".join(sorted(keys))
        
        visited = set([(start[0], start[1], "")])
        queue = deque([(start[0], start[1], "", 0)])

        directions = [(-1, 0), (0, -1), (0, 1), (1, 0)]

        while queue:
            i, j, cur_keys, step = queue.popleft()
            if cur_keys == all_keys:
                return step
            for di, dj in directions:
                ni, nj = i + di, j + dj
                if 0 <= ni < m and 0 <= nj < n:
                    if grid[ni][nj] == "#":
                        continue
                    new_keys = cur_keys
                    if "a" <= grid[ni][nj] <= "z":
                        key_set = set(cur_keys)
                        key_set.add(grid[ni][nj])
                        new_keys = "".join(sorted(key_set))
                    elif "A" <= grid[ni][nj] <= "Z" and grid[ni][nj].lower() not in cur_keys:
                        continue
                    
                    if (ni, nj, new_keys) not in visited:
                        queue.append((ni, nj, new_keys, step + 1))
                        visited.add((ni, nj, new_keys))
                
        return -1
    
if __name__ == "__main__":
    grid = ["@.a.#", "###.#", "b.A.B"]
    print(Solution().shortestPathAllKeys(grid))  # Output: 8
    # grid = ["@..aA", "..B#.", "....b"]
    # print(Solution().shortestPathAllKeys(grid))  # Output: 6
    # grid = ["@Aa"]
    # print(Solution().shortestPathAllKeys(grid))  # Output: -1