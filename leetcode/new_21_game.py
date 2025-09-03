"""
LeetCode #837: New 21 Game
https://leetcode.com/problems/new-21-game/

Return the probability that Alice has n or fewer points.

Time: O(n), Space: O(n)
"""


class Solution:
    """New 21 Game using dynamic programming with sliding window."""

    def new21Game(self, n: int, k: int, max_pts: int) -> float:
        """Calculate probability that Alice ends with n or fewer points."""
        if k == 0 or n >= k + max_pts:
            return 1.0

        dp = [0] * (1 + n)
        dp[0] = 1.0
        window_sum = 1.0
        final_prob = 0.0

        for i in range(1, n + 1):
            dp[i] = window_sum / max_pts

            if i < k:
                window_sum += dp[i]
            else:
                final_prob += dp[i]

            if i - max_pts >= 0:
                window_sum -= dp[i - max_pts]

        return final_prob


if __name__ == "__main__":
    solution = Solution()
    TEST_N1 = 10
    TEST_K1 = 1
    TEST_MAX_PTS1 = 10
    result1 = solution.new21Game(TEST_N1, TEST_K1, TEST_MAX_PTS1)
    print(f"Test 1 - n={TEST_N1}, k={TEST_K1}, maxPts={TEST_MAX_PTS1}: {result1}")

    TEST_N2 = 6
    TEST_K2 = 1
    TEST_MAX_PTS2 = 10
    result2 = solution.new21Game(TEST_N2, TEST_K2, TEST_MAX_PTS2)
    print(f"Test 2 - n={TEST_N2}, k={TEST_K2}, maxPts={TEST_MAX_PTS2}: {result2}")

    TEST_N3 = 21
    TEST_K3 = 17
    TEST_MAX_PTS3 = 10
    result3 = solution.new21Game(TEST_N3, TEST_K3, TEST_MAX_PTS3)
    print(f"Test 3 - n={TEST_N3}, k={TEST_K3}, maxPts={TEST_MAX_PTS3}: {result3}")
