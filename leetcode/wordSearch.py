from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        def traceBack(r: int, c: int, idx: int) -> bool:
            if idx == len(word):
                return True
            if r < 0 or r >= m or c < 0 or c >= n or word[idx] != board[r][c]:
                return False
            temp = board[r][c]
            board[r][c] = 'v'
            isFound = traceBack(r-1, c, idx+1) or traceBack(r+1, c, idx+1) or traceBack(r, c-1, idx+1) or traceBack(r, c+1, idx+1)
            board[r][c] = temp
            return isFound
        for i in range(m):
            for j in range(n):
                if traceBack(i, j, 0):
                    return True
        return False


if __name__ == "__main__":
    board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
    word = "ABCCED"
    print(Solution().exist(board, word))

