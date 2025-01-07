from typing import List

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        i = 0
        while i < len(nums):
            if nums[i] != i + 1:
                idx = nums[i] - 1
                nums[i], nums[idx] = nums[idx], nums[i]
            else:
                i += 1
        print(nums)

if __name__ == "__main__":
    nums = [4,3,2,7,8,2,3,1]
    print(Solution().findDisappearedNumbers(nums))