from typing import List 

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        res = [n * [0] for _ in range(n)]
        top  = left = 0
        bottom = right = n - 1
        i = 1
        while i <= n * n:
            for j in range(left, right + 1):
                res[top][j] = i
                i += 1
            top += 1
            for j in range(top, bottom + 1):
                res[j][right] = i
                i += 1
            right -= 1
            for j in range(right, left - 1, -1):
                res[bottom][j] = i
                i += 1
            bottom -= 1
            for j in range(bottom, top - 1, -1):
                res[j][left] = i
                i += 1
            left += 1
        

        return res


if __name__ == "__main__":
    n = 3
    for t in Solution().generateMatrix(n):
        print(t)
