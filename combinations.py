from typing import List

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        def traceBack(start: int, combs: List[int]):
            if len(combs) == k:
                res.append(combs[:])
                return
            for i in range(start, n):
                combs.append(i+1)
                traceBack(i + 1, combs)
                combs.pop()
        traceBack(0, [])
        return res




if __name__ == "__main__":
    n, k = 4, 2
    print(Solution().combine(n, k))