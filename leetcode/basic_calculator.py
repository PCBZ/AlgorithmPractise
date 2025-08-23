"""
Basic Calculator - LeetCode Problem Solution
Source: https://leetcode.com/problems/basic-calculator/description/

Implements basic calculator functionality for expressions with +, -, (, ).
Also includes a calculator for expressions with +, -, *, /.
"""


class Solution:
    """
    Solution class for Basic Calculator problems.

    Provides two calculator implementations:
    1. calculate: Handles +, -, (, ) with stack-based approach
    2. calculate2: Handles +, -, *, / with operator precedence
    """

    def calculate(self, expression: str) -> int:
        """
        Calculate the result of a basic arithmetic expression.

        Supports: +, -, (, ) operators with integers.

        Args:
            expression: String containing arithmetic expression

        Returns:
            Integer result of the calculation
        """
        stack = []
        sign = 1
        res = 0
        i = 0
        while i < len(expression):
            if expression[i].isdigit():
                start = i
                while i < len(expression) and expression[i].isdigit():
                    i += 1
                num = int(expression[start:i])
                res += sign * num
                i -= 1
            elif expression[i] == '+':
                sign = 1
            elif expression[i] == '-':
                sign = -1
            elif expression[i] == '(':
                stack.append(res)
                stack.append(sign)
                res = 0
                sign = 1
            elif expression[i] == ')':
                prev_sign = stack.pop()
                prev_res = stack.pop()
                res = prev_res + prev_sign * res

            i += 1
        return res

    def calculate2(self, expression: str) -> int:
        """
        Calculate the result of an arithmetic expression with operator precedence.

        Supports: +, -, *, / operators with proper precedence.

        Args:
            expression: String containing arithmetic expression

        Returns:
            Integer result of the calculation
        """
        stack = []
        cur_num = 0
        pre_op = '+'
        for i, char in enumerate(expression):
            if char.isdigit():
                cur_num = cur_num * 10 + int(char)
            if char in '+-*/' or i == len(expression) - 1:
                if pre_op == '+':
                    stack.append(cur_num)
                elif pre_op == '-':
                    stack.append(-cur_num)
                elif pre_op == '*':
                    stack.append(stack.pop() * cur_num)
                elif pre_op == '/':
                    stack.append(int(stack.pop() / cur_num))  # Handle negative division correctly
                pre_op = char
                cur_num = 0
        return sum(stack)


if __name__ == "__main__":
    test_expr1 = " 2-1 + 2 "
    print(Solution().calculate(test_expr1))

    test_expr2 = "3+2*2"
    print(Solution().calculate2(test_expr2))
