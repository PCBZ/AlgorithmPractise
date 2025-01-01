from typing import List

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        def findEqualAndSmallerCount(target: int) -> int:
            i, j = n - 1, 0
            count = 0
            while i >= 0 and j < n:
                if matrix[i][j] <= target:
                    j += 1
                    count += i + 1
                else:
                    i -= 1
            return count
        
        left, right = matrix[0][0], matrix[-1][-1]
        n = len(matrix)
        while left < right:
            mid = (left + right) // 2
            count = findEqualAndSmallerCount(mid)
            if count >= k:
                right = mid - 1
            else:
                left = mid + 1
        return left

if __name__ == "__main__":
    matrix = [[1,2],[1,3]]
    k = 3
    print(Solution().kthSmallest(matrix, k))