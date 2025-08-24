"""
LeetCode Problem #38: Count and Say

URL: https://leetcode.com/problems/count-and-say/

The count-and-say sequence is a sequence of digit strings defined by the
recursive formula:
- countAndSay(1) = "1"
- countAndSay(n) is the way you would "say" the digit string from
  countAndSay(n-1), which is then converted into a different digit string.

To determine how you "say" a digit string, you read it from left to right and
describe what you see. For example, "3322251" is "two 3s, three 2s, one 5, one 1".
"""


class Solution:
    """Solution for the Count and Say problem."""

    def countAndSay(self, n: int) -> str:
        """
        Generate the nth term in the count-and-say sequence.

        Args:
            n: The position in the sequence (1-indexed)

        Returns:
            The nth term in the count-and-say sequence

        Time Complexity: O(n * m) where m is the average length of sequences
        Space Complexity: O(m) for the result string
        """
        if n <= 0:
            return ""

        def next_rle(string: str) -> str:
            """
            Generate the next run-length encoding (count-and-say) string.

            Args:
                string: The current string to encode

            Returns:
                The run-length encoded string
            """
            if not string:
                return ""

            result = ''
            prev_char = ''
            count = 0

            for char in string:
                if char == prev_char or not prev_char:
                    count += 1
                else:
                    result += str(count) + prev_char
                    count = 1
                prev_char = char

            # Add the final group
            result += str(count) + prev_char
            return result

        result = '1'
        if n == 1:
            return result

        for _ in range(1, n):
            result = next_rle(result)
        return result


if __name__ == '__main__':
    test_n = 4
    solution = Solution()
    print(solution.countAndSay(test_n))
