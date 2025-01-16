from typing import List

class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        count = 0
        def traceBack(seq: List[str]) -> List[int]:
            nonlocal count
            if len(seq) == n:
                count += 1
            for i in range(n):
                if str(i+1) not in seq:
                    seq.append(str(i+1))
                    traceBack(seq)
                    if count == k:
                        return seq
                    seq.pop()
        seq = traceBack([])
        return ''.join(seq)

n = 3
k = 3

print(Solution().getPermutation(n, k))