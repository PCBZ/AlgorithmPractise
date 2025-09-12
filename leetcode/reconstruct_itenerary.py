"""
LeetCode 332. Reconstruct Itinerary
Given a list of airline tickets, reconstruct the itinerary in order.

URL: https://leetcode.com/problems/reconstruct-itinerary/
"""

from typing import List
from collections import defaultdict
import heapq


class Solution:
    """Solution for Reconstruct Itinerary using Hierholzer's algorithm."""

    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        """
        Reconstruct the itinerary using DFS and min-heap for lexicographic order.

        Args:
            tickets: List of [from, to] airport pairs

        Returns:
            The lexicographically smallest itinerary starting from "JFK"
        """
        # Build adjacency list with min-heap for lexicographic order
        graph = defaultdict(list)
        for src, dest in tickets:
            heapq.heappush(graph[src], dest)

        result = []

        def dfs(node: str):
            """DFS traversal using Hierholzer's algorithm for Eulerian path."""
            while graph[node]:
                next_node = heapq.heappop(graph[node])
                dfs(next_node)
            result.append(node)

        dfs("JFK")
        return result[::-1]


if __name__ == "__main__":
    solution = Solution()

    # Example 1: Simple cycle
    tickets1 = [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
    result1 = solution.findItinerary(tickets1)
    print(f"Input: {tickets1}")
    print(f"Output: {result1}")
    print("Explanation: JFK → MUC → LHR → SFO → SJC")
    print()

    # Example 2: Multiple paths with lexicographic preference
    tickets2 = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
    result2 = solution.findItinerary(tickets2)
    print(f"Input: {tickets2}")
    print(f"Output: {result2}")
    print("Explanation: Choose lexicographically smaller path when multiple options exist")
    print()

    # Example 3: Dead end requiring backtracking
    tickets3 = [["JFK","KUL"],["JFK","NRT"],["NRT","JFK"]]
    result3 = solution.findItinerary(tickets3)
    print(f"Input: {tickets3}")
    print(f"Output: {result3}")
    print("Explanation: Must visit NRT→JFK before going to KUL (dead end)")
    print()
