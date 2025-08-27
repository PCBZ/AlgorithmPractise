"""
LeetCode Problem #438: Find All Anagrams in a String
URL: https://leetcode.com/problems/find-all-anagrams-in-a-string/
"""
from collections import Counter
from typing import List


class Solution:
    """Solution for finding all anagrams in a string."""

    def findAnagrams(self, text: str, pattern: str) -> List[int]:
        """Find all start indices of anagrams of pattern in text."""
        if len(pattern) > len(text):
            return []

        result = []
        pattern_len = len(pattern)
        pattern_count = Counter(pattern)
        window_count = Counter()

        # Initialize sliding window
        for i in range(pattern_len):
            window_count[text[i]] += 1

        # Check first window
        if window_count == pattern_count:
            result.append(0)

        # Slide window through rest of string
        for i in range(pattern_len, len(text)):
            # Add new character
            window_count[text[i]] += 1

            # Remove old character
            left_char = text[i - pattern_len]
            window_count[left_char] -= 1
            if window_count[left_char] == 0:
                del window_count[left_char]

            # Check if current window is anagram
            if window_count == pattern_count:
                result.append(i - pattern_len + 1)

        return result


if __name__ == "__main__":
    # Example usage
    test_string = "cbaebabacd"
    test_pattern = "abc"
    solution = Solution()
    indices = solution.findAnagrams(test_string, test_pattern)
    print(f"Anagram indices: {indices}")
