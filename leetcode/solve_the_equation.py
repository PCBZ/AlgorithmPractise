
"""
LeetCode 640: Solve the Equation

Given a string equation representing a linear equation of the form 'ax+b=cx+d',
return the value of x in the form 'x=#'. If there is no solution, return 'No solution'.
If there are infinite solutions, return 'Infinite solutions'.

URL: https://leetcode.com/problems/solve-the-equation/
"""

class Solution:
    def solveEquation(self, equation: str) -> str:
        """
        Parse and solve a linear equation in one variable.
        Time: O(n), Space: O(1)
        """
        acc = ""  # Accumulate digits for current number
        signal = 1  # Current sign (+1 or -1)
        left_factor = right_factor = 0  # Coefficients for x and constants
        reverse = 1  # 1 for left side, -1 for right side
        for idx, char in enumerate(equation):
            if char == '=':
                if acc:
                    right_factor += -1 * reverse * signal * int(acc)
                    acc = ""
                    signal = 1
                reverse = -1  # Switch to right side
            elif char == 'x':
                left_factor += reverse * signal * (1 if not acc else int(acc))
                signal = 1
                acc = ""
            elif char == '+' or char == '-':
                if idx > 0 and equation[idx - 1] != 'x' and equation[idx - 1] != '=' and acc:
                    right_factor += -1 * reverse * signal * int(acc)
                    acc = ""
                signal = 1 if char == '+' else -1
            elif idx == len(equation) - 1:
                acc += char
                right_factor += -1 * reverse * signal * int(acc)
            if char.isdigit():
                acc += char

        if left_factor == 0 and right_factor == 0:
            return 'Infinite solutions'
        if left_factor == 0:
            return 'No solution'
        return f'x={right_factor // left_factor}'


if __name__ == "__main__":
    solution = Solution()
    test_equations = [
        "x+5-3+x=6+x-2",
        "x=x",
        "2x=x",
        "2x+3x-6x=x+2",
        "x=x+2",
        "1+1=x",
        "x+2=2+x"
    ]
    for eq in test_equations:
        print(f"Equation: {eq} -> {solution.solveEquation(eq)}")