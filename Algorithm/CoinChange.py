from typing import List
from functools import cache

class Solution:
    def DAC(self, coins: List[int], total_amount: int) -> int:
        @cache
        def top_down_DP(amount: int) -> int:
            if amount == 0:
                return 0
            result = float('inf')
            for coin in coins:
                if coin <= amount:
                    result = min(result, top_down_DP(amount - coin) + 1)
            return result
        return top_down_DP(total_amount)
    
    def bottom_up_DP(self, coins: List[int], total: int) -> int:
        dp = [float('inf')] * (total + 1)
        dp[0] = 0
        for i in range(1, total + 1):
            for coin in coins:
                if i - coin >= 0:
                    dp[i] = min(dp[i], dp[i - coin] + 1)
        return dp[-1]


    
if __name__ == "__main__":
    coins = [1, 2, 5]
    total_amount = 11
    solution = Solution()
    print(solution.DAC(coins, total_amount))
    print(solution.bottom_up_DP(coins, total_amount))
