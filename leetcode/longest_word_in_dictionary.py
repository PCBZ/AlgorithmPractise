"""
LeetCode Problem #720: Longest Word in Dictionary

Given an array of strings words representing an English dictionary, return the longest
word in words that can be built one character at a time by other words in words.

If there is more than one possible answer, return the longest word with the smallest
lexicographical order. If there is no answer, return the empty string.

URL: https://leetcode.com/problems/longest-word-in-dictionary/
"""

from typing import List


class Solution:
    """Solution for finding longest word that can be built one character at a time."""

    def longest_word(self, words: List[str]) -> str:
        """
        Find the longest word that can be built one character at a time.

        Uses a set to track buildable words and sorts by length and lexicographical order.

        Args:
            words: List of words in the dictionary

        Returns:
            The longest word that can be built one character at a time,
            or empty string if no such word exists
        """
        # Sort by length first, then lexicographically
        words.sort(key=lambda x: (len(x), x))
        word_set = set()
        longest_result = ""

        for word in words:
            if len(word) == 1:
                # Single character words are always buildable
                word_set.add(word)
                if len(word) > len(longest_result):
                    longest_result = word
            elif word[:-1] in word_set:
                # Word can be built if prefix (all but last char) exists
                word_set.add(word)
                if len(word) > len(longest_result):
                    longest_result = word

        return longest_result

    def get_build_path(self, words: List[str], target: str) -> List[str]:
        """
        Get the build path for a target word if it can be built.

        Args:
            words: List of words in the dictionary
            target: Target word to find build path for

        Returns:
            List of words showing the build path, or empty list if not buildable
        """
        if not target:
            return []

        words.sort(key=lambda x: (len(x), x))
        word_set = set()
        build_paths = {}

        for word in words:
            if len(word) == 1:
                word_set.add(word)
                build_paths[word] = [word]
            elif word[:-1] in word_set:
                word_set.add(word)
                build_paths[word] = build_paths[word[:-1]] + [word]

        return build_paths.get(target, [])


if __name__ == "__main__":
    solution = Solution()
    TEST_WORDS = ["yo", "ew", "fc", "zrc", "yodn", "fcm", "qm", "qmo",
                  "fcmz", "z", "ewq", "yod", "ewqz", "y"]
    result = solution.longest_word(TEST_WORDS)
    print(f"Longest word: {result}")

    # Test build path
    path = solution.get_build_path(TEST_WORDS, result)
    print(f"Build path for '{result}': {path}")
