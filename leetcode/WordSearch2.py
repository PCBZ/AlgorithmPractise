from typing import List, Tuple

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        def dfs(word: str, pos: Tuple[int, int], start: int, path: List[Tuple[int, int]]) -> bool:
            row, col = pos[0], pos[1]
            if row < 0 or row >= m or col < 0 or col >= n or pos in path or board[row][col] != word[start]:
                return False
            if start == len(word) - 1 and word[start] == board[row][col]:
                return True
            if word[start] == board[row][col]:
                path.append((row, col))
                return any(
                    dfs(word, (row + dr, col + dc), start + 1, path)
                    for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]
                )
        m, n = len(board), len(board[0])
        res = []
        for word in words:
            found = False
            for i in range(m):
                for j in range(n):
                    if dfs(word, (i, j), 0, []):
                        res.append(word)
                        found = True
                        break
                if found:
                    break
        return res

if __name__ == "__main__":
    board = [["a","b","c"],["a","e","d"],["a","f","g"]]
    words = ["eaafgdcba","eaabcdgfa"]
    print(Solution().findWords(board, words))