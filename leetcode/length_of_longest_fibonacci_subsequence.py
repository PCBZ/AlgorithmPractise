"""
LeetCode Problem #873: Length of Longest Fibonacci Subsequence
https://leetcode.com/problems/length-of-longest-fibonacci-subsequence/

Solution using dynamic programming to find longest Fibonacci-like subsequence.
Time Complexity: O(n^2) where n is the length of array
Space Complexity: O(n^2) for the DP table
"""
# pylint: disable=invalid-name

from typing import List

# pylint: disable=too-few-public-methods
class Solution:
    """Solution for Length of Longest Fibonacci Subsequence using DP."""

    def len_longest_fib_subseq(self, arr: List[int]) -> int:
        """
        Find the longest Fibonacci-like subsequence length.

        Args:
            arr: Strictly increasing array of positive integers

        Returns:
            Length of longest Fibonacci-like subsequence, or 0 if none exists
        """
        index_map = {ele: index for index, ele in enumerate(arr)}
        n = len(arr)
        dp = [[2] * n for _ in range(n)]
        longest = 0

        for i in range(n):
            for j in range(i):
                first = arr[i] - arr[j]
                if first < arr[j] and first in index_map:
                    new_idx = index_map[first]
                    dp[j][i] = dp[new_idx][j] + 1
                    longest = max(longest, dp[j][i])

        return longest if longest >= 3 else 0
if __name__ == "__main__":
    solution = Solution()

    test_arr = [1, 2, 3, 4, 5, 6, 7, 8]
    print(f"Test 1: {solution.len_longest_fib_subseq(test_arr)}")  # Output: 5

    test_arr = [1, 3, 7, 11, 12, 14, 18]
    print(f"Test 2: {solution.len_longest_fib_subseq(test_arr)}")  # Output: 3

    test_arr = [1, 2, 3]
    print(f"Test 3: {solution.len_longest_fib_subseq(test_arr)}")  # Output: 3
