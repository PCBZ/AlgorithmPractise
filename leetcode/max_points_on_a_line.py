"""
LeetCode Problem #149: Max Points on a Line

Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane,
return the maximum number of points that lie on the same straight line.

URL: https://leetcode.com/problems/max-points-on-a-line/

Time Complexity: O(n^2)
Space Complexity: O(n)
"""
from typing import List
from collections import defaultdict
from math import gcd


class Solution:
    """Solution for finding maximum points on a line using slope calculation."""

    def maxPoints(self, points: List[List[int]]) -> int:
        """
        Find the maximum number of points that lie on the same straight line.

        Uses slope calculation to group points that are collinear. For each point,
        calculates slopes to all other points and finds the maximum frequency.

        Args:
            points: List of [x, y] coordinates representing points

        Returns:
            Maximum number of points on the same line
        """
        if len(points) <= 2:
            return len(points)

        def get_slope(point1: List[int], point2: List[int]) -> tuple:
            """
            Calculate the slope between two points as a reduced fraction.

            Returns a tuple (dx, dy) representing the slope in reduced form.
            This avoids floating point precision issues.
            """
            x1, y1 = point1
            x2, y2 = point2
            dx = x2 - x1
            dy = y2 - y1

            if dx == 0:
                return (0, 1)  # Vertical line
            if dy == 0:
                return (1, 0)  # Horizontal line

            # Reduce the fraction to avoid precision issues
            g = gcd(abs(dx), abs(dy))
            dx //= g
            dy //= g

            # Ensure consistent sign representation
            if dy < 0:
                dx = -dx
                dy = -dy

            return (dx, dy)

        max_points = 0

        for i, point_i in enumerate(points):
            slope_count = defaultdict(int)
            duplicate_count = 0
            current_max = 0

            for j in range(i + 1, len(points)):
                x1, y1 = point_i
                x2, y2 = points[j]

                # Handle duplicate points
                if x1 == x2 and y1 == y2:
                    duplicate_count += 1
                else:
                    slope = get_slope(point_i, points[j])
                    slope_count[slope] += 1
                    current_max = max(current_max, slope_count[slope])

            # Add 1 for the current point, plus duplicates
            max_points = max(max_points, current_max + duplicate_count + 1)

        return max_points


if __name__ == '__main__':
    test_points = [[1, 1], [3, 2], [5, 3], [4, 1], [2, 3], [1, 4]]
    print(Solution().maxPoints(test_points))  # Expected: 4
