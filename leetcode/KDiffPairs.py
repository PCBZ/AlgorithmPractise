from typing import List

class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        nums.sort()
        j = 0
        count = 0
        n = len(nums)
        for i in range(n):
            while j < i and nums[i] - nums[j] > k:
                j += 1
            if i != j and nums[i] - nums[j] == k:
                count += 1
        return count

if __name__ == "__main__":
    nums = [3,1,4,1,5]
    k = 0
    print(Solution().findPairs(nums, k))