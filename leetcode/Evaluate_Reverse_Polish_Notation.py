"""
LeetCode Problem #150: Evaluate Reverse Polish Notation

URL: https://leetcode.com/problems/evaluate-reverse-polish-notation/

Evaluate arithmetic expressions in Reverse Polish Notation using a stack.
Example: ["2","1","+","3","*"] -> ((2 + 1) * 3) = 9
"""
from typing import List


class Solution:
    """Solution for evaluating Reverse Polish Notation using stack."""

    def evalRPN(self, token_list: List[str]) -> int:
        """
        Evaluate arithmetic expression in Reverse Polish Notation.

        Uses a stack to process operands and operators. When an operator
        is encountered, pop two operands, apply operation, and push result.

        Args:
            token_list: List of tokens (numbers and operators)

        Returns:
            Integer result of the arithmetic expression
        """
        def is_integer(s: str) -> bool:
            """Check if string represents an integer (including negative)."""
            try:
                int(s)
                return True
            except ValueError:
                return False

        stack = []
        for token in token_list:
            if is_integer(token):
                stack.append(int(token))
            else:
                # Pop two operands (order matters for subtraction/division)
                val2, val1 = stack.pop(), stack.pop()

                if token == "+":
                    result = val1 + val2
                elif token == "-":
                    result = val1 - val2
                elif token == "*":
                    result = val1 * val2
                else:  # token == "/"
                    # Truncate toward zero for division
                    result = int(val1 / val2)

                stack.append(result)

        return stack[-1]


if __name__ == "__main__":
    test_tokens = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
    print(Solution().evalRPN(test_tokens))
