from typing import List

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [['.'] * n for _ in range(n)]
        cols = set()
        diagno1 = set()
        diagno2 = set()

        res = []
        def backtrack(row: int):
            if row == n:
                res.append(["".join(row) for row in board])
                return
            for col in range(n):
                if col in cols or row - col in diagno1 or row + col in diagno2:
                    continue
                board[row][col] = 'Q'
                cols.add(col)
                diagno1.add(row - col)
                diagno2.add(row + col)
                backtrack(row + 1)
                board[row][col] = '.'
                cols.remove(col)
                diagno1.remove(row - col)
                diagno2.remove(row + col)
        backtrack(0)
        return res

if __name__ == "__main__":
    print(Solution().solveNQueens(8))