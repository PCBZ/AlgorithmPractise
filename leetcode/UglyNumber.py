class Solution:
    def isUgly(self, n: int) -> bool:
        while n > 1:
            if n % 2 == 0:
                n //= 2
            if n % 3 == 0:
                n //= 3
            if n % 5 == 0:
                n //= 5
        return n == 1
    
print(Solution().isUgly(14))