from typing import List
from bisect import bisect_left

class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        start_map = {}
        starts = []
        res = []
        for i, interval in enumerate(intervals):
            start_map[interval[0]] = i
            starts.append(interval[0])
        starts.sort()
        n = len(starts)
        for interval in intervals:
            j = 0
            while j < n:
                if starts[j] >= interval[1]:
                    break
                j += 1
            res.append(start_map[starts[j]] if j < n else -1)
        return res
    
if __name__ == "__main__":
    intervals = [[1, 2]]
    print(Solution().findRightInterval(intervals))