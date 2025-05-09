from typing import List
from collections import deque

class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        n = len(graph)
        queue = deque()
        seen = set()

        for i, _ in enumerate(graph):
            visited = 1 << i
            queue.append((i, visited, 0))
            seen.add((i, visited))
        
        full_mask = (1 << n) - 1

        while queue:
            node, visited, step = queue.popleft()
            if visited == full_mask:
                return step
            for neighbor in graph[node]:
                new_visited = visited | (1 << neighbor)
                if (neighbor, new_visited) not in seen:
                    seen.add((neighbor, new_visited))
                    queue.append((neighbor, new_visited, step + 1))
        
        return -1


if __name__ == "__main__":
    graph = [[1,2,3],[0],[0],[0]]
    print(Solution().shortestPathLength(graph))