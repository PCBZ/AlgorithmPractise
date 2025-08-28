"""
LeetCode Problem #375: Guess Number Higher or Lower II
URL: https://leetcode.com/problems/guess-number-higher-or-lower-ii/
"""


class Solution:
    """Solution for finding minimum money needed to guarantee win in number guessing game."""

    def getMoneyAmount(self, number_range: int) -> int:
        """Find minimum money amount to guarantee winning the guessing game.

        Use minimax with memoization: for each guess, we pay the guess amount
        and face the worst case of the two remaining subproblems.

        Args:
            number_range: The range of numbers from 1 to n

        Returns:
            Minimum money needed to guarantee win
        """
        memo = {}

        def dp(left: int, right: int) -> int:
            """Calculate minimum cost for range [left, right]."""
            # Memoization: check if already computed
            if (left, right) in memo:
                return memo[(left, right)]

            # Base case: no cost needed for single number or invalid range
            if left >= right:
                return 0

            min_cost = float('inf')

            # Try each possible guess in the range
            for guess in range(left, right + 1):
                # Cost = guess + max(left_cost, right_cost)
                # We face worst case between left and right subproblems
                left_cost = dp(left, guess - 1)
                right_cost = dp(guess + 1, right)
                current_cost = guess + max(left_cost, right_cost)

                # Take minimum across all possible guesses
                min_cost = min(min_cost, current_cost)

            # Store result for future use
            memo[(left, right)] = min_cost
            return min_cost

        return dp(1, number_range)


if __name__ == "__main__":
    test_n = 10
    result = Solution().getMoneyAmount(test_n)
    print(f"Range: 1 to {test_n}")
    print(f"Minimum money needed: {result}")
