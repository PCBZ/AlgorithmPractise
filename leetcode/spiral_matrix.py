"""
LeetCode Spiral Matrix Problems

LeetCode 59: Spiral Matrix II
https://leetcode.com/problems/spiral-matrix-ii/
Generate n×n matrix filled with 1 to n² in spiral order.

LeetCode 885: Spiral Matrix III  
https://leetcode.com/problems/spiral-matrix-iii/
Walk in spiral form starting from (rStart, cStart) and return coordinates in visiting order.
"""

from typing import List


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        """Generate n×n matrix filled 1 to n² in spiral order."""
        # Initialize matrix and boundaries
        res = [n * [0] for _ in range(n)]
        top  = left = 0
        bottom = right = n - 1
        i = 1

        # Fill matrix in spiral order
        while i <= n * n:
            # Right
            for j in range(left, right + 1):
                res[top][j] = i
                i += 1
            top += 1

            # Down
            for j in range(top, bottom + 1):
                res[j][right] = i
                i += 1
            right -= 1

            # Left
            for j in range(right, left - 1, -1):
                res[bottom][j] = i
                i += 1
            bottom -= 1

            # Up
            for j in range(bottom, top - 1, -1):
                res[j][left] = i
                i += 1
            left += 1


        return res

    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        """Walk in spiral form and return coordinates in visiting order."""
        res = []
        step = 1
        total_number = rows * cols
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Right, Down, Left, Up
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


def print_matrix(matrix: List[List[int]], title: str = "Matrix") -> None:
    """Print matrix in formatted way."""
    print(f"\n{title}:")
    if not matrix:
        print("[]")
        return

    max_width = max(len(str(val)) for row in matrix for val in row)

    for row in matrix:
        formatted_row = [str(val).rjust(max_width) for val in row]
        print("[" + ", ".join(formatted_row) + "]")


def print_coordinates(coords: List[List[int]], title: str = "Coordinates") -> None:
    """Print coordinates in formatted way."""
    print(f"\n{title}:")
    if not coords:
        print("[]")
        return
    
    formatted_coords = [f"({coord[0]},{coord[1]})" for coord in coords]
    # Print in rows of 10 for better readability
    for i in range(0, len(formatted_coords), 10):
        print(" ".join(formatted_coords[i:i+10]))


def demonstrate_spiral_pattern(n: int) -> None:
    """Demonstrate spiral pattern generation."""
    print(f"\n=== Generating {n}×{n} Spiral Matrix ===")
    print(f"Goal: Fill {n*n} cells with numbers 1 to {n*n} in spiral order")
    print("Pattern: Right → Down → Left → Up → Right → ...")

    solution = Solution()
    result = solution.generateMatrix(n)
    print_matrix(result, f"Result {n}×{n} Spiral Matrix")

    if n <= 5:
        print(f"\nSpiral path analysis:")
        print(f"Total elements: {n*n}")
        print(f"Starting from top-left, moving right...")

        # Show spiral path
        path = []
        for i in range(n):
            for j in range(n):
                path.append((result[i][j], i, j))

        path.sort()

        directions = ["→", "↓", "←", "↑"]
        for idx, (val, i, j) in enumerate(path):
            if idx < len(path) - 1:
                next_i, next_j = path[idx + 1][1], path[idx + 1][2]
                if next_j > j:
                    direction = "→"
                elif next_i > i:
                    direction = "↓"
                elif next_j < j:
                    direction = "←"
                else:
                    direction = "↑"
                print(f"  Step {val:2}: position ({i},{j}) {direction}")
            else:
                print(f"  Step {val:2}: position ({i},{j}) ✓")


def demonstrate_spiral_matrix_iii(rows: int, cols: int, rStart: int, cStart: int) -> None:
    """Demonstrate Spiral Matrix III walk pattern."""
    print(f"\n=== Spiral Matrix III: {rows}×{cols} grid, start ({rStart},{cStart}) ===")
    print(f"Goal: Visit all {rows*cols} cells in spiral order starting from ({rStart},{cStart})")
    print("Pattern: Right 1 → Down 1 → Left 2 → Up 2 → Right 3 → Down 3 → ...")
    
    solution = Solution()
    result = solution.spiralMatrixIII(rows, cols, rStart, cStart)
    
    print_coordinates(result, f"Visit order for {rows}×{cols} grid")
    
    # Show first few steps for small grids
    if rows * cols <= 20:
        print(f"\nStep-by-step walk:")
        for i, (r, c) in enumerate(result, 1):
            print(f"  Step {i:2}: visit cell ({r},{c})")


if __name__ == "__main__":
    """Test both spiral matrix problems with various sizes."""
    print("🌟 LeetCode Spiral Matrix Problems - Solution Demo 🌟")
    print("=" * 60)
    
    solution = Solution()
    
    # Demonstrate Spiral Matrix II
    print("\n📋 SPIRAL MATRIX II (Problem 59)")
    print("=" * 40)
    test_cases = [1, 2, 3, 4]
    
    for n in test_cases:
        demonstrate_spiral_pattern(n)
        print("-" * 35)
    
    # Demonstrate Spiral Matrix III  
    print("\n🎯 SPIRAL MATRIX III (Problem 885)")
    print("=" * 40)
    test_cases_iii = [
        (1, 4, 0, 0),
        (5, 6, 1, 4), 
        (3, 3, 1, 1),
        (2, 2, 0, 0)
    ]
    
    for rows, cols, rStart, cStart in test_cases_iii:
        demonstrate_spiral_matrix_iii(rows, cols, rStart, cStart)
        print("-" * 35)

    # Performance test for Spiral Matrix II
    print("\n🚀 Performance Test - Spiral Matrix II:")
    large_n = 10
    print(f"Generating {large_n}×{large_n} matrix ({large_n*large_n} elements)...")

    import time
    start_time = time.time()
    large_result = solution.generateMatrix(large_n)
    end_time = time.time()

    print(f"✅ Generated {large_n}×{large_n} matrix in {(end_time - start_time)*1000:.2f}ms")
    print(f"First row: {large_result[0]}")
    print(f"Last row:  {large_result[-1]}")

    # Verify matrix
    all_values = []
    for row in large_result:
        all_values.extend(row)
    all_values.sort()

    expected = list(range(1, large_n * large_n + 1))
    if all_values == expected:
        print("✅ All values from 1 to n² are present and unique")
    else:
        print("❌ Matrix validation failed")

    # Performance test for Spiral Matrix III
    print(f"\n🚀 Performance Test - Spiral Matrix III:")
    large_rows, large_cols = 50, 50
    start_r, start_c = 25, 25
    print(f"Walking {large_rows}×{large_cols} grid from ({start_r},{start_c})...")
    
    start_time = time.time()
    walk_result = solution.spiralMatrixIII(large_rows, large_cols, start_r, start_c)
    end_time = time.time()
    
    print(f"✅ Completed spiral walk in {(end_time - start_time)*1000:.2f}ms")
    print(f"Total coordinates: {len(walk_result)}")
    print(f"First 5 steps: {walk_result[:5]}")
    print(f"Last 5 steps: {walk_result[-5:]}")

    print("\n" + "=" * 60)
    print("Algorithm Analysis:")
    print("Spiral Matrix II:")
    print("  • Time Complexity: O(n²)")
    print("  • Space Complexity: O(n²)")
    print("  • Pattern: Right → Down → Left → Up")
    print("Spiral Matrix III:")
    print("  • Time Complexity: O(max(rows, cols)²)")
    print("  • Space Complexity: O(rows × cols)")
    print("  • Pattern: Expanding spiral with step increments")
