from typing import List

class Solution:
    def maximumSumOfHeights(self, heights: List[int]) -> int:
        max_sum = 0
        for i in range(len(heights)):
            res = heights[:]
            prev = heights[i]
            for j in range(i - 1, -1, -1):
                res[j] = min(res[j], prev)
                prev = res[j]
            res[i] = heights[i]
            prev = heights[i]
            for k in range(i + 1, len(heights)):
                res[k] = min(res[k], prev)
                prev = res[k]
            max_sum = max(max_sum, sum(res))
        return max_sum

print(Solution().maximumSumOfHeights([6,5,3,9,2,7]))  # Output: 20