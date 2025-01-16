from typing import List

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        def traceBack(start: int, subset: List[int]):
            res.append(subset[:])
            for i in range(start, n):
                if i > start and nums[i] == nums[i-1]:
                    continue
                subset.append(nums[i])
                traceBack(i+1, subset)
                subset.pop()
        nums.sort()
        res = []
        traceBack(0, [])
        return res
    
if __name__ == "__main__":
    nums = [1, 2, 2]
    print(Solution().subsetsWithDup(nums))  # [[], [1], [1, 2], [1, 2, 2], [2], [2, 2]]