"""
LeetCode Problem #481: Magical String
https://leetcode.com/problems/magical-string/

A magical string s consists only of '1' and '2' and obeys the following rules:
- The string s is magical if s[i] == count of s[i] in group i (1-indexed).
- The first few elements of string s are s = "1221121221221121122……".

Given an integer n, return the number of 1's in the first n characters of magical string s.

Time Complexity: O(n) where n is the input parameter
Space Complexity: O(n) for building the magical string
"""


class Solution:
    """Solution for Magical String problem."""

    def magical_string(self, n: int) -> int:
        """
        Count the number of 1's in the first n characters of magical string.

        The magical string is self-generating: each character indicates how many
        consecutive characters of the alternating pattern to include.

        Args:
            n: Number of characters to consider from the beginning

        Returns:
            Count of '1' characters in the first n positions
        """
        if n <= 0:
            return 0
        if n <= 3:
            return 1  # "122" has 1 one in first 1,2,3 positions

        # Start building the magical string
        magic_str = [1, 2, 2]  # Initial pattern: "122"
        pointer = 2  # Points to position that determines next group size
        ones_count = 1  # Count of 1's so far

        # Generate string until we have at least n characters
        while len(magic_str) < n:
            # Determine next character (alternate between 1 and 2)
            next_char = 1 if magic_str[-1] == 2 else 2

            # Get group size from the character at pointer position
            group_size = magic_str[pointer]

            # Add the group to our string
            for _ in range(group_size):
                if len(magic_str) < n:
                    magic_str.append(next_char)
                    if next_char == 1:
                        ones_count += 1
                else:
                    break

            pointer += 1

        return ones_count

    def get_magical_string_prefix(self, n: int) -> str:
        """
        Generate the first n characters of the magical string.

        Args:
            n: Number of characters to generate

        Returns:
            String containing first n characters of magical string
        """
        if n <= 0:
            return ""
        if n == 1:
            return "1"
        if n == 2:
            return "12"
        if n == 3:
            return "122"

        magic_str = [1, 2, 2]
        pointer = 2

        while len(magic_str) < n:
            next_char = 1 if magic_str[-1] == 2 else 2
            group_size = magic_str[pointer]

            for _ in range(group_size):
                if len(magic_str) < n:
                    magic_str.append(next_char)
                else:
                    break

            pointer += 1

        return ''.join(str(x) for x in magic_str[:n])

    def magical_string_optimized(self, n: int) -> int:
        """
        Optimized version using string operations.

        Args:
            n: Number of characters to consider

        Returns:
            Count of '1' characters in first n positions
        """
        if n <= 0:
            return 0
        if n <= 3:
            return 1

        magic_str = "122"
        pointer = 2

        while len(magic_str) < n:
            next_char = "1" if magic_str[-1] == "2" else "2"
            group_size = int(magic_str[pointer])
            magic_str += next_char * group_size
            pointer += 1

        return magic_str[:n].count("1")


if __name__ == "__main__":
    solution = Solution()

    # Test case 1
    TEST_N_1 = 6
    RESULT_1 = solution.magical_string(TEST_N_1)
    print(f"Input: n={TEST_N_1}")
    print(f"Output: {RESULT_1}")  # Expected: 3
    print(f"Magical string prefix: {solution.get_magical_string_prefix(TEST_N_1)}")

    # Test case 2
    TEST_N_2 = 1
    RESULT_2 = solution.magical_string(TEST_N_2)
    print(f"Input: n={TEST_N_2}")
    print(f"Output: {RESULT_2}")  # Expected: 1
