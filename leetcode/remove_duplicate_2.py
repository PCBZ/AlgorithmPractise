from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 1
        maj = nums[0]
        for i in range(1, len(nums)):
            if nums[i] != maj:
                if count == 0:
                    maj = nums[i]
                    count = 1
                else:
                    count -= 1
            else:
                if count == 0:
                    maj = nums[i]
                count += 1
        return maj
    
if __name__ == "__main__":
    test_nums = [8,8,7,7,7]
    print(Solution().majorityElement(test_nums))