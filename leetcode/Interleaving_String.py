"""
LeetCode Problem #97: Interleaving String
https://leetcode.com/problems/interleaving-string/

Given strings s1, s2, and s3, find whether s3 is formed by an interleaving of s1 and s2.
An interleaving is formed by merging two strings while preserving the relative order
of characters in each string.
"""


class Solution:
    """Solution for Interleaving String problem."""

    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        """
        Check if s3 is an interleaving of s1 and s2 using dynamic programming.
        Time: O(m*n), Space: O(m*n)
        """
        m, n = len(s1), len(s2)

        # Early exit if lengths don't match
        if m + n != len(s3):
            return False

        # dp[i][j] = True if s3[:i+j] can be formed by interleaving s1[:i] and s2[:j]
        dp = [[False] * (n + 1) for _ in range(m + 1)]

        for i in range(m + 1):
            for j in range(n + 1):
                if i == 0 and j == 0:
                    dp[i][j] = True
                elif i == 0:
                    # Only using characters from s2
                    dp[i][j] = dp[i][j-1] and s2[j-1] == s3[j-1]
                elif j == 0:
                    # Only using characters from s1
                    dp[i][j] = dp[i-1][j] and s1[i-1] == s3[i-1]
                else:
                    # Can take from either s1 or s2
                    take_s1 = dp[i-1][j] and s1[i-1] == s3[i+j-1]
                    take_s2 = dp[i][j-1] and s2[j-1] == s3[i+j-1]
                    dp[i][j] = take_s1 or take_s2

        return dp[m][n]


if __name__ == "__main__":
    test_s1 = "aabcc"
    test_s2 = "dbbca"
    test_s3 = "aadbbbaccc"
    print(Solution().isInterleave(test_s1, test_s2, test_s3))
