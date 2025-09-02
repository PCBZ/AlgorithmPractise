"""
LeetCode Problem #395: Longest Substring with At Least K Repeating Characters
https://leetcode.com/problems/longest-substring-with-at-least-k-repeating-characters/

Given a string s and an integer k, return the length of the longest substring
of s such that the frequency of each character in this substring is greater
than or equal to k.

Time Complexity: O(n * 26) = O(n) where n is the length of string
Space Complexity: O(n) for recursion stack in worst case
"""

from collections import defaultdict


class Solution:
    """Solution for finding longest substring with at least k repeating characters."""

    def longest_substring(self, s: str, k: int) -> int:
        """
        Find the longest substring where each character appears at least k times.

        Uses divide and conquer approach: if a character appears fewer than k times
        in the string, it cannot be part of any valid substring, so we can split
        the string at that character and recursively solve subproblems.

        Args:
            s: Input string
            k: Minimum frequency requirement for each character

        Returns:
            Length of the longest valid substring
        """
        if not s or k <= 0:
            return 0

        return self._divide_and_conquer(s, 0, len(s), k)

    def _divide_and_conquer(self, s: str, start: int, end: int, k: int) -> int:
        """
        Recursive helper function implementing divide and conquer strategy.

        Args:
            s: Input string
            start: Start index (inclusive)
            end: End index (exclusive)
            k: Minimum frequency requirement

        Returns:
            Length of longest valid substring in range [start, end)
        """
        if end - start < k:
            return 0

        # Count character frequencies in current range
        freq = defaultdict(int)
        for i in range(start, end):
            freq[s[i]] += 1

        # Find first character with frequency less than k
        for i in range(start, end):
            if freq[s[i]] < k:
                # Split at this character and solve subproblems
                left_result = self._divide_and_conquer(s, start, i, k)
                right_result = self._divide_and_conquer(s, i + 1, end, k)
                return max(left_result, right_result)

        # All characters in current range have frequency >= k
        return end - start

    def longest_substring_sliding_window(self, s: str, k: int) -> int:
        """
        Alternative solution using sliding window with unique character constraint.

        For each possible number of unique characters (1 to 26), use sliding
        window to find the longest substring with exactly that many unique
        characters where each appears at least k times.

        Args:
            s: Input string
            k: Minimum frequency requirement

        Returns:
            Length of the longest valid substring
        """
        if not s or k <= 0:
            return 0

        max_length = 0
        # Try all possible numbers of unique characters (1 to 26)
        for unique_chars in range(1, 27):
            max_length = max(max_length,
                           self._sliding_window_with_unique_count(s, k, unique_chars))

        return max_length

    def _sliding_window_with_unique_count(self, s: str, k: int, target_unique: int) -> int:
        """
        Find longest substring with exactly target_unique characters, each >= k times.

        Args:
            s: Input string
            k: Minimum frequency requirement
            target_unique: Target number of unique characters

        Returns:
            Length of longest valid substring
        """
        left = 0
        char_count = defaultdict(int)
        unique_count = 0  # Number of unique characters in window
        valid_count = 0   # Number of characters with frequency >= k
        max_length = 0

        for right, char in enumerate(s):

            # Expand window
            if char_count[char] == 0:
                unique_count += 1
            char_count[char] += 1
            if char_count[char] == k:
                valid_count += 1

            # Shrink window if too many unique characters
            while unique_count > target_unique:
                left_char = s[left]
                if char_count[left_char] == k:
                    valid_count -= 1
                char_count[left_char] -= 1
                if char_count[left_char] == 0:
                    unique_count -= 1
                left += 1

            # Update result if valid window
            if unique_count == target_unique and valid_count == unique_count:
                max_length = max(max_length, right - left + 1)

        return max_length


if __name__ == "__main__":
    solution = Solution()

    # Test case 1: Basic example
    TEST_STRING_1 = "aaabb"
    TEST_K_1 = 3
    result1 = solution.longest_substring(TEST_STRING_1, TEST_K_1)
    print(f"Input: s='{TEST_STRING_1}', k={TEST_K_1}")
    print(f"Output: {result1}")  # Expected: 3 (substring "aaa")

    # Test case 2: Another example
    TEST_STRING_2 = "ababbc"
    TEST_K_2 = 2
    result2 = solution.longest_substring(TEST_STRING_2, TEST_K_2)
    print(f"Input: s='{TEST_STRING_2}', k={TEST_K_2}")
    print(f"Output: {result2}")  # Expected: 5 (substring "ababb")
