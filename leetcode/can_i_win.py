"""
Can I Win - Game Theory with Memoization Solution.

This module contains a solution to determine if the first player can force a win
in a game where players take turns choosing integers from 1 to maxChoosableInteger
and the first player to reach or exceed desiredTotal wins.

LeetCode Problem: https://leetcode.com/problems/can-i-win/
Problem Number: 464
"""


class Solution:
    """Solution class for Can I Win problem."""

    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        """
        Determine if the first player can force a win.
        
        Uses game theory with memoization. Players take turns choosing integers
        from 1 to maxChoosableInteger (each integer can only be used once).
        The first player to reach or exceed desiredTotal wins.
        
        Args:
            maxChoosableInteger: Maximum integer that can be chosen
            desiredTotal: Target total to reach
            
        Returns:
            True if first player can force a win, False otherwise
        """
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
