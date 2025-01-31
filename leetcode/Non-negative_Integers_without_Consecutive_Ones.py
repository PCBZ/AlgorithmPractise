class Solution:
     def findIntegers(self, n: int) -> int:

        consecutives = [False] * (n + 1)
        count = 1
        for i in range(1, n + 1):
            if i & 1 == 1:
                has_consecutive = (i >> 1 & 1) or consecutives[i >> 1]
            else:
                has_consecutive = consecutives[i >> 1]
            if not has_consecutive:
                count += 1
            consecutives[i] = has_consecutive
        return count
            
if __name__ == "__main__":
    n = 5
    print(Solution().findIntegers(n))