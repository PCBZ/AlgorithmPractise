"""
LeetCode #1584: Min Cost to Connect All Points

Find minimum cost to connect all points using Manhattan distance.
Use Prim's algorithm to build minimum spanning tree.

Time: O(N^2 log N), Space: O(N^2)
"""
from typing import List
import heapq


class Solution:
    """Min cost to connect points using Prim's algorithm."""

    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        """Find minimum cost to connect all points."""
        if not points or len(points) <= 1:
            return 0

        n = len(points)
        visited = set()
        min_heap = [(0, 0)]  # (cost, point_index)
        total_cost = 0

        while len(visited) < n:
            cost, current_point = heapq.heappop(min_heap)

            if current_point in visited:
                continue

            visited.add(current_point)
            total_cost += cost

            # Add unvisited neighbors
            for next_point in range(n):
                if next_point not in visited:
                    # Manhattan distance
                    distance = (abs(points[current_point][0] - points[next_point][0]) +
                               abs(points[current_point][1] - points[next_point][1]))
                    heapq.heappush(min_heap, (distance, next_point))

        return total_cost


if __name__ == "__main__":
    TEST_POINTS = [[3, 12], [-2, 5], [-4, 1]]
    print(Solution().minCostConnectPoints(TEST_POINTS))
