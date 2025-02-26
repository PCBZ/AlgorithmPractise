from typing import List
import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low, high = sum(piles) // h, max(piles)
        while low < high:
            mid = (low + high) // 2
            h_spend = sum(map(lambda x: math.ceil(x / mid), piles))
            if h_spend <= h:
                high = mid
            else:
                low = mid + 1
        return mid + 1
    
if __name__ == "__main__":
    piles = [30,11,23,4,20]
    h = 5
    print(Solution().minEatingSpeed(piles, h))