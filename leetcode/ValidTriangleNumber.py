from typing import List

class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        count = 0
        def backtrack(index: int, path: List[int]):
            nonlocal count
            if len(path) == 3:
                count += 1
                print(path)
                return
            for i in range(index, n):
                if len(path) == 2 and nums[i] >= path[0] + path[1]:
                    break
                path.append(nums[i])
                backtrack(i + 1, path)
                path.pop()
        backtrack(0, [])
        return count                    

if __name__ == "__main__":
    nums = [2, 2, 3, 4]
    print(Solution().triangleNumber(nums))