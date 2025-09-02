"""
LeetCode Problem #473: Matchsticks to Square

URL: https://leetcode.com/problems/matchsticks-to-square/

Determine if given matchsticks can be arranged to form a square.
Uses backtracking to try all possible arrangements of matchsticks into 4 equal sides.
"""
from typing import List


class Solution:
    """Solution class for matchsticks to square problem using backtracking."""

    def makesquare(self, matchsticks: List[int]) -> bool:
        """
        Determine if matchsticks can form a square.

        Uses backtracking to try placing each matchstick on one of 4 sides.
        Optimization: sort matchsticks in descending order to fail faster.

        Args:
            matchsticks: List of positive integers representing matchstick lengths

        Returns:
            True if matchsticks can form a square, False otherwise

        Time Complexity: O(4^n) in worst case, where n is number of matchsticks
        Space Complexity: O(n) for recursion stack
        """
        if not matchsticks or len(matchsticks) < 4:
            return False

        total_length = sum(matchsticks)
        if total_length % 4 != 0:
            return False

        side_length = total_length // 4
        if any(stick > side_length for stick in matchsticks):
            return False

        # Sort in descending order for better pruning
        matchsticks.sort(reverse=True)
        sides = [0, 0, 0, 0]

        def backtrack(index: int) -> bool:
            """
            Recursively try placing matchsticks on each side.

            Args:
                index: Current matchstick index to place

            Returns:
                True if remaining matchsticks can complete the square
            """
            if index == len(matchsticks):
                return (sides[0] == side_length and sides[1] == side_length and
                        sides[2] == side_length and sides[3] == side_length)

            current_stick = matchsticks[index]

            for side_idx in range(4):
                if sides[side_idx] + current_stick <= side_length:
                    sides[side_idx] += current_stick

                    if backtrack(index + 1):
                        return True

                    sides[side_idx] -= current_stick

                    # Pruning: if this side is empty and we failed,
                    # no point trying other empty sides
                    if sides[side_idx] == 0:
                        break

            return False

        return backtrack(0)

    def makesquare_optimized(self, matchsticks: List[int]) -> bool:
        """
        Optimized version with additional pruning strategies.

        Args:
            matchsticks: List of positive integers representing matchstick lengths

        Returns:
            True if matchsticks can form a square, False otherwise

        Time Complexity: O(4^n) worst case, but with better pruning
        Space Complexity: O(n) for recursion stack
        """
        if not matchsticks or len(matchsticks) < 4:
            return False

        total_length = sum(matchsticks)
        if total_length % 4 != 0:
            return False

        side_length = total_length // 4
        if any(stick > side_length for stick in matchsticks):
            return False

        # Sort in descending order for better pruning
        matchsticks.sort(reverse=True)
        sides = [0] * 4

        def backtrack_optimized(index: int) -> bool:
            """
            Optimized backtracking with enhanced pruning.

            Args:
                index: Current matchstick index to place

            Returns:
                True if remaining matchsticks can complete the square
            """
            if index == len(matchsticks):
                return all(side == side_length for side in sides)

            current_stick = matchsticks[index]

            for side_idx in range(4):
                # Skip if adding this stick exceeds side length
                if sides[side_idx] + current_stick > side_length:
                    continue

                # Skip equivalent sides (same current length)
                if side_idx > 0 and sides[side_idx] == sides[side_idx - 1]:
                    continue

                sides[side_idx] += current_stick

                if backtrack_optimized(index + 1):
                    return True

                sides[side_idx] -= current_stick

                # Early termination: if this side is empty and we failed,
                # no point trying other sides
                if sides[side_idx] == 0:
                    break

            return False

        return backtrack_optimized(0)

    def makesquare_iterative(self, matchsticks: List[int]) -> bool:
        """
        Alternative iterative approach using bit manipulation and memoization.

        Args:
            matchsticks: List of positive integers representing matchstick lengths

        Returns:
            True if matchsticks can form a square, False otherwise

        Time Complexity: O(n * 2^n)
        Space Complexity: O(2^n) for memoization
        """
        if not matchsticks or len(matchsticks) < 4:
            return False

        total_length = sum(matchsticks)
        if total_length % 4 != 0:
            return False

        side_length = total_length // 4
        if any(stick > side_length for stick in matchsticks):
            return False

        n = len(matchsticks)
        memo = {}

        def can_form_side(mask: int) -> bool:
            """Check if subset represented by mask can form one side."""
            if mask in memo:
                return memo[mask]

            total = 0
            for i in range(n):
                if mask & (1 << i):
                    total += matchsticks[i]

            memo[mask] = total == side_length
            return memo[mask]

        # Try all possible combinations to form 4 sides
        for mask1 in range(1, 1 << n):
            if not can_form_side(mask1):
                continue

            for mask2 in range(1, 1 << n):
                if mask1 & mask2 or not can_form_side(mask2):
                    continue

                for mask3 in range(1, 1 << n):
                    if ((mask1 & mask3) or (mask2 & mask3) or
                            not can_form_side(mask3)):
                        continue

                    mask4 = ((1 << n) - 1) ^ mask1 ^ mask2 ^ mask3
                    if can_form_side(mask4):
                        return True

        return False


if __name__ == "__main__":
    solution = Solution()

    # Test case 1: Can form square
    test_matchsticks1 = [1, 1, 2, 2, 2]
    print(f"Test 1: {test_matchsticks1} -> {solution.makesquare(test_matchsticks1)}")

    # Test case 2: Cannot form square
    test_matchsticks2 = [3, 3, 3, 3, 4]
    print(f"Test 2: {test_matchsticks2} -> {solution.makesquare(test_matchsticks2)}")

    # Test case 3: Perfect square
    test_matchsticks3 = [5, 5, 5, 5]
    print(f"Test 3: {test_matchsticks3} -> {solution.makesquare(test_matchsticks3)}")

    # Test optimized version
    print(f"Optimized Test 1: {solution.makesquare_optimized(test_matchsticks1)}")
