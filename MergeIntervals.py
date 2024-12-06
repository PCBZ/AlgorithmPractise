from typing import List

class Solution(object):
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        n = len(intervals)
        res = []
        if n == 1:
            return intervals
        start = end = 0
        i = 1
        while i < n :
            if intervals[i-1][1] >= intervals[i][0]:
                end += 1
            else:
                res.append([intervals[start][0], intervals[end][1]])
                start = end = i
            i += 1
        res.append([intervals[start][0], intervals[end][1]])
        return res

if __name__ == '__main__':
    intervals = [[1, 4], [0, 4]]
    print(Solution().merge(intervals))