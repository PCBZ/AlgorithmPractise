"""
LeetCode 54: Spiral Matrix
https://leetcode.com/problems/spiral-matrix/
Return all elements of matrix in spiral order.
"""

from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        """Return all elements of matrix in spiral order."""
        # Set boundaries
        top, bottom = 0, len(matrix) - 1
        left, right = 0, len(matrix[0]) - 1
        res = []

        # Spiral traversal
        while left <= right and top <= bottom:
            # Right
            for i in range(left, right + 1):
                res.append(matrix[top][i])
            top += 1

            # Down
            for i in range(top, bottom + 1):
                res.append(matrix[i][right])
            right -= 1

            # Left
            if top <= bottom:
                for i in range(right, left - 1, -1):
                    res.append(matrix[bottom][i])
                bottom -= 1

            # Up
            if left <= right:
                for i in range(bottom, top - 1, -1):
                    res.append(matrix[i][left])
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


def print_spiral_path(matrix: List[List[int]], spiral_result: List[int]) -> None:
    """Show spiral traversal path with step numbers."""
    if not matrix or not spiral_result:
        return

    m, n = len(matrix), len(matrix[0])

    # Map values to step order
    value_to_step = {}
    for step, value in enumerate(spiral_result, 1):
        if value not in value_to_step:
            value_to_step[value] = step

    print(f"\nSpiral traversal path:")
    print(f"Total elements: {len(spiral_result)}")
    print(f"Order: {' → '.join(map(str, spiral_result))}")

    # Create step matrix
    step_matrix = [[0] * n for _ in range(m)]
    for i in range(m):
        for j in range(n):
            original_value = matrix[i][j]
            step_matrix[i][j] = value_to_step.get(original_value, 0)

    print(f"\nStep order matrix:")
    max_step_width = len(str(max(value_to_step.values()) if value_to_step else 1))
    for row in step_matrix:
        formatted_row = [str(val).rjust(max_step_width) for val in row]
        print("[" + ", ".join(formatted_row) + "]")


def demonstrate_spiral_order(matrix: List[List[int]]) -> None:
    """Demonstrate spiral order traversal."""
    m, n = len(matrix), len(matrix[0]) if matrix else 0
    print(f"\n=== Spiral Order: {m}×{n} Matrix ===")

    solution = Solution()
    result = solution.spiralOrder(matrix)

    print_matrix(matrix, f"Original {m}×{n} Matrix")
    print_spiral_path(matrix, result)

    print(f"\nResult: {result}")


if __name__ == '__main__':
    """Test spiral matrix traversal."""
    print("🌟 LeetCode 54: Spiral Matrix - Solution Demo 🌟")
    print("=" * 55)

    solution = Solution()

    # Test cases
    test_cases = [
        [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
        [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]],
        [[1, 2, 3, 4, 5]],
        [[1], [2], [3], [4]],
        [[42]],
        [[1, 2], [3, 4]],
        [[1, 2, 3], [4, 5, 6]],
        [
            [1,  2,  3,  4,  5],
            [6,  7,  8,  9,  10],
            [11, 12, 13, 14, 15],
            [16, 17, 18, 19, 20]
        ]
    ]

    for i, matrix in enumerate(test_cases, 1):
        demonstrate_spiral_order(matrix)
        if i < len(test_cases):
            print("-" * 45)

    # Performance test
    print(f"\n🚀 Performance Test:")
    import time

    # Create larger matrix
    large_matrix = []
    counter = 1
    for i in range(10):
        row = []
        for j in range(15):
            row.append(counter)
            counter += 1
        large_matrix.append(row)

    print(f"Testing 10×15 matrix ({len(large_matrix)*len(large_matrix[0])} elements)...")

    start_time = time.time()
    large_result = solution.spiralOrder(large_matrix)
    end_time = time.time()

    print(f"✅ Completed spiral traversal in {(end_time - start_time)*1000:.2f}ms")
    print(f"Result length: {len(large_result)}")
    print(f"First 10 elements: {large_result[:10]}")
    print(f"Last 10 elements: {large_result[-10:]}")

    # Verify correctness
    all_matrix_values = [val for row in large_matrix for val in row]
    all_matrix_values.sort()
    large_result_sorted = sorted(large_result)

    if all_matrix_values == large_result_sorted:
        print("✅ All matrix elements present in result")
    else:
        print("❌ Matrix traversal validation failed")

    print("\n" + "=" * 55)
    print("Algorithm Analysis:")
    print("• Time Complexity: O(m × n)")
    print("• Space Complexity: O(1)")
    print("• Pattern: Right → Down → Left → Up")
