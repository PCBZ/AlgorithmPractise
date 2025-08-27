"""
LeetCode Problem #448: Find All Numbers Disappeared in an Array
URL: https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/
"""
from typing import List


class Solution:
    """Solution for finding all disappeared numbers in an array."""

    def findDisappearedNumbers(self, numbers: List[int]) -> List[int]:
        """Find all numbers from 1 to n that are missing from the array."""
        n = len(numbers)

        # Mark numbers as seen by making values at those indices negative
        for num in numbers:
            index = abs(num) - 1  # Convert to 0-based index
            if numbers[index] > 0:
                numbers[index] = -numbers[index]

        # Find indices with positive values (missing numbers)
        result = []
        for i in range(n):
            if numbers[i] > 0:
                result.append(i + 1)  # Convert back to 1-based

        return result


if __name__ == "__main__":
    # Example usage
    test_nums = [4, 3, 2, 7, 8, 2, 3, 1]
    solution = Solution()
    missing = solution.findDisappearedNumbers(test_nums.copy())
    print(f"Missing numbers: {missing}")
