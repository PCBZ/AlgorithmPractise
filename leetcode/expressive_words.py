"""
LeetCode Problem #809: Expressive Words
URL: https://leetcode.com/problems/expressive-words/
"""


class Solution:
    """Solution for expressive words problem."""

    def expressiveWords(self, target, words):
        """Count words that can be made expressive to match target."""
        def is_expressive(target_str, word):
            """Check if word can be extended to match target."""
            target_len, word_len = len(target_str), len(word)
            target_pos = word_pos = 0

            while target_pos < target_len and word_pos < word_len:
                if target_str[target_pos] != word[word_pos]:
                    return False

                # Count consecutive characters
                target_count = 1
                while (target_pos + 1 < target_len and
                       target_str[target_pos + 1] == target_str[target_pos]):
                    target_pos += 1
                    target_count += 1

                word_count = 1
                while (word_pos + 1 < word_len and
                       word[word_pos + 1] == word[word_pos]):
                    word_pos += 1
                    word_count += 1

                # Extension rules: 1->3+, 2->2 only, 3+->3+
                if word_count > target_count:
                    return False
                if word_count < target_count:
                    if word_count == 2:
                        return False
                    if word_count == 1 and target_count < 3:
                        return False

                target_pos += 1
                word_pos += 1

            return target_pos == target_len and word_pos == word_len

        return sum(1 for word in words if is_expressive(target, word))


if __name__ == "__main__":
    # Example usage
    target_string = "heeellooo"
    word_list = ["hello", "hi", "helo"]
    solution = Solution()
    result = solution.expressiveWords(target_string, word_list)
    print(f"Number of expressive words: {result}")
