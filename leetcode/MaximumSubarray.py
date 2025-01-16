class Solution(object):
    def maxSubArray(self, nums):
        max_sum = 0
        cur_max = 0
        start = True
        for num in nums:
            if start:
                max_sum = num
                cur_max = num
                start = False
            else:
                cur_max = max(num, cur_max + num)
                max_sum = max(max_sum, cur_max)
        return max_sum

if __name__ == '__main__':
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print(Solution().maxSubArray(nums))  # 6