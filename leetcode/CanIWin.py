class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        if desiredTotal <= 0:
            return True
        total = maxChoosableInteger * (maxChoosableInteger + 1) // 2
        if total < desiredTotal:
            return False
        memo = {}

        def canWin(used: int, cur_total: int) -> bool:
            if cur_total >= desiredTotal:
                return False
            if used in memo:
                return memo[used]
            for i in range(maxChoosableInteger):
                if used & (1 << i) == 0:
                    if not canWin(used | (1 << i), cur_total + i + 1):
                        memo[used] = True
                        return True
            memo[used] = False
            return False
        
        return canWin(0, 0)



if __name__ == "__main__":
    print(Solution().canIWin(7, 16))