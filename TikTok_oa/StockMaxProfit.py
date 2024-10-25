from typing import List

class Solution:
  def getMaxProfit(price: List[int], profit: List[int]) -> int:
    n = len(price)
    max_profit = 0
    for j in range(1, n-1):
      max_profit_i = 0
      max_profit_k = 0
      for i in range(j):
        if price[i] < price[j]:
          max_profit_i = max(max_profit_i, profit[i])
      for k in range(j+1, n):
        if price[k] > price[j]:
          max_profit_k = max(max_profit_k, profit[k])
      max_profit = max(max_profit, max_profit_i + profit[j] + max_profit_k)
    return max_profit
  
  price = [1, 5, 3, 4, 6]
  profit = [2, 3, 4, 5, 6]
  print(getMaxProfit(price, profit))

