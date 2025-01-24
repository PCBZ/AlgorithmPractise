from typing import List

class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        left, right = 0, n - 1
        while left <= right:
            mid = (left + right) // 2
            kas = nums[mid]
            if mid % 2 == 1:
                mid -= 1
            if nums[mid] == nums[mid-1]:
                right = mid
            elif nums[mid] == nums[mid+1]:
                left = mid
            else:
                return nums[mid]

if __name__ == "__main__":
    nums = [3, 3, 7, 7, 10, 11, 11]
    print(Solution().singleNonDuplicate(nums))