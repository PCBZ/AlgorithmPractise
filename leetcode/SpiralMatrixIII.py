from typing import List

class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        res = []
        step = 1
        total_number = rows * cols
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        path = 0
        res.append([rStart, cStart])
        step_count = 1
        r, c = rStart, cStart
        cur_direction = directions[0]
        while step_count < total_number:
            dr, dc = cur_direction
            for _ in range(step):
                r += dr
                c += dc
                if 0 <= r < rows and 0 <= c < cols:
                    res.append([r, c])
                    step_count += 1
            path += 1
            if path % 2 == 0:
                step += 1
            cur_direction = directions[path % 4]
        return res

if __name__ == "__main__":
    rows = 1
    cols = 4
    rStart = 0
    cStart = 0
    print(Solution().spiralMatrixIII(rows, cols, rStart, cStart))
    # Output: [[0,0],[0,1],[0,2],[0,3]]