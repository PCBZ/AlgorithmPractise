"""
LeetCode Problem #424: Longest Repeating Character Replacement

Given a string s that consists of only uppercase English letters, you can perform
at most k operations on that string. In one operation, you can choose any character
of the string and change it to any other uppercase English letter.

URL: https://leetcode.com/problems/longest-repeating-character-replacement/
"""

from collections import defaultdict


class Solution:
    """Solution for finding longest repeating character replacement."""

    def character_replacement(self, s: str, k: int) -> int:
        """
        Find the longest substring with at most k character replacements.

        Uses sliding window technique with frequency counting.

        Args:
            s: String consisting of uppercase English letters
            k: Maximum number of operations allowed

        Returns:
            Length of the longest substring after at most k replacements
        """
        if not s:
            return 0

        left = 0
        max_count = 0
        max_length = 0
        counter = defaultdict(int)

        for right, char in enumerate(s):
            # Add current character to window
            counter[char] += 1
            # Update max frequency in current window
            max_count = max(max_count, counter[char])

            # If window is invalid (need more than k replacements)
            while right - left + 1 - max_count > k:
                counter[s[left]] -= 1
                left += 1

            # Update maximum length seen so far
            max_length = max(max_length, right - left + 1)

        return max_length

    def get_replacement_details(self, s: str, k: int) -> dict:
        """
        Get detailed information about the character replacement process.

        Args:
            s: String consisting of uppercase English letters
            k: Maximum number of operations allowed

        Returns:
            Dictionary with details about the optimal substring
        """
        if not s:
            return {"length": 0, "start": 0, "end": 0, "most_frequent": ""}

        left = 0
        max_count = 0
        max_length = 0
        best_start = 0
        best_end = 0
        most_frequent_char = ""
        counter = defaultdict(int)

        for right, char in enumerate(s):
            # Add current character to window
            counter[char] += 1
            # Update max frequency and most frequent character
            if counter[char] > max_count:
                max_count = counter[char]
                most_frequent_char = char

            # If window is invalid (need more than k replacements)
            while right - left + 1 - max_count > k:
                counter[s[left]] -= 1
                # Recalculate max_count after shrinking window
                if counter[s[left]] + 1 == max_count:
                    max_count = max(counter.values()) if counter else 0
                left += 1

            # Update maximum length and best window
            current_length = right - left + 1
            if current_length > max_length:
                max_length = current_length
                best_start = left
                best_end = right + 1

        return {
            "length": max_length,
            "start": best_start,
            "end": best_end,
            "most_frequent": most_frequent_char
        }


if __name__ == "__main__":
    solution = Solution()
    TEST_STRING_1 = "XYYX"
    TEST_K_1 = 2
    print(solution.character_replacement(TEST_STRING_1, TEST_K_1))  # Output: 4

    TEST_STRING_2 = "AAABABB"
    TEST_K_2 = 1
    print(solution.character_replacement(TEST_STRING_2, TEST_K_2))  # Output: 5
