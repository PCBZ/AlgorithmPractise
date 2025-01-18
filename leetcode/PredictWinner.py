from typing import List

class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        def helper(cur_nums: List[int], sum1: int, sum2: int, isPlayer1: bool) -> bool:
            if not cur_nums:
                return sum1 >= sum2
            if len(cur_nums) == 1:
                if isPlayer1:
                    return sum1 + cur_nums[0] >= sum2
                else:
                    return sum1 < cur_nums[0] + sum2
            cur_nums1, cur_nums2 = cur_nums[1:], cur_nums[:-1]
            if isPlayer1:
                return not helper(cur_nums1, sum1 + cur_nums[0], sum2, False) or not helper(cur_nums2, sum1 + cur_nums[-1], sum2, False)
            else:
                return not helper(cur_nums1, sum1, sum2 + cur_nums[0], True) or not helper(cur_nums2, sum1, sum2+ cur_nums[-1], True)
        
        return helper(nums, 0, 0, True)
    
if __name__ == "__main__":
    print(Solution().predictTheWinner([1, 1]))
            
                