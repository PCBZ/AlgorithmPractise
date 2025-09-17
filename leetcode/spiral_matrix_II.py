"""
LeetCode Spiral Matrix Problems - Complete Collection

This module contains solutions for all three spiral matrix problems:
- LeetCode 54: Spiral Matrix (I) - Traverse matrix in spiral order
- LeetCode 59: Spiral Matrix II - Generate n×n matrix filled in spiral order
- LeetCode 885: Spiral Matrix III - Walk in spiral form on a grid

URLs:
- https://leetcode.com/problems/spiral-matrix/
- https://leetcode.com/problems/spiral-matrix-ii/
- https://leetcode.com/problems/spiral-matrix-iii/
"""

from typing import List


class Solution:
    """Solution class containing all three spiral matrix algorithms."""

    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        """
        LeetCode 54: Spiral Matrix

        Traverse an m x n matrix in spiral order (clockwise from outside to inside).

        Algorithm:
        1. Define boundaries: top, bottom, left, right
        2. Traverse in 4 directions: right, down, left, up
        3. Shrink boundaries after each direction
        4. Stop when boundaries cross

        Time: O(m*n), Space: O(1) excluding result array

        Args:
            matrix: m x n matrix of integers

        Returns:
            List of elements in spiral order
        """
        if not matrix or not matrix[0]:
            return []

        top, bottom = 0, len(matrix) - 1
        left, right = 0, len(matrix[0]) - 1
        result = []

        while left <= right and top <= bottom:
            # Traverse right along top row
            for col in range(left, right + 1):
                result.append(matrix[top][col])
            top += 1

            # Traverse down along right column
            for row in range(top, bottom + 1):
                result.append(matrix[row][right])
            right -= 1

            # Traverse left along bottom row (if still valid)
            if top <= bottom:
                for col in range(right, left - 1, -1):
                    result.append(matrix[bottom][col])
                bottom -= 1

            # Traverse up along left column (if still valid)
            if left <= right:
                for row in range(bottom, top - 1, -1):
                    result.append(matrix[row][left])
                left += 1

        return result

    def generateMatrix(self, n: int) -> List[List[int]]:
        """
        LeetCode 59: Spiral Matrix II

        Generate an n×n matrix filled with elements 1 to n² in spiral order.

        Algorithm:
        1. Create n×n matrix filled with zeros
        2. Use same boundary approach as Spiral Matrix I
        3. Fill numbers 1 to n² in spiral pattern
        4. Move boundaries inward after each direction

        Time: O(n²), Space: O(n²) for the result matrix

        Args:
            n: Size of the square matrix

        Returns:
            n×n matrix filled in spiral order
        """
        # Initialize n×n matrix with zeros
        matrix = [[0] * n for _ in range(n)]

        # Define boundaries
        top = left = 0
        bottom = right = n - 1
        num = 1

        while num <= n * n:
            # Fill right along top row
            for col in range(left, right + 1):
                matrix[top][col] = num
                num += 1
            top += 1

            # Fill down along right column
            for row in range(top, bottom + 1):
                matrix[row][right] = num
                num += 1
            right -= 1

            # Fill left along bottom row
            for col in range(right, left - 1, -1):
                matrix[bottom][col] = num
                num += 1
            bottom -= 1

            # Fill up along left column
            for row in range(bottom, top - 1, -1):
                matrix[row][left] = num
                num += 1
            left += 1

        return matrix

    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        """
        LeetCode 885: Spiral Matrix III

        Walk in a spiral shape on a grid, starting from (rStart, cStart).
        Return coordinates of all cells visited in order.

        Algorithm:
        1. Start at given position, move in spiral pattern
        2. Directions: East, South, West, North (clockwise)
        3. Step count increases: 1,1,2,2,3,3,4,4,... (every 2 direction changes)
        4. Record only coordinates that are within grid bounds

        Time: O(max(rows, cols)²), Space: O(rows*cols) for result

        Args:
            rows: Number of rows in the grid
            cols: Number of columns in the grid
            rStart: Starting row position
            cStart: Starting column position

        Returns:
            List of [row, col] coordinates in visit order
        """
        # Direction vectors: East, South, West, North
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        result = []
        total_cells = rows * cols

        # Start at given position
        row, col = rStart, cStart
        result.append([row, col])

        if total_cells == 1:
            return result

        steps = 1  # Number of steps in current direction
        direction_idx = 0  # Current direction index

        while len(result) < total_cells:
            # Move in current direction for 'steps' times
            for _ in range(2):  # Each step count is used for 2 directions
                dr, dc = directions[direction_idx]

                for _ in range(steps):
                    row += dr
                    col += dc

                    # Add to result if within bounds
                    if 0 <= row < rows and 0 <= col < cols:
                        result.append([row, col])

                        # Early termination if all cells visited
                        if len(result) == total_cells:
                            return result

                # Change direction (clockwise)
                direction_idx = (direction_idx + 1) % 4

            # Increase step count after every 2 direction changes
            steps += 1

        return result


