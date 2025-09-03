"""
LeetCode Problem #363: Max Sum of Rectangle No Larger Than K

Given an m x n matrix and an integer k, return the max sum of a rectangle
in the matrix such that its sum is no larger than k.
"""
from typing import List


class Solution:
    """Solution for finding max sum rectangle no larger than k."""

    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        """
        Find the maximum sum of a rectangle in the matrix that is <= k.

        Uses brute force approach with 2D prefix sums for O(1) rectangle sum calculation.
        Time complexity: O(m^2 * n^2) where m is rows and n is columns.

        Args:
            matrix: 2D matrix of integers
            k: Maximum allowed sum

        Returns:
            Maximum sum of rectangle that is <= k
        """
        m, n = len(matrix), len(matrix[0])
        prefix_sum = [[0] * (n + 1) for _ in range(m + 1)]
        
        # Build 2D prefix sum array
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                prefix_sum[i][j] = (matrix[i-1][j-1] + prefix_sum[i-1][j] +
                                   prefix_sum[i][j-1] - prefix_sum[i-1][j-1])

        max_sum = float('-inf')

        # Check all possible rectangles
        for r1 in range(m):
            for c1 in range(n):
                for r2 in range(r1, m):
                    for c2 in range(c1, n):
                        # Calculate rectangle sum using prefix sum
                        rect_sum = (prefix_sum[r2+1][c2+1] - prefix_sum[r2+1][c1] -
                                   prefix_sum[r1][c2+1] + prefix_sum[r1][c1])

                        # Update max_sum if this rectangle sum is valid and better
                        if rect_sum <= k:
                            max_sum = max(max_sum, rect_sum)

                        # Early termination if we found exact k
                        if max_sum == k:
                            return k

        return max_sum


if __name__ == "__main__":
    TEST_MATRIX = [[1, 0, 1], [0, -2, 3]]
    TEST_K = 2
    print(Solution().maxSumSubmatrix(TEST_MATRIX, TEST_K))
