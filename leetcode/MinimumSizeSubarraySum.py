from typing import List

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        left = 0 
        right = 0
        cur_sum = 0
        min_len = float('inf')
        while right < n:
            cur_sum += nums[right]
            while cur_sum >= target:
                cur_len = right - left + 1
                min_len = min(min_len, cur_len)
                cur_sum -= nums[left]
                left += 1
            right += 1
        return min_len if min_len < float('inf') else 0

if __name__ == "__main__":
    nums = [1,1,1,1,1,1,1]
    print(Solution().minSubArrayLen(11, nums))