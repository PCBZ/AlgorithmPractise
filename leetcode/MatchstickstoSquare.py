from typing import List

class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        total = sum(matchsticks)
        if total % 4 != 0:
            return False
        target = total // 4
        matchsticks.sort(reverse=True)
        sums = [0] * 4

        def backtrack(start: int) -> bool:
            if start == len(matchsticks):
                return sums[0] == target and sums[1] == target and sums[2] == target
            for i in range(4):
                if sums[i] + matchsticks[start] <= target:
                    sums[i] += matchsticks[start]
                    if backtrack(start + 1):
                        return True
                    sums[i] -= matchsticks[start]
            return False
        
        return backtrack(0)


        

if __name__ == "__main__":
    matchsticks = [1, 1, 2, 2, 2]
    print(Solution().makesquare(matchsticks))