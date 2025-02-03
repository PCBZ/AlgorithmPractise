class Solution:
    def solveEquation(self, equation: str) -> str:
        acc = ""
        signal = 1
        left_factor = right_factor = 0
        reverse = 1
        for idx, char in enumerate(equation):
            if char == '=':
                if acc:
                    right_factor += -1 * reverse * signal * int(acc)
                    acc = ""
                    signal = 1
                reverse = -1
            elif char == 'x':
                left_factor += reverse * signal * (1 if not acc else int(acc))
                print(left_factor)
                signal = 1
                acc = ""
            elif char == "+" or char == "-":
                if idx > 0 and equation[idx - 1] != 'x' and equation[idx - 1] != '=':
                    right_factor += -1 * reverse * signal * int(acc)
                    acc = ""
                signal = 1 if char == "+" else -1
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
    equation = "1+1=x"
    print(Solution().solveEquation(equation))