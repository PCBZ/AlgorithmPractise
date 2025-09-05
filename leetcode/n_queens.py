"""
LeetCode 51: N-Queens
https://leetcode.com/problems/n-queens/

Solve the classic N-Queens puzzle using backtracking.
"""

from typing import List


class Solution:
    """Solution for N-Queens problem using backtracking."""

    def solveNQueens(self, n: int) -> List[List[str]]:  # pylint: disable=invalid-name
        """Find all solutions to place n queens on n×n board without attacking each other."""
        board = [['.' for _ in range(n)] for _ in range(n)]
        cols = set()
        diagonal1 = set()  # row - col
        diagonal2 = set()  # row + col
        results = []

        def backtrack(row: int):
            """Recursively place queens using backtracking."""
            if row == n:
                # Convert board to required string format
                board_solution = [''.join(board_row) for board_row in board]
                results.append(board_solution)
                return

            for col in range(n):
                # Check if current position conflicts with existing queens
                if (col in cols or
                    row - col in diagonal1 or
                    row + col in diagonal2):
                    continue

                # Place queen
                board[row][col] = 'Q'
                cols.add(col)
                diagonal1.add(row - col)
                diagonal2.add(row + col)

                # Recurse to next row
                backtrack(row + 1)

                # Backtrack - remove queen
                board[row][col] = '.'
                cols.remove(col)
                diagonal1.remove(row - col)
                diagonal2.remove(row + col)

        backtrack(0)
        return results


if __name__ == "__main__":
    solver = Solution()
    print(f"N-Queens solutions for n=4: {len(solver.solveNQueens(4))}")
