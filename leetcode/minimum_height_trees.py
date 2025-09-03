"""
LeetCode #310: Minimum Height Trees

Find all possible roots that would result in minimum height trees.

Time: O(n), Space: O(n)
"""
from typing import List
from collections import deque, defaultdict


class Solution:
    """Find minimum height trees using topological sorting approach."""

    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        """Find all possible roots that result in minimum height trees."""
        if n == 1:
            return [0]
        if n == 2:
            return [0, 1]

        graph = defaultdict(set)
        for node1, node2 in edges:
            graph[node1].add(node2)
            graph[node2].add(node1)

        leaves = deque([node for node in graph if len(graph[node]) == 1])

        remaining_count = n
        while remaining_count > 2:
            leaf_count = len(leaves)
            remaining_count -= leaf_count

            for _ in range(leaf_count):
                leaf = leaves.popleft()
                for neighbor in graph[leaf]:
                    graph[neighbor].remove(leaf)
                    if len(graph[neighbor]) == 1:
                        leaves.append(neighbor)

        return list(leaves)


if __name__ == "__main__":
    TEST_N = 6
    TEST_EDGES = [[3, 0], [3, 1], [3, 2], [3, 4], [5, 4]]
    solution = Solution()
    result = solution.findMinHeightTrees(TEST_N, TEST_EDGES)
    print(f"Input: n={TEST_N}, edges={TEST_EDGES}")
    print(f"Output: {result}")
