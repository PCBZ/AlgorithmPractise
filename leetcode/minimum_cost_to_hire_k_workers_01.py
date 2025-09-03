"""
LeetCode #857: Minimum Cost to Hire K Workers

Find minimum cost to hire exactly K workers where each worker has quality and minimum wage.
Use greedy approach with max heap to track workers with highest quality-to-wage ratio.

Time: O(N log N), Space: O(N)
"""
from typing import List
import heapq


class Solution:
    """Find minimum cost to hire K workers using greedy approach."""

    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        """
        Find minimum cost to hire exactly k workers.

        Key insight: Sort workers by wage/quality ratio. For any group of workers,
        the payment rate is determined by the worker with highest ratio in the group.
        """
        if not quality or not wage or k <= 0:
            return 0.0

        # Sort workers by wage/quality ratio (rate)
        workers = sorted([(w / q, q) for w, q in zip(wage, quality)])

        min_cost = float('inf')
        total_quality = 0
        max_heap = []  # Store negative quality for max heap

        for rate, q in workers:
            # Add current worker to heap
            heapq.heappush(max_heap, -q)
            total_quality += q

            # Remove worker with highest quality if we have more than k workers
            if len(max_heap) > k:
                total_quality += heapq.heappop(max_heap)  # heappop returns negative

            # Calculate cost when we have exactly k workers
            if len(max_heap) == k:
                min_cost = min(min_cost, rate * total_quality)

        return min_cost


if __name__ == "__main__":
    TEST_QUALITY = [10, 20, 5]
    TEST_WAGE = [70, 50, 30]
    TEST_K = 2
    print(Solution().mincostToHireWorkers(TEST_QUALITY, TEST_WAGE, TEST_K))
