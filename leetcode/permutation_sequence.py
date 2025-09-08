"""
LeetCode 60. Permutation Sequence
Given n and k, return the kth permutation sequence.

URL: https://leetcode.com/problems/permutation-sequence/
"""

from typing import List


class Solution:
    """Solution for Permutation Sequence using backtracking."""

    def getPermutation(self, n: int, k: int) -> str:
        """Find the kth permutation sequence using backtracking."""
        count = 0

        def traceBack(seq: List[str]) -> List[str]:
            """Recursive backtracking to generate permutations."""
            nonlocal count
            if len(seq) == n:
                count += 1
            for i in range(n):
                if str(i+1) not in seq:
                    seq.append(str(i+1))
                    traceBack(seq)
                    if count == k:
                        return seq
                    seq.pop()
            return None

        seq = traceBack([])
        return ''.join(seq) if seq else ""


def main():
    """Example usage."""
    solution = Solution()

    # Example 1: n=3, k=3
    n1, k1 = 3, 3
    result1 = solution.getPermutation(n1, k1)
    print(f"Input: n = {n1}, k = {k1}")
    print(f"Output: {result1}")
    print("Explanation: The permutations are: 123, 132, 213, 231, 312, 321. The 3rd permutation is 213.")
    print()

    # Example 2: n=4, k=9
    n2, k2 = 4, 9
    result2 = solution.getPermutation(n2, k2)
    print(f"Input: n = {n2}, k = {k2}")
    print(f"Output: {result2}")
    print("Explanation: The 9th permutation in lexicographic order for n=4 is 2314.")
    print()

    # Example 3: n=3, k=1
    n3, k3 = 3, 1
    result3 = solution.getPermutation(n3, k3)
    print(f"Input: n = {n3}, k = {k3}")
    print(f"Output: {result3}")
    print("Explanation: The first permutation is always 123.")
    print()
if __name__ == "__main__":
    main()
