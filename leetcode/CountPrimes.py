class Solution:
    def countPrimes(self, n: int) -> int:
        count = 0
        primes = [True for _ in range(n)]
        for i in range(n):
            if i == 0 or i == 1:
                continue
            if primes[i]:
                count += 1
                j = 2
                while i * j < n:
                    primes[i * j] = False
                    j += 1
        return count

n = 10
print(Solution().countPrimes(n))