from typing import List

class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
            n = len(nums)
            def backTrack(path: List[int], start: int):
                if len(path) >= 2:
                    res.append(path[:])
                used = set()
                for i in range(start, n):
                    if ( not path or path[-1] <= nums[i] ) and nums[i] not in used:
                        used.add(nums[i])
                        path.append(nums[i])
                        backTrack(path, i+1)
                        path.pop()
            res = []
            backTrack([], 0)
            return res

if __name__ == "__main__":
     nums = [4, 6, 7, 7]
     print(Solution().findSubsequences(nums))