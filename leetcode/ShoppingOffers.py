from typing import List, Tuple
from functools import cache

class Solution:
    def shoppingOffers(self, price: List[int], special: List[List[int]], needs: List[int]) -> int:
        n = len(needs)
        def dfs(needs_tuple: Tuple[int, ...]) -> int:
            needs = list(needs_tuple)
            min_cost = float('inf')       
            for offer in special:
                if all(offer[i] <= needs[i] for i in range(n)):
                    cost = offer[n] + dfs(tuple([needs[i] - offer[i] for i in range(n)]))
                    min_cost = min(min_cost, cost)
            return min(min_cost, sum(price[i] * needs[i] for i in range(n)))
        return dfs(tuple(needs))

if __name__ == "__main__":
    price = [2, 2]
    special = [[1,1,1],[1,1,2],[1,1,3],[1,1,4],[1,1,5],[1,1,6],[1,1,7],[1,1,8],[1,1,9],[1,1,10],[1,1,11],[1,1,12],[1,1,13],[1,1,14],[1,1,15]]
    needs = [10,10]
    print(Solution().shoppingOffers(price, special, needs))