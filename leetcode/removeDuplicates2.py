from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        end = 0
        count = 0
        for i in range(len(nums)): 
            if i == 0:
                count = 1
                end = 1
            else:
                if nums[i] == nums[i-1]:
                    count += 1
                else:
                    count = 1
                if count <= 2:
                    nums[end] = nums[i]
                    end += 1
        return end
            
if __name__ == '__main__':
    s = Solution()
    nums = [0,0,1,1,1,1,2,3,3]
    print(nums[0:s.removeDuplicates(nums)])