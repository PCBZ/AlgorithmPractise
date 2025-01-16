from typing import List
from math import floor, ceil

class Solution:
    def maxQualityScore(self, ratings: List[int], impactFactor: int) -> int:
        n = len(ratings)
        dp_no_strategy = [0] * n
        dp_amplify = [0] * n
        dp_adjust = [0] * n

        dp_no_strategy[0] = ratings[0]
        dp_amplify[0] = ratings[0] * impactFactor
        dp_adjust[0] = floor(ratings[0] / impactFactor) if ratings[0] > 0 else ceil(ratings[0] / impactFactor)

        max_quality_score = max(dp_no_strategy[0], dp_amplify[0], dp_adjust[0])

        for i in range(1, n):
            dp_no_strategy[i] = max(dp_no_strategy[i-1] + ratings[i], ratings[i])
            new_amplify = ratings[i] * impactFactor
            dp_amplify[i] = max(dp_amplify[i-1] + new_amplify, new_amplify)
            new_adjust = floor(ratings[i] / impactFactor) if ratings[i] > 0 else ceil(ratings[i] / impactFactor)
            dp_adjust[i] = max(dp_adjust[i-1] + new_adjust, new_adjust)
        
            max_quality_score = max(dp_no_strategy[-1], dp_amplify[-1], dp_adjust[-1])

        return max_quality_score
    
if __name__ == "__main__":
    ratings = [1, -2, 3, -4, 5]
    impactFactor = 2
    print(Solution().maxQualityScore(ratings, impactFactor))