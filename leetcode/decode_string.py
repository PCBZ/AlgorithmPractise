"""
LeetCode Problem #394: Decode String

URL: https://leetcode.com/problems/decode-string/

Decode strings with format k[encoded_string] where k is repetition count.
Example: "3[a2[c]]" -> "accaccacc"
"""


class Solution:
    """Solution for decoding strings using stack-based approach."""

    def decodeString(self, encoded_string: str) -> str:
        """
        Decode encoded string using stack for nested brackets.

        Args:
            encoded_string: String like "3[a]2[bc]" or "2[a3[b]]"

        Returns:
            Decoded string with repetitions applied
        """
        stack = []
        current_string = ""
        current_number = 0

        for char in encoded_string:
            if char.isdigit():
                current_number = current_number * 10 + int(char)
            elif char == '[':
                # Push state to stack and reset
                stack.append((current_string, current_number))
                current_string = ""
                current_number = 0
            elif char == ']':
                # Pop and build repeated string
                prev_string, repeat_count = stack.pop()
                current_string = prev_string + repeat_count * current_string
            else:
                # Add character
                current_string += char

        return current_string


if __name__ == "__main__":
    # Test example
    example_string = "3[a2[c]]"
    solution = Solution()
    print(solution.decodeString(example_string))
