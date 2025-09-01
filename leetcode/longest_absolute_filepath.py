"""
LeetCode Problem #388: Longest Absolute File Path

Given a string input representing the file system in a simplified way, return the length
of the longest absolute path to a file in the abstracted file system. If there is no file
in the system, return 0.

A file contains at least a dot and extension. A directory or subdirectory will not contain
a dot.

URL: https://leetcode.com/problems/longest-absolute-file-path/
"""


class Solution:
    """Solution for finding longest absolute file path."""

    def length_longest_path(self, input_str: str) -> int:
        """
        Find the length of the longest absolute path to a file.

        Uses a stack to track directory depths and cumulative path lengths.

        Args:
            input_str: String representation of the file system

        Returns:
            Length of the longest absolute path to a file, or 0 if no files exist
        """
        if not input_str:
            return 0

        lines = input_str.split('\n')
        stack = []  # Stack to store cumulative lengths at each depth
        max_length = 0

        for line in lines:
            # Count the number of tabs to determine depth
            depth = line.count('\t')
            name = line.lstrip('\t')

            # Pop from stack until we reach the correct depth
            while len(stack) > depth:
                stack.pop()

            # Calculate cumulative length up to current item
            # Add separator '/' if not at root level
            current_length = len(name)
            if stack:
                current_length += stack[-1] + 1  # +1 for '/' separator

            # If this is a file (contains '.'), check if it's the longest
            if '.' in name:
                max_length = max(max_length, current_length)
            else:
                # If it's a directory, add to stack for future calculations
                stack.append(current_length)

        return max_length

    def get_longest_file_path(self, input_str: str) -> str:
        """
        Get the actual longest absolute file path.

        Args:
            input_str: String representation of the file system

        Returns:
            The longest absolute file path, or empty string if no files exist
        """
        if not input_str:
            return ""

        lines = input_str.split('\n')
        stack = []  # Stack to store (cumulative_length, path_components)
        max_length = 0
        longest_path = ""

        for line in lines:
            depth = line.count('\t')
            name = line.lstrip('\t')

            # Pop from stack until we reach the correct depth
            while len(stack) > depth:
                stack.pop()

            # Build current path
            if stack:
                current_length = stack[-1][0] + len(name) + 1  # +1 for '/'
                current_path = stack[-1][1] + [name]
            else:
                current_length = len(name)
                current_path = [name]

            # If this is a file, check if it's the longest
            if '.' in name:
                if current_length > max_length:
                    max_length = current_length
                    longest_path = '/'.join(current_path)
            else:
                # If it's a directory, add to stack
                stack.append((current_length, current_path))

        return longest_path


if __name__ == "__main__":
    solution = Solution()
    TEST_INPUT = ("dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n"
                  "\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext")
    result = solution.length_longest_path(TEST_INPUT)
    print(f"Longest path length: {result}")

    LONGEST_FILE_PATH = solution.get_longest_file_path(TEST_INPUT)
    print(f"Longest path: {LONGEST_FILE_PATH}")
