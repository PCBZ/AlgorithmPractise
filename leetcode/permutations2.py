from typing import List

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []
        def traceBack(path, used):
            if len(path) == n:
                res.append(path[:])
                return
            for i in range(n):
                if used[i]:
                    continue
                if i > 0 and nums[i] == nums[i-1] and not used[i-1]:
                    continue  
                path.append(nums[i])       
                used[i] = True
                traceBack(path, used)
                path.pop()
                used[i] = False
        nums.sort()
        traceBack([], [False] * n)
        return res

if __name__ == '__main__':
    nums = [1, 1, 2]
    print(Solution().permuteUnique(nums))  # [[1, 1, 2], [1, 2, 1], [2, 1, 1]]