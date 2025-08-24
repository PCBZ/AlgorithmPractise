"""
Boats to Save People - Two Pointer Solution.

This module contains a solution to find the minimum number of boats needed
to save all people, where each boat can carry at most 2 people and has a
weight limit.

LeetCode Problem: https://leetcode.com/problems/boats-to-save-people/
Problem Number: 881
"""

from typing import List


class Solution:
    """Solution class for Boats to Save People problem."""

    def numRescueBoats(self, people: List[int], limit: int) -> int:
        """
        Find the minimum number of boats to save all people.
        
        Each boat can carry at most 2 people at the same time, provided the
        sum of their weights is at most limit. The strategy is to use a greedy
        approach with two pointers: pair the lightest with the heaviest person
        if possible, otherwise take the heaviest person alone.
        
        Args:
            people: List of people's weights
            limit: Maximum weight capacity of each boat
            
        Returns:
            Minimum number of boats needed
        """
        people.sort()
        count = 0
        left, right = 0, len(people) - 1

        while left <= right:
            # Try to pair lightest with heaviest
            if people[left] + people[right] <= limit:
                left += 1
            right -= 1
            count += 1

        return count


if __name__ == "__main__":
    test_people = [1, 5, 3, 5]
    test_limit = 7
    print(Solution().numRescueBoats(test_people, test_limit))
