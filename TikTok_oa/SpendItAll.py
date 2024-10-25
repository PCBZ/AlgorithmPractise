from typing import List

def spendItAll(cost: List[int], budget: int) -> int:
    n = len(cost)
    purchase = 0
    i = 0
    while budget > min(cost):
        if budget >= cost[i]:
            budget -= cost[i]
            purchase += 1
        i = (i+1) % n
    return purchase

cost = [5, 8, 3]
budget = 12
print(spendItAll(cost, budget))  # Output should be 4