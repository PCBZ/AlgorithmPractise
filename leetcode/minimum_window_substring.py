"""
LeetCode #76: Minimum Window Substring

Find the minimum window substring of s that contains all characters in t.

Time: O(|s| + |t|), Space: O(|s| + |t|)
"""
from collections import Counter


class Solution:
    """Find minimum window substring using sliding window technique."""

    def minWindow(self, s: str, t: str) -> str:
        """Find minimum window substring containing all characters of t."""
        if not s or not t or len(s) < len(t):
            return ""

        need = Counter(t)
        left = right = 0
        start, length = 0, float("inf")
        valid_count = 0
        window = {}

        while right < len(s):
            # Expand window
            char = s[right]
            right += 1
            if char in need:
                window[char] = window.get(char, 0) + 1
                if window[char] == need[char]:
                    valid_count += 1

            # Contract window
            while valid_count == len(need):
                if right - left < length:
                    start, length = left, right - left
                char = s[left]
                left += 1
                if char in need:
                    if window[char] == need[char]:
                        valid_count -= 1
                    window[char] -= 1

        return "" if length == float("inf") else s[start:start + length]


if __name__ == "__main__":
    TEST_S = "ADOBECODEBANC"
    TEST_T = "ABC"
    print(Solution().minWindow(TEST_S, TEST_T))
