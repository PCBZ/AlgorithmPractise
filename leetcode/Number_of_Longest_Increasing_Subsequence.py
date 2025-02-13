from typing import List

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1] * n
        for i in range(n):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)

    def findNumberOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1] * n
        count = [1] * n

        for i in range(n):
            for j in range(i):
                if nums[i] > nums[j]:
                    if dp[j] + 1 > dp[i]:
                        dp[i] = dp[j] + 1
                        count[i] = count[j]
                    elif dp[j] + 1 == dp[i]:
                        count[i] += count[j]
        max_len = max(dp)
        return sum(count[i] for i in range(n) if dp[i] == max_len)
    
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        start = 0
        n = len(nums)
        total_max = 1
        for end in range(1, n):
            if nums[end] > nums[start]:
                cur_max = end - start + 1
                total_max = max(cur_max, total_max)
            else:
                start = end
                cur_max = 1
        return total_max


if __name__ == "__main__":
    s = Solution()
    nums = [1,3,5,4,7]
    print(s.lengthOfLIS(nums))
    print(s.findNumberOfLIS(nums))
    print(s.findLengthOfLCIS(nums))

    