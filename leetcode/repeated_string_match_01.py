"""
LeetCode 686: Repeated String Match

Given two strings a and b, return the minimum number of times you should repeat string a
so that string b is a substring of it. If it is impossible for b to be a substring of a
after repeating it, return -1.

URL: https://leetcode.com/problems/repeated-string-match/
"""

from math import ceil


class Solution:  # pylint: disable=too-few-public-methods
    """Solution for Repeated String Match using optimal string matching."""

    def repeatedStringMatch(self, a: str, b: str) -> int:  # pylint: disable=invalid-name
        """
        Find minimum repetitions of string a to contain string b as substring.

        Algorithm:
        1. Calculate minimum repetitions needed: ceil(len(b) / len(a))
        2. Check if b is substring of a repeated that many times
        3. If not, try one more repetition (handles edge cases)
        4. Return -1 if impossible

        Time: O(n*m) where n=len(a)*repetitions, m=len(b)
        Space: O(n) for the repeated string
        """
        len_a, len_b = len(a), len(b)

        # Handle edge case: empty b
        if len_b == 0:
            return 1

        # Calculate minimum repetitions needed
        min_reps = ceil(len_b / len_a)

        # Try minimum repetitions
        repeated_string = a * min_reps
        if b in repeated_string:
            return min_reps

        # Try one more repetition for edge cases
        repeated_string += a
        if b in repeated_string:
            return min_reps + 1

        return -1


if __name__ == "__main__":
    sol = Solution()

    # Test case 1: a="abcd", b="cdabcdab" -> 3
    result1 = sol.repeatedStringMatch("abcd", "cdabcdab")
    print(f"Test 1: {result1}")

    # Test case 2: a="a", b="aa" -> 2
    result2 = sol.repeatedStringMatch("a", "aa")
    print(f"Test 2: {result2}")

    # Test case 3: a="a", b="a" -> 1
    result3 = sol.repeatedStringMatch("a", "a")
    print(f"Test 3: {result3}")

    # Test case 4: a="abc", b="wxyz" -> -1
    result4 = sol.repeatedStringMatch("abc", "wxyz")
    print(f"Test 4: {result4}")
