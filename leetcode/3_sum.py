from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        res = set()
        for i in range(n - 2):
            left, right = i + 1, n - 1
            while left < right:
                if nums[i] + nums[left] + nums[right] == 0:
                    res.add((nums[i], nums[left], nums[right]))
                    left += 1
                    right -= 1
                elif nums[i] + nums[left] + nums[right] < 0:
                    left += 1
                else:
                    right -= 1
        return list(map(list, res))

if __name__ == "__main__":
    nums = [0, 0, 0]
    print(Solution().threeSum(nums))