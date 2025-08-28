"""
LeetCode Problem #84: Largest Rectangle in Histogram
https://leetcode.com/problems/largest-rectangle-in-histogram/

Solution using monotonic stack to find the largest rectangle area in histogram.
Time Complexity: O(n) where n is the number of bars
Space Complexity: O(n) for the stack
"""
# pylint: disable=invalid-name

from typing import List

# pylint: disable=too-few-public-methods


class Solution:
    """Solution for Largest Rectangle in Histogram using monotonic stack."""

    def largestRectangleArea(self, heights: List[int]) -> int:
        """
        Find the largest rectangle area in histogram using monotonic stack.

        Args:
            heights: List of bar heights

        Returns:
            Maximum rectangle area

        Examples:
            >>> solution = Solution()
            >>> solution.largestRectangleArea([2, 1, 5, 6, 2, 3])
            10
            >>> solution.largestRectangleArea([2, 4])
            4
        """
        max_area = 0
        stack = []

        histogram = heights + [0]  # Sentinel to process remaining bars

        for idx, height in enumerate(histogram):
            # Process taller bars
            while stack and height < histogram[stack[-1]]:
                # Calculate area with popped bar as height
                bar_height = histogram[stack.pop()]

                # Calculate width
                width = idx - stack[-1] - 1 if stack else idx

                max_area = max(max_area, bar_height * width)

            stack.append(idx)

        return max_area


if __name__ == "__main__":
    solution = Solution()
    test_heights = [2, 1, 5, 6, 2, 3]
    result = solution.largestRectangleArea(test_heights)
    print(f"Largest rectangle area: {result}")  # Output: 10
