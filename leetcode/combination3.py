from typing import List

class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        def traceBack(start: int, path: List[int]):
            if len(path) == k:
                if sum(path) == n:
                    res.append(path[:])
                return
            for i in range(start + 1, 10):
                path.append(i)
                traceBack(i, path)
                path.pop()
        res = []
        traceBack(0, [])
        return res


if __name__ == "__main__":
    k, n = 3, 9
    print(Solution().combinationSum3(k, n))       