"""
LeetCode Problem #115: Distinct Subsequences

URL: https://leetcode.com/problems/distinct-subsequences/

Count distinct subsequences of string s that equal string t using dynamic programming.
Example: s="rabbbit", t="rabbit" -> 3 (remove different 'b's to get "rabbit")
"""


class Solution:
    """Solution for counting distinct subsequences using dynamic programming."""

    def numDistinct(self, source: str, target: str) -> int:
        """
        Count distinct subsequences of source that equal target.

        Uses 2D DP where dp[i][j] represents number of ways to form
        target[0:j] using source[0:i].

        Args:
            source: Source string to find subsequences in
            target: Target string to match

        Returns:
            Number of distinct subsequences
        """
        m, n = len(source), len(target)
        dp = [(n+1) * [0] for _ in range(m+1)]

        # Base case: empty target can be formed in 1 way (by choosing nothing)
        for i in range(m+1):
            dp[i][0] = 1

        for i in range(1, m+1):
            for j in range(1, n+1):
                if source[i-1] == target[j-1]:
                    # Can use current char or skip it
                    dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
                else:
                    # Can only skip current char
                    dp[i][j] = dp[i-1][j]

        return dp[m][n]


if __name__ == "__main__":
    test_s = "rabbbit"
    test_t = "rabbit"
    print(Solution().numDistinct(test_s, test_t))
