"""
LeetCode 316: Remove Duplicate Letters

URL: https://leetcode.com/problems/remove-duplicate-letters/
"""

from collections import Counter
from typing import Set


class Solution:
    """Solution for Remove Duplicate Letters using greedy monotonic stack."""

    def removeDuplicateLetters(self, s: str) -> str:
        """
        Remove duplicate letters to get lexicographically smallest result.
        Time: O(n), Space: O(1)
        """
        stack = []
        visited: Set[str] = set()
        char_count = Counter(s)

        for char in s:
            char_count[char] -= 1

            if char in visited:
                continue

            while (stack and stack[-1] > char and char_count[stack[-1]] > 0):
                removed_char = stack.pop()
                visited.remove(removed_char)

            stack.append(char)
            visited.add(char)

        return ''.join(stack)


if __name__ == "__main__":
    sol = Solution()

    TEST_STR = "cbacdcbc"
    RESULT = sol.removeDuplicateLetters(TEST_STR)
    print(f"Input: {TEST_STR}, Output: {RESULT}")
