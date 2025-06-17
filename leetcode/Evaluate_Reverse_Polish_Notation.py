from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        def is_integer(s: str) -> bool:
            try:
                int(s)
                return True
            except ValueError:
                return False
        stack = []
        for token in tokens:
            if is_integer(token):
                stack.append(int(token))
            else:
                val2, val1 = stack.pop(), stack.pop()
                val = 0
                if token == "+":
                    val = val1 + val2
                elif token == "-":
                    val = val1 - val2
                elif token == "*":
                    val = val1 * val2
                else:
                    val = int(val1 / val2)
                stack.append(val)
        return stack[-1]

if __name__ == "__main__":
    tokens=["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
    print(Solution().evalRPN(tokens))
