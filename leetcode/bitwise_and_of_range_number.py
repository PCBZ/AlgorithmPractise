"""
Bitwise AND of Numbers Range - Bit Manipulation Solution.

This module contains a solution to find the bitwise AND of all numbers
in a given range [left, right].

The key insight is that the bitwise AND of a range will have 1 bits only
in positions where all numbers in the range have 1 bits.

LeetCode Problem: https://leetcode.com/problems/bitwise-and-of-numbers-range/
Problem Number: 201
"""


class Solution:
    """Solution class for Bitwise AND of Numbers Range problem."""

    def rangeBitwiseAnd(self, range_left: int, range_right: int) -> int:
        """
        Find the bitwise AND of all numbers in the range [left, right].
        
        The algorithm works by finding the common prefix of the binary
        representations of left and right. The AND of all numbers in
        the range will be this common prefix followed by zeros.
        
        Args:
            range_left: The left boundary of the range (inclusive)
            range_right: The right boundary of the range (inclusive)
            
        Returns:
            The bitwise AND of all numbers in the range
        """
        move_count = 0
        while range_left != range_right:
            range_left >>= 1
            range_right >>= 1
            move_count += 1
        return range_left << move_count


if __name__ == "__main__":
    test_left, test_right = 5, 7
    print(Solution().rangeBitwiseAnd(test_left, test_right))
