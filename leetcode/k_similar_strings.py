"""
LeetCode Problem #854: K-Similar Strings
https://leetcode.com/problems/k-similar-strings/

Solution using BFS to find minimum swaps needed to transform one string into another.
Time Complexity: O(n! * n) where n is the string length (worst case)
Space Complexity: O(n! * n) for storing all possible states
"""

from typing import List
from collections import deque


class Solution:
    """Solution for K-Similar Strings problem using BFS."""

    def kSimilarity(self, first_string: str, second_string: str) -> int:
        """
        Find minimum number of swaps to transform first_string into second_string.

        Uses BFS to explore all possible swap states, finding the minimum number
        of swaps needed. Only considers swaps that bring us closer to the target.

        Args:
            first_string: Source string to transform
            second_string: Target string to achieve

        Returns:
            Minimum number of swaps needed, or -1 if impossible

        Examples:
            >>> solution = Solution()
            >>> solution.kSimilarity("ab", "ba")
            1
            >>> solution.kSimilarity("abc", "bca")
            2
        """
        def get_neighbors(current_string: str) -> List[str]:
            """
            Generate all valid neighbor strings by swapping characters.

            Finds the first position where current_string differs from target,
            then tries swapping with all positions that would bring us closer.

            Args:
                current_string: Current state string

            Returns:
                List of valid neighbor strings after one swap
            """
            neighbors_list = []

            # Find first position where strings differ
            position = 0
            while (position < len(current_string) and
                   current_string[position] == second_string[position]):
                position += 1

            # If strings are identical, no neighbors needed
            if position == len(current_string):
                return neighbors_list

            # Try swapping with positions that help us get closer to target
            for swap_pos in range(position + 1, len(current_string)):
                # Only swap if it places the correct character at position
                # and the character we're moving is currently in wrong place
                if (current_string[swap_pos] == second_string[position] and
                    current_string[swap_pos] != second_string[swap_pos]):

                    # Perform the swap
                    string_list = list(current_string)
                    string_list[position], string_list[swap_pos] = (
                        string_list[swap_pos], string_list[position])
                    neighbors_list.append("".join(string_list))

            return neighbors_list

        # BFS to find minimum swaps
        queue = deque([(first_string, 0)])
        visited = {first_string}

        while queue:
            current_state, steps = queue.popleft()

            # Check if we've reached the target
            if current_state == second_string:
                return steps

            # Explore all valid neighbors
            for neighbor in get_neighbors(current_state):
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, steps + 1))

        return -1  # Should not reach here for valid inputs


if __name__ == "__main__":
    solution = Solution()
    test_string_1 = "ab"
    test_string_2 = "ba"
    result = solution.kSimilarity(test_string_1, test_string_2)
    print(f"K-Similarity of '{test_string_1}' and '{test_string_2}': {result}")
