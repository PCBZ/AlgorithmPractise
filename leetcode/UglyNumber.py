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
    
    def nthUglyNumber(self, n: int) -> int:
        res = [1]
        i1 = i2 = i3 = 0
        for _ in range(1, n):
            u1, u2, u3 = res[i1] * 2, res[i2] * 3, res[i3] * 5
            next_u = min(u1, u2, u3)
            res.append(next_u)
            if next_u == u1:
                i1 += 1
            if next_u == u2:
                i2 += 1
            if next_u == u3:
                i3 += 1
        return res[-1]
    
if __name__ == "__main__":
    # print(Solution().isUgly(14))
    print(Solution().nthUglyNumber(10))