"""
Search a 2D Matrix - Binary Search Solution
Source: https://leetcode.com/problems/search-a-2d-matrix/description/
"""

from typing import List

class Solution:
    """
    Solution class for the Search a 2D Matrix problem.
    Uses binary search on the flattened matrix to find the target value.
    """

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """
        Search for a target value in a 2D matrix.
        
        Args:
            matrix: 2D matrix sorted in ascending order
            target: The value to search for
            
        Returns:
            True if target is found, False otherwise
        """
        m, n = len(matrix), len(matrix[0])
        start, end = 0, m * n - 1
        while start <= end:
            mid = (start + end) // 2
            row, col = mid // n, mid % n
            if matrix[row][col] == target:
                return True
            if matrix[row][col] < target:
                start = mid + 1
            else:
                end = mid - 1
        return False


if __name__ == "__main__":
    test_matrix = [[1, 2, 4, 8], [10, 11, 12, 13], [14, 20, 30, 40]]
    test_target = 10
    print(Solution().searchMatrix(test_matrix, test_target))
