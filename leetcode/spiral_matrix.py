"""
LeetCode 59: Spiral Matrix II
Generate n×n matrix filled with 1 to n² in spiral order.
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


if __name__ == "__main__":
    """Test spiral matrix generation with various sizes."""
    print("🌟 LeetCode 59: Spiral Matrix II - Solution Demo 🌟")
    print("=" * 55)

    test_cases = [1, 2, 3, 4, 5]
    solution = Solution()

    for n in test_cases:
        demonstrate_spiral_pattern(n)
        print("-" * 40)

    # Performance test
    print("\n🚀 Performance Test:")
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

    print("\n" + "=" * 55)
    print("Algorithm Analysis:")
    print("• Time Complexity: O(n²)")
    print("• Space Complexity: O(n²)")
    print("• Pattern: Right → Down → Left → Up")
