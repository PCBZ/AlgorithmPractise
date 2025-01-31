import math

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        x = num
        next_x = x
        while True:
            next_x = x - ( x * x - num ) / (2 * x)
            if abs(next_x - x) < 0.01:
                break
            x = next_x
        return abs(next_x * next_x - num) < 0.0001

print(Solution().isPerfectSquare(16))

def consective_ones(num: int) -> int:
    prev_digit = 0
    while num > 0:
        cur_digit = num & 1
        if prev_digit == 1 and cur_digit == 1:
            print(num)
            return 0
        num >>= 1
        prev_digit = cur_digit
    return 1

consective_ones(3)

class Solution:
    def findIntegers(self, n: int) -> int:
        def consective_ones(num: int) -> int:
            prev_digit = 0
            while num > 0:
                cur_digit = num & 1
                if prev_digit == 1 and cur_digit == 1:
                    return 0
                num >>= 1
                prev_digit = cur_digit
            return 1

        return reduce(lambda accum, i: accum + consective_ones(i), range(n+1), 0)