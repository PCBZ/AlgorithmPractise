"""
LeetCode Problem #926: Flip String to Monotone Increasing
URL: https://leetcode.com/problems/flip-string-to-monotone-increasing/
"""


class Solution:
    """Solution for flipping string to monotone increasing."""

    def minFlipsMonoIncr(self, binary_string: str) -> int:
        """Find minimum flips to make string monotone increasing.

        A string is monotone increasing if all 0s appear before all 1s.
        Use dynamic programming to track minimum flips.

        Args:
            binary_string: String containing only '0' and '1'

        Returns:
            Minimum number of flips needed
        """
        # dp0: min flips if ending with all 0s
        # dp1: min flips if ending with 0s followed by 1s
        dp0 = dp1 = 0

        for digit in binary_string:
            if digit == '0':
                # To keep '0', we can flip previous 1s to 0s or keep current state
                dp1 = min(dp0, dp1) + 1
            else:
                # To keep '1', we either start 1s section or continue it
                new_dp1 = min(dp0, dp1)
                # To force all 0s, we must flip this '1' to '0'
                dp0 += 1
                dp1 = new_dp1

        # Return minimum of both strategies
        return min(dp0, dp1)


if __name__ == "__main__":
    test_string = "00110"
    result = Solution().minFlipsMonoIncr(test_string)
    print(f"Input: {test_string}")
    print(f"Minimum flips: {result}")
