from math import gcd, lcm
from functools import reduce

class Solution:
    def fractionAddition(self, expression: str) -> str:
        top, bottom = [], []
        signal = 1
        cur = ''
        for idx, char in enumerate(expression):
            if char == '-' or char == '+':
                if cur:
                    bottom.append(int(cur))
                    cur = ""
                signal = -1 if char == "-" else 1
            elif char == '/':
                top.append(int(cur) * signal)
                cur = ''
            else:
                cur += char
            if idx == len(expression) - 1:
                bottom.append(int(cur))
        print(top, bottom)
        total_lcm = reduce(lcm, bottom)
        top = list(map(lambda x: x[1] * total_lcm // bottom[x[0]] , enumerate(top)))
        top_value = sum(top)
        res_gcd = gcd(top_value, total_lcm)
        return str(top_value // res_gcd) + '/' + str(total_lcm // res_gcd)

if __name__ == "__main__":
    expression = "1/3-1/2"
    print(Solution().fractionAddition(expression))