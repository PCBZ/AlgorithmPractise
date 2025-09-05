"""
LeetCode 600: Non-negative Integers without Consecutive Ones
https://leetcode.com/problems/non-negative-integers-without-consecutive-ones/

Count integers in [0, n] without consecutive 1s in binary representation.
"""


class Solution:
    """Solution using digit DP with Fibonacci pattern."""

    def findIntegers(self, n: int) -> int:  # pylint: disable=invalid-name
        """Count integers without consecutive 1s using digit DP."""
        bits = bin(n)[2:]
        m = len(bits)
        fibonacci = [0] * (m + 1)
        fibonacci[0], fibonacci[1] = 1, 2
        for i in range(2, m + 1):
            fibonacci[i] = fibonacci[i - 1] + fibonacci[i - 2]

        count = 0
        prev = '0'
        for idx, bit in enumerate(bits):
            if bit == '1':
                count += fibonacci[m - 1 - idx]
                if prev == '1':
                    return count
            prev = bit
        return count + 1


if __name__ == "__main__":
    solution = Solution()
    print(solution.findIntegers(5))
