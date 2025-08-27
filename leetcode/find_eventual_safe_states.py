"""
LeetCode Problem #802: Find Eventual Safe States
URL: https://leetcode.com/problems/find-eventual-safe-states/
"""
from typing import List


class Solution:
    """Solution for finding eventual safe states in a directed graph."""

    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        """Find all eventually safe nodes in the graph."""
        num_nodes = len(graph)
        # 0: unvisited, 1: visiting, 2: safe
        state = [0] * num_nodes

        def is_safe(node):
            """Check if a node is eventually safe using DFS."""
            if state[node] != 0:
                return state[node] == 2

            state[node] = 1  # Mark as visiting

            # Check all neighbors
            for neighbor in graph[node]:
                if not is_safe(neighbor):
                    return False

            state[node] = 2  # Mark as safe
            return True

        result = []
        for i in range(num_nodes):
            if is_safe(i):
                result.append(i)

        return result


if __name__ == "__main__":
    # Example usage
    test_graph = [[], [0, 2, 3, 4], [3], [4], []]
    solution = Solution()
    safe_nodes = solution.eventualSafeNodes(test_graph)
    print(f"Eventually safe nodes: {safe_nodes}")
