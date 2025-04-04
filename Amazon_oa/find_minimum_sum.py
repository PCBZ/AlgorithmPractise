from typing import List

class Solution:
    def find_minimum_sum(self, power: List[int]) -> int:
        increase = 0
        n = len(power)
        for i in range(1, n):
            if power[i] < power[i - 1]:
                diff = power[i - 1] - power[i]
                increase += diff
        return increase

if __name__ == "__main__":
    power = [3,2,1,9,2]
    print(Solution().find_minimum_sum(power))
