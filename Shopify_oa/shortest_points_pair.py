from typing import List, Tuple

class Solution:
    def shortest_points_pair(self, points: List[int]) -> List[int]:

        def shortest_points_pair_helper(points: List[int]) -> Tuple[int, Tuple[List[int]]]:
            def get_distance(point1: Tuple[int, int], point2: Tuple[int, int]) -> float:
                return ((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)**0.5
               
            def bruteforce(points: List[int]) -> Tuple[int, Tuple[List]]:
                n = len(points)
                min_dist = float('inf')
                pairs = None
                for i in range(n):
                    for j in range(i + 1, n):
                        dist = get_distance(points[i], points[j])
                        if dist < min_dist:
                            min_dist = dist
                            pairs = points[i], points[j]
                return min_dist, pairs
            
            n = len(points)
            if n <= 3:
                return bruteforce(points)
            
            mid = n // 2
            left_dist, left_pairs = shortest_points_pair_helper(points[:mid])
            right_dist, right_pairs = shortest_points_pair_helper(points[mid:])

            min_dist = min(left_dist, right_dist)
            pairs = left_pairs if min_dist == left_dist else right_pairs

            strip = [point for point in points if abs(point[0] - points[mid][0]) < min_dist]
            m = len(strip)
            for i in range(m):
                for j in range(i+1, m):
                    dist = get_distance(strip[i], strip[j])
                    if dist < min_dist:
                        min_dist = dist
                        pairs = strip[i], strip[j] 
            return min_dist, pairs
        
        return shortest_points_pair_helper(points)[1]
    
if __name__ == "__main__":
    points = [(2, 3), (12, 30), (40, 50), (5, 1), (12, 10), (3, 4)]
    print(Solution().shortest_points_pair(points))



