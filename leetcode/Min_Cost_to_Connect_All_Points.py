from typing import List
import heapq
from collections import defaultdict

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        graph = defaultdict(list)
        n = len(points)
        for i in range(n):
            for j in range(i+1, n):
                distance = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                graph[tuple(points[i])].append((tuple(points[j]), distance))
                graph[tuple(points[j])].append((tuple(points[i]), distance))
        
        min_cost = 0
        candidates = [(-1, (0, 0))]
        visited = set()
        while candidates:
            weight, point = heapq.heappop(candidates)
            if point in visited:
                continue
            visited.add(point)
            if weight > 0:
                min_cost += weight
            for neighbor, next_weight in graph[point]:
                if neighbor not in visited:
                    heapq.heappush(candidates, (next_weight, neighbor))
        return min_cost
    
if __name__ == "__main__":
    points = [[3,12],[-2,5],[-4,1]]
    print(Solution().minCostConnectPoints(points))