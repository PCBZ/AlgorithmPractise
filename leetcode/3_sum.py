"""
3Sum - Two Pointers Solution
Source: https://leetcode.com/problems/3sum/description/
"""

from typing import List

class Solution:
    """
    Solution class for the 3Sum problem.
    Uses sorting and two pointers technique to find triplets that sum to zero.
    """

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        Find all unique triplets in the array that sum to zero.
        
        Args:
            nums: List of integers
            
        Returns:
            List of unique triplets that sum to zero
        """
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
    test_nums = [0, 0, 0]
    print(Solution().threeSum(test_nums))
