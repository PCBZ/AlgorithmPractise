from math import ceil

class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        m, n = len(a), len(b)
        t = ceil(n / m)
        repeated_a = a * t
        if b in repeated_a:
            return t
        repeated_a += a
        if b in repeated_a:
            return t + 1
        return -1
    
if __name__ == "__main__":
    a = "a"
    b = "aa"
    print(Solution().repeatedStringMatch(a, b))
