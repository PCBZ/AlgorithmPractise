from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        def search2D(matrix: List[List[int]], start: int, end: int, target: int) -> bool:
            mid = (start + end) // 2
            x = mid // n
            y = mid % m
            if start > end:
                return False
            if target == matrix[x][y]:
                return True
            if target < matrix[x][y]:
                return search2D(matrix, start, mid - 1, target)
            else:
                return search2D(matrix, mid + 1, end, target)
        return search2D(matrix, 0, m*n-1, target)
    
if __name__ == "__main__":
    matrix = [[1, 1]]
    print(Solution().searchMatrix(matrix, 2))