from typing import List

class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        stack = []
        res = [-1] * n

        for i in range(2*n):
            if i < n and (not stack or nums[i % n] <= nums[stack[-1]]):
                stack.append(i)
            else:
                while stack and nums[i % n] > nums[stack[-1]]:
                    res[stack.pop()] = nums[i % n]
                if i < n:
                    stack.append(i)
        return res
    
if __name__ == "__main__":
    nums = [1, 2, 3, 4, 3]
    print(Solution().nextGreaterElements(nums))