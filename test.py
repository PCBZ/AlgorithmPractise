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


print((ord('z') - ord('a')) % 26)

summ = 0
for i in range(1, 11):
    summ += i * (2 ** (i - 1))
print(summ)

print(math.log2(1))

a = [1, 2, 3]
print(a[1:], a[:-1])