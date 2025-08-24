"""
LeetCode Problem #472: Concatenated Words

URL: https://leetcode.com/problems/concatenated-words/

Given an array of strings words (without duplicates), return all the
concatenated words in the given list of words.

A concatenated word is defined as a string that is comprised entirely of
at least two shorter words in the given array.
"""
from typing import List


class Solution:
    """Solution for finding all concatenated words in a dictionary."""

    def findAllConcatenatedWordsInADict(self, word_list: List[str]) -> List[str]:
        """
        Find all concatenated words in the given dictionary.

        A concatenated word is comprised entirely of at least two shorter
        words from the given array.

        Args:
            word_list: List of words (without duplicates)

        Returns:
            List of concatenated words found in the dictionary

        Time Complexity: O(n * m^3) where n is number of words, m is max word length
        Space Complexity: O(n + m) for word set and recursion stack
        """
        if not word_list:
            return []

        def is_concatenated(word: str) -> bool:
            """
            Check if a word can be formed by concatenating other words.

            Args:
                word: The word to check

            Returns:
                True if the word is concatenated, False otherwise
            """
            word_length = len(word)
            # Create word set excluding the current word to avoid self-reference
            current_word_set = set(filter(lambda w: w != word, word_set))

            def depth_first_search(start_pos: int) -> bool:
                """
                DFS to check if remaining part can be formed by concatenation.

                Args:
                    start_pos: Starting position in the word

                Returns:
                    True if remaining part can be concatenated, False otherwise
                """
                if start_pos == word_length:
                    return True

                for end_pos in range(start_pos, word_length):
                    substring = word[start_pos:end_pos + 1]
                    if substring in current_word_set:
                        if depth_first_search(end_pos + 1):
                            return True
                return False

            return depth_first_search(0)

        word_set = set(word_list)
        return list(filter(is_concatenated, word_list))


if __name__ == "__main__":
    test_words = ["cat", "cats", "catsdogcats", "dog", "dogcatsdog",
                  "hippopotamuses", "rat", "ratcatdogcat"]
    solution = Solution()
    print(solution.findAllConcatenatedWordsInADict(test_words))
