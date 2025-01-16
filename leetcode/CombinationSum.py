from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        self.traceBack(0, candidates, [], target, res)
        return res


    def traceBack(self, start: int, candidates: List[int], combines: List[int], remain: int, res: List[int]):
        if remain == 0:
            res.append(combines.copy())
        if remain < 0:
            return
        for i in range(start, len(candidates)):
            combines.append(candidates[i])
            self.traceBack(i, candidates, combines, remain - candidates[i], res)
            combines.pop()

if __name__ == '__main__':
    s = Solution()
    print(s.combinationSum([2,3,6,7], 7))