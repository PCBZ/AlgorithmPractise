"""
LeetCode Problem #516: Longest Palindromic Subsequence
https://leetcode.com/problems/longest-palindromic-subsequence/

Solution using dynamic programming to find the longest palindromic subsequence.
Time Complexity: O(n^2) where n is the length of string
Space Complexity: O(n^2) for the DP table
"""


class Solution:
    """Solution for Longest Palindromic Subsequence using DP."""

    def longest_palindrome_subseq(self, s: str) -> int:
        """
        Find the length of the longest palindromic subsequence.

        Args:
            s: Input string

        Returns:
            Length of longest palindromic subsequence
        """
        if not s:
            return 0

        n = len(s)
        # dp[i][j] represents length of longest palindromic subsequence
        # in substring s[i:j+1]
        dp = [[0] * n for _ in range(n)]

        # Fill the DP table
        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if i == j:
                    # Single character is always palindromic
                    dp[i][j] = 1
                elif s[i] == s[j]:
                    # Characters match, add 2 to inner subsequence
                    dp[i][j] = dp[i + 1][j - 1] + 2
                else:
                    # Characters don't match, take max of excluding either end
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])

        return dp[0][n - 1]

    def get_longest_palindrome_subseq(self, s: str) -> str:
        """
        Get the actual longest palindromic subsequence string.

        Args:
            s: Input string

        Returns:
            One of the longest palindromic subsequences
        """
        if not s:
            return ""

        n = len(s)
        dp = [[0] * n for _ in range(n)]

        # Fill the DP table
        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if i == j:
                    dp[i][j] = 1
                elif s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1] + 2
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])

        # Reconstruct palindromic subsequence
        def backtrack(i: int, j: int) -> str:
            if i > j:
                return ""
            if i == j:
                return s[i]

            if s[i] == s[j]:
                # Characters match - they're part of palindrome
                return s[i] + backtrack(i + 1, j - 1) + s[j]

            # Choose the direction that gives longer subsequence
            if dp[i + 1][j] > dp[i][j - 1]:
                return backtrack(i + 1, j)
            return backtrack(i, j - 1)

        return backtrack(0, n - 1)


if __name__ == "__main__":
    solution = Solution()
    TEST_STRING = "bbbab"
    result = solution.longest_palindrome_subseq(TEST_STRING)
    print(f"Longest palindromic subsequence in '{TEST_STRING}': {result}")
