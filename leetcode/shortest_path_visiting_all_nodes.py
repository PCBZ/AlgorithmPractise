"""
LeetCode 847: Shortest Path Visiting All Nodes

Return the length of the shortest path that visits every node.
You may start and end at any node, and you may revisit nodes and traverse edges.

URL: https://leetcode.com/problems/shortest-path-visiting-all-nodes/
"""

from typing import List
from collections import deque


class Solution:  # pylint: disable=too-few-public-methods
    """Solution using BFS with bitmask to track visited nodes."""
    def shortestPathLength(self, graph: List[List[int]]) -> int:  # pylint: disable=invalid-name
        """
        Find shortest path visiting all nodes using BFS with bitmask.

        Time: O(n * 2^n), Space: O(n * 2^n)
        """
        n = len(graph)
        if n <= 1:
            return 0

        queue = deque()
        visited_states = set()

        # Start from every node
        for start_node in range(n):
            initial_mask = 1 << start_node
            queue.append((start_node, initial_mask, 0))
            visited_states.add((start_node, initial_mask))

        target_mask = (1 << n) - 1

        while queue:
            current_node, visited_mask, steps = queue.popleft()

            if visited_mask == target_mask:
                return steps

            for neighbor in graph[current_node]:
                new_visited_mask = visited_mask | (1 << neighbor)
                new_state = (neighbor, new_visited_mask)

                if new_state not in visited_states:
                    visited_states.add(new_state)
                    queue.append((neighbor, new_visited_mask, steps + 1))

        return -1


if __name__ == "__main__":
    sol = Solution()

    # Star graph
    graph1 = [[1, 2, 3], [0], [0], [0]]
    result1 = sol.shortestPathLength(graph1)
    print(f"Test 1: {graph1}")
    print(f"Result: {result1}")
    print()

    # Linear path
    graph2 = [[1], [0, 2], [1]]
    result2 = sol.shortestPathLength(graph2)
    print(f"Test 2: {graph2}")
    print(f"Result: {result2}")
    print()

    # Single node
    graph3 = [[]]
    result3 = sol.shortestPathLength(graph3)
    print(f"Test 3: {graph3}")
    print(f"Result: {result3}")
    print()

    # Triangle
    graph4 = [[1, 2], [0, 2], [0, 1]]
    result4 = sol.shortestPathLength(graph4)
    print(f"Test 4: {graph4}")
    print(f"Result: {result4}")
