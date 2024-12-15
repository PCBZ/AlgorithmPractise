from typing import List

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        remain = 0
        for start in range(n):
            remain = gas[start]
            for i in range(1, n+1):
                idx = (start + i) % n
                remain -= cost[idx-1]
                if remain < 0:
                    break
                remain += gas[idx]
            if remain >= 0:
                return start
        return -1

gas = [1, 2, 3, 4, 5]
cost = [3, 4, 5, 1, 2]
print(Solution().canCompleteCircuit(gas, cost))