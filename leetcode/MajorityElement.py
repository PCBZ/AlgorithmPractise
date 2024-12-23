from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        res = None
        count = 0
        for num in nums:
            if count == 0:
                res = num
            count += 1 if res == num else -1
        return res
    
    def majorityElement2(self, nums: List[int]) -> List[int]:
        candidate1 = candidate2 = None
        count1 = count2 = 0
        for num in nums:
            if count1 == 0:
                candidate1, count1 = num, 1
            elif count2 == 0:
                candidate2, count2 = num, 1
            elif candidate1 == num:
                count1 += 1
            elif candidate2 == num:
                count2 += 1
            else:
                count1 -= 1
                count2 -= 1
        return list(filter(lambda count: nums.count(count) > len(nums) / 3, [candidate1, candidate2]))

if __name__ == "__main__":
    nums = [2,2,1,1,1,2,2]
    solution = Solution()
    nums = [1, 1, 3, 2, 2, 2, 3, 3, 1, 2, 1]
    print(solution.majorityElement2(nums))
