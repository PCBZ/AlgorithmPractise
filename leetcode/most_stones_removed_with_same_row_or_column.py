"""
LeetCode Problem: https://leetcode.com/problems/most-stones-removed-with-same-row-or-column/
947. Most Stones Removed with Same Row or Column

On a 2D plane, we place n stones at some integer coordinate points.
Each coordinate point may have at most one stone.

A stone can be removed if it shares a row or column with another stone
that has not been removed.

Given an array stones of length n where stones[i] = [xi, yi] represents
the location of the ith stone, return the maximum number of stones that
can be removed.
"""

from typing import List


class Solution:
    """Solution for LeetCode Problem 947: Most Stones Removed with Same Row or Column."""

    def removeStones(self, stones: List[List[int]]) -> int:
        """
        Find maximum stones removable using Union-Find.
        
        Stones sharing row/column form connected components.
        Remove all but one stone from each component.
        
        Time: O(n * α(n)), Space: O(n)
        """
        parent = {}

        def find(node: int) -> int:
            """Find root with path compression."""
            parent.setdefault(node, node)
            if parent[node] != node:
                parent[node] = find(parent[node])
            return parent[node]

        def union(node1: int, node2: int) -> None:
            """Union two nodes by root connection."""
            root1, root2 = find(node1), find(node2)
            if root1 != root2:
                parent[root1] = root2

        # Union stones sharing row/column (~col distinguishes from row)
        for row, col in stones:
            union(row, ~col)

        # Count components
        unique_roots = {find(node) for node in parent}

        # Remove all but one stone per component
        return len(stones) - len(unique_roots)


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        [[0, 0], [0, 1], [1, 0], [1, 2], [2, 1], [2, 2]],  # Expected: 5
        [[0, 0], [0, 2], [1, 1], [2, 0], [2, 2]],          # Expected: 3
        [[0, 0]],                                            # Expected: 0
    ]

    for i, test_stones in enumerate(test_cases):
        result = solution.removeStones(test_stones)
        print(f"Test case {i+1}: {test_stones} -> {result}")
