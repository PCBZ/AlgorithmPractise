from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        def binSearch(nums: List[int], start: int, end: int, target: int) -> bool:
            if start > end:
                return False
            mid = (start + end) // 2
            if nums[mid] == target:
                return True
            if nums[mid] > nums[start]:
                if target > nums[start] and target < nums[mid]:
                    return binSearch(nums, start, mid - 1, target)
                else:
                    return binSearch(nums, mid+1, end, target)
            else:
                if target < nums[end] and target > nums[mid]:
                    return binSearch(nums, mid+1, end, target)
                else:
                    return binSearch(nums, start, mid-1, target)
        return binSearch(nums, 0, len(nums)-1, target)
    
if __name__ == "__main__":
    nums = [1,0,1,1,1]
    print(Solution().search(nums, 0))