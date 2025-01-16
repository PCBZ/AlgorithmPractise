from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0
        prev = 0
        count = 0
        for idx in range(1, n):
            if nums[prev] != nums[idx]:
                prev += 1
                nums[prev] = nums[idx]
            else:
                count += 1
        return count
            
if __name__ == '__main__':
    # begin
    s = Solution()
    nums = [1,1,2]
    print(s.removeDuplicates(nums))
    print(nums)