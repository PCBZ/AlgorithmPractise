from typing import List
import heapq

class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], K: int) -> float:
        workers = sorted([(w / q, q) for w, q in zip(wage, quality)])
        res = float('inf')
        total_quality = 0
        heap = []
        for rate, q in workers:
            heapq.heappush(heap, -q)
            total_quality += q
            if len(heap) > K:
                total_quality += heapq.heappop(heap)
            if len(heap) == K:
                res = min(res, rate * total_quality)
        return res

        

if __name__ == "__main__":
    quality = [10, 20, 5]
    wage = [70, 50, 30]
    K = 2
    print(Solution().mincostToHireWorkers(quality, wage, K))  # Output: 105.0