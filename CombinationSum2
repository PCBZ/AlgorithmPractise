from typing import List

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        def traceBack(start: int, candidates: List[int], total: int, values: List[int]):
            if total == target:
                res.append(list(values))
                return
            if total > target:
                return
            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i-1]:
                    continue
                values.append(candidates[i])
                traceBack(i+1, candidates, total + candidates[i], values)
                values.pop()
        
        traceBack(0, candidates, 0, [])
        return res

if __name__ == '__main__':
    s = Solution()
    print(s.combinationSum2([10,1,2,7,6,1,5], 8))