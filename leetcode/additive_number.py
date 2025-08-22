"""
Additive Number - LeetCode Problem Solution
Source: https://leetcode.com/problems/additive-number/description/

An additive number is a string whose digits can form an additive sequence.
A valid additive sequence should contain at least three numbers.
"""


class Solution:
    """
    Solution class for the Additive Number problem.

    Uses backtracking to check if a string can form an additive sequence.
    """

    def isAdditiveNumber(self, number: str) -> bool:
        """
        Check if the given string is an additive number.

        Args:
            number: String of digits to check

        Returns:
            True if the string can form an additive sequence, False otherwise
        """
        def isValidFrom(first: int, second: int, start: int) -> bool:
            count = 2
            while start < n:
                third = first + second
                third_str = str(third)
                if not number.startswith(third_str, start):
                    return False
                first, second = second, third
                start += len(third_str)
                count += 1
            return count >= 3

        n = len(number)
        for i in range(1, n):
            for j in range(i+1, n+1):
                first, second = number[:i], number[i:j]
                if (len(first) > 1 and first[0] == '0') or \
                   (len(second) > 1 and second[0] == "0"):
                    continue
                if isValidFrom(int(first), int(second), j):
                    return True
        return False


if __name__ == "__main__":
    test_num = "112358"
    print(Solution().isAdditiveNumber(test_num))
