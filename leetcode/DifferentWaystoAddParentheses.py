from typing import List

class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        mem = {}
        def compute(expr: str) -> List[int]:
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
    expr = "2*3-4*5"
    print(Solution().diffWaysToCompute(expr))