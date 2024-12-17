from typing import List
from collections import defaultdict
from math import gcd

class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:

        def getSlope(p1: List[int], p2: List[int]) -> float:
            x1, y1 = p1
            x2, y2 = p2
            dx, dy = x1 - x2, y1 - y2
            if dy == 0:
                return float('inf')
            return (dx / dy)
        
        total_max = 0
        n = len(points)
        for i in range(n):
            slopes = defaultdict(int)
            x1, y1 = points[i][0], points[i][1]
            duplicate = 1
            cur_max = 0
            for j in range(i + 1, n):
                x2, y2 = points[j][0], points[j][1]
                if x1 == x2 and y1 == y2:
                    duplicate += 1
                else:
                    slope = getSlope(points[i], points[j])
                    slopes[slope] += 1
                    print(slopes, i)
                    cur_max = max(cur_max, slopes[slope])
            total_max = max(total_max, cur_max + duplicate)
        return total_max
        

if __name__ == '__main__':
    points = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
    print(Solution().maxPoints(points))