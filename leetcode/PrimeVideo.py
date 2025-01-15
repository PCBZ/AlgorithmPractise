from typing import List

class Solution:
    def primeVideo(self, power: List[int], armor: int) -> int:
        cost = sum(power)
        min_health = float('inf')
        for po in power:
            min_health = min(min_health, cost - po + max(0, po - armor) + 1)
        return min_health



if __name__ == "__main__":
    power = [1, 2, 6, 7]
    armor = 5
    print(Solution().primeVideo(power, armor))