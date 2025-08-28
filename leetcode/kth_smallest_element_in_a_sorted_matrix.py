"""
LeetCode Problem #378: Kth Smallest Element in a Sorted Matrix
https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/

Solution using heap to efficiently find the kth smallest element.
Time Complexity: O(k * log(min(k, n))) where n is matrix size
Space Complexity: O(min(k, n))
"""

from typing import List
import heapq


# pylint: disable=invalid-name,too-few-public-methods

class Solution:
    """Solution for Kth Smallest Element in a Sorted Matrix using min-heap."""

    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        """
        Find the kth smallest element in a sorted matrix.

        Uses a min-heap to efficiently extract elements in sorted order.
        Only processes elements as needed up to the kth element.

        Args:
            matrix: n x n matrix where each row and column is sorted in ascending order
            k: The rank of the element to find (1-indexed)

        Returns:
            The kth smallest element in the matrix

        Examples:
            >>> solution = Solution()
            >>> solution.kthSmallest([[1,5,9],[10,11,13],[12,13,15]], 8)
            13
            >>> solution.kthSmallest([[1,2],[1,3]], 3)
            2
        """
        matrix_size = len(matrix)

        # Initialize heap with first element of each row
        min_heap = []

        # Add first element of each row to heap
        for i in range(min(k, matrix_size)):
            heapq.heappush(min_heap, (matrix[i][0], i, 0))

        # Extract k elements from heap
        element_result = 0
        for _ in range(k):
            # Get smallest element
            value, row, col = heapq.heappop(min_heap)
            element_result = value

            # Add next element from same row if exists
            if col + 1 < matrix_size:
                heapq.heappush(min_heap, (matrix[row][col + 1], row, col + 1))

        return element_result


if __name__ == "__main__":
    solution = Solution()
    TEST_MATRIX = [[1, 2], [1, 3]]
    TEST_K = 3
    algorithm_result = solution.kthSmallest(TEST_MATRIX, TEST_K)
    print(f"Kth smallest element: {algorithm_result}")
