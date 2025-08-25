"""
LeetCode Problem #241: Different Ways to Add Parentheses

URL: https://leetcode.com/problems/different-ways-to-add-parentheses/

Generate all possible results from computing different parenthesizations of expression.
Example: "2*3-4*5" -> [-34, -14, -10, -10, 10]
"""
from typing import List


class Solution:
    """Solution for computing different ways to add parentheses using divide and conquer."""

    def diffWaysToCompute(self, expression: str) -> List[int]:
        """
        Compute all possible results from different parenthesizations.

        Args:
            expression: String containing digits and operators (+, -, *)

        Returns:
            List of all possible computed results
        """
        mem = {}

        def compute(expr: str) -> List[int]:
            """Helper function to recursively compute results with memoization."""
            if expr in mem:
                return mem[expr]
            if expr.isdigit():
                return [int(expr)]
            res = []
            for i, char in enumerate(expr):
                if char in '+-*':
                    left = compute(expr[:i])
                    right = compute(expr[i+1:])
                    for left_expr in left:
                        for right_expr in right:
                            cur_expr = 0
                            if char == "+":
                                cur_expr = left_expr + right_expr
                            elif char == "-":
                                cur_expr = left_expr - right_expr
                            else:
                                cur_expr = left_expr * right_expr
                            res.append(cur_expr)
            mem[expr] = res
            return res

        return compute(expression)


if __name__ == "__main__":
    test_expr = "2*3-4*5"
    print(Solution().diffWaysToCompute(test_expr))
