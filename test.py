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


