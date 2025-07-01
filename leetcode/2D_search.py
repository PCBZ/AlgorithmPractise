from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        start, end = 0, m * n - 1
        while start <= end:
            mid = (start + end) // 2
            row, col = mid // n, mid % n
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] < target:
                start = mid + 1
            else:
                end = mid - 1
        return False

if __name__ == "__main__":
    matrix=[[1,2,4,8],[10,11,12,13],[14,20,30,40]]
    target=10
    print(Solution().searchMatrix(matrix, target))