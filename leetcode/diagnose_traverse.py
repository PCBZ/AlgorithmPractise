from typing import List

class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        m, n = len(mat), len(mat[0])
        res = []
        i = j = 0
        direction_up = True

        while i < m and j < n:
            res.append(mat[i][j])
            if direction_up:
                if i == 0 and j < n - 1:
                    j += 1
                    direction_up = not direction_up
                elif j == n - 1:
                    i += 1
                    direction_up = not direction_up
                else:
                    i -= 1
                    j += 1
            else:
                if j == 0 and i < m - 1:
                    i += 1
                    direction_up = not direction_up
                elif i == m - 1:
                    j += 1
                    direction_up = not direction_up
                else:
                    i += 1
                    j -= 1
        return res

if __name__ == "__main__":
    mat = [[6, 9, 7]]
    print(Solution().findDiagonalOrder(mat))