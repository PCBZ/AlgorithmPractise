"""
LeetCode Problem #30: Substring with Concatenation of All Words

URL: https://leetcode.com/problems/substring-with-concatenation-of-all-words/

Given a string s and an array of strings words, return all starting indices of
substring(s) that is the concatenation of each word in words exactly once,
in any order, and without any intervening characters.
"""
from typing import List


class Solution:
    """Solution for finding substrings formed by concatenation of all words."""

    def findSubstring(self, input_string: str, word_list: List[str]) -> List[int]:
        """
        Find all starting indices where concatenated words form a substring.

        Args:
            input_string: The input string to search in
            word_list: List of words to concatenate

        Returns:
            List of starting indices where valid concatenations are found

        Time Complexity: O(n * m * k) where n is string length, m is number of words,
                        k is word length
        Space Complexity: O(m) for the words list copy
        """
        if not input_string or not word_list or not word_list[0]:
            return []

        word_len = len(word_list[0])
        total_len = len(word_list) * word_len
        result = []

        for start in range(len(input_string) - total_len + 1):
            remaining_words = word_list.copy()
            position = start

            while position <= start + total_len - word_len:
                current_word = input_string[position:position + word_len]
                if current_word in remaining_words:
                    remaining_words.remove(current_word)
                    position += word_len
                else:
                    break

            if not remaining_words:
                result.append(start)

        return result


if __name__ == '__main__':
    test_string = "barfoothefoobarman"
    test_words = ["foo", "bar"]
    solution = Solution()
    print(solution.findSubstring(test_string, test_words))
