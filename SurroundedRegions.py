from typing import List, Tuple

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def isSurrounded(i: int, j: int, path: List[Tuple[int, int]]) -> bool:
            visited[i][j] = True
            if (i == 0 or i == m - 1 or j == 0 or j == n - 1) and board[i][j] == 'O':
                return False
            if board[i][j] == 'X' or (i, j) in path:
                return True
            path.append((i, j))
            return isSurrounded(i-1, j, path) and isSurrounded(i+1, j, path) and isSurrounded(i,j-1, path) and isSurrounded(i, j+1, path)

        m, n = len(board), len(board[0])
        visited = [n * [False] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if visited[i][j]:
                    continue
                if board[i][j] == 'O':
                    path = []
                    if isSurrounded(i, j, path):
                        for (k, t) in path:
                            board[k][t] = 'X'
                    else:
                        for (k, t) in path:
                            board[k][t] = '#'
        print(visited)

board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
Solution().solve(board)
print(board)

        
        