# Helper functions for testing and examples
def print_matrix(matrix: List[List[int]], title: str = "Matrix"):
    """Print matrix in a formatted way."""
    print(f"\n{title}:")
    if not matrix:
        print("[]")
        return

    # Calculate column width for alignment
    max_width = max(len(str(matrix[i][j]))
                   for i in range(len(matrix))
                   for j in range(len(matrix[0])))

    for row in matrix:
        formatted_row = [str(cell).rjust(max_width) for cell in row]
        print(f"[{', '.join(formatted_row)}]")


def print_coordinates(coords: List[List[int]], title: str = "Coordinates"):
    """Print list of coordinates in a formatted way."""
    print(f"\n{title}:")
    coord_strs = [f"[{coord[0]},{coord[1]}]" for coord in coords]

    # Print in rows of 8 for readability
    for i in range(0, len(coord_strs), 8):
        print(" ".join(coord_strs[i:i+8]))


if __name__ == "__main__":
    solution = Solution()

    print("🌀 LeetCode Spiral Matrix Problems - Complete Collection")
    print("=" * 65)

    # ===== SPIRAL MATRIX I (LeetCode 54) =====
    print("\n📝 Problem 1: Spiral Matrix (LeetCode 54)")
    print("Traverse matrix in spiral order")
    print("-" * 40)

    # Example 1: 3x4 matrix
    matrix1 = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
    print_matrix(matrix1, "Input Matrix")
    result1 = solution.spiralOrder(matrix1)
    print(f"Spiral Order: {result1}")

    # Example 2: 3x3 matrix
    matrix2 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print_matrix(matrix2, "Input Matrix")
    result2 = solution.spiralOrder(matrix2)
    print(f"Spiral Order: {result2}")

    # ===== SPIRAL MATRIX II (LeetCode 59) =====
    print("\n\n📝 Problem 2: Spiral Matrix II (LeetCode 59)")
    print("Generate n×n matrix filled in spiral order")
    print("-" * 45)

    # Example 1: n=3
    n1 = 3
    result3 = solution.generateMatrix(n1)
    print_matrix(result3, f"Generated {n1}×{n1} Spiral Matrix")

    # Example 2: n=4
    n2 = 4
    result4 = solution.generateMatrix(n2)
    print_matrix(result4, f"Generated {n2}×{n2} Spiral Matrix")

    # Example 3: n=1
    n3 = 1
    result5 = solution.generateMatrix(n3)
    print_matrix(result5, f"Generated {n3}×{n3} Spiral Matrix")

    # ===== SPIRAL MATRIX III (LeetCode 885) =====
    print("\n\n📝 Problem 3: Spiral Matrix III (LeetCode 885)")
    print("Walk in spiral form starting from given position")
    print("-" * 50)

    # Example 1: 1x4 grid
    rows1, cols1, rStart1, cStart1 = 1, 4, 0, 0
    result6 = solution.spiralMatrixIII(rows1, cols1, rStart1, cStart1)
    print(f"Grid: {rows1}×{cols1}, Start: ({rStart1},{cStart1})")
    print_coordinates(result6, "Visit Order")

    # Example 2: 5x6 grid
    rows2, cols2, rStart2, cStart2 = 5, 6, 1, 4
    result7 = solution.spiralMatrixIII(rows2, cols2, rStart2, cStart2)
    print(f"\nGrid: {rows2}×{cols2}, Start: ({rStart2},{cStart2})")
    print_coordinates(result7, "Visit Order")

    # Example 3: 3x3 grid from center
    rows3, cols3, rStart3, cStart3 = 3, 3, 1, 1
    result8 = solution.spiralMatrixIII(rows3, cols3, rStart3, cStart3)
    print(f"\nGrid: {rows3}×{cols3}, Start: ({rStart3},{cStart3})")
    print_coordinates(result8, "Visit Order")

    print("\n" + "=" * 65)
    print("✅ All spiral matrix problems demonstrated successfully!")
    print("🔄 Time Complexities:")
    print("   • Spiral Matrix I: O(m×n)")
    print("   • Spiral Matrix II: O(n²)")
    print("   • Spiral Matrix III: O(max(rows,cols)²)")
    print("💾 Space Complexities:")
    print("   • Spiral Matrix I: O(1) excluding result")
    print("   • Spiral Matrix II: O(n²) for result matrix")
    print("   • Spiral Matrix III: O(rows×cols) for result")
